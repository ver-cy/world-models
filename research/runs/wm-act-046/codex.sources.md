# WM-ACT-046 source notes

Accessed 2026-09-06. The fallback used primary official specifications and registries only.

- HL7 FHIR R5 Observation 5.0.0: event-result identity, status, subject, focus, encounter, effective time, value choices, missingness, interpretation, method, specimen, device, reference range, membership and derivation. It explicitly separates ordinary observations from diagnoses.
- HL7 FHIR R5 Condition 5.0.0: diagnosis or condition assertion, clinical status, verification status, onset, abatement, stage and evidence. It distinguishes symptoms used as observations from concerns requiring ongoing condition management.
- HL7 FHIR R5 DiagnosticReport and ClinicalImpression: report versus atomic-result boundaries and an assessment or differential layer before management; both retain explicit Trial Use and maturity limits.
- openEHR RM 1.1.0: OBSERVATION has data, subject state and protocol, whereas EVALUATION covers interpretations, diagnoses, differentials, hypotheses and risks; INSTRUCTION owns actionable future statements.
- SNOMED CT official concept and editorial guides: observable entity is a question or assessment, clinical finding is an observation or judgment result, and disorder entails abnormality, pathology and persistence.
- LOINC 2.82 knowledge base: component, property, time aspect, system, scale and method qualify the meaning of laboratory and clinical observations.
- WHO ICD-11 2026-01 and ICD API v2: release-qualified classifications and stable ICD URIs; ICD mapping is a projection rather than the source clinical assertion.
- OMOP CDM 5.4: Measurement, Observation and Condition Occurrence are separate analytic domains; source concept and provenance fields are necessary because normalization can lose rule-out and source distinctions.
- DICOM PS3.3 current edition: imaging observation context, structured content and evidence or image references are a specialized report projection.
- UCUM 2.2: machine-unit identity and conversion semantics for quantities.
- GDPR, PROV-O and RFC 3339: protected health-data handling, attributable revision or invalidation, and precise event and knowledge timestamps.

No source was used to claim universal clinical safety, diagnostic authority, legal compliance or complete interoperability. Those remain adopter-profile and independent-review responsibilities.
