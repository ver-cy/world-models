# WM-ECO-009 - Payment research

Status: **validated synthesis published as a public research draft; not yet a
canonical release**.

| Result | Sources | Bundles | Layers | Findings | Questions | Artifacts | Functions |
|---|---:|---:|---:|---:|---:|---:|---:|
| Claude | 15 | 6 | 13 | 27 | 100 | 25 | 11 |
| Grok (normalized) | 11 | 6 | 12 | 21 | 63 | 31 | 10 |
| Synthesis | 26 | 6 | 13 | 35 | 124 | 37 | 14 |

The no-tools adjudication classified Payment as an `aggregate`. Its ordered
lifecycle events, per-leg states and separately retained dependent records
cannot be governed as one event. Grok's event framing is retained as the
lifecycle-event-history projection rather than the model entry kind.

Claude was retained as the structural base. Accepted Grok additions cover
travel-rule payloads, mandate and request-to-pay authority, PvP/DvP linkage,
proxy addressing, verification of payee, instrument and initiation direction,
payment-order grain, and instant execution clocks. Sixteen decisions were
recorded and no critical conflict remains. Currency/instrument, invoice,
accounting postings and party identity remain sibling references; the missing
Account/Holding registry boundary is explicitly deferred.

Both provider runs used the same frozen contract and clean input commit
`7bb5ac25829b2d2539095d230c004f342a0eb27e`. Grok returned its substantive
answer in an alternate provider envelope; the raw wrapper remains outside Git.
A no-tools pass normalized only the transport shape, made no semantic repairs,
and renamed two cross-grain duplicate identifiers. Both provider results and
the synthesis pass schema and semantic validation.

Live source verification and deduplication, authority-tier reconciliation,
primary-text rechecks, multi-profile validation and regime-scoped publication
of every threshold and clock remain publication holds. See
`synthesis-plan.json`, `adjudication.json`, `comparison.json` and
`synthesis.validation.json`.

Published draft:
<https://ver.cy/models/wm-eco-009-payment/>
