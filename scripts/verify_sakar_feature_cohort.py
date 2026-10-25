#!/usr/bin/env python3
"""Audit the official UCI Sakar Parkinson's Disease Classification feature cohort.

This dataset is feature-only: it does not include the underlying voice recordings.
The audit emits aggregate cohort/label/repeat/missingness counts only. Never emit
subject IDs or row-level records into public artifacts.
"""
from __future__ import annotations

import argparse
import json
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


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--output", default="uci_feature_audit_PRIVATE.json")
    parser.add_argument("--dataset-id", type=int, choices=(470, 489), default=489)
    args = parser.parse_args()

    dataset_id = args.dataset_id
    metadata = DATASETS[dataset_id]
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
    # Prefer the full original table when present, otherwise reconstruct it by
    # combining IDs, features and targets row-wise without publishing any rows.
    if not original.empty:
        frame = original.copy()
    else:
        frame = pd.concat(
            [table.reset_index(drop=True) for table in (id_table, features, targets)
             if table is not None and not table.empty],
            axis=1
        )
        frame = frame.loc[:, ~frame.columns.duplicated()]

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
        "status": "feature_cohort_audit_completed",
        "row_count_recordings": int(len(frame)),
        "feature_column_count_from_ucimlrepo": int(len(features.columns)),
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
            "756 recordings are repeated observations from 252 speakers; participant-grouped handling is mandatory.",
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
