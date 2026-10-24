# Route A prior-art audit: label-free reliability and abstention

**Audit date:** 2026-10-25  
**Status:** Targeted search only; not a completed systematic review.  
**Decision:** The original idea is plausible as a PD-voice application, but it is **not cleared as methodologically novel**. Do not describe it as the first label-free reliability or abstention framework.

## Question being tested

Can unlabeled target recordings provide warning signals that a Parkinson's disease (PD) voice classifier is likely to fail when moved to a new corpus, and can a deferral policy chosen without inspecting target labels reduce errors among predictions retained for display?

This remains a hypothesis. No dataset has yet been analyzed and no model has been trained.

## Closest prior art and overlap

| Work | What it already establishes | Implication for our proposal |
|---|---|---|
| Kiyasseh et al., SUDO, *Nature Communications* (2024), DOI [10.1038/s41467-024-46000-9](https://www.nature.com/articles/s41467-024-46000-9) | Uses unlabeled deployment data and pseudo-label discrepancy to estimate reliability, identify unreliable predictions, rank models, and examine bias without target ground truth. Tested on dermatology images, histopathology, and clinical notes. | **Major conceptual overlap.** “Label-free reliability monitoring plus triage/abstention” is not a new general method. A PD speech study must explicitly compare against SUDO or explain why it cannot be applied. |
| “Selective Classification Under Distribution Shifts,” TMLR (2024; full text available via PMC) | Studies selective prediction when deployment distribution shifts; abstention is an established strategy. [Article](https://pmc.ncbi.nlm.nih.gov/articles/PMC12470254/) | Risk–coverage analysis and abstention alone are not novel. |
| “Out-of-Distribution Detection as a Risk-Control Strategy for Medical Classification Machine Learning Models” (2025/2026 record) | Evaluates OOD detection as a risk-control strategy across medical classification settings. [PubMed record](https://pubmed.ncbi.nlm.nih.gov/41127928/) | Medical OOD-triggered deferral is already an active general approach. Need a specific empirical gap, not simply a new disease label. |
| Shahriar, “Uncertainty-aware personalized estimation of Parkinson’s disease severity from longitudinal speech,” *PLOS ONE* (2026), DOI [10.1371/journal.pone.0343191](https://journals.plos.org/plosone/article?id=10.1371/journal.pone.0343191) | Uncertainty-aware speech-based PD severity estimation, mainly a longitudinal severity task rather than binary screening. | PD voice uncertainty already has direct precedent, though the task differs. |
| “Beyond Accuracy: Enhancing Parkinson’s Diagnosis with Uncertainty Quantification of Machine Learning Models” (2026) | Applies uncertainty quantification to PD diagnosis across modalities including voice. [PMC article](https://pmc.ncbi.nlm.nih.gov/articles/PMC12718125/) | Generic uncertainty quantification in PD is not novel. Check the full method before defining our comparison set. |
| Guo et al., “A Biocybernetic System for Quantifying Parkinsonian Motor Impairment from Voice with Uncertainty-Aware Closed-Loop Monitoring” (2026), DOI [10.1007/s40846-026-01040-y](https://doi.org/10.1007/s40846-026-01040-y) | Uncertainty-aware voice monitoring with Spanish training and Italian external validation. | Further evidence that uncertainty-aware PD voice evaluation exists; compare the endpoint and deployment assumptions carefully. |
| ParkMAE, *Scientific Reports* (online 2025; volume 2026), DOI [10.1038/s41598-025-30251-7](https://www.nature.com/articles/s41598-025-30251-7) | Multilingual representation learning and leave-one-corpus/language-out PD speech evaluation. | Cross-language/corpus transfer is not novel by itself. |
| Hossain et al., *Scientific Reports* (2026), DOI [10.1038/s41598-026-76171-y](https://www.nature.com/articles/s41598-026-76171-y) | Cross-corpus feature stability, external tests and reported probability-calibration metrics. | Cross-corpus robustness and calibration already overlap with the broader problem. Re-check exact final version and methods during full review. |
| Ahammad, *Digital Health* (2026), DOI [10.1177/20552076261467837](https://pmc.ncbi.nlm.nih.gov/articles/PMC13346734/) | Cross-dataset PD speech framework with explainability, federated simulation and Brier-score reporting. | Generalization and calibration are not new alone. |
| Twala (2026), reproducibility report [Zenodo record](https://zenodo.org/records/22735799) | Reports inflation from non-grouped splits and severe failures in some cross-dataset models. | Subject grouping and cross-dataset testing are necessary, but not a sufficient novelty claim. |

## What remains potentially defensible

The defensible contribution, if data access and a broader search support it, is a **carefully controlled comparative benchmark in PD voice screening**, not a new general theory of label-free AI reliability:

1. Compare a prespecified set of unlabeled-target diagnostics (e.g., acoustic feature shift, representation-space distance, predictive entropy/margin, model disagreement, and a SUDO-style score) against the *observed* external performance degradation of a source-trained PD voice model.
2. Evaluate whether each warning score adds information beyond simple confidence and source-validation performance, using held-out target corpora and strict no-target-label tuning.
3. Assess whether a deferral rule fixed using source validation reduces error among covered participants, while reporting coverage, sensitivity, specificity, calibration where estimable, and uncertainty.
4. Quantify whether deferral rates differ by sex, age, language/corpus, severity or other available subgroups; show uncertainty and avoid treating missing subgroup metadata as evidence of fairness.
5. Explicitly document confounding: language, site, task, microphone, recruitment and diagnosis mix may be inseparable. If so, call it **cross-corpus/domain generalization**, not an isolated causal effect of language.

This may be useful as a disease-specific benchmark, but whether it is sufficiently novel for publication is unresolved. If SUDO or another prior method already covers the exact operational evaluation after closer inspection, narrow the work to a head-to-head benchmark and reproducibility study, or pivot to a review if compatible datasets cannot be accessed.

## Design cautions that materially affect validity

- **Unit of analysis:** participant, not recording, window or repeated feature row. Aggregate repeated recordings with a prespecified rule; keep all recordings from one participant in the same split.
- **External validation:** source train/validation and target test must be separated by corpus and participant. Do not use target diagnostic labels for threshold selection, feature selection, calibration, warning-score tuning or model selection.
- **Target labels in retrospective research:** labels may be used *after* all decisions are frozen to evaluate whether the warning score predicted failure. They must not leak into the warning policy.
- **Define “failure” before looking at target results:** choose a clinically interpretable source-selected operating threshold (with a sensitivity target if feasible) and prespecify the primary external endpoint. AUROC alone can conceal a dangerous sensitivity collapse.
- **Small cohorts:** several corpora have few participants. Use participant-level uncertainty intervals, show denominators, avoid overinterpreting subgroup rankings, and treat estimates from tiny test cohorts as exploratory.
- **Abstention is not automatically safe:** report the errors among covered cases *and* how many/which participants are deferred. Unequal deferral can shift harm rather than remove it.
- **SUDO feasibility:** its published procedure uses unlabeled target predictions but also relies on labeled reference data and a held-out evaluation step to assess pseudo-label classifiers. Reproduce the published method faithfully; do not call it “fully label-free” in the sense that no labeled reference set is needed.
- **Clinical claim:** retrospective public-dataset results can support a methodological proof-of-concept only. They cannot establish safety, clinical utility or prospective deployment readiness.

## Search scope and limitations

This pass used targeted web searches for PD speech label-free reliability, selective prediction/abstention, clinical speech domain shift, SUDO, and medical OOD risk control. It identified important direct and adjacent precedents above. It was **not** a registered or exhaustive search: databases such as PubMed/MEDLINE, Scopus, Web of Science, IEEE Xplore, ACM Digital Library and conference proceedings have not all been systematically searched, deduplicated or screened. Search terms, date ranges and all exclusions still need to be logged in the full search workflow. No “first study” or “first method” claim is warranted.

## Go/no-go decision

**Current decision: conditional go for feasibility work; no-go for claiming novelty or training a final model yet.**

Next gates:
1. Run the complete structured prior-art search and add every close result to the comparison matrix.
2. Inspect SUDO methods and implementation closely and determine whether a faithful baseline is feasible for the small multi-corpus setting.
3. Confirm lawful access, participant IDs, compatible labels, metadata and audio/features for at least two or preferably three independent cohorts.
4. Write a protocol with one primary endpoint, source-only tuning, sample-size/precision limitations, and subgroup deferral analysis before running the confirmatory benchmark.
5. If these gates fail, pivot transparently to a systematic/scoping review or a reproducibility study rather than manufacturing a broader claim.
