# WM-ACT-014 - Health Care Delivery research

Status: **validated dual-provider synthesis prepared and distributed as a published public research draft; not a canonical release**.

| Result | Sources | Bundles | Layers | Findings | Questions | Artifacts | Functions |
| --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| Claude | 18 | 6 | 16 | 27 | 95 | 17 | 16 |
| Grok | 17 | 4 | 12 | 18 | 59 | 19 | 14 |
| Synthesis | 34 | 6 | 16 | 28 | 98 | 19 | 18 |

Claude and Grok independently researched the frozen registry boundary. The Grok wrapper required transport-only normalization; the normalized result passed the same schema and semantic validator without adding new research facts. A separate no-tools Claude adversarial adjudication compared the validated results.

Both providers classified the research-plane subject as an `aggregate`. The adjudicator selected Claude as base, accepted one Grok finding and two Grok functions, recorded nineteen explicit decisions and found no critical conflict. The synthesis preserves `WM-ACT-018` as the owner of encounter lifecycle and detailed event semantics.

Nine publication holds remain, including live source and version verification, multi-profile testing, FHIR release pinning, confirmation of candidate relations, legacy-card supersession and waiting-clock rule validation. The result therefore remains `reviewable-draft` and `publishable` is false, while its distribution lifecycle is `published`.

The evidence chain is in `claude.result.json`, `grok.result.json`, `comparison.json`, `synthesis-plan.json`, `adjudication.json`, `source-verification.csv` and `synthesis.validation.json`. The generated public package is `publications/wm-act-014-health-care-delivery/`.
