# Selected research question — 25 October 2026

## Decision

**Selected direction:** a narrowly scoped, participant-level external-validation study testing whether acoustic-domain distance adds information beyond predictive confidence when identifying errors from Parkinson's disease (PD) voice-screening models.

This is the best current balance of scientific usefulness, possible independent contribution, public-data feasibility, and manageable computational requirements for an MBBS student without assumed patient access. It is **not** declared novel or publication-guaranteed. The literature search is targeted, not exhaustive, and data access has not yet passed its integrity gate.

## Selected working title

**Does Acoustic-Domain Distance Add Value to Confidence for Detecting Errors in Parkinson’s Voice Screening? A Participant-Level External Validation Study**

### Primary research question

> Among participant-level predictions made by a PD voice classifier trained on one cohort and tested on independent held-out voice cohorts, does adding a source-reference acoustic-distance score to predictive confidence improve detection of incorrect predictions?

### Clinical secondary question

At a prespecified coverage level, does the distance-augmented risk score reduce the proportion of wrong predictions that are still shown as eligible for automated screening, and are the deferred participants disproportionately drawn from any available age/sex subgroup?

Do not claim prospective safety. A “defer” result means the automated screen should not be presented as reliable; it is not a diagnosis or a substitute for clinical assessment.

## Why this question was selected

1. **It is narrower than the crowded topics.** Cross-language classification, cross-corpus transfer, feature stability, demographic confounding, calibration, uncertainty, OOD detection and abstention all have prior art. These will be comparators or context, not our novelty claim.
2. **It asks for an incremental test rather than a new algorithm.** The key comparison is confidence-only versus confidence plus a prespecified source-reference acoustic-distance signal.
3. **It is voice-specific.** The 2026 PARK remote-screening system already studies uncertainty and finds that performance falls in higher-uncertainty groups, but it fuses speech with facial and motor tasks. Our potential distinction is a voice-only, held-out-cohort comparison of *whether acoustic-domain distance adds beyond confidence*, not uncertainty alone. This exact distinction is not yet fully cleared by an exhaustive prior-art search.
4. **It can be tested with transparent baselines.** It does not require building a large neural network or collecting new patients.
5. **A null result remains informative.** Acoustic distance may identify unfamiliar recordings but fail to predict errors. That result would still be worth reporting if the design is prespecified and uncertainty is honest.

## What this study is not

- Not a claim to invent OOD detection, uncertainty estimation or selective prediction.
- Not another paper reporting a high random-split accuracy.
- Not proof of cross-language generalization from sustained vowels. A sustained /a/ task has no lexical content; comparisons across sites/languages also mix microphones, environment, task protocol, recruitment and demographics.
- Not a clinically validated diagnostic tool.
- Not yet a registered protocol or completed experiment.

## Literature boundary that shapes the question

