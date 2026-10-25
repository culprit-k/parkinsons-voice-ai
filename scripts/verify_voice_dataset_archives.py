#!/usr/bin/env python3
"""Download and inventory public candidate Parkinson's voice archives.

Run in a network-enabled research environment:
    python scripts/verify_voice_dataset_archives.py --dataset all

Raw audio and per-file manifests remain local and must never be committed.
This script audits files and WAV headers; it does not adjudicate participant
identity, diagnosis provenance, or spreadsheet-to-audio joins.
"""
from __future__ import annotations

import argparse
import csv
import hashlib
import json
import shutil
import stat
import sys
import time
import urllib.request
import wave
import zipfile
from collections import Counter, defaultdict
from pathlib import Path
from typing import Any

IPVS_URL = (
    "https://huggingface.co/datasets/birgermoell/Italian_Parkinsons_Voice_and_Speech/"
    "resolve/70d1714cf738b248d687b003551351cbe37e0298/italian_parkinson/"
    "Italian%20Parkinson%27s%20Voice%20and%20speech.zip"
)
IPVS_EXPECTED_SHA256 = (
    "3c4cd221345f7a81f0eeaceedf44dedbfd33b08ecd18ab5a3307edefcfbacfed"
)
UAMS_URL = "https://api.figshare.com/v2/articles/23849127"
MDVR_URL = "https://zenodo.org/api/records/2867216"
AUDIO_EXTENSIONS = {".wav", ".flac", ".m4a", ".mp3", ".ogg"}


def sha256_file(path: Path) -> str:
    digest = hashlib.sha256()
    with path.open("rb") as stream:
        for block in iter(lambda: stream.read(1024 * 1024), b""):
            digest.update(block)
    return digest.hexdigest()


def download(url: str, destination: Path) -> dict[str, Any]:
    destination.parent.mkdir(parents=True, exist_ok=True)
    request = urllib.request.Request(
        url,
        headers={"User-Agent": "PDVoiceDatasetAudit/1.0 (research reproducibility)"},
    )
    started = time.time()
    temporary = destination.with_suffix(destination.suffix + ".part")
    with urllib.request.urlopen(request, timeout=90) as response:
        content_length = response.headers.get("Content-Length")
        with temporary.open("wb") as output:
            shutil.copyfileobj(response, output, length=1024 * 1024)
    temporary.replace(destination)
    return {
        "url": url,
        "bytes": destination.stat().st_size,
        "content_length_header": content_length,
        "sha256_local": sha256_file(destination),
        "seconds": round(time.time() - started, 2),
        "downloaded_now": True,
    }


def safe_extract(archive: Path, destination: Path) -> int:
    """Extract a ZIP safely; reject traversal paths and symbolic links."""
    destination.mkdir(parents=True, exist_ok=True)
    root = destination.resolve()
    extracted = 0
    with zipfile.ZipFile(archive) as zipped:
        for item in zipped.infolist():
            target = (destination / item.filename).resolve()
            if target != root and root not in target.parents:
                raise ValueError(f"Unsafe ZIP path in {archive.name}: {item.filename!r}")
            mode = item.external_attr >> 16
            if stat.S_ISLNK(mode):
                raise ValueError(f"Refusing symbolic-link entry: {item.filename!r}")
            if item.is_dir():
                target.mkdir(parents=True, exist_ok=True)
                continue
            target.parent.mkdir(parents=True, exist_ok=True)
            with zipped.open(item) as source, target.open("wb") as output:
                shutil.copyfileobj(source, output, length=1024 * 1024)
            extracted += 1
    return extracted


def unpack_nested_zips(root: Path, max_depth: int = 3) -> list[dict[str, Any]]:
    results: list[dict[str, Any]] = []
    seen: set[str] = set()
    for depth in range(1, max_depth + 1):
        archives = [
            path for path in sorted(root.rglob("*.zip"))
            if path.is_file() and str(path.resolve()) not in seen
        ]
        if not archives:
            break
        for archive in archives:
            seen.add(str(archive.resolve()))
            target = archive.parent / (archive.stem + "_extracted")
            try:
                count = safe_extract(archive, target)
                results.append({
                    "archive_relative_path": archive.relative_to(root).as_posix(),
                    "files_extracted": count,
                    "depth": depth,
                    "status": "ok",
                })
            except Exception as exc:
                results.append({
                    "archive_relative_path": archive.relative_to(root).as_posix(),
                    "depth": depth,
                    "status": "failed",
                    "error": f"{type(exc).__name__}: {exc}",
                })
    return results


