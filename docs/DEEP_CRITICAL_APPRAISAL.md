# Deep critical appraisal of the closest Parkinson voice-AI studies

**Review date:** 2026-10-25  
**Status:** Targeted methods-level appraisal. This is not yet a completed systematic review: the full search log, screening of all records, duplicate removal, and complete extraction have not been finished.

## Executive decision

The broad research idea is important, but generic novelty claims do not survive the current literature review. Existing studies already address cross-language modeling, leave-one-language-out testing, cross-corpus feature stability, subject-aware external validation, target-domain adaptation, demographic error gaps, age-only baselines, and Brier-score/temperature-scaling analyses.

A defensible contribution may still come from (a) a carefully scoped, independent replication with a precise additional analysis that prior work has not adequately answered, or (b) a rigorous updated review of primary studies that actually perform external/cross-corpus evaluation. The data-access audit will decide which pathway is credible. We should not finalize a novel hypothesis or title yet.

## 1. Lim et al. (2025): cross-language speech model

**Citation:** Lim et al. “A cross-language speech model for detection of Parkinson’s disease.” *Journal of Neural Transmission* 132:579–590. DOI: https://doi.org/10.1007/s00702-024-02874-z. Full text: https://pmc.ncbi.nlm.nih.gov/articles/PMC11909049/

### Study design and reported results
- 646 participants: 347 with PD and 299 healthy controls, recruited in South Korea and Taiwan.
- PD recordings were collected in the medication “on” phase.
- Korean and Taiwanese speakers differed in speech material and protocol; the Taiwanese cohort used a standardized fixed-length passage.
- The paper’s setup included controls and early-stage PD for training and controls and advanced-stage PD for validation. AUROC was reported around 0.82 in an early-stage analysis and around 0.90 for an advanced-stage validation setup; reported performance varied with speech length/task definition.

### Strengths
- A relatively substantial clinical cohort compared with classic voice-feature benchmarks.
- Clinical diagnosis and disease-stage information.
- Explicit attention to language and speech duration.

### Critical limitations for our research question
1. This is not a clean held-out-language test: the training/validation design is also separated by disease stage and cohort.
2. Language is entangled with site, speech task/material, recruitment and participant characteristics. A model’s change in performance cannot be attributed to language alone.
3. Controls were recruited through the patients’ social network in the described cohorts, and demographic distributions differ between cases and controls. These details matter for confounding.
4. AUROC measures ranking, not calibrated probabilities, a clinically chosen screening threshold, or prospective screening safety.

**Implication:** cross-language voice modeling is established. Separation of language from the rest of domain shift remains difficult, and clinical reliability requires evaluation beyond AUROC.

## 2. Ando et al. / ParkMAE: cross-linguistic self-supervised representations

**Citation:** Ando et al. “ParkMAE: a cross-linguistic masked autoencoder framework for robust Parkinson’s disease detection from speech.” *Scientific Reports* 16:783. DOI: https://doi.org/10.1038/s41598-025-30251-7. Full text: https://www.nature.com/articles/s41598-025-30251-7

### Study design and reported results
- Self-supervised pretraining on approximately 750 hours of multilingual speech.
- Four principal evaluation datasets/languages: EWA-DB (Slovak), ItalianPVS (Italian), MDVR (UK English) and NeuroVoz (Castilian Spanish). PVA is PD-only and is not a binary PD/control cohort.
- In the cross-linguistic setting, three language-associated datasets are used for training and the fourth is held out.
- The paper reports mean cross-linguistic F1 of approximately 0.39 ± 0.08 for ParkMAE and a substantial decline from in-domain performance. Performance varies strongly by dataset.

### Strengths
- A held-out-corpus test is more realistic than randomly mixing participants from all languages in one split.
- It compares multiple speech representations and reports sensitivity, specificity and predictive values, not only accuracy.
- The discussion acknowledges that language is entangled with task, cohort size, equipment and recording conditions.

