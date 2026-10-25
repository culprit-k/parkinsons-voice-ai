# Third-cohort search and data-access plan — 25 October 2026

## Decision

Three archives now pass basic file-integrity/audio-header checks (IPVS, UAMS, MDVR-KCL), but they are **not three compatible independent cohorts** for the selected participant-level external-error study. UAMS and the sustained-vowel subset of IPVS can support a task-matched feasibility pilot after the IPVS governance/mapping and UAMS clinical-provenance checks. MDVR-KCL is connected read/dialogue speech and must not be mixed into a sustained-vowel-only primary analysis.

The best third-cohort request is **EWA-DB (Slovak)** because the catalogue describes sustained-vowel phonation as one of its tasks and reports an audio subset from speakers who gave written consent. **mPower** is the best second route for another sustained-vowel mobile-recording cohort, but requires Synapse research access and has diagnostic-label caveats. Neither is counted as available until access, licensing, manifests and labels have been confirmed.

## Evidence and candidate assessment

| Candidate | What source evidence says | Task match | Access and decision |
|---|---|---|---|
| **EWA-DB (Slovak; ELRA-S0489)** | The ELRA-linked catalogue describes 1,649 speakers across clinical/control groups and says WAV audio is published for 1,003 speakers who provided written consent. Tasks include sustained vowels, diadochokinesis, naming, and picture description. [ELRA catalogue](https://catalogue.elra.info/en-us/repository/browse/ELRA-S0489/) · [ISLRN record](https://www.islrn.org/resources/730-022-142-264-9/) | Potentially strong if the release provides PD and control recordings of the same sustained-vowel task and usable participant IDs. | License/request mediated; metadata do not prove our account has permission or that every clinical group has audio. **Priority 1 request.** |
| **mPower (US; mobile sustained vowel)** | A peer-reviewed study describes 10-second sustained-vowel recordings and says qualified researchers must validate a Synapse account, submit a data-use statement and agree to terms. The literature notes PD status may be self-reported. [Study/data access](https://www.nature.com/articles/s41598-024-81824-x) · [Synapse access guidance](https://docs.synapse.org/synapse-docs/getting-started) | Strong task match, but diagnosis provenance, repeated observations, medication timing, missingness and device/app selection need audit. | Requires account validation/conditions. **Priority 2 fallback or complementary domain**; not fully open. |
| **NeuroVoz v3 (Castilian Spanish)** | The corpus paper reports sustained vowels, DDK, listen-and-repeat utterances and spontaneous monologues; the latest Zenodo v3 record reports 112 participants and 2,977 files. [Paper](https://www.nature.com/articles/s41597-024-04186-z) · [v3 Zenodo record](https://zenodo.org/records/13647600) | Sustained vowel is potentially task-matched; connected speech must be a separate analysis. | Zenodo marks the dataset restricted. **Request permission; not available unless approved.** |
| **PC-GITA (Colombian Spanish)** | Published studies describe sustained vowels plus DDK, reading and spontaneous speech, commonly about 100 participants. [Systematic review](https://www.mdpi.com/2306-5354/12/11/1279) | Potentially strong for sustained vowel and a later connected-speech analysis. | Access is described as request/institutional collaboration. **Backup request candidate**, not assumed open. |
| **UNLaM Parkinson Voice Database (Argentine Spanish)** | A 2026 paper describes the Spanish data as openly available and reports n=126, while other descriptions report 119; exact version/provenance needs reconciliation. [2026 paper/data statement](https://doi.org/10.1007/s40846-026-01040-y) | Potentially task-matched if the release contains original sustained-vowel audio with IDs and labels. | Verify repository URL/version, raw-audio availability, license, unique IDs, and why cohort counts differ. **Verification lead, not yet accepted.** |
| **MDVR-KCL (UK English)** | This project downloaded 73 readable WAV files; literature describes read text and spontaneous dialogue. [Zenodo](https://zenodo.org/records/2867216) | **Not task-matched** to a sustained-vowel-only primary analysis. | Keep for a separately prespecified connected-speech pilot only if participant/diagnosis mapping is verified. |
| **Bridge2AI Voice** | Rich voice cohort with additional access conditions for some raw data; later release shares participants with earlier release. [PhysioNet](https://physionet.org/content/b2ai-voice/4.0.0/) | Tasks and population differ; diagnosis composition and target endpoint need confirmation. | Not the immediate third PD/control cohort. Do not count overlapping releases as independent. |

### Interpretation boundary

A sustained-vowel model evaluates sustained phonation/acoustic patterns. Vowel-only data do not test lexical, grammatical, or spontaneous-language generalization. Evaluation across Italian, Slovak and US phone-app recordings would still combine language, site, device, environment, age/sex mix, recruitment and diagnosis-label differences. The accurate claim would be cross-dataset/recording-domain robustness of sustained phonation, not isolated language causality.

## Exact access-request questions

For each custodian, ask:

1. What license, data-use agreement, institutional affiliation, ethics approval or other prerequisites apply to an MBBS student conducting secondary analysis without new recruitment?
2. May the project access raw audio, de-identified participant IDs, PD/control labels, permitted age/sex fields, task labels, recording/device/site metadata, medication state and relevant clinical scores?
3. Does each participant have a stable ID linking recordings/tasks and visits? How are repeat visits, trials and multiple recordings represented?
4. What is the operational diagnosis definition and source: clinician diagnosis, chart review, self-report, questionnaire or other? Are controls screened for neurological/voice conditions?
5. Which exact sustained-vowel task(s) exist, and are they available for both PD and controls? What are the sample rate, recording device and allowed normalization?
6. Can aggregate counts and code be published? Can raw audio, embeddings or transformed data be redistributed? We will not redistribute audio unless expressly permitted.
7. Are there known overlaps with other releases, shared source participants or prior benchmark/pretraining use that affect independent external validation?

## Ready-to-edit email: EWA-DB / ELRA access

**Subject:** Research access enquiry — EWA-DB (ELRA-S0489) for Parkinson's voice robustness study

Dear EWA-DB / ELRA data-access team,

I am an MBBS student at [institution] preparing a prespecified secondary-data study of voice-based Parkinson's disease screening. The study would use previously collected recordings only; we are not recruiting participants or making clinical decisions from a model.

I am writing to ask about eligibility and the exact terms for research access to EWA-DB, particularly the sustained-vowel task. Could you clarify whether the permitted release includes de-identified participant-level IDs, PD/control labels, task identifiers and basic permitted demographics for speakers with accessible WAV files? I would also appreciate details on the current license/data-use agreement, any fees, institutional sign-off or ethics documentation required, and publication/code-sharing restrictions.

The planned analysis would split and evaluate data by participant, avoid publishing personal information or audio, and report only aggregated research results. Access would be used only in accordance with the license and data-use conditions. I will obtain any institutional ethics/governance determination required before analysis.

Thank you for your time and guidance.

Best regards,  
[Full name]  
[Institution and department]  
[Institutional email]  
[Supervisor/faculty contact, if applicable]

## Ready-to-edit email: NeuroVoz access

**Subject:** Request for access conditions — NeuroVoz v3 for secondary Parkinson's speech research

Dear NeuroVoz research team,

I am an MBBS student at [institution] planning a prespecified secondary-data study of robustness and error monitoring for voice-based Parkinson's disease screening. I reviewed the NeuroVoz paper and the Zenodo v3 record, which currently appears access-restricted.

Could you please advise whether access may be granted for an academically supervised student project, the required affiliation and ethics/governance documents, and whether de-identified participant IDs and diagnostic labels can be supplied with the recordings? The immediate analysis of interest would be the sustained-vowel task, with connected-speech tasks reserved for a separate, appropriately matched analysis. I would follow all data-use, privacy, retention and publication conditions and would not redistribute raw audio.

Thank you for considering the request.

Best regards,  
[Full name]  
[Institution and department]  
[Institutional email]  
[Supervisor/faculty contact, if applicable]

## mPower access checklist

1. Create/validate the research Synapse account using the official workflow.
2. Read the current project-specific data-use conditions and submit the required data-use statement.
3. Record the exact dataset/release identifier, participant-consent scope and whether the intended voice files are available to the approved user.
4. Audit label source (self-reported vs clinically confirmed), repeated recordings per participant, medication timing, quality exclusions, missingness, age/sex availability and overlap with derived-feature releases.
5. Keep credentials and restricted data private. Never put raw audio, IDs, manifests, access tokens or controlled data into the public GitHub repository.

## Promotion gate

A cohort can be promoted from **candidate** to **approved for analysis** only after: (a) access/license permission is documented; (b) raw audio or a reproducible compatible feature release is obtained lawfully; (c) unique participant IDs and PD/control labels are mapped to files; (d) task compatibility is confirmed; (e) repeated sessions and duplicates are handled; (f) diagnosis provenance is understood; and (g) overlap with other cohorts is ruled out or accounted for.

Until then:
- Do **not** count EWA-DB, mPower, NeuroVoz, PC-GITA or UNLaM as an available third cohort.
- Do **not** train a confirmatory model or lock the protocol.
- If only two compatible cohorts clear the gate, call the work a feasibility pilot and make no broad cross-language claim.
- If IPVS privacy/mapping cannot be resolved lawfully, exclude it rather than attempting name-to-audio linkage without governance approval.


## Addendum — post-search verification (25 October 2026)

### EWA-DB status

EWA-DB remains the highest-priority request candidate, not a cleared dataset. The ISLRN/ELRA record states 1,649 speakers overall: 175 PD, 2 mixed AD+PD, 87 AD, 62 MCI and 1,323 healthy controls, across sustained vowel, diadochokinesis, naming and picture-description tasks. WAV audio is published for 1,003 speakers with written consent; the exact PD/control breakdown for that audio-available subset is not specified in the catalogue. Obtain the data-use license, actual audio/manifest, and group-by-task counts before any cohort promotion. ELRA lists 0.00 EUR for its listed license options, but current conditions and eligibility must be confirmed. [ISLRN](https://www.islrn.org/resources/730-022-142-264-9/) · [ELRA](https://catalogue.elra.info/en-us/repository/browse/ELRA-S0489/) · [paper](https://www.nature.com/articles/s41597-024-04171-6).

### mPower and UCI 301 decision

mPower is a secondary route for sustained /a/ because its raw voice requires Synapse account validation/certification, a data-use statement and acceptance of conditions; PD diagnosis is self-reported and recordings repeat within people. It remains unavailable until access is granted and the exact approved release is audited. [mPower study and access](https://pmc.ncbi.nlm.nih.gov/articles/4776701/) · [2024 transfer paper](https://www.nature.com/articles/s41598-024-81824-x).

UCI Dataset 301's UCI release consists of extracted acoustic feature tables rather than raw WAVs; the advertised test file contains recordings/features for 28 PD participants without a corresponding control test arm. It therefore cannot replace the missing third raw-audio PD/control cohort. [Official UCI record](https://archive.ics.uci.edu/dataset/301/parkinson+speech+dataset+with+multiple+types+of+sound+recordings).

### Research implications

The candidate question remains an **unlocked comparative reliability question**: does source-reference acoustic-domain distance add to calibrated confidence when ranking participant-level errors in external cohorts? ParkMAE (2025/2026), Lim et al. (2025), and a June 2026 Spanish-to-Italian uncertainty-aware system demonstrate substantial nearby prior art. Recheck direct overlap with uncertainty/OOD error-monitoring methods before any novelty claim. A sustained vowel cannot establish lexical or spontaneous-language generalization; any claim must be limited to cross-cohort robustness of sustained phonation unless matched connected-speech tasks are separately evaluated. No model has been trained.


## Further access and novelty check (25 October 2026)

- **EWA-DB Zenodo access is confirmed restricted.** A research access form is required; the provider sends a EULA and issues the download link after receiving the signed agreement. The catalogue's listed €0 price is not a grant of access. Exact PD/control numbers among audio-available people must be checked after access. [Zenodo access instructions](https://zenodo.org/records/10952480).
- **Additional cross-language prior art:** Hassanat et al. (29 April 2026) report an Arabic cohort of 40 people (17 PD, 23 controls) and independent Spanish evaluation on 100 people. This makes any broad "new cross-language PD classifier" claim untenable. [PubMed](https://pubmed.ncbi.nlm.nih.gov/42100562/).
- **HeyJay! (June 2026)** adds 8,669 English atypical-speech utterances and speech-quality ratings, including PD, but it is restricted-access and is not established as a labelled PD/control screening cohort from the public summary. Consider only for a separate accessibility/robustness question after access and diagnosis stratification are verified. [Dataset article](https://www.nature.com/articles/s41597-026-07497-5) · [ICPSR record](https://www.icpsr.umich.edu/web/ICPSR/studies/39448).


## EWA-DB cohort count reconciliation and access action — 25 October 2026

The access-specific checklist is now at [EWA_DB_ACCESS_AND_AUDIT_CHECKLIST_2026-10-25.md](EWA_DB_ACCESS_AND_AUDIT_CHECKLIST_2026-10-25.md). It includes a draft message to the listed corresponding author and the local-only audit utility [`scripts/audit_ewa_db_local.py`](../scripts/audit_ewa_db_local.py).

Important cohort-size discrepancy to resolve with the custodian:
- Data descriptor: 1,649 total speakers, of whom 175 are labelled PD, 2 mixed AD+PD, 87 AD, 62 MCI, and 1,323 controls.
- Descriptor: 1,122 speakers meet the stated inclusion criteria; WAV files are publishable for 1,003 speakers who gave recording-publication consent.
- ParkMAE evaluation table: 956 EWA-DB speakers, 95 PD and 861 controls, 6,692 audio files, 88 h 10 min.
These are not interchangeable sample sizes. The ParkMAE subset may reflect task, group and inclusion filtering; it does not prove that all such files are available to this project. Request counts of unique audio-available participants by diagnosis and task, and a de-identified manifest.

The EWA-DB data descriptor reports manifest/diagnostic complexity: the PD group includes manifest and prodromal cases recruited by different routes, and some speakers do not meet every predefined inclusion criterion. If the manifest allows, prespecify manifest-PD-only as primary; keep prodromal and mixed AD+PD out of the principal PD-vs-HC contrast or treat them separately. EWA recordings were collected via different mobile devices/sites/environments, with audio quality flags and variable contexts, so include these as domain/quality factors rather than assuming homogeneous recording conditions.

No request has been submitted and no EWA audio has been downloaded. Promotion remains pending written access approval, EULA review, task-specific PD/HC counts, ID/repeat-session verification, privacy/governance review, and local audit.
