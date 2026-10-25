#!/usr/bin/env python3
"""Local, privacy-preserving inventory audit for restricted EWA-DB audio.

Reads an authorized local corpus copy and writes aggregate counts only. It never
emits participant IDs, file names, paths, audio hashes, transcripts or metadata.
Expected layout: ROOT/<group>/<random-participant-code>/<task-folder>/*.wav.
Confirm exact diagnosis/task folder names from your authorized release before use.
"""
from __future__ import annotations
import argparse
import hashlib
import json
import statistics
import sys
import wave
from collections import Counter, defaultdict
from pathlib import Path
from typing import Any


def wav_info(path: Path) -> dict[str, Any] | None:
    try:
        with wave.open(str(path), "rb") as w:
            channels, rate, frames = w.getnchannels(), w.getframerate(), w.getnframes()
            width, compression = w.getsampwidth(), w.getcomptype()
            if channels <= 0 or rate <= 0 or frames < 0:
                return None
            return {"channels": channels, "sample_rate_hz": rate, "frames": frames,
                    "duration_s": frames / rate, "sample_width_bytes": width,
                    "compression_type": compression}
    except (wave.Error, EOFError, OSError, ValueError):
        return None


def sha256_file(path: Path, chunk_size: int = 1024 * 1024) -> str | None:
    digest = hashlib.sha256()
    try:
        with path.open("rb") as f:
            for block in iter(lambda: f.read(chunk_size), b""):
                digest.update(block)
        return digest.hexdigest()
    except OSError:
        return None


def duration_summary(values: list[float]) -> dict[str, float | None]:
    if not values:
        return {"min": None, "median": None, "max": None}
    return {"min": round(min(values), 4),
            "median": round(statistics.median(values), 4),
            "max": round(max(values), 4)}


