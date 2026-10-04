Verdict: Conditional accept of both candidates as non-roots. Allocate no identifier. Operations Landscape is accepted only as a governed declaration plus a projection that can be regenerated from already drafted masters and execution facts. Supply Network is accepted only as a scoped graph view over party, facility and supply-relation masters, not as a master and not as a root. Missing roots stay open and identifier-unassigned: Lot/Batch, Handling Unit, As-Built Assembly, Party/Supplier, Facility/Location, Supply Relationship, Transformation Plan, Actual Consumption/Production Event, and Occurrence/Event.

Strongest evidence: Completed drafts already cover physical items, product types, variants, engineering definitions and BOMs, inventory positions, goods and inventory movements, shipments, supply trace, work orders, and purchase/sales orders with fulfilment. The proposal reuses those drafts and refuses to promote a view or a declaration into an aggregate that could override evidence. The required separations (design versus actual, plan versus execution, serialized versus lot, stock versus movement, shipment versus consignment, custody versus title, movement versus posting, delivery versus acceptance) are the only way a recall can stay honest.

Strongest counterexample: A recalled component lot is design-eligible for a finished item under an engineering BOM, and an intermediate transformation sits at an unknown supplier. If the landscape projection or the network edge is allowed to stand in for an actual consumption event, the finished item is reported proven affected. That is false. Without a cited actual event, quantity, unit, time, location or explicit unknown, source, confidence and evidence, the item is not-evidenced. BOM membership is not composition.

Identity/mastership: No new root identity is created here. Landscape identity is the identity of a declaration (scope, version, effective time, owner, approval evidence), not of an item, lot, party or facility. Network identity is the identity of a scoped query result, not of a supply relation. Party, facility and supply-relation mastership remain outside this package and unassigned. Lot, handling unit, as-built assembly, transformation plan, and actual consumption/production and occurrence events likewise remain unassigned. Reuse does not confer an identifier.

Landscape/network: Landscape answers what is in governed operational scope and how the projection is regenerated. It may version and reproject; it may not rewrite execution. Network answers which parties and facilities are linked by supply relations under a stated scope. A network snapshot is not genealogy and must not invent edges absent from supply-relation masters or from actual movements. Neither is a root.

Design/BOM: Engineering definition, BOM and variant stay type-level design intent. They bound possible composition. They never prove that a particular lot or serial entered a particular assembly. An edge from component lot to finished item that cites only a BOM is rejected.

Transformations: A transformation plan is intent and remains identifier-unassigned. Actual composition is only an as-built assembly supported by actual consumption and production events, also unassigned. Plan quantity, plan location and plan supplier do not substitute for executed quantity, location and party. Where the intermediate event is missing, the chain stops and is marked incomplete.

Lots/inventory: Serialized item identity is not lot or bulk identity. Inventory position is stock at a time and place, not a movement and not a genealogy node. A recalled lot affects only positions and items that cite that lot through actual events. Handling unit remains unassigned, so packing is not treated as proof of contents.

Movements/delivery: Goods and inventory movement is distinct from inventory posting. Shipment is distinct from consignment. Custody is distinct from title. Delivery is distinct from acceptance. A shipment of a lot shows movement of custody or possession only to the extent the movement record says so; it does not prove the receiver accepted, took title, or consumed the lot into an assembly.

Trace/evidence: Every genealogy edge must cite an actual event, quantity and unit, time, location or capacity (or explicit unknown), source, confidence and evidence. Unknown origin and incomplete trace are first-class states, not empty fields. Supply trace in the existing draft is an evidence-bearing relation, not a new master.

Recall: Results partition only into proven affected, potentially affected, and not-evidenced. Proven requires an actual consumption or incorporation event citing the recalled lot, with quantity, unit, time and location or explicit unknown. Potentially affected is limited to items that share a scoped supply path or handling context where the linking event is partial. Not-evidenced covers BOM-only, plan-only, and any break at an unknown supplier. The unknown supplier break is exposed; it is not bridged.

Time/quantity/governance: Quantities without units are invalid on evidence edges. Time is mandatory; location or capacity is mandatory or explicitly unknown. Landscape governance is approval and reproducibility of the projection, not authority over posted stock or title. Effective time of a declaration does not backdate an execution event.

Scenario: Recalled component lot enters a candidate finished item only on the engineering BOM for that product type. The supplying party on the relevant tier is unknown, and no actual consumption event is on record. Work-order and purchase-order drafts show planned use, not execution. Result: finished item not-evidenced; any sibling lot of the same product type not-evidenced; no proven-affected set; unknown supplier break exposed; BOM edge rejected as composition proof. A second finished item with an actual consumption event citing the recalled lot, quantity, unit, time and location is proven affected to the consumed quantity only.

Invariants:

1. No genealogy edge without an actual event citation.
2. BOM or engineering definition never proves actual composition.
3. Supply Network is not a persistent root master.
4. Landscape projection is reproducible from the declaration plus cited sources.
5. Serialized identity is distinct from lot or bulk identity.
6. Stock position is distinct from movement.
7. Shipment is distinct from consignment; custody is distinct from title.
8. Movement is distinct from posting; delivery is distinct from acceptance.
9. Unknown origin and incomplete trace are explicit states.
10. Recall returns only proven, potentially affected, or not-evidenced.
11. Evidence edges carry quantity and unit, and time plus location or explicit unknown.
12. Plans and transformation plans do not substitute for execution events.
13. Neither candidate allocates an identifier to the unassigned set.
14. A network or landscape edge cannot close an unknown supplier break.

Minimum model set: Reuse product type, variant, engineering definition/BOM as intent, inventory position, goods and inventory movement, shipment, supply trace as evidence-bearing relation, work order, and purchase/sales order with fulfilment. No added identifiers. Unassigned concepts remain named gaps.

Blockers: Actual consumption/production event and occurrence identity are unassigned, so provenance cannot be closed inside this package. Lot/batch and as-built assembly identity are unassigned, so the recall test cannot name stable affected instances beyond what existing drafts already identify. Party, facility and supply relationship are unassigned, so the network view has no mastership home here. Until those gaps are assigned elsewhere, EM-LND-11 can declare and project, and can view, but cannot certify a complete genealogy. Not publication-ready; no identifier allocated.
