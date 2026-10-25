# Research decision memo — 25 October 2026

## Executive decision

**Decision: CONDITIONAL GO for a narrow participant-level empirical benchmark; NO-GO for claiming a new general method or proceeding directly to confirmatory training.**

The initial idea (“label-free monitoring and abstention under cross-corpus shift”) was too broad. Label-free performance monitoring, OOD detection, risk–coverage evaluation, cross-language PD speech detection, domain adaptation, uncertainty-aware voice assessment, and demographic confounding all have prior art.

The targeted search did **not** identify a PD-voice paper that directly evaluates whether label-free, per-participant risk scores predict *which individual voice-screening predictions will be wrong* on independent, held-out corpora and quantifies the resulting error–coverage trade-off. This is a **candidate application-level gap**, not a completed priority search and not a verified novelty claim. General medical OOD work and Parkinson-related monitoring in non-voice modalities are close adjacent work.

The data gate also remains incomplete. Two public raw-audio resources with a common sustained-vowel task are clearly described (ItalianPVS and UAMS Figshare); a third comparable independent cohort is not yet both legally accessible and locally verified. The study should not advance to confirmatory training until this is resolved.

## Revised primary question

> **In sustained-vowel Parkinson’s voice screening, do label-free confidence and acoustic/representation-distance scores identify incorrect predictions on a held-out data source better than confidence alone, and what error–coverage and subgroup-deferral trade-offs result?**

Provisional title:

**“Do Label-Free Risk Scores Identify Wrong Parkinson’s Voice-Screening Predictions Under Dataset Shift? A Participant-Level External Validation Study.”**

This is a focused comparison of existing methods, not a proposed novel algorithm. The manuscript must avoid “first,” “novel,” “clinically safe,” or “language-invariant” claims unless later evidence supports them.

## Why this is the best current question

1. It preserves the project’s priorities: cross-language/domain generalization, demographic bias, and clinical reliability.
2. It asks a concrete deployment question: can a model warn that an individual prediction is likely wrong before a clinical reference label is available?
3. It can be answered with reproducible, relatively lightweight acoustic models. A large neural model is not needed to test the primary hypothesis.
4. It is distinct from batch-level monitoring papers such as SUDO/D3M in the primary endpoint, while comparing against general OOD/error-detection principles. Do not convert batch-level method outputs into individual scores without a separately justified method.
5. It can yield a valuable negative result: uncertainty or distance may fail to identify erroneous predictions under corpus shift.

## Critical prior art and implications

- **Cross-corpus PD voice classification is established.** Lim (2025), Ibarra et al. (2023), ParkMAE (online 2025/volume 2026), Hossain et al. (2026), Ganatra (2026), and Şaraldı & Bozdağ Karakeçi (2026) cover multilingual models, domain adaptation, feature stability, target adaptation or leave-one-dataset-out testing.
- **Uncertainty-aware voice PD assessment is established.** Guo et al. (2026) report Spanish-to-Italian external evaluation. Generic uncertainty or calibration cannot be the claim.
- **OOD error detection in health has general precedent.** Weng et al. (2025) compared OOD detectors on three modalities, including Parkinson’s diagnosis from smartphone-rest activity data rather than voice. Park et al. (NeurIPS 2021) also studied dataset-shift detection for health ML including PD-related activity data. D3M (NeurIPS 2025) directly studies unlabeled deployment deterioration; SUDO (Nature Communications 2024) estimates clinical-AI reliability without target labels.
- **A recent PD-voice LODO paper has a useful reproducibility warning.** Şaraldı & Bozdağ Karakeçi (2026-09-30) call some aggregated results “subject-level,” but their methods state that for mPower and MDVR-KCL aggregation is actually at recording level because repeated recordings are treated as independent samples. Their validation split is segment-level, not speaker-level, and they used one random seed. This is a reason for stricter unit-of-analysis standards, not proof that all their results are invalid.
- **Public prior art exists for shortcut audits.** A September 2026 GitHub project describes silence-only controls and cross-corpus acoustic modeling on IPVS/MDVR-KCL. Its metrics have not been independently reproduced here, but duplicating its headline contribution would be unwise.
- **A recent arXiv preprint titled “Label-Free Parkinson’s Disease Screening from Face and Voice through Mechanistic Interpretability” (2026-08-10) also uses “label-free PD screening” in a different sense (no PD labels used to fit a voice/face score).** Distinguish label-free screening from label-free model-performance monitoring.

