# Research progress ledger

Last updated: 2026-10-25

## Status summary

| Workstream | Status | Next action |
|---|---|---|
| Topic selection | Complete | Voice-based Parkinson's research selected |
| Broad objective | Complete | Cross-language generalization, demographic bias, robustness |
| Preliminary literature discovery | In progress | Expand targeted search into a reproducible multi-database search |
| Structured literature review | Not complete | Record exact searches, deduplicate, screen, and extract all eligible studies |
| Dataset audit | Preliminary audit complete | Verify current access terms, licenses, participant IDs, labels, and metadata for candidate releases |
| Research protocol | Provisional hypothesis only | Finalize after prior-art and dataset feasibility gates |
| Code and environment | Not started | Implement only after protocol/data gates |
| Experiments | Not started | No model results currently available |
| Manuscript | Not started | Draft after review; results only after real experiments |

## Decisions
1. Cross-language modeling, cross-corpus feature stability, demographic-only baselines, target-data adaptation, participant-level splitting, uncertainty quantification and probability calibration all have prior art; none alone is our novelty claim.
2. The candidate Route A idea overlaps conceptually with SUDO (label-free evaluation/identification of unreliable predictions) and general selective classification/OOD risk control.
3. Any defensible contribution should be framed as a rigorous PD-voice comparative benchmark of unlabeled-target warning signals versus observed external failure, not as a new general method, unless further prior-art search supports a narrower claim.
4. Include demographic-only baselines and confounding checks where metadata permit.
5. Prefer independent external evaluation where compatible datasets permit.
6. Use participant-level splitting to prevent leakage where IDs permit.
7. Report uncertainty and limitations; do not overstate clinical readiness.

## Candidate resources (not approved yet)
- Bridge2AI-Voice: verify exact release, variables, data-use requirements, raw versus derived access.
- NeuroVoz: verify original paper, availability, protocol, and metadata.
- Oxford/UCI Parkinson's voice datasets: identify exact version and verify participant IDs, repeated-measure structure, language and recording context.

Do not assume these resources are mutually compatible. Do not claim cross-language evidence unless language and collection details are documented.

## Next actions
- [ ] Build literature search log and screening table.
- [ ] Verify bibliographic records from original publisher/repository pages.
- [ ] Create dataset compatibility matrix.
- [ ] Decide feasibility with available public data and metadata.
- [ ] Version the protocol before confirmatory model training.

## Change log
- 2026-10-25: Initialized from project conversation. No experiments or manuscript results claimed.
- 2026-10-25: Added preliminary Route A hypothesis and data-access cautions.
- 2026-10-25: Added a targeted prior-art audit. Found substantial conceptual overlap with SUDO and general selective/OOD methods; the proposed PD-voice benchmark remains a conditional hypothesis, not a cleared novelty claim. No experiments performed.


## 2026-10-25 — Expanded prior-art and dataset-independence audit

- Added docs/UPDATED_PRIOR_ART_REVIEW_2026-10-25.md with direct PD overlap (September 2026 LODO paper; May 2026 target-data adaptation and sex-specific FNR; October 22 cross-corpus consensus-feature work; June 2026 uncertainty-aware Spanish-to-Italian study) and general label-free monitoring methods (SUDO, D3M, selective classification, label-free confusion-matrix estimation).
- Identified a public September 2026 repository claiming an acoustic-shortcut/silence-only audit and IPVS/MDVR-KCL cross-corpus model. Its reported results have not been independently reproduced here, but it is material public prior art and reduces the value of repeating that project.
- Revised the candidate to a comparative benchmark of existing **participant-level error-ranking/selective-prediction** and **batch/domain-level degradation-monitoring** methods. These are separate tasks and must not be mixed into one endpoint.
- Added docs/DATASET_FEASIBILITY_GATE.md. At least three independent, legally accessible cohorts are required for the intended benchmark; four are preferred. The data gate is not passed: MDVR-KCL and ItalianPVS are candidates but have not yet undergone local integrity checks; UNLaM has a count/version discrepancy; PC-GITA, NeuroVoz and EWA-DB require access verification; Bridge2AI v3/v4 overlap.
- Updated Route A to version 0.2 and the primary-study matrix with new close-overlap papers and methods.
- No local dataset download, model training, or experimental validation was performed in this update. No performance results are claimed.


