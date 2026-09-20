# WM-ECO-020 - Sales Order research

Status: **validated Claude-only synthesis prepared as a public reviewable
research draft; not a canonical release**.

| Result | Sources | Bundles | Layers | Findings | Questions | Artifacts | Functions |
|---|---:|---:|---:|---:|---:|---:|---:|
| Claude | 12 | 6 | 13 | 24 | 100 | 14 | 8 |
| Synthesis | 12 | 6 | 13 | 24 | 100 | 14 | 8 |

The repository owner explicitly waived Grok for this run. No Grok output was
fabricated or inferred. A separate no-tools Claude adversarial audit challenged
the validated result against its frozen registry record and relationship
contract. The audit could reject or defer claims but could not add facts,
findings or functions.

The audit reclassified Sales Order as an `aggregate`: the seller-scoped order
identifier and header form the consistency root, while lines and all emitted
artifacts have no independent lifecycle outside that root. Invoice, despatch and
transport, payment and credit, inventory availability and allocation, returns,
party and trade-item masters remain neighbouring responsibilities. No critical
conflict was found.

Open holds include live verification of all 12 sources, re-tiering three
overview or portal sources, restating unsupported access/ownership/retention
coverage, registering the currently empty relationship contract, reconciling
registry `standalone-mm` with subject-model `aggregate`, grounding
consumer-protection duties in primary legislation, artifact cardinality and
function gaps, plus the explicit single-provider waiver. The result therefore
remains `reviewable-draft`, `publishable` is false, and every public artifact
exposes the waiver and holds. See `provider-policy.json`, `comparison.json`,
`synthesis-plan.json`, `adjudication.json`, `source-verification.csv` and
`synthesis.validation.json`.

Published draft:
<https://ver.cy/models/wm-eco-020-sales-order/>
