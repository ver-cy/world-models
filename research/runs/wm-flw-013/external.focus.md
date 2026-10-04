# WM-FLW-013 bounded external research focus

Produce one complete schema-valid result for `WM-FLW-013 Supply-chain Trace /
Chain of Custody`.

Treat the root as a reusable cross-organizational traceability pattern that
links independently mastered traceable-object identities, lifecycle events,
custody assertions, transformations, aggregations, locations, parties and
evidence into a governed time-aware trace graph. Distinguish the persistent
event/provenance graph, a query or trace request, a versioned result or
snapshot, a chain-of-custody claim and a recall or exposure analysis. A trace
records qualified assertions and gaps; it does not make every assertion true.

Cover trace identity, scope and revision; traceable objects, lots, serials,
handling units, shipments and identifiers; aggregation and disaggregation;
input-output transformation; critical tracking events and key data elements;
event, effective, observation, record, ingestion and correction clocks;
business step, disposition, read point, business location, source and
destination; party, role, custody, possession, control, responsibility and
ownership distinctions; handover intervals and acknowledgements; authoritative
source, evidence, integrity, signature, credential, confidence and quality;
duplicates, gaps, conflicts, error declarations, retractions and successors;
backward trace, forward trace, exposure, recall and provenance queries;
federated discovery and access; retention, privacy, confidentiality and audit;
physical segregation, controlled blending, mass balance and book-and-claim
chain-of-custody profiles; loss-aware standards projections.

Keep product, material, lot, serial, handling unit, shipment, consignment,
inventory movement, journey, location, party, event, observation, custody
handover, document, credential, incident, recall action, claim and evidence as
external masters. Do not conflate chain of custody with mere location history,
traceability with tracking, custody with ownership, event assertion with
verified fact, aggregation with transformation, physical flow with book-and-
claim attribution, trace result with the underlying graph, a document hash with
proof of its content, or recall scope with a recall decision.

Review, but do not automatically approve, candidate parent `WM-FLW-004 Goods
Movement / Logistics`. Review candidate `COMPOSE WM-ACT-015 Occurrence / Event`
as typed event composition only; generic event identity and lifecycle remain
external. Keep `WM-FLW-011 Shipment / Consignment` and `WM-FLW-012 Inventory
Movement` as boundary neighbors. Preserve missing or candidate canonical
relations as holds.

Target 6 bundles, 12 layers, 24 findings, 72 questions, 24 artifacts and 10
functions. Prefer GS1 EPCIS 2.0.1, CBV 2.0 and Global Traceability 2.0;
UN/CEFACT Integrated Track and Trace; ISO 22095 including current mass-balance
and book-and-claim parts, ISO 22005 and ISO 28000; FDA food traceability and EU
Digital Product Passport as jurisdiction profiles; IATA ONE Record and DCSA
Track and Trace as modal profiles; RFC 3339 and RFC 8785; PROV-O, Verifiable
Credentials, Data Integrity, DQV and ODRL. Pin versions or access dates and keep
sector, jurisdiction, claims, certification, security, privacy, licensing and
conformance limits explicit.

