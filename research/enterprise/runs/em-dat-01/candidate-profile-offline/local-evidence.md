# EM-DAT-01 local evidence review

## Existing authority

WM-DAT-001 already owns dataset identity, catalogue-record distinction, dataset versions, distributions, checksums, provenance summaries, quality evidence, rights and retirement. WM-DAT-004 already owns schema and data-contract identity, immutable contract versions, property structure, term and value-domain bindings, compatibility modes, producer/consumer obligations and publication.

The two models therefore cover the complete EM-DAT-01 acceptance scenario without introducing another aggregate:

1. one stable dataset identity has a released dataset version;
2. that version has two format-specific distributions with separate media types and checksums;
3. both distributions point to the same pinned contract version;
4. a later contract version is checked under its declared compatibility mode;
5. a corresponding dataset version preserves its predecessor and provenance links.

## Enterprise constraints absent from the bases

The base contracts express several necessary elements as optional. A useful Enterprise profile would make only these cross-model rules normative:

- distinguish the stable dataset identifier from each released dataset-version identifier;
- require checksum/fixity for each distribution;
- require a version-pinned schema/contract reference and explicit conformance status;
- require all distributions of a dataset version to bind to the same contract version;
- require a compatibility mode and a published compatibility outcome for a new contract version;
- derive the dataset breaking-change indicator from the contract compatibility outcome;
- require a declared consumer scope and change-notice path;
- require predecessor and provenance assertions when a dataset version is issued;
- require authoritative term/value-domain references for designated critical data elements.

These constraints tighten cardinalities and connect existing assertions. They do not create a new identity, lifecycle, event stream or state machine.

## Boundary decisions

- A catalogue record describes a dataset and remains distinct from it.
- Distribution bytes and format are manifestations of a dataset version, not independent dataset identities.
- Dataset version and contract version advance independently, with an explicit binding between them.
- Structural property definitions belong to the contract; business meaning remains in governed term and value-domain authorities.
- Dataset-level quality evidence does not absorb the quality metric and assessment-run models.
- Dataset provenance summaries do not absorb the full lineage graph.

## Publication holds

Both base releases are marked published but still carry `publishableCanonical: false` and `adjudicationStatus: reviewable-draft`. That blocks a canonical normative Enterprise release.

Additional limits inherited from the bases:

- DataCite source-version inconsistency prevents clause-level relation-type claims.
- ODCS source pinning and `dataProduct` deprecation need resolution before claiming exact ODCS conformance.
- ISO/IEC 11179 access limits the result to an alignment statement rather than clause-level conformance.
- multi-profile SHACL validation has not established DCAT-AP/DCAT-US conformance.

## Current disposition

`PROFILE`, with no new runtime identity. Draft the Enterprise profile as a version-and-digest-pinned conformance layer over WM-DAT-001 and WM-DAT-004. Do not publish it as canonical until the base holds are cleared. If independent review shows that the nine constraints are deployment policy rather than portable semantics, downgrade to `REUSE ONLY` and publish only an adoption mapping.
