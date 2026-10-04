# WM-XCT-010 - Location Referencing / Address research

Status: **validated synthesis published as a public research draft; not yet a
canonical release**.

| Result | Sources | Bundles | Layers | Findings | Questions | Artifacts | Functions |
|---|---:|---:|---:|---:|---:|---:|---:|
| Claude (ID-repaired) | 19 | 6 | 16 | 27 | 124 | 21 | 11 |
| Grok (normalized) | 16 | 4 | 14 | 16 | 64 | 16 | 12 |
| Synthesis | 33 | 6 | 16 | 28 | 128 | 22 | 15 |

Both providers independently classify Location Referencing / Address as a
reusable `mixin`. It owns governed reference records for addresses, positions,
geographic identifiers, toponyms and POI facets. Addressable objects, parties,
transport-network geometry, geodetic parameter registries and public-law
mandates remain sibling responsibilities.

The no-tools adjudication retained Claude's finer boundary and accepted Grok's
ISO 19160-3 quality-element structure plus a missing crosswalk operation. It
rejected duplicate address/gazetteer/POI structures and vendor-specific code
functions, while deferring weakly grounded linear-referencing expansion.

Claude's direct result had one cross-grain ID collision; the deterministic
repair changed the finding ID to `finding-addressable-object-binding` and records
that change in the provider manifest. Grok's malformed JSON transport was
syntax-normalized by a no-tools Claude pass. All provider and synthesis results
pass schema and semantic validation.

No critical structural conflicts remain. Paywalled ISO clauses, blocked FGDC
and NENA source documents, UPU/ISO lineage, live version pins, non-Western
address profiles and jurisdictional privacy/retention policy remain explicit
publication holds. See `synthesis-plan.json`, `adjudication.json`,
`comparison.json` and `synthesis.validation.json`.

Published draft:
<https://ver.cy/models/wm-xct-010-location-referencing-address/>
