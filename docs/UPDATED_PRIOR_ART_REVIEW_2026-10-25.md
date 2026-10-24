# Updated prior-art review: reliability monitoring and cross-corpus PD voice AI

**Audit cutoff:** 2026-10-25  
**Status:** Targeted update; not a completed systematic review.  
**Decision:** The broad idea of cross-corpus transfer, uncertainty, OOD detection, or abstention is not novel. The defensible candidate is a PD-voice-specific comparative evaluation of existing monitoring methods, conditional on data access and a complete prior-art search.

## 1. Direct Parkinson’s speech overlap

| Study | Scope and methods | What is already covered | Consequence for us |
|---|---|---|---|
| Şaraldi & Bozdağ Karakeçi (2026-09-30), [DOI 10.46578/humder.1923413](https://doi.org/10.46578/humder.1923413) | Compares CNN+ViT spectrogram modeling, Wav2Vec 2.0 and classical ML on PC-GITA, MDVR-KCL and mPower under leave-one-dataset-out evaluation. | Multi-corpus transfer, cross-dataset evaluation and model comparisons. | Neither cross-corpus testing nor LODO testing alone can be our novelty claim. Reported high results vary across target datasets; inspect code, task matching and participant-level construction before treating metrics as comparable. |
| Ganatra (2026-05-15), [paper](https://nhsjs.com/2026/limited-target-data-calibration-improves-cross-dataset-transfer-for-parkinsons-disease-detection-from-speech/) / [code](https://github.com/ynganatra/pd-speech-cross-dataset-transfer) | Frozen Wav2Vec2 with several PD speech datasets; zero-shot transfer, limited target-data adaptation, and sex-stratified false-negative rates. | Transfer failure, target adaptation and subgroup error rates. | We cannot claim those analyses as new. The current work should not tune with target labels; its emphasis, if supported, is label-free monitoring and out-of-sample error detection. |
| Hossain, Banu & Chowdhury (2026-10-22), [DOI 10.1038/s41598-026-76171-y](https://www.nature.com/articles/s41598-026-76171-y) | Cross-corpus consensus feature selection and external validation across speech datasets/languages, with probability calibration reported. | Cross-corpus feature stability, multilingual transfer, external tests and calibration. | A feature-stability or calibrated cross-corpus classifier would be too close. This is an early publication record; verify the final version, supplement and exact cohort split in the full review. |
| Guo, Zhou & Xing (2026-06-23), [DOI 10.1007/s40846-026-01040-y](https://doi.org/10.1007/s40846-026-01040-y) | Uncertainty-aware voice assessment; trained on Spanish speech and externally evaluated on Italian speech without retraining; also models severity. | Uncertainty-aware PD voice assessment and Spanish-to-Italian external validation. | Generic voice uncertainty and this language pair are not novel. Italian n=50 may correspond to the usual 28 PD / 22 elderly-control ItalianPVS subset; do not count it as a new independent cohort without provenance confirmation. |
| ParkMAE, Ando et al., [DOI 10.1038/s41598-025-30251-7](https://www.nature.com/articles/s41598-025-30251-7) | Multilingual masked-autoencoder speech representation, with held-out corpus/language tests. | Cross-linguistic representation learning and leave-one-corpus-out testing. | Multilingual representations and LODO tests are established. |
| Lim et al. (2025), [full text](https://pmc.ncbi.nlm.nih.gov/articles/PMC11909049/) | Cross-language speech model using cohorts from South Korea and Taiwan. | Cross-language PD speech classification. | Language/site/task/severity entanglement remains a key interpretive problem. |
| Shukla et al. (2026), [JMIR DOI 10.2196/95609](https://www.jmir.org/2026/1/e95609) | Bridge2AI Voice v3 demographic-confounding analysis; age-only baseline and age-restricted/matched analyses. | Age/site confounding in voice-based PD screening. | Repeating a basic age-only baseline on the same release is not enough. We need to test monitoring quality or another distinct prespecified gap. |
| Ahammad (2026), [Digital Health / PMC](https://pmc.ncbi.nlm.nih.gov/articles/PMC13346734/), [DOI 10.1177/20552076261467837](https://doi.org/10.1177/20552076261467837) | Cross-dataset PD speech, explainability, federated simulation and Brier-score reporting. | Generalization and probability evaluation across data sources. | Generalization plus calibration alone has close prior art. |
| Adnan et al. (2025), [npj Parkinson’s Disease](https://www.nature.com/articles/s41531-025-00956-7) | Semi-supervised speech embeddings, participant-ID splits, external tests and subgroup analyses. | Embedding classifiers, participant grouping, external testing and demographic analysis. | These practices are required baselines, not novelty. |
| Twala, [available Zenodo report](https://zenodo.org/records/22735799) | Reproducibility audit of participant-level grouping and cross-dataset transfer on Oxford/Sakar-style feature data. | Split leakage, metric inflation and unstable transfer. | Correct participant-level evaluation is essential but not sufficient as a primary contribution. Distinguish the already-available report from later issue-date records. |
| Public repository [Parkinson-Voice-Detection](https://github.com/BennedictQuanTon/Parkinson-Voice-Detection), created September 2026 | Self-described acoustic shortcut audit, silence-only negative control and IPVS/MDVR-KCL cross-corpus modeling. | A very similar public project audits acoustic artifacts and cross-corpus modeling on two likely candidate cohorts. | This is not peer-reviewed evidence and its numerical claims have not been independently reproduced here; nevertheless it is material public prior art. Avoid duplicating its headline question or claiming its results as ours. |

## 2. General label-free performance monitoring and selective prediction

| Method | Core idea | Required implication for our protocol |
|---|---|---|
| Kiyasseh et al., SUDO, *Nature Communications* (2024), [DOI 10.1038/s41467-024-46000-9](https://www.nature.com/articles/s41467-024-46000-9) | Estimates reliability of clinical AI on deployment data without target ground-truth, using prediction bins, pseudo-labels and a labelled reference set to estimate class contamination/reliability. | A SUDO-style method is a key comparator only if its assumptions and sample-size needs fit. “No target labels” does not mean “no labels/reference data anywhere.” |
| Nguyen et al., D3M, NeurIPS 2025, [official proceedings](https://proceedings.neurips.cc/paper_files/paper/2025/hash/0bb251eba663f0345c0929f5bbbfb6dc-Abstract-Conference.html) / [project page](https://www.cs.toronto.edu/~viet/d3m.html) | Uses disagreement rates between predictive models on held-out validation data and unlabeled deployment queries to monitor post-deployment performance deterioration. | Strong direct overlap for **batch/domain-level** monitoring. Consider a faithful D3M comparator rather than treating disagreement monitoring as our method. |
| Liang, Peng & Sun, “Selective Classification Under Distribution Shifts,” [TMLR/PMC](https://pmc.ncbi.nlm.nih.gov/articles/PMC12470254/) | Studies risk–coverage and selective prediction under covariate/distribution shifts. | Abstention and risk–coverage curves are established tools; must be treated as comparators and evaluation methods. |
| Guan & Zhou, “Detecting Performance Degradation under Data Shift in Pathology Vision-Language Model,” [arXiv 2601.00716](https://arxiv.org/abs/2601.00716) | Combines input-level shift with output-confidence signals to detect performance deterioration in pathology models. | The general combination of feature shift and predictive confidence has prior art outside PD speech. |
| Flühmann et al., “Label-free estimation of clinically relevant performance metrics under distribution shifts,” [arXiv 2507.22776](https://arxiv.org/abs/2507.22776) | Estimates confusion-matrix quantities, including clinically relevant sensitivity/specificity-related measures, under target shift without target labels; evaluated on chest X-ray shifts. | Potential **batch-level performance-estimation** baseline if a faithful implementation is practical. It answers a different question from per-person abstention. |
| “Out-of-Distribution Detection as a Risk-Control Strategy for Medical Classification ML Models,” [PubMed](https://pubmed.ncbi.nlm.nih.gov/41127928/) | Evaluates OOD detection as a risk-control strategy in medical classification. | OOD-triggered deferral is an active general method, not new by itself. |
| Domain-shift detection for speech enhancement (2026), [article](https://link.springer.com/article/10.1186/s13636-026-00448-3) | Shift detection for a speech/audio task, but not PD diagnosis. | Relevant audio-domain adjacent work; include in the broader screen if its methods are applicable. |

## 3. Revised defensible question

> On independent Parkinson speech corpora held out from model development, do prespecified label-free monitoring methods identify participant-level errors or batch-level performance degradation better than confidence-only baselines, and what risk–coverage and subgroup-deferral trade-offs result?

This is an **application-level comparative benchmark of existing methods**, not a new general-purpose OOD or abstention method.

Two endpoints must remain distinct:

1. **Participant-level error detection/selective prediction:** rank individual participants by estimated risk and evaluate whether incorrect model predictions receive higher risk scores, using target diagnosis labels only after all methods/rules are frozen.
2. **Batch/domain-level deterioration monitoring:** apply SUDO, D3M or a label-free confusion-matrix estimator to an unlabeled batch/corpus; only after freezing the monitor compare its warning/estimate with actual held-out target performance.

Do not treat multiple random subsets from the same small corpus as independent domains. Do not claim “label-free” means there are no labelled source/reference data. Do not combine per-person and per-batch methods under one endpoint unless a method’s adaptation is explicitly justified and separately validated.

## 4. Minimum method panel to investigate

Keep it small and reproducible:
- **Confidence-only comparator:** maximum predicted probability, margin/entropy.
- **Input-level shift comparator:** a prespecified distance between source and target acoustic-feature distributions; embedding distance only if the encoder is fixed and documented.
- **Disagreement monitor:** D3M or a faithful disagreement-rate baseline at batch/domain level.
- **One label-free clinical performance estimator:** SUDO or Flühmann-style confusion-matrix estimation, chosen after checking method code, assumptions and feasibility.

Do not implement a dozen loosely related “OOD scores” and select the winner on the same external outcomes. The main comparison and threshold must be prespecified. Any target labels are for retrospective evaluation only, never to select the monitor, threshold, features, calibrator, preprocessing, or model.

## 5. Data feasibility and independence: current decision

**Data gate not passed.** Two lower-friction raw-audio candidates are identifiable, but three fully verified, independent, legally accessible cohorts have not been established.

| Cohort | Known facts / access | Current disposition |
|---|---|---|
| MDVR-KCL | UK English; reported 16 PD / 21 controls; Zenodo [10.5281/zenodo.2867216](https://doi.org/10.5281/zenodo.2867216). | Candidate A; exact package, labels, participant manifest and license still need a local integrity check. |
| ItalianPVS / IPVS | Italian; common older-control analysis uses 28 PD + 22 elderly controls; full release also has 15 young controls. Official [IEEE DataPort record](https://ieee-dataport.org/open-access/italian-parkinsons-voice-and-speech). | Candidate B; verify portal access, terms, participant IDs, and task structure. |
| UNLaM Parkinson Voice Database | Spanish/Argentina; original report describes 55 PD + 64 controls (119); 2026 paper reports n=126. | Potential candidate; resolve count/version discrepancy and verify an exact downloadable raw-audio manifest and licence. |
| PC-GITA | Colombian Spanish; often described as around 50 PD + 50 controls. Access has been described as academic request through Universidad de Antioquia. | Request candidate; not approved until permission and data manifests are confirmed. |
| NeuroVoz | Spanish; 54 PD + 58 controls in the data paper. Zenodo records show restricted access: [record](https://zenodo.org/records/10777657). | Access-request candidate, not automatically downloadable. |
| EWA-DB | Slovak; metadata catalogue reports 1,649 speakers including PD, controls and other diagnoses; audio is a smaller consented subset. [ELRA-S0489](https://catalogue.elra.info/en-us/repository/browse/ELRA-S0489/). | Licence/request candidate; catalogue participant totals are not usable-audio totals. |
| Bridge2AI Voice v4.0.0 | Released 2026-10-19; 1,370 participants and 48,226 recordings. [PhysioNet](https://physionet.org/content/b2ai-voice/4.0.0/). Public release provides derived features; raw audio has additional institutional sign-off. Version 4 shares many participant IDs with version 3. | Possible within-cohort/site/task analysis; not an independent dataset versus v3, and not automatically cross-language. |
| mPower | US remote smartphone collection with differing recruitment/diagnosis definitions. | Could be a cohort if exact voice task, diagnosis labels, access and participant IDs check out. |
| Oxford/UCI Telemonitoring | 42 PD participants, 5,875 repeated voice records; designed for severity regression, not a healthy-control binary task. [UCI](https://archive.ics.uci.edu/dataset/189/parkinsons+telemonitoring). | Not a binary PD/control cohort. Use only for suitable regression or split-code checks. |
| ParkCeleb | Video-derived, celebrity speakers; public record mainly metadata/links and access restrictions. [Zenodo](https://zenodo.org/records/13954768). | Not a primary raw-audio candidate; source/speaker confounding and licensing/re-identification risks. |
| UCI 301/489 and other engineered-feature data | Repeated participant rows; not raw audio and not necessarily comparable. | Useful for split/reproducibility checks, not a substitute for cross-corpus acoustic shift analysis. |

### Independence cautions
- The Italian n=50 validation sample reported in the 2026 Spanish-to-Italian paper may be the ordinary 28-PD/22-elderly-control IPVS subset; assume possible overlap until provenance proves otherwise.
- The UNLaM count discrepancy (119 vs 126) must be reconciled by version and inclusion criteria.
- Bridge2AI v3 and v4 are not independent cohorts; do not count them as independent external datasets.
- One participant with many clips is still one participant. Deduplicate IDs before computing N or splitting.
- Never upload raw or restricted speech files to GitHub. Commit code, permitted aggregate manifests, data-free tests, citations and checksums instead.

### Go/no-go criterion
For the intended external monitoring benchmark, require **at least three independent, legally accessible cohorts** with participant-level PD/control labels and usable compatible inputs; four or more is preferred. Before approving each one, document the exact release, download date, licence/DUA, class counts, participant count, task, language, device/site, diagnosis criteria, demographics, missingness and duplicate/overlap checks. If only two cohorts are available, re-scope as a clearly labelled two-corpus pilot or pivot to a review/reproducibility project. Do not claim broad multilingual external validation without the data.

## 6. Search scope and limits

This update was based on targeted current searches for PD speech + label-free reliability, SUDO, OOD, domain-shift detection, selective prediction, abstention, performance deterioration, dataset transfer, and the nearest PD-specific work. It identified substantial direct and adjacent prior art, including D3M and label-free confusion-matrix estimation. It is **not** a completed systematic search: the planned searches across PubMed/MEDLINE, Europe PMC, Scopus, Web of Science, IEEE Xplore, ACM Digital Library, arXiv and conference proceedings, full deduplication, screening, supplementary-file review and forward/backward citation chaining remain incomplete.

No priority/“first study” claim is justified. No models have been trained and there are no new empirical results.

## 7. Decision

**GO:** continue prior-art verification and data-access/independence checks.  
**HOLD:** final protocol lock, model training, and any first-of-kind claim.

If the data gate passes, write a precise prespecified protocol with one primary endpoint, source-only monitor/threshold selection, participant-level uncertainty and subgroup deferral. If it fails, change the project scope transparently rather than pretending the intended multi-corpus study was completed.
