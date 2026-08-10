# F3 Goods Movement & Logistics

This meta-model describes the physical movement of goods across space and across hands: shipments and their cargo, planned routes decomposed into transport legs, the vehicles and vessels that perform them, the chain of custody from dispatch to delivery, and the clearance and tracking events along the way. It is its own model because movement semantics, who has the goods, where they are, and what happened en route, are independent of what the goods are worth or who ultimately owns them.

## Manifest

```yaml
muif:
  version: "1.0"
metaModel:
  id: "vercy:world:f3"
  csn: world.goodsMovement
  version: 0.2.0
  displayName: Goods Movement & Logistics
  description: Shipments, routes, transport legs, custody chains and tracking of physical goods.
conformance:
  muc: "2.0: Conformant"
  mmas: A1
namespaces:
  - world.goodsMovement
bundles:
  - csn: world.goodsMovement.consignment
    displayName: Consignment
    layers:
      - world.goodsMovement.consignment.shipmentAndCargo
      - world.goodsMovement.consignment.packagingHierarchy
  - csn: world.goodsMovement.routing
    displayName: Routing
    layers:
      - world.goodsMovement.routing.routePlan
      - world.goodsMovement.routing.transportLegs
  - csn: world.goodsMovement.custody
    displayName: Custody
    layers:
      - world.goodsMovement.custody.custodyChain
      - world.goodsMovement.custody.borderAndClearance
  - csn: world.goodsMovement.visibility
    displayName: Visibility
    layers:
      - world.goodsMovement.visibility.trackingEvents
      - world.goodsMovement.visibility.exceptionsAndDelays
imports:
  - source: un-cefact
    version: "*"
  - source: gs1-epcis
    version: "*"
  - source: wco-hs
    version: "*"
```

## Bundles and layers

| Bundle | Responsibility | Layers |
|---|---|---|
| `consignment` | What moves | `shipmentAndCargo`: shipments and the cargo items they carry · `packagingHierarchy`: pallets, containers and package units nesting cargo |
| `routing` | How it moves | `routePlan`: the intended origin-to-destination plan · `transportLegs`: ordered legs, modes and the means performing them |
| `custody` | Who has it | `custodyChain`: handovers of physical responsibility along the route · `borderAndClearance`: authorizations required to cross regulatory boundaries |
| `visibility` | What happened | `trackingEvents`: observed milestones tied to shipments and legs · `exceptionsAndDelays`: deviations from plan and their resolution |

## Objects

- `shipment`: a consignment moving under one transport arrangement; key attributes: shipmentId, incotermRef, declaredValue, status.
- `cargoItem`: a line of goods within a shipment; key attributes: description, commodityCode, quantity, weight.
- `packageUnit`: a physical packing unit (box, pallet, container); key attributes: unitType, identifier, sealNumber.
- `routePlan`: the planned path of a shipment; key attributes: origin, destination, plannedDepartureTime, plannedArrivalTime.
- `transportLeg`: one segment of a route under a single mode and carrier; key attributes: mode, sequence, fromLocation, toLocation.
- `transportMeans`: the vehicle, vessel, aircraft or wagon performing legs; key attributes: meansType, identifier, capacity.
- `custodyTransfer`: a handover of physical responsibility for a shipment; key attributes: fromCustodianRef, toCustodianRef, occurredAt, evidenceRef.
- `clearanceRecord`: an authorization to move goods across a regulatory boundary; key attributes: boundaryType, status, grantedAt.

## Relationships

- `shipment` -> contains -> `cargoItem` (1:n): the goods lines of a consignment.
- `cargoItem` -> packedIn -> `packageUnit` (n:1): the physical unit carrying an item.
- `shipment` -> follows -> `routePlan` (n:1): the plan a shipment executes.
- `routePlan` -> comprises -> `transportLeg` (1:n): ordered decomposition into legs.
- `transportLeg` -> performedBy -> `transportMeans` (n:1): the means executing a leg.
- `custodyTransfer` -> handsOver -> `shipment` (n:1): the shipment changing hands.
- `clearanceRecord` -> authorizes -> `transportLeg` (n:1): the boundary crossing a clearance permits.

## Events

- `shipmentDispatched`: a shipment left its origin and entered the custody chain.
- `legDeparted`: a transport leg began.
- `legArrived`: a transport leg completed at its destination location.
- `custodyTransferred`: physical responsibility passed from one custodian to another.
- `clearanceGranted`: a regulatory boundary crossing was authorized.
- `exceptionRaised`: a deviation (damage, delay, loss, misroute) was recorded against a shipment or leg.
- `shipmentDelivered`: the shipment reached its consignee and the custody chain closed.

## Contracts

- `shipmentTrackingAccess`: consignor, consignee or their delegates read tracking events for a named shipment.
- `custodyChainAudit`: an authorized party verifies the complete, ordered custody record of a shipment.
- `tradeFlowStatistics`: a consumer receives commodity-level flow aggregates with parties and shipments anonymized.

## Projections

- `consigneeTrackingView`: current status and milestone history of one's own inbound shipments; omits carrier internals and other customers.
- `carrierOperationsView`: legs, means and exceptions for a carrier's own operations; omits cargo commercial detail.
- `tradeFlowAggregate`: origin-destination commodity volumes per period; omits all shipment-level identity.

## Composition

- COMPOSE `world.money` (F2): declared values and freight charges embed the money value object.
- REFERENCE `world.organization` (O1): shippers, carriers and terminal operators are organizations resolved by reference.
- REFERENCE `world.passengerMobility` (F7): freight and passenger services share corridors, terminals and multimodal infrastructure.
- The `custody` bundle is designed as an EXTEND point: `world.waterFoodSupply` (F4) and `world.wasteFlow` (F5) specialize its custody chain for their regulated consignments.
- imports: UN/CEFACT (ALIGN): field equivalences with multimodal transport reference semantics.
- imports: GS1 EPCIS (ALIGN): event vocabulary equivalences for object tracking (what, where, when, why).
- imports: WCO HS (REFERENCE): externally governed commodity classification of cargo items.

## Stewardship

The shipper stewards the shipment record, and each carrier stewards the legs and custody segments it performs, so stewardship follows the custody chain leg by leg. Access is granted per record by its steward through the catalogue's S1/S2 ownership and access models, with custody audits recorded via S4.