## 2026-10-25 — Second search pass and source-version verification

- Added Siniukov et al. (2025) on HuBERT-based multilingual domain adaptation, Ibarra et al. (2023) on corpus/language-independent screening, Francesconi et al. (2026) on fairness-aware partial-label domain adaptation, DAT-PD (2026) on severity trajectories, and the 2025 systematic review of 69 studies to the prior-art record.
- Created docs/TARGETED_SEARCH_LOG_2026-10-25.md to distinguish searches actually run from the planned full systematic search. The current evidence retrieval was web-based and targeted; it is not represented as a completed database systematic review.
- Verified that NeuroVoz counts depend on release: current v3 reports 112 participants (54 PD / 58 controls; 2,977 recordings), while v1.0.0 reports 108 (53 PD / 55 controls; 2,903 recordings). Both records mark files as restricted. Count/version and access must be logged in the dataset manifest.
- No models trained. No audio downloaded. No target labels or performance metrics created.


## 2026-10-25 — Final research-direction decision after deeper prior-art/data search

- Added docs/FINAL_RESEARCH_DECISION_2026-10-25.md: conditional-go decision, revised primary question, concise protocol sketch, prior-art verdict, data matrix and stop/go gates.
- Narrowed Route A v0.3 to per-participant error detection under held-out dataset shift. Batch-level monitoring (SUDO/D3M) is separate and secondary/exploratory only because there are few independent corpora.
- Found OOD risk-control studies in general medical ML and Parkinson-related smartphone movement data (not voice), plus a 2026 label-free PD face/voice screening preprint. This strengthens the view that no generic label-free/OOD novelty claim is warranted.
- Detailed a methodology limitation in the September 2026 LODO paper: it calls two aggregated results “subject-level” even though the methods say their unit for mPower/MDVR is recording, and it acknowledges segment-level validation and a single random seed. These are directly reported limitations, not proof that all external results are invalid.
- Added UAMS Figshare sustained-/a/ telephone-recorded audio as a second public raw-audio candidate alongside ItalianPVS. The exact participant manifest remains unaudited. A third independent cohort is not yet verified; mPower access/label provenance and UNLaM raw data availability remain open checks.
- Overall: **conditional GO** for a small task-matched feasibility pilot and completion of access/novelty gates; **HOLD** on confirmatory training and novelty claims until a third suitable cohort and participant IDs/labels are verified. No experiments or data downloads claimed.


## 2026-10-25 — Final targeted-query synthesis and design correction

- Added Hireš et al. (2023), which directly demonstrates inter-dataset performance degradation for sustained-vowel PD voice classification across four datasets; cross-corpus transfer itself is not a novelty claim.
- Added Zahir et al. (2026) single-center participant-wise model and its stated need for external/multicenter validation; added Su & Sun (2026) label-free face/voice screening and distinguished it from target-domain error monitoring.
- Updated mPower access details: sustained /a/ up to 10 seconds, Synapse research access, and potential dependence on self-reported professional diagnosis.
- Corrected the intended interpretation: ItalianPVS/UAMS sustained-/a/ comparisons test cross-dataset/recording-domain robustness, not isolated language generalization.
- No recordings downloaded, participant IDs/labels audited locally, or models trained. The data gate remains incomplete.


## 2026-10-25 — Single research direction selected

- Selected the most defensible current candidate: test whether source-reference acoustic-domain distance adds predictive value beyond classifier confidence for detecting participant-level errors on held-out PD voice datasets.
- This narrower claim explicitly accounts for the 2026 PARK multimodal study, which already connects prediction uncertainty to lower performance, and for established cross-corpus/OOD literature.
- The proposed contribution is an independent voice-only comparative validation of an existing signal, not a new general OOD algorithm. Novelty remains un-cleared pending systematic searching and citation chaining.
- Data gate remains open: ItalianPVS and UAMS are raw-audio candidates; mPower is a possible third cohort only after research access and diagnosis-label review. No data have been downloaded, no model trained and no results generated.


