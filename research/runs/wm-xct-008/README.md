# WM-XCT-008 - Quantity / Unit research

Status: **validated synthesis published as a public research draft; not yet a
canonical release**.

| Result | Sources | Bundles | Layers | Findings | Questions | Artifacts | Functions |
|---|---:|---:|---:|---:|---:|---:|---:|
| Claude | 16 | 7 | 16 | 26 | 95 | 13 | 11 |
| Grok (normalized) | 11 | 7 | 19 | 30 | 103 | 16 | 8 |
| Synthesis | 22 | 7 | 16 | 29 | 105 | 15 | 14 |

Both providers independently classify Quantity / Unit as a reusable `mixin` and
embedded value object. It owns quantity value forms, kind/dimension, unit
identity, scale, conversion, uncertainty/tolerance and minimum provenance, but
does not own the observing event, calendar semantics, money, calibration-chain
records, external unit registries or domain property catalogues.

The no-tools adjudication retained Claude's tighter boundary and accepted
Grok's independently grounded system-of-quantities frame, quantity calculus,
coherent-factor accounting and a narrowed metrological-traceability claim. It
also added the missing operation to freeze an original value before conversion.

Grok's substantive answer had malformed JSON transport. The immutable raw
wrapper remains outside Git; a no-tools Claude pass repaired syntax/schema only,
and the normalized result passes both schema and semantic validation.

No critical structural conflicts remain. Live source/version checks, FHIR/QUDT
release reconciliation, multi-profile tests, inherited ownership/access/
retention policy, paywalled ISO clauses, current UCUM prefixes and eventual
VIM4 changes remain explicit publication holds. See `synthesis-plan.json`,
`adjudication.json`, `comparison.json` and `synthesis.validation.json`.

Published draft:
<https://ver.cy/models/wm-xct-008-quantity-unit/>
