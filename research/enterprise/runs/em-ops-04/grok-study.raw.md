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