### Critical questions to verify
1. The methods describe dividing recordings into overlapping audio windows, assigning windows the recording’s label, and learning a classifier over windows. The in-domain cross-validation unit is not clearly documented as participant-grouped in the main methods text. This is a reporting/reproducibility question, **not proof that data leakage occurred**. Inspect code or seek clarification before making any stronger statement.
2. F1 depends on threshold and class prevalence. Probability calibration is not the main focus of the paper.
3. Small held-out cohorts yield uncertain estimates, even when a point estimate appears impressive.
4. The full data filters and final participant counts differ from corpus-wide counts; the exact version and exclusions need to be recorded.
5. The data-availability description refers to public or request-based datasets; a fully reproducible dedicated ParkMAE training repository and weights are not clearly linked in the article text reviewed.

**Implication:** cross-linguistic evaluation is already studied. A replication can investigate how conclusions change under participant-level aggregation, explicit uncertainty and clinically meaningful probability evaluation, but those additions must be justified against newer studies.

## 3. Hossain, Banu and Chowdhury (2026): cross-corpus consensus features

**Citation:** “Cross-corpus consensus feature selection for language-invariant Parkinson’s disease detection: a dual-stream acoustic and spectrogram-attention framework.” *Scientific Reports*, early accepted version published online 22 October 2026. DOI: https://doi.org/10.1038/s41598-026-76171-y. Article: https://www.nature.com/articles/s41598-026-76171-y

### Study design
- A stream of 156 handcrafted acoustic descriptors is filtered using feature-selection/model agreement across derivation corpora.
- A second stream uses spectrogram representations and combines saliency/attention approaches to define selected regions.
- The article describes three derivation corpora associated with English, Italian and Bengali and held-out corpora associated with Spanish, English and Spanish, including PC-GITA, ParkCeleb and NeuroVoz.
- Its appendix reports an LLM experiment in which engineered numeric acoustic feature/value pairs are serialized as text and given to GPT-4 Turbo. This is not raw voice/audio diagnosis by GPT.
- A calibration experiment reserves a derivation-data subset, applies temperature scaling and minimizes Brier score before external evaluation.

### Strengths
- Feature stability is assessed across corpora rather than inferred from one train/test split.
- The article distinguishes derivation corpora from external validation corpora.
- The appendix explicitly describes a held-back calibration subset for probability scaling.

### Critical questions
1. The article is marked as an early accepted version and may be edited before the final version of record; recheck before quoting exact claims.
2. Cross-corpus feature stability, language-invariant features, and post-hoc calibration are close overlap with our original idea and cannot be claimed as novel by themselves.
3. For the LLM branch, make the distinction explicit: the inputs are engineered feature/value pairs, not waveforms.
4. Some external corpora require request-based or institutional access. The results are not independently reproducible for us until access, preprocessing, IDs and code are verified.
5. Do not infer adequate demographic fairness power from the presence of multiple languages; check the available age/sex metadata and participant counts by diagnosis.

**Implication:** cross-corpus stability and probability calibration already have direct precedent. We need a much sharper question or an honest independent reproduction.

## 4. Ahammad (2026): cross-dataset framework with explainability and Brier score

**Citation:** “Generalization over accuracy: A cross-dataset, explainable, and federated learning framework for Parkinson’s disease detection.” *Digital Health*, first published 8 July 2026. DOI: https://doi.org/10.1177/20552076261467837. Full text: https://journals.sagepub.com/doi/10.1177/20552076261467837

### Study design
- Three engineered-feature datasets are combined/harmonized: a Kaggle PD feature dataset, UCI 301 (Parkinson Speech Dataset with Multiple Types of Sound Recordings), and UCI 489 (Parkinson Dataset with Replicated Acoustic Features).
- The paper discusses subject-aware internal evaluation, cross-dataset testing, SHAP/LIME explainability, federated-learning simulation, and Brier score.
- Code is described as available on request, rather than as a public versioned repository.

