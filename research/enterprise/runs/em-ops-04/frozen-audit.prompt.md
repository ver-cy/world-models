You are the single final frozen semantic auditor for EM-OPS-04. Use only the supplied frozen materials. No tools, browsing, external facts, invented identifiers, publication claims, or requests for another review. Reconcile Claude and Grok, decide whether the boundary is settled, and audit every candidate/profile/fixture/policy artifact. Preserve the settled decision unless the supplied evidence proves it inconsistent.

Return exactly:
1. Verdict on decision and artifacts.
2. Material defects and exact deterministic remediation, numbered D1..., with literal field/value edits sufficient for a local script. Cover root decisions, authority, identity, lifecycle, kind/version, quantity/unit/basis, effectivity, provenance, intent-vs-actual separation, firmware/SBOM, incomplete relations, and publication holds.
3. Additional fixtures as one fenced JSON array. Each item must contain id, target, kind, input, expect, violates, closesDefect; every negative item also needs expectedCode. Add enough positive and negative fixtures to close every defect and provider invariant.
4. Exact final fixture counts, combining all existing fixtures with additions.
5. Freeze decision stating deterministic remediation closes the audit without rerun.

Do not allocate identifiers. Do not promote an unassigned candidate or invent internal schemas for referenced models. Treat the visible Grok response as evidence; hidden reasoning and UI sources are excluded.

FROZEN MATERIALS

## FILE local-evidence.md
# EM-OPS-04 local synthesis

## Disposition

- Split Item Definition across WM-OBJ-002 commercial/product type and WM-OBJ-018 engineering definition; do not create a combined root.
- Profile SKU as a party-scoped identifier on WM-OBJ-002 or WM-OBJ-017, not a root or serial number.
- Keep Engineering Revision as an immutable contained revision/baseline of WM-OBJ-018.
- Reuse WM-OBJ-019 for EBOM; keep BOM Line as a baseline-scoped occurrence and Substitution Rule as a contained component-selection profile.
- Leave MBOM/Manufacturing Plan, As-Built Assembly, Lot/Batch, Actual Transformation Event and Production Work Order identifier-unassigned.
- Allocate no catalogue or runtime identifier.

## Identity and mastership

Product type, configuration variant, engineering design, design revision, EBOM baseline, BOM occurrence, serialized item, lot, as-built assembly, firmware release and transformation event remain distinct.

WM-OBJ-002 owns catalog/type identity. WM-OBJ-017 owns configuration variants. WM-OBJ-018 owns controlled design and immutable revisions. WM-OBJ-019 owns EBOM baselines and occurrences. WM-OBJ-001 owns individuated physical items.

SKU, Engineering Revision, BOM Line and Substitution Rule have scoped identities and no independent lifecycle outside their owner.

## Product, SKU and variant

SKU is a seller-scoped alias or variant qualifier and never identifies a serial item. A sellable priced unit belongs to the separate Offering boundary. Commercial product substitution differs from engineering component substitution and must not merge.

One Product record cannot simultaneously mean catalog item, drawing/design, BOM, firmware release and serial number.

## Engineering definition and revision

Design identity is stable across immutable revisions. Each revision pins representations, requirements, authority, release status and effectivity. Successors never overwrite predecessors. File names and exports do not establish design identity.

## EBOM and MBOM

WM-OBJ-019 is the EBOM master: declared view, immutable baseline, occurrences, quantities, effectivity, alternates and substitutions. It explicitly excludes production routes and actual consumption.

MBOM/Manufacturing Plan needs a separate root for routing, operations, plant/line applicability, process-added material, scrap and yield. Reconciliation is an explicit evidenced mapping between EBOM occurrences and MBOM operations.

## Lines, substitutions and effectivity

BOM occurrences are baseline-scoped and remain distinct even when displayed row numbers match. Quantities state unit, parent base, conversion and rounding; alternates are not summed as installed.

Substitution is directional and carries applicable design/BOM revisions, serial/lot/time/site range, evidence and approving authority. Lot-based effectivity cannot resolve without a lot master.

## Firmware and software