def path_group_hint(path: Path) -> str:
    text = "/".join(part.lower() for part in path.parts)
    if any(token in text for token in ("young healthy", "young control", "15 yhc", "yhc")):
        return "young_control"
    if any(token in text for token in ("elderly healthy", "elderly control", "healthy control", "hc_ah", "/hc/")):
        return "healthy_control"
    if any(token in text for token in ("people with parkinson", "parkinson's disease", "pd_ah", "/pd/")):
        return "parkinson"
    return "unknown"


def wav_metadata(path: Path) -> dict[str, Any]:
    try:
        with wave.open(str(path), "rb") as audio:
            rate = audio.getframerate()
            frames = audio.getnframes()
            return {
                "wav_header_status": "ok",
                "channels": audio.getnchannels(),
                "sample_width_bytes": audio.getsampwidth(),
                "sample_rate_hz": rate,
                "frames": frames,
                "duration_seconds": round(frames / rate, 5) if rate else None,
                "compression": audio.getcomptype(),
            }
    except (wave.Error, EOFError, OSError) as exc:
        wave_error = f"{type(exc).__name__}: {exc}"
        try:
            import soundfile as sf
            info = sf.info(str(path))
            return {
                "wav_header_status": "ok_soundfile_fallback",
                "channels": info.channels,
                "sample_width_bytes": None,
                "sample_rate_hz": info.samplerate,
                "frames": info.frames,
                "duration_seconds": round(info.duration, 5),
                "compression": info.format + "/" + str(info.subtype),
                "stdlib_wave_error": wave_error,
            }
        except Exception as fallback_exc:
            return {
                "wav_header_status": f"error: {type(fallback_exc).__name__}: {fallback_exc}",
                "stdlib_wave_error": wave_error,
            }


def inventory(root: Path, dataset: str, destination: Path) -> dict[str, Any]:
    records: list[dict[str, Any]] = []
    files = sorted(path for path in root.rglob("*") if path.is_file())
    extensions = Counter(path.suffix.lower() or "[no_extension]" for path in files)

    for path in files:
        rel = path.relative_to(root)
        record: dict[str, Any] = {
            "dataset": dataset,
            "path_private": rel.as_posix(),
            "extension": path.suffix.lower(),
            "bytes": path.stat().st_size,
            "group_path_hint_not_a_label": path_group_hint(rel),
        }
        if path.suffix.lower() in AUDIO_EXTENSIONS:
            record["sha256"] = sha256_file(path)
        if path.suffix.lower() == ".wav":
            record.update(wav_metadata(path))
        records.append(record)

    destination.parent.mkdir(parents=True, exist_ok=True)
    manifest = destination.with_name(dataset + "_manifest_PRIVATE.csv")
    fieldnames = sorted({key for record in records for key in record})
    with manifest.open("w", newline="", encoding="utf-8") as stream:
        writer = csv.DictWriter(stream, fieldnames=fieldnames)
        writer.writeheader()
        writer.writerows(records)

    audio = [row for row in records if row.get("extension") in AUDIO_EXTENSIONS]
    wavs = [row for row in audio if row.get("extension") == ".wav"]
    rates = Counter(str(row["sample_rate_hz"]) for row in wavs if row.get("sample_rate_hz"))
    channels = Counter(str(row["channels"]) for row in wavs if row.get("channels"))
    hashes: dict[str, list[str]] = defaultdict(list)
    for row in audio:
        if row.get("sha256"):
            hashes[row["sha256"]].append(row["path_private"])
    duplicate_groups = [
        {"sha256": digest, "paths_private": paths}
        for digest, paths in hashes.items() if len(paths) > 1
    ]
    duplicate_relationships = []
    for group in duplicate_groups:
        group_paths = [Path(path) for path in group["paths_private"]]
        duplicate_relationships.append({
            "group_size": len(group_paths),
            "same_parent_directory": len({path.parent.as_posix() for path in group_paths}) == 1,
            "cohort_groups": sorted({path_group_hint(path) for path in group_paths}),
        })
    durations = [row["duration_seconds"] for row in wavs if row.get("duration_seconds") is not None]

    return {
        "dataset": dataset,
        "file_count_all_types": len(records),
        "file_count_by_extension": dict(extensions),
        "audio_file_count": len(audio),
        "wav_file_count": len(wavs),
        "wav_headers_readable": sum(str(row.get("wav_header_status", "")).startswith("ok") for row in wavs),
        "wav_header_error_counts": dict(Counter(
            row.get("wav_header_status", "unknown")
            for row in wavs if not str(row.get("wav_header_status", "")).startswith("ok")
        )),
        "sample_rate_count_hz": dict(rates),
        "channel_count": dict(channels),
        "wav_duration_min_seconds": min(durations) if durations else None,
        "wav_duration_max_seconds": max(durations) if durations else None,
        "duplicate_audio_hash_groups": duplicate_groups,
        "duplicate_audio_relationships": duplicate_relationships,
        "cohort_path_summary": cohort_path_summary(root),
        "private_manifest": str(manifest),
        "warning": (
            "Group names inferred from file paths are hints, not validated diagnoses. "
            "Unique participants, repeats, workbook joins and diagnostic provenance need "
            "separate review before modelling."
        ),
    }


