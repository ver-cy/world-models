# WM-ACT-026 bounded external research focus

Produce one concise, complete `model-research.schema.json` result for
`WM-ACT-026 Appointment / Reservation Event`.

## Frozen boundary

- Treat the frozen `standalone-mm` value as record-plane metadata and choose a
  defensible subject-model kind. Test event versus aggregate explicitly.
- Model a proposed, held or confirmed future allocation of time, capacity,
  service, place or resource among participants. Separate appointment,
  reservation, availability, slot, schedule, request, encounter, order,
  resource, payment and notification.
- Preserve organizer or provider, requester or customer, participants,
  resource and service references, time zone and recurrence, capacity,
  location, terms, holds, confirmation and waitlist state.
- Represent propose, hold, accept, reject, confirm, modify, reschedule,
  cancel, expire, no-show and fulfil as attributable events with effective and
  knowledge time. Never rewrite history silently.
- Keep party, resource, service, schedule, encounter, payment, authorization,
  message, policy and audit masters external.
- Distinguish planned allocation from actual encounter, attendance, service
  delivery, payment and outcome.

## Size and evidence limits

- Target 6 bundles, 12 layers, 24 findings, 72 discriminating questions, 24
  artifacts and 10 functions.
- Use at least 8 current primary official sources from at least 4 independent
  organizations. Prefer IETF iCalendar, iTIP and JSCalendar, HL7 FHIR
  Appointment, Schedule and Slot, TM Forum Appointment Management, Schema.org
  Reservation and Event, W3C PROV and official time standards.
- Every structure and function element needs source references.
- State sector, timezone, recurrence, overbooking, privacy, payment,
  interoperability and external-review limitations as holds.
