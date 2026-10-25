# EWA-DB access and audit checklist — 25 October 2026

## Purpose and current status

EWA-DB (Slovak) is the leading candidate for a third raw-audio cohort. **Access has not been requested or granted by this project, no files are in our possession, and no audit of EWA-DB audio has yet been performed.** The official Zenodo record is restricted; the provider says an access request is followed by a signed End User License Agreement (EULA), then a download link. Submit the form using the researcher's own name and email: [Zenodo EWA-DB record](https://zenodo.org/records/10952480).

Corresponding author listed by the data paper: Milan Rusko, `milan.rusko@savba.sk`. [Scientific Data paper](https://www.nature.com/articles/s41597-024-04171-6). The data custodian—not Zenodo support—controls access to restricted files.

## Evidence already available before access

The data descriptor reports 1,649 speakers: 175 PD, 2 mixed AD+PD, 87 AD, 62 MCI, and 1,323 healthy controls. WAV audio is available for 1,003 speakers who consented to publication; the others have JSON records/transcripts only. The descriptor says participants performed sustained vowel /a/, diadochokinesis, naming and picture-description tasks. WAV recordings are documented as mono PCM, 16 kHz, 16-bit. PD participants include diagnosed manifest PD and a prodromal-PD subgroup; the distinction must be preserved if available. The metadata includes age, gender, education, and MoCA-related fields, and includes subjective audio-quality markers. The paper notes that audio recordings were made across different devices/sites/environments and that some participants in the full cohort did not meet every study inclusion criterion.

A later ParkMAE paper reports a model-evaluation EWA-DB subset of 956 speakers (95 PD, 861 controls), 6,692 audio files, 88 h 10 min. These are published study counts—not a guarantee that the same subset is available for our access request. Resolve the difference among the 1,649 total speakers, 1,122 meeting defined inclusion criteria, 1,003 with publishable audio, and the 956-person PD/control subset before fixing the sample-size expectation. Sources: [EWA-DB data descriptor](https://www.nature.com/articles/s41597-024-04171-6); [ParkMAE paper and dataset table](https://pmc.ncbi.nlm.nih.gov/articles/PMC12780117/).

## Access request form

Use the [official Zenodo record](https://zenodo.org/records/10952480), sign in or create the researcher's own account if requested, submit the access request and verify the email. The record says its team will send a EULA; read it, complete it truthfully, and return it only after reviewing its permitted uses, restrictions, retention and publication rules. Do not agree to terms on behalf of an institution or supervisor.

## Questions to send the data custodian

1. Is access to the WAV release permitted for an MBBS student's academic secondary-data project based at Bukhara State Medical Institute, Uzbekistan? Which institutional, supervisor, ethics or data-use documents are required?
2. Among the WAV-released participants, how many unique people have PD, healthy-control, mixed AD+PD, AD and MCI labels? For each group, how many have the sustained /a/ task? Could we receive a de-identified participant-level manifest with random IDs, task/recording IDs and diagnosis labels, under the EULA?
3. Can the provider reconcile the official counts (1,649 total; 1,122 meeting defined inclusion criteria; 1,003 with published WAVs) with the 956-person PD/control subset (95 PD/861 controls; 6,692 recordings) reported by ParkMAE? Is that subset reproducible from the current release/version?
4. Does the PD folder include both manifest and prodromal PD? Can the manifest identify these separately, and indicate the diagnostic basis and any available Hoehn–Yahr/severity or medication-state fields?
5. Do stable anonymized IDs identify repeated recordings and participant visits? What is the exact number of sessions/takes per person and the relationship between audio files and JSON records?
6. Which fields are covered by the EULA and available for secondary research: age, sex/gender, education, MoCA, recording device/site/date, task labels, quality flags and inclusion-criterion status?
7. Are there any known participant overlaps with any releases in the literature we may use for model development? We will keep EWA-DB completely outside model training, tuning and pretraining if using it as external validation.
8. May the project publish aggregate QC statistics and code, while keeping audio, participant IDs, row-level manifests, transcripts and embeddings private? Are derived features/embeddings governed by the same restrictions?

## Email draft

**To:** `milan.rusko@savba.sk`  
**Subject:** Research access and manifest clarification for EWA-DB (ELRA-S0489 / Zenodo 10952480)

Dear Dr. Rusko and the EWA-DB team,

I am an MBBS student at Bukhara State Medical Institute in Uzbekistan, preparing a secondary-data research project on the reliability of voice-based Parkinson's disease screening across independent cohorts. I am interested in using EWA-DB as a held-out external cohort, with the primary analysis limited to the sustained /a/ phonation task and any connected-speech analysis prespecified separately.

I have read the EWA-DB data descriptor and the restricted Zenodo record. I understand that access requires a request and an End User License Agreement (EULA). Could you advise whether student-led academic secondary analysis is eligible, and what supervisor, institutional or ethics/governance documentation is required? I will obtain any required institutional determination before analysis and will follow the granted terms.

Before finalizing the study design, could you also clarify the number of unique participants with available WAV recordings in the PD and healthy-control groups for sustained /a/ phonation; whether manifest and prodromal PD can be identified separately; and whether a de-identified participant/task/recording manifest is available under the agreement? The public descriptor reports 1,649 total speakers, 1,122 meeting defined inclusion criteria, and 1,003 with published WAV recordings, whereas the ParkMAE paper reports a 956-person PD/control EWA-DB subset (95 PD, 861 controls; 6,692 audio files). I would appreciate guidance on how these counts map to the current release.

I would use the files only under the approved license, keep raw audio and participant-level materials private, avoid redistribution, and publish aggregate quality-control results and code only to the extent permitted. I would also keep EWA-DB out of model development and tuning if it is used as external validation.

Thank you for your time and for making this resource available to research.

Best regards,  
[Full name]  
MBBS student, Bukhara State Medical Institute, Uzbekistan  
[Institutional email]  
[Supervisor/contact, if required]

## Audit plan once access is granted

### A. Administrative and provenance gate
- Save the exact granted EULA/access terms, release/version, access date and permitted use in a private local record—not public GitHub.
- Verify the accepted diagnosis definition, whether the target is manifest PD only or includes prodromal PD, and the provider's mapping from group folders to clinical labels.
- Confirm whether age/gender/education and quality flags may be used and reported; confirm whether aggregated row counts and code may be published.
- Confirm stable participant IDs, repeats, multiple takes and visit structure; confirm non-overlap with all source cohorts and ensure EWA-DB is not used in any training/pretraining or tuning.

### B. Local technical audit
The repository contains `scripts/audit_ewa_db_local.py`. Run it only against the lawfully downloaded local copy; it produces aggregate JSON and no participant IDs, filenames, hashes or metadata records.

```bash
python scripts/audit_ewa_db_local.py \
  --root /path/to/authorized/EWA-DB \
  --pd-dir '<exact PD folder name>' \
  --control-dir '<exact healthy-control folder name>' \
  --task-dir phonation \
  --out ewa_db_audio_audit_aggregate.json
```

First inspect the names of the top-level group folders locally and pass the exact names; do not upload a folder listing or IDs. Confirm the exact task-folder name (the paper names it `phonation`). The script checks readable WAV headers, channel/sample-rate/bit-depth counts, durations, recording counts by task, repeated recordings per participant folder and exact-duplicate audio hashes. Test run on synthetic audio passed. It has **not** been run on EWA-DB.

### C. Required cohort-level checks before promotion
- Match the provider manifest to recordings and task folders without publishing participant IDs.
- Confirm usable PD and healthy-control counts for sustained /a/, count exclusions, and quantify missingness by diagnosis.
- Inspect WAV integrity, exact duplicates, low-quality flags and recording duration; determine whether repeated takes are independent clips from the same participant.
- Summarize allowed demographics by diagnosis; compare age, gender, education, MoCA, device/site and quality where available to identify confounding.
- Prespecify inclusion/exclusion, participant-grouped sampling, feature/audio normalization and the primary task.
- Exclude or separately analyze prodromal PD and mixed AD+PD; do not silently combine clinically heterogeneous labels.
- Check overlap and potential information leakage. The EWA cohort must remain entirely held out for external evaluation; do not use any EWA recordings/features/embeddings for training, tuning, threshold selection or pretraining.
- Publish only aggregate QC and permitted analysis outputs. Never commit the EULA, raw WAVs, participant IDs, JSON metadata rows, file manifests, transcripts or embeddings to public GitHub.

## Promotion decision rule

EWA-DB becomes an approved third cohort only after legal access is documented; sustained /a/ recordings exist for both PD and healthy controls; participant-level diagnosis/ID/task mapping and repeat-session scheme are understood; license-governed metadata use is settled; dataset integrity passes; and independent held-out status is defensible. Until then, status is **candidate / access pending**, and no confirmatory model training starts.


## Utility test result

The aggregate-only utility's synthetic test workflow passed: [GitHub Actions run 40183230376](https://github.com/culprit-k/parkinsons-voice-ai/actions/runs/40183230376). It verified group/recording counts, exact duplicate detection across labels, that participant IDs/file names/local paths do not appear in aggregate JSON, and that missing class folders fail closed. The workflow used synthetic files only; it is not an EWA-DB data audit.
