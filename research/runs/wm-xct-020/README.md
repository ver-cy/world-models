# WM-XCT-020 - Classification Binding research

Status: **validated synthesis published as a public research draft; not yet a
canonical release**.

| Result | Sources | Bundles | Layers | Findings | Questions | Artifacts | Functions |
|---|---:|---:|---:|---:|---:|---:|---:|
| Claude | 16 | 6 | 14 | 27 | 92 | 14 | 13 |
| Grok (normalized) | 8 | 6 | 12 | 15 | 63 | 9 | 8 |
| Synthesis | 23 | 6 | 14 | 32 | 112 | 17 | 16 |

Both providers independently reclassify Classification Binding as a reusable
`pattern`. The pattern owns the reified assertion that binds a subject to a
scheme term and the design-time slot constraint that governs which terms may
fill it. Scheme-internal structure, value-set composition and cross-scheme
mapping remain sibling responsibilities.

The no-tools adjudication retained Claude's explicit split between design-time
Binding Specification and instance-time Binding Assertion. It accepted Grok's
additional distinctions for value set versus code system, multilingual lexical
forms, classification facet, scheme jurisdiction/custodianship and parallel
codings that translate one concept.

Grok's substantive answer had a malformed JSON transport. The immutable raw
wrapper remains outside Git; a no-tools Claude pass repaired syntax/schema only,
and the normalized result passes both schema and semantic validation.

No critical structural conflicts remain. Clause-level ISO evidence, live source
pinning, additional domain profiles, missing sibling registry entries, XKOS URL
verification and confidence/calibration semantics remain explicit publication
holds. See `synthesis-plan.json`, `adjudication.json`, `comparison.json` and
`synthesis.validation.json` for the evidence trail.

Published draft:
<https://ver.cy/models/wm-xct-020-classification-binding/>
