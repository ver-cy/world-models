# Source inspection and access checks

Checked on 2026-09-07. These are inspection-depth statements, not claims of
complete standards compliance. Source URLs and versions are in codex.result.json.

| Source | Direct HTTP | Inspected support | Remaining limitation |
| --- | --- | --- | --- |
| SRC-001 | 200 | ProductGroup grouping, variation axes and inheritance exceptions | Development vocabulary snapshot; no tested crosswalk |
| SRC-002 | 200 | ProductModel and isVariantOf distinction and non-transitive inheritance | No blanket equivalence to engineering variant or individual item |
| SRC-003 | 200 | GS1 CPV guideline 1.1; consumer variant scope and first consulting GTIN management rules | No complete GDSN mapping or identifier-allocation certification |
| SRC-004 | 200 | Official page dated 2026-05-06; typed options, conditional fields, tables, calculations and BOM selection | Vendor implementation evidence, not universal solver semantics |
| SRC-005 | 200 | UBL 2.4 catalogue item specification versus pricing update purpose | No executable UBL transformation or round-trip fixtures |
| SRC-006 | 200 | PROV-DM entity, activity, agent and derivation vocabulary | Vercy policy choices are proposed design, not PROV requirements |
| SRC-007 | 200 | RFC 3339 timestamps with seconds and offset | Timestamp is not unique identity |
| SRC-008 | 403 | Official indexed ISO 10007:2017 public abstract available | Direct anti-bot restriction; licensed clauses not read |
| SRC-009 | 403 | Official indexed ISO 10303-242:2025 public engineering scope available | Direct anti-bot restriction; licensed clauses and mappings not read |

Sources proposed in early notes but not admitted: AAS, QUDT, ECLASS, IEC CDD
and Digital Link URI syntax. They are not counted as verified support in this
release. A larger bibliography without completed inspection is not a quality
improvement. Physical and capability records are explicitly proposed Vercy
extensions that require per-product evidence on adoption.
