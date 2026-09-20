# WM-ACT-046 pre-provider boundary freeze

- Subject: one source-qualified clinical assertion record, profiled as observation or diagnosis.
- Required discriminator: `observation-result`, `clinical-impression` or `diagnosis-condition`; adopters may extend profiles but may not merge their semantics silently.
- Owns: assertion identity and lineage, profile, subject and encounter bindings, observed or assessed meaning, result or diagnostic statement, interpretation, evidence basis, participants, time semantics, verification and lifecycle events, amendment or refutation lineage, access, provenance, retention and projections.
- Does not own: patient, related person, practitioner, care team, encounter, episode, specimen, device, service request, procedure, diagnostic report, disease or biological condition, terminology, care plan, treatment, medication, consent, audit or master record lifecycles.
- Candidate relation: Encounter CONTAINS this model. This is not an approved edge and does not grant this model ownership of Encounter lifecycle.
- Parent hint: WM-LIV-021 Disease / Biological Condition remains an external subject or concept master; a diagnosis assertion is not the disease entity itself.
- Core invariants: observable definition is not a result; result is not diagnosis; preliminary is not final; clinical status is not verification status; refuted is not deleted; absence, unknown and not-performed are distinct; unit, method, specimen and reference range qualify a value; event time and knowledge time remain separate.
- Publication target: lifecycle published, assurance reviewable-draft, medium or low confidence if external providers fail.
