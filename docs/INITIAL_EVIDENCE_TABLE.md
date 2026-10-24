# Initial evidence table

**Search date:** 2026-10-25  
**Status:** Targeted preliminary audit. Not a systematic review; search strings, screening, and full-text extraction remain incomplete.

## Closest studies and resources

| Study/resource | Verified details from source | Why it matters | Remaining appraisal questions |
|---|---|---|---|
| Lim et al. *A cross-language speech model for detection of Parkinson's disease*. Journal of Neural Transmission. Published online 2024-12-30; 2025;132(4):579-590. DOI: 10.1007/s00702-024-02874-z. [Publisher](https://link.springer.com/article/10.1007/s00702-024-02874-z) | Develops a cross-language PD speech model using Taiwanese and Korean speech datasets. | Establishes that cross-language PD modelling is not itself new. | Extract exact sample sizes, language/task mapping, train/test direction, subject independence, metrics, uncertainty, and data/code availability from full text. |
| Ando et al. *ParkMAE: a cross-linguistic masked autoencoder framework for robust Parkinson's disease detection from speech*. Scientific Reports 16, 783 (2026); published 2025-12-10. DOI: 10.1038/s41598-025-30251-7. [Publisher](https://www.nature.com/articles/s41598-025-30251-7) | Reports approximately 750 hours of multilingual pretraining data and 100 hours of evaluation across four languages; reports 39% F1 for cross-linguistic diagnosis and evaluation of unseen languages without language-specific fine-tuning. | Directly overlaps the initial cross-language proposal. A new study must offer a different question or a clearly justified independent benchmark. | Check language/task-specific results, splits, participant overlap, comparator settings, confidence intervals, code/data access, and how “unseen language” is defined. Do not compare F1 with AUROC as if interchangeable. |
| Shukla et al. *Demographic Confounding in Voice-Based Parkinson Disease Screening: Methodological Analysis of the Bridge2AI Voice Dataset*. Journal of Medical Internet Research. 2026;28:e95609. DOI: 10.2196/95609. [Publisher](https://www.jmir.org/2026/1/e95609) | Uses participant-level 5-fold CV and age/sex baselines on Bridge2AI v3.0.0. Full cohort: age-only AUC 0.875 vs AST AUC 0.843 for PD (not statistically distinguishable). Age/site-restricted analyses lower performance; reports preprocessing sensitivity. | Demographic-only baselines, age restriction and dataset shift have already been investigated on this dataset. Repeating only those analyses on the same release is unlikely to be novel. | Assess whether a new question can be answered with independent data, additional variables, a prespecified external validation, or a different justified methodological contribution. Examine shared control cohort and limitations. |
| Bensoussan et al. *Bridge2AI-Voice: An ethically-sourced, diverse voice dataset linked to health information*. PhysioNet release v4.0.0 (2026-10-19). [Official dataset page](https://www.physionet.org/content/b2ai-voice/4.0.0/) | v4.0.0 reports 1,370 participants overall, 48,226 recordings, with updated quality review and some Spanish-language recordings. Access is restricted to credentialed users under a data-use agreement; the PhysioNet resource contains derived features, while raw audio access uses a separate process requiring institutional sign-off. | Potentially useful for within-dataset confounding and selected language analyses, but not automatically a balanced multilingual cohort. | Verify current v4 files, PD diagnosis labels and counts, Spanish speaker/diagnosis cross-tabulation, participant overlap, and access approval. Do not assume Spanish subgroup supports robust external cross-language validation. |
| *NeuroVoz: a Castillian Spanish corpus of parkinsonian speech*. Scientific Data (2024). [Publisher](https://www.nature.com/articles/s41597-024-04186-z) | 112 native Castilian Spanish speakers: 54 with PD and 58 healthy controls; source reports an age difference between groups (PD mean 71.13, control mean 64.04 years). | Potential Spanish-language data resource; age imbalance must be considered. | Verify actual download/access terms, speech tasks, participant-level metadata, recording structure, and whether comparable English or other-language cohorts exist. |
| Bridge2AI-Voice project documentation. [Dataset overview](https://bridge2ai.org/datasets/) | Describes adult dataset versions, multiple North American clinical sites, derived voice features and clinical/demographic information. | Useful source for current release selection and dataset provenance. | Pin the exact version used; do not mix versions without a documented compatibility plan. |

## Preliminary synthesis

1. **Cross-language generalization alone is not a defensible novelty claim.** At least two directly relevant peer-reviewed papers have been identified: Lim et al. and ParkMAE.
2. **Demographic confounding on Bridge2AI is also directly studied.** A project that only repeats age-only baselines on the same release is unlikely to contribute enough by itself.
3. **A possible direction remains conditional:** a prespecified, independent and participant-level benchmark that evaluates demographic confounding, calibration and recording/domain shift across compatible datasets. This is only a candidate; feasibility and novelty require further checking.
4. **Language, site, task and dataset can be confounded.** If each language comes from a different dataset/site/task, performance differences cannot be attributed to language alone.
5. **Data access is a gating issue.** Bridge2AI adult access is restricted and raw audio access has additional requirements. NeuroVoz and any comparison datasets need official access/licensing checks.
6. **No experiments have been run.** Values above are reported from the cited publications, not results from this project.

## Next extraction tasks

- [ ] Read the full methods and supplements of Lim et al.
- [ ] Read ParkMAE methods, dataset table, split protocol and code availability.
- [ ] Read the full JMIR methods and limitations; inspect its supplementary review of prior voice-PD studies.
- [ ] Check Bridge2AI v4.0.0 phenotype, recording, language and data-access documentation.
- [ ] Verify NeuroVoz downloadable files and license/access.
- [ ] Search additional literature on cross-dataset validation, calibration, demographic fairness, and speech acquisition shift.
- [ ] Update the research question only after this comparison.
