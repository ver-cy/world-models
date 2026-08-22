# WM-XCT-022 — Version / Change History research

Status: **validated synthesis published as a public research draft; not yet a
canonical release**.

| Result | Sources | Bundles | Layers | Findings | Questions | Artifacts | Functions |
|---|---:|---:|---:|---:|---:|---:|---:|
| Claude | 27 | 6 | 12 | 25 | 115 | 23 | 17 |
| Grok (normalized) | 9 | 4 | 8 | 13 | 59 | 12 | 11 |
| Synthesis | 32 | 6 | 12 | 25 | 115 | 23 | 19 |

Both providers classify Version / Change History as a reusable `mixin`. The
synthesis retains Claude's detailed boundaries for revision/series identity,
lineage topology, change substance and migration, temporal/lifecycle semantics,
authority/integrity, and history access/retention. Grok independently confirms
the structure and adds explicit operations to freeze a released revision and to
publish one immutable revision as the current member of a series.

Grok's substantive answer completed with malformed JSON transport. Its raw
wrapper is retained unchanged outside Git. A no-tools Claude pass performed only
schema normalization; `grok.normalization.manifest.json` records the source and
result hashes, disabled tools and validation. The normalized result passes both
JSON Schema and semantic validation.

Important decisions:

- A mutable series/permalink, current pointer and immutable revision have
  different identities and citation semantics.
- Revision, translation, rendition, derivation and format variant use different
  typed relations.
- History is a graph; a single `previousVersion` link loses merge and branch
  semantics.
- SemVer expresses an intended designation policy, not proven compatibility.
- Git diff, JSON Patch and database migration are projections of a logical
  source-target change set with preconditions and loss/verification rules.
- Version identity is not a timestamp; timestamps are separate RFC 3339 facts
  with seconds and explicit timezone.

Source verification and cross-representation profile tests remain open. See
`synthesis-plan.json`, `adjudication.json`, `comparison.json` and
`synthesis.validation.json` for the evidence trail.

Published draft:
<https://ver.cy/models/wm-xct-022-version-change-history/>