def audit_one(name: str, url: str, expected_sha: str | None, output: Path) -> dict[str, Any]:
    base = output / name
    download_dir = base / "downloads"
    extraction_dir = base / "extracted"
    archive = download_dir / (name + "_all_files.zip")
    download_dir.mkdir(parents=True, exist_ok=True)

    if archive.exists():
        info: dict[str, Any] = {
            "url": url,
            "bytes": archive.stat().st_size,
            "sha256_local": sha256_file(archive),
            "downloaded_now": False,
        }
    else:
        info = download(url, archive)

    if expected_sha and info["sha256_local"].lower() != expected_sha.lower():
        raise ValueError(
            f"Host checksum mismatch: expected {expected_sha}, got {info['sha256_local']}"
        )
    if not zipfile.is_zipfile(archive):
        raise ValueError(
            "Downloaded response is not a ZIP archive; it may be an HTML error response. "
            f"File retained for diagnosis at {archive}"
        )

    first_level_count = safe_extract(archive, extraction_dir)
    nested = unpack_nested_zips(extraction_dir)
    report = inventory(extraction_dir, name, base / "private_manifests" / "placeholder.csv")
    report.update({
        "spreadsheet_audit": audit_spreadsheets(extraction_dir),
        "archive_path": str(archive),
        "archive_bytes": info["bytes"],
        "archive_sha256_local": info["sha256_local"],
        "host_sha256_expected": expected_sha,
        "host_hash_match": (
            info["sha256_local"].lower() == expected_sha.lower()
            if expected_sha else None
        ),
        "first_level_files_extracted": first_level_count,
        "nested_zip_extractions": nested,
        "status": "archive_downloaded_and_inventory_completed",
    })
    return report


def cohort_path_summary(root: Path) -> dict[str, Any]:
    """Summarize WAV counts and directory-depth structure without exposing folder names."""
    accum: dict[str, dict[str, Any]] = {}
    for path in sorted(root.rglob("*.wav")):
        rel = path.relative_to(root)
        group = path_group_hint(rel)
        if group == "unknown":
            continue
        parts = rel.parts
        category_idx = next(
            (i for i, part in enumerate(parts)
             if path_group_hint(Path(part)) == group
             and any(token in part.lower() for token in (
                 "young healthy", "young control", "elderly healthy",
                 "elderly control", "people with parkinson", "parkinson's disease"
             ))),
            None,
        )
        if category_idx is None:
            continue
        directory_parts = parts[category_idx + 1:-1]
        entry = accum.setdefault(group, {
            "wav_count": 0,
            "directory_prefixes_by_depth": defaultdict(set),
            "directory_names_by_depth": defaultdict(set),
        })
        entry["wav_count"] += 1
        for depth in range(1, len(directory_parts) + 1):
            entry["directory_prefixes_by_depth"][depth].add(
                "/".join(directory_parts[:depth])
            )
            entry["directory_names_by_depth"][depth].add(directory_parts[depth - 1])

    output: dict[str, Any] = {}
    for group, item in accum.items():
        output[group] = {
            "wav_count": item["wav_count"],
            "unique_directory_counts_by_depth": {
                str(depth): len(prefixes)
                for depth, prefixes in sorted(item["directory_prefixes_by_depth"].items())
            },
            "unique_directory_name_counts_by_depth": {
                str(depth): len(names)
                for depth, names in sorted(item["directory_names_by_depth"].items())
            },
            "participant_count": "not inferred from folder depth; requires source-specific mapping",
        }
    return output

