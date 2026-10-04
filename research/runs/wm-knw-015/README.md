# WM-KNW-015 - Risk / Opportunity research

Status: **validated Claude-only synthesis prepared as a public reviewable
research draft; not a canonical release**.

| Sources | Bundles | Layers | Findings | Questions | Artifacts | Functions |
|---:|---:|---:|---:|---:|---:|---:|
| 14 | 6 | 13 | 26 | 106 | 12 | 12 |

Claude completed one full web-enabled research pass and the local schema and
semantic validator accepted it. The repository owner explicitly waived Grok
for this queue; no Grok output was fabricated or inferred. A separate no-tools
Claude adversarial audit inspected the compact result without adding facts,
findings or functions. It accepted `entity` as the subject-model entry kind,
kept registry `standalone-mm` as a separate record-plane classification and
reported no critical conflicts.

The structure models a persistent risk or opportunity item independently of
its changing assessments and register membership. It covers identity and
valence, definition scheme, context and objectives, uncertain event or effect,
causes and consequences, likelihood and impact, assessment method and scale,
inherent/current/residual/target views, appetite and tolerance, controls and
treatment links, ownership and acceptance, review, lifecycle, realisation,
aggregation, reporting, provenance, access and retention. Materialised events,
control execution, treatment actions and decisions remain referenced
neighbours.

Open holds include the single-provider waiver, live verification and version
pinning of all 14 sources, cited-but-unretrieved ISO and Basel texts, an
unsupported composition-coverage claim and dangling checklist reference,
registry defects around the two entry-kind axes and adverse-only purpose text,
and the unratified WM-ACT-017 parent. The draft also records thin protection-
plane question coverage and the open question whether Risk Register deserves a
separate registry-kind sibling. It therefore remains `reviewable-draft`,
`publishable` is false, and every public artifact exposes the waiver and holds.
See `comparison.json`, `synthesis-plan.json`, `adjudication.json`,
`source-verification.csv` and `synthesis.validation.json`.

Published draft:
<https://ver.cy/models/wm-knw-015-risk-opportunity/>
