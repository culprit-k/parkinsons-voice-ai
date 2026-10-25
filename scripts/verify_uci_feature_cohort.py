#!/usr/bin/env python3
"""Audit official UCI repeated-sustained-vowel Parkinson's acoustic-feature cohorts.

This dataset is feature-only: it does not include the underlying voice recordings.
The audit emits aggregate cohort/label/repeat/missingness counts only. Never emit
subject IDs or row-level records into public artifacts.
"""
from __future__ import annotations

import argparse
import io
import json
import shutil
import subprocess
import tempfile
import urllib.request
import zipfile
from pathlib import Path
from typing import Any

import pandas as pd
from ucimlrepo import fetch_ucirepo

DATASETS = {
    470: {
        "source": "https://archive.ics.uci.edu/dataset/470/parkinson+s+disease+classification",
        "doi": "10.24432/C5MS4X",
        "expected_participants": 252,
        "expected_repetitions": 3,
        "description": "Sakar Parkinson's Disease Classification (754 engineered features; raw audio not included)",
    },
    489: {
        "source": "https://archive.ics.uci.edu/dataset/489/parkinson+dataset+with+replicated+acoustic+features",
        "doi": "10.24432/C5701F",
        "expected_participants": 80,
        "expected_repetitions": 3,
        "description": "Parkinson Dataset with replicated acoustic features (45 features; raw audio not included)",
    },
}


def find_column(columns: list[str], preferred: tuple[str, ...]) -> str | None:
    normalized = {str(c).strip().lower().replace(" ", "_"): c for c in columns}
    for candidate in preferred:
        if candidate in normalized:
            return str(normalized[candidate])
    for candidate in preferred:
        for norm, original in normalized.items():
            if candidate in norm:
                return str(original)
    return None


def safe_value_counts(series: pd.Series) -> dict[str, int]:
    return {str(key): int(value) for key, value in series.value_counts(dropna=False).items()}


def read_table_bytes(payload: bytes, filename: str) -> pd.DataFrame:
    """Read a CSV/TSV/data table from an official UCI download payload."""
    if zipfile.is_zipfile(io.BytesIO(payload)):
        with zipfile.ZipFile(io.BytesIO(payload)) as archive:
            candidates = [
                name for name in archive.namelist()
                if not name.endswith("/")
                and Path(name).suffix.lower() in {".csv", ".tsv", ".data", ".txt"}
                and Path(name).name.lower() not in {"readme.txt", "description.txt"}
            ]
            if not candidates:
                raise ValueError(
                    "Official UCI ZIP has no obvious table file; files are "
                    + ", ".join(Path(name).name for name in archive.namelist()[:20])
                )
            # Pick a likely data table, preferring CSV then the shortest data filename.
            candidates.sort(
                key=lambda name: (
                    0 if Path(name).suffix.lower() == ".csv" else 1,
                    len(name),
                )
            )
            member = candidates[0]
            with archive.open(member) as stream:
                raw = stream.read()
            return pd.read_csv(io.BytesIO(raw), sep=None, engine="python")

    if payload[:7].lower().startswith(b"rar!"):
        rar_path = Path(tempfile.mkstemp(prefix="uci_pd_", suffix=".rar")[1])
        try:
            rar_path.write_bytes(payload)
            # GitHub runner may have a command-line RAR reader. Raw archive is
            # ephemeral and never uploaded; only the parsed table's aggregate stats leave.
            extractor = shutil.which("7z") or shutil.which("7zz") or shutil.which("unar")
            if not extractor:
                raise RuntimeError(
                    "UCI API returned a RAR archive and no command-line extractor is installed"
                )
            out_dir = rar_path.with_suffix("")
            out_dir.mkdir()
            if Path(extractor).name == "unar":
                subprocess.run(
                    [extractor, "-quiet", "-output-directory", str(out_dir), str(rar_path)],
                    check=True, capture_output=True, text=True
                )
            else:
                subprocess.run(
                    [extractor, "x", "-y", f"-o{out_dir}", str(rar_path)],
                    check=True, capture_output=True, text=True
                )
            tables = [
                p for p in out_dir.rglob("*")
                if p.is_file() and p.suffix.lower() in {".csv", ".tsv", ".data", ".txt"}
                and p.name.lower() not in {"readme.txt", "description.txt"}
            ]
            if not tables:
                raise ValueError("RAR archive was extracted but no table file was found")
            tables.sort(key=lambda p: (0 if p.suffix.lower() == ".csv" else 1, len(p.name)))
            return pd.read_csv(tables[0], sep=None, engine="python")
        finally:
            rar_path.unlink(missing_ok=True)

    return pd.read_csv(io.BytesIO(payload), sep=None, engine="python")


