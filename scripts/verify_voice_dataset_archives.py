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
        return {"wav_header_status": f"error: {type(exc).__name__}: {exc}"}


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
    durations = [row["duration_seconds"] for row in wavs if row.get("duration_seconds") is not None]

    return {
        "dataset": dataset,
        "file_count_all_types": len(records),
        "file_count_by_extension": dict(extensions),
        "audio_file_count": len(audio),
        "wav_file_count": len(wavs),
        "wav_headers_readable": sum(row.get("wav_header_status") == "ok" for row in wavs),
        "sample_rate_count_hz": dict(rates),
        "channel_count": dict(channels),
        "wav_duration_min_seconds": min(durations) if durations else None,
        "wav_duration_max_seconds": max(durations) if durations else None,
        "duplicate_audio_hash_groups": duplicate_groups,
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
        if zipfile.is_zipfile(destination):
            safe_extract(destination, extraction_dir / destination.stem)
        else:
            shutil.copy2(destination, extraction_dir / filename)

    nested = unpack_nested_zips(extraction_dir)
    report = inventory(
        extraction_dir, name, base / "private_manifests" / "placeholder.csv"
    )
    report.update({
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


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--dataset", choices=("ipvs", "uams", "all"), default="all")
    parser.add_argument("--output-dir", default="data/raw/_audit")
    args = parser.parse_args()

    output = Path(args.output_dir).expanduser().resolve()
    targets: list[tuple[str, str, str | None]] = []
    if args.dataset in ("ipvs", "all"):
        targets.append(("ipvs", IPVS_URL, IPVS_EXPECTED_SHA256))
    if args.dataset in ("uams", "all"):
        targets.append(("uams", UAMS_URL, None))

    summary: dict[str, Any] = {
        "audit_time_utc": time.strftime("%Y-%m-%dT%H:%M:%SZ", time.gmtime()),
        "datasets": {},
    }
    for name, url, expected in targets:
        print(f"[{name}] starting download/inventory", flush=True)
        try:
            if name == "uams":
                summary["datasets"][name] = audit_figshare_article(name, url, output)
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
