Verdict: Conditional accept. Create identifier-unassigned Lot and Transformation Event roots. Reuse WM-OBJ-020 Stock Position and WM-FLW-011 Shipment. Do not create a Logistics Event root; split it across existing observation, movement, trace and fulfilment masters. Add only a thin Inventory–Genealogy binding profile. Allocate no identifier. Acceptance is conditional on the blockers below.

Five candidates. Lot: create, identifier unassigned. StockPosition: reuse WM-OBJ-020; do not extend it into lot identity or genealogy. TransformationEvent: create, identifier unassigned. Shipment: reuse WM-FLW-011 as plan or container, not as the movement ledger and not as acceptance. LogisticsEvent: reject as a root; split. Missing roots under this package: none. Serial item, handling unit, work order, shipment plan versus actual movement, custody transfer, receipt, inspection, acceptance, balance snapshot and correction event must stay separable and must not be collapsed into the five names. The binding profile is not a root.

Strongest evidence. Complete drafts already cover fulfilment and delivery, physical items, stock positions, goods movements, shipments, inventory movements, supply trace, work orders and purchase and sales orders. Reuse plus split avoids a second stock master and a second shipment master. Lot and transformation are not covered by those drafts as first-class concerns: lot is quantity-homogeneous identity, not a position; transformation is the irreversible multi-input, multi-output fact, not a work order and not a movement. The raw-lot to serialized-assembly to partial-ship to targeted-recall path cannot be stated if those two are reduced to stock or shipment.

Strongest counterexample. One raw lot is split across two transformations into serialized assemblies; only a subset is shipped; carrier custody has transferred but the customer has not accepted; a defect is later tied to part of the raw lot. If transformation is only a join of split logistics fragments, proven serials cannot be separated from potential co-mingled units, residual lot quantity is lost, a balance inferred from shipment status overstates available stock, and recall collapses to the SKU.

Identity and mastership. Lot and Transformation Event are new roots with no identifier allocated. They are not subtypes of WM-OBJ-020 or WM-FLW-011. Stock position is state at a place. Shipment is a logistics grouping. Observation, movement, trace and fulfilment remain the masters that absorb the former Logistics Event. The binding profile references those masters; it does not duplicate identifiers or states.

Lot, items and stock. Lot identity is distinct from serial item, handling unit, SKU and position. A position holds a quantity of a lot or of serials; it does not define them. Partial consumption leaves residual lot quantity traceable. Handling unit is a packaging identity, not a lot and not a position.

Transformation. A work order authorizes; it is not the event. Every transformation records inputs, outputs, quantities, units, yield, scrap, time, place, authority and evidence as one concern. Genealogy is many-to-many and survives later position changes.

Shipment and movement. Shipment plan is not actual movement and not custody transfer. Movement changes place or custody. Observation records a measured fact. Trace records lineage links. None of these is the transformation.

Fulfilment and acceptance. Shipped does not mean delivered, received, inspected or accepted. Receipt, inspection and acceptance are separate fulfilment facts. Partial shipment does not close the source lot or the unshipped serials.

Balance and corrections. Balances come only from a declared snapshot or a complete event ledger. A correction is an explicit compensating event. Silent overwrite is forbidden. Incomplete shipment status is not a balance.

Recall. Scope is proven affected units plus potential units that share the defective genealogy. It is not the SKU. The binding profile must be sufficient to compute both sets from transformation inputs and outputs and from residual quantities.

Time and provenance. Time and place are recorded on the event that occurred. Authority and evidence are attributes of that event, not inferred from a later status.

Governance. No identifier is allocated. Reuse of WM-OBJ-020 and WM-FLW-011 is a reference to named drafts, not a verification that those drafts already meet these constraints. This review does not claim publication readiness.

Scenario. Raw-material lot L is consumed by two transformations into serialized assemblies. Yield and scrap are recorded; residual L remains. A subset of serials is placed on a shipment plan and actually moved; custody transfers; acceptance has not occurred. A defect is tied to part of L. Proven serials are those whose input genealogy includes the defective portion. Potential units are residual L, unshipped serials from the same inputs, and co-mingled outputs not yet excluded by evidence. Unrelated serials of the same SKU are out of scope.

Invariants.

1. Lot ≠ serial item ≠ handling unit ≠ stock position ≠ work order.
2. A position holds quantity; it does not define lot or serial identity.
3. Transformation consumes inputs and produces outputs with quantities, units, yield and scrap.
4. Every transformation records genealogy, time, place, authority and evidence.
5. Genealogy is many-to-many and survives position change and partial consumption.
6. Residual lot quantity remains traceable.
7. Shipment plan ≠ actual movement ≠ custody transfer.
8. Shipped ≠ delivered ≠ received ≠ inspected ≠ accepted.
9. Balances derive only from declared snapshots or a complete event ledger.
10. Every correction is an explicit event; silent mutation is forbidden.
11. Recall scope is proven plus potential genealogy, not the SKU.
12. Partial shipment does not close the source lot or unshipped serials.
13. A work order authorizes transformation; it is not the transformation.
14. Evidence and authority belong to the event, not to a later status.
15. The binding profile references masters and adds no business-object master.

Minimum model set. Identifier-unassigned Lot root; identifier-unassigned Transformation Event root; reused WM-OBJ-020 Stock Position; reused WM-FLW-011 Shipment; existing observation, movement, trace and fulfilment masters in place of Logistics Event; thin Inventory–Genealogy binding profile. Separable, not newly rooted here: serial item, handling unit, work order, plan versus movement, custody, receipt, inspection, acceptance, snapshot, correction.

Blockers. Binding-profile ownership is underspecified: it must state what it may reference and what it must not own. Correction semantics are not yet a required event type. Reuse of WM-OBJ-020 and WM-FLW-011 is not verified against those drafts. Targeted recall is unsupported if transformation genealogy is optional. No identifier may be allocated to close these gaps.
