# WM-ACT-047 pre-provider boundary freeze

- Subject: one medical procedure occurrence or explicitly recorded non-performance, represented as a clinical event summary rather than a real-time control system.
- Owns: occurrence identity and lineage, procedure classification, request and plan bindings, status, subject and focus references, performers, timing, site, technique, used and focal-item references, immediate outcome, output and report links, complication and follow-up links, corrections, provenance, privacy, retention and projections.
- Does not own: reusable procedure definition, ServiceRequest, CarePlan, Appointment, Task, Encounter, Consent, Patient, Practitioner, Organization, Location, Device, Substance, Medication, Specimen, Observation, DiagnosticReport, Condition, AdverseEvent, payment, claim, audit or record lifecycles.
- Candidate relation: WM-ACT-049 Care Plan / Episode CONTAINS WM-ACT-047. This is not an approved edge and grants no cascade behavior.
- Parent hint: WM-ACT-014 Health Care Delivery remains an external system context, not a lifecycle owner for the procedure occurrence.
- Core invariants: order is not performance; scheduled is not in-progress; completed does not prove success; outcome is not complication; complication is not necessarily causation; reported is not primary source; date is not identity; corrections never overwrite released history.
- Publication target: lifecycle published, assurance reviewable-draft, medium or low confidence if external providers fail.
