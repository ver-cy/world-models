# WM-ACT-026 Codex pre-provider boundary

Status: preparatory boundary analysis. This is not a provider result.

- The root represents an agreement or managed hold over future capacity, not
  the schedule definition, availability slot, encounter or delivered service.
- A reservation can temporarily hold capacity before confirmation; an
  appointment normally binds named participants or roles to a time and
  service. Profiles may narrow these terms but must declare the distinction.
- Planned start and end, timezone, recurrence, arrival window, deadlines and
  modification times are different temporal facts.
- Confirmation, cancellation and no-show are source-qualified assertions and
  do not prove attendance, encounter completion or service outcome.
- Resource, service, location, parties, schedule, payment, policy, consent,
  notification and audit history retain external identity and lifecycle.
- Capacity conflict, overbooking, double booking, stale availability and
  concurrent modification must be visible validation outcomes.
- An identifier or timestamp alone is not appointment identity; use the
  authoritative booking or scheduling system and stable lineage.

Adjudication must reject actual attendance inferred from confirmation,
destructive rescheduling, timezone-free instants, silent recurrence expansion,
hidden waitlist priority, payment treated as booking identity and a generic
event model that omits allocation, capacity and participant commitments.