References and exact links are collated in the updated prior-art review and the primary-study comparison matrix.

## Candidate cohorts and access decision

| Cohort | Useful facts | Data decision |
|---|---|---|
| **ItalianPVS/IPVS** | 65 participants in the full described cohort: 28 PD, 22 elderly healthy controls, 15 young healthy controls; multiple tasks including sustained vowels; the dataset is described as openly available under CC BY 4.0. | Strong candidate. Primary binary analysis should use PD versus elderly controls; keep young controls separate as a sensitivity analysis because age can be a shortcut. The exact files, IDs, task labels and checksums still need local audit. |
| **UAMS Figshare voice samples** | Public Figshare record provides a demographics file with sample IDs/age/sex/labels and phone-recorded prolonged /a/ WAV archives; record advertises a 4.18 MB download under CC BY 4.0. A paper reports 81 voice records (40 PD, 41 healthy controls). | Strong second candidate for sustained /a/. Confirm unique participant count, one-to-one ID mapping, recording multiplicity and label provenance from the actual manifest. |
| **mPower** | Large, remote smartphone study includes sustained-vowel recordings, but diagnosis/recruitment labels differ from tightly controlled clinician-diagnosed cohorts. Research access is through Synapse. | Possible third cohort, but **not approved** until access, terms, speaker IDs and diagnostic label provenance are checked. Treat as an external stress test or sensitivity analysis if label quality is weaker. |
| **UNLaM Argentine Spanish corpus** | Original report describes 55 PD and 64 controls (119 total); a 2026 paper reports n=126 and says the Spanish voice data are available. | Potential multilingual third cohort, but we have not located and verified a direct downloadable, versioned raw-audio manifest. Do not count it as accessible until that link/licence and the 119-versus-126 discrepancy are resolved. |
| **NeuroVoz** | Latest Zenodo v3 record reports 112 participants (54 PD, 58 controls; 2,977 files), but files are restricted. Older v1 lists 108 (53/55; 2,903 files). | Request/approval candidate, not open-by-default. Never mix version counts. |
| **MDVR-KCL** | 37 participants (16 PD/21 controls) in common descriptions, mostly reading and spontaneous speech; raw data are distributed through repository/platform sources. | Useful for a separate connected-speech robustness analysis if licence and manifest are verified, but not the main sustained-/a/ task-matched cohort. |
| **PC-GITA / EWA-DB** | Valuable Spanish/Slovak datasets, but institutional/academic request or licensing restrictions apply. | Access-request candidates only; not assumed available. |
| **Bridge2AI Voice v4.0.0** | 1,370 participants, 48,226 recordings across five sites; derived features on credentialed/DUA access; raw audio has additional institutional sign-off. Only 23 participants completed the Spanish protocol, not automatically a viable Spanish PD/control cohort. | Possible future feature-level study; not necessary for the first pilot and not independent from earlier versions. |

**Current access verdict:** We can name two plausible, openly posted raw-audio sources for a task-matched *pilot*. This is not proof that files have been downloaded or that labels/participant IDs are valid. A broader independent benchmark needs a third cohort and a written data manifest. If that gate fails, limit scope to a two-corpus pilot or switch to a reproducibility review; do not claim broad multilingual validation.

## Prespecified design to take to a supervisor

### Population and task
Retrospective, public-data study of adults with diagnosed PD and non-PD controls. Primary task: sustained /a/ phonation only, if the accepted cohorts have comparable task definitions. This restricts external validity to sustained phonation; no claim about spontaneous conversation follows.

