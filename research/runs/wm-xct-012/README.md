# WM-XCT-012 — Provenance research

Status: **both independent provider passes complete; synthesis pending**.

| Result | Sources | Bundles | Layers | Findings | Questions | Artifacts | Functions |
|---|---:|---:|---:|---:|---:|---:|---:|
| Claude | 19 | 6 | 14 | 30 | 113 | 27 | 14 |
| Grok | 14 | 7 | 16 | 21 | 72 | 10 | 12 |

Both providers classify Provenance as a reusable `mixin`. The deterministic
comparison identifies candidate overlap in 5 bundles and 12 layers. Semantic
adjudication is still required before a canonical synthesis is created.

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

See the provider results, validation reports and `comparison.json` in this
directory. No canonical specification has been published from this research.
