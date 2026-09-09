# WM-DAT-006 - Data Lineage research

Status: **validated Claude-only synthesis prepared as a public reviewable
research draft; not a canonical release**.

| Result | Sources | Bundles | Layers | Findings | Questions | Artifacts | Functions |
|---|---:|---:|---:|---:|---:|---:|---:|
| Claude | 15 | 7 | 14 | 28 | 109 | 12 | 9 |
| Synthesis | 15 | 7 | 14 | 28 | 109 | 12 | 9 |

The repository owner explicitly waived Grok for this run. No Grok output was
fabricated or inferred. A separate no-tools Claude adversarial audit challenged
the validated result against its frozen registry record and relationship
contract. The audit could reject or defer claims but could not add facts,
findings or functions.

The audit accepted Data Lineage as a `pattern` whose principal consistency unit
is a lineage assertion over externally owned data, process and agent identities.
Dataset and pipeline parents compose the pattern as candidate boundaries, while
the graph store, access enforcement, audit log and physical data lifecycle stay
outside it. No critical conflict was found.

Open holds include live source/version verification, candidate COMPOSE edges,
the unreconciled WM-XCT-012 parent, unregistered governance neighbours,
unsupported checklist policy surfaces, artifact seriality and missing producing
functions, plus the explicit single-provider waiver. The result therefore
remains `reviewable-draft`, `publishable` is false, and every public artifact
exposes the waiver and holds. See `provider-policy.json`, `comparison.json`,
`synthesis-plan.json`, `adjudication.json`, `source-verification.csv` and
`synthesis.validation.json`.

Published draft:
<https://ver.cy/models/wm-dat-006-data-lineage/>
