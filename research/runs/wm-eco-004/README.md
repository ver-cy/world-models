# WM-ECO-004 - Money / Instrument research

Status: **validated synthesis published as a public research draft; not yet a
canonical release**.

| Result | Sources | Bundles | Layers | Findings | Questions | Artifacts | Functions |
|---|---:|---:|---:|---:|---:|---:|---:|
| Claude | 21 | 6 | 14 | 26 | 105 | 19 | 10 |
| Grok (normalized) | 10 | 5 | 14 | 16 | 48 | 16 | 8 |
| Synthesis | 29 | 6 | 14 | 28 | 111 | 21 | 10 |

The no-tools adjudication classified Money / Instrument as an `entity`. Its
governed root owns the monetary unit of account, the monetary instrument class
and the reusable monetary-amount value object. Payment execution, named
accounts, holder balances and as-of positions remain in WM-ECO-009,
WM-ECO-015 and WM-ECO-017 respectively.

Claude was retained as the structural base. Two Grok findings were accepted to
add the SDR unit/reserve distinction and retail-versus-wholesale CBDC classes.
Grok's issuer-level outstanding-stock finding and broad-money classification
were rejected because they crossed the frozen position/aggregate boundary. A
manual synthesis plan also deferred the FATF virtual-asset finding and its
admission function because importing them verbatim would contradict the base
classification of currency-referencing tokens. Grok service-layer merging was
disabled because it reintroduced issuer operational stock. Sixteen decisions
were recorded and no critical conflict remains; seven topics remain deferred.

Both valid provider runs used the same frozen contract and clean input commit
`dc9f3202e403556f33e9cbff853ff76b55a5f596`. Grok returned substantive content
in a non-canonical schema. A no-tools pass normalized only the transport shape,
source identifiers and required contract fields; it made no semantic repair.
Both provider results and the final synthesis pass schema and semantic
validation.

Live source/version verification, ISO 4217 amendment reconciliation,
multi-profile legal validation, primary-source assessment for the accepted SDR
and CBDC additions, and explicit publication of the known coverage limits
remain publication holds. See `synthesis-plan.manual.json`,
`synthesis-plan.json`, `adjudication.json`, `comparison.json` and
`synthesis.validation.json`.

Published draft:
<https://ver.cy/models/wm-eco-004-money-instrument/>
