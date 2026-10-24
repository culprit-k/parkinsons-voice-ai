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
