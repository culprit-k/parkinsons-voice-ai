# Dataset feasibility and independence gate

**Audit date:** 2026-10-25  
**Status:** preliminary evidence audit; no local data download or identity check completed in this update.

## Decision rule

The intended cross-corpus monitoring benchmark requires **at least three independent, legally accessible cohorts** with participant-level PD/control labels and compatible usable inputs; four or more are preferred. Two datasets cannot establish that a monitoring relationship generalizes across heterogeneous domains. A subset or alternate release containing the same participant IDs is not a new independent cohort.

## Candidate matrix

| Dataset | Reported design/cohort | Availability and known barrier | Status |
|---|---|---|---|
| MDVR-KCL | UK English; reported 16 PD / 21 controls; several speech tasks; smartphone/telephone-style recordings. | [Zenodo DOI 10.5281/zenodo.2867216](https://doi.org/10.5281/zenodo.2867216). Lower-friction raw-audio candidate; verify exact package, participant manifest, labels and licence. | Candidate A, not yet locally verified. |
| ItalianPVS/IPVS | Italian; common elderly-control subset 28 PD / 22 controls (n=50); full release also includes 15 young controls. | [IEEE DataPort official record](https://ieee-dataport.org/open-access/italian-parkinsons-voice-and-speech). Portal access/terms and exact manifests need checking. | Candidate B, not yet locally verified. |
| UNLaM Parkinson Voice Database | Argentine Spanish; original article reports 55 PD + 64 controls (119); a 2026 paper reports n=126. | Dataset described as available in the literature; exact downloadable raw-audio manifest, version, licence and explanation for count difference need verification. | Potential third cohort; not approved. |
| PC-GITA | Colombian Spanish; commonly described as about 50 PD and 50 healthy controls. | Raw audio described as available by academic/institutional request through Universidad de Antioquia. Permission is not assumed. | Request candidate. |
| NeuroVoz | Spanish; data paper reports 54 PD and 58 controls. | [Zenodo record](https://zenodo.org/records/10777657) is restricted; request/approval required. | Request candidate. |
| EWA-DB | Slovak; ELRA catalogue metadata lists 1,649 people including multiple diagnoses; audio is a consented subset. | [ELRA-S0489 catalogue](https://catalogue.elra.info/en-us/repository/browse/ELRA-S0489/). License/request terms and usable audio counts must be verified. | Request candidate. |
| Bridge2AI Voice v4.0.0 | 1,370 participants, 48,226 recordings; multi-site North American data. | [PhysioNet v4](https://physionet.org/content/b2ai-voice/4.0.0/): derived features publicly available; raw voice has additional institutional sign-off. Version 4 shares participants with v3. | Secondary candidate; not independent from v3. |
| mPower | US remote smartphone collection; diagnostic/recruitment definitions differ from clinical corpora. | Verify exact voice task, labels, participant IDs, access and terms for the intended version. | Potential candidate; not approved. |
| Oxford/UCI Parkinson's Telemonitoring | 42 PD participants and 5,875 repeated voice recordings, designed for symptom-severity regression. | [UCI record](https://archive.ics.uci.edu/dataset/189/parkinsons+telemonitoring). Not a binary PD/control cohort. | Not suitable as a main screening cohort. |
| ParkCeleb | Celebrity video-derived cohort with age/sex/ethnicity matching claims. | [Zenodo record](https://zenodo.org/records/13954768) primarily has metadata/links, with access/licensing and privacy issues. | Not a primary raw-audio candidate. |
| UCI 301/489 and engineered-feature collections | Small participant populations with repeated feature rows; no raw audio in many releases. | Public subsets are useful for code/split checks, but cannot measure raw-audio quality shift. | Secondary methodological checks only. |

### NeuroVoz version-specific counts

The current latest Zenodo version (v3, record [10.5281/zenodo.13647600](https://zenodo.org/records/13647600)) reports **112 participants (54 PD, 58 healthy controls) and 2,977 audio files**, with files restricted unless access is granted. The older v1.0.0 record ([10.5281/zenodo.10777657](https://zenodo.org/records/10777657)) reports **108 participants (53 PD, 55 controls) and 2,903 files**. These are version-specific counts; use the chosen release’s manifest, not a pooled or casually mixed count.

## Independence and integrity cautions

1. The n=50 Italian test cohort in Guo et al. (2026) may be the standard ItalianPVS subset (28 PD + 22 elderly controls); treat as possible overlap until identifiers and provenance are checked.
2. UNLaM has a published count discrepancy (119 vs 126). Resolve exact version, participant exclusions and diagnostic labels before counting it.
3. Bridge2AI v3 and v4 share participants; they are not independent cohorts.
4. Do not count separate files, repeated tasks or overlapping windows as independent participants.
5. Do not count full catalogue metadata as usable speech audio. Restrict counts to licensed, accessible recordings with diagnosis and participant identifiers.
6. Do not upload raw or restricted speech recordings to GitHub. Store source code, allowed manifests, aggregate summaries and checksums only.

## Required acceptance checklist for every cohort

- Exact URL, release/version, access date, licence/DUA and permissions for intended features/analysis.
- Counts of unique participants and recordings by diagnosis, after exclusions.
- Stable participant IDs; duplicated participants/sessions audited.
- Diagnosis definition, disease severity and medication state when available.
- Language, prompted speech task, recording device/sample rate, site and environment.
- Age/sex metadata and missingness, with small-subgroup limitations logged.
- Whether raw audio is available or only derived features; whether feature extraction is reproducible.
- Whether participant overlap with all other candidate cohorts or pretraining data can be ruled out.
- Exact allowed outputs for publication and code/data release.

## Current go/no-go

**Data gate is NOT passed.** MDVR-KCL and ItalianPVS are the two most immediately plausible raw-audio candidates, but the project has not yet completed a local access and integrity check for either, and a third independent fully usable corpus is not yet established.

Proceed with verification of these two plus UNLaM/PC-GITA/NeuroVoz/EWA-DB access. If a third cohort cannot be obtained legally and reliably, narrow the study to a two-corpus pilot and avoid broad multilingual claims, or pivot to a review/reproducibility paper. Do not begin confirmatory model training until the cohort manifest and protocol are versioned.


## Additional candidate: UAMS telephone-recorded voice samples

A second candidate with an explicit public raw-audio record was identified during the deeper search:
- Figshare page: https://figshare.com/articles/dataset/Voice_Samples_for_Patients_with_Parkinson_s_Disease_and_Healthy_Controls/23849127
- Description says the demographic file links sample IDs to two .wav archives (PD_AH.zip and HC_AH.zip), containing prolonged /a/ recordings made by telephone; the record advertises a 4.18 MB download and CC BY 4.0.
- A related paper reports 81 voice records (40 PD and 41 healthy controls). The actual manifest must still be checked to confirm one sample per unique person, no repeat recordings, label provenance, and exact demographic denominators.

This is an attractive task-matched external cohort for ItalianPVS, but the two-cohort design alone is a limited pilot, not sufficient evidence for broad language generalization. The public existence of the record does not mean the files have been downloaded or validated by this project.

## Revised current access decision

Two plausible public raw-audio cohorts are identifiable for a task-matched sustained-/a/ pilot: ItalianPVS and UAMS Figshare. A third task-compatible, independent cohort is **not yet approved**. mPower requires research access and a label-provenance audit; UNLaM has a report that describes a database and a 2026 paper claiming open data, but an exact versioned raw-audio download manifest has not been verified here; NeuroVoz v3 is restricted. See the final decision memo for the current decision and exact go/no-go criteria.


## Final targeted-check notes

### mPower sustained /a/ is potentially task-compatible but restricted
The mPower methods literature describes smartphone sustained /a/ recordings up to 10 seconds under uncontrolled daily conditions. Raw data access uses Synapse account validation/certification, an intended-use statement and source-specific terms. Some voice studies identify PD using self-report of having received a professional diagnosis. mPower is a plausible third domain only after confirming the exact diagnostic variable, missingness, number of unique participants, repeat recordings/medication timing and legal use. Do not equate app self-report with independent chart-confirmed diagnosis.

### UNLaM/Mendeley report needs provenance resolution
The 2026 Spanish-to-Italian voice paper says Spanish data are openly available from the UNLaM Parkinson Voice Database and Italian data from Mendeley Data DOI https://doi.org/10.17632/4yryrv6xrh.1. This is a specific repository lead, but does not prove the Italian cohort is independent of standard ItalianPVS; nor does it resolve why the Spanish cohort is reported as 119 by its original database paper and n=126 in a 2026 paper. Confirm repository metadata, source paper, sample IDs, labels and exact version before counting any additional cohort.

### Task comparability is not language generalization
UAMS and ItalianPVS both contain sustained /a/ recordings, but their comparison combines language community, recording apparatus, environment, collection site, recruitment, age/sex distribution and label definition. The vowel contains no lexical content, so these two datasets cannot establish generalization of speech recognition or linguistic content across languages. The appropriate primary pilot claim is cross-dataset/recording-domain robustness of sustained phonation.

### Current data status
No raw recordings or demographic files have been downloaded in this project. UAMS and ItalianPVS are candidate public resources, not yet integrity-validated datasets; mPower is a restricted-access candidate, UNLaM is a repository lead with unresolved cohort/version counts, and NeuroVoz v3 is restricted. The data gate remains incomplete.


## Selected study requirement

The selected question is about whether source-reference acoustic distance adds beyond predictive confidence for detecting participant-level external errors. That requires raw audio or harmonized participant-level acoustic features from at least three independently sampled, legally accessible cohorts, with participant IDs and diagnosis labels validated. ItalianPVS and UAMS are only candidate sources; mPower needs access and label provenance checks. If only two datasets are cleared, the project must be labelled a pilot, not a confirmatory cross-corpus study.