### Strengths
- Goes beyond accuracy and explicitly discusses Brier score and cross-dataset degradation.
- Feature-based setup is easier to investigate than restricted raw-audio encoders.
- Recognizes that random-split performance can be an unreliable proxy for transfer.

### Critical audit points
1. UCI 301 contains 1,040 training rows from 40 speakers (20 PD and 20 controls), with repeated tasks per speaker; its separate test collection contains 28 PD participants only. A PD-only test set cannot support an ordinary two-class AUROC or specificity estimate without controls.
2. UCI 489 has 240 rows from 80 participants, each represented by three acoustic-feature replications. UCI documentation explicitly warns that these rows are not independent.
3. Although subject-aware evaluation is described, the methods/results also name stratified split procedures. We must inspect the exact outer and inner folds to determine whether grouping is respected at every stage; terminology alone does not prove absence or presence of leakage.
4. Some narrative summaries of metrics appear difficult to reconcile with the displayed baseline table. This must be resolved with data/code reproduction before relying on the summary.
5. This study does not constitute a cross-language raw-audio experiment.

**Implication:** a broad cross-dataset benchmark with Brier score is already established. It is not sufficient to claim novelty.

## 5. Ganatra (2026): target-domain adaptation

**Citation:** Yash N. Ganatra, “Limited Target Data Calibration Improves Cross-Dataset Transfer for Parkinson’s Disease Detection from Speech.” NHSJS, 15 May 2026. Article: https://nhsjs.com/2026/limited-target-data-calibration-improves-cross-dataset-transfer-for-parkinsons-disease-detection-from-speech/. Code: https://github.com/ynganatra/pd-speech-cross-dataset-transfer

### Study design and reported results
- Frozen Wav2Vec2 representation with separate task heads for sustained vowels versus read/other speech.
- Uses NeuroVoz, EWA-DB, ItalianPVS, MDVR-KCL and a US sustained-vowel corpus.
- Compares within-dataset performance, zero-shot transfer, and adaptation after adding a small speaker-balanced subset of target-domain speakers.
- Evaluates a sex-specific false-negative-rate difference.
- For one held-out Slovak evaluation, the article reports a zero-shot AUROC around 0.41, improving to roughly 0.58–0.67 depending on the target-data condition.

### Strengths
- Public code is available.
- Treats zero-shot failure as a key result and explores limited target data.
- Reports a sex-related false-negative disparity.

### Limitations
- Several datasets are small and differ in speech task, language, site and recording conditions.
- The enhanced transfer experiment centers on one main target domain, rather than repeating adaptation uniformly for every held-out corpus.
- The paper reports three-seed summaries but does not prominently report participant-clustered confidence intervals.
- Some headline metrics are calculated per clip, and a speaker can contribute multiple clips; clip-level summaries may overweight speakers who contribute more data.
- “Calibration” in the title mainly denotes adding target-domain examples for adaptation. It is not the same as evaluating probability calibration via Brier score or calibration slope.

**Implication:** target-data adaptation and sex-stratified false-negative analysis already have precedent. Any extension must differ in a specific, defensible way.

## 6. Shukla et al. (2026): demographic confounding on Bridge2AI

**Citation:** “Demographic Confounding in Voice-Based Parkinson Disease Screening: Methodological Analysis of the Bridge2AI Voice Dataset.” *Journal of Medical Internet Research* 28:e95609. DOI: https://doi.org/10.2196/95609. Full text: https://www.jmir.org/2026/1/e95609

### Design and results
- Evaluates Bridge2AI Voice v3 with participant-level five-fold cross-validation.
- Compares an audio model with demographic-only prediction and evaluates age-restricted, US-only and age/sex-matched sensitivity analyses.
- Reports AUROC around 0.843 for the audio model and 0.875 for age-only prediction in the full cohort. In the 60–80 age subset the audio-model AUROC falls to around 0.787; more restricted analyses report lower results.

