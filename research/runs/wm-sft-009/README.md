# WM-SFT-009 - Deployment research

Status: **validated Claude-only synthesis prepared as a public reviewable
research draft; not a canonical release**.

| Result | Sources | Bundles | Layers | Findings | Questions | Artifacts | Functions |
|---|---:|---:|---:|---:|---:|---:|---:|
| Synthesis | 13 | 6 | 12 | 24 | 92 | 8 | 9 |

The Claude result passed the complete provider schema and semantic validator.
The repository owner explicitly waived Grok for this queue, so no Grok output
was fabricated or inferred. A separate no-tools Claude adversarial audit
challenged the result without adding findings or functions and found no
critical conflict.

The audit confirmed `aggregate` as the subject-model entry kind. A deployment
record has its own identity across repeated deployment attempts and owns an
append-only history, plan, completion report and verification index under one
consistency boundary. A rollout operation is an event inside that history;
Deployment itself is not reduced to the Release-to-Environment relationship.
The frozen candidate REFERENCE links to WM-SFT-008 Release and WM-SFT-010
Runtime Environment remain explicit registry-plane relations.

Publication holds cover live source pins, the owner-authorized
single-provider waiver, unregistered CHILD/EXTEND assertions, type-scoped
artifacts and foreign-key-derived history identity, plus partial lifecycle,
relationship and jurisdictional coverage. Target withdrawal, field-level
redaction, database migrations, OTA fleets and five missing governance
functions remain deferred. The package therefore stays `reviewable-draft`,
`canonical_publishable` is false, and every public artifact exposes the waiver
and holds.

Published draft:
<https://ver.cy/models/wm-sft-009-deployment/>
