# Route A proposal: Label-free reliability monitoring for Parkinson voice AI under domain shift

**Version:** 0.2 (revised after expanded prior-art audit)  
**Date:** 2026-10-25  
**Status:** Revised candidate only. Novelty is NOT established and the dataset gate is not passed. No experiments have been run.

## Working title

**Can We Know When a Parkinson’s Voice Model Should Abstain? A Label-Free Audit of Reliability Under Cross-Dataset Shift**

Alternative, more technical title:
**Predicting Cross-Corpus Failure in Voice-Based Parkinson’s Screening Using Unlabeled-Target Shift Diagnostics and Selective Prediction**

## 1. Why this direction?

Recent PD voice papers already study cross-language models, domain adaptation, cross-corpus feature stability, demographic confounding, uncertainty estimation, and cross-dataset evaluation. Therefore a new classifier, a multilingual benchmark, or a generic calibration analysis would be weak novelty claims.

The proposed shift is to study a different deployment question:

> Before diagnostic labels from a new target population are available, can measurable properties of its voice data warn us that a source-trained PD screening model may be unreliable, and can an abstention policy reduce harmful confident errors?

The clinical value is not that the algorithm claims to diagnose PD autonomously. It would flag recordings/domains where the model should not issue a confident screening result and should instead defer to clinical assessment or a validated workflow.

## 2. Novelty audit: what already exists?

### Directly relevant PD literature
- Lim et al. (2025) studied a cross-language speech model, but did not establish a general label-free warning system for when an external model should abstain.
- ParkMAE (2026) evaluated leave-one-language-out generalization.
- Hossain et al. (2026) studied cross-corpus feature stability and included probability calibration.
- Ahammad (2026) studied cross-dataset transfer, feature harmonization and Brier score.
- Ganatra (2026) studied zero-shot transfer, target-domain adaptation and sex-specific false-negative differences.
- Shukla et al. (2026) studied age/site confounding in Bridge2AI Voice.
- Recent PD work also evaluates uncertainty estimation; therefore uncertainty estimation alone is not novel.
- Twala’s 2026 reproducibility report shows serious participant-split and cross-dataset transfer failures on Oxford/Sakar feature data.

### Adjacent methodological literature
- Kiyasseh et al. (2024) proposed SUDO, a framework for evaluating clinical AI systems without target ground-truth labels: https://www.nature.com/articles/s41467-024-46000-9
- Selective classification under distribution shift has been studied more generally: https://pmc.ncbi.nlm.nih.gov/articles/PMC12470254/
- Out-of-distribution detection as a risk-control strategy has been evaluated on several medical modalities: https://pubmed.ncbi.nlm.nih.gov/41127928/
- Domain-shift detection in speech enhancement has also been studied, though its task and failure definition differ from PD screening: https://link.springer.com/article/10.1186/s13636-026-00448-3

**Important limitation:** an initial targeted search did not identify a directly matching PD-voice paper that systematically compares label-free target-domain warning scores against observed external clinical failure and tests a predeclared abstention policy. This is not enough to claim priority. We must conduct a broader search across OOD detection, selective prediction, uncertainty estimation, speech biometrics, and clinical deployment monitoring before asserting novelty.

## 3. Proposed research question

**Primary RQ:** Across independent Parkinson speech datasets, how well do unlabeled-target shift indicators predict when a source-trained model’s participant-level screening performance will deteriorate, and does a source-validated abstention policy reduce high-confidence errors at an acceptable coverage cost?

### Secondary questions
1. Which shift indicators are most useful: embedding-distance scores, simple acoustic feature shift, prediction entropy/margin, model disagreement, or a label-free target evaluation criterion inspired by SUDO?
2. Do shift warnings identify genuine performance degradation better than source-domain confidence alone?
3. Does abstention improve risk among the retained predictions, and what fraction of participants must be deferred?
4. Are warnings driven by language-associated domain shift, recording task, sex/age composition, or dataset identity?
5. Does the result persist across different feature families and more than one source/target direction?

## 4. Hypotheses (provisional)

- **H1:** At least one prespecified unlabeled-target warning score predicts external degradation better than source validation performance alone.
- **H2:** A warning/abstention policy chosen only on source validation data reduces participant-level error among predictions retained for automated output, with a measurable coverage cost.
- **H3:** Warning performance varies by type of shift; a single global score may not reliably identify every failure mode.

These are hypotheses, not findings. Null results are scientifically useful.

## 5. Study design

