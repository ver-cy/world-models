# Verdict

No candidate earns a new root. All six resolve to existing roots or to contained identities inside them: **ItemDefinition → reject** (splits across WM-OBJ-002 commercial type and WM-OBJ-018 engineering definition; as a single root it re-creates the negative case). **SKU → reject as root; profile** as a scoped, party-qualified alias on WM-OBJ-002 (`secondary-and-partner-keys`) and/or a WM-OBJ-017 variant qualifier; a priced sellable unit belongs to the EM-PRD-01 Offering candidate. **EngineeringRevision → reject as root; profile** the contained immutable revision of WM-OBJ-018 (`design-revision`, `baseline-package`). **BillOfMaterials → reuse WM-OBJ-019** for the EBOM only. **BOMLine → reject as root**; it is the baseline-scoped occurrence inside WM-OBJ-019 (`component-occurrence`), with no identity or lifecycle outside its baseline. **SubstitutionRule → reject as root; profile** WM-OBJ-019 `component-selection`, extended with applicability/effectivity and authority.

Three masters are **missing**: manufacturing BOM/manufacturing plan (routing, operations, process consumption, scrap/yield), as-built assembly, and lot/batch — plus the actual transformation/consumption-production event and a production work order.

# Evidence

WM-OBJ-002 masters type identity, classification, variant structure and packaging, and explicitly out-of-scopes "the internal structure and effectivity logic of the engineering bill of material", holding only a reference to the governing BOM revision. WM-OBJ-018 masters controlled design revisions and baseline packages and out-of-scopes BOM composition. WM-OBJ-019 masters occurrences, quantity basis, effectivity, options/alternates/substitutes and declares view and revision — and out-of-scopes "production routes, procurement execution" and "as-built item state, actual material consumption". WM-OBJ-001 masters the individuated instance and refuses identity to batch, bulk and fungible matter, redirecting to a sibling it names as missing. WM-FLW-013 requires every genealogy edge to cite an actual event with evidence and forbids inferring composition from intent.

# Identity/mastership

Distinct identities, each with independent lifecycle: catalog item/type (WM-OBJ-002); configuration variant (WM-OBJ-017); engineering design (WM-OBJ-018) and its revision (contained); EBOM baseline (WM-OBJ-019) and its occurrence (contained); MBOM/routing (missing); serialized item (WM-OBJ-001); lot/batch (missing); as-built assembly (missing; WM-OBJ-012 appears only as a dangling relation target); firmware/software release (WM-SFT-008) and its component/package (WM-SFT-007); SBOM document (WM-SFT-012); actual transformation event (missing). SKU, EngineeringRevision, BOMLine and SubstitutionRule are contained identities, not roots.

# Product/SKU/variant

WM-OBJ-002 carries a scheme-neutral anchor with explicit granularity; SKU is a seller-scoped key, never authoritative and never a serial. WM-OBJ-017 sits between type and instance and CLASSIFIES configured instances — note it expresses CLASSIFIES as REFERENCE because the research enum lacks the term, diverging from the relations ledger. Commercial succession/substitution on WM-OBJ-002 (`predecessor-successor-and-substitution`) is a different relation from engineering substitution in WM-OBJ-019 and must not be merged.

# Engineering definition/revision

WM-OBJ-018 owns intended definition, representation authority, requirement realization and release/effectivity; revisions are immutable, superseded by linked successors, and design identity is independent of filenames and exports. Two revisions of one design are two contained baselines under one design identity, not two designs and not two product types.

# EBOM/MBOM

EBOM is reusable type-level composition under a declared view. MBOM/manufacturing plan — routing, operations, process-added material, scrap and yield basis, plant/line applicability — has no reservation and cannot be derived from the EBOM. Reconciliation is an explicit, evidenced mapping between EBOM occurrences and MBOM operations, not a transformation of one into the other. BOM kind and immutable version are mandatory on both.

# Lines/substitutions/effectivity

