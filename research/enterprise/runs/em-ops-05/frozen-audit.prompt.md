# Frozen semantic audit — EM-OPS-05

You are the single final frozen semantic auditor. Use only the supplied dossier and artifacts. No tools, browsing, identifier invention, registry allocation, standards conformance claims, or publication-readiness claims. Do not request another provider study or rerun.

Adjudicated intent: keep Lot and Transformation Event as independent identifier-unassigned candidates; reuse WM-OBJ-020 Stock Position and WM-FLW-011 Shipment; reject Logistics Event as a root and split it across observation, movement, trace and fulfilment masters; keep Inventory–Genealogy as a thin declarative profile with no runtime ID. Check identity/mastership, required genealogy, partial consumption, balance derivation, correction events, shipment/delivery/acceptance separation, recall scope, effective/record/knowledge time, provenance, and zero-identifier/publication holds.

Return: (1) verdict; (2) numbered material defects in the submitted artifacts only, each with exact mechanical remediation text; (3) one exact JSON array of additional deterministic fixtures needed, each with id, target, kind, input, expect, violates, closesDefect; (4) freeze decision. Preserve valid prior fixtures, require expectedCode on every negative, and state the exact defect and fixture counts. Do not re-study the business boundary unless an artifact contradicts the reconciled decision.

## Local evidence

```
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

```

## Initial Claude study

