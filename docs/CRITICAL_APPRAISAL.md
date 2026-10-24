# Critical appraisal: closest prior studies

**Review date:** 2026-10-25  
**Status:** Targeted critical appraisal based on publisher full text/abstracts. This is not a systematic review. Full supplemental-material review and wider screening remain open tasks.

## 1. Lim et al. (2025): A cross-language speech model for detection of Parkinson's disease

**Citation:** Lim WS, Chiu SI, Peng PL, et al. *A cross-language speech model for detection of Parkinson's disease.* Journal of Neural Transmission. 2025;132:579-590. DOI: [10.1007/s00702-024-02874-z](https://doi.org/10.1007/s00702-024-02874-z). Open access: [Publisher](https://link.springer.com/article/10.1007/s00702-024-02874-z), [PubMed Central](https://pmc.ncbi.nlm.nih.gov/articles/PMC11909049/).

### Design and reported results
- 646 participants recruited from movement-disorder clinics in South Korea and Taiwan: 347 with PD and 299 healthy controls.
- Participants with PD recorded smartphone speech during the medication “on” phase.
- Korean and Taiwanese speech datasets were combined; the training set used controls and early-stage PD, while the validation set used controls and advanced-stage PD.
- Random forest/AdaBoost models reported AUROC 0.82 for early-stage PD versus controls; the random-forest validation AUROC was reported as 0.90 for advanced-stage PD.
- Performance varied by speech-length/task combination; a short-speech merged dataset reported lower performance (AUROC 0.72).

### Strengths
- Large cohort relative to many voice-PD studies.
- Uses two linguistically distinct East Asian language settings.
- Reports a stage-related evaluation rather than only a conventional random split.
- Uses both acoustic and linguistic speech features.

### Limitations / questions for full-text and supplement extraction
- The validation construction mixes disease stage and potentially cohort/language/task differences; AUROC in advanced-stage PD versus controls is not equivalent to validation on a fully independent language/site with the same clinical spectrum.
- Korean and Taiwanese recording tasks and lengths differ, so language effects may not be separable from task/protocol effects.
- Need to extract participant-level split details, all model comparisons, confidence intervals, calibration, demographic balance, and availability of code/data from full methods and supplements.
- Medication-on recordings limit inference to other medication states.
- Do not interpret the reported AUROCs as evidence of ready-for-clinic diagnostic utility.

### Relevance to our study
Cross-language classification is already demonstrated. A useful follow-on must answer a distinct, prespecified question and use a transparent validation design.

## 2. Ando et al. (2026): ParkMAE

**Citation:** Ando A, Lesage A, De Gennes M, et al. *ParkMAE: a cross-linguistic masked autoencoder framework for robust Parkinson's disease detection from speech.* Scientific Reports. 2026;16:783. Published online 2025-12-10. DOI: [10.1038/s41598-025-30251-7](https://doi.org/10.1038/s41598-025-30251-7). [Publisher full text](https://www.nature.com/articles/s41598-025-30251-7).

### Design and reported results
- Reports about 750 hours of multilingual pretraining data and 100 hours of evaluation data across four languages.
- Uses a self-supervised masked-autoencoder speech representation.
- Reports 39% F1 for cross-linguistic diagnosis and compares against eGeMAPS and Whisper.
- Cross-linguistic linear probing uses four evaluation datasets representing four languages: EWA-DB, ItalianPVS, MDVR, and NeuroVoz.
- In cross-linguistic experiments, three datasets are used for training and the remaining language's dataset for testing; PVA is excluded from binary diagnosis because it has no healthy control class.

### Strengths
- Explicit unseen-language evaluation.
- Multiple datasets and model families are compared.
- Evaluates more than binary diagnosis, including medication state, severity and cognitive measures.
- The authors describe code and methodological documentation as available.

### Limitations / questions for full-text and supplement extraction
- The held-out language is also represented by a held-out dataset; language, cohort, site, task and acquisition effects may remain entangled. This is best described as cross-dataset/unseen-language generalization unless these factors can be separated.
- Need to inspect the participant counts and diagnostic composition of each dataset, repeated-speaker overlap, exact split construction, and uncertainty around reported metrics.
- F1 depends on class prevalence and threshold; do not directly compare the reported 39% F1 with AUROC values in other studies.
- Need to reproduce the dataset-by-dataset results and confirm software/data availability before choosing a comparable benchmark.
- Claims about “robustness” need to be tied to the actual perturbations and evaluation performed.

