The team agrees: the contour is a version-pinned profile over the two existing masters, not a new aggregate.

## DECISION
**PROFILE**

A thin, version-pinned Enterprise conformance layer over WM-DAT-001 and WM-DAT-004 is justified. The bases already own the subject types. What the contour adds is a small set of cross-model rules that are optional in those bases and that the acceptance scenario needs. A new aggregate would invent a runtime identity that DCAT 3, ODCS, JSON Schema and ISO/IEC 11179 do not define. Plain reuse would leave the joining rules unenforced.

## BOUNDARY CHECK
WM-DAT-001 already owns the dataset aggregate: abstract dataset identity, version identity, distribution bytes, the catalogue-record facet, fixity, asset-level provenance, rights and permitted use, quality evidence, a breaking-change flag, and a declared schema/contract reference. Field semantics, compatibility modes and producer–consumer obligations are out of scope and pointed at WM-DAT-004. The catalogue record is a registration object (`dcat:CatalogRecord`); it does not replace the dataset.

WM-DAT-004 already owns schema and contract as citable resources: independent immutable versions, structural properties, ISO/IEC 11179-style term and value-domain bindings, compatibility modes and check records, producer/owner and consumer obligations, publication status distinct from version, and a `dcterms:conformsTo` binding to a dataset or distribution. It does not own dataset identity, distribution bytes or catalogue records.

WM-DAT-008 and EM-DAT-02 own the consumer-facing data-product offering. EM-DAT-03 owns pipeline and deep lineage. EM-DAT-04 owns the quality-rule engine. EM-DAT-01 must reference those neighbours, not absorb them.

DCAT 3 separates Dataset, Distribution and CatalogRecord; adds `dcat:version` / `dcat:previousVersion` / `dcat:hasCurrentVersion`; allows `spdx:checksum` on a distribution; and uses `dcterms:conformsTo` for an external schema or profile. It has no data-contract class. DQV attaches measurements to a dataset or distribution; `QualityPolicy` is not a producer–consumer contract. PROV-O supplies `wasRevisionOf`, `wasDerivedFrom`, `wasGeneratedBy` and `wasAttributedTo` without defining Dataset. DataCite 4.6 treats Version as optional and uses relation types for major-version identity; 4.7 is a compatible vocabulary extension, not a new type. ODCS is a contract document dialect (live v3.2.0; the base is still pinned near v3.1.0). JSON Schema identifies schema resources. ISO/IEC 11179 separates data-element concept, conceptual domain, value domain and representation.

No portable standard requires a fused Dataset+Schema+Contract personality. The missing piece is constraint promotion, not a third master.

## ACCEPTANCE SCENARIO
One dataset keeps a stable abstract identifier. Two delivery formats are two Distributions of one DatasetVersion, each with its own media type, byte size and checksum. A later structural change issues a new WM-DAT-004 contract version. Dataset version advances only if content or the published compatibility outcome requires it; schema/contract version is free to move on its own. The new dataset version carries a predecessor pointer and PROV assertions. Compatibility mode and check outcome are published; the dataset breaking flag is derived from that outcome, not asserted independently. The catalogue record continues to point at the same dataset. The negative case — a new CSV minting a new semantic dataset — is already rejected by DCAT 3 and WM-DAT-001.

This path holds only if the joining rules below are required. Installed as-is, both bases allow the scenario to fail: checksum, version-pin, compatibility outcome and predecessor may all be omitted.

## PORTABLE CONSTRAINTS
Retain in the reusable Enterprise profile (pin WM-DAT-001 `0.3.0-research.1` and WM-DAT-004 `0.3.0-research.1`):

- Stable abstract dataset identifier plus a version-scoped identifier on every release.
- Checksum on every distribution of a published dataset version.
- Version-pinned contract reference and recorded comformance status.
- One contract version across all distributions of one dataset version.
- Required compatibility mode and a published compatibility-check outcome.
- Dataset breaking-change flag derived from that outcome.
- Declared consumer scope and an explicit change-notice path (existence of the path, not its SLA).
- Predecessor and provenance assertions required when a dataset version is issued.
- Authoritative term and value-domain bindings for designated critical data elements.

Deployment policy, not profile semantics: notice-period length and channel; which properties are designated critical; consumer-registration enforcement; master-system and PID-scheme choice (DOI-per-version versus abstract-plus-version, provided the policy is explicit); licence catalogue; SLA and freshness numbers; choice of ODCS dialect beyond “pin a version.”

## HOLDS
Both bases are `adjudicationStatus: reviewable-draft` and `publishableCanonical: false`. Open source holds that actually block canonical publication:

- Live re-fetch and version-pin of WM-DAT-001 sources; DataCite 4.6 versus 4.7 citation-vocabulary consistency.
- ODCS source pinning and the v3.1.0 `dataProduct` deprecation contradiction versus live v3.2.0.
- ISO/IEC 11179-3:2023 and 11179-31:2023 remain catalogue-level; clause-level evidence is hypothesis only.
- Multi-profile SHACL validation (DCAT-AP 3.0.0 and at least one further profile) is unrun.

These holds sit on the bases. They do not create a missing aggregate. A non-canonical Enterprise profile draft is still appropriate: it can pin the two research versions, state the tightening rules, and inherit the holds instead of claiming they are closed.

## PUBLICATION RECOMMENDATION
Publish EM-DAT-01 as an Enterprise profile companion, not as a new subject model and not as a silent reuse map. Version-pin both bases. Do not mint a DatasetSchemaContract identity. Keep catalogue-record, data-product, lineage and quality-engine ownership with their existing models. Ship as `reviewable-draft` with `publishableCanonical: false` until the inherited source, ODCS, 11179 and SHACL holds close. Fixture the acceptance scenario (one dataset, two distributions, later schema version, predecessor plus derived compatibility) before any canonical claim.