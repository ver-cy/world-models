# WM-ACT-042 - Incident Response research

Status: **validated Claude-only synthesis prepared as a public reviewable
research draft; not a canonical release**.

| Result | Sources | Bundles | Layers | Findings | Questions | Artifacts | Functions |
|---|---:|---:|---:|---:|---:|---:|---:|
| Claude | 17 | 7 | 15 | 26 | 108 | 18 | 17 |
| Synthesis | 17 | 7 | 15 | 26 | 108 | 18 | 17 |

The repository owner explicitly waived Grok for this run. No Grok output was
fabricated or inferred. A separate no-tools Claude adversarial audit challenged
the validated result against its frozen registry record and relationship
contract. The audit could reject or defer claims but could not add facts,
findings or functions.

The audit reclassified the research-plane root as an `aggregate` response case,
not the incident itself. The case owns response identity, state, decisions,
actions, communications and closure evidence, while the incident, crisis,
forensic evidence, notification obligations and follow-up work remain referenced
or externally owned. No critical conflict was found.

Open holds include the unresolved COMPOSE-versus-REFERENCE edge to the incident,
missing producing functions for six artifacts, access and tombstone coverage
overclaims, source/version verification, artifact serial semantics and the
explicit single-provider waiver. The result therefore remains
`reviewable-draft`, `publishable` is false, and every public artifact exposes the
waiver and holds. See `provider-policy.json`, `comparison.json`,
`synthesis-plan.json`, `adjudication.json`, `source-verification.csv` and
`synthesis.validation.json`.

Published draft:
<https://ver.cy/models/wm-act-042-incident-response/>
