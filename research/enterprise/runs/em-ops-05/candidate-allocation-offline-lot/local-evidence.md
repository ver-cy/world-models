# EM-OPS-05 local synthesis

## Disposition

- Propose identifier-unassigned **Lot** and **Transformation Event** roots.
- Reuse WM-OBJ-020 for Stock Position.
- Reuse WM-FLW-011 for Shipment with its mandatory shipment/consignment kind.
- Split Logistics Event across WM-FLW-004 observations, WM-FLW-012 stock transitions, WM-FLW-013 trace edges and WM-ECO-024 fulfilment milestones; do not create a generic event root.
- Add only a thin Inventory–Genealogy binding profile; allocate no catalogue or runtime identifier.

## Identity and mastership

Lot, serialized item, handling unit, stock position, movement, shipment/consignment, goods-flow plan/leg, trace edge, fulfilment obligation and work order remain distinct.

Lot requires its own issuer-qualified identity and lifecycle: production, split, merge, blend, quarantine, release, expiry, exhaustion and recall. Lot membership on a serialized item is provenance, never item identity.

Transformation Event requires independent identity because existing movement and trace drafts do not own authoritative input/output sets, yield, scrap or execution evidence.

## Lot, items and stock

WM-OBJ-001 owns individuated serial items and explicitly excludes bulk/batch material. WM-OBJ-020 owns a source-qualified quantity at declared grain. A stock position does not decompose into instances unless each item is identified.

Handling Unit is separate from lot and item. Scanning a handling-unit identifier creates neither material nor ownership.

## Transformation and genealogy

Each Transformation Event pins consumed lots and quantities, produced lots and serial items, yield, scrap, units/bases, event and record times, place/read point, performing agent, authority, evidence digest and correction lineage.

Every genealogy edge cites the actual event and evidence. BOM and routing state intent only and never prove composition.

## Shipment, movement and logistics

Shipment reuse requires explicit kind: trade shipment, transport consignment or combined view. Split/consolidation preserves many-to-many allocations.

Planned route and shipment, actual movement, stock posting, custody transfer, delivery receipt and acceptance remain distinct. Handling-unit membership is time-bounded and does not imply title.

## Fulfilment and acceptance

WM-ECO-024 owns dispatch, receipt, inspection and acceptance assertions. Dispatch never proves delivery; delivery never proves intended-recipient receipt; receipt never proves inspection; inspection never proves acceptance or discharge.

Inspection determination and conformity authority remain external gaps.

## Balance and corrections

A source snapshot and an event-derived balance are distinct modes. Each stock position declares whether it comes from an authoritative snapshot or a projection over complete movement postings and corrections.

Missing rows are unobserved, never zero. Counts do not authorize adjustments. Corrections append successors and preserve prior states.

## Recall and impact

Proven affected items follow event-backed consumption/output edges. Potentially affected material follows blended, mass-balance, inferred, stale or incomplete edges with reason codes. Same-SKU or BOM-only matches are not evidenced.

Exposure analysis is not a recall decision. Recall authority remains external and a whole SKU is never recalled merely because one lot is affected.

## Acceptance result

Raw lot L is consumed by T, producing S1–S10, one blended co-product lot and scrap. Movements place outputs into stock. Shipment SH dispatches S1–S6; only five are received and one carries a damage exception, so S6 is not delivered or accepted. Recall analysis marks S1–S10 proven affected through T, the blended co-product potentially affected, and same-SKU units from other lots not evidenced. It never recalls the whole SKU automatically.

## Required invariants

1. Genealogy edges cite actual events and evidence.
2. BOM/routing never establishes actual composition.
3. Plan, movement, posting and acceptance remain distinct.
4. Lot, item, handling unit and stock position remain distinct.
5. Every quantity carries unit and scope.
6. Missing rows are unobserved.
7. Custody is not title; location is not custody.
8. Transformation records inputs, outputs, yield and scrap.
9. Inferred edges never become asserted facts.
10. Corrections append and identifiers are never reused.
11. Shipped, delivered and accepted remain distinct.
12. Exposure analysis is not recall authority.

## Holds

Lot, Transformation Event, production work order, handling unit, as-built assembly, occurrence/event and inspection authority remain unallocated or absent. Registry parent/containment signals conflict with model specifications. Registry/spec entry-kind axes are inconsistent. EPCIS and UBL pins diverge, WM-ACT-007 is maintenance-scoped, and flow drafts contain template leakage. Crosswalks, fixtures and independent review are absent. No installability or publication-readiness claim is made.


## Provider reconciliation and frozen audit

Grok independently upheld Lot and Transformation Event as identifier-unassigned roots, reused WM-OBJ-020 and WM-FLW-011, rejected Logistics Event as a root and kept Inventory–Genealogy as a thin profile. The sole frozen Claude audit preserved that decision and identified 35 mechanical artifact defects; all 35 are remediated without rerun. Its exact 51-case fixture array is retained, producing 63 cases with the twelve prior cases preserved and one moved to its correct profile scope. No catalogue, model, registry or runtime identifier is allocated, and no canonical publishability claim is made.