Occurrences are stable, repeated and never merged by displayed row number. Quantities state unit, parent base quantity, conversion/rounding policy and explicit unknowns; alternates are never summed as simultaneously installed. Substitution is directional, evidence-qualified, and must carry applicability/effectivity range and approving authority; a candidate alternate is not an installed component. Effectivity predicates are resolvable only against a referent — lot-based effectivity therefore depends on the missing lot/batch master.

# Firmware/software

Firmware is WM-SFT-007 (component/package) plus WM-SFT-008 (release, artifact digests, provenance, support window) with WM-SFT-012 as the referenced SBOM document. A release is not a device and not a part number in the EBOM; binding a release to a serialized item is a deployment/installation occurrence (WM-SFT-009, referenced but unsupplied here), not a BOM line and not a shared Product record.

# Instance/lot/as-built

Serialized instances are WM-OBJ-001; lots are not instances and lot membership is provenance only. As-built composition is proven exclusively from actual events — attach/detach membership periods, aggregation/disaggregation, transformation with successor derivation — each carrying event time, location, agent, method and evidence digest. BOM intent never establishes as-built content. With WM-OBJ-012 absent, no root currently masters the as-built graph; WM-OBJ-001 holds only the membership pointer.

# Time/quantity/provenance

Event, effective, observation, record, posting, ingestion, publication and correction times stay distinct, RFC 3339 with explicit offset. Every quantity carries unit, basis and code-list version; unknown, zero, not-applicable and withheld never collapse. Declared, observed and inferred edges remain separated; corrections append successors and never overwrite.

# Governance

Owners: product/catalog steward (WM-OBJ-002), design authority and release approver (WM-OBJ-018), composition authority (WM-OBJ-019), item steward (WM-OBJ-001), software product owner (WM-SFT-007/008/012). Deny-by-default access; substitution approval, revision release and effectivity changes require named authority; conformance claims require stored evidence.

# Acceptance scenario

Design D has revisions R1 and R2 (contained in WM-OBJ-018). EBOM baselines B1(R1) and B2(R2) in WM-OBJ-019 differ at one occurrence, where B2 adds an approved alternate with an effectivity range and authority. Firmware F v1.2.0 is a WM-SFT-008 release with an SBOM reference. Lot L is manufactured under B2 effectivity; unit S/N-001 from L is a WM-OBJ-001 instance. Its as-built content is assembled from consumption/attach events citing the alternate actually installed, and F v1.2.0 appears only via an installation occurrence. Revision effectivity by lot is expressible as a predicate but **not resolvable** until the lot master exists; as-built composition holds because it derives from events, not from B2.

# Invariants

1. Every BOM states kind and an immutable version. 2. Every quantity carries unit and basis. 3. Every substitution carries applicability/effectivity and approving authority. 4. One record never serves as drawing, SKU and serial. 5. As-built composition derives only from actual events with evidence. 6. Occurrence identity is baseline-scoped and never global. 7. Alternates are candidates, not installed components. 8. A release is not a device and not an EBOM line. 9. Lot is not an instance. 10. EBOM never yields MBOM without an evidenced mapping. 11. Identifiers are never reused; retirement leaves a tombstone.

# Minimal model set

WM-OBJ-002, WM-OBJ-017, WM-OBJ-018, WM-OBJ-019, WM-OBJ-001, WM-SFT-007, WM-SFT-008, WM-SFT-012, WM-FLW-013, plus missing MBOM/manufacturing-plan, as-built assembly, lot/batch, actual transformation event and production work order.

# Holds

Relation contradictions: WM-OBJ-019↔WM-OBJ-002 is simultaneously parent, COMPOSE and REFERENCE; WM-OBJ-018 as child of WM-OBJ-002 conflicts with its own required REFERENCE; WM-SFT-012 and WM-SFT-008 claim CHILD of WM-SFT-007 while the ledger records REFERENCE or no edge; WM-OBJ-012/020/021/022 and WM-ACT-015 are dangling targets; CLASSIFIES is absent from the enum; WM-ACT-007 is maintenance-scoped with unresolved K11 duplication. Most bases are single-provider waivers, all are reviewable drafts, crosswalks and fixtures are absent, and no identifier was allocated. No claim of canonical completeness, installability or publication readiness is made.
