# WM-XCT-025 - Observable Result Fields research

Status: **validated Claude-only synthesis prepared as a public reviewable
research draft; not a canonical release**.

| Result | Sources | Bundles | Layers | Findings | Questions | Artifacts | Functions |
|---|---:|---:|---:|---:|---:|---:|---:|
| Synthesis | 13 | 7 | 16 | 25 | 100 | 3 | 10 |

The Claude result passed the complete provider schema and semantic validator.
The repository owner explicitly waived Grok for this queue, so no Grok output
was fabricated or inferred. A separate no-tools Claude adversarial audit
challenged the result without adding findings or functions and found no
critical conflict.

The audit confirmed `mixin` as the subject-model entry kind. WM-XCT-025 owns a
format-neutral result field group for values, units, quantities, methods,
uncertainty, quality and result-time semantics. The host observation record,
including its subject and lifecycle, remains owned by WM-MAT-008 or another
adopting host. Every create, supersede, withdraw, retain or delete rule is
therefore a host-scoped obligation rather than an independent aggregate
lifecycle.

Publication holds cover the owner-authorized single-provider waiver, live
verification of thirteen sources, an empty relationship contract, unresolved
field-group identity/version semantics and the frozen candidate registry state.
The package therefore remains `reviewable-draft`, `canonical_publishable` is
false, and every public artifact exposes the waiver and holds.

Published draft:
<https://ver.cy/models/wm-xct-025-observable-result-fields/>
