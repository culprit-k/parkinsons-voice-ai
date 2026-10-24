# Literature review plan

**Status:** Preliminary discovery only; not a completed systematic or scoping review.

## Objective
Map evidence on voice-based Parkinson's disease detection, focusing on:
1. Cross-language and cross-dataset generalization.
2. Demographic confounding and subgroup performance.
3. Recording-condition robustness and preprocessing sensitivity.
4. Calibration, uncertainty, and clinical validation.
5. Dataset limitations, leakage, and reproducibility.

## Search sources
- PubMed/MEDLINE
- Europe PMC
- Crossref and publisher sites for bibliographic verification
- Google Scholar for citation chaining and discovery
- Official dataset repositories and dataset papers

Record search date, exact query, source, number of records, and filters. Update searches near manuscript submission.

## Draft search concepts
- (Parkinson disease OR Parkinson's disease) AND (voice OR speech OR acoustic OR phonation) AND (machine learning OR deep learning OR classification)
- Above AND (cross-lingual OR multilingual OR language generalization OR external validation)
- Above AND (demographic bias OR age OR sex OR confounding OR fairness)
- Above AND (robustness OR recording conditions OR calibration OR dataset shift)

These are draft concepts, not evidence that a reproducible search has already been run.

## Provisional inclusion criteria
- Peer-reviewed empirical studies or well-documented dataset papers relevant to voice/speech and Parkinson's disease.
- Studies of model development, validation, bias/confounding, robustness, or clinical validity.
- Relevant preprints may be tracked separately and labelled as not peer-reviewed.
- No single-language restriction during discovery.

## Provisional exclusion criteria
- Not about Parkinson's disease or voice/speech, unless directly relevant to dataset/methodology.
- Editorials without usable methods or evidence (may be retained for context).
- Duplicate reports of the same experiment; retain the most complete report and record related publications.
- Unverifiable claims.

## Extraction fields
Citation; DOI/URL; year; peer-review status; site/country; languages; dataset; unique participants and recordings; diagnosis criteria; speech tasks; model; split strategy; external validation; leakage controls; metrics and confidence intervals; demographic adjustment; subgroup analysis; recording robustness; calibration; limitations; code/data availability.

## Novelty rule
Do not claim novelty from a small informal search. Compare directly with the closest prior studies, especially multilingual and demographic-confounding work. If already answered, narrow the question or choose a useful replication/benchmarking contribution.
