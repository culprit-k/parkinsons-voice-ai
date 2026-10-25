# Prior-art and dataset verification gate — 25 October 2026

## Status

**Protocol: NOT LOCKED. Model development: NOT STARTED.**

This document records the targeted prior-art search and dataset findings as of 25 October 2026. Raw archives for IPVS, UAMS and MDVR-KCL have now been downloaded and checked through the network-enabled [GitHub Actions run](https://github.com/culprit-k/parkinsons-voice-ai/actions/runs/40170614840). File integrity/audio-header checks are partly passed, but **no cohort is fully approved for the planned analysis** until participant mapping, diagnostic provenance, task compatibility, privacy and a third independent compatible cohort are resolved.

## A. Updated prior-art verdict

### 1. The current question is narrower, but still provisional

Candidate question:

> Does adding a source-reference acoustic-domain distance score to predictive confidence improve participant-level detection of wrong Parkinson's voice-screening predictions on independent held-out cohorts?

The distinction is the *incremental value* of acoustic distance beyond confidence, evaluated on participant-level external errors. It is not a claim to invent OOD detection, uncertainty estimation, selective prediction, or cross-corpus validation.

### 2. Direct and near-direct prior art

| Prior work | Overlap | Consequence |
|---|---|---|
| Ando et al., ParkMAE (2025/2026), four evaluation corpora and four languages, including ItalianPVS, MDVR-KCL, EWA-DB and NeuroVoz. [Scientific Reports](https://www.nature.com/articles/s41598-025-30251-7) | Cross-linguistic external evaluation; multiple feature/model baselines; public datasets/code claims. | Cross-language model evaluation is not new. Its weak cross-linguistic F1 (reported mean about 0.39) also cautions against equating a large architecture with high generalization. |
| Hireš et al. (2023), four datasets with sustained-vowel phonation. [ScienceDirect](https://www.sciencedirect.com/science/article/pii/S1386505623002551) | Directly studies inter-dataset generalization and performance degradation. | Cross-dataset testing itself is established. |
| Hossain et al. (2026), cross-corpus consensus acoustic features and a dual-stream architecture. [Scientific Reports](https://www.nature.com/articles/s41598-026-76171-y) | Cross-corpus features, multilingual PD detection, external testing, calibration-related metrics. | Feature stability plus cross-corpus classification is close adjacent work; avoid presenting it as novel. |
| Guo et al. (2026), uncertainty-aware voice assessment with Spanish-to-Italian evaluation. [Springer](https://doi.org/10.1007/s40846-026-01040-y) | Voice-specific uncertainty and cross-language external validation. | Uncertainty-aware voice assessment is established. |
| PARK remote multimodal screening (2026), 1,865 participants across eight studies; speech, face and motor tasks; uncertainty and calibration; performance decreases in higher-uncertainty bins. [Communications Medicine/PMC](https://pmc.ncbi.nlm.nih.gov/articles/PMC13586151/) | Directly evaluates uncertainty–performance relationships and external cohorts, although it is multimodal and not the same voice-only acoustic-distance comparison. | “Uncertainty predicts errors” is not an independent contribution. Test only incremental value beyond confidence and acknowledge this study explicitly. |
| Weng et al. (2025), medical OOD detection/risk control including Parkinson-related smartphone activity data (not voice). [PubMed](https://pubmed.ncbi.nlm.nih.gov/41127928/) | OOD detection and error-risk control in medical ML. | General OOD detection is prior art. |
| SUDO (2024), clinical-AI reliability without ground-truth target labels. [Nature Communications](https://www.nature.com/articles/s41467-024-46000-9); D3M (NeurIPS 2025), deployment-stream monitoring. [NeurIPS](https://proceedings.neurips.cc/paper_files/paper/2025/hash/0bb251eba663f0345c0929f5bbbfb6dc-Abstract-Conference.html) | Label-free reliability monitoring. | The method family is not new. |
| Public repository, *Parkinson-Voice-Detection* (created 2026-09-12, updated 2026-09-26), uses IPVS and MDVR-KCL, acoustic-shortcut/silence controls, eGeMAPSv02, channel normalization, leave-one-corpus-out nested CV, calibration and demographic checks. [GitHub](https://github.com/BennedictQuanTon/Parkinson-Voice-Detection) | Extremely close to the proposed corpus pair and several robustness/audit methods. It reports results, but we have not independently reproduced them or verified every assertion. | **Major overlap warning.** Do not reuse the same IPVS–MDVR-KCL cross-corpus audit as the headline contribution. Treat its results as a prior-art claim to independently inspect, not as verified ground truth. |
| Twala (2026), reproducibility report for Oxford/Sakar datasets. [ScienceDirect](https://www.sciencedirect.com/science/article/pii/S2666521226001572); [Zenodo](https://zenodo.org/records/22735799) | Participant-level evaluation, leakage checks, cross-dataset transfer, subgroup errors and confidence intervals. | Basic leakage/cross-dataset reproducibility work is already being published. |

### 3. Novelty decision

**Not cleared.** The narrow incremental question—whether a prespecified acoustic-distance score improves error detection beyond confidence on held-out PD voice cohorts—remains potentially useful, but a targeted search is not a novelty certificate. Before protocol lock, complete database searches (PubMed/MEDLINE, Europe PMC, IEEE Xplore, Scopus/Web of Science if available, ACM DL, arXiv and relevant conference proceedings), plus backward/forward citation chaining for the closest papers above. Search terms must combine voice/acoustics, domain shift/OOD, confidence/error prediction, selective prediction/abstention and Parkinson's disease.

A genuinely new complex mathematical architecture is **not justified yet**. Complexity does not guarantee accuracy, generalization, or clinical utility. First establish the data are valid and identify a contribution that remains after prior-art review. If the incremental question is already covered, change the question before modelling.

## B. Dataset verification status

### Status legend
- **Metadata confirmed:** public catalogue/paper reports the stated contents.
- **Archive integrity verified:** archive downloaded and checksum validated.
- **Manifest verified:** sample-level IDs, labels, repeated recordings, task and metadata inspected locally.
- **Approved for analysis:** licence/access, provenance, IDs and task are adequate for the planned endpoint.

No candidate currently meets all four stages in this project.

| Candidate | What public metadata currently says | Open issues | Current status |
|---|---|---|---|
| **ItalianPVS/IPVS** | Public mirror declares CC BY 4.0; 831 WAV + 6 XLSX + 1 TXT were extracted; the ZIP SHA-256 matched the pinned mirror and all 831 WAV headers were readable. [Official IEEE DataPort record](https://ieee-dataport.org/open-access/italian-parkinsons-voice-and-speech); [mirror listing](https://huggingface.co/datasets/birgermoell/Italian_Parkinsons_Voice_and_Speech/tree/main/italian_parkinson) | One exact duplicate-audio pair found. A spreadsheet includes direct name/surname fields; no names were copied into the repository. Participant/session and label mapping remain unresolved; no name-to-audio link should be attempted without governance approval. | **Archive/audio QC PASS; participant/privacy gate OPEN.** |
| **UAMS telephone prolonged-/a/ recordings** | Figshare source files downloaded individually; all published per-file MD5 checks passed; 81/81 WAV headers readable; 81 unique Sample IDs; 41 HC / 40 PwPD; 81/81 ID-to-filename matches. [Figshare record](https://figshare.com/articles/dataset/Voice_Samples_for_Patients_with_Parkinson_s_Disease_and_Healthy_Controls/23849127) | Need verify diagnosis provenance and whether each sample ID is an independent participant/no repeated visits. | **File integrity and filename linkage PASS; clinical provenance/independence OPEN.** |
| **mPower** | Large remote cohort with smartphone sustained /a/ recordings; published work reports extensive voice recordings. [Scientific Data](https://www.nature.com/articles/sdata201611) | Research access procedures, exact version/terms, participant IDs, repeat recordings, missingness, diagnostic-field provenance and whether the label is self-reported must be verified. Cohort is not assumed open or approved. | **Access/label audit required.** |
| **MDVR-KCL** | Zenodo source file downloaded; published MD5 matched; 73 readable mono WAVs at 44.1 kHz; no exact duplicate hashes. [Zenodo](https://zenodo.org/records/2867216) | Raw participant/diagnosis label mapping remains unverified. Tasks are read text and spontaneous dialogue, not sustained vowel. It overlaps directly with public prior art on cross-corpus auditing. | **File integrity PASS; participant/label gate OPEN; connected-speech only.** |
| **NeuroVoz** | Spanish speech corpus; latest Zenodo version reports 112 participants and 2,977 files. [Zenodo](https://zenodo.org/records/12517368) | Access marked restricted; ensure approval, exact version and label/task manifest. | **Restricted; request/approval needed.** |
| **EWA-DB** | Slovak corpus with multiple diagnostic groups; audio availability restricted to a consented subset and terms apply. [ELRA catalogue](https://catalogue.elra.info/en-us/repository/browse/ELRA-S0489/) | License/EULA, subset counts, labels and accessible audio manifest require confirmation. | **Request/approval needed.** |
| **UNLaM / Spanish Parkinson Voice Database** | Referenced by recent work as a Spanish dataset. | Exact downloadable raw-audio version, license, sample IDs and a reported cohort-size discrepancy (119 vs 126) remain unresolved. Do not count it as an independent third cohort yet. | **Unverified lead.** |
| **Bridge2AI Voice** | Multi-site resource with rich speech metadata and derived features; raw audio requires additional access controls. [PhysioNet](https://www.physionet.org/content/b2ai-voice/4.0.0/) | Need credentialed access, DUA, raw-audio sign-off where relevant, version-specific cohort and task/diagnosis subset audit. | **Potential alternative; not currently approved.** |

### Dataset gate outcome

**FAIL / NOT YET PASSED.** This means no confirmatory modelling or protocol lock. It does not mean these datasets are invalid; it means this project has not yet performed the local archive and manifest checks needed to establish that they are valid for this exact study.

### Required local audit checklist

For each candidate cohort, create a versioned manifest containing:
1. Official source URL, version/date, license/access terms and citation.
2. Archive filename, byte size, SHA-256 and download date.
3. Number of files, audio format, sample rate, channel count, duration distribution and corrupt/unreadable files.
4. Participant-level ID mapping and number of unique participants versus recordings/sessions.
5. Repeated recordings, repeat visits and potential overlap between cohorts.
6. Diagnosis definition/provenance, label missingness, disease group and control selection.
7. Task identity (sustained vowel, reading, spontaneous speech), recording device/site/environment where available.
8. Age/sex completeness, subgroup counts, and whether PD/control labels are confounded with dataset or recording batch.
9. Inclusion/exclusion log and reasons, without modifying the source archives.
10. Explicit analysis decision: approved, approved only for sensitivity analysis, restricted, or rejected.

Do not use a dataset's paper-reported counts as if they were verified manifest counts. Do not combine cohorts merely because they have WAV files and a PD/control label.

## C. Revised sequence of work

1. Finish the systematic novelty search and citation-chain review.
2. Obtain lawful access to candidate datasets.
3. Download only to a separate raw-data directory; never commit patient audio to GitHub.
4. Verify checksums and build manifests; audit repeated participants and labels.
5. Decide whether the cohorts genuinely support the same endpoint and whether there are enough independent cohorts.
6. Select the study question only after comparing the final evidence map with the verified dataset matrix.
7. Write and lock a prespecified protocol and analysis plan.
8. Only then train a baseline; develop a more complex model only if a justified gap remains and the baseline/data support it.

## D. What has and has not been done

Completed in this pass:
- Targeted web search for cross-language PD speech, OOD/error detection, uncertainty, acoustic shortcuts and dataset access.
- Inspection of public paper/catalogue metadata for candidate datasets.
- Identification of direct prior-art overlap with a public cross-corpus acoustic-shortcut repository.
- Explicit decision to keep the protocol unlocked.

Not completed:
- Exhaustive systematic database search and citation chaining.
- Download, SHA-256 verification, unpacking or local audio QC of candidate datasets.
- Participant-ID/label manifest audit.
- Model training, results or performance comparisons.

These boundaries are deliberate: they prevent a paper from making unsupported claims.


## Addendum: raw archive checks completed — 25 October 2026

The earlier status above that raw archives had not been downloaded is superseded by the completed [GitHub Actions audit](https://github.com/culprit-k/parkinsons-voice-ai/actions/runs/40170280356).

- IPVS archive SHA-256 was recomputed locally and matches the pinned mirror. Extracted inventory: 831 WAV, 6 XLSX, 1 TXT. All WAV headers readable; mono; 671 at 16 kHz and 160 at 44.1 kHz. Folder-level counts: 437 PD-labelled, 349 elderly-control-labelled and 45 young-control-labelled recordings. One exact duplicate pair was detected. Participant-level mapping remains unresolved, and a workbook contains direct name/surname fields; treat this as a data-governance and privacy blocker for demographic linkage.
- UAMS files were downloaded individually through the public Figshare API. Available per-file MD5 checks passed. There are 81 readable mono WAVs at 8 kHz and one workbook. The Parselmouth sheet has 81 unique Sample IDs, labels 41 HC / 40 PwPD, and all 81 IDs match audio filenames.
- The raw-file gate is now partially passed for IPVS and UAMS. Overall feasibility is still NOT PASSED because IPVS unique-participant/label mapping and duplicate adjudication remain open, UAMS diagnostic provenance/participant independence need confirmation, and a third independent compatible cohort is not established.
- No model was trained; no predictive results exist. Protocol remains NOT LOCKED.


## Addendum: three archive audits and final compatibility decision

The raw archives for IPVS, UAMS and MDVR-KCL were downloaded and inspected through the successful [GitHub Actions run](https://github.com/culprit-k/parkinsons-voice-ai/actions/runs/40170614840).

- IPVS: checksum matched; 831 readable mono WAVs (671 at 16 kHz, 160 at 44.1 kHz), plus 6 XLSX and 1 TXT. Path categories contain 437 PD, 349 elderly-control and 45 young-control recordings. One exact duplicate pair occurs within the same parent directory under a PD-labelled path. Participant-level mapping remains unresolved. A workbook contains name/surname fields, so privacy/governance must be addressed before demographic linkage.
- UAMS: per-file MD5 checks passed; 81 readable mono WAVs at 8 kHz. Its Parselmouth sheet contains 81 unique Sample IDs, 41 HC / 40 PwPD, and all 81 IDs match audio filenames. No exact duplicate hashes.
- MDVR-KCL: Zenodo MD5 matched; 73 readable mono WAVs at 44.1 kHz, 73.04–220.64 seconds, no exact duplicate hashes. The raw participant/label manifest has not been verified. The literature describes read-text and spontaneous-dialogue tasks.

Three corpora have now passed basic file-level download and audio-header checks, but this is not three compatible cohorts. UAMS is sustained /a/; MDVR-KCL is connected speech; IPVS contains multiple tasks but participant-level mapping is not cleared. NeuroVoz, a potential Spanish connected-speech cohort, is marked restricted at Zenodo and is not available for this audit without access approval. Overall data gate remains NOT PASSED; protocol remains NOT LOCKED.

Novelty note: recent 2026 work on limited-target-data calibration reports cross-dataset transfer using a dataset set that includes IPVS, MDVR-KCL and a US sustained-"ah" cohort, further narrowing any claim that cross-dataset calibration/transfer itself is new. Our candidate remains, at best, a narrow comparative evaluation of error ranking by confidence versus confidence plus acoustic distance, pending a more complete citation-chain search.


## Current access decision — 25 October 2026

The prioritized third-cohort request is EWA-DB (ELRA-S0489), whose catalogue describes sustained-vowel phonation and a WAV subset from speakers who provided written consent. It is a request candidate, not yet available to this project. mPower is a second sustained-vowel route through Synapse, but requires a validated research account, data-use statement and terms agreement; PD labels may be self-reported. NeuroVoz v3 is restricted at Zenodo, and PC-GITA is another request-mediated alternative. The [third-cohort/access plan](THIRD_COHORT_AND_ACCESS_REQUEST_PLAN_2026-10-25.md) records source evidence and draft permission requests.

No model has been trained and no empirical prediction results exist. The narrow comparative question remains conditional; the overall data gate and novelty gate are **NOT PASSED**, and the protocol remains **NOT LOCKED**.