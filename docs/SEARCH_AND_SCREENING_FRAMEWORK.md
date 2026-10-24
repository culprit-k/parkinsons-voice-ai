# Literature search and screening framework

**Version:** 0.1  
**Prepared:** 2026-10-25  
**Status:** planned review methods; searches are not yet fully executed or deduplicated. Do not describe this as a completed systematic review or claim PRISMA compliance until the protocol is followed and records are logged.

## 1. Purpose and review questions

Primary question: What evidence exists on out-of-sample generalization, demographic confounding/fairness, and clinical reliability of voice- or speech-based machine-learning models for Parkinson’s disease (PD) detection?

Secondary questions:
1. How often are participants—not recordings/windows—the independent split unit?
2. How frequently are external datasets or languages evaluated?
3. Are language effects separable from site, recording device, task, recruitment and severity?
4. Are calibration and clinically meaningful operating points evaluated, or is evidence limited to discrimination metrics?
5. Are age/sex subgroup sample sizes, baseline models, uncertainty and missingness reported?
6. Can another research group reproduce the result using accessible data, code, and preprocessing details?

## 2. Sources to search

Search the following bibliographic databases where access is available:
- PubMed/MEDLINE
- Europe PMC
- Scopus
- Web of Science
- IEEE Xplore
- ACM Digital Library

Supplement with:
- Crossref/DOI landing pages and journal full text
- Google Scholar or equivalent citation chaining for discovery
- Official dataset repositories and source papers
- GitHub/Zenodo records for code and data releases
- Reference lists and forward citations from the most relevant systematic reviews

Record exact access date, database, query string, number of hits returned, exported file name, and any search syntax modifications. Do not combine hits from different sources into one unexplained number. Save exports and duplicate-removal results if tooling permits.

## 3. Date range and language

- Primary search period: 1 January 2010 to 25 October 2026.
- English-language title/abstract/full-text eligibility for the initial review.
- Include non-English speech corpora and papers if the study report is available in English.
- Include preprints, technical reports and published articles, but classify publication status explicitly and conduct sensitivity analysis excluding non-peer-reviewed work.

This date period can be refined after the first query run; do not retroactively change it without logging the reason.

## 4. Search strings

Adapt syntax per database, preserving the concepts. Use both broad and targeted queries.

### Core PD voice-AI query
("Parkinson disease" OR Parkinson* OR parkinsonism) AND (voice OR speech OR phonation OR acoustic OR prosody) AND (machine learning OR deep learning OR artificial intelligence OR neural network OR classifier)

### External/generalization query
("Parkinson disease" OR Parkinson*) AND (voice OR speech OR acoustic) AND ("external validation" OR "cross-dataset" OR cross-corpus OR cross-language OR multilingual OR generalization OR "domain shift" OR transfer)

### Demographic confounding/fairness query
("Parkinson disease" OR Parkinson*) AND (voice OR speech) AND (bias OR fairness OR demographic OR age OR sex OR gender OR ethnicity OR confounding OR subgroup)

### Clinical reliability/calibration query
("Parkinson disease" OR Parkinson*) AND (voice OR speech) AND (calibration OR "Brier score" OR "calibration slope" OR "calibration intercept" OR sensitivity OR specificity OR "decision curve" OR clinical utility OR threshold)

### Reproducibility/leakage query
("Parkinson disease" OR Parkinson*) AND (voice OR speech OR acoustic) AND (reproducibility OR leakage OR "subject-level" OR "participant-level" OR speaker-level OR "data split" OR cross-validation OR benchmark)

### Dataset/access query
(Parkinson* AND (speech corpus OR voice dataset OR audio dataset OR acoustic features OR benchmark)) AND (language OR multilingual OR access OR license OR repository)

## 5. Eligibility criteria

### Include
- Human-participant research using voice, speech, phonation or audio-derived acoustic/speech representations to identify PD versus controls, classify PD state/severity, or evaluate PD-related screening.
- Primary studies with model development or evaluation, external validation, domain adaptation, fairness/confounding, calibration, reproducibility, or dataset-methodology analyses.
- Systematic/scoping reviews and umbrella reviews for background and reference harvesting, but not counted as independent primary evidence.
- Studies using raw audio, spectrograms, embeddings or engineered acoustic features, with the input type recorded.