def audit_spreadsheets(root: Path) -> list[dict[str, Any]]:
    """Summarize workbook structure and safe aggregate ID/label linkage metrics."""
    try:
        import openpyxl
    except ImportError:
        return [{"status": "openpyxl_not_installed"}]

    audio_stems = {
        path.stem.strip().lower()
        for path in root.rglob("*")
        if path.is_file() and path.suffix.lower() in AUDIO_EXTENSIONS
    }
    reports: list[dict[str, Any]] = []
    for workbook_path in sorted(root.rglob("*.xlsx")):
        workbook_report: dict[str, Any] = {
            "workbook_filename_private": workbook_path.name,
            "status": "ok",
            "sheets": [],
        }
        try:
            workbook = openpyxl.load_workbook(workbook_path, read_only=True, data_only=True)
            for sheet in workbook.worksheets:
                rows = list(sheet.iter_rows(values_only=True))
                nonempty_rows = [tuple(row) for row in rows if any(value is not None for value in row)]
                if not nonempty_rows:
                    workbook_report["sheets"].append({
                        "sheet_name_private": sheet.title,
                        "nonempty_rows": 0,
                    })
                    continue
                header_idx = 0
                header_score = -1
                for candidate_idx, candidate_row in enumerate(nonempty_rows[:10]):
                    candidate_headers = [
                        str(value).strip().lower() if value is not None else ""
                        for value in candidate_row
                    ]
                    score = sum(
                        any(token in value for token in (
                            "id", "sample", "subject", "participant", "filename",
                            "label", "diagnosis", "disease", "condition", "class",
                            "group", "status", "age", "sex", "gender",
                        ))
                        for value in candidate_headers
                    )
                    if score > header_score:
                        header_score = score
                        header_idx = candidate_idx
                headers = [
                    str(value).strip() if value is not None else ""
                    for value in nonempty_rows[header_idx]
                ]
                normalized = [value.lower() for value in headers]
                id_index = next(
                    (i for i, value in enumerate(normalized)
                     if any(token in value for token in (
                         "sample id", "sample_id", "participant", "subject", "filename",
                         "patient id", "recording id", "file id"
                     )) or value.strip() in {"id", "sample", "subject_id", "subject id"}),
                    None,
                )
                label_index = next(
                    (i for i, value in enumerate(normalized)
                     if any(token in value for token in (
                         "label", "diagnosis", "disease", "condition", "class", "group", "status"
                     ))),
                    None,
                )
                data_rows = nonempty_rows[header_idx + 1:]
                ids = [
                    str(row[id_index]).strip().lower()
                    for row in data_rows
                    if id_index is not None and id_index < len(row) and row[id_index] is not None
                ]
                labels = Counter(
                    str(row[label_index]).strip()
                    for row in data_rows
                    if label_index is not None and label_index < len(row) and row[label_index] is not None
                )
                matched = 0
                if id_index is not None:
                    matched = sum(
                        1 for sample_id in ids
                        if sample_id in audio_stems
                        or Path(sample_id).stem in audio_stems
                        or any(stem.endswith(sample_id) for stem in audio_stems)
                    )
                workbook_report["sheets"].append({
                    "sheet_name_private": sheet.title,
                    "nonempty_rows_including_header": len(nonempty_rows),
                    "data_rows": len(data_rows),
                    "column_headers_private": headers,
                    "direct_name_fields_present": any(value in {"name", "first name", "surname", "last name"} for value in normalized),
                    "id_column_detected": headers[id_index] if id_index is not None else None,
                    "label_column_detected": headers[label_index] if label_index is not None else None,
                    "rows_with_id": len(ids),
                    "unique_ids": len(set(ids)),
                    "rows_missing_id": max(0, len(data_rows) - len(ids)) if id_index is not None else None,
                    "label_value_counts": dict(labels),
                    "ids_matching_audio_filename": matched if id_index is not None else None,
                    "ids_not_matching_audio_filename": max(0, len(set(ids)) - matched) if id_index is not None else None,
                })
            workbook.close()
        except Exception as exc:
            workbook_report["status"] = f"failed: {type(exc).__name__}: {exc}"
        reports.append(workbook_report)
    return reports


