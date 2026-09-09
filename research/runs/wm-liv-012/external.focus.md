# WM-LIV-012 bounded external research focus

Produce one complete schema-valid result for `WM-LIV-012 Genomic Sequence /
Variant`.

Treat the root as a governed aggregate with an explicit sequence, molecular
variant or combined-package discriminator. Keep immutable biological sequence
identity distinct from an accession, assembly, sequence collection, specimen,
read, alignment or annotation. Keep a normalized molecular variant definition
distinct from its textual expression, database accession, observed call,
genotype, allele frequency, predicted consequence, clinical interpretation and
disease association.

Cover identity, class and scope; molecule and alphabet; residue sequence,
length, topology, digest and canonicalization; authoritative accession and
version; organism and taxon reference; assembly, sequence collection,
chromosome or contig membership; coordinate convention, interval, orientation
and strand; reference and alternate state; substitution, insertion, deletion,
indel, repeat, copy-number and structural variation profiles; allele, haplotype
and variation-set composition; normalization and computed identifiers; HGVS,
SPDI, VCF and VRS expressions; mappings and equivalence assertions; lifecycle,
merge, split, deprecation and replacement; provenance and validation; evidence
and quality; access, consent and retention bindings; loss-aware projections.

Keep organism, chromosome, gene, transcript, protein, specimen, person,
consent, assay, run, reads, alignments, call set, genotype, population frequency,
phenotype, disease, clinical assertion, treatment, publication and external
archive as referenced masters. Never infer pathogenicity from molecular
existence, an observed call from a variant definition, equivalence from a shared
label, or coordinate compatibility from an assembly name alone. Preserve
reference accession plus version, digest, coordinate convention and
normalization algorithm. Separate experimentally observed from computationally
predicted consequences and retain competing interpretations without
last-write-wins.

Review registered parent `WM-LIV-011` but do not expand it into ownership of
organisms, genomes, genes or specimens. Hold unclear direction or semantics for
later joint boundary review.

Target 6 bundles, 12 layers, 24 findings, 72 questions, 24 artifacts and 10
functions. Prefer GA4GH VRS 2.0, refget Sequences 2.0 and Sequence Collections
1.0, HGVS 21.1.4, VCF 4.5, INSDC, NCBI RefSeq and Variation Services, ClinVar,
EMBL-EBI EVA, Sequence Ontology, ClinGen, ACMG/AMP, HL7 FHIR R5, GA4GH DUO and
responsible-sharing guidance, W3C PROV-O and DQV, ODRL, RFC 3339 and JSON-LD.
Pin exact versions or access dates and keep clinical, species, jurisdiction,
privacy, consent, licensing, maturity and conformance limitations explicit.
