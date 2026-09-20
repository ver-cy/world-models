# WM-KNW-010 - Decision / Rationale research

Status: **validated Claude-only synthesis prepared as a public reviewable
research draft; not a canonical release**.

| Result | Sources | Bundles | Layers | Findings | Questions | Artifacts | Functions |
|---|---:|---:|---:|---:|---:|---:|---:|
| Core pass | 12 | 3 | 6 | 13 | 59 | 3 | 5 |
| Reasoning pass | 12 | 3 | 6 | 13 | 60 | 7 | 5 |
| Governance pass | 12 | 3 | 6 | 13 | 56 | 4 | 11 |
| Synthesis | 33 | 9 | 18 | 39 | 175 | 14 | 21 |

Two monolithic Claude attempts ended with the same API/network error without
producing a result. The bounded workflow therefore used three non-overlapping
passes: `core` owns problem framing, alternatives, criteria, evaluation and
outcome; `reasoning` owns reasons, evidence bindings, assumptions, uncertainty,
argumentation, dissent and explanations; and `governance` owns authority,
participation, lifecycle and all canonical service rules. Each pass passed the
complete provider schema and semantic validator. The deterministic merger
remapped source identifiers, rejected duplicate IDs and questions, routed the
coverage checklist to explicit owners and produced a separately validated
synthesis.

The repository owner explicitly waived Grok for this queue. No Grok output was
fabricated or inferred. A separate no-tools Claude adversarial audit challenged
the merged result without adding findings or functions. It confirmed
`aggregate` as the subject-model entry kind, kept registry `standalone-mm` as a
separate record-plane classification and found no critical conflict.

Open holds include live verification and version pinning of all 33 sources,
the single-provider waiver, a historical-only label for the superseded 2024
40 CFR pattern, reconciliation of four neighbour references with the frozen
relation ledger, and a complete discriminator registry plus one sequence scope
for every serial artefact. The model also records unresolved gaps around
counterfactual rationale, reason-weight aggregation and conflict-of-interest
structure. It therefore remains `reviewable-draft`, `publishable` is false,
and every public artifact exposes the waiver and holds. See `split-plan.md`,
`coverage-plan.json`, `comparison.json`, `synthesis-plan.json`,
`adjudication.json`, `source-verification.csv` and
`synthesis.validation.json`.

Published draft:
<https://ver.cy/models/wm-knw-010-decision-rationale/>
