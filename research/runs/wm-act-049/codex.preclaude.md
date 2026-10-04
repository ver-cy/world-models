# WM-ACT-049 Codex pre-provider note

This is preparatory boundary evidence, not provider research and not a
publication artifact.

- Registry identity: `vr.wm-act-049`, model `WM-ACT-049`, name Care Plan /
  Episode.
- Registry record plane: `world-model`; catalogue entry kind:
  `standalone-mm`; candidate subject-schema kind: `aggregate`.
- Purpose: represent goals, problems, intended interventions, responsible team
  and episode responsibility without conflating planning with performed care.
- Candidate outgoing relations: `REFERENCE WM-LIV-021`, `CONTAINS WM-ACT-047`
  and `CONTAINS WM-ACT-048`; do not approve them or inherit target lifecycles.
- Expected external masters: patient or group, practitioner, organization,
  condition, observation, encounter, consent, protocol definition, request,
  task, procedure, medication, appointment, communication, adverse event,
  provenance, audit and records policy.
- Required direct properties: independent plan and episode identifiers,
  statuses and periods; intent, category, subject, concerns, goals, targets,
  preferences, responsible roles, activity links, dependencies, progress,
  transitions, closure and successor lineage.
- Required safety boundary: no autonomous diagnosis, care authorization,
  treatment change, assignment, execution, clinical inference, disclosure or
  disposition without explicit delegated authority and applicable policy.
- Required time format: RFC 3339 with seconds and explicit offset or `Z`, with
  authored, effective, planned, scheduled, occurrence, evaluation, transition,
  recorded, ingested and knowledge times separated whenever they differ.
