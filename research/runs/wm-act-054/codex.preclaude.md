# WM-ACT-054 Codex pre-provider note

This is preparatory boundary evidence, not provider research and not a
publication artifact.

- Registry identity: `vr.wm-act-054`, model `WM-ACT-054`, name Research Subject
  / Participant.
- Registry record plane: `world-model`; catalogue entry kind:
  `standalone-mm`; candidate subject-schema kind: `aggregate`.
- Purpose: represent a governed subject-to-study participation relationship,
  not a person, study, consent form, medical record or research result.
- Candidate incoming relation: `WM-ACT-036 CONTAINS WM-ACT-054`, rationale
  `Research governance`. It is a boundary signal only and grants no cascade.
- Expected external masters: person, animal, organization, specimen, study,
  protocol, consent artifact, eligibility criterion, intervention, encounter,
  observation, adverse event, payment, identity linkage, ethics decision,
  provenance, access audit and records policy.
- Required direct properties: subject and study references, subject profile,
  study-specific identifiers, recruitment and screening, eligibility decision,
  consent and permission bindings, enrolment and allocation, arm and period,
  participation activities, safety references, outcome and reason, data-use,
  pseudonymisation, corrections, access and retention.
- Required safety boundary: no autonomous recruitment, eligibility, consent,
  allocation, intervention, unblinding, re-identification, safety decision,
  compensation, disclosure or deletion outside explicit delegated authority.
- Required time format: RFC 3339 with seconds and explicit offset or `Z`, with
  recruitment, screening, consent, enrolment, allocation, participation,
  observation, withdrawal, recorded, ingested and knowledge times distinct.