```
# EM-OPS-05 — independent adjudication

## Verdict
Five candidates, five decisions. **StockPosition — reuse** WM-OBJ-020 unchanged. **Shipment — reuse** WM-FLW-011, constrained by its mandatory semantic kind. **LogisticsEvent — reuse, no single root**: it decomposes onto WM-FLW-004 observations, WM-FLW-012 stock transitions, WM-FLW-013 graph edges and WM-ECO-024 milestones; minting one generic logistics event would duplicate four masters. **Lot — new root required**, identifier unassigned. **TransformationEvent — new root required**, identifier unassigned. Plus a thin enterprise Inventory–Genealogy profile for cross-model bindings, also identifier-unassigned. No identifier allocated here.

## Evidence
All ten drafts are `publishableCanonical: false` / `reviewable-draft`. WM-OBJ-001 and WM-ECO-019 are dual-provider; WM-ECO-024, WM-OBJ-020, WM-FLW-004/011/012/013 and WM-ACT-007 are codex-only under the 2026-09-06 single-provider waiver, each with an absence-of-external-review hold. WM-ECO-024 maps `conceptual-candidate` to EM-OPS-05 at `index-and-publication-metadata` depth only. Relation review states are all `candidate`. Evidence therefore supports boundary adjudication, not conformance.

## Identity/mastership
Eleven identities stay separate and are already separately mastered: product type, configured variant, serial item (WM-OBJ-001), stock position (WM-OBJ-020), handling unit (WM-OBJ-021, referenced but absent from the dossier), inventory movement (WM-FLW-012), shipment/consignment (WM-FLW-011), goods movement plan and leg (WM-FLW-004), trace edge (WM-FLW-013), fulfilment obligation with receipt, inspection and acceptance assertions (WM-ECO-024), work order (WM-ACT-007). Lot and transformation event have no master. WM-OBJ-001 refuses batch, bulk and fungible matter and redirects to a sibling that does not exist.

## Lot/items/stock
Lot needs an independent root: its own identity (lot code under an issuer scheme), quantity and unit, expiry, status, and a lifecycle WM-OBJ-001 cannot carry — creation by transformation, split, merge, blend, quarantine, release, expiry, exhaustion, recall. Lot membership on a serial item is provenance, never instance identity; ISO 22095 mass balance and controlled blending break one-to-one continuity. StockPosition stays the quantity aggregate at a declared dimension grain and must not be decomposed into instances unless each is separately identified. Handling unit remains a third thing: scanning an SSCC creates no item and no lot.

## Transformation/genealogy
WM-FLW-012 owns one stock-affecting transition with source and destination; it carries no input/output set, no yield, no scrap. WM-FLW-013 composes transformation edges but declares event masters external and requires WM-ACT-015, which is unregistered here. WM-OBJ-001's `transform-item-identity` was adjudicated as evidentiary re-grounding, explicitly "rejected as node". So the authoritative actual transformation event is a genuine gap. The new root must bind: input lots and consumed quantities with units, output lots and serialized outputs, yield and scrap with basis, event and record time, place and read point, performing agent and authority, evidence digest, and correction lineage. Planned routing and BOM intent never substitute.

## Shipment/logistics/movement
WM-FLW-011 is reusable only with its kind discriminator declared (trade-shipment, transport-consignment or combined view) and its many-to-many allocation intact; split and consolidation cannot be forced into containment. Planned shipment (WM-FLW-011 plan plus WM-FLW-004 route and leg) stays distinct from actual movement (WM-FLW-012 posting reference, WM-FLW-004 observation) and from custody transfer (WM-FLW-004 handover, WM-FLW-013 custody interval). Handling-unit membership is typed, time-bounded membership, not ownership of the unit.

## Fulfilment/receipt/acceptance
WM-ECO-024 already holds the negative case: dispatched does not prove delivered, delivered does not prove intended-recipient receipt, receipt does not prove inspection, inspection does not prove acceptance, completion does not prove conformity or discharge. Reuse it for delivery receipt, inspection and acceptance assertions. Its inspection determination and conformity authority remain external and unnamed — record that as a missing neighbour, not as covered.

## Balance/corrections
The brief's event-derived balance and WM-OBJ-020's source-qualified snapshot are not the same construct; WM-OBJ-020 explicitly assumes no complete movement ledger. The enterprise profile must declare derivation mode per position: source snapshot, or projection over WM-FLW-012 postings plus explicit corrections within a closed completeness perimeter. Neither authorizes a posting. A missing row is unobserved, never zero; unknown, zero, not-applicable, withheld and suppressed stay distinct. Counts do not adjust stock; corrections append successors and never overwrite.

## Recall/impact
Proven affected units are reachable by event-backed consumption and output edges from the recalled lot through transformation to serialized outputs. Potentially affected units follow mass-balance, blended, inferred, stale or incomplete edges and each carries its reason. Units matching only by product type or BOM are not evidenced and cannot be declared unaffected absent a closed perimeter. Whole-SKU recall is refused: it substitutes classification for genealogy. Exposure sets are analysis; recall, alert and enforcement are authority decisions outside every model here.

## Time/quantity/provenance
Keep planned, promised, effective, event, observation, record, posting, ingestion, publication and correction times distinct, RFC 3339 with seconds and explicit offset. Every quantity states item scope, unit with pinned code-list version, precision and measurement basis; unit conversion is sourced, not inferred. Every assertion carries source system, asserting agent, method, confidence and evidence digest, and declared, observed and inferred edges never merge.

## Governance
Mastership: inventory steward for positions, posting authority for ledger effects, production authority for transformations, logistics steward for shipments, recipient authority for inspection and acceptance. Deny-by-default, purpose-bound access; lot, serial, route and recipient data are sensitive. Projections declare version pins and semantic loss. No model may allocate, dispatch, post, accept or recall on its own authority.

## Acceptance scenario
Raw lot L (new Lot root) is consumed by transformation T, which outputs serialized assemblies S1–S10 with lot-of-origin provenance on WM-OBJ-001, a co-product lot from a blended silo, and recorded scrap. WM-FLW-012 postings move outputs into positions; WM-OBJ-020 reflects the grain. Shipment SH (trade-shipment kind) carries handling units holding S1–S6; WM-ECO-024 records dispatch, then receipt of five units with one damage exception — S6 is dispatched but neither delivered nor accepted. Recall of L: S1–S10 are proven affected via T's output edges; S7–S10 are quarantined by a status-change movement; the blended co-product lot is potentially affected on mass-balance grounds; same-SKU units from other lots are not evidenced. The SKU is not recalled.

## Invariants
1. Genealogy edges cite an actual event plus evidence. 2. BOM or routing never establishes actual composition. 3. Plan ≠ movement ≠ posting ≠ acceptance. 4. Lot ≠ serial item ≠ handling unit ≠ position. 5. Every quantity carries unit and scope. 6. Absent row is unobserved. 7. Custody ≠ title; location ≠ custody. 8. Transformation preserves inputs, outputs, yield and scrap. 9. Inferred never becomes asserted. 10. Corrections append; identifiers are never reused. 11. Shipped ≠ delivered ≠ accepted. 12. Exposure analysis is not a recall decision.

## Holds
Lot, TransformationEvent, production work order, handling unit (WM-OBJ-021), as-built assembly (WM-OBJ-012), occurrence/event (WM-ACT-015) and the inspection authority are unallocated or absent here. Registry parent signals contradict specs for WM-OBJ-020→WM-OBJ-001, WM-FLW-012→WM-OBJ-020, WM-FLW-011/013→WM-FLW-004 and WM-ECO-019→WM-ECO-024 (CONTAINS versus COMPOSE); registry `entry_kind` disagrees with spec `entryKind` on four models — reconcile, do not overwrite. EPCIS 2.0 versus 2.0.1 and UBL 2.3 versus 2.4 pins diverge; WM-ACT-007 is maintenance-scoped with unresolved K11 duplication; WM-FLW-011/012/013 bundle descriptions carry "Route / Itinerary" template leakage. Crosswalks and fixtures are absent. No canonical completeness, installability or publication readiness is claimed.

```

