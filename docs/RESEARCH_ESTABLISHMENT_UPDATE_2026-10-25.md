# Research establishment update — 25 October 2026

## 2026-10-25 — Research establishment update (post-audit evidence)

### Decision on the current research question

**Candidate question (not protocol-locked):**

> On independent held-out Parkinson's voice cohorts, does a prespecified source-reference acoustic-domain-distance score improve detection/ranking of participant-level screening errors beyond calibrated predictive confidence alone?

This is a comparative reliability study, not a claim to have invented a new general AI architecture. The targeted literature search still does not prove global novelty. Cross-language Parkinson's voice modelling and uncertainty-aware assessment already have close prior art, including ParkMAE (published 10 December 2025; Scientific Reports volume 16, 2026), Lim et al.'s Korean/Taiwanese cross-language model, and a 23 June 2026 study reporting Spanish-to-Italian external validation and an uncertainty-aware assessment system. These works substantially constrain any novelty claim. The remaining potentially useful contribution is the *specific head-to-head error-monitoring question*—distance plus confidence versus confidence alone—evaluated by participant on genuinely independent cohorts. It remains a hypothesis to test, not an established novelty claim.

### UCI Dataset 489: schema and label audit clarified

The official UCI variable description specifies **STATUS 0 = Healthy and 1 = Parkinson's disease**, and **Gender 0 = Man and 1 = Woman**. Its enumerated acoustic variables comprise 44 engineered acoustic measures: jitter (4), shimmer (5), HNR (5), MFCCs (13), delta-MFCCs (13), RPDE, DFA, PPE and GNE (4). Gender is a separate covariate; ID, recording/repetition and status are identifiers/label metadata. This explains why some secondary descriptions count 45 columns when they include gender, while the pipeline identifies 44 acoustic predictors. The source record explicitly says the three rows per person are dependent and must not be treated as independent samples.

Verified facts from the completed aggregate-only audit remain: 240 rows, 80 people, exactly 3 repeated rows/person, 40 PD and 40 healthy at participant level, no within-person label changes and no missing values in the selected acoustic columns. This release has no raw WAV files and **does not count as a third audio cohort**. Use participant-level grouping for any separate feature-only analysis; do not combine its engineered features with waveforms/audio embeddings as if the modalities were interchangeable.

Sources: [UCI Dataset 489 and variable definitions](https://archive.ics.uci.edu/dataset/489/parkinson+dataset+with+replicated+acoustic+features); [Naranjo et al., Addressing voice recording replications for Parkinson's disease detection](https://doi.org/10.1016/j.eswa.2015.10.034).

### Current leading cohort-access route

**EWA-DB (Slovak)** is the leading request candidate for a third raw-audio cohort because the catalog lists sustained-vowel phonation and reports 1,649 speakers overall: 175 with PD, 2 with mixed AD+PD, 87 with AD, 62 with MCI and 1,323 healthy controls. WAV files are released for the 1,003 speakers who provided written consent; the exact PD/control breakdown within those WAV files is not established by the public catalogue. Access is gated through ELRA, and the listing displays €0 prices for its listed license options; terms, eligibility and current download conditions still require confirmation. Do not count EWA-DB as available until access and its audio-specific participant/label manifest are verified.

Sources: [Scientific Data corpus description](https://www.nature.com/articles/s41597-024-04171-6); [ISLRN record](https://www.islrn.org/resources/730-022-142-264-9/); [ELRA catalogue](https://catalogue.elra.info/en-us/repository/browse/ELRA-S0489/).

**mPower** remains a fallback/complementary cohort, not yet available to this project. Its sustained /a/ task is relevant, but raw voice requires validated/certified Synapse research access and acceptance of data-use conditions; disease status is based on participant self-report, and many participants contribute repeated recordings. Any evaluation must group by participant, audit duplicate/repeat visits and report the diagnosis-label limitation.

Sources: [mPower study](https://pmc.ncbi.nlm.nih.gov/articles/4776701/); [2024 transfer-learning paper/data access description](https://www.nature.com/articles/s41598-024-81824-x).

UCI Dataset 301 ("Parkinson's Speech with Multiple Types of Sound Recordings") is **not** an alternative raw-audio cohort in its UCI release: the repository provides extracted acoustic-feature tables, with the training data described for 20 PD and 20 controls and a separate test set of 28 PD participants only. Its task diversity is useful background, but this release cannot supply a third waveform cohort or an independently labelled PD/control test set for the current audio-distance analysis.

Source: [UCI Dataset 301](https://archive.ics.uci.edu/dataset/301/parkinson+speech+dataset+with+multiple+types+of+sound+recordings).

### Gating decisions

1. Keep protocol **NOT LOCKED** and confirmatory modelling **NOT STARTED**.
2. Do not claim cross-language generalization from sustained vowel alone. At most, it tests cross-cohort/recording-domain robustness of sustained phonation; lexical/language transfer needs a matched connected-speech task and separate design.
3. IPVS contains direct identifiers in a spreadsheet. Do not publish the spreadsheet, names, raw audio or participant-level linkage. Resolve governance and the authorized label/ID mapping before demographic analysis; exclude the dataset if lawful separation cannot be confirmed.
4. UAMS has a substantial age imbalance between PD and healthy controls in the audited subset. Prespecify an age-only baseline and an age-overlap sensitivity analysis, subject to viable cell sizes; do not present raw discrimination as independent of age without testing.
5. MDVR-KCL is a connected read/dialogue cohort and remains a separate task stratum; its participant-to-diagnosis mapping still needs verification.
6. Only promote an access candidate after written access/license terms, task-matched audio in both groups, usable participant IDs and labels, repeat-session handling, demographics/provenance and cohort independence are verified.

No model was trained, no performance estimate was produced, and no clinical efficacy or novelty is claimed in this update.
