# EM-LND-11 — Operations Landscape and Supply Network

## Verdict
**OperationsLandscape: accept as a governed declaration plus reproducible projection.** It gets local artifact identity only — scope, viewpoint, owner, pinned input revisions, as-of instant, completeness perimeter, disclosure policy, publication digest. No subject identity, no runtime/catalogue identifier allocated here.

**SupplyNetwork: reject as a stable subject root. Accept as a scoped network declaration realised as a graph projection** over party, facility and supply-relation masters, hosted inside the OperationsLandscape declaration. Its nodes (supplier party, facility) and its edges (sourcing relationship) are not mastered anywhere in the frozen dossier; promoting it to a root would mint a second master for supplier identity — exactly the failure WM-OBJ-001 forbids for asset, stock, passport and shell records.

## Evidence
Fourteen drafts, all `publishableCanonical: false`. WM-OBJ-001 and WM-OBJ-002 are dual-provider; WM-ECO-019 dual-provider; WM-ECO-020 Claude-only waiver; WM-OBJ-017/018/019/020, WM-FLW-004/011/012/013, WM-ACT-007, WM-ECO-024 are Codex single-provider waivers with visible absence-of-external-review holds. Prior boundary work (EM-LND-12, EM-LND-13, EM-LND-17) already settled that a landscape is a named, tenant-scoped, time-stamped projection with artifact identity, and that a second dependency/lineage graph is rejected when edge semantics are already owned. This adjudication follows that precedent.

## Identity/mastership
Distinct identities, each with one owner: product type (WM-OBJ-002, classifier), variant (WM-OBJ-017), design (WM-OBJ-018, informational), engineering BOM revision and occurrence (WM-OBJ-019), serialized item (WM-OBJ-001, entity), stock position (WM-OBJ-020), inventory movement (WM-FLW-012, event), shipment/consignment with mandatory semantic kind (WM-FLW-011), goods-movement flow (WM-FLW-004), trace graph/result (WM-FLW-013, pattern), work order (WM-ACT-007), purchase order (WM-ECO-019), sales order (WM-ECO-020), fulfilment case (WM-ECO-024). **Unmastered and required: lot/batch, handling unit, as-built assembly, occurrence/event, party/supplier, facility/location, supply relationship, transformation plan, actual consumption/production event.**

## Landscape/network
OperationsLandscape declares: viewpoint and stakeholder concerns; scope over supply, transformation, inventory and delivery flows; time horizon; traceability policy; scenario code; pinned source revisions; completeness perimeter; freshness policy; projection and disclosure policy. Every view answers as-of a stated instant and records rule version and trace so it regenerates identically. SupplyNetwork is one such view: parties, facilities and supply relations with validity intervals, determination method, evidence and confidence. Absence of an edge means unobserved unless a closed, versioned perimeter licenses an absence claim.

## Product/design/BOM
Product type classifies instances; variant classifies configured instances; design realises requirements; BOM composes component types. All four are intent, not composition fact. WM-OBJ-019 states the rule directly: engineering occurrence is not a serialized item, candidate alternate lines do not imply installed components, and a nominal aggregate is not a measured property. Registry direction is contradictory — `parent_ids: WM-OBJ-002` for WM-OBJ-019 against relation row `WM-OBJ-019 COMPOSE WM-OBJ-002`; unresolved.

## Work/transform events
WM-ACT-007 authorizes work and explicitly never proves that work occurred; completion is an external claim evaluated against issued acceptance criteria. Its purpose is upkeep of assets (legacy K11 maintenance-and-repair), so a **production/transformation work order and its routing/manufacturing plan are missing**, as is the actual consumption/production event. EPCIS TransformationEvent appears only as an alignment on WM-OBJ-001, WM-FLW-012 and WM-FLW-013 — an alignment cannot serve as the genealogy master.

## Lots/items/inventory
WM-OBJ-001 refuses instance identity to matter without an individuating boundary and redirects batch, bulk and fungible material to a sibling model that does not exist in this dossier. It records lot membership as provenance, never identity. WM-OBJ-020 owns quantity by dimension tuple, declares that a missing row is not zero, and forbids treating a count as authority to post. WM-FLW-012 owns one stock-affecting transition and holds the authoritative posting as an external reference.

## Movements/shipment/delivery
WM-FLW-011 requires a trade-shipment / transport-consignment / combined-view discriminator and supports many-to-many shipment↔consignment allocation; handling-unit CONTAINS is typed membership only. WM-FLW-004 owns plan, route, leg, custody and observation, and refuses to infer custody, delivery acceptance or clearance from a scan or status code. WM-ECO-024 keeps dispatch, handover, receipt, inspection, acceptance and completion on separate axes. Plan is never movement; movement is never posting; posting is never acceptance.