Retrospective multi-corpus benchmark with strict participant-level splits and leave-one-dataset-out/external evaluation. No new patient recruitment is assumed. The design proceeds only if at least two independent corpora are legally accessible and contain usable participant-level labels; three or more independent corpora are strongly preferred for testing more than one source/target direction.

### Unit of analysis
Primary unit: participant. If multiple tasks/recordings exist, aggregate according to a rule prespecified using training data only. Keep participant, recording, task, dataset and language identifiers separate.

### Baseline PD classifiers
Start with interpretable, reproducible baselines:
- logistic regression or linear SVM on a harmonized set of acoustic features;
- gradient-boosted trees on the same features;
- if legal raw audio and adequate compute are available, a frozen pretrained speech embedding plus a small classifier.

Do not begin by training a large neural model. First establish data integrity and reproduce a published baseline.

### Unlabeled-target shift indicators
Prespecify a small, interpretable family:
1. **Acoustic shift:** distance between source-training and target feature distributions (for example, standardized mean differences and a multivariate distance).
2. **Embedding shift:** distance from target representations to source-training representation support.
3. **Prediction uncertainty:** entropy or probability margin; this is a confidence baseline, not a sufficient OOD detector.
4. **Model disagreement:** variance across independently trained source-only models/seeds, if feasible.
5. **Label-free target evaluation score:** assess whether a method inspired by SUDO can be adapted to the binary PD speech setting without target labels. Any adaptation must be specified transparently and must not be tuned on target diagnostic labels.

Avoid selecting the best detector using the same external test outcomes and then reporting that result as independent validation. Use nested source validation and a held-out external domain for final evaluation.

### Defining “external failure”
Predefine degradation relative to source validation in clinically meaningful metrics, such as sensitivity at a source-selected operating threshold and balanced accuracy. Do not define failure using AUROC alone. The exact margin must be chosen before looking at target labels and justified clinically/statistically; conduct sensitivity analyses for alternative margins.

### Abstention policy
A source-validation-selected rule may return:
- **screening result eligible for display**, or
- **defer / out-of-scope; do not return an automated screening classification**.

The rule must be selected using source validation only. Report:
- coverage (fraction not deferred);
- error among covered participants;
- sensitivity and specificity among covered participants;
- coverage-risk curve;
- number and demographic composition of deferred participants;
- uncertainty intervals resampled at participant level.

An abstention system is not clinically safe merely because it reduces error: it could disproportionately defer a language or demographic subgroup. Report coverage by available subgroup and uncertainty.

## 6. Data feasibility gate

Candidate datasets are not automatically approved:
- **MDVR-KCL** and **ItalianPVS** are lower-friction raw-audio candidates but small.
- **EWA-DB** requires a request/license; the audio subset is smaller than the full metadata cohort.
- **NeuroVoz** is access-restricted.
- **PC-GITA** and **ParkCeleb** may require institutional/author access.
- **Bridge2AI Voice** requires credentialed access/DUA; public v4 provides derived features, while raw audio has separate institutional sign-off.
- Oxford/UCI datasets are engineered-feature cohorts and may help validate split/metric code but cannot by themselves test raw-audio cross-language shift.

Proceed only after verifying license, participant IDs, diagnosis labels, tasks, age/sex metadata, number of unique participants per class, and permitted derived outputs. If fewer than three independent domains are feasible, re-scope and clearly state that the evidence is a limited pilot; do not claim broad multilingual generalization.

## 7. Statistical analysis plan (draft)

Primary:
- participant-level sensitivity at a prespecified source-derived threshold;
- balanced accuracy;
- external degradation versus source-validation estimate;
- AUROC as secondary discrimination metric;
- warning-score association with external performance degradation across source/target domain pairs;
- risk-versus-coverage curve and coverage at a fixed maximum tolerated error chosen before external testing.

Secondary:
- specificity, PPV/NPV with explicit caveats about case-control prevalence;
- calibration metrics only if probability predictions and sample size support them;
- subgroup coverage/error by age and sex when metadata and denominators permit;
- dataset-only and demographic-only baselines to expose shortcuts;
- matched-task sensitivity analyses where task overlap allows it.

Use participant-clustered bootstrap intervals. With very few datasets, do not pretend dataset-pair observations are independent or fit an overparameterized regression to them. Treat domain-pair results as small-sample evidence and report all directions, not only the best one.

## 8. Threats to validity

