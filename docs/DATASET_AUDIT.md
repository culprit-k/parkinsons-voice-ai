# Dataset feasibility audit

**Status:** Candidates identified; no dataset approved for analysis yet.

## Candidate comparison

| Resource | Potential role | Must verify |
|---|---|---|
| Bridge2AI-Voice | Clinical voice and demographic/confounding analysis | Exact version, labels, cohort, site/language coverage, raw/derived access, data-use terms, participant IDs |
| NeuroVoz | Spanish-language Parkinson's voice data | Original paper, data availability, tasks, diagnosis criteria, participant metadata, license |
| Oxford/UCI Parkinson's voice dataset(s) | Possible acoustic-feature baseline | Exact identity/version, source paper, participant IDs, repeated measures, feature definitions, language and recording context |

## Compatibility checklist
- [ ] Canonical title and version
- [ ] Original paper and official source
- [ ] Access date and access conditions
- [ ] License or data-use agreement
- [ ] Unique participants by diagnosis (not only recording count)
- [ ] Diagnostic definition and control eligibility
- [ ] Languages/dialects and language labels
- [ ] Speech tasks and elicitation protocol
- [ ] Age and sex/gender metadata and missingness
- [ ] Site/device/microphone/recording metadata
- [ ] Repeated recordings and participant identifiers
- [ ] Raw audio versus derived features
- [ ] Exclusions and quality limitations
- [ ] Independence of external test set
- [ ] Permitted use of data, code, and aggregate outputs

## Feasibility rule
A cross-language comparison is defensible only when language is documented and outcome labels, participants, tasks, and data provenance are sufficiently understood. If language is confounded with dataset/site or task, describe the finding as cross-dataset generalization rather than attributing it to language alone.

Never commit raw audio, restricted data, or identifying metadata to this repository.
