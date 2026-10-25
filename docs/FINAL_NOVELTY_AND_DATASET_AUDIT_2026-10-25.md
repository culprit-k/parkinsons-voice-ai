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

The raw-data request is **not completed**. Download attempts to Hugging Face, Figshare and Zenodo fail in this runtime with DNS resolution errors. We have not obtained archive bytes, recomputed hashes, unpacked audio or linked sample IDs to diagnosis labels. The remote metadata review uncovered a material IPVS file-count discrepancy. This document intentionally separates public metadata evidence from local file verification.

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

### Italian Parkinson's Voice and Speech (IPVS / ItalianPVS)

Sources: [official IEEE DataPort record](https://ieee-dataport.org/open-access/italian-parkinsons-voice-and-speech), DOI 10.21227/aw6b-tg17; [public Hugging Face mirror](https://huggingface.co/datasets/birgermoell/Italian_Parkinsons_Voice_and_Speech/tree/main/italian_parkinson).

Remote mirror metadata reviewed:
- Declared licence: CC BY 4.0.
- Folder categories displayed: 28 PD directories, 22 elderly-control directories, 15 young-control directories.
- ZIP file: about 593 MB; pinned mirror revision 70d1714cf738b248d687b003551351cbe37e0298.
- Host-displayed SHA-256: 3c4cd221345f7a81f0eeaceedf44dedbfd33b08ecd18ab5a3307edefcfbacfed. This is host metadata, not a hash independently computed by our project.
- The mirror reports 839 uploaded files and its converted viewer reports around 1.66k rows; the latter must not be treated as a raw WAV or participant count.

**Unresolved inventory discrepancy:** prior dataset documentation describes 831 WAVs (437 PD, 349 elderly controls, 45 young controls) plus six spreadsheets. Adding the ZIP itself gives 838 files, while the mirror lists 839 files. The difference is unresolved. The archive itself must be downloaded and inventoried; it is not safe to choose one count without evidence.

A separate public repository reports that three of the 28 PD folders are repeat sessions, resulting in 25 unique PD participants; it also reports acquisition confounding and an IPVS silence-only AUROC of 1.000. These observations matter as public prior art but have not been reproduced by this project's own data processing.

| Verification step | Status in this project |
|---|---|
| Public mirror/licence/source metadata observed | Verified remotely |
| ZIP size and host-displayed hash recorded | Verified remotely as page metadata only |
| ZIP bytes downloaded into our project | **Not done; runtime DNS fails** |
| SHA-256 recomputed locally | **Not done** |
| ZIP unpacked; 839-vs-838 discrepancy reconciled | **Not done** |
| WAV sample rate, encoding, channels, durations, corruption inspected | **Not done** |
| Participant IDs/repeated sessions/demographic label joins audited | **Not done** |

### UAMS telephone-recorded prolonged /a/

Source: [Figshare record](https://figshare.com/articles/dataset/Voice_Samples_for_Patients_with_Parkinson_s_Disease_and_Healthy_Controls/23849127).

Remote metadata says:
- Figshare advertises an all-files archive of 4.18 MB and declares CC BY 4.0.
- The demographic spreadsheet is described as linking Sample ID, age, sex and HC/PwPD label to PD_AH.zip and HC_AH.zip.
- Voice files are WAV recordings of prolonged /a/ recorded using participants' telephones.
- The associated literature describes a public subset with 40 PD and 41 controls. The original paper and a later correction should be checked before relying on nonessential methods or performance claims. [Original paper](https://pubmed.ncbi.nlm.nih.gov/37996478/) · [Correction record](https://pubmed.ncbi.nlm.nih.gov/42562853/)

**Integrity status:** the Figshare download endpoint was inaccessible in this runtime. No ZIP or workbook was downloaded. Actual WAV count, unique IDs, duplicates/repeats, sample rates, demographic joins, and label provenance are unverified locally. The remote file size and paper cohort counts are not a substitute for inspecting the archive.

### mPower

mPower has smartphone sustained-/a/ recordings, often repeated in uncontrolled settings. Access is through Synapse research/data-use procedures, rather than a guaranteed anonymous one-click archive. Some studies use self-reported professional diagnosis, which must not automatically be equated with an independently adjudicated clinical diagnosis. This project has not requested/received data access and has no local manifest. [Original mPower study](https://www.nature.com/articles/sdata201611) · [Recent voice transfer study](https://www.nature.com/articles/s41598-024-81824-x)

Status: possible third cohort, **not approved** pending access, label-provenance and unique-participant audit.

### MDVR-KCL

Source: [Zenodo DOI 10.5281/zenodo.2867216](https://doi.org/10.5281/zenodo.2867216). The public dataset is described as English continuous speech, whereas UAMS and the intended IPVS comparison use sustained /a/. The raw archive and checksum have not been verified by this project. Do not count MDVR-KCL as an interchangeable third cohort in a sustained-vowel analysis. It could support a separate continuous-speech design, but the public Parkinson-Voice-Detection repository already overlaps substantially on IPVS/MDVR-KCL shortcut controls and cross-corpus evaluation.

## 3. Final data decision

**Raw-data gate: FAIL / NOT PASSED.** This is a status of our verification process, not proof the datasets are unusable.

Two candidates are identified for a sustained-/a/ recording-domain feasibility study:
- IPVS: usable candidate, subject to resolving the mirror inventory discrepancy, participant identity, and acquisition confounding.
- UAMS: usable candidate, subject to archive and workbook verification.

mPower may be a third recording domain, but access and labels have not passed. Therefore, a three-cohort confirmatory benchmark is **not currently established**.

Important scope correction: comparing sustained /a/ cohorts tests cross-dataset/recording-domain robustness. It does not, by itself, test lexical cross-language generalization. For a genuine language-generalization claim, we would need compatible connected-speech tasks and methods that separate language from site, task, device, recruitment and demographic differences.

## 4. Reproducible next step and stop/go criteria

In a network-enabled research environment, attempt the two public archives and write the audit files outside Git:
- IPVS ZIP: use the pinned Hugging Face link above and check SHA-256 against the host metadata.
- UAMS Figshare: https://figshare.com/ndownloader/articles/23849127

The companion script at scripts/verify_voice_dataset_archives.py performs archive downloads, local SHA-256 calculation, safe ZIP extraction, audio file inventory, basic WAV-header inspection and duplicate-file hash reporting. It writes raw data and private manifests under data/raw/_audit/; these must never be committed. The script has **not** been executed successfully in this network-restricted runtime.

Even when the script runs, additional human/data-curation checks remain mandatory:
1. Reconcile the IPVS file inventory and independently recompute checksums.
2. Join audio files to stable anonymised participant keys and diagnosis labels; inspect repeated recordings and duplicate content.
3. Check the UAMS spreadsheet against the WAV archives, including unique IDs and demographic missingness.
4. Establish lawful mPower access and confirm diagnostic-variable provenance if a third cohort is needed.
5. Establish three independent, compatible and legally accessible participant cohorts, or explicitly downgrade to a two-cohort pilot.
6. Freeze the statistical analysis plan before looking at the held-out cohort labels or selecting error-detection metrics.

**Final status:** targeted novelty review completed; broad novelty claims rejected; narrow comparison retained only as a conditional study direction; local raw-data integrity verification blocked by runtime DNS failure; no data downloads, local hashes, participant manifest audits, models or empirical results are claimed.


## Additional targeted search results — confidence gating and speech-domain shift

Two further sources found during the final targeted search strengthen the conservative novelty boundary:

- **Confidence-Gated Hybrid CNN Ensemble for PD speech analysis**, Electronics 15(3):587, published 29 January 2026. It uses per-sample confidence indicators (maximum posterior, decision margin, entropy) to gate or weight an ensemble for PD classification on public UCI voice datasets. This is not the same endpoint as ranking incorrect participant-level predictions on held-out cohorts with an acoustic-distance feature, but it means confidence-gated PD voice modelling itself is already reported. [Paper](https://www.mdpi.com/2079-9292/15/3/587)
- **Detection of actionable domain shifts in speech enhancement systems by tracking prediction uncertainty**, published 28 February 2026. This speech-processing study explicitly monitors prediction uncertainty to identify shifts associated with degraded performance. It concerns speech enhancement and shift-at-the-batch/system level, not PD diagnosis or participant-level classification-error ranking, but it is clear adjacent prior art for using uncertainty as a speech-domain-shift signal. [Paper](https://link.springer.com/article/10.1186/s13636-026-00448-3)

These sources do not prove that the exact candidate comparison has already been done, but further reduce support for presenting confidence gating or speech-domain monitoring as a novel method. The plausible contribution remains a narrow comparative test: does a frozen acoustic-distance signal add value beyond confidence for identifying errors in independent PD-voice cohorts?
