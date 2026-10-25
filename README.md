# Parkinson's Voice AI Research

**Status (25 Oct 2026):** targeted novelty review and file-level archive audits completed for three candidate corpora. Participant/diagnosis validation and third-cohort access remain open; no model experiments or clinical performance claims have been produced.

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
- [x] Basic archive integrity and WAV-header audits completed for IPVS, UAMS and MDVR-KCL
- [ ] Participant-level label/provenance, privacy/governance, and repeated-session checks completed
- [ ] Third independent task-compatible cohort lawfully accessed and audited
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

**Current blocker:** archive/file integrity has passed for IPVS, UAMS and MDVR-KCL via [GitHub Actions run 40175159872](https://github.com/culprit-k/parkinsons-voice-ai/actions/runs/40175159872), but three compatible independent cohorts are not yet approved. IPVS participant/session mapping and direct-identifier governance remain unresolved; UAMS diagnosis provenance and participant independence need confirmation; MDVR-KCL participant-label mapping remains open and its connected-speech task is not matched to sustained /a/. No model has been trained and no new experimental results are claimed.


See also the [targeted search log](docs/TARGETED_SEARCH_LOG_2026-10-25.md), which records the queries and source types actually checked to date.


## Final research decision (2026-10-25)

The broad generic “label-free monitoring/abstention” idea is not a new method. The current candidate is a narrower participant-level external-error benchmark for sustained-vowel PD voice screening. This remains a conditional research direction, not a cleared novelty claim; third-cohort access and participant-ID validation are still needed.

- [Final research decision and proposed design](docs/FINAL_RESEARCH_DECISION_2026-10-25.md)
- [Updated prior-art review](docs/UPDATED_PRIOR_ART_REVIEW_2026-10-25.md)
- [Dataset feasibility gate](docs/DATASET_FEASIBILITY_GATE.md)
- [Targeted search log](docs/TARGETED_SEARCH_LOG_2026-10-25.md)


## Final design clarification

The current sustained-/a/ pilot is a cross-dataset/recording-domain study, not an isolated language-generalization experiment. See the [final decision memo](docs/FINAL_RESEARCH_DECISION_2026-10-25.md), [dataset gate](docs/DATASET_FEASIBILITY_GATE.md) and [targeted search log](docs/TARGETED_SEARCH_LOG_2026-10-25.md).


## Selected research direction

**Question:** Does adding source-reference acoustic-domain distance to predictive confidence improve participant-level detection of wrong PD voice-screening predictions on independent held-out cohorts?

This is a focused comparison of existing signals, not a claimed new general-purpose method. The 2026 PARK multimodal screening study already evaluates uncertainty–performance relationships, so our candidate must test the incremental value of voice-specific acoustic distance beyond confidence. Data and novelty gates remain open.

- [Selected research question and draft protocol](docs/SELECTED_RESEARCH_QUESTION.md)
- [Final research decision](docs/FINAL_RESEARCH_DECISION_2026-10-25.md)


## Current gate status (2026-10-25)

**Protocol remains unlocked; data gate not passed.** Archive integrity and audio-header checks have now passed for IPVS, UAMS and MDVR-KCL through a network-enabled runner, but participant-level diagnosis validity and a third task-compatible independent cohort remain unverified. EWA-DB is the prioritized access request, with mPower as a fallback; neither is approved or accessed. A close-overlap public repository already reports IPVS/MDVR-KCL shortcut and cross-corpus work, and recent BUCC 2026 work directly studies Parkinson speech-corpus comparability. Novelty is not cleared.

- [Actual archive-integrity and data-gate audit](docs/FINAL_NOVELTY_AND_DATASET_AUDIT_2026-10-25.md)
- [Third-cohort search and draft access requests](docs/THIRD_COHORT_AND_ACCESS_REQUEST_PLAN_2026-10-25.md)
- [Current remaining blockers issue](https://github.com/culprit-k/parkinsons-voice-ai/issues/2)
