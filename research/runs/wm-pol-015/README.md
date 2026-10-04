# WM-POL-015 - Jurisdiction research

Status: **validated Claude-only synthesis prepared as a public reviewable
research draft; not a canonical release**.

| Result | Sources | Bundles | Layers | Findings | Questions | Artifacts | Functions |
|---|---:|---:|---:|---:|---:|---:|---:|
| Synthesis | 19 | 6 | 13 | 28 | 113 | 10 | 11 |

The Claude result passed the complete provider schema and semantic validator.
The repository owner explicitly waived Grok for this queue, so no Grok output
was fabricated or inferred. A separate no-tools Claude adversarial audit
challenged the result without adding findings or functions and found no
critical conflict.

The audit confirmed `entity` as the subject-model entry kind. A Jurisdiction
record has identity independent of both its authority-holder and its spatial or
subject-matter scope: it can survive reorganisation, scope change and
succession, and it is retired through an obsolescence marker rather than
re-keyed. The registry-plane `standalone-mm` value remains a separate catalogue
classification. Review must still settle the one-holder-per-competence-scope
cardinality and how prescriptive, adjudicative and enforcement reach may differ
inside one record.

Publication holds cover live source/version verification, the owner-authorized
single-provider waiver, an empty frozen relationship contract, two artifact
identity corrections and overstated coverage claims. Deferred research also
covers State succession, non-territorial regimes, current treaty editions and
arbitral competence. The package therefore remains `reviewable-draft`,
`canonical_publishable` is false, and every public artifact exposes the waiver
and holds.

Published draft:
<https://ver.cy/models/wm-pol-015-jurisdiction/>
