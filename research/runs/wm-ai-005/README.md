# WM-AI-005 - Prompt / Agent Configuration research

Status: **validated synthesis published as a public research draft; not yet a
canonical release**.

| Result | Sources | Bundles | Layers | Findings | Questions | Artifacts | Functions |
|---|---:|---:|---:|---:|---:|---:|---:|
| Claude | 19 | 7 | 15 | 28 | 102 | 25 | 10 |
| Grok (normalized) | 14 | 4 | 8 | 16 | 64 | 16 | 7 |
| Synthesis | 32 | 7 | 15 | 32 | 118 | 29 | 12 |

The providers disagreed on entry kind. The no-tools adjudication accepted
`aggregate`: the pin-able revision is the consistency root, while instruction
blocks, template arguments, tool and context grants, guardrail bindings and
autonomy caps have no independent lifecycle outside that revision. AI agents,
individual runs, reusable skills, model weights, knowledge corpora, secrets and
runtime data remain sibling records connected through typed references.

Claude was retained as the structural base. Accepted Grok additions cover
portable skill packages and progressive disclosure, configuration kind and
intended use, an external-schema alignment map, default modalities and narrowed
handoff bindings. Sixteen decisions resolved the provider differences and no
critical conflict remains. Dynamic instructions, effective-stack digests,
guardrail failure modes, hosted prompt objects, experiments, determinism and
internationalisation remain deferred research.

Both provider runs used the same frozen contract and clean input commit
`b9376565c531d7e5db37864c78f0b9f11876b4ed`. Grok returned substantive content
using a non-canonical response envelope. The raw wrapper remains outside Git; a
no-tools pass normalized only the contract shape, made no semantic repairs and
required no cross-grain identifier repairs. Both provider results and the
synthesis pass schema and semantic validation.

Live source and revision pinning, provisional MCP/OTel labelling, licensed ISO
verification, source-ID remapping review, additional domain profiles, OWASP
edition reconciliation and locale-equivalence evidence remain publication
holds. See `synthesis-plan.json`, `adjudication.json`, `comparison.json` and
`synthesis.validation.json`.

Published draft:
<https://ver.cy/models/wm-ai-005-prompt-agent-configuration/>