def load_official_uci_table(dataset_id: int) -> tuple[pd.DataFrame, str]:
    """Use the public UCI API data URL if ucimlrepo cannot import this legacy release."""
    api_url = f"https://archive.ics.uci.edu/api/dataset?id={dataset_id}"
    request = urllib.request.Request(
        api_url,
        headers={"User-Agent": "PDVoiceDatasetAudit/1.0 (research reproducibility)"}
    )
    with urllib.request.urlopen(request, timeout=60) as response:
        envelope = json.load(response)
    data = envelope.get("data", envelope)
    data_url = data.get("data_url") or data.get("download_url")
    if not data_url:
        files = data.get("files", [])
        if isinstance(files, list):
            links = [
                f.get("link") or f.get("url") or f.get("download_url")
                for f in files if isinstance(f, dict)
            ]
            data_url = next((link for link in links if link), None)
    if not data_url:
        raise ValueError(
            f"Official UCI API has no import URL for dataset {dataset_id}; "
            f"metadata keys={sorted(data.keys())}"
        )
    request = urllib.request.Request(
        data_url,
        headers={"User-Agent": "PDVoiceDatasetAudit/1.0 (research reproducibility)"}
    )
    with urllib.request.urlopen(request, timeout=90) as response:
        payload = response.read()
        reported_name = response.headers.get("Content-Disposition", "")
        filename = reported_name.split("filename=", 1)[-1].strip('"') if "filename=" in reported_name else Path(data_url).name
    frame = read_table_bytes(payload, filename)
    return frame, str(data_url)


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--output", default="uci_feature_cohort_PRIVATE.json")
    parser.add_argument("--dataset-id", type=int, choices=(470, 489), default=489)
    args = parser.parse_args()

    dataset_id = args.dataset_id
    metadata = DATASETS[dataset_id]
    import_method = "ucimlrepo"
    source_download_url = None
    try:
        dataset = fetch_ucirepo(id=dataset_id)
        features = dataset.data.features.copy()
        targets = dataset.data.targets.copy() if dataset.data.targets is not None else pd.DataFrame()
        variables = dataset.variables.copy() if dataset.variables is not None else pd.DataFrame()
        id_table = (
            dataset.data.ids.copy()
            if getattr(dataset.data, "ids", None) is not None
            else pd.DataFrame()
        )
        original = (
            dataset.data.original.copy()
            if getattr(dataset.data, "original", None) is not None
            else pd.DataFrame()
        )

        # UCI's client separates role=ID columns from .features on some datasets.
        if not original.empty:
            frame = original.copy()
        else:
            frame = pd.concat(
                [table.reset_index(drop=True) for table in (id_table, features, targets)
                 if table is not None and not table.empty],
                axis=1
            )
            frame = frame.loc[:, ~frame.columns.duplicated()]
    except Exception as import_error:
        # Some older UCI records remain downloadable but are not yet import-enabled
        # in the ucimlrepo API. Use only the official UCI API's own data_url as fallback.
        frame, source_download_url = load_official_uci_table(dataset_id)
        features = frame.copy()
        targets = pd.DataFrame()
        variables = pd.DataFrame()
        id_table = pd.DataFrame()
        original = frame.copy()
        import_method = "official_uci_api_direct_download_fallback"
        print(
            f"ucimlrepo import unavailable ({type(import_error).__name__}); "
            "used the official UCI API data URL."
        )

    columns = list(frame.columns)
    id_col = find_column(columns, ("subject_id", "subject", "participant_id", "patient_id", "id"))
    record_col = find_column(columns, ("recording_id", "recording", "replication", "replicate", "trial"))
    label_col = find_column(list(targets.columns), ("class", "status", "label", "diagnosis", "target"))
    if label_col is None:
        label_col = find_column(columns, ("class", "status", "label", "diagnosis", "target"))

    # If column names are atypical, infer the participant key by the strong public
    # design constraint: each of 252 speakers contributes exactly three rows.
    expected_participants = metadata["expected_participants"]
    if id_col is None or frame[id_col].nunique(dropna=True) != expected_participants:
        candidate_ids = [
            str(col) for col in columns
            if frame[col].nunique(dropna=True) == expected_participants
            and frame[col].notna().all()
        ]
        id_col = candidate_ids[0] if len(candidate_ids) == 1 else id_col

    if id_col is None or label_col is None:
        raise ValueError(
            "Could not unambiguously identify subject ID and target label columns. "
            f"Columns={columns[:20]!r}; targets={list(targets.columns)!r}"
        )

    grouped = frame.groupby(id_col, dropna=False, sort=False)
    rows_per_subject = grouped.size()
    per_subject_label_counts = grouped[label_col].nunique(dropna=False)
    participant_label_counts = grouped[label_col].first().value_counts(dropna=False)

    # If a recording indicator is present, validate repeat count and row uniqueness
    # only as a QC signal; never treat 756 recordings as 756 people.
    missing_by_column = {
        str(col): int(frame[col].isna().sum())
        for col in columns
        if frame[col].isna().any()
    }
    acoustic_cols = [
        col for col in features.columns
        if col not in {id_col, record_col}
        and str(col).strip().lower() not in {
            "gender", "sex", "age", "class", "status", "label", "diagnosis",
            "target", "subject", "subject_id", "participant_id", "patient_id"
        }
    ]
    acoustic_missing = int(features[acoustic_cols].isna().sum().sum()) if acoustic_cols else None

    sex_col = find_column(columns, ("gender", "sex"))
    sex_counts = safe_value_counts(frame[sex_col]) if sex_col else None
    record_unique_per_subject = None
    if record_col is not None:
        record_unique_per_subject = int(
            grouped[record_col].nunique(dropna=False).min()
        ) if len(rows_per_subject) else None

    # Official metadata are public, but the exact feature names and all row-level IDs
    # stay out of the shareable artifact.
    report: dict[str, Any] = {
        "source": metadata["source"],
        "doi": metadata["doi"],
        "uci_dataset_id": dataset_id,
        "dataset_description": metadata["description"],
        "license": "CC BY 4.0 (per official UCI record)",
        "raw_voice_audio_in_release": False,
        "data_access_method": import_method,
        "source_download_url_from_official_api": source_download_url,
        "status": "feature_cohort_audit_completed",
        "row_count_recordings": int(len(frame)),
        "feature_column_count": int(len(acoustic_cols)),
        "subject_id_column_detected": True,
        "participant_count": int(frame[id_col].nunique(dropna=True)),
        "recording_count_per_subject_min": int(rows_per_subject.min()),
        "recording_count_per_subject_max": int(rows_per_subject.max()),
        "recording_count_per_subject_all_equal_expected": bool((rows_per_subject == metadata["expected_repetitions"]).all()),
        "expected_recordings_per_subject": metadata["expected_repetitions"],
        "recording_indicator_detected": record_col is not None,
        "recording_indicator_unique_values_min_per_subject": record_unique_per_subject,
        "label_column_detected": True,
        "recording_level_label_counts": safe_value_counts(frame[label_col]),
        "participant_level_label_counts": {
            str(key): int(value) for key, value in participant_label_counts.items()
        },
        "subjects_with_more_than_one_label_across_repetitions": int(
            (per_subject_label_counts > 1).sum()
        ),
        "age_variable_present": bool(find_column(columns, ("age",)) is not None),
        "sex_variable_present": sex_col is not None,
        "sex_recording_level_counts": sex_counts,
        "acoustic_features_missing_value_cells": acoustic_missing,
        "columns_with_missing_values": missing_by_column,
        "feature_schema_note": (
            "Dataset 470: 754 features (21 baseline, 11 time-frequency, 84 MFCC, "
            "182 wavelet, 22 vocal-fold, 434 TWQT-derived per source literature). "
            "Dataset 489: 45 repeated acoustic features per official UCI variable description."
            if dataset_id == 470 else
            "Dataset 489: 45 features covering jitter, shimmer, HNR, MFCC-derived measures, RPDE, DFA and PPE per official UCI variable description."
        ),
        "limitations": [
            "Feature-only cohort: no WAV audio is included in this release.",
            f"{len(frame)} recordings are repeated observations from {int(frame[id_col].nunique(dropna=True))} speakers; participant-grouped handling is mandatory.",
            "This cohort is not yet approved for the target study until the harmonizable feature subset and extraction provenance are documented.",
            "No model was trained and no performance metric was calculated."
        ],
        "participant_ids_or_rows_emitted": False,
    }

    output = Path(args.output)
    output.parent.mkdir(parents=True, exist_ok=True)
    output.write_text(json.dumps(report, indent=2), encoding="utf-8")
    print(json.dumps(report, indent=2))
    print(f"Aggregate audit saved to {output}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