Firmware uses WM-SFT-007 component/package plus WM-SFT-008 release, with WM-SFT-012 as SBOM record. A firmware release is neither a device nor an EBOM line.

Binding firmware to a physical item is a deployment/installation occurrence with its own time and evidence, not shared Product identity.

## Instance, lot and as-built

Serialized items are WM-OBJ-001. Lots are separate bulk/batch entities; lot membership is provenance only. As-built composition derives exclusively from attach, detach, aggregation, disaggregation and transformation events with time, location, agent, quantity and evidence.

BOM intent never proves actual composition.

## Acceptance result

Design D has revisions R1 and R2. EBOM B2 for R2 adds one approved alternate with effectivity and authority. Firmware F 1.2.0 is a release with SBOM. Lot L is manufactured under B2 and serialized unit S/N-001 belongs to L. Actual consumption and attach events prove which alternate was installed; firmware is linked by an installation occurrence. Lot-based effectivity remains unresolved until the lot master exists.

## Required invariants

1. Every BOM states kind and immutable version.
2. Every quantity carries unit and basis.
3. Every substitution carries applicability, effectivity and authority.
4. Drawing, SKU and serial remain distinct.
5. As-built composition derives only from actual events.
6. Occurrence identity is baseline-scoped.
7. Alternates are candidates, not installed components.
8. Firmware release is not a device or EBOM line.
9. Lot is not a serialized instance.
10. EBOM never becomes MBOM without an evidenced mapping.
11. Retired identifiers remain resolvable and are never reused.

## Holds

MBOM/Manufacturing Plan, As-Built Assembly, Lot/Batch, Actual Transformation Event and Production Work Order remain unallocated. WM-OBJ-019/002 relations conflict across parent, COMPOSE and REFERENCE; WM-OBJ-018 parentage conflicts with its reference boundary; software CHILD/REFERENCE edges disagree; several referenced object/action models are absent; CLASSIFIES is missing from the relation enum; WM-ACT-007 is maintenance-only with unresolved duplication. Most drafts are single-provider and all non-canonical; crosswalks and fixtures are absent. No installability or publication-readiness claim is made.


## FILE claude-study.raw.md
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


## FILE grok-prompt.md
# Exact unsent Grok prompt — EM-OPS-04

Independent enterprise metamodel review. Do not browse, invent identifiers or claim publication readiness.

EM-OPS-04 covers ItemDefinition, SKU, EngineeringRevision, BillOfMaterials, BOMLine and SubstitutionRule. Complete drafts cover physical items, product types, variants, engineering definitions, EBOMs, software components/releases, SBOMs, work orders and traceability.

Assess this proposal: split ItemDefinition between product type and engineering definition; profile SKU as a party-scoped key; contain Engineering Revision in WM-OBJ-018; reuse WM-OBJ-019 for EBOM; contain BOM Line and Substitution Rule in a baseline. Leave MBOM/Manufacturing Plan, As-Built Assembly, Lot/Batch, Actual Transformation Event and Production Work Order unassigned. Allocate no identifier.

Separate catalog item, SKU, variant, engineering design/revision, EBOM, MBOM/routing, occurrence, substitution, firmware release, SBOM, serialized item, lot, as-built assembly and transformation evidence. BOMs require kind/version; quantities require units/basis; substitutions require effectivity and authority. Never let one Product record mean drawing, SKU and serial.

Test two design revisions, one alternate component, one firmware release and one manufactured instance. Resolve lot effectivity and as-built content only from authoritative lot and actual events, never BOM intent.

Return <=900 words with: Verdict; strongest evidence; strongest counterexample; identity/mastership; product/SKU; design/revision; EBOM/MBOM; lines/substitution/effectivity; firmware; instance/lot/as-built; time/quantity/provenance; governance; scenario; at least 10 invariants; minimum model set; blockers. Decide every candidate and missing root.


