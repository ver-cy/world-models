# WM-LIV-021 bounded external research focus

Produce one complete schema-valid result for `WM-LIV-021 Disease / Biological
Condition`.

Treat the root as a governed aggregate for one condition occurrence concerning
an organism and source-qualified assertions about it. Keep the occurrence
distinct from a disease concept, diagnosis statement, problem-list entry,
encounter diagnosis, symptom, observation, phenotype, adverse event, risk,
care encounter, care plan and treatment episode. A code never proves presence.

Cover stable occurrence identity, subject, disease or condition concept and
classification bindings; assertion kind and source; clinical versus
verification versus record status; onset, manifestation, recognition,
diagnosis, recorded, effective, abatement, remission, relapse, recurrence and
resolution time; course, severity, stage and grade; anatomical site, laterality,
morphology and pathological process; etiology, causative agent, mode of
inheritance, transmission, risk factor and trigger with explicit evidence and
causal status; signs, symptoms, observations, tests and diagnostic-criteria
references; functional impact and ICF context; complication, comorbidity and
sequela relations; prognosis and uncertainty; provenance, review, correction,
duplicate, merge, split, refutation and supersession; access, privacy, consent,
retention and loss-aware projections.

Keep organism, person, specimen, encounter, care plan, intervention, medication,
procedure, observation, test result, phenotype, gene, variant, pathogen,
classification scheme, diagnostic rule, evidence artifact, prediction and
clinical decision as external masters. Do not equate disorder with momentary
finding, clinical status with verification, recurrence with duplicate record,
remission with cure, association with causation, susceptibility with disease,
or predicted prognosis with outcome. Preserve competing diagnoses and
source-qualified status or stage assertions without last-write-wins.

Review registered parent `WM-LIV-002 Organism Individual` and incoming reference
from `WM-ACT-049 Care Plan / Episode`. Retain both as references; condition
occurrence does not own the organism or care episode.

Target 6 bundles, 12 layers, 24 findings, 72 questions, 24 artifacts and 10
functions. Prefer WHO ICD-11 2026 and ICD API 2.6, WHO ICF, SNOMED CT clinical
finding and disorder model, HL7 FHIR R5 Condition and related resources, OMOP
CDM 5.4, Mondo, Human Disease Ontology, Orphanet/Orphadata, HPO, GA4GH
Phenopackets 2.0, ClinGen gene-disease validity, CDC public-health case
definitions, PROV-O, DQV, ODRL, RFC 3339 and JSON-LD. Pin versions or access
dates and keep terminology licenses, jurisdiction, species, clinical evidence,
privacy, maturity and conformance limitations explicit.