### Strengths
- Makes demographic-only baselines central to the evaluation.
- Studies age, site and preprocessing/version effects, rather than relying on one unadjusted result.
- Demonstrates why case/control discrimination alone may be misleading.

### Limitations
- It is specific to a Bridge2AI version and its recruitment/metadata structure.
- The broad idea of age-only baselines and age-restricted sensitivity checks is already directly studied.
- Site/country and diagnosis are not fully separable in all groups.

**Implication:** a new demographic analysis needs more than repeating the v3 baseline. Bridge2AI v4 is a major release change, but a version-comparison question is justified only if exact cohort overlap, diagnosis labels and features can be audited.

## 7. Adnan et al. (2025): embedding fusion and external tests

**Citation:** “A novel fusion architecture for detecting Parkinson’s Disease using semi-supervised speech embeddings.” *npj Parkinson’s Disease* 11:176. DOI: https://doi.org/10.1038/s41531-025-00956-7. Full text: https://www.nature.com/articles/s41531-025-00956-7. Code/features: https://github.com/tmadnan/PARK-speech-fusion

### Design and reported results
- 1,306 participants (392 with PD, 914 non-PD) and 1,854 clips.
- English pangram speech represented using Wav2Vec 2.0, WavLM and ImageBind embeddings.
- Main 70/15/15 split is grouped by participant ID.
- The best fusion AUROC is reported around 0.889; external evaluation in other clinical/recording settings reports AUROCs around 0.821 and 0.784, plus around 0.774 for an additional spontaneous-English speech test.
- Subgroup/error analyses include age, sex and ethnicity.
- Original audio is not distributed with the public features; derived representations and code are available.

### Strengths
- Participant-level main split and external-setting evaluation.
- Public code/features and demographic subgroup/error analysis.
- Reports participant counts separately from clips.

### Limitations
- English-only; does not resolve cross-language generalization.
- Some home-cohort diagnosis labels are self-reported while other cohort labels are clinically confirmed. Diagnostic certainty is entangled with recruitment/recording setting.
- External settings also change participant mix and recording conditions.
- Subgroup sample sizes limit conclusions from nonsignificant differences.
- It is not primarily a probabilistic-calibration paper.

**Implication:** external testing and demographic analysis are already in the literature. They do not create novelty on their own.

## 8. Twala (2026): split-design and transfer reproducibility

**Sources:** Zenodo report/code: https://zenodo.org/records/22735799. Publisher page: https://www.sciencedirect.com/science/article/pii/S2666521226001572

The currently available reproducibility record reports that participant-level evaluation on two public feature datasets yielded accuracy around 78–84% and AUROC around 0.75–0.85. It reports that ungrouped Oxford splits inflated accuracy by up to 11.1 percentage points and AUROC by up to 0.169; four of six transfer models predicted every external participant as PD; and a pitch-period-entropy feature changed direction across corpora.

The publisher page lists a November 2026 issue date, which is after this review’s 25 October 2026 date. Until updated, describe it as a current reproducibility report/record and recheck publication status before final citation.

**Implication:** subject-level splitting and basic cross-dataset transfer are already the subject of a reproducibility study. A replication may still be useful if transparent, but should not be advertised as a wholly new concept.

## 9. Reviews and reporting standards

- Ahn et al. (2025), “Voice-Based Detection of Parkinson’s Disease Using Machine and Deep Learning Approaches: A Systematic Review.” *Bioengineering* 12(11):1279. DOI: https://doi.org/10.3390/bioengineering12111279. Included 69 studies and searched major bibliographic databases through September 2025. It is a starting point, but it does not encompass late-2025 and 2026 studies.
- Sheikh Taheri et al. (2026), “Diagnosis of Parkinson’s Disease Based on Voice and Speech Using Machine Learning and Deep Learning: A Systematic Umbrella Review.” PubMed: https://pubmed.ncbi.nlm.nih.gov/42493288/. Included 22 reviews; noted generally low methodological quality and limited reporting of medication state, language, severity, recording conditions, external validation, calibration, fairness and interpretability.
- TRIPOD+AI: https://doi.org/10.1136/bmj-2023-078378 — reporting guideline for prediction-model studies, not a risk-of-bias tool.
- PROBAST+AI: https://doi.org/10.1136/bmj-2024-082505 — assesses risk of bias and applicability.
- STARD-AI: https://doi.org/10.1038/s41591-025-03953-8 — reporting guideline for AI diagnostic-accuracy studies.