## FILE grok-study.raw.md
Verdict. Conditional accept as a definition-side scope cut; reject as coverage of the EM-OPS-04 test. Accept the ItemDefinition split (product type versus engineering definition), SKU as a party-scoped key, baseline location for BOM Line and Substitution Rule, deferral of MBOM/Manufacturing Plan, As-Built Assembly, Lot/Batch, Actual Transformation Event and Production Work Order, and allocation of no identifier. Conditionally accept containing Engineering Revision in WM-OBJ-018 and reusing WM-OBJ-019 for EBOM only if those objects already master versioned definitions, not sellable items or serials. The mandated scenario does not close inside the assigned set.

Strongest evidence. The split and the party-scoped SKU are the minimum that stop one Product record from meaning drawing, SKU and serial at once. Two design revisions, an alternate, a firmware release and a manufactured instance are indistinguishable if catalog type, engineering definition, commercial key and instance share identity.

Strongest counterexample. Lot effectivity and as-built content may be resolved only from authoritative lot records and actual events. Those roots are unassigned. A manufactured instance that consumed an alternate under lot effectivity and a firmware release cannot be read from WM-OBJ-018, WM-OBJ-019 or a baseline Substitution Rule. Using EBOM intent as as-built content violates the resolution rule.

Identity/mastership. No identifier is allocated; no new root is named. Product type does not master engineering definition. Engineering revision does not master SKU or serial. EBOM does not master MBOM, occurrence, lot or as-built. WM-OBJ-018 and WM-OBJ-019 are given containers only; their internal schemas are not invented. Unassigned roots stay outside EM-OPS-04 mastership.

Product/SKU. Product type is decided as the catalog/type root from the split. Engineering definition is decided as a separate root. SKU is decided as a party-scoped commercial key, mappable to one or more engineering definitions, never identical to a revision or a serial. Variant is a configured selection over product type, not a revision and not an SKU. Catalog item is not SKU.

Design/revision. Engineering Revision is decided as contained in WM-OBJ-018, not as a new root and not as item identity. Two design revisions of one engineering definition must be distinguishable inside that container without re-identifying the product type or the SKU. If WM-OBJ-018 masters item identity rather than a versioned definition, containment is rejected.

EBOM/MBOM. EBOM is decided as a reuse of WM-OBJ-019 and must carry kind and version. Kind EBOM is intent only. MBOM and manufacturing plan/routing are decided as unassigned and must not be implied by that reuse. Occurrence (position in structure) is a missing root, distinct from BOM line and from serialized item.

Lines/substitution/effectivity. BOM Line and Substitution Rule are decided as baseline contents, not as complete models. A line quantity is invalid without unit and basis. A substitution is invalid without an effectivity bound (time, lot or serial) and an authority. An alternate is not a silent line overwrite. Baseline containment does not by itself name the effectivity-authority owner.

Firmware. Firmware release is a missing root: a versioned software component/release, not an Engineering Revision of a mechanical design and not an EBOM line by default. SBOM is a missing root: a BOM kind with its own version, not a substitute for firmware-release identity and not a collapse into ItemDefinition.

Instance/lot/as-built. Serialized item, Lot/Batch, As-Built Assembly, Actual Transformation Event and Production Work Order are decided unassigned. That deferral is correct. As-built content and lot effectivity are readable only from lot records and actual transformation events. BOM intent must not be projected onto a manufactured instance. A work order may bind consumption; it is not assigned here.

Time/quantity/provenance. Effectivity is time-, lot- or serial-bounded and always carries an authority reference. Quantity carries unit and basis (each, per, length, or other stated basis). Provenance of as-built is the chain of actual transformation events plus lot records, not the EBOM hierarchy. Design revision time is definition history; it is not instance history.

Governance. Substitution authority and effectivity owner are unresolved. No party is granted the right to treat EBOM reuse as manufacturing authorization. Cross-party SKU maps are relations, not identity. Unassigned actuals remain the only authorities for manufactured content.

Scenario. Two design revisions: distinguishable only inside WM-OBJ-018, if that container versions definitions. One alternate: resolvable only if the baseline Substitution Rule carries effectivity and authority; otherwise unresolved. One firmware release: unresolved; no decided root. One manufactured instance: identity unresolved. Lot effectivity and as-built content: not answerable inside EM-OPS-04. That gap is an acceptable scope cut only if stated; it is not coverage.

Invariants.