## Traceability/evidence
Every genealogy edge must carry: relation type (aggregation, disaggregation, transformation, custody), the citing actual event, quantity with unit, event time plus record/ingestion time, read point and business location, capacity or yield where applicable, source system and asserting agent, determination method, confidence, and evidence digest. Declared, observed and inferred edges stay distinguishable; an inferred edge never becomes an asserted fact. ISO 22095 mass balance and controlled blending explicitly break one-to-one identity, so a custody claim is not instance continuity.

## Recall/impact
For a recalled component lot: **proven affected** = outputs reachable by transformation or aggregation edges citing actual consumption events with quantity, unit, time and location, plus verified evidence digests. **Potentially affected** = outputs produced while the lot occupied the consuming position, or reached only through mass-balance/blending, inferred or stale edges, or unserialised bulk — classified with the reason code. **Not evidenced** = outputs whose BOM cites the component type with no event tying this lot; this is not "unaffected", which requires a closed completeness perimeter. The **unknown supplier break** appears where the inbound lot has no resolvable party master: the backward trace terminates at an explicit unknown-origin marker, the sibling-lot question is unanswerable, and the result is returned as incomplete with residual uncertainty. Recall, alert and enforcement decisions stay with accountable authorities.

## Time/quantity/provenance
Event, effective, observation, record, posting, ingestion, publication and correction times are separate, RFC 3339 with seconds and explicit offset. Quantity always carries item scope, unit with pinned code-list version, precision and measurement basis. Unknown, zero, not-applicable, withheld and suppressed remain distinct values. Corrections append linked successors; issued revisions are immutable.

## Governance
One owning Dimension per fact; unknown mastership blocks mutation. Deny-by-default disclosure with purpose-bound minimum projections; withheld segments marked withheld, never absent. Retention, legal hold, tombstoning and disposition execute in the adopting Dimension's records model. Landscape views never mutate sources and never execute allocation, dispatch, posting, acceptance or recall.

## Acceptance scenario
Recalled lot L of component type C. Trace returns: three serialized units with cited TransformationEvent consumption edges (quantity, unit, time, work centre, evidence) → **proven affected**. Two bulk output lots produced from a blended silo during L's residency → **potentially affected**, reason mass-balance. Forty units whose BOM lists C but for which no consumption event exists → **not evidenced**, not cleared. Inbound L came from a supplier with no party master → unknown-origin marker; upstream sibling lots unresolved; result flagged incomplete. Negative case fails as required: the BOM alone proves nothing.

## Invariants
1. Genealogy edges cite actual events with evidence. 2. Plan is not movement; movement is not posting; posting is not acceptance. 3. BOM never establishes actual lot composition. 4. Unknown origin and incomplete trace are explicit first-class states. 5. Absence of an edge implies non-exposure only inside a closed declared perimeter. 6. Custody is not title; location is not custody. 7. Every quantity carries unit and item scope. 8. Inferred edges never masquerade as asserted. 9. Landscape views declare viewpoint, scope, as-of, freshness, completeness and policy. 10. Retired identifiers stay resolvable and are never reused.

## Minimal model set
Reuse all fourteen drafts as-is. Add, as identifier-unassigned candidates requiring registry reservation and boundary review: **Lot/Batch**, **Handling Unit**, **As-Built Assembly**, **Party/Supplier**, **Facility/Location**, **Supply Relationship**, **Transformation Plan (routing/manufacturing BOM)**, **Actual Consumption/Production Event**, **Occurrence/Event**. OperationsLandscape is a declaration artifact; SupplyNetwork is a view definition within it.

## Holds
No canonical completeness, installability or publication readiness is claimed. All bases are reviewable drafts; ten carry single-provider waivers. Registry `entry_kind` (standalone-mm) conflicts with specification entry kinds (aggregate, event, pattern) across most entries. Parent signals for WM-FLW-011/012/013, WM-ECO-024, WM-OBJ-019 and WM-OBJ-020 are candidate only and contradict their specs. WM-ACT-007 is maintenance-scoped and carries an unresolved K11 duplication. External pins diverge: EPCIS 2.0 vs 2.0.1 (with a URL/PDF label mismatch), CBV 2.0 vs 2.0.0, UBL 2.3 vs 2.4. No fixtures were run; no crosswalk was validated; no identifiers were allocated.