def audit_figshare_article(name: str, metadata_url: str, output: Path) -> dict[str, Any]:
    """Download public Figshare article files individually through its public API."""
    request = urllib.request.Request(
        metadata_url,
        headers={"User-Agent": "PDVoiceDatasetAudit/1.0 (research reproducibility)"},
    )
    with urllib.request.urlopen(request, timeout=60) as response:
        metadata = json.load(response)

    files = metadata.get("files", [])
    if not files:
        raise ValueError("Figshare API returned no public files for the article")

    base = output / name
    download_dir = base / "downloads"
    extraction_dir = base / "extracted"
    download_dir.mkdir(parents=True, exist_ok=True)
    extraction_dir.mkdir(parents=True, exist_ok=True)
    file_checks: list[dict[str, Any]] = []

    for item in files:
        filename = Path(item.get("name", f"figshare_file_{item.get('id')}")).name
        destination = download_dir / filename
        info = download(item["download_url"], destination)
        md5 = hashlib.md5()
        with destination.open("rb") as stream:
            for block in iter(lambda: stream.read(1024 * 1024), b""):
                md5.update(block)
        local_md5 = md5.hexdigest()
        expected_md5 = item.get("computed_md5") or item.get("supplied_md5")
        md5_match = local_md5.lower() == expected_md5.lower() if expected_md5 else None
        if md5_match is False:
            raise ValueError(
                f"Figshare MD5 mismatch for {filename}: expected {expected_md5}, got {local_md5}"
            )
        file_checks.append({
            "filename_private": filename,
            "bytes_local": destination.stat().st_size,
            "sha256_local": info["sha256_local"],
            "md5_local": local_md5,
            "md5_expected": expected_md5,
            "md5_match": md5_match,
            "figshare_file_id": item.get("id"),
        })
        if destination.suffix.lower() == ".zip" and zipfile.is_zipfile(destination):
            safe_extract(destination, extraction_dir / destination.stem)
        else:
            shutil.copy2(destination, extraction_dir / filename)

    nested = unpack_nested_zips(extraction_dir)
    report = inventory(
        extraction_dir, name, base / "private_manifests" / "placeholder.csv"
    )
    report.update({
        "spreadsheet_audit": audit_spreadsheets(extraction_dir),
        "figshare_article_id": metadata.get("id"),
        "figshare_title": metadata.get("title"),
        "figshare_license": metadata.get("license"),
        "figshare_version": metadata.get("version"),
        "figshare_source_file_count": len(files),
        "figshare_source_file_checks": file_checks,
        "archive_bytes": sum(item["bytes_local"] for item in file_checks),
        "archive_sha256_local": None,
        "host_sha256_expected": None,
        "host_hash_match": None,
        "nested_zip_extractions": nested,
        "status": "archive_downloaded_and_inventory_completed",
        "warning": (
            "Audio files were inventoried, but workbook-to-audio participant joins and "
            "diagnostic provenance require separate inspection."
        ),
    })
    return report


