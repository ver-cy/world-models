# WM-ACT-048 verified source notes

Accessed 2026-09-06. These are official primary or first-party sources used by
the Codex fallback. Provider wrappers are not sources.

- HL7 FHIR R5 MedicationRequest 5.0.0, maturity 4, Trial Use: order/request for
  one medication, subject, intent, status, priority, authored time, requester,
  dosage intent, dispense authorization, repeats and substitution limits.
- HL7 FHIR R5 MedicationDispense 5.0.0, maturity 2, Trial Use: an independent
  supply event with authorizing prescription, performer, prepared and handover
  times, quantity, days supply, receiver and substitution evidence.
- HL7 FHIR R5 MedicationAdministration 5.0.0, maturity 2, Trial Use: an
  independent actual or not-done administration event with occurrence and
  recorded times, actor, actual dose, route, site, method, rate, subpotency and
  waste semantics.
- HL7 FHIR R5 MedicationStatement 5.0.0, maturity 4, Trial Use: a reported or
  derived belief about medication use, explicitly outside the prescribe,
  dispense and administer event sequence.
- HL7 FHIR R5 Medication and Medications Module 5.0.0: product identity and the
  boundaries among request, dispense, administration and statement resources.
- WHO Medication Safety in Transitions of Care, 2019: best possible medication
  history, source verification, discrepancy reconciliation, list update and
  communication at care transitions.
- WHO Medication Safety in High-risk Situations, 2019: medication, patient or
  provider, and system risk factors with risk-reduction controls.
- WHO INN Programme: globally recognized public generic substance names, not a
  product authorization or recommendation.
- EMA ISO IDMP overview: substance, dose form, route, unit, product,
  authorization, packaging and manufacturing identifiers across the product
  lifecycle; regional implementation details remain profiles.
- SNOMED CT Pharmaceutical and Biologic Product model: international abstract
  medicinal-product classes and national-extension boundaries for actual
  products and packages.
- NLM RxNorm Overview: normalized US clinical-drug and pack names, identifiers
  and mappings; regional scope and source-version limits apply.
- OMOP CDM 5.4 Drug Exposure: prescriptions, dispenses and administrations can
  coexist in one analytic table, but provenance type, original source values,
  unique event identity and ETL choices must be preserved.
- UCUM 2.2: machine-interoperable quantity units and expression semantics,
  including clinical dose and dose-rate units.
- EU GDPR, W3C PROV-O and RFC 3339: purpose limitation, provenance and explicit
  interoperable event and knowledge timestamps.
