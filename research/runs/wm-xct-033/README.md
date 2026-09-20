# WM-XCT-033 - Geometry / Coordinate Reference research

Status: **validated Claude-only synthesis prepared as a public reviewable
research draft; not a canonical release**.

| Result | Sources | Bundles | Layers | Findings | Questions | Artifacts | Functions |
|---|---:|---:|---:|---:|---:|---:|---:|
| Synthesis | 53 | 13 | 30 | 64 | 284 | 24 | 46 |

Claude researched the model through six independently schema-valid bounded
passes: geometry core, CRS identity, dynamic and compound CRS context,
transformation quality, governance controls, and service operations. Their
local identifiers are disjoint. The deterministic merger remapped and
deduplicated sources, routed coverage dimensions, selected the governance
service layer, and revalidated the complete structure.

The original combined CRS-context pass and the original combined
governance-services pass exceeded the provider timeout and produced no
accepted result. Each was divided into smaller bounded passes. A first
transformation-quality attempt ended with a transient generic API error and
was repeated with the same scope. No partial or failed provider output entered
the synthesis.

The first no-tools audit found no critical conflict but exposed two correctable
boundary defects. Geometry representation was incorrectly marked not
applicable even though the merged core defines it. Six composition entries
also described WM-XCT-010 as a geometry parent, although its registry title is
Location Referencing / Address and the frozen relationship contract is empty.
The result now marks geometry representation covered and treats every
WM-XCT-010 edge as a provisional registry parent candidate. These changes are
recorded in `adjudication-repairs.json`; hashes were updated and the repaired
result was independently re-adjudicated with zero critical conflicts.

The final audit retained `mixin` as the best entry kind. Geometry values remain
host-dependent, while local service concurrency, supersession and tombstone
rules apply to the versioned attachment rather than creating a separate entity.
The missing relationship contract, live source and version verification, and
several primary standards that could not be retrieved remain visible
publication holds.

The repository owner explicitly waived Grok for this queue, so no Grok output
was fabricated or inferred. The package visibly retains that single-provider
hold and remains `reviewable-draft`; it is not a final or canonical result.

Published draft:
<https://ver.cy/models/wm-xct-033-geometry-coordinate-reference/>