- Language is often confounded with site, task, device and recruitment. Use “dataset/domain shift” unless design supports a language-specific interpretation.
- A model can fail because labels, task, preprocessing or measurement implementations differ, not only because of language.
- A dataset-level shift score can detect obvious source differences but may not predict whether the differences are clinically harmful.
- A label-free score may be miscalibrated when target class prevalence changes.
- Small public corpora create wide uncertainty intervals and unstable subgroup estimates.
- Repeated recordings/windows can leak identity if splits are not participant-grouped.
- Retrospective benchmark results do not prove prospective clinical safety or clinical utility.

## 9. Predefined success/failure interpretation

A positive result would require:
1. warning scores evaluated on multiple held-out domain pairs;
2. superiority to a simple source-performance/confidence baseline, with uncertainty;
3. reduced error among covered participants at a predeclared coverage level or a meaningful risk–coverage improvement;
4. no unreported severe subgroup coverage penalty;
5. fully reproducible code and an independent test domain untouched during model/rule selection.

A negative result is also publishable if warning scores do not predict failure, or if no abstention rule achieves an acceptable risk–coverage trade-off. Do not redefine success after seeing results.

## 10. Novelty gate before implementation

Before claiming novelty:
- Search PubMed, Europe PMC, Scopus, Web of Science, IEEE Xplore, ACM DL, arXiv and citation graphs using combinations of “Parkinson speech/voice,” “label-free evaluation,” “out-of-distribution,” “domain shift detection,” “selective prediction,” “abstention,” “risk-coverage,” “SUDO,” “uncertainty,” and “unlabeled target.”
- Review supplementary methods and code for ParkMAE, Hossain et al., Ahammad, Ganatra, recent PD uncertainty papers and all identified general medical OOD/abstention work.
- Verify whether any existing PD speech study has already tested whether an unlabeled-target score predicts observed external clinical failure and used it to trigger abstention.
- If direct overlap is found, change the question or explicitly frame the work as replication/benchmarking.
- Do not write “first,” “novel,” or “new to science” in the title/abstract until the search is documented and a supervisor/librarian-level review supports it.

## 11. Feasibility decision

**Current decision: GO for literature verification and data-access audit; HOLD on model training.**

This is the strongest candidate identified so far for an independent empirical contribution, but it is not yet proven novel and may fail the data-feasibility gate. First secure legal access to enough independent datasets, then lock the analysis plan, version it in GitHub, and run a small data-integrity pilot before any confirmatory experiment.

No project results have been generated.


---

## Version 0.2 — decision update after the 2026-10-25 prior-art audit

### What changed

The direct and adjacent prior art is broader than the first proposal captured. PD-specific papers now cover leave-one-dataset-out testing, zero-shot transfer, limited target-data adaptation, sex-stratified false-negative rates, cross-corpus feature stability, probability calibration and uncertainty-aware Spanish-to-Italian voice assessment. A public GitHub project also describes acoustic shortcut controls and IPVS/MDVR-KCL cross-corpus modeling. General methods include SUDO, D3M disagreement-driven degradation monitoring, selective classification under distribution shifts and label-free estimation of clinically relevant performance metrics.

Therefore, the project must not be framed as inventing label-free reliability monitoring, OOD detection, or abstention. The candidate is a **disease-specific comparative benchmark of existing monitors**, if a complete prior-art search and data gate justify it.

### Revised primary question

> On independent Parkinson speech corpora held out from model development, do prespecified label-free monitoring methods identify participant-level errors or batch-level performance degradation better than confidence-only baselines, and what risk–coverage and subgroup-deferral trade-offs result?

Possible future title: **“Do Label-Free Reliability Monitors Predict External Errors in Parkinson’s Voice Screening? A Comparative Multi-Corpus Benchmark.”** This title is provisional and is not a novelty claim.

### Separate primary-analysis levels

1. **Participant-level error detection/selective prediction:** rank individual participant predictions by a prespecified risk score (e.g. confidence/margin, source-reference feature distance, or a valid per-case uncertainty score). After the score/rule is frozen, use target diagnostic labels only to evaluate whether errors were ranked as riskier and assess risk–coverage.
2. **Batch/domain-level performance monitoring:** run a published method such as SUDO, D3M, or a label-free confusion-matrix estimator on an unlabeled target batch/corpus; after the monitor is frozen, reveal target labels for retrospective comparison with actual performance degradation.

These tasks are not interchangeable. The protocol must select one primary endpoint and classify each baseline by its intended operating level. Do not count overlapping random batches from one small dataset as independent target domains.

