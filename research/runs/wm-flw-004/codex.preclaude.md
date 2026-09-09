# WM-FLW-004 Codex pre-provider boundary

Status: independent source-planning note. It is not Claude or Grok output.

The model owns the governed plan and observed history of moving identified consignments and cargo units through ordered transport legs, locations, custody transitions, milestones and exceptions. It references goods, handling units, transport equipment, parties, organizations, facilities, contracts, customs records, permits, invoices, payments, sensor streams and evidence held by their master systems.

Candidate structure:

1. Identity, scope and transport arrangement.
2. Cargo, package and handling-unit composition.
3. Route, schedule, modes and legs.
4. Dispatch, loading, departure, arrival, transshipment, delivery and return observations.
5. Custody, possession, condition, seals and delivery evidence.
6. Exceptions, estimates, replanning, resolution and claims references.
7. Regulatory interfaces, controls, projections and interoperability.

Adversarial requirements:

- Never collapse shipment, consignment, cargo item, package, handling unit and transport equipment.
- Separate plan and estimate from actual observation and correction; event time and capture time are distinct.
- Custody, possession, carrier responsibility, title and ownership are different relations.
- Status is derived from append-only evidence and deterministic precedence, not last-write-wins.
- Customs, dangerous-goods, carrier, vehicle and facility semantics are governed profiles or references, not silently imported masters.
- Automated ETA and exception classification retain model, input, confidence, freshness and override provenance.
- Public tracking projections minimize commercial, personal, security and location-sensitive data.
- Artifact timestamps use RFC 3339 with seconds and explicit offset; artifact identity prefers an authoritative master-system ID.

The no-tools audit must reject legal-delivery, custody, ownership or compliance claims derived only from a tracking scan. Confidence remains medium when external provider review is absent. Proposed sibling relations remain on hold until approved by relationship governance.