1. A product-type record is not an engineering definition and is not a serial.
2. A catalog item identity is not an SKU identity.
3. An SKU is party-scoped and does not identify a design revision.
4. An engineering revision versions a design definition, not a sellable SKU or a serial.
5. One Product record must not simultaneously be drawing, SKU and serial.
6. EBOM kind and version are mandatory and express intent only.
7. EBOM version is distinct from MBOM version; reuse of WM-OBJ-019 is not an MBOM.
8. A BOM line quantity without unit and basis is invalid.
9. A substitution requires effectivity and authority; absence does not imply interchangeability.
10. An alternate is not a silent BOM-line overwrite.
11. Variant is a configuration choice, not an engineering revision and not a party SKU.
12. Occurrence is distinct from catalog item, BOM line and serialized item.
13. Firmware release is not an Engineering Revision and not an EBOM line by default.
14. SBOM is a versioned BOM kind, not firmware-release identity.
15. As-built content and lot effectivity are derived only from Lot/Batch and Actual Transformation Event, never from BOM intent.
16. Production Work Order and actual events are the only authorities that bind a manufactured instance to consumed lots.
17. A party-scoped SKU may map to several engineering definitions; the map is not identity.
18. No identifier is allocated, so no new root may be named inside this proposal.

Minimum model set. Decided here: ProductType, EngineeringDefinition, EngineeringRevision (contained in WM-OBJ-018), PartyScopedSKU, EBOM (reuse of WM-OBJ-019, kind and version), BOMLine (quantity, unit, basis), SubstitutionRule (effectivity, authority). Still required, and missing or unassigned: Variant, Occurrence, FirmwareRelease, SBOM, MBOM/routing, SerializedItem, Lot/Batch, AsBuiltAssembly, ActualTransformationEvent, ProductionWorkOrder.

Blockers. (a) No resolution path from unassigned lot and actual events back to the contained revision without crossing mastership. (b) Firmware release and SBOM have no decided root. (c) Baseline containment of Substitution Rule does not name the effectivity-authority owner. (d) Reuse of WM-OBJ-019 must not imply EBOM equals MBOM. (e) WM-OBJ-018/019 contents are not invented; if they master item identity rather than versioned definitions, containment and reuse are rejected. (f) The test instance cannot be closed while actuals remain unassigned. No publication readiness is claimed.


## FILE candidate-allocation-offline-as-built-assembly/allocation-candidate.json
{"format":"vercy-model-allocation-candidate/v1","contourId":"EM-OPS-04","proposedName":"As-Built Assembly","modelId":null,"registryId":null,"allocationState":"unassigned","decision":"NEW MODEL","canonicalPublishable":false,"identityTest":{"stableIdentity":"An evidenced physical composition state remains identifiable independently of design intent, lots and serialized items.","versionIdentity":"Attach, detach, aggregation, disaggregation and transformation events append composition-state successors.","independentLifecycle":["initiated","assembled","verified","effective","modified","disassembled","superseded","closed"],"mastership":"authorized production and asset genealogy authority"},"boundary":{"owns":["as-built assembly identity","parent instance binding","time-bounded component memberships","actual quantities and locations","event-derived composition state","verification and evidence bindings","successor history"],"references":[{"target":"WM-OBJ-001","purpose":"Serialized physical item"},{"target":"WM-OBJ-019","purpose":"Design intent comparison"},{"target":"WM-MAT-008","purpose":"Observation evidence"},{"target":"WM-KNW-008","purpose":"Evidence citation"}],"excludes":["EBOM or MBOM intent","lot identity","component master","serialized item identity","firmware release","production authorization"]},"objects":{"AsBuiltAssembly":{"identity":["asBuiltAssemblyId"],"required":["parentItemRef","effectiveFrom","status"],"optional":["effectiveTo","supersedesRef"]},"ComponentMembership":{"identity":["asBuiltAssemblyId","membershipId"],"required":["componentRef","quantity","validFrom","sourceEventRef"],"optional":["validTo","locationRef"]}},"invariants":["Composition derives only from actual events.","BOM intent never proves installation.","Each membership identifies source event.","Quantities carry unit and basis.","Membership validity is time-bounded.","Attach and detach are explicit.","Alternates are not summed as installed.","Firmware binding uses installation evidence.","Corrections append successors.","Missing event evidence remains unknown."],"holds":["Registry allocation is pending and no identifier may be guessed.","Independent Grok review and one frozen semantic audit are pending.","Base specifications and approved relations remain incomplete.","Package conversion and live verification are pending."]}


