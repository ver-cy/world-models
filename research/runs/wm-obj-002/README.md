# WM-OBJ-002 - Product Type / Catalog Item research

Status: **validated synthesis published as a public research draft; not yet a
canonical release**.

| Result | Sources | Bundles | Layers | Findings | Questions | Artifacts | Functions |
|---|---:|---:|---:|---:|---:|---:|---:|
| Claude | 15 | 7 | 14 | 28 | 112 | 16 | 12 |
| Grok (normalized) | 19 | 7 | 12 | 13 | 47 | 10 | 8 |
| Synthesis | 30 | 7 | 14 | 30 | 120 | 17 | 14 |

Both providers independently classify Product Type / Catalog Item as a
`classifier`: it governs the class or type that instances conform to. Physical
or serialised instances, lots or batches, commercial offers and prices,
inventory, logistics units and engineering BOM structures remain neighbouring
responsibilities.

The no-tools adjudication retained Claude's scheme-neutral identity and
granularity model and accepted Grok's regulated type identifiers plus the
class-to-instance classification edge and bounded BOM reference. GTIN is not
treated as the sole identity anchor; product model, trade item, packaging level
and regulated grouping may occupy different grains under different governing
schemes.

Grok's substantive answer arrived as an unrecognized transport envelope. The
immutable raw wrapper remains outside Git; a no-tools pass normalized transport
only. Both provider results pass schema and semantic validation without manual
content edits.

No critical structural conflicts remain. Live GS1/schema/GPC/HS/FDA pins,
ratified GTIN rule text, UNTP 1.0, ESPR article text, four domain-profile round
trips and the open product-master security evidence gap remain explicit
publication holds. See `synthesis-plan.json`, `adjudication.json`,
`comparison.json` and `synthesis.validation.json`.

Published draft:
<https://ver.cy/models/wm-obj-002-product-type-catalog-item/>
