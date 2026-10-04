# Exact unsent Grok prompt — EM-OPS-04

Independent enterprise metamodel review. Do not browse, invent identifiers or claim publication readiness.

EM-OPS-04 covers ItemDefinition, SKU, EngineeringRevision, BillOfMaterials, BOMLine and SubstitutionRule. Complete drafts cover physical items, product types, variants, engineering definitions, EBOMs, software components/releases, SBOMs, work orders and traceability.

Assess this proposal: split ItemDefinition between product type and engineering definition; profile SKU as a party-scoped key; contain Engineering Revision in WM-OBJ-018; reuse WM-OBJ-019 for EBOM; contain BOM Line and Substitution Rule in a baseline. Leave MBOM/Manufacturing Plan, As-Built Assembly, Lot/Batch, Actual Transformation Event and Production Work Order unassigned. Allocate no identifier.

Separate catalog item, SKU, variant, engineering design/revision, EBOM, MBOM/routing, occurrence, substitution, firmware release, SBOM, serialized item, lot, as-built assembly and transformation evidence. BOMs require kind/version; quantities require units/basis; substitutions require effectivity and authority. Never let one Product record mean drawing, SKU and serial.

Test two design revisions, one alternate component, one firmware release and one manufactured instance. Resolve lot effectivity and as-built content only from authoritative lot and actual events, never BOM intent.

Return <=900 words with: Verdict; strongest evidence; strongest counterexample; identity/mastership; product/SKU; design/revision; EBOM/MBOM; lines/substitution/effectivity; firmware; instance/lot/as-built; time/quantity/provenance; governance; scenario; at least 10 invariants; minimum model set; blockers. Decide every candidate and missing root.
