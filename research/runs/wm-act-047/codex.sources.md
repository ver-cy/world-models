# WM-ACT-047 source notes

Accessed 2026-09-06. The fallback used primary official specifications, classifications and authority guidance.

- HL7 FHIR R5 Procedure: summary event for what was or is being performed, with request, plan, parent, subject, occurrence, performer, site, outcome, report, complication, follow-up, focal-device and used-item links. It is Trial Use at maturity level 4 and is not a real-time control record.
- HL7 FHIR R5 ServiceRequest and CarePlan: proposal, plan or order semantics remain separate from the occurrence. FHIR AdverseEvent owns harmful, potential or avoided safety-event context and evolving causality. FHIR Observation owns measured results.
- openEHR RM 1.1.0: INSTRUCTION and ACTIVITY specify intended work; ACTION records what was actually done, including ad hoc action and state transitions across organizations.
- SNOMED CT official procedure guides: procedure method, site, morphology, approach, device, substance, focus, intent and recipient attributes; combined procedures and routine components require explicit modelling choices.
- WHO ICHI: intervention target, action and means, multiple actions, routine components, residual categories and extension codes. The cited guide is a current development publication, not a universal clinical record contract.
- WHO Surgical Safety Checklist and Joint Commission Universal Protocol: subject, site, procedure, consent and team verification checkpoints. Local policy and jurisdiction remain required.
- OMOP CDM 5.4: Procedure Occurrence identity, subject, provider, visit, start and end times, source values, standardized concepts and modifiers; ETL choices can lose source distinctions.
- FDA UDI: device versus production identifiers, including lot, serial and expiry, for exact item-use references. This is a United States profile.
- GDPR, PROV-O and RFC 3339: protected procedure data, attributable revision and invalidation, and precise event and knowledge timestamps.

No source was used to claim universal clinical safety, consent validity, causal attribution, legal compliance or complete interoperability. Those remain adopter-profile and independent-review responsibilities.
