# Targeted search log — 2026-10-25

**Purpose:** record the targeted searches performed during preliminary prior-art identification.  
**Important:** this is not a complete systematic search, not a PRISMA flow record, and not evidence that every indexed publication has been found. Full database searching, deduplication, screening and citation chaining remain outstanding.

## 1. Search runs actually performed

Searches used general web-index queries and citation/source-page inspection. Queries were grouped by question; results were reviewed for titles, abstracts, official publisher/registry records and, where available, methods/full text.

| Search batch | Query strings (literal or near-literal) | Purpose |
|---|---|---|
| A — PD + reliability/abstention | `Parkinson voice speech "label-free" performance monitoring out-of-distribution abstention`; `site:pubmed.ncbi.nlm.nih.gov Parkinson voice "out-of-distribution" monitoring`; `Parkinson's disease voice "abstention" "selective prediction" speech`; `Parkinson voice domain adaptation failure detection labeled target data monitoring methods`; `site:arxiv.org Parkinson speech domain shift label-free generalization 2025 2026` | Seek direct PD-speech studies on label-free monitoring, abstention, OOD and domain shift. |
| B — general clinical monitoring methods | `Parkinson speech "label-free performance estimation" OR "post-deployment monitoring" OR D3M`; `"Reliably detecting model failures in deployment without labels" D3M NeurIPS 2025`; `"Label-free estimation of clinically relevant performance metrics under distribution shifts" 2025` | Identify existing general methods for label-free deployment failure detection and estimating clinically relevant metrics. |
| C — current PD cross-corpus work | `"Parkinson's Disease Detection from Speech Signals" "Cross-Corpus Evaluation" 2026`; `"uncertainty-aware" Parkinson voice Spanish Italian 2026 Guo`; `Parkinson speech corpus availability MDVR-KCL ItalianPVS UNLaM PC-GITA` | Find current PD cross-corpus comparisons, uncertainty papers and possible public cohorts. |
| D — additional prior art | `Parkinson speech "label-free" performance monitoring out-of-distribution`; `Parkinson voice domain shift uncertainty cross-corpus 2025 2026`; `site:arxiv.org Parkinson voice domain adaptation fairness 2026`; exact-title searches for D3M, SUDO and the candidate PD papers. | Follow new results into adjacent domain adaptation, fairness and general monitoring methods. |
| E — repository/code checks | GitHub repository search for `Parkinson Voice Detection`, plus direct README/tree inspection of public repositories. | Discover public prior art that may not yet be peer reviewed and inspect whether the same candidate datasets/question are already being used. |

## 2. Findings logged