## Exact Grok study

```
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

```

## Lot allocation

```
{"format":"vercy-model-allocation-candidate/v1","contourId":"EM-OPS-05","proposedName":"Lot","modelId":null,"registryId":null,"allocationState":"unassigned","decision":"NEW MODEL","canonicalPublishable":false,"identityTest":{"stableIdentity":"An issuer-qualified material lot remains identifiable across locations, stock positions, transformations, shipments and membership changes while its trace status evolves.","versionIdentity":"Corrections to attributes or status create append-only versions; split, merge or blend creates new related lots rather than rewriting the source lot.","independentLifecycle":["created","available","quarantined","released","partially-consumed","exhausted","expired","recalled","closed"],"mastership":"manufacturing or material-trace authority"},"boundary":{"owns":["persistent issuer-qualified lot identity","material or product definition reference","production or receipt origin","quantity basis and unit","quality, quarantine, release and expiry status","split, merge and blend lineage","recall and closure status","lot-to-item provenance membership"],"references":[{"target":"WM-OBJ-001","purpose":"Serialized physical-item identity"},{"target":"WM-OBJ-020","purpose":"Source-qualified stock position"},{"target":"WM-FLW-011","purpose":"Shipment or consignment"},{"target":"WM-FLW-013","purpose":"Supply trace edge"},{"target":"WM-ECO-024","purpose":"Dispatch, receipt, inspection and acceptance assertions"}],"excludes":["serialized item, handling unit or stock-position identity","transformation occurrence or work-order identity","movement, shipment or fulfilment milestone","custody, title or ownership","BOM, routing or planned composition","recall authority or inspection determination"]},"objects":{"Lot":{"identity":["issuerRef","lotId"],"required":["definitionRef","quantityBasis","unit","status"],"optional":["originRef","producedAt","expiresAt","successorRefs"],"lifecycle":["created","available","quarantined","released","partially-consumed","exhausted","expired","recalled","closed"]}},"invariants":["Lot identity is issuer-qualified and never inferred from SKU, location or stock position.","Lot, serialized item, handling unit and stock position retain separate identities.","Lot membership on an item is provenance and never becomes item identity.","Every lot quantity carries unit, basis and scope.","Split, merge and blend create explicit successor lots with lineage.","BOM and routing never prove actual lot composition.","Location never implies custody and custody never implies title.","Missing stock or genealogy rows are unobserved, never zero.","Quarantine, release, expiry, exhaustion and recall remain distinct states.","Recall analysis never creates recall authority.","Same-SKU membership never proves affectedness across unrelated lots.","Corrections append successors and lot identifiers are never reused."],"holds":["Registry allocation is pending and no identifier may be guessed.","Independent Grok review and one frozen semantic audit are pending.","Handling-unit, recall-authority and inspection boundaries require canonical resolution.","External trace crosswalks and fixtures remain pending."]}

```

