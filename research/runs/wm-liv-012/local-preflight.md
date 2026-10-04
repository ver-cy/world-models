# WM-LIV-012 canonical preflight

- Sequence: 178
- Registry identity: `vr.wm-liv-012`
- Model identity: `WM-LIV-012`
- Registered name: `Genomic Sequence / Variant`
- Registry-plane kind: `standalone-mm`
- Candidate subject kind: `aggregate`
- Navigation: `NAV.PHY.LIV.MOL`
- Domain: `PHY.LIV.MOL`
- Registered parent: `WM-LIV-011`
- Registered purpose: independent identity, provenance and clinical or research lifecycle

## Frozen boundary

The root is a governed aggregate for immutable biological sequence identity and
computable molecular variation relative to an explicit reference context. It
may own sequence content identity, sequence collection membership, coordinate
and orientation semantics, normalized molecular variant definitions, alternate
expressions, lifecycle and provenance. It does not own organisms, specimens,
people, consent, assays, reads, alignments, call sets, genotypes, frequencies,
phenotypes, diseases, clinical interpretations, treatment decisions or source
archives. Those remain referenced master records.

The name combines two related but non-identical subjects. The result therefore
requires an explicit sequence, variant or combined-package discriminator and
must not treat a variant expression, database accession, call, observation or
clinical assertion as the molecular variant itself.

## Relation hold

`WM-LIV-011` is retained as a registered parent reference until its meaning is
reviewed. Parentage must not imply that a sequence or variant owns its organism,
genome, chromosome, gene, specimen or observation.

## Evidence posture

Use current official GA4GH VRS and refget releases, HGVS recommendations, the
canonical VCF specification, INSDC and NCBI sequence identity rules, NCBI
variation and ClinVar data models, EMBL-EBI EVA, ClinGen and ACMG guidance,
HL7 FHIR, Sequence Ontology and official provenance, quality, access and time
standards. Pin versions or access dates and expose draft, trial-use, licensed,
jurisdictional and profile limitations.
