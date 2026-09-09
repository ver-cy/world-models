# WM-LIV-012 Codex pre-provider position

The defensible root is an aggregate because a normalized variation depends on
an immutable reference sequence and coordinate semantics, while a sequence may
also exist independently. A mandatory discriminator prevents the registered
slash-name from collapsing these distinct identities.

The core identity chain is sequence content digest plus accession/version,
sequence collection or assembly context, coordinate convention, normalized
reference and alternate state, variation class and algorithm-versioned computed
identifier. Textual HGVS, SPDI and VCF expressions and database accessions are
projections or mappings, not identity by themselves.

Clinical meaning is outside the aggregate. A molecular variant may be observed
in a specimen or person and may support a condition-specific assertion, but
calls, genotypes, frequencies, consequences, evidence classifications and
clinical decisions retain their own provenance and lifecycle.

Likely critical errors are silent assembly lift-over, accession without version,
coordinate-base or interval ambiguity, reverse-complement mistakes, repeat
normalization drift, collapsing multi-allelic or phased variation, treating
predicted consequence as observation, and disclosing identifiable genomic data
without purpose and consent checks.

Any source or provider may narrow this position with evidence. Exact equivalence
among VRS, HGVS, SPDI, VCF, RefSNP, ClinVar and EVA identities must never be
claimed without release-pinned normalization and round-trip tests.