## FILE candidate-allocation-offline-as-built-assembly/fixtures.json
{"format":"vercy-enterprise-allocation-fixtures/v1","candidateName":"As-Built Assembly","cases":[{"id":"attached-component","kind":"positive","input":"An attach event installs an approved alternate.","expect":"A membership opens with event evidence."},{"id":"detached-component","kind":"positive","input":"A detach event removes the component.","expect":"The membership closes without deletion."},{"id":"bom-as-built","kind":"negative","input":"An EBOM row is treated as installed composition.","expect":"The inference is rejected."},{"id":"silent-replacement","kind":"negative","input":"A component reference is overwritten without events.","expect":"The mutation is rejected."}]}


## FILE candidate-allocation-offline-as-built-assembly/validation-policy.json
{"format":"vercy-allocation-validation/v1","requirements":{"modelIdMustBeNull":true,"registryIdMustBeNull":true,"allocationState":"unassigned","minimumInvariants":8,"minimumReferences":3,"minimumFixtures":3,"requiresPositiveAndNegativeFixtures":true,"requiresStableIdentityStatement":true,"requiresIndependentLifecycle":true}}


## FILE candidate-allocation-offline-as-built-assembly/README.md
# EM-OPS-04: As-Built Assembly

Offline review package. Identifier allocation, publication and runtime registration remain pending.


## FILE candidate-allocation-offline-lot-batch/allocation-candidate.json
{"format":"vercy-model-allocation-candidate/v1","contourId":"EM-OPS-04","proposedName":"Lot / Batch","modelId":null,"registryId":null,"allocationState":"unassigned","decision":"NEW MODEL","canonicalPublishable":false,"identityTest":{"stableIdentity":"A produced or received bulk cohort remains identifiable independently of serialized members, product type and production order.","versionIdentity":"Corrections preserve the stable lot identity and append provenance assertions rather than reusing identifiers.","independentLifecycle":["created","released","quarantined","blocked","partiallyConsumed","exhausted","recalled","closed"],"mastership":"authorized inventory and production genealogy authority"},"boundary":{"owns":["lot identity","issuer-scoped lot identifiers","product and process context","quantity and unit history","production or receipt interval","membership and split/merge provenance","quality and disposition state"],"references":[{"target":"WM-OBJ-002","purpose":"Product type"},{"target":"WM-OBJ-001","purpose":"Serialized member"},{"target":"WM-OBJ-019","purpose":"BOM effectivity"},{"target":"WM-ACT-034","purpose":"Quality assessment"}],"excludes":["serialized item identity","product definition","work order","transformation event","as-built assembly","universal serial identity"]},"objects":{"Lot":{"identity":["lotId"],"required":["issuerRef","identifierSchemeRef","lotCode","productRef","status"],"optional":["producedInterval","quantity","parentLotRefs"]}},"invariants":["Lot codes are issuer and scheme scoped.","A lot is not a serialized instance.","Lot membership is provenance, not identity.","Quantities carry units.","Splits and merges preserve parent provenance.","Lot-based effectivity requires a resolvable lot.","Quality state is time-bounded.","Recall never deletes genealogy.","Identifiers are never reused.","Missing membership remains unknown."],"holds":["Registry allocation is pending and no identifier may be guessed.","Independent Grok review and one frozen semantic audit are pending.","Base specifications and approved relations remain incomplete.","Package conversion and live verification are pending."]}


