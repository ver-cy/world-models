# WM-XCT-009 — Time / Calendar research

Status: **validated synthesis published as a public research draft; not yet a
canonical release**.

| Result | Sources | Bundles | Layers | Findings | Questions | Artifacts | Functions |
|---|---:|---:|---:|---:|---:|---:|---:|
| Claude | 24 | 7 | 20 | 20 | 111 | 27 | 13 |
| Grok (normalized) | 14 | 3 | 6 | 13 | 52 | 14 | 8 |
| Synthesis | 31 | 7 | 20 | 20 | 111 | 27 | 13 |

Both providers classify Time / Calendar as a reusable `mixin` plus governed
reference data. The synthesis retains Claude's more granular seven-bundle
hierarchy. Grok independently confirms the same time-base, zone, calendar,
recurrence, holiday and observance boundary and contributes sources, access
rules, omissions, conflicts, regional assumptions and adversarial checks.

Grok completed its research with substantive content but malformed JSON. The raw
wrapper is retained unchanged outside Git; a no-tools Claude pass performed only
schema normalization. `grok.normalization.manifest.json` records its input hash,
output hash, validation and four cross-grain `data-*` ID repairs. The normalized
provider result passes both JSON Schema and semantic validation.

Important decisions:

- Artifact timestamps use RFC 3339 with seconds and an explicit offset or `Z`,
  but identity uses the authoritative master-system ID or UUIDv7/ULID.
- Civil-time law and the tzdb mirror are separate authorities and can diverge.
- Floating, numeric-offset and named-zone times are not interchangeable.
- Recurrence expansion is calendar-, zone-, exception- and version-dependent.
- Missing jurisdictional holiday coverage remains unknown; it never implies a
  working day.

The source-verification and global jurisdictional coverage holds remain open.
See `synthesis-plan.json`, `adjudication.json`, `comparison.json` and
`synthesis.validation.json` for the evidence trail.

Published draft:
<https://ver.cy/models/wm-xct-009-time-calendar/>
