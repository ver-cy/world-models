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
