# WM-ACT-026 Codex source ledger

Status: verified primary-source discovery for the Codex fallback. This is not
an external-provider result.

| ID | Primary source | Intended use |
| --- | --- | --- |
| SRC-001 | HL7 FHIR R5 Appointment, https://www.hl7.org/fhir/appointment.html | Appointment boundary, participants, time, recurrence and lifecycle. |
| SRC-002 | HL7 FHIR R5 Slot, https://www.hl7.org/fhir/slot.html | Slot state, interval, service classes and overbooking. |
| SRC-003 | HL7 FHIR R5 Schedule, https://www.hl7.org/fhir/schedule.html | Availability container and separation from booked appointments. |
| SRC-004 | HL7 FHIR R5 AppointmentResponse, https://www.hl7.org/fhir/appointmentresponse.html | Participant responses and recurrence scope. |
| SRC-005 | IETF RFC 5545, https://www.rfc-editor.org/rfc/rfc5545 | Event identity, organizer, attendee, time, resources and recurrence. |
| SRC-006 | IETF RFC 5546, https://www.rfc-editor.org/rfc/rfc5546 | Request, reply, cancel, counter, sequencing, security and privacy. |
| SRC-007 | IETF RFC 8984, https://www.rfc-editor.org/rfc/rfc8984 | JSON event, participants, locations, time zones and recurrence overrides. |
| SRC-008 | IETF RFC 9557, https://www.rfc-editor.org/rfc/rfc9557 | Offset timestamps, named time-zone intent and future local time. |
| SRC-009 | Schema.org Reservation, https://schema.org/Reservation | Reservation identity, parties, subject, status, ticket and price. |
| SRC-010 | Schema.org Event, https://schema.org/Event | Event time, place, attendance mode, capacity, schedule and status. |
| SRC-011 | TM Forum TMF646 v4.0.1, https://www.tmforum.org/resources/specifications/tmf646-appointment-management-api-rest-specification-r19-0-0/ | Cross-industry free-slot search and appointment creation. |
| SRC-012 | W3C PROV-O, https://www.w3.org/TR/prov-o/ | Booking event, revision, source and responsible-agent provenance. |

Boundary note: availability observation, temporary hold, participant response,
confirmed booking, actual encounter and service outcome are separate assertions.
The booking references parties, resources, services, schedules, orders, payments,
messages and encounters without absorbing their master lifecycles.
