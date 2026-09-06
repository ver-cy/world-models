# WM-ACT-048 Codex pre-provider note

This is preparatory boundary evidence, not provider research and not a
publication artifact.

- Registry identity: `vr.wm-act-048`, model `WM-ACT-048`, name Medication Order
  / Administration.
- Registry record plane: `world-model`; catalogue entry kind:
  `standalone-mm`; candidate subject-schema kind: `aggregate`.
- Purpose: represent the prescription, dispense and administration lifecycle
  while retaining distinct identifiers, states, times, actors and evidence for
  each stage.
- Incoming relation: candidate `WM-ACT-049 CONTAINS WM-ACT-048`; do not approve
  it or inherit care-plan lifecycle semantics in this run.
- Expected external masters: patient or group, practitioner and organization,
  encounter, care plan, medication and medicinal-product definition, condition,
  observation, allergy, adverse event, detected issue, coverage, claim,
  inventory, device, provenance, consent, audit and records policy.
- Required direct properties: order intent and priority, medication binding,
  dosage intent, dispense authorization, substitution limits, actual dispense,
  actual administration or non-administration, dose, route, site, method, rate,
  lot or package binding, event and record times, statuses and reasons.
- Required safety boundary: no autonomous prescribing, dispensing,
  administration, dose change, interaction interpretation, causal attribution,
  disclosure or record disposition without explicit authority and applicable
  clinical policy.
- Required time format: RFC 3339 with seconds and explicit offset or `Z`, with
  event, authored, prepared, handed-over, administration, recorded, reported,
  ingested and knowledge times separated whenever they differ.
