# Literature review batch 3 — dataset feasibility and updated novelty audit

**Review date:** 2026-10-25  
**Status:** targeted review and feasibility triage; not a completed systematic review. This document records the effect of newly identified work on our research direction.

## 1. New close-overlap study: Ganatra (2026)

Yash N. Ganatra, “Limited Target Data Calibration Improves Cross-Dataset Transfer for Parkinson’s Disease Detection from Speech.” NHSJS, May 15, 2026. [Article](https://nhsjs.com/2026/limited-target-data-calibration-improves-cross-dataset-transfer-for-parkinsons-disease-detection-from-speech/) · [Code](https://github.com/ynganatra/pd-speech-cross-dataset-transfer).

The study uses NeuroVoz (Castilian Spanish), EWA-DB (Slovak), IPVS (Italian), MDVR-KCL (UK English), and a US sustained-“Ah” dataset. It uses a frozen Wav2Vec2 backbone with separate heads for vowel versus read/other speech. The article reports poor zero-shot transfer, AUROC around 0.41 for a multilingual model evaluated on the held-out Slovak target domain, and improvement to about 0.67 after adding a small target-domain training subset.

Important limitations acknowledged by the paper:
- It does not isolate language effects from site, task, recording environment, and protocol.
- The target-data adaptation experiment is focused on one left-out target dataset rather than repeated across multiple held-out domains.
- Several datasets have very small test sets.
- It reports no confidence intervals/bootstrap intervals.
- It does not comprehensively compare classical feature baselines, fully fine-tuned encoders, and alternative domain-adaptation methods.

**Terminology warning:** the word “calibration” in this title primarily means adding target-domain examples to adapt the model. This is not the same as a full probabilistic calibration evaluation using metrics such as Brier score, calibration slope/intercept, or expected calibration error.

## 2. Other new/adjacent work affecting novelty

- **Twala (2026), reproducibility report**, *Evaluation design, class imbalance, and cross-dataset generalisation in voice-based Parkinson’s disease detection*. [ScienceDirect](https://www.sciencedirect.com/science/article/pii/S2666521226001572) · [Zenodo/code record](https://zenodo.org/records/22735799). It directly evaluates participant-level splitting and cross-dataset transfer on Oxford and Sakar features. The article reports inflated results from ungrouped splits and severe failures in several transfer directions. Leakage-aware splitting and cross-dataset transfer alone are therefore not a sufficient novelty claim.
- **Adnan et al. (2025)**, semi-supervised speech embedding fusion, already reports external clinical tests, demographic analyses, and a spontaneous-English speech test. [Paper](https://www.nature.com/articles/s41531-025-00956-7) · [Code/features](https://github.com/tmadnan/PARK-speech-fusion.git). Original audio is not publicly redistributed; extracted features are available.
- **ParkMAE (2026)** already reports cross-linguistic evaluation across EWA-DB, ItalianPVS, MDVR and NeuroVoz. [Full text](https://pmc.ncbi.nlm.nih.gov/articles/PMC12780117/). It uses three datasets for training and the fourth as a held-out language test. Cross-language evaluation alone is not novel.
- **Bridge2AI-Voice v4.0.0**, released 2026-10-19, has 1,370 participants and 48,226 recordings (189.7 hours), with derived audio features and detailed phenotype/task metadata. It includes 23 participants with Spanish-language protocol recordings, but this fact alone does not establish an adequate Spanish-speaking PD cohort. The release excludes original audio; raw-audio access requires institutional sign-off. The dataset is credentialed-access and requires a data-use agreement. [Official dataset page](https://www.physionet.org/content/b2ai-voice/4.0.0/).
- **Bridge2AI demographic confounding analysis** by Shukla et al. (2026) already studies age confounding in an earlier Bridge2AI release. [Full text](https://pmc.ncbi.nlm.nih.gov/articles/PMC13492483/). A new analysis using v4 needs a clear reason beyond repeating the v3 analysis; version changes and reprocessed features may support a specific version-sensitivity study, but only after cohort labels and identifiers are checked.

## 3. Dataset feasibility matrix (provisional)

This is a triage table, not a verified download/access audit. Access, exact licenses, IDs, and metadata must be checked directly before any dataset is approved.

| Dataset / resource | Language(s) | What appears available | Main feasibility risk | Provisional status |
|---|---|---|---|---|
| EWA-DB | Slovak | 956 speakers reported in ParkMAE table; 95 PD / 861 controls; multiple speech tasks; MoCA available | Strong class imbalance; metadata/task harmonization and access terms need checking; mixed diagnoses require careful exclusion rules | High-priority candidate to verify |
| ItalianPVS / IPVS | Italian | 59 speakers in ParkMAE table; 27 PD / 32 controls | Very small participant count; confidence intervals likely wide; access/license must be confirmed | Candidate, likely limited power |
| MDVR-KCL / MDVR | UK English | 36 speakers in ParkMAE table; 15 PD / 21 controls; reading and other speech | Very small cohort; results highly uncertain; access and task comparability need checking | Candidate, limited power |
| NeuroVoz | Castilian Spanish | 105 speakers in ParkMAE table; 50 PD / 55 controls; corpus paper reports a Spanish speech corpus | Need verify current raw-audio download/access and license; task and demographic differences can confound language | Candidate, high priority to verify |
| Oxford Parkinson’s voice features | English (feature dataset) | Engineered acoustic features, repeated recordings per participant | Small number of participants; participant-level split essential; not raw audio and may not support speech-encoder experiments | Useful for leakage/reproducibility baseline only |
| Sakar / UCI biomedical voice features | English (feature dataset) | Engineered acoustic features with repeated measurements | Different feature implementation and cohort from Oxford; recent transfer paper reports a feature-sign reversal | Useful for methodological baseline only |
| Adnan/PARK speech-fusion extracted features | English | De-identified extracted embeddings/features and model code | Original audio unavailable; features tied to a specific pipeline and cohort; overlap with original analysis must be respected | Potential reproduction/extension only |
| Bridge2AI-Voice v4.0.0 | Mostly English; Spanish protocol recordings also present | Derived audio features, transcripts for eligible tasks, detailed metadata; 1,370 participants overall | Credentialed access/DUA; no raw audio on PhysioNet; must confirm PD case count and usable control group for exact task; v4 features differ from earlier versions | Possible feature-based study if access and labels fit |
| mPower | US English | Large mobile voice dataset, including sustained vowel recordings | Self-reported diagnosis and task/recording limitations; need assess current access/license and participant-level label quality | Candidate for sensitivity analysis, not automatic gold standard |
| PVA / Parkinson Voice Initiative | English | ParkMAE table reports 620 PD participants, no healthy controls | Cannot support ordinary PD-vs-control binary classification by itself; may be useful for severity/medication questions | Not eligible for primary binary endpoint alone |

Dataset counts above are drawn from the ParkMAE evaluation table and dataset sources; they are not necessarily the complete source-cohort counts and should be rechecked in the original dataset documentation.

## 4. What gap might still be defensible?

A broad cross-language model benchmark is no longer a defensible novelty claim. A broad fairness study or “we use GroupKFold” is also insufficient.

A more specific candidate to test against the remaining literature is:

> **Under participant-level external validation, how do probabilistic calibration and clinically relevant screening operating points change across public Parkinson’s speech datasets, and can simple post-hoc recalibration improve probability reliability without changing the underlying model ranking?**

This is only a **candidate question**, not a novelty claim. It must be checked against recent work including multimodal remote screening papers, the newest cross-corpus work, and any supplementary methods not yet fully reviewed. It is feasible only if at least two or three independent datasets provide compatible binary labels, participant identifiers, and out-of-sample predictions.

Potential outcomes:
- Discrimination: AUROC and area under the precision-recall curve.
- Clinical operating point: sensitivity, specificity, PPV and NPV at a threshold chosen on validation data, not the test set.
- Probability reliability: Brier score and calibration plots; calibration intercept/slope or ECE only where sample size and method make them meaningful.
- Robustness: bootstrap confidence intervals at the participant level; compare source-domain and external-domain performance.
- Optional subgroup analyses only where sample sizes support meaningful estimates.

Caution: the probability of PD in a case-control dataset may be determined by study recruitment rather than real-world prevalence. PPV, NPV, and probability calibration therefore cannot be assumed to transport directly to a screening population.

## 5. Go/no-go criteria before protocol finalization

Proceed with an empirical benchmark only if:
1. At least two independent datasets can be accessed legally and their PD/control labels are documented.
2. Participant IDs permit participant-level splits and aggregation of repeated recordings.
3. We can harmonize at least one speech task or explicitly frame the comparison as combined dataset/domain shift.
4. Metadata permit basic audit of age and sex, or we clearly state that subgroup bias cannot be evaluated.
5. We can retain an untouched external test set and estimate uncertainty at participant level.
6. A paper-by-paper novelty table confirms that the exact proposed endpoint/analysis is not already reported.

If these conditions fail, pivot to a carefully documented systematic/scoping review or a methodological replication rather than claiming an underpowered or confounded empirical discovery.

## 6. Next steps

1. Inspect the source PDF from Puerta Acevedo et al. (2025) and confirm its complete ten-corpus list.
2. Check the official access pages/licenses for EWA-DB, ItalianPVS, MDVR-KCL, and NeuroVoz.
3. Review the code/model card of Ganatra and the full supplement/code for ParkMAE and Adnan et al.
4. Search specifically for calibration intercept/slope, Brier score, ECE, and decision-curve analysis in voice-only PD screening papers published through 2026.
5. Create a final evidence table with exact endpoint, participant count, validation unit, external test, uncertainty, calibration, demographic analysis, and code/data access.
6. Only then decide the protocol and prespecified analysis plan.
