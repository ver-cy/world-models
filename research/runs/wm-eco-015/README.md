# WM-ECO-015 - Financial Account research

Status: **validated Claude-only synthesis prepared as a public reviewable
research draft; not a canonical release**.

| Result | Sources | Bundles | Layers | Findings | Questions | Artifacts | Functions |
|---|---:|---:|---:|---:|---:|---:|---:|
| Claude | 14 | 6 | 14 | 26 | 102 | 16 | 11 |
| Synthesis | 14 | 6 | 14 | 26 | 102 | 16 | 11 |

The repository owner explicitly waived Grok for this run. No Grok output was
fabricated or inferred. A separate no-tools Claude adversarial audit challenged
the validated result against its frozen registry record and relationship
contract. The audit could reject or defer claims but could not add facts,
findings or functions.

The audit accepted Financial Account as an `entity`: the identified account
container retains its identity while holders, classifications and lifecycle
states change. The holder-institution arrangement, account groups and pooling,
posting semantics, monetary-unit semantics, payment instructions and product
catalogue remain outside the aggregate root or are deferred to neighbouring
models. No critical conflict was found.

Open holds include live verification and immutable version pins for all 14
sources, regulatory currency, unread ISO 20022 and ISO 13616 normative text,
unverified AML thresholds and retention periods, partial rather than complete
security/privacy/access/retention/interoperability coverage, unregistered
neighbour relations, artifact seriality and function gaps, plus the explicit
single-provider waiver. The result therefore remains `reviewable-draft`,
`publishable` is false, and every public artifact exposes the waiver and holds.
See `provider-policy.json`, `comparison.json`, `synthesis-plan.json`,
`adjudication.json`, `source-verification.csv` and
`synthesis.validation.json`.

Published draft:
<https://ver.cy/models/wm-eco-015-financial-account/>
