# EM-LND-11 local synthesis

## Disposition

- Treat **Operations Landscape** as a governed declaration plus reproducible, exception-aware projection.
- Treat **Supply Network** as a scoped graph declaration/view over party, facility and supply-relation masters, not a subject root.
- Reuse current product, design, BOM, asset, stock, movement, shipment, trace, work-order, order and delivery drafts without allocating IDs.
- Record identifier-unassigned gaps for Lot/Batch, Handling Unit, As-Built Assembly, Party/Supplier, Facility/Location, Supply Relationship, Transformation Plan, Actual Consumption/Production Event and Occurrence/Event.
- Allocate no catalogue or runtime identifier.

## Identity and mastership

Product type, variant, design, engineering BOM, serialized item, stock position, inventory movement, shipment/consignment, goods flow, trace graph, work order, purchase order, sales order and fulfilment retain separate identities and masters.

Operations Landscape owns only viewpoint, scope, pinned source revisions, as-of time, completeness perimeter, freshness and disclosure policy, projection digest and gap/conflict register. It never mutates sources.

Supply Network is one landscape view. Its nodes and edges carry validity, determination method, evidence and confidence. It cannot master supplier identity or supply relationships. Missing edges mean unobserved unless a closed, versioned perimeter authorizes an absence claim.

## Product, design and BOM

Product type and variant classify instances; design and engineering BOM state intended structure. Engineering occurrences, candidate alternates and nominal aggregates do not prove installed components, serialized identity or measured properties.

BOM is never evidence of actual lot composition. Actual genealogy requires events that consumed, transformed, aggregated, disaggregated or produced material.

## Work and transformation

WM-ACT-007 authorizes maintenance work and does not prove execution. A production/transformation work order and routing/manufacturing plan are missing, as is the authoritative actual consumption/production event. External EPCIS alignment cannot substitute for an allocated master.

Plan, movement, posting, custody transfer, receipt, inspection and acceptance remain distinct events or assertions.

## Lots, items and inventory

WM-OBJ-001 owns individuated physical items and explicitly redirects batch, bulk and fungible material to a missing sibling model. Lot membership is provenance, not instance identity.

WM-OBJ-020 owns quantity by dimension tuple. Missing rows are not zero and stock counts do not authorize postings. Handling units and as-built assemblies need their own lifecycle boundaries before allocation.

## Movements, shipment and delivery

Shipment and transport consignment remain distinguished and may relate many-to-many. Goods movement owns plan, route, leg, custody and observation but does not infer custody, delivery acceptance or clearance from scans. Fulfilment keeps dispatch, handover, receipt, inspection, acceptance and completion on separate axes.

## Traceability and evidence

Every genealogy edge states relation type, cited actual event, quantity/unit, event and record times, location/read point, capacity or yield, source, asserting agent, determination method, confidence and evidence digest.

Declared, observed and inferred edges remain distinct. Mass balance and controlled blending break one-to-one continuity. Unknown origin, withheld data and incomplete trace are first-class states.

## Recall and impact

Proven affected items require event-backed consumption/transformation edges. Potentially affected items follow mass-balance, blending, stale, inferred or incomplete edges and carry a reason. BOM-only matches are not evidenced and cannot be called unaffected without a closed completeness perimeter.

An unresolved supplier terminates backward tracing at an explicit unknown-origin marker and preserves residual uncertainty. Recall and enforcement remain authority decisions outside the landscape.

## Time, quantity and governance

Event, effective, observation, record, posting, ingestion, publication and correction times remain distinct. Quantities state scope, unit, code-list version, precision and measurement basis. Unknown, zero, not applicable, withheld and suppressed never collapse.

Corrections append successors. Access is deny-by-default and purpose-bound. Landscape views cannot allocate, dispatch, post, accept or recall.

## Acceptance result

Recalled component lot L yields three serialized units with event-backed consumption edges: proven affected. Two bulk output lots from a blended silo are potentially affected with mass-balance reason. Forty units whose BOM lists the component but lack consumption events are not evidenced. L's inbound supplier cannot resolve to a party master, so the upstream trace ends with unknown origin and the result remains incomplete.

## Required invariants

1. Genealogy edges cite actual events and evidence.
2. Plan is not movement; movement is not posting; posting is not acceptance.
3. BOM never establishes actual lot composition.
4. Unknown origin and incomplete trace are explicit.
5. Absence proves non-exposure only inside a closed completeness perimeter.
6. Custody is not title; location is not custody.
7. Every quantity carries unit and item scope.
8. Inferred edges never become asserted facts.
9. Views declare viewpoint, scope, as-of, freshness, completeness and policy.
10. Corrections append lineage and identifiers are never reused.

## Holds

Nine required subject/event boundaries remain unallocated. Registry parent signals for shipment, movement, trace, fulfilment, BOM and stock conflict with their specs. WM-ACT-007 is maintenance-scoped and has an unresolved legacy duplication. EPCIS, CBV and UBL pins diverge. Most drafts are single-provider and all are non-canonical; crosswalks are absent and fixtures are specified but not executed. No installability or publication-readiness claim is made.

## Grok reconciliation and frozen audit

Grok confirmed both candidates as non-roots. Proven-affected quantity is bounded by the cited consumed quantity; a network or landscape edge cannot close an unknown-origin break. The single frozen audit found D1-D30 and all deterministic remediations were applied. Final suite: 119 cases (32 positive, 87 negative).
