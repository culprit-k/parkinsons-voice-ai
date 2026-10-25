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

- Final search refinement found a Jan 2026 confidence-gated PD voice ensemble and a Feb 2026 uncertainty-based speech-domain shift detector. They are adjacent rather than exact matches for the candidate error-ranking endpoint, but further narrow the defensible contribution to a comparative validation study.


## 2026-10-25 — Raw archive verification completed

- Added a network-enabled GitHub Actions workflow because the local runtime could not resolve dataset hosts. The successful audit is https://github.com/culprit-k/parkinsons-voice-ai/actions/runs/40170280356. Only a sanitized aggregate report was uploaded; raw audio and participant paths were not published as artifacts.
- IPVS: local SHA-256 matched the pinned mirror. Archive extracted to 831 WAV, 6 XLSX and 1 TXT. All 831 WAV headers were readable and mono; 671 at 16 kHz, 160 at 44.1 kHz. Folder-level label counts are 437 PD, 349 elderly controls and 45 young controls. One exact duplicate pair was found. Participant-level mapping remains unresolved; a spreadsheet contains direct name/surname fields, creating a privacy/governance blocker for demographic linkage.
- UAMS: individual source files downloaded via Figshare API; per-file MD5 checks passed. Inventory contains 81 readable mono 8-kHz WAVs plus one workbook. The Parselmouth sheet has 81 unique IDs, 41 HC / 40 PwPD labels, and 81/81 ID-to-audio filename matches. No exact duplicate audio hashes were found.
- Overall data gate remains NOT PASSED: IPVS duplicate and participant mapping are unresolved; UAMS diagnostic provenance and independent-participant status need confirmation; third independent compatible cohort not established.
- No model training or empirical prediction evaluation has occurred; protocol remains NOT LOCKED.


## 2026-10-25 — MDVR-KCL verification and three-corpus decision

- Added MDVR-KCL via Zenodo API to the archive-audit script and workflow. In successful run https://github.com/culprit-k/parkinsons-voice-ai/actions/runs/40170614840, the 606,144,431-byte source file matched Zenodo's MD5. The archive yielded 73 readable mono WAV files at 44.1 kHz, durations 73.03902–220.63916 seconds, with no exact duplicate audio hashes.
- MDVR-KCL participant IDs and raw file-to-label mapping were not verified. Its connected-speech tasks are not directly task-matched to UAMS sustained /a/.
- Three raw corpora have passed basic file-level download/audio-header checks (IPVS, UAMS, MDVR-KCL), but three compatible independent participant cohorts have NOT been established.
- IPVS duplicate pair is in the same parent directory under a PD-labelled path; whether it is a duplicate file or repeated take remains unresolved. IPVS spreadsheets include name/surname columns, requiring privacy/governance review before any demographic linkage.
- NeuroVoz is a promising Spanish connected-speech corpus but Zenodo lists its files as restricted; no access has been granted.
- Novelty remains conditional: 2026 limited-target calibration work uses overlapping datasets, so the only defensible candidate is a prespecified comparative evaluation of confidence-only versus confidence-plus-acoustic-distance error ranking, not a new general algorithm.
- No model trained; no empirical prediction results; protocol not locked.


## 2026-10-25 — Third-cohort search and verification-tool hardening

- Confirmed the three-dataset GitHub Actions run 40170614840 completed successfully and downloaded the sanitized result artifact for review. IPVS SHA-256 matched its pinned mirror; UAMS per-file MD5 checks and 81/81 sample-ID-to-filename matches passed; MDVR-KCL Zenodo MD5 matched. All WAV headers were readable for the three audited releases.
- Hardened the spreadsheet audit in scripts/verify_voice_dataset_archives.py: workbook ID-to-audio matching now uses exact normalized filename stems instead of permissive suffix/sub-string matching; aggregate counts include duplicate ID rows and IDs with conflicting labels without printing identifier values.
- Added docs/THIRD_COHORT_AND_ACCESS_REQUEST_PLAN_2026-10-25.md with an evidence-based shortlist, the EWA-DB priority request, mPower fallback steps, NeuroVoz permission request, and access/approval promotion criteria.
- Third-cohort search: EWA-DB is the priority request because the catalogue lists sustained-vowel phonation and a consented audio subset; mPower is the next sustained-vowel candidate through Synapse; NeuroVoz v3 is restricted; PC-GITA is request-mediated; UNLaM has an unresolved cohort/version count discrepancy. No external request has been sent and no access has been granted.
- The overall data gate remains NOT PASSED: IPVS participant/session mapping and PII governance are open; UAMS label provenance and participant independence are open; MDVR-KCL participant-label mapping is open and its task differs; a third compatible cohort is not yet approved. No model has been trained, no results exist, protocol remains NOT LOCKED.