- Cross-dataset PD voice generalization is established, including a four-dataset sustained-vowel study that reported degradation under external testing: Hireš et al. (2023), [PubMed](https://pubmed.ncbi.nlm.nih.gov/37801807/).
- Cross-corpus feature stability and held-out-language work are current, including Hossain et al. (2026), [Scientific Reports](https://www.nature.com/articles/s41598-026-76171-y).
- PD voice uncertainty and Spanish-to-Italian external testing already appear in Guo et al. (2026), [Springer](https://doi.org/10.1007/s40846-026-01040-y).
- The PARK remote multimodal screening study evaluates eight studies and reports lower model performance at higher prediction uncertainty. This is direct adjacent overlap that forces our comparison to go beyond confidence/uncertainty alone: [Communications Medicine (2026)](https://pmc.ncbi.nlm.nih.gov/articles/PMC13586151/).
- SUDO addresses label-free reliability estimation for clinical AI: [Nature Communications (2024)](https://www.nature.com/articles/s41467-024-46000-9). D3M studies label-free batch/deployment degradation monitoring: [NeurIPS 2025](https://proceedings.neurips.cc/paper_files/paper/2025/hash/0bb251eba663f0345c0929f5bbbfb6dc-Abstract-Conference.html).
- OOD risk control has also been studied in medical tasks including Parkinson-related movement/activity data rather than voice: [PubMed](https://pubmed.ncbi.nlm.nih.gov/41127928/).
- A September 2026 public repository describes acoustic-shortcut controls and IPVS/MDVR-KCL cross-corpus modelling: [GitHub](https://github.com/BennedictQuanTon/Parkinson-Voice-Detection). This is public prior art even though its numerical claims have not been independently reproduced here.

**Novelty verdict:** the specific incremental question may be independently useful, but is **plausible, not cleared**. The full database search and citation-chain review can still find direct overlap. Do not use “first,” “novel,” or “new to science” in the title/abstract without that evidence.

## Candidate data and feasibility

### Candidate cohorts after actual raw-file audit
- **ItalianPVS/IPVS:** the pinned public mirror archive SHA-256 matched; 831/831 WAV headers readable (671 at 16 kHz, 160 at 44.1 kHz). The extraction contains 831 WAV + 6 XLSX + 1 TXT. One exact duplicate-audio pair was found, and at least one spreadsheet contains direct name/surname columns. Participant/session/label mapping is unresolved; do not attempt name-to-audio linkage without governance review. [Official portal](https://ieee-dataport.org/open-access/italian-parkinsons-voice-and-speech).
- **UAMS telephone voice samples:** file-level MD5 checks passed; 81/81 8-kHz mono WAV headers readable; 81 unique Sample IDs, 41 HC / 40 PwPD, all 81 IDs matched audio filename stems. Clinical-label provenance and participant independence/repeated visits still need source confirmation. [Figshare record](https://figshare.com/articles/dataset/Voice_Samples_for_Patients_with_Parkinson_s_Disease_and_Healthy_Controls/23849127).
- **MDVR-KCL:** Zenodo MD5 matched; 73/73 44.1-kHz mono WAV headers readable. Its read-text and spontaneous-dialogue tasks are not matched to the sustained-/a/ primary task, and participant-to-diagnosis mapping remains unverified. [Zenodo record](https://zenodo.org/records/2867216).
- **Best third-cohort request:** EWA-DB (Slovak; ELRA-S0489), which catalogue metadata describe as having sustained-vowel tasks and WAV audio for a consented subset. Access, eligible PD/control recordings and label/ID mapping are not yet approved. [ELRA catalogue](https://catalogue.elra.info/en-us/repository/browse/ELRA-S0489/).
- **Second access route:** mPower sustained-/a/ recordings through Synapse research access; check data-use conditions, repeated observations and whether PD labels are self-reported. NeuroVoz v3 is restricted; PC-GITA is request-mediated; UNLaM counts/version need reconciliation. See [third-cohort and access request plan](THIRD_COHORT_AND_ACCESS_REQUEST_PLAN_2026-10-25.md).

### Data go/no-go
Raw audio archives for IPVS, UAMS and MDVR-KCL have been downloaded and passed basic archive/audio-header checks through GitHub Actions [run 40170614840](https://github.com/culprit-k/parkinsons-voice-ai/actions/runs/40170614840). This is not equivalent to three approved independent cohorts: IPVS participant/label mapping and privacy are unresolved, UAMS diagnostic provenance/independence needs confirmation, and MDVR-KCL lacks a verified participant-label map and is not task-matched to sustained vowels. The intended confirmatory benchmark requires at least **three independent, legally accessible task-compatible cohorts**. If only two clear the gate, call it a feasibility pilot and do not claim broad language generalization.

## Draft methods to lock only after the data gate

### Unit, splits and target-label firewall
- Unit of analysis and inference: participant. Never treat multiple files/segments from one speaker as independent cases.
- Train the classifier and fit all preprocessing on source participants only.
- Keep target cohort labels inaccessible while choosing features, model, confidence score, distance metric, normalization, thresholds and analysis code.
- Freeze the risk scores first; reveal target labels only to calculate external errors and evaluate scores.

### Baseline and candidate risk scores
1. **Classifier baseline:** regularized logistic regression on a prespecified harmonized acoustic feature set (e.g., pinned openSMILE eGeMAPSv02 extraction) with all standardization fitted on the source training set.
2. **Confidence-only risk score:** a fixed function of probability margin or entropy; select one primary definition before testing.
3. **Acoustic-distance risk score:** a prespecified distance from each participant's feature representation to the source-training reference distribution (e.g., robust standardized k-nearest-neighbour distance or regularized Mahalanobis distance). Freeze the metric and any transforms using source data only.
4. **Combined score:** confidence plus distance with a combination rule selected only on source validation data, or an equal-weight standardized rank sum prespecified before target evaluation. If source error counts are too low to fit a reliable error-prediction model, do not fit one; use the prespecified simple comparison.

Do not deploy an ensemble of many detectors and choose the winner on target labels.

### Primary endpoint
For each external cohort, compare the **AUROC of the risk score for distinguishing incorrect from correct participant-level classifier predictions** between (a) confidence-only and (b) confidence-plus-acoustic-distance. Report the paired difference with participant-bootstrap intervals, denominators and all transfer directions. If either class of the error-detection endpoint has too few participants or almost no errors, report estimates as non-informative/exploratory rather than forcing a significance claim.

### Secondary outcomes
- Error-versus-coverage curves and risk among covered cases at fixed descriptive coverage points.
- Sensitivity and specificity of the original PD classifier and among covered cases.
- Secondary focus on identifying false negatives among people with PD, because missed PD cases matter for screening.
- Deferred fraction overall and by age/sex where counts permit; no subgroup claim without denominators and uncertainty.
- Dataset-only/demographic-only and recording-quality negative controls, if metadata allow.
- Calibration metrics only if the sample size and protocol support them.

### Statistical and interpretation safeguards
- Treat cohort directions as individual external-validation experiments; do not make a precise universal claim from two or three datasets.
- Participants, not audio files, are resampled for confidence intervals.
- Language is not a causal explanation if language is fully confounded with dataset, task, device or site. For sustained vowels, state explicitly that this is recording-domain/dataset shift, not linguistic generalization.
- No threshold tuning or calibration on target labels. No clinical-safety claim. Report negative and contradictory results as found.

## Study gates

1. **Novelty gate:** search PubMed/MEDLINE, Europe PMC, IEEE Xplore, Scopus/Web of Science if available, ACM DL, arXiv and proceedings; backward/forward citation-chain all the closest PD voice and general OOD papers. Search per-sample risk, selective prediction, acoustic distance, target shift and confidence-error association.
2. **Data gate:** verify exact licenses/access, sample manifests, participant IDs, diagnoses, duplicate participants, task, device and metadata for at least three independent cohorts.
3. **Integrity pilot:** run data-free code tests and a participant-identity/label audit before fitting any model. Do not use pilot results to claim confirmatory performance.
4. **Protocol lock:** freeze the model, primary risk scores, target-label firewall, endpoints, bootstrap and subgroup analysis before confirmatory testing.
5. **Analysis and manuscript:** report only real results, with uncertainty; no model or result is currently available.

## Final recommendation

**This is the single selected research direction.** Proceed with the literature and dataset feasibility gates for this specific question. Do not change the topic again unless the broader search finds direct overlap or the required data cannot be accessed. If the data gate fails, transparently re-scope to a two-cohort feasibility report or a reproducibility study rather than claiming the original benchmark was completed.


## Status update — provisional, not locked

The selected question remains a candidate only. A close-overlap public repository already reports IPVS/MDVR-KCL acoustic-shortcut auditing, leave-one-corpus-out modeling, channel normalization, eGeMAPSv02, calibration and subgroup checks. The incremental comparison of acoustic distance beyond confidence may still differ, but the novelty gate is not passed.

The dataset gate is also not passed: public metadata have been inspected, but raw audio has not been downloaded, checksummed, unpacked or locally checked for unique participants, repeats, labels, tasks and duplicate sessions. ItalianPVS counts differ across descriptions (including 831 commonly reported recordings versus a mirror listing 839 uploaded files), which must be resolved from a versioned manifest.

**Do not lock the protocol or begin confirmatory training yet.** See [PRIOR_ART_AND_DATASET_GATE_2026-10-25.md](PRIOR_ART_AND_DATASET_GATE_2026-10-25.md).


## Final targeted novelty and data-gate update — 25 October 2026

The targeted audit does not clear global novelty. Cross-dataset/cross-language PD voice modelling, demographic-confounding audits, uncertainty-aware PD screening, and generic label-free deployment monitoring are established areas. A public September 2026 repository also overlaps substantially on IPVS silence/channel shortcut audits and IPVS/MDVR-KCL cross-corpus modelling. The precise confidence-only versus confidence-plus-acoustic-distance error-ranking comparison remains a conditional voice-specific comparative study, not a new general OOD algorithm.

The raw-data gate remains **NOT PASSED**. IPVS mirror metadata shows a 593 MB ZIP and host-displayed SHA-256, but the 839-file listing does not reconcile with the documented 831 WAV + six spreadsheets + ZIP inventory. UAMS metadata describes a 4.18 MB prolonged-/a/ dataset; the associated publication reports 40 PD and 41 controls in the public subset, but the archive and demographics workbook have not been audited locally. The runtime cannot resolve the dataset hosts, so there was no raw data download, local hash, WAV inspection, or participant-label join. See [the final targeted audit](FINAL_NOVELTY_AND_DATASET_AUDIT_2026-10-25.md) and [the archive verification script](../scripts/verify_voice_dataset_archives.py).

No models were trained. The protocol must remain unlocked until archive integrity, participant keys, diagnostic label mapping, duplicates and access are verified, and a sufficient number of independent compatible cohorts is established.


Additional targeted search found a January 2026 confidence-gated PD-voice ensemble and a February 2026 speech-enhancement domain-shift detector based on prediction uncertainty. They are not identical to acoustic-distance-augmented participant-level error ranking, but further reinforce that the potential contribution is a narrow comparative external-validation study rather than a novel general method. See the [final audit](FINAL_NOVELTY_AND_DATASET_AUDIT_2026-10-25.md).


## Raw data verification update — 25 October 2026

The archive-integrity check is no longer metadata-only. See [the completed audit](FINAL_NOVELTY_AND_DATASET_AUDIT_2026-10-25.md) and [the successful workflow](https://github.com/culprit-k/parkinsons-voice-ai/actions/runs/40170280356).

IPVS checksum and WAV QC passed (831 WAVs; one exact duplicate pair), but participant-level mapping remains unresolved and a spreadsheet contains direct name/surname fields. UAMS archive checks passed (81 readable mono 8-kHz WAVs; 81 unique Sample IDs, 41 HC / 40 PwPD, all IDs matched to filenames). UAMS diagnostic provenance and independence need source confirmation. No third compatible cohort is established. Therefore the candidate question remains conditional, the protocol remains unlocked, and no model has been trained.


## Three-corpus file audit update — 25 October 2026

IPVS, UAMS and MDVR-KCL source files have now been downloaded and checked through the [successful GitHub Actions audit](https://github.com/culprit-k/parkinsons-voice-ai/actions/runs/40170614840). File-level results and limits are in the [final audit](FINAL_NOVELTY_AND_DATASET_AUDIT_2026-10-25.md).

IPVS checksum and audio QC passed, but the participant mapping remains unresolved, a duplicate PD-path pair needs adjudication, and the package contains a spreadsheet with direct name/surname fields. UAMS has 81 readable 8-kHz mono WAVs, 81 unique Sample IDs, 41 HC / 40 PwPD, and 81/81 ID-to-filename matches. MDVR-KCL has 73 readable 44.1-kHz mono WAVs, but participant/label linkage is not verified. UAMS sustained /a/ and MDVR-KCL connected speech are not task-matched. NeuroVoz requires access approval.

The current question remains a conditional comparative study, not a novelty-cleared method. Three downloaded corpora do not yet equal three compatible, independent cohorts. Do not lock the protocol or train confirmatory models until privacy, participant linkage, task compatibility and independent-cohort availability are resolved.


## Current cohort and access status — 25 October 2026

The third-cohort search has identified EWA-DB as the first request target and mPower as a sustained-vowel access fallback. EWA-DB's catalogue reports sustained-vowel phonation and audio for a subset who provided written consent; access has not been granted. mPower requires Synapse research access and its diagnosis source must be checked. Neither is counted as available. Access email drafts and the acceptance checklist are in [THIRD_COHORT_AND_ACCESS_REQUEST_PLAN_2026-10-25.md](THIRD_COHORT_AND_ACCESS_REQUEST_PLAN_2026-10-25.md).

The protocol and model training remain on hold. A cross-language claim requires a task-appropriate design and verified independent cohorts; a sustained-vowel comparison should be described as cross-dataset/recording-domain robustness, not lexical language generalization.