def audit_zenodo_record(name: str, metadata_url: str, output: Path) -> dict[str, Any]:
    """Download and verify the public files listed by a Zenodo record API."""
    request = urllib.request.Request(
        metadata_url,
        headers={"User-Agent": "PDVoiceDatasetAudit/1.0 (research reproducibility)"},
    )
    with urllib.request.urlopen(request, timeout=60) as response:
        metadata = json.load(response)
    files = metadata.get("files", [])
    if not files:
        raise ValueError("Zenodo API returned no public files for the record")

    base = output / name
    download_dir = base / "downloads"
    extraction_dir = base / "extracted"
    download_dir.mkdir(parents=True, exist_ok=True)
    extraction_dir.mkdir(parents=True, exist_ok=True)
    checks: list[dict[str, Any]] = []

    for item in files:
        filename = Path(item.get("key", f"zenodo_file_{item.get('id')}")).name
        destination = download_dir / filename
        url = item.get("links", {}).get("self") or item.get("links", {}).get("download")
        if not url:
            raise ValueError(f"No public download URL for Zenodo file {filename}")
        info = download(url, destination)
        md5 = hashlib.md5()
        with destination.open("rb") as stream:
            for block in iter(lambda: stream.read(1024 * 1024), b""):
                md5.update(block)
        local_md5 = md5.hexdigest()
        checksum = item.get("checksum", "")
        expected_md5 = checksum.split(":", 1)[1] if checksum.startswith("md5:") else None
        md5_match = local_md5.lower() == expected_md5.lower() if expected_md5 else None
        if md5_match is False:
            raise ValueError(
                f"Zenodo MD5 mismatch for {filename}: expected {expected_md5}, got {local_md5}"
            )
        checks.append({
            "filename_private": filename,
            "bytes_local": destination.stat().st_size,
            "sha256_local": info["sha256_local"],
            "md5_local": local_md5,
            "md5_expected": expected_md5,
            "md5_match": md5_match,
            "zenodo_file_id": item.get("id"),
        })
        if destination.suffix.lower() == ".zip" and zipfile.is_zipfile(destination):
            safe_extract(destination, extraction_dir / destination.stem)
        else:
            shutil.copy2(destination, extraction_dir / filename)

    nested = unpack_nested_zips(extraction_dir)
    report = inventory(
        extraction_dir, name, base / "private_manifests" / "placeholder.csv"
    )
    report.update({
        "zenodo_record_id": metadata.get("id"),
        "zenodo_doi": metadata.get("metadata", {}).get("doi"),
        "zenodo_title": metadata.get("metadata", {}).get("title"),
        "zenodo_license": metadata.get("metadata", {}).get("license"),
        "source_file_count": len(files),
        "source_file_checks": checks,
        "archive_bytes": sum(item["bytes_local"] for item in checks),
        "archive_sha256_local": None,
        "host_sha256_expected": None,
        "host_hash_match": None,
        "spreadsheet_audit": audit_spreadsheets(extraction_dir),
        "nested_zip_extractions": nested,
        "status": "archive_downloaded_and_inventory_completed",
        "warning": (
            "Participant independence and diagnosis provenance require review of source "
            "documentation; task is connected speech and is not task-matched to sustained /a/."
        ),
    })
    return report


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--dataset", choices=("ipvs", "uams", "mdvr", "all"), default="all")
    parser.add_argument("--output-dir", default="data/raw/_audit")
    args = parser.parse_args()

    output = Path(args.output_dir).expanduser().resolve()
    targets: list[tuple[str, str, str | None]] = []
    if args.dataset in ("ipvs", "all"):
        targets.append(("ipvs", IPVS_URL, IPVS_EXPECTED_SHA256))
    if args.dataset in ("uams", "all"):
        targets.append(("uams", UAMS_URL, None))
    if args.dataset in ("mdvr", "all"):
        targets.append(("mdvr", MDVR_URL, None))

    summary: dict[str, Any] = {
        "audit_time_utc": time.strftime("%Y-%m-%dT%H:%M:%SZ", time.gmtime()),
        "datasets": {},
    }
    for name, url, expected in targets:
        print(f"[{name}] starting download/inventory", flush=True)
        try:
            if name == "uams":
                summary["datasets"][name] = audit_figshare_article(name, url, output)
            elif name == "mdvr":
                summary["datasets"][name] = audit_zenodo_record(name, url, output)
            else:
                summary["datasets"][name] = audit_one(name, url, expected, output)
            print(f"[{name}] inventory complete", flush=True)
        except Exception as exc:
            summary["datasets"][name] = {
                "status": "FAILED",
                "url": url,
                "host_sha256_expected": expected,
                "error": f"{type(exc).__name__}: {exc}",
            }
            print(f"[{name}] failed: {type(exc).__name__}: {exc}", file=sys.stderr, flush=True)

    output.mkdir(parents=True, exist_ok=True)
    summary_path = output / "aggregate_summary_PRIVATE.json"
    summary_path.write_text(json.dumps(summary, indent=2), encoding="utf-8")
    print(f"Summary saved privately to {summary_path}")
    print("Do not commit raw archives, per-file manifests or this private summary.", file=sys.stderr)
    return 0 if all(item.get("status") != "FAILED" for item in summary["datasets"].values()) else 1


if __name__ == "__main__":
    raise SystemExit(main())
