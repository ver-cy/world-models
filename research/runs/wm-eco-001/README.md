# WM-ECO-001 - Market / Exchange research

Status: **validated dual-provider synthesis prepared and distributed as a published public research draft; not a canonical release**.

| Result | Sources | Bundles | Layers | Findings | Questions | Artifacts | Functions |
| --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| Claude | 15 | 6 | 12 | 26 | 99 | 23 | 11 |
| Grok | 10 | 6 | 8 | 12 | 48 | 8 | 11 |
| Synthesis | 23 | 6 | 12 | 28 | 106 | 23 | 12 |

Claude and Grok independently researched the frozen registry boundary. The Grok wrapper required transport-only normalization and one validator-label repair that prefixed its existing ISO 10383 MIC value with the required authoritative master-system identifier label. No factual content was added or removed. Both normalized provider results passed the same schema and semantic validator.

The providers disagreed on research-plane kind: Claude proposed `aggregate` and Grok proposed `entity`. A separate no-tools Claude adversarial adjudication accepted `aggregate`, selected Claude as base, accepted two Grok findings and one Grok function, recorded eighteen explicit decisions and found no critical conflict.

Eight publication holds and eight deferred research items remain. The result therefore remains `reviewable-draft` and `publishable` is false, while its distribution lifecycle is `published`.

The evidence chain is in `claude.result.json`, `grok.result.json`, `comparison.json`, `synthesis-plan.json`, `adjudication.json`, `source-verification.csv` and `synthesis.validation.json`. The generated public package is `publications/wm-eco-001-market-exchange/`.