## FILE candidate-allocation-offline-lot-batch/fixtures.json
{"format":"vercy-enterprise-allocation-fixtures/v1","candidateName":"Lot / Batch","cases":[{"id":"produced-lot","kind":"positive","input":"A batch is produced under one plan version.","expect":"Lot identity and production context remain stable."},{"id":"split","kind":"positive","input":"A lot is split into two child lots.","expect":"Parent provenance is retained."},{"id":"serial-collapse","kind":"negative","input":"The lot code is used as every item's serial.","expect":"The conflation is rejected."},{"id":"unresolved-effectivity","kind":"negative","input":"Lot-based substitution is applied without a lot master.","expect":"The application is rejected."}]}


## FILE candidate-allocation-offline-lot-batch/validation-policy.json
{"format":"vercy-allocation-validation/v1","requirements":{"modelIdMustBeNull":true,"registryIdMustBeNull":true,"allocationState":"unassigned","minimumInvariants":8,"minimumReferences":3,"minimumFixtures":3,"requiresPositiveAndNegativeFixtures":true,"requiresStableIdentityStatement":true,"requiresIndependentLifecycle":true}}


## FILE candidate-allocation-offline-lot-batch/README.md
# EM-OPS-04: Lot / Batch

Offline review package. Identifier allocation, publication and runtime registration remain pending.


## FILE candidate-allocation-offline-manufacturing-plan/allocation-candidate.json
{"format":"vercy-model-allocation-candidate/v1","contourId":"EM-OPS-04","proposedName":"MBOM / Manufacturing Plan","modelId":null,"registryId":null,"allocationState":"unassigned","decision":"NEW MODEL","canonicalPublishable":false,"identityTest":{"stableIdentity":"A governed production definition remains identifiable independently of engineering BOMs, work orders and actual transformations.","versionIdentity":"Routing, operation, plant applicability, material, scrap or yield changes create immutable successor versions.","independentLifecycle":["draft","reviewed","approved","released","effective","superseded","retired"],"mastership":"manufacturing engineering authority"},"boundary":{"owns":["manufacturing-plan identity","immutable MBOM versions","routing and operations","plant and line applicability","process-added material","scrap and yield assumptions","EBOM reconciliation mappings"],"references":[{"target":"WM-OBJ-018","purpose":"Engineering definition and revision"},{"target":"WM-OBJ-019","purpose":"EBOM baseline"},{"target":"WM-OBJ-002","purpose":"Product type"},{"target":"WM-REC-010","purpose":"Release decision"}],"excludes":["engineering BOM ownership","production order","actual consumption","lot identity","serialized item","as-built composition"]},"objects":{"ManufacturingPlan":{"identity":["manufacturingPlanId"],"required":["name","ownerRef","status"],"optional":["successorRef"]},"PlanVersion":{"identity":["manufacturingPlanId","version"],"required":["operations","applicability","validFrom","contentDigest"],"optional":["materialRules","yieldRules","ebomMappings","validTo"]}},"invariants":["Every plan states immutable version.","Routing and operation order are explicit.","Plant and line applicability are explicit.","Quantities carry unit and basis.","EBOM and MBOM remain separate masters.","Reconciliation is an evidenced mapping.","Plan material never proves actual consumption.","Yield and scrap remain assumptions until observed.","Published versions are immutable.","Retirement preserves historical production references."],"holds":["Registry allocation is pending and no identifier may be guessed.","Independent Grok review and one frozen semantic audit are pending.","Base specifications and approved relations remain incomplete.","Package conversion and live verification are pending."]}


## FILE candidate-allocation-offline-manufacturing-plan/profile-candidate.json
{"format":"vercy-enterprise-profile-candidate/v1","contourId":"EM-OPS-04","name":"Enterprise Product Engineering and Manufacturing","decision":"PROFILE","newRuntimeId":false,"bases":["WM-OBJ-002","WM-OBJ-017","WM-OBJ-018","WM-OBJ-019","WM-OBJ-001","WM-SFT-007","WM-SFT-008","WM-SFT-012"],"constraints":["Product type, design, revision, EBOM, serialized item, lot and as-built assembly remain distinct.","SKU is a party-scoped identifier and never a serial identity.","Engineering Revision and BOM Line remain owner-scoped members.","BOM intent never proves actual composition.","Firmware installation is an evidenced occurrence, not shared product identity."]}


