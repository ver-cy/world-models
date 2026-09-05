# WM-ECO-008 - Invoice / Commercial Document research

Status: **validated synthesis published as a public research draft; not yet a
canonical release**.

| Result | Sources | Bundles | Layers | Findings | Questions | Artifacts | Functions |
|---|---:|---:|---:|---:|---:|---:|---:|
| Claude | 14 | 6 | 15 | 27 | 110 | 29 | 12 |
| Grok (normalized) | 8 | 6 | 11 | 15 | 48 | 16 | 8 |
| Synthesis | 22 | 6 | 15 | 28 | 113 | 30 | 14 |

The no-tools adjudication classified the invoice family as an `aggregate`:
lines, allowances, tax breakdown groups and totals have no independent identity
outside the document. Invoice, credit note, debit note, self-billed and
corrective variants share one commercial consistency boundary while generic
recordkeeping remains delegated to the N1 Document & Record model.

Claude was retained as the structural base. Grok's self-billing, prepayment and
special-billing-process finding was accepted. Customs valuation invoices were
kept out as a different legal act requiring a sibling trade-document model.
Thirteen decisions were recorded and no critical conflict remains.

Both provider runs used the same frozen contract and clean input commit
`89acbf9640784d76ad204209b6290ada1143326a`. The first Claude attempt timed out
without a result; a clean retry completed under the same research settings with
only a larger runtime window. Grok returned an alternate provider envelope; a
no-tools pass normalized only its transport shape, used no tools, made no
semantic repairs and required no identifier repair. Raw wrappers remain outside
Git.

Source/version verification, EU-law re-grounding, EN 16931 conformance limits,
UN/CEFACT BRS currency, non-EU profile validation and registry parent/alias
reconciliation remain publication holds. The authoritative published identity
is `vr.wm-eco-008`; Grok's local alternate identifier is not propagated. See
`synthesis-plan.json`, `adjudication.json`, `comparison.json` and
`synthesis.validation.json`.

Published draft:
<https://ver.cy/models/wm-eco-008-invoice-commercial-document/>