### Method shortlist, not yet locked

- Confidence-only baseline: maximum predicted probability, class margin or entropy.
- Input-level shift baseline: a prespecified distance between source and target acoustic distributions; representation distance only with a fixed, documented encoder.
- Batch-level disagreement monitor: D3M or a faithful disagreement-rate baseline.
- One label-free performance estimator: SUDO or the Flühmann-style confusion-matrix estimator, selected after checking code, assumptions and sample-size feasibility.

The shortlist should remain small. Implement methods faithfully and do not tune them against target labels. An unlabeled-target method can still require labeled source/reference data; describe this precisely.

### Data gate and analysis safeguards

No confirmatory training until at least three independent, legally accessible cohorts with participant-level PD/control labels and compatible inputs are verified; four is preferable. The n=50 Italian cohort used by a recent uncertainty-aware paper may overlap with the standard ItalianPVS subset. UNLaM has a 119-vs-126 count discrepancy. Bridge2AI v3 and v4 are not independent cohorts. See [dataset feasibility gate](DATASET_FEASIBILITY_GATE.md).

Predefine thresholds on source data only. Keep all recordings from each participant together. Use participant-level outcomes and uncertainty. Report all source-to-target directions, sensitivity at the chosen threshold, specificity, balanced accuracy, AUROC as secondary, risk–coverage, subgroup coverage/deferral and negative controls. Describe combined dataset/domain shift where language is confounded with site, device, task or recruitment.

### Decision

**Proceed:** full literature verification, implementation-method review and lawful data-access verification.  
**Hold:** final protocol lock, model training and any “first-of-its-kind” claim.

If the dataset gate fails, pivot to a transparent two-corpus pilot or a review/reproducibility project. Do not claim the intended multi-corpus study is complete unless its data and design requirements are met.


## Version 0.2 addendum — broader domain-adaptation prior art

The latest targeted pass also found Siniukov et al. (2025) on HuBERT-based multilingual adaptation, Ibarra et al. (2023) on corpus/language-independent screening and shortcut reduction, and Francesconi et al. (2026) on fairness-aware partial-label voice-domain adaptation. These make broad claims about cross-language robustness, domain adaptation, fairness-aware representations or shortcut mitigation even less defensible as standalone novelty.

The updated decision is unchanged: test existing label-free monitors as an empirical comparative benchmark only if data feasibility is confirmed. The method comparison must include or justify excluding relevant existing approaches; the paper must remain honest if the result is a replication or domain-specific evaluation rather than a methodological invention.


---

## Version 0.3 — primary question narrowed after deeper prior-art and data audit

The primary endpoint is now **participant-level error detection** under held-out dataset shift, not a combined test of participant-level deferral and batch-level performance monitoring.

**Revised primary RQ:** In sustained-vowel Parkinson’s voice screening, do label-free confidence and acoustic/representation-distance scores identify incorrect predictions on a held-out data source better than confidence alone, and what error–coverage and subgroup-deferral trade-offs result?

Why narrow it:
- The general idea of label-free monitoring is established by SUDO and D3M; OOD risk control has been evaluated in medical classification, including PD-related smartphone activity data, though not specifically in PD voice-screening.
- Three or more target corpora provide too few independent observations for a strong claim about a general batch-level monitoring law; overlapping bootstrap batches do not solve this.
- A per-participant risk-score benchmark can be evaluated against held-out errors after the score is frozen, without allowing target labels into inference/tuning.

Primary dataset task is sustained /a/ because two openly posted raw-audio sources (ItalianPVS and UAMS Figshare) explicitly include comparable prolonged/sustained vowels. This is a pilot setup only: a third independent cohort is not yet verified, and cohort counts/IDs must be audited locally before confirmatory experiments.

See the final research decision memo for the full design, prior-art verdict, dataset matrix and go/no-go gates.


## Selected narrowing — 25 October 2026

The one selected primary question is whether **source-reference acoustic-domain distance adds useful information beyond predictive confidence for detecting participant-level errors** on independent held-out PD voice datasets.

The 2026 PARK multimodal PD-screening paper already relates model uncertainty to performance decline, so “uncertainty predicts mistakes” alone is too weak. Our candidate difference is the incremental voice-specific acoustic-distance comparison under held-out voice-corpus evaluation. It is a comparative application study, not a new OOD method. See [SELECTED_RESEARCH_QUESTION.md](SELECTED_RESEARCH_QUESTION.md) for the draft analysis plan and gates.
