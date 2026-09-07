# WM-LIV-021 Codex source notes

The synthesis treats `Disease / Biological Condition` as a governed aggregate
for one condition occurrence concerning one organism. The occurrence remains
distinct from a terminology concept, a diagnosis assertion, a problem-list
entry, a care encounter and a public-health surveillance case. This boundary
allows assertions to be corrected without rewriting the biological subject or
the terminology master.

WHO ICD-11 supplies international classification and coding. SNOMED CT adds
clinical finding and disorder semantics plus modeled attributes such as site,
morphology, cause, severity and course. Mondo, Human Disease Ontology,
Orphanet and NCI Thesaurus provide complementary disease concepts and mappings.
Every binding therefore preserves the terminology, concept identity, release,
profile, mapping relation and provenance rather than using a display label as
identity.

FHIR R5 Condition distinguishes clinical status from verification status and
keeps onset, abatement, severity, stage, body site and evidence explicit.
ClinicalImpression separates an assessment, differential and prognosis from
the condition. Observation separates measurements and findings. OMOP CDM 5.4
provides an analytics-oriented ConditionOccurrence and derived ConditionEra,
but those operational rules are projections rather than biological truth.

HPO and Phenopackets keep phenotypic abnormalities separate from a disease
diagnosis or hypothesis. ClinGen similarly treats gene-disease validity as an
evidence-based relationship assertion. CDC surveillance definitions apply
uniform reporting criteria and explicitly do not replace individual clinical
diagnosis. A gene, variant, pathogen, risk factor, phenotype or surveillance
rule therefore cannot silently become proof of disease.

WHO ICF places functioning, disability, activity, participation and contextual
factors alongside, not inside, disease classification. Course, severity,
stage, functional impact, causal attribution and prognosis are time-bound,
method-qualified assertions. Clinical status, verification status and record
status remain separate. Remission is not cure, recurrence is not a duplicate,
susceptibility is not disease and prognosis is not outcome.

PROV-O, DQV and ODRL provide provenance, quality and policy projections. RFC
3339 supplies second-precision timestamps with explicit offsets and RFC 8785
supplies deterministic JSON canonicalization. Protected condition data remains
deny-by-default and minimum-necessary, with consent or lawful basis, purpose,
jurisdiction, retention and audit evaluated independently from terminology.
