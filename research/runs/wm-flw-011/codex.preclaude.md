# Codex pre-provider hypothesis for WM-FLW-011

## Boundary

Shipment / Consignment should be an aggregate family only for cross-domain
discovery. Every instance needs a mandatory trade-shipment,
transport-consignment or combined-logistics-view discriminator. The first owns
the seller-to-buyer goods grouping; the second owns the consignor-to-consignee
grouping under one transport-service contract. Their allocation is many-to-many.

Goods, orders, fulfilment obligations, handling units, inventory movements,
journeys, routes, services, parties, locations, documents, declarations,
dangerous-goods masters, events, trace, sensors, incidents, claims and evidence
remain external masters.

## Proposed structure

1. Identity, semantic kind and commercial/transport boundary.
2. Items, packages and logistics composition.
3. Locations, movement plan and service bindings.
4. Requirements, milestones and condition.
5. Responsibility, exceptions and measures.
6. Documents, provenance, access and interoperability.

Each bundle should contain two layers and four findings. Each finding should
ask three model-specific questions and define one data element and one serial
evidence artifact. Ten functions should register, allocate shipment and
consignment, compose items, bind handling units, bind locations and movement,
apply service/compliance requirements, record milestone assertions, record
exceptions, reconcile measures/documents and project.

## Expected hard points

- UN/CEFACT and WCO distinguish trade shipment from transport consignment.
- Containment of handling units is membership only; unit identity and lifecycle
  remain in WM-OBJ-021.
- Movement execution stays in WM-FLW-009 and generic trace or chain of custody
  stays in WM-FLW-013.
- Status reports, EPCIS events and sensor observations are evidence; they do not
  silently overwrite shipment or consignment master assertions.
- Modal, customs, dangerous-goods and jurisdiction profiles require separate
  validation and exact source-version pins.