## FILE candidate-allocation-offline-manufacturing-plan/fixtures.json
{"format":"vercy-enterprise-allocation-fixtures/v1","candidateName":"MBOM / Manufacturing Plan","cases":[{"id":"released-plan","kind":"positive","input":"A plant-specific route is released against an EBOM baseline.","expect":"The plan and mapping remain independently versioned."},{"id":"successor-route","kind":"positive","input":"An operation changes.","expect":"A successor version is appended."},{"id":"actual-consumption","kind":"negative","input":"Planned material is treated as consumed material.","expect":"The inference is rejected."},{"id":"ebom-overwrite","kind":"negative","input":"Manufacturing routing overwrites the EBOM.","expect":"The mutation is rejected."}]}


## FILE candidate-allocation-offline-manufacturing-plan/validation-policy.json
{"format":"vercy-allocation-validation/v1","requirements":{"modelIdMustBeNull":true,"registryIdMustBeNull":true,"allocationState":"unassigned","minimumInvariants":8,"minimumReferences":3,"minimumFixtures":3,"requiresPositiveAndNegativeFixtures":true,"requiresStableIdentityStatement":true,"requiresIndependentLifecycle":true}}


## FILE candidate-allocation-offline-manufacturing-plan/README.md
# EM-OPS-04: MBOM / Manufacturing Plan

Offline review package. Identifier allocation, publication and runtime registration remain pending.


## FILE candidate-allocation-offline-production-work-order/allocation-candidate.json
{"format":"vercy-model-allocation-candidate/v1","contourId":"EM-OPS-04","proposedName":"Production Work Order","modelId":null,"registryId":null,"allocationState":"unassigned","decision":"NEW MODEL","canonicalPublishable":false,"identityTest":{"stableIdentity":"A bounded authorization to manufacture a quantity under pinned definitions remains identifiable independently of plans and execution events.","versionIdentity":"Scope or authority changes create successor authorization revisions while preserving issued history.","independentLifecycle":["draft","released","scheduled","dispatched","inProgress","suspended","completed","closed","cancelled"],"mastership":"authorized production control authority"},"boundary":{"owns":["production-order identity","authorized product and quantity","pinned design and manufacturing-plan versions","site and time window","material reservation intent","acceptance criteria","authorization and status history"],"references":[{"target":"WM-OBJ-018","purpose":"Engineering revision"},{"target":"WM-OBJ-019","purpose":"EBOM baseline"},{"target":"WM-REC-010","purpose":"Authorization decision"},{"target":"WM-ORG-016","purpose":"Responsible assignment"}],"excludes":["actual transformation","actual consumption","lot identity","as-built composition","manufacturing-plan definition","inventory movement"]},"objects":{"ProductionWorkOrder":{"identity":["productionWorkOrderId"],"required":["productRef","quantity","planVersionRef","siteRef","decisionRef","status"],"optional":["designRevisionRef","scheduledWindow","acceptanceCriteria","supersedesRef"]}},"invariants":["An order pins product and quantity.","Quantity carries unit and basis.","Plan and design versions are pinned.","Authorization decision is explicit.","Site and scope are bounded.","Released or closed status never proves execution.","Reservations never prove consumption.","Completion requires external event evidence.","Cancellation preserves issued history.","Missing execution remains unknown."],"holds":["Registry allocation is pending and no identifier may be guessed.","Independent Grok review and one frozen semantic audit are pending.","Base specifications and approved relations remain incomplete.","Package conversion and live verification are pending."]}


## FILE candidate-allocation-offline-production-work-order/fixtures.json
{"format":"vercy-enterprise-allocation-fixtures/v1","candidateName":"Production Work Order","cases":[{"id":"released-order","kind":"positive","input":"An order authorizes 100 units under one plan version.","expect":"Authorization remains distinct from execution."},{"id":"completed-order","kind":"positive","input":"External events satisfy quantity and criteria.","expect":"Completion references execution evidence."},{"id":"closed-proof","kind":"negative","input":"Closed status is treated as production evidence.","expect":"The inference is rejected."},{"id":"floating-plan","kind":"negative","input":"An order references an unversioned plan.","expect":"The authorization is rejected."}]}


