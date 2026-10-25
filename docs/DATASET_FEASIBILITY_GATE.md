# Dataset feasibility and independence gate

**Audit date:** 2026-10-25  
**Current status (25 Oct 2026):** three public source archives have passed basic file-level integrity/audio-header checks on GitHub Actions (IPVS, UAMS, MDVR-KCL). The overall dataset gate remains **NOT PASSED** because participant/diagnosis mapping, privacy/provenance and task-compatible third-cohort access remain unresolved.

## Decision rule

The intended cross-corpus monitoring benchmark requires **at least three independent, legally accessible cohorts** with participant-level PD/control labels and compatible usable inputs; four or more are preferred. Two datasets cannot establish that a monitoring relationship generalizes across heterogeneous domains. A subset or alternate release containing the same participant IDs is not a new independent cohort.

## Candidate matrix

| Dataset | Reported design/cohort | Availability and known barrier | Status |
|---|---|---|---|
| MDVR-KCL | UK English; literature reports 16 PD / 21 controls; read text and spontaneous dialogue. | [Zenodo DOI 10.5281/zenodo.2867216](https://doi.org/10.5281/zenodo.2867216). Archive MD5 and 73 WAV headers passed in run 40170614840; participant-label mapping and task are not compatible with a vowel-only primary analysis. | **File integrity PASS; participant/label gate OPEN; connected-speech candidate only.** |
| ItalianPVS/IPVS | Italian; reported 28 PD, 22 elderly controls and 15 young controls; multiple speech tasks. | [IEEE DataPort official record](https://ieee-dataport.org/open-access/italian-parkinsons-voice-and-speech) and [pinned public mirror](https://huggingface.co/datasets/birgermoell/Italian_Parkinsons_Voice_and_Speech/tree/main/italian_parkinson). SHA-256 matched the pinned mirror; 831/831 WAV headers passed. One exact duplicate pair found. Spreadsheet contains direct name/surname fields; do not attempt name-to-audio linkage pending governance review. | **File integrity/audio QC PASS; participant/session and privacy gates OPEN.** |
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

**Data gate is NOT passed.** IPVS, UAMS and MDVR-KCL now have successful file-level archive/audio checks, but none is fully approved for the planned confirmatory benchmark: IPVS participant/session/label mapping and privacy are unresolved, UAMS diagnosis provenance/independence are unresolved, and MDVR-KCL participant-label mapping is unresolved and the task is not sustained vowel. A third independent task-compatible cohort has not been approved.

Next priority is to request EWA-DB access and, in parallel if useful, follow the mPower Synapse research-access process. NeuroVoz and PC-GITA are additional request candidates; UNLaM remains a version/manifest lead. Do not treat any as available until permission, raw task-compatible PD/control audio, stable participant IDs and diagnosis provenance are verified. If a third cohort cannot be obtained legally and reliably, narrow the project to a two-corpus feasibility pilot or pivot to a reproducibility/systematic-review paper. Do not begin confirmatory model training until the cohort manifest and protocol are versioned.


## Additional candidate: UAMS telephone-recorded voice samples

A second candidate with an explicit public raw-audio record was identified during the deeper search:
- Figshare page: https://figshare.com/articles/dataset/Voice_Samples_for_Patients_with_Parkinson_s_Disease_and_Healthy_Controls/23849127
- Description says the demographic file links sample IDs to two .wav archives (PD_AH.zip and HC_AH.zip), containing prolonged /a/ recordings made by telephone; the record advertises a 4.18 MB download and CC BY 4.0.
- A related paper reports 81 voice records (40 PD and 41 healthy controls). The actual manifest must still be checked to confirm one sample per unique person, no repeat recordings, label provenance, and exact demographic denominators.

This is an attractive task-matched candidate for ItalianPVS. The source files have now been downloaded via the public Figshare API: 81/81 WAV headers passed, source MD5 checks passed, and 81/81 Sample IDs matched audio filename stems. The two-cohort design alone remains a limited pilot, not sufficient evidence for broad language generalization. Clinical label provenance and independent-participant status still need confirmation.

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
The network-enabled workflow has now downloaded and audited raw source files for IPVS, UAMS and MDVR-KCL. IPVS: 831 readable WAV files, checksum match, one duplicate pair, unresolved participant/session mapping, and name/surname fields in an included spreadsheet. UAMS: 81 readable WAVs, source MD5 checks passed, 81 unique IDs and 81/81 filename matches with 41 HC and 40 PwPD labels; clinical label provenance and independent-participant status remain open. MDVR-KCL: 73 readable WAVs and Zenodo MD5 match; raw participant/diagnosis mapping remains unverified. The gate remains incomplete.


## Selected study requirement

The selected question is about whether source-reference acoustic distance adds beyond predictive confidence for detecting participant-level external errors. That requires raw audio or harmonized participant-level acoustic features from at least three independently sampled, legally accessible cohorts, with participant IDs and diagnosis labels validated. ItalianPVS and UAMS are only candidate sources; mPower needs access and label provenance checks. If only two datasets are cleared, the project must be labelled a pilot, not a confirmatory cross-corpus study.


## Current gate status — 2026-10-25

Raw archives have been downloaded, checked against source metadata, unpacked and audited in the GitHub Actions runner; see runs [40170280356](https://github.com/culprit-k/parkinsons-voice-ai/actions/runs/40170280356) and [40170614840](https://github.com/culprit-k/parkinsons-voice-ai/actions/runs/40170614840). IPVS contains 831 WAV + 6 XLSX + 1 TXT = 838 extracted files; the mirror lists 839 items including the ZIP itself. This explains the one-item difference in the listing versus extracted archive inventory. UAMS ID-to-filename linkage passed. mPower still requires research access and label review. The overall dataset gate remains **NOT PASSED** because participant/session mapping, provenance and a third compatible independent cohort remain open.


## Raw archive verification update — 25 October 2026

The network-enabled audit first downloaded and inspected IPVS and UAMS (run 40170280356), then added MDVR-KCL and stricter ID-to-filename checks (runs 40170614840 and 40174963060). See the final audit addendum for exact per-cohort findings.

- **IPVS:** local SHA-256 matches the pinned mirror. Extracted inventory is 831 WAV + 6 XLSX + 1 TXT (838 files); 831/831 WAV headers readable, all mono, 671 at 16 kHz and 160 at 44.1 kHz. Path-derived labels cover 437 PD, 349 elderly controls and 45 young controls. One exact duplicate-audio hash group contains two WAV files. The participant-level mapping is not resolved. A spreadsheet contains direct name/surname fields; no identifying values have been copied to the repository, and the dataset must not be used for linked demographic analysis until governance/ethics and privacy-preserving mapping are resolved.
- **UAMS:** individual files downloaded through the public Figshare API; all available per-file MD5 checks passed. Inventory is 81 mono WAV files at 8 kHz plus one workbook. All WAV headers are readable; duration range is 1.51612–7.208 s. The Parselmouth sheet has 81 unique Sample IDs and labels 41 HC / 40 PwPD; all 81 IDs match audio filenames. Repeated visits/participant independence and diagnosis provenance still need confirmation.
- **Overall gate:** IPVS archive integrity and audio QC PASS; UAMS file integrity, audio QC and sample-ID-to-filename linkage PASS. IPVS participant/session mapping remains OPEN, and the exact duplicate pair needs adjudication. Three independent, compatible cohorts are not established. Protocol remains NOT LOCKED; modelling remains NOT STARTED.


### MDVR-KCL — file-level verification completed

The Zenodo archive audit succeeded at [GitHub Actions run 40170614840](https://github.com/culprit-k/parkinsons-voice-ai/actions/runs/40170614840). The downloaded source archive was 606,144,431 bytes and its MD5 matched Zenodo metadata. It contains 73 readable mono WAV files at 44.1 kHz, with durations 73.03902–220.63916 seconds; no exact duplicate audio hashes were detected. Raw participant IDs and file-to-diagnosis linkage were not verified. The literature describes read-text and spontaneous-dialogue tasks, so this corpus is not task-matched to UAMS sustained /a/ recordings.

This gives us three *downloaded audio corpora*, but **not three independent, compatible cohorts for the current prespecified question**. The task mismatch and unresolved IPVS mapping remain disqualifying for confirmatory modeling.


## Third-cohort search result — current as of 25 October 2026

**Priority request:** EWA-DB (Slovak; ELRA-S0489). The catalogue describes sustained-vowel phonation and says WAV audio is available for a consented subset. It is potentially compatible, but access/license, the actual PD/control audio subset, stable participant IDs, task labels and diagnosis provenance must be verified. Start from the [ELRA catalogue](https://catalogue.elra.info/en-us/repository/browse/ELRA-S0489/) and the [OneVoice-MSD collaborative dataset request form](https://forms.gle/58vskDQBY8xdBNd39) / contact listed on that dataset page. Do not describe it as downloaded or available until permission is approved.

**Fallback:** mPower offers sustained-/a/ voice records but is accessed through Synapse research procedures and may depend on self-reported diagnosis. **Additional request candidate:** NeuroVoz v3 (restricted) and PC-GITA (request-mediated). UNLaM is a metadata/repository lead with an unresolved 119 vs 126 participant-count/version discrepancy. Details and ready-to-edit emails are in [THIRD_COHORT_AND_ACCESS_REQUEST_PLAN_2026-10-25.md](THIRD_COHORT_AND_ACCESS_REQUEST_PLAN_2026-10-25.md).

If three compatible independent cohorts do not clear the gates, do not force a confirmatory paper: either preregister and label the work as a two-cohort feasibility pilot or pivot to a reproducibility/systematic-review study. Keep the protocol unlocked until then.

## Additional public resource audited: UCI Dataset 489

The official UCI Dataset 489 audit completed successfully in [run 40176480093](https://github.com/culprit-k/parkinsons-voice-ai/actions/runs/40176480093). It contains 240 rows from 80 participants, three repeated recordings/feature rows per participant, balanced participant labels (40/40), no cross-repetition label inconsistencies, and no missing values in the selected acoustic-feature columns. Sex-coded information is present; age is absent. See [official UCI record](https://archive.ics.uci.edu/dataset/489/parkinson+dataset+with+replicated+acoustic+features).

**Gate decision: NOT compatible as an audio cohort.** This is a feature-only release with no WAV files, so it cannot be used as a raw-audio cohort or directly compared with audio embeddings/domain-distance scores. It may be considered for a separate feature-only, participant-grouped analysis after label semantics, original feature-extraction provenance and task comparability are verified. The coded label mapping is not yet cleared. Do not count this as the missing third compatible audio cohort.