## Lot fixtures

```
{"format":"vercy-enterprise-allocation-fixtures/v1","candidateName":"Lot","cases":[{"id":"split-lot","kind":"positive","input":"One raw lot is split into two successor lots.","expect":"Both successors receive distinct identities and cite the source lineage."},{"id":"serialized-membership","kind":"positive","input":"Ten serialized assemblies are produced from one lot.","expect":"Each item keeps its identity and references lot provenance."},{"id":"targeted-recall","kind":"positive","input":"One lot is affected while same-SKU units from other lots have no event-backed link.","expect":"Only proven or reason-coded potential descendants are included in exposure analysis."},{"id":"sku-is-lot","kind":"negative","input":"All units with one SKU are treated as the same lot.","expect":"The identity merge is rejected."},{"id":"stock-position-is-lot","kind":"negative","input":"A warehouse stock position is used as lot identity.","expect":"The inference is rejected."},{"id":"bom-proves-genealogy","kind":"negative","input":"BOM membership alone proves actual lot composition.","expect":"The claim is rejected."}]}

```

## Binding profile

```
{"format":"vercy-enterprise-profile-candidate/v1","contourId":"EM-OPS-05","name":"Enterprise Inventory and Genealogy Binding","decision":"PROFILE","newRuntimeId":false,"bases":["WM-OBJ-020","WM-FLW-011","WM-FLW-004","WM-FLW-012","WM-FLW-013","WM-ECO-024"],"constraints":["Stock Position reuses WM-OBJ-020 and declares snapshot or complete-ledger projection mode.","Shipment reuses WM-FLW-011 with an explicit trade-shipment, transport-consignment or combined kind.","Generic Logistics Event is split across observation, movement, trace and fulfilment masters.","Plan, movement, stock posting, custody transfer, receipt, inspection and acceptance remain distinct.","Every genealogy edge cites an actual transformation or movement event and evidence.","Corrections append successors; missing rows remain unobserved and counts never authorize adjustments."]}

```

## Lot validation policy

```
{"format":"vercy-allocation-validation/v1","requirements":{"modelIdMustBeNull":true,"registryIdMustBeNull":true,"allocationState":"unassigned","minimumInvariants":8,"minimumReferences":3,"minimumFixtures":3,"requiresPositiveAndNegativeFixtures":true,"requiresStableIdentityStatement":true,"requiresIndependentLifecycle":true}}

```

## Transformation allocation

