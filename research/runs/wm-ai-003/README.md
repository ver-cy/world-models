# WM-AI-003 - AI Model Evaluation research

Status: **validated synthesis published as a public research draft; not yet a
canonical release**.

| Result | Sources | Bundles | Layers | Findings | Questions | Artifacts | Functions |
|---|---:|---:|---:|---:|---:|---:|---:|
| Claude | 15 | 5 | 13 | 26 | 104 | 28 | 14 |
| Grok (normalized) | 10 | 5 | 9 | 14 | 57 | 14 | 9 |
| Synthesis | 25 | 5 | 13 | 28 | 112 | 30 | 16 |

The no-tools adjudication classified AI Model Evaluation as an `aggregate`.
The governed root is one bounded evaluation instance for a specific AI model or
system version. Evaluation campaigns group such instances but do not replace
their identity. The model artifact, benchmark dataset, individual inference
run, AI management system, risk record and conformity assessment remain sibling
records.

Claude was retained as the structural base. Two Grok findings were accepted to
cover adaptation and agentic sandboxing plus model-as-judge/oracle definition;
two Grok functions were also added. The campaign-scoped identity finding was
explicitly deferred because importing it verbatim would contradict the chosen
single-evaluation-instance root. Eighteen decisions were recorded and no
critical conflict remains; six topics remain deferred.

Both valid provider runs used the same frozen contract and clean input commit
`e2a534fb55bb8d3c70ed59811de472b5b7ded517`. Grok returned substantive content
inside a non-canonical response envelope. A no-tools pass normalized only the
contract shape and applied one cross-grain identifier namespace repair; it made
no semantic repair. Both provider results and the synthesis pass schema and
semantic validation.

Live source and revision verification, verification of the completed source-ID
remapping, the Croissant version conflict, paywalled ISO alignment verification,
provisional NIST AI 200-2 vocabulary and multi-profile validation remain
publication holds. See
`synthesis-plan.json`, `adjudication.json`, `comparison.json` and
`synthesis.validation.json`.

Published draft:
<https://ver.cy/models/wm-ai-003-ai-model-evaluation/>