## FILE candidate-allocation-offline-production-work-order/validation-policy.json
{"format":"vercy-allocation-validation/v1","requirements":{"modelIdMustBeNull":true,"registryIdMustBeNull":true,"allocationState":"unassigned","minimumInvariants":8,"minimumReferences":3,"minimumFixtures":3,"requiresPositiveAndNegativeFixtures":true,"requiresStableIdentityStatement":true,"requiresIndependentLifecycle":true}}


## FILE candidate-allocation-offline-production-work-order/README.md
# EM-OPS-04: Production Work Order

Offline review package. Identifier allocation, publication and runtime registration remain pending.


## FILE candidate-allocation-offline-transformation-event/allocation-candidate.json
{"format":"vercy-model-allocation-candidate/v1","contourId":"EM-OPS-04","proposedName":"Actual Transformation Event","modelId":null,"registryId":null,"allocationState":"unassigned","decision":"NEW MODEL","canonicalPublishable":false,"identityTest":{"stableIdentity":"An actual material or assembly transformation occurrence remains identifiable independently of plans, work orders, lots and resulting items.","versionIdentity":"Corrections append attributable revisions while preserving the original occurrence and evidence.","independentLifecycle":["recorded","verified","accepted","rejected","corrected","voided","superseded","closed"],"mastership":"authorized production execution recorder"},"boundary":{"owns":["transformation-event identity","actual time and location","input and output quantities","consumption and production facts","agent and equipment bindings","process evidence","correction history"],"references":[{"target":"WM-OBJ-001","purpose":"Physical inputs and outputs"},{"target":"WM-OBJ-002","purpose":"Product types"},{"target":"WM-MAT-008","purpose":"Process observations"},{"target":"WM-KNW-008","purpose":"Evidence citation"}],"excludes":["manufacturing-plan definition","production authorization","lot master","item master","as-built projection","inventory balance"]},"objects":{"TransformationEvent":{"identity":["transformationEventId"],"required":["eventTime","locationRef","inputs","outputs","status"],"optional":["workOrderRef","agentRefs","equipmentRefs","evidenceRefs","supersedesRef"]}},"invariants":["Event identity is distinct from authorization.","Inputs and outputs are explicit.","Quantities carry unit and basis.","Actual time differs from planned time.","Consumption ends or reduces input state explicitly.","Outputs receive distinct identities or lot bindings.","Evidence is attributable.","Corrections append and never erase originals.","Plans never substitute for actual events.","Missing output evidence remains unknown."],"holds":["Registry allocation is pending and no identifier may be guessed.","Independent Grok review and one frozen semantic audit are pending.","Base specifications and approved relations remain incomplete.","Package conversion and live verification are pending."]}


## FILE candidate-allocation-offline-transformation-event/fixtures.json
{"format":"vercy-enterprise-allocation-fixtures/v1","candidateName":"Actual Transformation Event","cases":[{"id":"consume-produce","kind":"positive","input":"Material lots are consumed and a new lot produced.","expect":"Inputs, outputs and provenance are explicit."},{"id":"assembly","kind":"positive","input":"Components are aggregated into a serialized parent.","expect":"The event supports an as-built projection."},{"id":"planned-as-actual","kind":"negative","input":"Planned quantities are recorded as actual consumption.","expect":"The inference is rejected."},{"id":"overwrite","kind":"negative","input":"A correction overwrites the original event.","expect":"The mutation is rejected."}]}


## FILE candidate-allocation-offline-transformation-event/validation-policy.json
{"format":"vercy-allocation-validation/v1","requirements":{"modelIdMustBeNull":true,"registryIdMustBeNull":true,"allocationState":"unassigned","minimumInvariants":8,"minimumReferences":3,"minimumFixtures":3,"requiresPositiveAndNegativeFixtures":true,"requiresStableIdentityStatement":true,"requiresIndependentLifecycle":true}}


## FILE candidate-allocation-offline-transformation-event/README.md
# EM-OPS-04: Actual Transformation Event

Offline review package. Identifier allocation, publication and runtime registration remain pending.