### Exclude from the primary evidence table
- Studies not involving PD or not evaluating a voice/speech signal.
- Non-human studies, editorials without original methods, general opinion pieces, and publications with no extractable methods.
- Diagnostic studies based only on handwriting, gait, imaging, genetics, blood, or other modalities without a voice/speech component.

### Keep in a separate contextual table
- PD-only datasets without healthy controls.
- Studies with self-reported diagnoses or unclear labels.
- Conference abstracts/preprints without accessible methods, if relevant to the research frontier.
- Mixed-modality studies where voice-only performance cannot be isolated.

## 6. Screening procedure

1. Export all records and log the precise query/date.
2. Deduplicate using DOI, title, author/year and manual review.
3. Screen titles/abstracts against inclusion criteria.
4. Record one exclusion reason at full-text screening.
5. Resolve uncertain eligibility by re-reading methods and supplements.
6. Use citation chasing from the 2025 systematic review and newest 2025–2026 cross-corpus papers.
7. Keep peer-reviewed studies, preprints and repository reports clearly labeled.

If only one reviewer performs screening, record this as a limitation; do not describe the process as independent dual-reviewer screening.

## 7. Data extraction form

For each primary study, record:
- Full citation, DOI/URL, publication status/version, year
- Study aim/design and whether preregistered
- Dataset name/version and provenance
- Number of participants and number of recordings/clips/windows (separately)
- PD/control counts, diagnosis source, stage/severity and medication state
- Language, country/site, recruitment source, recording device and speech tasks
- Age, sex/gender, ethnicity and missingness by diagnosis
- Raw audio, spectrogram, transcript, embedding or engineered features
- Preprocessing and task filtering
- Participant IDs available? Are repeated recordings grouped?
- Split method at every stage: train, validation, calibration, test, cross-validation
- External test cohort independent of training? Any overlap risk?
- Baseline models, including demographic-only/source-only baselines if reported
- Metrics and confidence intervals; participant-level versus clip-level aggregation
- Threshold choice; calibration metric/plot; PPV/NPV prevalence handling
- Subgroup sample sizes and uncertainty
- Explainability/interpretability assessment
- Data availability, license/access route, code and model availability
- Authors’ stated limitations
- Reviewer’s critical appraisal and relevance to our question

## 8. Risk-of-bias and applicability framework

Use a structured narrative informed by:
- PROBAST+AI for prediction-model risk of bias and applicability
- TRIPOD+AI for reporting completeness
- STARD-AI when evaluating diagnostic-accuracy studies

For each paper, flag:
1. Participant selection and disease/control spectrum
2. Reference standard and label certainty
3. Predictor measurement, preprocessing and task/device comparability
4. Outcome leakage, participant overlap, model-selection leakage and threshold tuning
5. Missing-data handling
6. External validation and uncertainty
7. Calibration and threshold transport
8. Demographic confounding and subgroup validity
9. Reproducibility and data-access feasibility

These checklists have different purposes; reporting completeness is not the same as low risk of bias.

## 9. Synthesis plan

Do not meta-analyze AUROCs or F1 values by default. These metrics may be based on different datasets, case mixes, thresholds, units (clip versus participant), class prevalence and validation designs.

First create a structured narrative synthesis grouped by:
- validation design (random/in-domain, participant-grouped, external same-language, cross-language/domain-shift)
- modality (engineered features, classic acoustic features, embeddings, end-to-end audio)
- label source and disease stage
- demographic confounding/fairness
- calibration and clinical operating points
- reproducibility and data accessibility

Only consider quantitative pooling if at least several studies have sufficiently compatible endpoints, populations and independent units, with a defensible model for heterogeneity. Report why pooling is or is not justified.

## 10. Current search status

The project has performed targeted discovery and critical appraisal of selected recent studies, including Lim et al., ParkMAE, Hossain et al. (early accepted 2026 paper), Ahammad, Ganatra, Shukla et al., Adnan et al., and the Twala reproducibility report, plus recent reviews. Full database searches, deduplication, dual screening and complete extraction remain undone.

The present task is to complete these steps before presenting a systematic review, PRISMA flow diagram or formal novelty claim.