Use the guidelines according to their distinct roles: TRIPOD+AI for transparent model reporting, PROBAST+AI for appraising bias/applicability, and STARD-AI if we frame our evaluation as diagnostic-accuracy research.

## 10. Cross-cutting methodological conclusions

### Participants are not recordings or windows
Several corpora have many more files than participants. Repeated files, overlapping windows or replicated feature rows are not independent people. Store participant ID, recording ID, task ID, dataset ID and language separately. Group all records from the same participant into one fold and one split. If uncertainty is estimated by bootstrap, resample participants and keep their recordings together.

### External-language performance is usually combined domain shift
Language, recruitment site, task, equipment, protocol, severity and demographic mix commonly change together. Unless the design separates these factors, describe the result as cross-dataset/domain generalization, not a causal effect of language.

### Discrimination is not calibration
- AUROC is ranking, not probability reliability.
- Sensitivity and specificity depend on the threshold.
- Brier score assesses squared probability error but is influenced by case mix and prevalence.
- Reliability diagrams and calibration slope/intercept may be unstable in tiny external cohorts.
- Any threshold, feature selection or calibrator must be selected using training/validation data, never the untouched external test set.
- Case-control prevalence often does not reflect real-world screening prevalence; PPV, NPV and absolute risks may not transport directly.

### Fairness claims need subgroup counts and uncertainty
A difference in female and male false-negative rates is descriptive unless denominators and uncertainty are reported. A nonsignificant difference is not evidence of equivalence. Include age-only, sex-only or dataset/source-only baselines when supported by the metadata, and do not fit thresholds on the same external set used to report subgroup error rates.

### Dataset identity can become a shortcut
Test if task, source dataset or recording metadata predicts disease label. A corpus dominated by one class can let a model exploit source identity rather than disease. Where compatible metadata exist, consider dataset-only baselines, matched-task sensitivity analyses, and leave-one-dataset-out evaluation.

## 11. What is not novel by itself

Do not claim novelty for:
- voice-AI classification of PD versus controls;
- cross-language model training/testing;
- leave-one-language-out evaluation;
- cross-corpus feature stability;
- subject-wise splitting;
- cross-dataset generalization;
- age-only baselines or simple demographic subgroup analysis;
- adding target-domain examples;
- reporting Brier score or applying temperature scaling.

## 12. Provisional pathways (not finalized claims)

1. **Focused systematic review / meta-research:** assess primary PD voice-AI studies that actually conduct external/cross-corpus evaluation, with structured appraisal of participant-level separation, demographic shortcuts, calibration, thresholds, cohort/task confounding and public reproducibility. It must be narrower than or meaningfully updated beyond earlier reviews.
2. **Independent replication/benchmark:** reproduce selected open baselines, explicitly compare row-wise versus participant-grouped splitting where valid, and report participant-level uncertainty. Because related work exists, frame it as a transparent replication plus a precisely justified additional analysis.
3. **Multi-domain subgroup stress test:** examine sex-specific errors across held-out datasets only if at least three independent corpora contain compatible sex metadata and enough subgroup participants. This overlaps with Ganatra, so it is not cleared as novel.

## Recommendation

Do not freeze the title, abstract, hypothesis or novelty claim. First complete the evidence matrix and verify dataset access. If at least two independent compatible cohorts can be used legally, an empirical reproduction/stress test may be appropriate. If not, pivot to a focused review rather than forcing a weak cross-language model.

No model has been trained, and no project-derived experimental result exists.
