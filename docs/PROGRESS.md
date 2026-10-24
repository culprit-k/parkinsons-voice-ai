# Research progress ledger

Last updated: 2026-10-25

## Status summary

| Workstream | Status | Next action |
|---|---|---|
| Topic selection | Complete | Voice-based Parkinson's research selected |
| Broad objective | Complete | Cross-language generalization, demographic bias, robustness |
| Preliminary literature discovery | Started | Verify original publications and methods |
| Structured literature review | Not complete | Record exact searches, screening, and extraction |
| Dataset audit | Not complete | Verify sources, access, license, labels, languages, metadata, participant overlap |
| Research protocol | Not complete | Prespecify endpoints, splits, baselines, metrics, subgroup analyses |
| Code and environment | Not started | Implement after protocol and dataset decisions |
| Experiments | Not started | No model results currently available |
| Manuscript | Not started | Draft after review; results only after real experiments |

## Decisions
1. Cross-language generalization is an established research area, not automatically a novel contribution.
2. Include demographic-only baselines and confounding checks where metadata permit.
3. Prefer independent external evaluation where compatible datasets permit.
4. Use participant-level splitting to prevent leakage where IDs permit.
5. Report uncertainty and limitations; do not overstate clinical readiness.

## Candidate resources (not approved yet)
- Bridge2AI-Voice: verify exact release, variables, data-use requirements, raw versus derived access.
- NeuroVoz: verify original paper, availability, protocol, and metadata.
- Oxford/UCI Parkinson's voice datasets: identify exact version and verify participant IDs, repeated-measure structure, language and recording context.

Do not assume these resources are mutually compatible. Do not claim cross-language evidence unless language and collection details are documented.

## Next actions
- [ ] Build literature search log and screening table.
- [ ] Verify bibliographic records from original publisher/repository pages.
- [ ] Create dataset compatibility matrix.
- [ ] Decide feasibility with available public data and metadata.
- [ ] Version the protocol before confirmatory model training.

## Change log
- 2026-10-25: Initialized from project conversation. No experiments or manuscript results claimed.


## 2026-10-25 — Deep literature and dataset access audit

- Added docs/DEEP_CRITICAL_APPRAISAL.md: methods-level critical appraisal of Lim, ParkMAE, Hossain et al. (2026), Ahammad (2026), Ganatra (2026), Shukla (2026), Adnan et al. (2025), and the recent leakage/transfer reproducibility report; includes reporting standards and limits of novelty claims.
- Added docs/DATA_ACCESS_AUDIT.md: documentary feasibility audit for EWA-DB, ItalianPVS, MDVR-KCL, NeuroVoz, PC-GITA, ParkCeleb, PVA, UCI feature datasets, Oxford, PARK derived features, Bridge2AI v4 and mPower.
- Core update: cross-language modeling, cross-corpus feature stability, basic demographic baselines, target-data adaptation, participant-grouped splitting, cross-dataset transfer and Brier-score analysis have direct precedent. Do not claim any of these alone as novel.
- Important current update: Bridge2AI-Voice v4.0.0 was released on 2026-10-19; 1,370 participants, 48,226 recordings and 23 people with Spanish protocol recordings. Its PhysioNet release provides derived features, not raw audio; raw audio has a separate institutional sign-off process. Spanish protocol recordings do not prove a sufficiently sized Spanish PD/control comparison.
- Major feasibility risk: EWA-DB and NeuroVoz require requests/licenses; PC-GITA, ParkCeleb and Bridge2AI data involve additional access constraints. MDVR-KCL and ItalianPVS are lower-friction candidates but small.
- Methodology checkpoint: independent unit is the participant, not file/window/feature row. The protocol must document every split stage and use participant-clustered uncertainty. Language effects cannot be isolated where language is fully confounded with site, task, device or recruitment.
- Research question remains provisional. No model has been trained and no new experimental performance results exist.


## 2026-10-25 — Search protocol and primary-study matrix

- Added docs/SEARCH_AND_SCREENING_FRAMEWORK.md with proposed databases, search strings, inclusion/exclusion criteria, screening stages, extraction fields, and risk-of-bias/synthesis plan. These are planned methods; the full search and screening have not yet been executed.
- Added docs/PRIMARY_STUDY_COMPARISON_MATRIX.md with a first-pass comparison of the closest direct-overlap studies and supporting reviews.
- Current decision: no final novelty claim. Cross-language model evaluation, cross-corpus feature stability, participant-level splitting, demographic-only baselines, target-data adaptation, and Brier-score evaluation have prior art. Any future empirical contribution must specify its additional analysis and be justified against the completed matrix.
- Dataset feasibility remains the key gate. Need verify licenses, participant identifiers, labels, languages/tasks, and available features in the exact release before approving datasets.


## 2026-10-25 — Route A candidate defined

- Added docs/ROUTE_A_LABEL_FREE_RELIABILITY_PROPOSAL.md.
- Candidate question: can unlabeled-target shift indicators predict external failure of a source-trained PD voice model, and can a source-validation-selected abstention policy reduce error among predictions retained for automated output?
- This is a hypothesis-generation document only. A targeted search found related general medical label-free evaluation/selective classification methods and PD-specific uncertainty work; novelty is not established.
- Hold model training until the broader prior-art search, exact dataset-access checks, and participant-level data integrity pilot are complete.
- The plan explicitly allows a null result and requires reporting coverage and subgroup deferral so abstention cannot hide unequal performance.
