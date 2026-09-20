# WM-PER-007 Personal Health independent pre-provider boundary

## Frozen root

A Personal Health instance is the longitudinal, person-grain context of health
states, observations, risks, interventions, care intentions and supporting
evidence for one subject. It can federate clinical and personal sources without
silently replacing their masters or treating an unverified assertion as truth.

## External boundaries

- The person and every practitioner, organization, related person and device
  retain external identity and lifecycle.
- Encounters, appointments, tasks, services, claims, coverage, research,
  public-health reporting, devices, products, specimens, images and genomic
  sequences retain their own masters.
- Clinical terminologies and classifications are versioned references, not
  copied vocabularies.
- Custody, controller duties and data-subject rights are jurisdiction-specific;
  no universal legal-ownership claim is inferred.

## Expected bundles

1. Subject, record identity and longitudinal boundary.
2. Conditions, risks, function and current health state.
3. Observations, diagnostics, specimens and evidence.
4. Allergies, medications, immunizations and procedures.
5. Encounters, care plans, goals and coordination.
6. Provenance, consent, privacy, access and retention.
7. Interoperability, summaries, validation and safe agent operations.

## Non-negotiable checks

- Never merge records on name or demographic similarity alone.
- Diagnosis, self-report, observation, device output and algorithmic inference
  remain different assertion kinds with separate authority and confidence.
- Codes pin system and version; measurements pin unit, method, reference range,
  body site, time and interpretation where applicable.
- Missing, unknown, not asked, not performed and redacted are not equivalent.
- Agent-generated clinical changes remain proposals unless current policy and
  accountable clinical authority permit the exact action.
- Emergency access is purpose-bound, minimum necessary, time-limited, logged
  and reviewed; it is never a reusable bypass.
