# Final targeted novelty and dataset-integrity audit

Audit cutoff: 25 October 2026  
Protocol status: NOT LOCKED  
Confirmatory modelling: NOT STARTED  
Novelty clearance: NOT PASSED  
Raw-data integrity gate: NOT PASSED

## Executive decision

The broad area is already well established: cross-corpus and cross-language Parkinson's disease (PD) voice detection, demographic-confounding audits, uncertainty-aware PD screening, and label-free deployment reliability all have prior art.

Our remaining candidate question is:

> Does a source-reference acoustic-domain-distance score add information beyond predictive confidence when ranking participant-level errors from a fixed PD voice-screening model on independent held-out voice cohorts?

The exact comparative question could be useful, but current evidence does not clear global novelty. We did not identify an exact published match in this targeted search; that is not proof that none exists. Generic OOD and error-monitoring research is close prior art. Do not claim a new general algorithm, "first", patentability, or guaranteed novelty. The study should be described as a voice-specific comparative external-validation benchmark, and only after a more complete database and citation-chain search.

The raw-data audit is now **partially completed through a network-enabled GitHub Actions runner**; this supersedes the earlier note about DNS failures in the interactive runtime. The successful run downloaded and inventoried IPVS, UAMS and MDVR-KCL: [run 40170614840](https://github.com/culprit-k/parkinsons-voice-ai/actions/runs/40170614840). IPVS archive SHA-256 matched the pinned mirror and all 831 WAV headers were readable; UAMS source-file MD5 checks and all 81 WAV headers passed, with 81/81 sample IDs matching audio filename stems; MDVR-KCL source MD5 and all 73 WAV headers passed. These are archive/audio integrity checks, not confirmation of independent participants or clinical label validity. The full feasibility gate remains **NOT PASSED** because IPVS participant/session mapping and a privacy issue remain open, UAMS diagnosis provenance/participant independence need confirmation, MDVR-KCL participant/diagnosis mapping is unresolved, and a third compatible independent cohort is not yet available.

## 1. Novelty verdict

| Proposed direction | Prior-art finding | Decision |
|---|---|---|
| PD voice classification across datasets | Established. Hireš et al. tested four datasets and reported degraded performance on new datasets, including sustained-vowel data. | Not a novelty claim. |
| Cross-language PD speech models | Established. ParkMAE reports multilingual pretraining and cross-linguistic evaluation across four languages. | Not a novelty claim. |
| IPVS/MDVR-KCL shortcut audits plus cross-corpus model | Close public overlap. A public repository contains methods, scripts, notebooks, findings, result tables, figures, provenance and a model artifact describing IPVS silence/channel controls and IPVS-to-MDVR-KCL cross-corpus evaluation. Its reported numbers have not been independently reproduced by this project, but the public work itself is material prior art. | Do not present this as our independent contribution. |
| Demographic confounding in voice screening | Established. Shukla et al. (2026) evaluate age/site confounding and use demographic-only baselines on Bridge2AI Voice. | Include demographic-only comparisons and subgroup/restricted analyses where metadata permit; not novel by itself. |
| Confidence or uncertainty-aware PD screening | Established/adjacent. PARK (2026) evaluates uncertainty-aware remote multimodal screening; Guo et al. (2026) describe uncertainty-aware speech assessment with external Spanish-to-Italian evaluation. | Confidence, calibration, uncertainty, or external validation alone are not our contribution. |
| Label-free error/reliability detection or deployment monitoring | Established beyond PD voice. SUDO (2024) estimates clinical-AI reliability under shift without labels. D3M (NeurIPS 2025) monitors degradation after deployment using model disagreement. | Do not claim invention of generic OOD or label-free reliability monitoring. |
| **Confidence-only vs confidence plus acoustic distance for participant-level error ranking under held-out PD-voice cohort shift** | **Potentially distinct as a prespecified comparative study, but not cleared as a novel method.** No exact match was identified in the targeted sources reviewed, but adjacent literature is strong and a broader search could reveal direct overlap. | Conditional GO for literature/data feasibility only; not registered and not ready for confirmatory modelling. |

### Key sources

1. Hireš et al. (2023), "On the inter-dataset generalization of machine learning approaches to Parkinson's disease detection from voice." Four-dataset evaluation found that high within-dataset performance did not reliably transfer to unseen datasets. [PubMed](https://pubmed.ncbi.nlm.nih.gov/37801807/) · [ScienceDirect](https://www.sciencedirect.com/science/article/pii/S1386505623002551)

2. ParkMAE, Scientific Reports (online publication 10 December 2025; volume 16, 2026): multilingual speech foundation model and evaluation across four languages. This is direct prior art for multilingual PD speech modelling. [Paper](https://www.nature.com/articles/s41598-025-30251-7) · [PMC](https://pmc.ncbi.nlm.nih.gov/articles/PMC12780117/)

3. Public repository Parkinson-Voice-Detection. The inspected Git tree has 183 entries, including phase scripts/notebooks, methods, findings, dataset version notes, figures/tables and a model artifact. Its authors report an IPVS silence-only AUROC of 1.000 and IPVS/MDVR-KCL cross-corpus experiments, including eGeMAPSv02 LOCO evaluation. These are the repository authors' claims, not results independently reproduced in our project; however, their public methods and claims establish material prior art for the broad project framing. [Repository](https://github.com/BennedictQuanTon/Parkinson-Voice-Detection/) · [Findings](https://github.com/BennedictQuanTon/Parkinson-Voice-Detection/blob/main/FINDINGS.md) · [Dataset version notes](https://github.com/BennedictQuanTon/Parkinson-Voice-Detection/blob/main/docs/DATASET_VERSION.md)

4. Shukla et al. (20 August 2026), demographic confounding in Bridge2AI Voice. The authors found age alone was competitive with the speech model on the full cohort, and adjusted/restricted estimates were lower. Their recommendations make demographic-only baselines and careful cohort construction important. [JMIR](https://www.jmir.org/2026/1/e95609)

5. PARK, Communications Medicine (6 May 2026), remote multimodal PD screening over eight studies and 1,865 participants. The system combines speech with facial and motor measures and analyses predictive uncertainty. This is adjacent prior art, although not the same voice-only distance-plus-confidence comparison. [PMC full text](https://pmc.ncbi.nlm.nih.gov/articles/PMC13586151/)

6. Guo et al. (2026), uncertainty-aware voice assessment with Spanish-to-Italian external evaluation. This further limits any uncertainty-only or external-validation novelty claim. [DOI](https://doi.org/10.1007/s40846-026-01040-y) · [Code](https://github.com/guoleiyong/PD-Voice-MM-CAF)

7. SUDO (Kiyasseh et al., Nature Communications 2024) is a generic label-free clinical-AI reliability framework that can identify unreliable predictions under shift, including overconfident errors. This is conceptually close prior art. [Paper](https://www.nature.com/articles/s41467-024-46000-9)

8. D3M (NeurIPS 2025) addresses label-free monitoring of model degradation after deployment using predictive model disagreement. [Paper](https://proceedings.neurips.cc/paper_files/paper/2025/hash/0bb251eba663f0345c0929f5bbbfb6dc-Abstract-Conference.html)

9. Shahriar, PLOS One (5 August 2026), evaluates uncertainty-aware personalized severity estimation from longitudinal PD speech. Its target is severity rather than PD/control screening, but it is additional adjacent work against a broad uncertainty novelty claim. [Paper](https://journals.plos.org/plosone/article?id=10.1371/journal.pone.0343191)

### Defensible future wording

After the remaining search and data gates, the contribution could be worded as:

> "We evaluate whether a prespecified acoustic-domain-distance signal improves participant-level error ranking beyond classifier confidence under external cohort shift in Parkinson's voice screening."

Do not write "we propose a novel OOD algorithm", "first cross-lingual model", "clinically validated", or "most accurate" on the current evidence.

### Search-scope limitation

This is a targeted novelty audit, **not** a completed PRISMA-style systematic review. Searches and source checks covered cross-corpus/cross-language PD voice, external validation, confidence/uncertainty, reliability/error detection, demographic confounding, public dataset access and repository prior art. A registered or systematic review still needs database-specific search strings, deduplication, screening logs, inclusion/exclusion reasons, backward/forward citation chasing and verification of bibliographic records. Absence of an exact match in this targeted audit is not proof of universal absence.

## 2. Dataset metadata and integrity findings

> **Editorial status note:** The subsection below began as a remote-metadata-only snapshot. Where it conflicts with the actual archive findings in the “Addendum: actual archive verification completed on GitHub Actions” near the end of this file, the later addendum is authoritative. The stale per-dataset status rows in this early snapshot are being retained only to preserve the audit trail of what was known before the runner job.

### Italian Parkinson's Voice and Speech (IPVS / ItalianPVS)

Sources: [official IEEE DataPort record](https://ieee-dataport.org/open-access/italian-parkinsons-voice-and-speech), DOI 10.21227/aw6b-tg17; [public Hugging Face mirror](https://huggingface.co/datasets/birgermoell/Italian_Parkinsons_Voice_and_Speech/tree/main/italian_parkinson).

Remote mirror metadata reviewed:
- Declared licence: CC BY 4.0.
- Folder categories displayed: 28 PD directories, 22 elderly-control directories, 15 young-control directories.
- ZIP file: about 593 MB; pinned mirror revision 70d1714cf738b248d687b003551351cbe37e0298.
- Host-displayed SHA-256: 3c4cd221345f7a81f0eeaceedf44dedbfd33b08ecd18ab5a3307edefcfbacfed. This is host metadata, not a hash independently computed by our project.
- The mirror reports 839 uploaded files and its converted viewer reports around 1.66k rows; the latter must not be treated as a raw WAV or participant count.

**Inventory count reconciled:** the downloaded archive extracted to 831 WAV + 6 XLSX + 1 TXT = 838 extracted files. The public mirror listing contains 839 items because it also lists the ZIP archive itself. This explains the one-item difference between the listing and extracted file inventory; no extra WAV is inferred.

A separate public repository reports that three of the 28 PD folders are repeat sessions, resulting in 25 unique PD participants; it also reports acquisition confounding and an IPVS silence-only AUROC of 1.000. These observations matter as public prior art but have not been reproduced by this project's own data processing.

| Verification step | Status in this project |
|---|---|
| Public mirror/licence/source metadata observed | Verified remotely |
| ZIP size and host-displayed hash recorded | Verified remotely as page metadata only |
| ZIP bytes downloaded and extracted through GitHub Actions | **PASS** — [run 40170614840](https://github.com/culprit-k/parkinsons-voice-ai/actions/runs/40170614840) |
| SHA-256 recomputed locally on runner | **PASS** — matches pinned mirror digest |
| Extracted inventory reconciled with mirror listing | **PASS** — 838 extracted files plus the ZIP listing item = 839 listed items |
| WAV format/header, channels, sample rates, duration and exact duplicate hashes inspected | **PASS for file-level QC** — 831/831 headers readable; one duplicate hash pair |
| Participant IDs/repeated sessions/clinical label joins audited | **OPEN** — the spreadsheets do not supply a fully verified anonymized participant/audio/diagnosis mapping; direct names/surnames appear in at least one workbook |

### UAMS telephone-recorded prolonged /a/

Source: [Figshare record](https://figshare.com/articles/dataset/Voice_Samples_for_Patients_with_Parkinson_s_Disease_and_Healthy_Controls/23849127).

Remote metadata says:
- Figshare advertises an all-files archive of 4.18 MB and declares CC BY 4.0.
- The demographic spreadsheet is described as linking Sample ID, age, sex and HC/PwPD label to PD_AH.zip and HC_AH.zip.
- Voice files are WAV recordings of prolonged /a/ recorded using participants' telephones.
- The associated literature describes a public subset with 40 PD and 41 controls. The original paper and a later correction should be checked before relying on nonessential methods or performance claims. [Original paper](https://pubmed.ncbi.nlm.nih.gov/37996478/) · [Correction record](https://pubmed.ncbi.nlm.nih.gov/42562853/)

**Integrity status:** file-level audit passed in [GitHub Actions run 40175159872](https://github.com/culprit-k/parkinsons-voice-ai/actions/runs/40175159872). Three Figshare source files were downloaded individually through the public API; all published per-file MD5 checks passed. The extracted inventory is 81 WAV + one XLSX workbook. All 81/81 WAV headers are readable, mono at 8 kHz, with durations 1.51612–7.208 s. The workbook has 81 unique Sample IDs and labels 41 HC / 40 PwPD; all 81 matched exact normalized audio filename stems, with zero missing IDs, duplicate ID rows or conflicting-label IDs; no exact duplicate-audio hashes were detected.

**Clinical and selection provenance clarified from the published sources:** the source study originally recruited 50 PwPD and 50 healthy controls. The 2025 peer-reviewed follow-up reports that the analysis subset contains 40 PD and 41 control recordings after discarding recordings shorter than 1.5 seconds after trimming silence. It says PwPD were examined and diagnosed by a movement-disorders neurologist, whereas healthy controls and mPower participants were not neurologically examined and self-reported whether they had voice, neurological or psychiatric conditions. In that analysis subset, mean age was **66.6 ± 9.0 years for PD versus 47.9 ± 14.5 for controls**, a material potential age shortcut. Sources: [2025 Scientific Reports study](https://pmc.ncbi.nlm.nih.gov/articles/PMC11873116/), [UAMS dataset paper](https://pubmed.ncbi.nlm.nih.gov/37996478/).

**Important literature correction:** on 6 August 2026, the authors corrected their 2023 UAMS voice-identification paper because of an implementation issue in its CNN analysis pipeline. The corrected CNN mean AUC is **0.83** for both colour and greyscale spectrograms, replacing the originally reported 0.97 and 0.96; the table/results for some conventional baselines were also corrected. Do not quote the original CNN performance as valid. [Author correction](https://pmc.ncbi.nlm.nih.gov/articles/PMC13448817/).

Therefore, UAMS label provenance is no longer simply “unknown”: the PD arm has a reported specialist diagnosis, while the HC arm relies on self-report without a neurologist examination. The key remaining items are confirmation that the released sample IDs are one-per-independent-person/no repeat visits, plus a prespecified age-confounding strategy (age-only baseline and defensible age-restricted sensitivity analyses if cell sizes permit).

### mPower

mPower has smartphone sustained-/a/ recordings, often repeated in uncontrolled settings. Access is through Synapse research/data-use procedures, rather than a guaranteed anonymous one-click archive. Some studies use self-reported professional diagnosis, which must not automatically be equated with an independently adjudicated clinical diagnosis. This project has not requested/received data access and has no local manifest. [Original mPower study](https://www.nature.com/articles/sdata201611) · [Recent voice transfer study](https://www.nature.com/articles/s41598-024-81824-x)

Status: possible third cohort, **not approved** pending access, label-provenance and unique-participant audit.

### MDVR-KCL

Source: [Zenodo record](https://zenodo.org/records/2867216). The source file was downloaded through the Zenodo API; its MD5 matched Zenodo metadata. The extracted inventory contains 73 WAV files, all with readable headers, mono at 44.1 kHz, durations 73.03902–220.63916 s, and no exact duplicate-audio hash groups. The raw participant-ID and file-to-diagnosis manifest has **not** been verified. Its read-text and spontaneous-dialogue tasks are not interchangeable with sustained /a/. Do not count MDVR-KCL as the sustained-vowel third cohort; it may support a separate connected-speech design if participant-label mapping is verified. The public Parkinson-Voice-Detection repository is close prior art for IPVS/MDVR-KCL shortcut controls and cross-corpus evaluation.

## 3. Final data decision

**Raw-data gate: FAIL / NOT PASSED.** This is a status of our verification process, not proof the datasets are unusable.

Two **provisional** candidates for a sustained-/a/ recording-domain feasibility study are IPVS and UAMS, but neither is approved for final analysis. IPVS file integrity passed; participant/session and label mapping remain unresolved and the source package contains direct identifiers. UAMS archive integrity and filename linkage passed, and published sources clarify diagnosis sources and serious age imbalance: PD diagnoses were specialist-confirmed, but controls were self-reported and substantially younger on average; a 2026 correction also reduced a widely quoted prior CNN AUC from 0.97/0.96 to 0.83. One-person-per-Sample-ID/repeat-visit status still needs confirmation. MDVR-KCL passed file-level integrity but its tasks and participant-label linkage do not support the sustained-vowel primary benchmark. EWA-DB is the priority third-cohort access request; mPower is a secondary access route. Neither has been approved or obtained. Therefore, a three-cohort confirmatory benchmark is **not currently established**.

Important scope correction: comparing sustained /a/ cohorts tests cross-dataset/recording-domain robustness. It does not, by itself, test lexical cross-language generalization. For a genuine language-generalization claim, we would need compatible connected-speech tasks and methods that separate language from site, task, device, recruitment and demographic differences.

## 4. Reproducible next step and stop/go criteria

The archive-audit script has now run successfully on a network-enabled GitHub Actions runner for IPVS, UAMS and MDVR-KCL; see [run 40170614840](https://github.com/culprit-k/parkinsons-voice-ai/actions/runs/40170614840). Raw archives, individual audio manifests and private summaries remain only in the runner workspace and were not uploaded to GitHub. The checked-in workflow uploads only a sanitized aggregate report.

The companion script at scripts/verify_voice_dataset_archives.py performs archive downloads, local SHA-256 calculation, safe ZIP extraction, audio file inventory, basic WAV-header inspection and duplicate-file hash reporting. It writes raw data and private manifests under data/raw/_audit/; these must never be committed. The script has **not** been executed successfully in this network-restricted runtime.

Even when the script runs, additional human/data-curation checks remain mandatory:
1. Reconcile the IPVS file inventory and independently recompute checksums.
2. Join audio files to stable anonymised participant keys and diagnosis labels; inspect repeated recordings and duplicate content.
3. Check the UAMS spreadsheet against the WAV archives, including unique IDs and demographic missingness.
4. Establish lawful mPower access and confirm diagnostic-variable provenance if a third cohort is needed.
5. Establish three independent, compatible and legally accessible participant cohorts, or explicitly downgrade to a two-cohort pilot.
6. Freeze the statistical analysis plan before looking at the held-out cohort labels or selecting error-detection metrics.

**Final status:** targeted novelty review completed but global novelty is **not cleared**; broad algorithm novelty claims are rejected; a narrow comparison remains a conditional study direction. Archive/audio file-integrity checks passed for IPVS, UAMS and MDVR-KCL in the runner. Participant/diagnosis mapping, privacy/governance, UAMS diagnosis provenance, MDVR-KCL participant linkage, and a third compatible independent cohort remain unresolved. No model has been trained and no predictive results have been produced.


## Additional targeted search results — confidence gating and speech-domain shift

Two further sources found during the final targeted search strengthen the conservative novelty boundary:

- **Confidence-Gated Hybrid CNN Ensemble for PD speech analysis**, Electronics 15(3):587, published 29 January 2026. It uses per-sample confidence indicators (maximum posterior, decision margin, entropy) to gate or weight an ensemble for PD classification on public UCI voice datasets. This is not the same endpoint as ranking incorrect participant-level predictions on held-out cohorts with an acoustic-distance feature, but it means confidence-gated PD voice modelling itself is already reported. [Paper](https://www.mdpi.com/2079-9292/15/3/587)
- **Detection of actionable domain shifts in speech enhancement systems by tracking prediction uncertainty**, published 28 February 2026. This speech-processing study explicitly monitors prediction uncertainty to identify shifts associated with degraded performance. It concerns speech enhancement and shift-at-the-batch/system level, not PD diagnosis or participant-level classification-error ranking, but it is clear adjacent prior art for using uncertainty as a speech-domain-shift signal. [Paper](https://link.springer.com/article/10.1186/s13636-026-00448-3)

These sources do not prove that the exact candidate comparison has already been done, but further reduce support for presenting confidence gating or speech-domain monitoring as a novel method. The plausible contribution remains a narrow comparative test: does a frozen acoustic-distance signal add value beyond confidence for identifying errors in independent PD-voice cohorts?


## Addendum: actual archive verification completed on GitHub Actions — 25 October 2026

This addendum supersedes the earlier statement in this document that raw archive verification had not been performed. The initial local runtime could not resolve the dataset hosts, so I added a network-enabled GitHub Actions workflow and ran the archive audit there. No audio or participant-level manifest was uploaded as an artifact; only a sanitized aggregate report was uploaded.

### IPVS archive — byte integrity and audio inventory passed; participant mapping remains unresolved

- Downloaded archive size: **592,905,531 bytes**.
- Locally computed SHA-256: 3c4cd221345f7a81f0eeaceedf44dedbfd33b08ecd18ab5a3307edefcfbacfed.
- This exactly matches the SHA-256 shown by the pinned public mirror.
- Extracted inventory: **831 WAV + 6 XLSX + 1 TXT = 838 files**. The mirror's 839-item upload count includes the ZIP itself, explaining the apparent discrepancy.
- All **831/831 WAV headers** were readable; all were mono. 671 were 16 kHz and 160 were 44.1 kHz. Durations ranged from 3.375 to 250.3125 seconds.
- Folder labels yield 437 PD-labelled, 349 elderly-control-labelled and 45 young-control-labelled WAV files. These are recording counts, not participant counts.
- Exact content-hash audit found one duplicate group of two WAV files. The private paths were not published; this duplicate pair must be located in the private manifest and adjudicated before model splitting.
- One or more spreadsheets contain name and surname columns alongside demographics. **Direct identifiers are present in the public package.** Do not copy or commit these spreadsheets, names, or raw audio into this GitHub repository. Do not attempt to link names to audio for the research protocol without a data-governance/ethics review. The current automatic audit does not establish a reliable participant-ID-to-label mapping for IPVS.
- Nested folder structure is not a reliable participant manifest on its own: PD recordings are organised across multiple directory levels. A source-specific, privacy-preserving mapping is still needed to resolve repeated sessions and unique participants.

### UAMS telephone vowel archive — archive and ID-label join checks passed at the file level

The public Figshare API was used to download the source files individually after its "download all" endpoint returned HTTP 401.

- Total downloaded source-file bytes: **4,378,057**.
- The audit completed all available per-file MD5 checks against the public API metadata without a mismatch.
- Extracted inventory: **81 WAV files plus one XLSX workbook**.
- All **81/81 WAV headers** were readable; all were mono at 8 kHz. Durations ranged from 1.51612 to 7.208 seconds.
- The workbook's Parselmouth sheet contains 81 rows, 81 unique Sample IDs, no missing Sample IDs, and labels **41 HC / 40 PwPD**.
- All **81/81** Sample IDs matched an audio filename; zero unmatched IDs were found.
- The same workbook contains derived-feature sheets. For the planned reproducible analysis, use the raw WAV files and recompute features from the audio rather than treating precomputed feature sheets as independent recordings.
- The audit found no exact duplicate-audio hash groups among the 81 WAV files.
- The workbook contains demographic fields (age and sex), but no direct name/surname fields were detected in the sheet used for ID-label linkage. Diagnosis provenance and participant independence still need confirmation from the dataset paper/data documentation.

### What has and has not passed

| Gate | Result |
|---|---|
| IPVS archive byte integrity | **PASS** — local SHA-256 matches pinned mirror |
| IPVS WAV header and basic format inventory | **PASS** |
| IPVS duplicate-file review | **OPEN** — one exact duplicate pair |
| IPVS unique participant/session and label mapping | **OPEN** — no verified participant-level manifest; direct identifiers present in workbook |
| UAMS source-file checksum checks | **PASS** — per-file MD5 checks passed |
| UAMS WAV header and basic format inventory | **PASS** |
| UAMS Sample ID to audio filename linkage | **PASS** — 81/81 matched |
| UAMS unique participant count | **Provisionally 81 Sample IDs**; independence/repeated visits require source confirmation |
| Three independent compatible cohorts | **NOT ESTABLISHED** |
| Protocol lock / confirmatory modelling | **NOT APPROVED** |

The initial IPVS/UAMS workflow succeeded at run 40170280356; the expanded three-dataset workflow later succeeded at [run 40170614840](https://github.com/culprit-k/parkinsons-voice-ai/actions/runs/40170614840). The earlier Figshare all-files endpoint returned 401, so UAMS files were subsequently downloaded individually through the public Figshare API. The report upload includes aggregate QC only; raw audio and participant-level paths are not published. The workflow report deliberately excludes raw audio and participant-level paths.

**Updated decision:** archive integrity is now verified for IPVS and UAMS, but the dataset feasibility gate as a whole remains **NOT PASSED**. The main blocker is no longer download access; it is the IPVS participant/label mapping and direct-identifier risk, plus the absence of a third independent, compatible cohort. No model has been trained and no predictive results have been produced.


### MDVR-KCL archive — file integrity passed; task/label linkage remains unverified

The Zenodo API download and inventory succeeded in [GitHub Actions run 40170614840](https://github.com/culprit-k/parkinsons-voice-ai/actions/runs/40170614840).

- One source archive/file of **606,144,431 bytes** was downloaded. Its MD5 matched the checksum in Zenodo metadata.
- Extracted inventory: **73 WAV files**; all 73 WAV headers readable, all mono at 44.1 kHz. Durations ranged from 73.03902 to 220.63916 seconds.
- No exact duplicate-audio hash groups were detected.
- The raw inventory does not by itself establish participant IDs or verified file-to-diagnosis labels. Literature describes 37 participants (16 PD and 21 controls) with read-text and spontaneous-dialogue tasks, but this project has not verified the participant-level manifest from the raw files.
- MDVR-KCL is **not task-matched** to UAMS sustained /a/ recordings. It could support a connected-speech analysis, but only with a connected-speech cohort from another language and verified participant-level labels.

### Duplicate-file adjudication refinement

The IPVS duplicate-audio pair is in the same parent directory and both files fall under the PD-labelled path category. This suggests an exact duplicate within one folder, but it does not prove whether it is a duplicated file, a repeated session or a valid repeated take. The private manifest must be reviewed locally before deduplication. No file paths or participant names were published.


### Final novelty boundary after dataset audit

The candidate should not be framed as a novel general cross-dataset calibration method. A 2026 limited-target-data calibration paper reports cross-dataset PD-speech transfer using overlapping corpora including IPVS, MDVR-KCL and a US sustained-/ah cohort; the exact endpoint differs, but this is additional close prior art for transfer/calibration on the same data ecosystem. See [the 2026 study](https://nhsjs.com/2026/limited-target-data-calibration-improves-cross-dataset-transfer-for-parkinsons-disease-detection-from-speech/).

NeuroVoz is a potentially valuable Spanish cohort with both sustained-vowel and connected-speech tasks, but its current Zenodo v3 record lists the files as restricted. We have not obtained access and cannot count it as available. EWA-DB is now the prioritized request for a third sustained-vowel-compatible cohort because its catalogue describes sustained vowels and a consented WAV subset; mPower is the secondary route but requires Synapse research access and careful evaluation of self-reported diagnosis. The access-request templates and promotion criteria are in [the third-cohort plan](THIRD_COHORT_AND_ACCESS_REQUEST_PLAN_2026-10-25.md).


## Current decision after three-cohort search — 25 October 2026

A new source search identified EWA-DB (ELRA-S0489) as the prioritized third-cohort request: the catalogue describes 1,649 speakers, audio for 1,003 speakers with written consent, and sustained-vowel phonation among the tasks. This is **not access confirmation**. mPower is another task-matched option via Synapse, but the literature describes account validation, a data-use statement and terms of use, and potential self-reported PD labels. NeuroVoz remains restricted at Zenodo. See [the third-cohort/access plan](THIRD_COHORT_AND_ACCESS_REQUEST_PLAN_2026-10-25.md).

The target study must stay focused on sustained-vowel acoustic-domain robustness if it uses IPVS, UAMS and a vowel cohort. Do not claim lexical or spontaneous-language generalization from sustained vowels. No cohort is approved for final analysis until access, participant IDs, diagnostic provenance, repeats, task mapping and cross-cohort independence are documented. No model has been trained; no performance results exist.

## UCI Dataset 489 audit — successful workflow run

A sanitized automated audit completed successfully on 25 October 2026: [GitHub Actions run 40176480093](https://github.com/culprit-k/parkinsons-voice-ai/actions/runs/40176480093). The official UCI record is [Parkinson Dataset with replicated acoustic features](https://archive.ics.uci.edu/dataset/489/parkinson+dataset+with+replicated+acoustic+features), DOI 10.24432/C5701F, listed under CC BY 4.0.

Aggregate results:
- 240 rows/recordings from **80 participant IDs**, exactly 3 repeated recordings per participant.
- Participant-level labels are balanced at 40 / 40; row-level labels are balanced at 120 / 120.
- No participant changed label across the three repeated rows.
- 44 engineered feature columns were detected by the audit parser; no missing cells were detected in those acoustic-feature columns.
- A sex/gender-coded field is present; age is not present.
- The release contains **no raw WAV audio**. It is a feature-only cohort.

**Interpretation:** this adds a fourth audited public data resource, but it does **not** establish a third compatible audio cohort for the proposed confidence-versus-distance audio benchmark. Its repeated engineered features may support a separate participant-grouped feature-only replication only if original feature extraction and task provenance are sufficiently documented and compatible. The public labels' clinical semantics still need confirmation from the official variable description/source paper before interpreting coded values as control/PD. Do not pool this feature-only release with WAV audio as if they were the same input modality.

No model was trained and no predictive performance was calculated.


## Post-audit establishment update — 25 October 2026

The latest source check resolves UCI Dataset 489's label coding: its official variable text says STATUS 0 = Healthy and 1 = PD; Gender 0 = Man and 1 = Woman. The 44 enumerated acoustic predictors are separate from gender, participant ID, recording number and status. The rows are repeated observations from 80 subjects, not 240 independent people. The feature-only cohort remains unusable as a raw-audio external cohort. [Official UCI definition](https://archive.ics.uci.edu/dataset/489/parkinson+dataset+with+replicated+acoustic+features).

The leading candidate for the missing third raw-audio cohort is EWA-DB (Slovak): 1,649 speakers overall, including 175 PD and 1,323 healthy controls; WAV audio is reported for 1,003 consented speakers, but the label/group counts within that audio subset must be verified. Access is gated through ELRA, and it is not counted as available until authorized access, audio-specific IDs and compatible task labels are confirmed. [Scientific Data description](https://www.nature.com/articles/s41597-024-04171-6) · [ISLRN record](https://www.islrn.org/resources/730-022-142-264-9/).

mPower remains a fallback: it contains sustained /a/ recordings but uses self-reported PD status, repeated observations and controlled Synapse access. UCI Dataset 301 is not a raw-audio substitute in its UCI release; it provides extracted features and a test set containing PD subjects only. [mPower data access/label caveats](https://www.nature.com/articles/s41598-024-81824-x) · [UCI Dataset 301](https://archive.ics.uci.edu/dataset/301/parkinson+speech+dataset+with+multiple+types+of+sound+recordings).

The candidate research question remains: whether a prespecified source-reference acoustic-domain-distance score improves ranking/detection of **participant-level errors** beyond calibrated model confidence on independent held-out cohorts. Novelty is not cleared: prior work already includes multilingual ParkMAE, cross-language Korean/Taiwanese PD speech and a 2026 Spanish-to-Italian uncertainty-aware assessment study. Any contribution must be framed as a narrowly defined comparative reliability benchmark—not a first-of-its-kind model. [ParkMAE](https://www.nature.com/articles/s41598-025-30251-7) · [Lim et al.](https://pubmed.ncbi.nlm.nih.gov/39739129/) · [2026 uncertainty-aware cross-language work](https://doi.org/10.1007/s40846-026-01040-y).

No model has been trained and no performance results have been produced. Protocol and confirmatory modelling gates remain closed.
