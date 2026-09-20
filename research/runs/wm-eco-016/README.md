# WM-ECO-016 - Financial Transaction / Journal Entry research

Status: **validated synthesis published as a public research draft; not yet a
canonical release**.

| Result | Sources | Bundles | Layers | Findings | Questions | Artifacts | Functions |
|---|---:|---:|---:|---:|---:|---:|---:|
| Claude | 14 | 6 | 13 | 26 | 95 | 19 | 12 |
| Grok (normalized) | 13 | 7 | 13 | 19 | 64 | 20 | 8 |
| Synthesis | 24 | 6 | 13 | 28 | 102 | 21 | 15 |

The no-tools adjudication classified the journal entry as an `aggregate`.
Its defining invariant binds one header to two or more posting lines whose
debits and credits balance within a declared scope; this cannot be enforced on
one flat event record. Grok's event framing is retained as explicit document,
effective, posting, value, booking, capture and ingestion time roles rather
than as the model entry kind.

Claude was retained as the structural base. Accepted Grok additions cover
top-side and consolidating adjustments, management-override control evidence,
and a closed-period exception function. Sixteen decisions were recorded and
no critical conflict remains. Accounts, ledger profiles, balances, payments,
source business documents, reporting statements and audit fieldwork remain
sibling concerns or referenced context rather than being absorbed into the
journal-entry aggregate.

Both provider runs used the same frozen contract and clean input commit
`cf097890bb68e098cee017d047d05865f9eeb756`. Grok returned its substantive
answer in an alternate provider envelope; the raw wrapper remains outside Git.
A no-tools pass normalized only the transport shape, made no semantic repairs
and required no cross-grain identifier repairs. Both provider results and the
synthesis pass schema and semantic validation.

Live source and version verification, multi-profile validation, a primary
privacy-law basis, alignment-only wording, publication of the entry-kind
rationale and jurisdiction-specific retention declarations remain publication
holds. See `synthesis-plan.json`, `adjudication.json`, `comparison.json` and
`synthesis.validation.json`.

Published draft:
<https://ver.cy/models/wm-eco-016-financial-transaction-journal-entry/>