## 2026-10-25 — Final verification rerun and blocker tracking

- Hardened workbook join logic to require exact normalized filename-stem matches, and added privacy-safe aggregate checks for duplicate sample-ID rows and conflicting labels. The latest workflow run [40175159872](https://github.com/culprit-k/parkinsons-voice-ai/actions/runs/40175159872) completed successfully; its sanitized artifact reports UAMS 81 unique Sample IDs, 81/81 filename matches, zero unmatched IDs, zero duplicate-ID rows and zero conflicting-label IDs in the Parselmouth sheet. It contains no sample ID values or private file paths.
- Reconciled the IPVS public mirror listing: the downloaded ZIP extracts to 831 WAV + 6 XLSX + 1 TXT = 838 files; the mirror's 839-item list includes the ZIP itself. One exact duplicate-audio pair remains for source-level adjudication; this is separate from the one-item listing difference.
- Updated README and core data/novelty docs to distinguish completed file-integrity checks from unresolved clinical/participant-level gates.
- Opened [Issue #2: Remaining data-gate blockers before protocol lock](https://github.com/culprit-k/parkinsons-voice-ai/issues/2) as a checklist for custodian/governance review, UAMS label provenance, MDVR mapping, third-cohort access and novelty completion.
- Drafted EWA-DB and NeuroVoz permission-request emails in the access-plan document. No email or access request was sent, no restricted data were accessed, and no terms were accepted on the user's behalf.
- Current decision remains **HOLD confirmatory modeling**: a third independent task-compatible cohort is not available/approved; IPVS mapping/privacy and UAMS clinical provenance remain open; MDVR-KCL task and label mapping are not fit for the primary sustained-vowel analysis. No model or empirical prediction results exist.


## 2026-10-25 — Additional distance-based audio OOD prior-art check

- Ran focused searches for the specific PD-voice question and for audio feature-distance/error-detection methods. Added Bukhsh & Saeed (ICASSP 2023) on deep k-nearest-neighbour distance for OOD audio, Yilmaz & Toraman (NAACL 2022) on distance-to-uniform out-of-scope detection, Sony Research's 2024 audio-disease uncertainty plus latent-distance framework, and a 2026 medical-imaging failure-detection benchmark to the targeted search log and prior-art review.
- This strengthens the novelty boundary: feature distance, confidence, uncertainty, audio OOD detection and comparative failure ranking are established method families. No exact match was found in this query pass for the specific participant-level confidence-only versus confidence-plus-distance comparison on held-out PD-voice cohorts; this is not evidence of universal absence.
- The candidate question remains only a prespecified empirical comparison on independent PD-voice cohorts. A full database/citation-chain review is still required before novelty clearance; no new general OOD detector is justified.
- The sanitized final workflow run [40175159872](https://github.com/culprit-k/parkinsons-voice-ai/actions/runs/40175159872) succeeded. The public report includes aggregate match-quality fields and no sample ID values/private paths.
- [Issue #2](https://github.com/culprit-k/parkinsons-voice-ai/issues/2) tracks the remaining dataset, governance, access and protocol gates. No emails were sent and no external access approval was obtained.

## 2026-10-25 — UAMS source-provenance review and correction check

- Read the 2025 peer-reviewed study that uses the public UAMS telephone-vowel archive and the August 2026 author correction to its 2023 precursor study.
- Diagnosis-source asymmetry is now documented rather than left wholly unresolved: the UAMS PD participants were professionally diagnosed by a movement-disorders neurologist; healthy controls were not neurologically examined and self-reported relevant voice/neurological/psychiatric conditions.
- The analysed 81-record UAMS subset (40 PD / 41 HC) was obtained after excluding recordings shorter than 1.5 seconds after trimming; its mean ages were 66.6 ± 9.0 years for PD and 47.9 ± 14.5 for HC. This is a major potential age shortcut, so any future model comparison must include an age-only baseline and appropriate sensitivity analysis.
- The August 6, 2026 correction states that a CNN-pipeline implementation issue in the 2023 UAMS paper required revising the reported CNN mean AUC from 0.97/0.96 to 0.83/0.83. We must cite the correction and avoid repeating superseded figures as valid results.
- Still open: document one independent participant per released Sample ID/no repeat visits; determine whether a sensible age-restricted analysis leaves a sufficiently powered sample. This is a data/design limitation, not a reason to hide the cohort.
