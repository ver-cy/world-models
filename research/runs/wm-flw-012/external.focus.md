# WM-FLW-012 bounded external research focus

Produce one complete schema-valid result for `WM-FLW-012 Inventory Movement`.

Treat the root as an event aggregate for one governed stock-affecting movement
that changes, or is expected to change, a stock position between inventory
locations, status buckets, owners or custodians. Distinguish a movement request,
order, reservation or warehouse task from the physical handling activity, its
observations, the authoritative inventory posting and the resulting stock
position. Keep planned, reserved, allocated, in-transit, executed, posted,
reconciled, reversed and corrected assertions independently typed.

Cover stable identity, namespace, revision and idempotency; movement type,
direction and reason; original, correction, reversal and successor lineage;
product, item, lot, batch, serial, handling-unit and inventory-position
references; quantity, unit, precision, tolerance and conversion basis; source
and destination warehouse, site, zone, bin, virtual location and stock bucket;
owner, custodian, availability, quality, quarantine and disposition changes;
order, reservation, warehouse-task, production, shipment, return and adjustment
triggers; planned, effective, event, posting, observation and record clocks;
authorization, segregation of duties and posting authority; execution evidence,
scans, counts, documents and event references; shortage, excess, damage,
mismatch, partial movement, split, merge and reconciliation; provenance,
quality, access, retention and loss-aware projections.

Keep the product or material, lot and serial, handling unit, warehouse and bin,
inventory stock position and balance, stock ledger, order and fulfilment,
production order, shipment or consignment, journey or route, chain-of-custody
trace, payment, valuation and accounting entry, generic observation, document,
incident and evidence as external masters. Do not conflate physical movement
with ledger posting, a request with an executed event, custody with ownership,
location with stock status, an inventory position with the event that changes
it, a count discrepancy with a movement, a shipment milestone with an inventory
receipt or issue, or a correction with destructive mutation of a prior event.

Review, but do not automatically approve, candidate parent `WM-OBJ-020
Inventory Stock Position`; an event that references and changes a position is
not necessarily contained by the position aggregate. Keep `WM-FLW-011 Shipment
/ Consignment` and `WM-FLW-013 Supply-chain Trace / Chain of Custody` as
boundary neighbors. Preserve missing canonical relation rows as a hold.

Target 6 bundles, 12 layers, 24 findings, 72 questions, 24 artifacts and 10
functions. Prefer GS1 EPCIS 2.0.1 and CBV 2.0; OASIS UBL 2.4 Inventory Report,
Despatch Advice and Receipt Advice; UN/CEFACT inventory movement code lists and
Buy-Ship-Pay semantics; ISA-95 / IEC 62264 manufacturing-operation boundaries;
UN/CEFACT Recommendation 20 units; RFC 3339; PROV-O; DQV and ODRL. Pin versions
or access dates and keep industry, jurisdiction, accounting, valuation,
dangerous-goods, safety, privacy, licensing and conformance limits explicit.