### Relevance to our study
A generic “train on some languages, test on another” study would substantially overlap with ParkMAE. Potential contribution must be more specific, such as an independently prespecified robustness/calibration audit, provided suitable data and a meaningful difference from existing work can be demonstrated.

## 3. Shukla et al. (2026): demographic confounding in Bridge2AI-Voice

**Citation:** Shukla S, Naliyatthaliyazchayil P, Gichoya JW, Purkayastha S. *Demographic Confounding in Voice-Based Parkinson Disease Screening: Methodological Analysis of the Bridge2AI Voice Dataset.* Journal of Medical Internet Research. 2026;28:e95609. DOI: [10.2196/95609](https://doi.org/10.2196/95609). [Publisher full text](https://www.jmir.org/2026/1/e95609).

### Design and reported results
- Uses Bridge2AI-Voice v3.0.0 and five-fold participant-level cross-validation.
- Parkinson's cohort: 253 participants, 106 cases and 147 controls, with 2,131 recordings across eight selected tasks.
- Compares an audio spectrogram transformer (AST) with age-only and age-plus-sex logistic-regression baselines under the same folds.
- Full-cohort PD AUROC: AST 0.843; age-only 0.875 (DeLong P=.36).
- Age-restricted analyses show lower but nontrivial audio-model performance; the article reports AUROC 0.787 for ages 60–80 and 0.726 for the US-only ages 60–80 analysis.
- Cross-version preprocessing evaluation reported AUROC 0.618, which concerns preprocessing/version sensitivity, not population-level external validation.

### Strengths
- Participant-level splits reduce repeated-recording leakage.
- Same-fold demographic-only baselines directly test a plausible shortcut.
- Uses age restriction, country/site proxy analysis, propensity matching and retraining sensitivity analyses.
- Reports methodological details and reporting recommendations.

### Limitations and interpretation cautions
- It is a single dataset/version analysis; the results do not settle how confounding behaves in every language, site or recording setup.
- Country is a coarse proxy for site where explicit site identifiers were unavailable; residual confounding remains possible.
- The paper reports that its Bridge2AI cohort is English-language, limiting direct multilingual conclusions.
- Cross-version preprocessing results should not be described as external population validation.
- Repeating the same analyses on the same release without a new methodological or validation contribution is unlikely to be sufficiently novel.

### Relevance to our study
Age-only baselines and demographic confounding checks should be treated as necessary methodological safeguards, not as the primary novelty claim by themselves.

## Cross-study synthesis

| Dimension | Lim et al. | ParkMAE | Shukla et al. |
|---|---|---|---|
| Main question | Cross-language PD classification | Multilingual foundation model and unseen-language testing | Demographic confounding and preprocessing sensitivity |
| Independent language/dataset evaluation | Mixed-language cohort and stage-based validation | Yes, held-out language dataset design | No; within Bridge2AI with cross-version preprocessing sensitivity |
| Demographic-only baseline | Not established from this preliminary extraction | Must verify in full paper/supplements | Central component |
| Recording/preprocessing robustness | Speech-length/task sensitivity is reported | Must extract exact perturbation/robustness experiments | Cross-version preprocessing sensitivity |
| Novelty overlap with our original idea | High for cross-language detection | Very high for unseen-language generalization | High for demographic-confounding audit on Bridge2AI |

## Candidate research direction (not yet approved)

A prespecified, transparent evaluation of how performance, calibration and subgroup estimates change under independently held-out datasets and recording/domain shifts could be useful. However, we must first:
1. Search for studies that already combine external validation, demographic adjustment, and calibration in voice-PD models.
2. Confirm which datasets have compatible diagnosis labels, language/task metadata, participant IDs, and permitted access.
3. Establish whether language can be separated from site, dataset, and task.
4. Define one primary estimand and a feasible sample-size/precision strategy.
5. Decide whether the project should be a new empirical benchmark, a methodological replication, or a structured review.

No final novelty claim should be made until those steps are complete.