def audit_group(group_root: Path, expected_task: str) -> tuple[dict[str, Any], dict[str, set[str]]]:
    wavs = [p for p in group_root.rglob("*") if p.is_file() and p.suffix.lower() == ".wav"]
    participant_folders: set[str] = set()
    readable = unreadable = 0
    durations: list[float] = []
    rates: Counter[str] = Counter()
    channels: Counter[str] = Counter()
    widths: Counter[str] = Counter()
    compression: Counter[str] = Counter()
    task_counts: Counter[str] = Counter()
    task_people: dict[str, set[str]] = defaultdict(set)
    person_task_counts: dict[str, Counter[str]] = defaultdict(Counter)
    hashes: dict[str, set[str]] = defaultdict(set)
    cross_group_ready: dict[str, set[str]] = defaultdict(set)
    expected_task_positive = 0

    for path in wavs:
        rel = path.relative_to(group_root)
        if len(rel.parts) >= 3:
            person, task = rel.parts[0], rel.parts[1]
        elif len(rel.parts) == 2:
            person, task = rel.parts[0], "direct_under_participant"
        else:
            person, task = "__unmapped_layout__", "unmapped_layout"
        participant_folders.add(person)
        task_counts[task] += 1
        task_people[task].add(person)
        person_task_counts[person][task] += 1
        info = wav_info(path)
        if info is None:
            unreadable += 1
        else:
            readable += 1
            durations.append(info["duration_s"])
            rates[str(info["sample_rate_hz"])] += 1
            channels[str(info["channels"])] += 1
            widths[str(info["sample_width_bytes"])] += 1
            compression[str(info["compression_type"])] += 1
            if task == expected_task and info["duration_s"] > 0:
                expected_task_positive += 1
        digest = sha256_file(path)
        if digest:
            hashes[digest].add(str(path.resolve()))

    task_summary = {
        task: {"recordings": int(n),
               "participants_with_task": len(task_people[task]),
               "participants_with_multiple_files_for_task": sum(
                   1 for person in participant_folders if person_task_counts[person][task] > 1)}
        for task, n in sorted(task_counts.items())
    }
    report = {
        "wav_files_found": len(wavs),
        "distinct_participant_folders_with_wav": len(participant_folders),
        "readable_pcm_wav_headers": readable,
        "unreadable_or_unsupported_wav_files": unreadable,
        "sample_rate_hz_recording_counts": dict(sorted(rates.items())),
        "channel_count_recording_counts": dict(sorted(channels.items())),
        "sample_width_bytes_recording_counts": dict(sorted(widths.items())),
        "compression_type_recording_counts": dict(sorted(compression.items())),
        "duration_seconds": duration_summary(durations),
        "task_summary": task_summary,
        "expected_task_folder_exact_match": expected_task in task_counts,
        "expected_task_positive_duration_files": expected_task_positive,
        "exact_duplicate_audio_hash_groups": sum(1 for files in hashes.values() if len(files) > 1),
        "duplicate_files_beyond_first_copy": sum(len(files) - 1 for files in hashes.values() if len(files) > 1),
        "participant_folder_layout_warning": "unmapped_layout" in task_counts,
    }
    return report, hashes


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--root", required=True, type=Path, help="Authorized local EWA-DB root")
    parser.add_argument("--pd-dir", required=True, help="Exact immediate folder name for PD group")
    parser.add_argument("--control-dir", required=True, help="Exact immediate folder name for healthy controls")
    parser.add_argument("--task-dir", default="phonation", help="Exact sustained-vowel task-folder name; verify from release")
    parser.add_argument("--out", type=Path, default=Path("ewa_db_audio_audit_aggregate.json"), help="Aggregate JSON output")
    args = parser.parse_args()
    root = args.root.expanduser().resolve()
    if not root.is_dir():
        print("ERROR: --root is not an existing directory.", file=sys.stderr)
        return 2
    if args.pd_dir == args.control_dir:
        print("ERROR: PD and control folder names must differ.", file=sys.stderr)
        return 2
    pd_root, hc_root = root / args.pd_dir, root / args.control_dir
    missing = [label for label, p in (("PD", pd_root), ("control", hc_root)) if not p.is_dir()]
    if missing:
        print("ERROR: group directory not found: " + ", ".join(missing) +
              ". Inspect only top-level group names locally, then rerun.", file=sys.stderr)
        return 2

    pd_report, pd_hashes = audit_group(pd_root, args.task_dir)
    hc_report, hc_hashes = audit_group(hc_root, args.task_dir)
    pd_digests, hc_digests = set(pd_hashes), set(hc_hashes)
    shared = pd_digests & hc_digests
    result = {
        "audit_name": "EWA-DB local aggregate-only audio inventory",
        "audit_version": "1.0.0",
        "expected_layout": "group/participant_code/task/*.wav; actual names remain local",
        "selected_task_folder_name": args.task_dir,
        "cohort_summary": {
            "pd_participant_folders_with_wav": pd_report["distinct_participant_folders_with_wav"],
            "control_participant_folders_with_wav": hc_report["distinct_participant_folders_with_wav"],
            "combined_pd_control_participant_folders_with_wav":
                pd_report["distinct_participant_folders_with_wav"] + hc_report["distinct_participant_folders_with_wav"],
            "folder_count_is_not_proof_of_unique_individuals": True,
        },
        "group_audio_summary": {"PD": pd_report, "healthy_control": hc_report},
        "cross_group_exact_duplicate_audio_hash_groups": len(shared),
        "privacy": {"contains_participant_ids": False, "contains_file_paths_or_names": False,
                    "contains_audio_hashes": False, "contains_transcripts_or_metadata_rows": False,
                    "aggregate_counts_only": True},
        "interpretation_warnings": [
            "Folder counts do not prove unique subjects; verify participant manifest and repeat-visit policy.",
            "This is technical file QC, not validation of diagnosis, consent, licensing or cohort independence.",
            "Task summary assumes the task folder is the second path component below each group folder.",
            "Use only lawfully obtained files; do not upload audio, IDs, manifests or row-level metadata to public GitHub or third-party services."
        ],
    }
    output = args.out.expanduser().resolve()
    output.parent.mkdir(parents=True, exist_ok=True)
    output.write_text(json.dumps(result, indent=2, sort_keys=True) + "\n", encoding="utf-8")
    print(f"Aggregate-only audit written to: {output}")
    print(f"PD participant folders with WAV: {pd_report['distinct_participant_folders_with_wav']}; "
          f"control participant folders with WAV: {hc_report['distinct_participant_folders_with_wav']}")
    print("No participant IDs, filenames, file paths, audio hashes, transcripts or metadata values were written.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
