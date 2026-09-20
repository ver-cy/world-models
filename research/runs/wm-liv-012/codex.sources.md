# WM-LIV-012 Codex source notes

The synthesis treats `Genomic Sequence / Variant` as a governed aggregate with
a mandatory sequence, molecular-variant or combined-package discriminator.
GA4GH refget anchors immutable sequence and sequence-collection identity in
canonical content digests. GA4GH VRS anchors computable molecular variation in
explicit defining fields, sequence references and algorithm-versioned
identifiers. Neither identity is replaced by an archive accession, filename,
coordinate string or display name.

HGVS 21.1.4 requires an accepted immutable reference sequence and distinguishes
experimentally determined from predicted RNA or protein consequences. VCF 4.5
is a file representation whose record and genotype context cannot silently
become canonical molecular identity. NCBI SPDI, ClinVar, RefSeq and EMBL-EBI
EVA provide complementary normalization, accession, archive, submission and
aggregation models. Cross-system equivalence therefore requires pinned source
and target releases, reference context, normalization method and round-trip
evidence.

Sequence Ontology supplies typed sequence alteration and consequence terms.
ClinGen and ACMG/AMP govern condition-specific evidence interpretation, but
these clinical assertions remain outside the molecular definition. ClinVar's
submitted classification, variant aggregate and variant-condition aggregate
identities demonstrate why a variant, an observation and a clinical
classification cannot be merged.

FHIR R5 MolecularSequence and Beacon v2 are exchange or discovery projections,
not mastership rules. FHIR's resource is Trial Use. GA4GH VRS 2.1 is under
ballot, the ACMG/AMP replacement is in development and living vocabularies and
archives require exact release pins. Production conformance cannot be inferred
from alignment to a moving or immature specification.

GA4GH DUO and the Responsible Sharing Framework establish purpose, consent,
permitted-use, privacy and security context. PROV-O, DQV, ODRL, RFC 3339, RFC
8785 and JSON-LD provide provenance, quality, rights, clocks, deterministic JSON
and linked-data projections. Person or specimen linkage makes genomic content
sensitive even when the molecular variant itself is publicly known; disclosure
therefore remains deny-by-default and minimum-necessary.
