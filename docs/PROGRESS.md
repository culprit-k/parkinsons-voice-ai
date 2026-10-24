# Research progress ledger

Last updated: 2026-10-25

## Status summary

| Workstream | Status | Next action |
|---|---|---|
| Topic selection | Complete | Voice-based Parkinson's research selected |
| Broad objective | Complete | Cross-language generalization, demographic bias, robustness |
| Preliminary literature discovery | In progress | Expand targeted search into a reproducible multi-database search |
| Structured literature review | Not complete | Record exact searches, deduplicate, screen, and extract all eligible studies |
| Dataset audit | Preliminary audit complete | Verify current access terms, licenses, participant IDs, labels, and metadata for candidate releases |
| Research protocol | Provisional hypothesis only | Finalize after prior-art and dataset feasibility gates |
| Code and environment | Not started | Implement only after protocol/data gates |
| Experiments | Not started | No model results currently available |
| Manuscript | Not started | Draft after review; results only after real experiments |

## Decisions
1. Cross-language modeling, cross-corpus feature stability, demographic-only baselines, target-data adaptation, participant-level splitting, uncertainty quantification and probability calibration all have prior art; none alone is our novelty claim.
2. The candidate Route A idea overlaps conceptually with SUDO (label-free evaluation/identification of unreliable predictions) and general selective classification/OOD risk control.
3. Any defensible contribution should be framed as a rigorous PD-voice comparative benchmark of unlabeled-target warning signals versus observed external failure, not as a new general method, unless further prior-art search supports a narrower claim.
4. Include demographic-only baselines and confounding checks where metadata permit.
5. Prefer independent external evaluation where compatible datasets permit.
6. Use participant-level splitting to prevent leakage where IDs permit.
7. Report uncertainty and limitations; do not overstate clinical readiness.

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
- 2026-10-25: Added preliminary Route A hypothesis and data-access cautions.
- 2026-10-25: Added a targeted prior-art audit. Found substantial conceptual overlap with SUDO and general selective/OOD methods; the proposed PD-voice benchmark remains a conditional hypothesis, not a cleared novelty claim. No experiments performed.
