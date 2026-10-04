# WM-XCT-021 — Lifecycle / Status research

Status: **validated synthesis published as a public research draft; not yet a
canonical release**.

| Result | Sources | Bundles | Layers | Findings | Questions | Artifacts | Functions |
|---|---:|---:|---:|---:|---:|---:|---:|
| Claude | 24 | 5 | 12 | 27 | 113 | 26 | 14 |
| Grok (normalized) | 12 | 6 | 12 | 30 | 90 | 7 | 11 |
| Synthesis | 29 | 5 | 12 | 32 | 128 | 26 | 17 |

Both providers classify Lifecycle / Status as a host-bound `mixin`. The
synthesis uses Claude's boundaries for lifecycle definition, assertions and
history, bitemporal validity, succession/invalidation/disposition, and
operations/interoperability. It adds Grok's independently grounded findings for
binding identity, host/aspect multiplicity, lifecycle profile families, active
configuration with lossy scalar projection, and replacement versus
`entered-in-error`.

Grok's research completed with substantive content but malformed JSON. Its raw
wrapper is retained unchanged outside Git. A no-tools Claude pass performed only
schema normalization; `grok.normalization.manifest.json` records the hashes,
tool-free constraint and validation result. The normalized Grok result passes
both JSON Schema and semantic validation.

Important decisions:

- There is no universal status-code list across workflow, publication, clinical,
  records and other lifecycle families; they are versioned profiles.
- A host can carry several orthogonal lifecycle bindings and a state machine can
  have multiple active states. A scalar projection must report loss.
- Valid time, event time, observation time and transaction/record time remain
  separate.
- `unknown`, `inactive`, `completed`, `retired`, `revoked` and
  `entered-in-error` are not synonyms.
- Identity uses the master-system ID or UUIDv7/ULID; timestamp is a separate RFC
  3339 fact with seconds and explicit timezone.

The source-verification and cross-domain profile tests remain open. See
`synthesis-plan.json`, `adjudication.json`, `comparison.json` and
`synthesis.validation.json` for the evidence trail.

Published draft:
<https://ver.cy/models/wm-xct-021-lifecycle-status/>
