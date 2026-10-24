# Parkinson's Voice AI Research

**Status:** Project setup and preliminary evidence audit. No model experiments or clinical performance claims have been produced.

## Objective
Investigate voice-based machine-learning approaches for Parkinson's disease research, emphasizing cross-language generalization, demographic confounding, recording robustness, and calibration.

## Provisional research questions
1. How well do models generalize to a language, site, or dataset not represented during training?
2. How much observed performance is explained by demographic or dataset/site differences?
3. How sensitive are results to recording conditions and preprocessing?
4. Are predicted probabilities calibrated, and how uncertain are subgroup estimates?

These questions remain provisional until literature and dataset feasibility reviews are complete.

## Project status
- [x] Topic and broad objective selected
- [x] Initial candidate studies and datasets identified
- [ ] Structured literature review completed
- [ ] Dataset access, labels, languages, and metadata verified
- [ ] Protocol and analysis plan prespecified
- [ ] Reproducible baseline implemented
- [ ] Generalization and bias analyses run
- [ ] Manuscript drafted from actual results

See [docs/PROGRESS.md](docs/PROGRESS.md), [docs/LITERATURE_REVIEW_PLAN.md](docs/LITERATURE_REVIEW_PLAN.md), and [docs/DATASET_AUDIT.md](docs/DATASET_AUDIT.md).

## Principles
- No fabricated data, results, citations, or novelty claims.
- Split by participant, not recording, whenever participant IDs permit.
- Keep raw audio, restricted data, credentials, and identifying information out of Git.
- Document dataset versions, licenses, exclusions, preprocessing, seeds, and software versions.
- Distinguish exploratory from prespecified confirmatory analysis.
- This is research software, not a clinically validated diagnostic tool.

## Planned structure
- `docs/`: research log, protocol, dataset audit, literature screening
- `references/`: citation exports and search strategy
- `src/`: reusable preprocessing and modelling code
- `notebooks/`: exploratory analysis
- `tests/`: validation and leakage checks
- `results/`: reproducible outputs after experiments
- `manuscript/`: paper drafts and reporting checklist

## First milestone
Complete a structured literature audit and dataset feasibility audit before choosing the final research question or training models.


## Research decision update — 2026-10-25

The targeted prior-art update found direct overlap with cross-corpus transfer, uncertainty-aware voice assessment, target-data adaptation and general label-free clinical-AI monitoring (including SUDO and D3M). The current candidate is a **comparative benchmark of existing label-free monitoring methods for Parkinson's voice AI**, not a claim of a new general-purpose OOD/abstention method.

- [Updated prior-art review](docs/UPDATED_PRIOR_ART_REVIEW_2026-10-25.md)
- [Dataset feasibility and independence gate](docs/DATASET_FEASIBILITY_GATE.md)
- [Revised Route A proposal](docs/ROUTE_A_LABEL_FREE_RELIABILITY_PROPOSAL.md)
- [Primary-study comparison matrix](docs/PRIMARY_STUDY_COMPARISON_MATRIX.md)
- [Progress ledger](docs/PROGRESS.md)

**Current blocker:** at least three independent, legally accessible cohorts are not yet verified. No models have been trained and no new experimental results are claimed.