### Models
Start with one transparent primary classifier (regularized logistic regression on a harmonized acoustic feature set) and one secondary classifier (e.g., linear SVM). Use feature extraction in a pinned version of openSMILE eGeMAPSv02 or an equally prespecified package; standardize features using source-training data only. Frozen speech embeddings can be an optional later sensitivity analysis, not a requirement.

### Risk scores (no target labels used to compute them)
- Confidence baseline: 1 minus the maximum predicted class probability, plus margin/entropy as secondary confidence measures.
- Input/representation-distance score: distance to source-training support, e.g. a prespecified standardized-feature k-nearest-neighbour or class-conditional Mahalanobis distance.
- Optional ensemble disagreement only if multiple source-trained models can be fit without leakage and the score is frozen before target labels are revealed.

Avoid a large menu of detectors; compare a small set faithfully.

### Splits and analysis
- Unit of inference: **participant**, never clip, frame, segment or feature row.
- All recordings from a participant must remain in one split; aggregate recording predictions by a prespecified rule.
- Source-side training, preprocessing, calibration and model selection are completed without target participants/labels. External corpus labels are held out until the monitor scores and analysis code are frozen.
- For each external participant, compute the base classifier prediction and a risk score. Only then use the hidden label for retrospective evaluation of whether the score predicts mistakes.
- Primary endpoint: AUROC of each risk score for distinguishing incorrect from correct external participant predictions, with participant-bootstrap confidence intervals and baseline-paired comparisons.
- Key secondary outcome: error-versus-coverage curves, error among retained cases at prespecified coverages, and sensitivity/specificity among retained cases. Coverage is a methodological trade-off, not automatically clinically acceptable.
- Report all source/target directions; do not select the best one and hide the rest.
- Subgroup checks by age and sex only when the sample counts support interpretable estimates; report denominators and wide intervals. A high deferral rate for a group is a potential harm, not proof of fairness.
- Dataset-level monitoring (SUDO/D3M) may be explored separately only if there are enough independent target batches/domains and a faithful implementation. It is **not** the primary endpoint in this version because only a few real corpora create weak statistical support for correlating batch-level alarms with performance drops.

### Negative controls and robustness
- Demographic-only baseline where age/sex is available.
- Recording-quality metadata or simple technical-feature baseline if licensing/metadata permit.
- Match sustained /a/ task duration where possible and log sample-rate/resampling method.
- Audit label definitions and diagnosis provenance per source.
- Sensitivity analyses including/excluding young controls, and report when “language” is confounded with site, device, task or recruitment.
- No target-label-based threshold selection, calibration, tuning or feature selection.

### Interpretation
The study can show that a risk score predicts error in these datasets; it cannot prove clinical safety or future deployment performance. With small cohorts, treat the study as an external-validation pilot and show uncertainty rather than overstate precision.

## Go/no-go gates

**Gate 1 — Prior art:** targeted searches found meaningful direct/adjacent work. The revised application-level question remains plausible but not cleared. Finish PubMed/MEDLINE, Europe PMC, IEEE Xplore, ACM DL, arXiv and citation chaining before writing a priority claim.

**Gate 2 — Data:** not yet passed. Verify the two candidate file manifests and establish at least one additional independent, lawful, task-compatible cohort (preferably mPower after appropriate access/label audit, or UNLaM once direct data access and cohort counts are resolved).

**Gate 3 — Reproducibility pilot:** run code-only tests and participant-ID validation, then a small pilot using only two approved datasets. Report data integrity and feasibility, not confirmatory performance. If labels/IDs cannot be reliably mapped, stop.

**Gate 4 — Protocol lock:** finalize protocol, analysis plan and exclusion/threshold definitions before running the confirmatory benchmark.

**Gate 5 — Results:** report real results only. Negative or inconclusive results must not be rewritten as success.

## Final recommendation

Proceed with this narrow candidate as a **conditional empirical benchmark**. Do not claim the original generic monitoring/abstention concept is novel, do not start a large model-training pipeline yet, and do not promise three-language external validation until a third cohort is actually accessible, independent, and task-compatible.