## 2026-10-25 — Novelty and dataset gate strengthened; protocol remains unlocked

- Found a major close-overlap public repository (created 2026-09-12; updated 2026-09-26) that already reports IPVS/MDVR-KCL cross-corpus acoustic-shortcut audits, silence controls, eGeMAPSv02, CMVN, LOCO nested validation, calibration and subgroup checks. Its empirical claims are not independently verified here, but it must be treated as prior art. Do not claim the same corpus pair/audit as our headline contribution.
- Re-reviewed ParkMAE (cross-linguistic multi-corpus evaluation), Hireš et al. (cross-dataset sustained vowels), Hossain et al. (cross-corpus feature stability), Guo et al. (voice uncertainty and Spanish-to-Italian evaluation), PARK (2026 multimodal uncertainty/external validation), SUDO/D3M and medical OOD risk-control work. The selected incremental question remains provisional; novelty is not cleared.
- Metadata-level dataset checks identified count/manifest discrepancies requiring local verification: ItalianPVS cohort and file counts vary across descriptions; a public mirror lists 839 uploaded files, while commonly cited reports say 831 recordings. UAMS metadata describes prolonged-/a/ files and a demographic key but the actual archive and IDs have not been audited. mPower requires access/label review.
- No raw audio archive has been downloaded, hashed, unpacked or locally audited. No model has been trained. No protocol has been locked.
- Added docs/PRIOR_ART_AND_DATASET_GATE_2026-10-25.md as the current source of truth for prior-art and dataset gate status.


## 2026-10-25 — Final targeted novelty and data integrity audit

- Added docs/FINAL_NOVELTY_AND_DATASET_AUDIT_2026-10-25.md with the final targeted novelty verdict, the close-overlap prior-art matrix and remote metadata findings separated from local raw-file verification.
- Broad novelty claims are rejected: cross-dataset/cross-language PD voice, acoustic shortcut auditing, demographic confounding analysis, uncertainty-aware screening and generic label-free reliability monitoring all have prior art.
- The narrow confidence-only versus confidence-plus-acoustic-distance error-ranking question remains a conditional comparative-validation study, not a cleared novel algorithm claim.
- Inspected the public Parkinson-Voice-Detection GitHub tree beyond its README: 183 entries include methods, phase scripts, notebooks, findings, tables/figures, dataset version notes and a model artifact. Its empirical numbers were not reproduced by this project, but it is material public prior art for IPVS shortcut controls and IPVS/MDVR-KCL cross-corpus evaluation.
- IPVS remote metadata displays a 593 MB ZIP and host-side SHA-256 3c4cd221345f7a81f0eeaceedf44dedbfd33b08ecd18ab5a3307edefcfbacfed. The mirror's 839-file listing does not reconcile with commonly documented 831 WAVs + six spreadsheets + the ZIP itself (838 items). This remains unresolved.
- UAMS Figshare metadata describes a 4.18 MB CC BY 4.0 archive of prolonged-/a/ WAVs linked to demographics; the associated literature reports 40 PD and 41 controls for the public subset. Actual archive bytes and workbook joins remain unverified.
- Network-enabled archive preflight against Hugging Face, Figshare and Zenodo fails with DNS resolution errors in this runtime. No raw audio was downloaded, no hash was recomputed locally, and no WAV or participant manifest was inspected locally.
- Added scripts/verify_voice_dataset_archives.py and .gitignore to support a later local audit without committing speech files/private manifests.
- Status remains: protocol NOT LOCKED; confirmatory modelling NOT STARTED; raw-data integrity gate NOT PASSED. Sustained-/a/ cohort comparison should be described as recording-domain robustness, not lexical cross-language generalization.