| Topic | Source record | Why it matters |
|---|---|---|
| LODO PD speech comparison | Şaraldi & Bozdağ Karakeçi (2026-09-30), [DOI 10.46578/humder.1923413](https://doi.org/10.46578/humder.1923413) | Three corpora (PC-GITA, MDVR-KCL, mPower), different architectures and leave-one-dataset-out validation. |
| Cross-dataset target-data adaptation / subgroup FNR | Ganatra (2026), [NHSJS article](https://nhsjs.com/2026/limited-target-data-calibration-improves-cross-dataset-transfer-for-parkinsons-disease-detection-from-speech/) | Tests zero-shot transfer, limited target calibration/adaptation and sex-stratified false-negative rates. |
| Cross-corpus feature stability and calibration | Hossain et al. (2026-10-22), [Scientific Reports](https://www.nature.com/articles/s41598-026-76171-y) | Strong overlap with multilingual/cross-corpus feature evaluation and calibration. |
| Uncertainty-aware Spanish-to-Italian voice assessment | Guo et al. (2026-06-23), [DOI 10.1007/s40846-026-01040-y](https://doi.org/10.1007/s40846-026-01040-y) | Uncertainty and external voice validation already have recent PD-specific precedent. |
| Multilingual/self-supervised PD speech | Siniukov et al. (2025), [arXiv:2501.03581](https://arxiv.org/abs/2501.03581); ParkMAE, [Scientific Reports](https://www.nature.com/articles/s41598-025-30251-7); Lim et al. (2025), [PMC](https://pmc.ncbi.nlm.nih.gov/articles/PMC11909049/) | Cross-language models and adaptation are already established. |
| Fairness-aware domain adaptation | Francesconi et al. (2026), [arXiv:2602.18535](https://arxiv.org/abs/2602.18535) | Cross-cohort voice adaptation and gender-related fairness are active research. |
| Corpus-independent screening/shortcut reduction | Ibarra et al. (2023), [PMC](https://pmc.ncbi.nlm.nih.gov/articles/PMC10669342/) | General corpus- and language-independent PD speech screening and domain adaptation are established. |
| Label-free reliability estimation | SUDO, Kiyasseh et al. (2024), [Nature Communications](https://www.nature.com/articles/s41467-024-46000-9) | Existing clinical-AI reliability method; must be evaluated as relevant comparator. |
| Deployment degradation monitoring | D3M, Nguyen et al. (NeurIPS 2025), [official proceedings](https://proceedings.neurips.cc/paper_files/paper/2025/hash/0bb251eba663f0345c0929f5bbbfb6dc-Abstract-Conference.html) | Existing label-free batch/domain-level monitor. |
| Label-free clinical metric estimation | Flühmann et al. (2025), [arXiv:2507.22776](https://arxiv.org/abs/2507.22776) | Estimates clinically relevant metrics/confusion matrix under shift, not merely AUROC. |
| Selective prediction under shift | Liang, Peng & Sun, [PMC article](https://pmc.ncbi.nlm.nih.gov/articles/PMC12470254/) | Abstention and risk–coverage are standard methods. |
| Demographic confounding | Shukla et al. (2026), [JMIR](https://www.jmir.org/2026/1/e95609) | Age/site confounding needs to be treated directly. |
| Public shortcut-audit repository | [Parkinson-Voice-Detection](https://github.com/BennedictQuanTon/Parkinson-Voice-Detection) | Self-described IPVS silence controls and IPVS/MDVR-KCL cross-corpus audit overlap. Not peer-reviewed and not reproduced. |
| Dataset version control | [NeuroVoz latest v3](https://zenodo.org/records/13647600) vs [v1.0.0](https://zenodo.org/records/10777657) | Latest v3 lists 112 participants (54/58) and 2,977 files, while v1.0.0 lists 108 (53/55) and 2,903 files; both are restricted. |

## 3. Search and screening limitations

- These queries are targeted, not a fully executed search across every planned database.
- No complete export, automated deduplication, double screening, full-text exclusion log, or PRISMA flow diagram has been generated.
- Citation chasing is partial. Every major review and close-overlap paper still needs reference-list and forward-citation screening.
- Some publisher pages are blocked or expose only abstracts; supplements, code and split definitions remain to inspect.
- The public GitHub shortcut-audit repository's metrics are self-reported and have not been independently reproduced.
- Dataset availability is not the same as permission/access. Current official NeuroVoz v3 record marks files Restricted; an institutional or record-owner request may be needed.
- Search results from October 2026 must be date-stamped and checked against publication dates; do not cite a future issue date as already published.

## 4. Next systematic-search workflow

1. Run the frozen query protocol separately in PubMed/MEDLINE, Europe PMC, Scopus, Web of Science, IEEE Xplore, ACM Digital Library and arXiv.
2. Export RIS/BibTeX/CSV with the database name, exact query and run date; preserve every result before deduplication.
3. Deduplicate by DOI, PMID, title and manual match; retain preprints and versions but link them as the same work when appropriate.
4. Screen titles/abstracts, then full texts, against explicit inclusion/exclusion criteria; preserve reasons for full-text exclusion.
5. Search backward references and forward citations for SUDO, D3M, selective classification, label-free performance estimation and each direct PD paper.
6. Extract cohorts, unique participants, task, language, device/site, target-label use, split unit, metrics, uncertainty, subgroup evaluation, code and access status.
7. Update the study matrix before finalizing the protocol. Do not claim systematic-review compliance until those steps are documented.
