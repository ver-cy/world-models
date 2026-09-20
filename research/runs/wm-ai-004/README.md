# WM-AI-004 - AI Inference / Agent Run research

Status: **validated synthesis published as a public research draft; not yet a
canonical release**.

| Result | Sources | Bundles | Layers | Findings | Questions | Artifacts | Functions |
|---|---:|---:|---:|---:|---:|---:|---:|
| Claude | 16 | 7 | 15 | 28 | 107 | 18 | 10 |
| Grok (normalized) | 11 | 6 | 12 | 22 | 86 | 21 | 9 |
| Synthesis | 23 | 7 | 15 | 30 | 115 | 20 | 11 |

The no-tools adjudication classified AI Inference / Agent Run as an `event`.
The run is a bounded occurrent or activity with its own identity and lifecycle;
the executing agent, configuration revision, registered AI system, model
artifact, conversation container and evaluation result remain sibling records.
Trace and span identifiers correlate distributed evidence but do not replace
the run identity.

Claude was retained as the structural base. Accepted Grok additions bind the
stable executing-agent identity, cover rare endings such as folded retries,
cancellation, compaction and fetch-without-inference, and add an explicit
content-capture-policy operation before redaction. Seventeen decisions were
recorded and no critical conflict remains. Memory operations, MCP telemetry,
billed-versus-consumed tokens, encrypted replay material, proxy attribution,
sampling obligations and global run identity remain deferred research.

Both provider runs used the same frozen contract and clean input commit
`1ac541dfa9889657919eccb6e67deb8fb45d8053`. Grok returned substantive content
using a non-canonical response envelope. The raw wrapper remains outside Git; a
no-tools pass normalized only the contract shape, made no semantic repairs and
required no cross-grain identifier repairs. Both provider results and the
synthesis pass schema and semantic validation.

Official EU AI Act verification, live source and revision pinning, evidence
resolution for accepted additions, additional domain profiles, current legal
application dates and OpenTelemetry-versus-vendor cost wording remain
publication holds. See `synthesis-plan.json`, `adjudication.json`,
`comparison.json` and `synthesis.validation.json`.

Published draft:
<https://ver.cy/models/wm-ai-004-ai-inference-agent-run/>
