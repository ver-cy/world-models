# WM-FLW-011 bounded external research focus

Produce one complete schema-valid result for `WM-FLW-011 Shipment / Consignment`.

Treat the root as an aggregate family with a mandatory discriminator:
`trade-shipment`, `transport-consignment`, or `combined-logistics-view`.
UN/CEFACT and WCO distinguish a shipment as the trade or goods view of what is
shipped from seller or shipper to buyer or recipient, while a consignment is
the transport-contract view of how goods move from one consignor to one
consignee. Model their many-to-many allocation explicitly: a shipment may move
in several consignments and one consignment may consolidate all or part of
several shipments.

Cover stable identity and revision; commercial, transport, customs and carrier
identifiers; seller, buyer, shipper, consignor, consignee, carrier, freight
forwarder, transport-service buyer/provider, customs declarant and delivery
roles; goods and consignment items, quantities, classifications, marks and
declared values; packages, pieces, handling units and transport-equipment
bindings; origin, destination, receipt, acceptance, loading, transshipment,
unloading and delivery locations; requested services, modes, routes, journeys,
legs and schedules as references; planned, estimated, predicted, observed and
actual milestone clocks; delivery terms, handling instructions, dangerous
goods, temperature, security, regulatory and customs requirements; lifecycle
and status assertions; custody, responsibility and possession bindings;
exceptions, shortage, excess, damage, loss, delay, failed delivery, refusal,
return and claims references; weight, volume, count, dimensional and chargeable
measures; shipping instructions, waybill or bill of lading, packing list,
customs and certificate references; provenance, quality, access, retention,
licensing, reconciliation and loss-aware projections.

Keep goods and products, orders, fulfilment and delivery obligations, handling
units and containers, inventory movements, journeys and routes, services and
schedules, parties and locations, contracts, bookings, transport documents,
customs declarations, dangerous-goods master data, sensor observations,
generic events, chain-of-custody trace, incidents, insurance claims and evidence
as external masters. Do not conflate shipment with consignment, trade item with
consignment item, package with handling unit or transport equipment, custody
with ownership, transport status with inventory state, planned movement with
actual journey, milestone assertion with trace event, proof of delivery with
delivery obligation, or waybill with the goods or transport contract itself.

Review, but do not automatically approve, candidate parent `WM-FLW-004 Goods
Movement / Logistics`. Preserve candidate `CONTAINS WM-OBJ-021 Handling Unit /
Logistics Container` as a governed membership relation without importing the
handling-unit lifecycle. Preserve `REFERENCE WM-FLW-009 Journey / Trip` for
movement execution. Keep incoming `WM-ECO-024 Fulfilment / Delivery` as a
reference to physical delivery rather than ownership of fulfilment obligations.
Keep WM-FLW-012 Inventory Movement and WM-FLW-013 Supply-chain Trace / Chain of
Custody as boundary neighbors.

Target 6 bundles, 12 layers, 24 findings, 72 questions, 24 artifacts and 10
functions. Prefer current UN/CEFACT Buy-Ship-Pay, SCRDM, MMT and Integrated
Track and Trace material; WCO Data Model 4.1 guidance; OASIS UBL 2.4; GS1 EPCIS
2.0.1 and CBV 2.0; IATA ONE Record 3.2; DCSA Track and Trace; EU eFTI Regulation
2020/1056; UN/LOCODE; ISO 15459 where relevant; RFC 3339; PROV-O; DQV and ODRL.
Pin versions or access dates and keep mode, jurisdiction, dangerous-goods,
customs, trade, safety, privacy, licensing and conformance limits explicit.