```
{"format":"vercy-model-allocation-candidate/v1","contourId":"EM-OPS-05","proposedName":"Transformation Event","modelId":null,"registryId":null,"allocationState":"unassigned","decision":"NEW MODEL","canonicalPublishable":false,"identityTest":{"stableIdentity":"An actual material transformation occurrence remains identifiable independently of its work order, input/output lots, movements and later corrections.","versionIdentity":"Corrections append successor assertions for the same occurrence; a separate execution occurrence receives a new event identity.","independentLifecycle":["recorded","validated","corrected","superseded","voided","closed"],"mastership":"production execution or material genealogy authority"},"boundary":{"owns":["persistent transformation-occurrence identity","consumed input lots and quantities","produced lots and serialized items","yield, scrap and co-product quantities","unit and quantity bases","event time, record time and place","performing agent, authority and evidence","correction and supersession lineage"],"references":[{"target":"WM-OBJ-001","purpose":"Produced serialized-item identity"},{"target":"WM-OBJ-020","purpose":"Stock-position consequences"},{"target":"WM-FLW-012","purpose":"Inventory movement or posting"},{"target":"WM-FLW-013","purpose":"Derived supply-trace edges"},{"target":"WM-ACT-007","purpose":"Work-order reference with maintenance-only scope caveat"},{"target":"WM-ECO-024","purpose":"Fulfilment milestones and acceptance boundary"}],"excludes":["lot, item, stock position or handling-unit identity","BOM, routing, plan or work-order identity","movement, shipment, custody transfer or acceptance","recall decision or exposure authority","generic observation or trace-edge identity","inventory adjustment authority"]},"objects":{"TransformationEvent":{"identity":["transformationEventId"],"required":["inputs","outputs","eventTime","placeRef","performingAgentRef","evidenceDigest","status"],"optional":["workOrderRef","yield","scrap","coProducts","recordTime","authorityRef","supersedesRef"],"lifecycle":["recorded","validated","corrected","superseded","voided","closed"]}},"invariants":["Every event records explicit input and output sets with quantities, units and bases.","Transformation identity remains separate from work order, plan, movement and trace-edge identity.","Every genealogy edge cites the actual transformation event and evidence.","BOM and routing describe intent and never prove actual composition.","Yield, scrap and co-products remain explicit and reconcile under a declared method.","Event time and record time remain distinct.","Corrections append successors and preserve prior assertions.","Input consumption never silently transfers title or custody.","Output creation never proves stock posting, shipment, receipt or acceptance.","Inferred, mass-balance and stale edges remain labelled and never become asserted facts.","Missing inputs or outputs produce incomplete or indeterminate genealogy, never zero.","Exposure analysis follows event-backed edges but never exercises recall authority."],"holds":["Registry allocation is pending and no identifier may be guessed.","Independent Grok review and one frozen semantic audit are pending.","Production-work-order and generic occurrence boundaries require canonical allocation.","Mass-balance, unit conversion and external trace crosswalks remain pending."]}

```

## Transformation fixtures

```
{"format":"vercy-enterprise-allocation-fixtures/v1","candidateName":"Transformation Event","cases":[{"id":"raw-to-assemblies","kind":"positive","input":"Raw lot L is consumed to produce serialized items S1-S10, a blended co-product and scrap.","expect":"Inputs, outputs, yield, scrap, units, authority and evidence are captured under one event identity."},{"id":"corrected-quantity","kind":"positive","input":"A validated quantity is later corrected from 99 to 100 units.","expect":"A successor assertion preserves the original event record."},{"id":"partial-shipment-after-production","kind":"positive","input":"Six outputs are dispatched but only five are received.","expect":"Transformation, stock, shipment, receipt and acceptance remain separate."},{"id":"routing-proves-event","kind":"negative","input":"A routing plan is used as proof that the transformation occurred.","expect":"The claim is rejected."},{"id":"event-is-work-order","kind":"negative","input":"The production work order and actual execution share identity.","expect":"The identity merge is rejected."},{"id":"output-means-accepted","kind":"negative","input":"Produced output is treated as delivered and accepted.","expect":"Both inferences are rejected."}]}

```

## Transformation validation policy

```
{"format":"vercy-allocation-validation/v1","requirements":{"modelIdMustBeNull":true,"registryIdMustBeNull":true,"allocationState":"unassigned","minimumInvariants":8,"minimumReferences":3,"minimumFixtures":3,"requiresPositiveAndNegativeFixtures":true,"requiresStableIdentityStatement":true,"requiresIndependentLifecycle":true}}

```
