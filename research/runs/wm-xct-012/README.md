# WM-XCT-012 — Provenance research

Status: **validated synthesis published as a public research draft; not yet a
canonical release**.

| Result | Sources | Bundles | Layers | Findings | Questions | Artifacts | Functions |
|---|---:|---:|---:|---:|---:|---:|---:|
| Claude | 19 | 6 | 14 | 30 | 113 | 27 | 14 |
| Grok | 14 | 7 | 16 | 21 | 72 | 10 | 12 |
| Synthesis | 28 | 6 | 14 | 33 | 123 | 28 | 14 |

Both providers classify Provenance as a reusable `mixin`. The synthesis uses the
more complete standards-led Claude hierarchy and adds Grok's separately grounded
findings for generation/usage/communication constraints, start/end/invalidation
events, and the distinction among claim generator, signer and trusted builder.

Key conflicts already surfaced for adjudication:

- W3C PROV uses provenance as a derivation graph, while ISO 19115 distinguishes
  provenance from lineage and Dublin Core commonly uses a narrative statement.
- Legal title, physical custody, attribution, responsibility and signer/builder
  trust must remain distinct.
- C2PA records assertions without declaring content good or bad; SLSA levels are
  assurance grades and cannot be inferred from a C2PA manifest.
- Persistence and archive requirements can conflict with privacy and erasure;
  redaction/tombstone semantics must be explicit.
- A provenance assertion may be structurally valid while its asserter is not
  trusted; syntax, evidence integrity and trust evaluation are separate.

The result passes the Vercy schema and semantic gate with no critical conflicts.
It remains a research draft while live source/claim verification and sector
profiles are open. See `synthesis-plan.json`, `adjudication.json`,
`comparison.json` and `synthesis.validation.json` for the evidence trail.

Published draft:
<https://ver.cy/models/wm-xct-012-provenance/>
