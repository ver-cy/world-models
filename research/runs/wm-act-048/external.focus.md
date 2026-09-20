# WM-ACT-048 bounded provider focus

Research the aggregate that links a medication request, each dispense event and
each administration or explicit non-administration event without conflating
them. Preserve the distinctions among intent, authorization, supply, actual
administration, reported medication use, clinical observation, adverse event,
inventory, product definition and care-plan lifecycle.

Use current official primary sources. At minimum inspect the permanent HL7 FHIR
R5 MedicationRequest, MedicationDispense, MedicationAdministration,
MedicationStatement and Medication pages. Cross-check medication product
identity against official EMA IDMP, SNOMED CT medicinal-product and NLM RxNorm
materials; cross-check reconciliation and safety against WHO Medication Without
Harm material. Preserve each source's version and maturity status.

Stress-test these specific semantics:

- one request concerns one medication, while refills, partial fills,
  substitutions, administrations, omitted doses and waste are independent
  child events with their own identifiers and times;
- status on the request, dispense and administration are separate state axes;
- prescribed dosage, dispensed instructions and actually administered dose,
  route, site, method and rate must never be silently collapsed;
- an administration record is stronger event evidence than a reported
  MedicationStatement, but neither alone proves adherence, effectiveness or
  causation;
- medication knowledge, contraindication, interaction and decision-support
  outputs remain external and versioned; a safety check records evidence and
  decision basis without becoming an autonomous clinical decision maker;
- lot, serial, package, expiry and product identifiers remain source-qualified
  and jurisdiction-specific;
- reconciliation at transitions must retain source discrepancies, resolution,
  responsible actor and communication rather than overwriting prior lists;
- order cancellation does not retroactively cancel completed dispense or
  administration events, and correction creates successor lineage.

Treat the incoming candidate relation from WM-ACT-049 Care Plan / Episode as a
relationship-completeness hold. It does not transfer the care-plan lifecycle or
authorize cascade mutation. The result must remain a reviewable draft unless an
independent valid provider result and all release-pinned mappings are verified.
