# WM-ECO-019 - Purchase Order research

Status: **validated synthesis published as a public research draft; not yet a
canonical release**.

| Result | Sources | Bundles | Layers | Findings | Questions | Artifacts | Functions |
|---|---:|---:|---:|---:|---:|---:|---:|
| Claude | 11 | 6 | 14 | 24 | 92 | 15 | 13 |
| Grok (normalized) | 8 | 6 | 12 | 16 | 57 | 13 | 7 |
| Synthesis | 16 | 6 | 14 | 27 | 102 | 18 | 15 |

Both providers independently classified the model as an `aggregate`. The order
header is the aggregate root and order lines have no independent identity,
version or retention life. The boundary is the exchanged buyer-to-seller
commitment: quotations, framework clauses, fulfilment events, invoices,
payments and accounting entries remain sibling references.

The no-tools adjudication retained Claude as the structural base and accepted
Grok additions for the offer-expiry validity window, consignment and
vendor-managed-inventory patterns, signature and integrity evidence,
anticipated-total calculation and contract conclusion. It also records the
UN/EDIFACT trap: document-name code 105 is an internal requisition sense, while
this model describes the exchanged order commitment, typically code 220.
Fifteen decisions were recorded and no critical conflict remains.

Both provider runs used the same frozen contract and clean input commit
`7b75022aa8270b5e39b0f482c3fea071dc887134`. Grok returned its substantive
answer in an alternate provider envelope; the raw wrapper remains outside Git.
A no-tools pass normalized only the transport shape, used no tools, made no
semantic repairs and required no identifier repair. Both provider results and
the synthesis pass schema and semantic validation.

Live source and version-pin verification, Peppol release and authority-tier
reconciliation, broader profile validation, jurisdiction-neutral retention and
tax-representation limits remain publication holds. See
`synthesis-plan.json`, `adjudication.json`, `comparison.json` and
`synthesis.validation.json`.

Published draft:
<https://ver.cy/models/wm-eco-019-purchase-order/>
