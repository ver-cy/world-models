# Frozen no-tools semantic audit — EM-DAT-01

You are the final static semantic auditor. Use only this frozen packet. Do not browse, call tools, invent identifiers or grant publication authority.

Disposition: PROFILE over WM-DAT-001 and WM-DAT-004. No new model or runtime identity. The profile only promotes portable cross-model constraints; organization-specific PID, notice duration, SLA, freshness, catalogue and enforcement choices stay deployment policy.

Audit questions:
- Does any constraint introduce a hidden DatasetSchemaContract root, duplicate master or lifecycle?
- Are dataset, dataset-version, distribution, catalogue record, schema/contract version, quality, lineage and data-product boundaries unambiguous?
- Can independent dataset/contract versioning, mixed distribution formats, compatibility derivation or provenance still yield contradiction?
- Are deployment-policy values correctly excluded from reusable profile semantics?
- Which inherited holds prevent canonical publication but still allow a non-canonical reviewable draft?

Return at most 500 words with exactly: Verdict (`ACCEPT WITH LIMITS`, `REVISE`, or `REJECT`); Critical findings; Required holds; Scenario result; Identifier decision. Treat inherited base publication blockers as holds unless they contradict the candidate.

## Candidate

{
  "format": "vercy-enterprise-profile-candidate/v1",
  "contourId": "EM-DAT-01",
  "name": "Enterprise Dataset and Data Contract",
  "decision": "PROFILE",
  "newRuntimeId": false,
  "bases": [
    "WM-DAT-001",
    "WM-DAT-004"
  ],
  "constraints": [
    "WM-DAT-001 remains the sole authority for dataset, dataset-version and distribution identity; EM-DAT-01 creates no aggregate or runtime identity.",
    "WM-DAT-004 remains the sole authority for schema and contract-version identity, compatibility assessment and producer-consumer obligations.",
    "Every released dataset version has a stable dataset identifier and a distinct version-scoped identifier.",
    "Every published distribution carries media type and checksum or equivalent fixity evidence.",
    "Every governed dataset version pins one exact WM-DAT-004 contract version and records conformance status.",
    "All distributions of one dataset version bind the same contract version while dataset and contract versions may advance independently.",
    "Every successor contract version declares a compatibility mode and publishes one compatibility-check outcome.",
    "Dataset breaking-change status is derived from the published compatibility outcome and is never asserted independently.",
    "Consumer scope and an explicit change-notice path are declared; channel, notice duration and service levels remain deployment policy.",
    "Issuing a successor dataset version records predecessor and provenance assertions without absorbing the full lineage graph.",
    "Designated critical data elements bind authoritative governed-term and value-domain versions; the designation policy remains external.",
    "A catalogue record describes a dataset and never replaces the dataset or its version identity.",
    "A data-product offering, quality assessment engine and pipeline or deep-lineage graph remain external masters referenced by this profile.",
    "PID scheme, licence catalogue, consumer-registration enforcement, freshness targets and ODCS dialect selection beyond an exact version pin remain deployment policy."
  ],
  "holds": [
    "WM-DAT-001 and WM-DAT-004 remain reviewable drafts with publishableCanonical false.",
    "DataCite source-version consistency and live source pinning remain unresolved.",
    "ODCS version pinning and the dataProduct deprecation contradiction remain unresolved.",
    "ISO/IEC 11179 alignment lacks clause-level evidence.",
    "Multi-profile SHACL validation remains unrun.",
    "This candidate is a non-canonical reviewable profile only."
  ],
  "version": "0.1.0-candidate.2"
}


## Fixtures

{
  "format": "vercy-enterprise-profile-fixtures/v1",
  "profileName": "Enterprise Dataset and Data Contract",
  "cases": [
    {
      "id": "two-distributions",
      "kind": "positive",
      "input": "One dataset version is released as CSV and Parquet.",
      "expect": "Both distributions keep separate bytes and fixity while binding the same pinned contract version."
    },
    {
      "id": "independent-contract-version",
      "kind": "positive",
      "input": "The structural contract advances compatibly while dataset content does not change.",
      "expect": "The contract version advances independently and the dataset keeps its version while its exact conformance binding is updated under publication rules."
    },
    {
      "id": "dataset-successor",
      "kind": "positive",
      "input": "Dataset content changes under an unchanged compatible contract.",
      "expect": "A successor dataset version is issued with predecessor and provenance while retaining the exact contract pin."
    },
    {
      "id": "catalogue-record",
      "kind": "positive",
      "input": "A catalogue record registers the abstract dataset and is revised.",
      "expect": "The record changes without minting or replacing dataset identity."
    },
    {
      "id": "critical-term-binding",
      "kind": "positive",
      "input": "A designated critical field binds a governed term and a versioned value domain.",
      "expect": "The profile accepts the field while leaving designation policy external."
    },
    {
      "id": "missing-distribution-fixity",
      "kind": "negative",
      "input": "A published Parquet distribution has no checksum or equivalent fixity evidence.",
      "expect": "The release is rejected."
    },
    {
      "id": "mixed-contracts",
      "kind": "negative",
      "input": "CSV and Parquet distributions of one dataset version bind different contract versions.",
      "expect": "The release is rejected as incoherent."
    },
    {
      "id": "mutable-contract-link",
      "kind": "negative",
      "input": "A dataset version references latest contract without version or digest.",
      "expect": "Conformance is rejected as unpinned."
    },
    {
      "id": "missing-compatibility-outcome",
      "kind": "negative",
      "input": "A successor contract is published with a mode but no compatibility-check outcome.",
      "expect": "Publication is rejected."
    },
    {
      "id": "independent-breaking-flag",
      "kind": "negative",
      "input": "The dataset is marked non-breaking while the published compatibility outcome is breaking.",
      "expect": "The independent flag is rejected and must be derived from the outcome."
    },
    {
      "id": "missing-provenance",
      "kind": "negative",
      "input": "A successor dataset version has no predecessor or provenance assertions.",
      "expect": "Version issuance is rejected."
    },
    {
      "id": "catalogue-as-dataset",
      "kind": "negative",
      "input": "A catalogue record identifier is used as the dataset master identifier.",
      "expect": "The identity collapse is rejected."
    },
    {
      "id": "sla-as-profile-semantics",
      "kind": "negative",
      "input": "The reusable profile mandates a thirty-day notice period and one-hour freshness SLA.",
      "expect": "Those organization-specific values are rejected as deployment policy."
    },
    {
      "id": "fused-new-root",
      "kind": "negative",
      "input": "A DatasetSchemaContract root is minted for the same dataset and contract pair.",
      "expect": "The duplicate aggregate and runtime identity are rejected."
    }
  ],
  "version": "0.1.0-candidate.2"
}


## Local evidence

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


## Initial Claude study

# DECISION

**PROFILE.** Every question and invariant in EM-DAT-01 is already answerable from WM-DAT-001 plus WM-DAT-004, but the elements that would make the invariants *hold* are optional in both bases, and the two models carry two unreconciled breaking-change signals — that calls for normative tightening, not a new aggregate or a new runtime identity.

Normative constraints absent from the base models (the whole profile):

1. **Two-level identity.** A version-independent dataset identifier plus a version-scoped identifier per released version; `de-version-string` becomes required once a second version exists (base: `0..1`, optional).
2. **Mandatory fixity.** Every distribution carries a checksum (base: `de-checksum 0..1`) alongside the already-required media type.
3. **Version-pinned conformance.** `de-conforms-to` is required for any dataset under contract and pins contract *id plus version*; `de-conformance-status` must state asserted or verified (all three optional in base).
4. **Distribution coherence.** All distributions of one dataset version conform to the same contract version; a format regenerated with different bytes either re-declares fixity under the same version or forces a new dataset version.
5. **Declared compatibility mode.** `compatibilityMode` is required; `NONE` requires a recorded exception via `fn-record-exception`.
6. **Single breaking-change master.** `de-breaking-flag` on the dataset is *derived from* WM-DAT-004's `compatibilityCheckOutcome`, which must be published with the new contract version.
7. **Named consumer scope.** Either registered consumers, or an explicit declaration of unregistered consumption with a named notice channel and notice period.
8. **Provenance on issue.** On version issue, previous-version plus derived-from/generated-by/generated-at must be populated — the PROV-O mix-in stops being optional.
9. **Term binding for critical data elements.** For designated CDEs, at least one `authoritativeDefinitionReference` and a pinned value-domain/code-list version.

No new identity, lifecycle or state machine is introduced; the profile only raises cardinalities and adds derivation rules over existing findings.

# BOUNDARY FINDINGS

**1. Dataset vs catalogue record.** Settled in the base and correct. WM-DAT-001 holds registration as a facet (`catalogue-record-and-listing`, record state and its own timestamps) and explicitly declines to model the catalogue as an entity; the adjudication resolved Grok's contrary view in favour of the base. EM-DAT-01's third invariant is therefore already satisfied — do not reopen it.

**2. Stable identity vs version vs bytes.** Three-way separation exists (`de-master-dataset-id` required; `de-persistent-id`; `de-version-string`; distribution-level checksum/byte size), but the dossier never states whether the master identifier denotes the abstract dataset or a released version. That ambiguity is the real defect, and it is a cardinality and semantics question, not a missing aggregate.

**3. Dataset version vs schema/contract version.** Genuinely independent and modelled as such — WM-DAT-004 warns against conflating semantic version, registry version number and fingerprint. The flaw is asymmetry: WM-DAT-004's `governedTargetReference` is required `1..n`, while the dataset's conformance link, schema version and conformance status are all optional. The enterprise invariant is stated as a MUST against optional base elements.

**4. Structural schema vs meaning.** Cleanly split: `f-object-property-structure` (logicalType/physicalType, nesting, additionalProperties policy) versus `f-term-value-domain-binding` on the ISO/IEC 11179 conceptual/representational separation. But both binding references are optional, and the 11179 alignment is an unverified hypothesis (see holds) — the split is modelled, not mandated.

**5. Compatible vs incompatible change.** Strongest area of the base: seven compatibility modes plus transitive variants, `fn-check-compatibility`, `fn-publish-version` immutability, `fn-deprecate-and-sunset`, consumer registration, and the correct upgrade-order rule (consumers first under BACKWARD, producers first under FORWARD). Two defects: the mode is optional and `NONE` is permissible, and the dataset's breaking flag can be asserted independently of the contract's check outcome. Notice period and impact list appear only in prose, not as data elements.

**6/7.** Below.

# ACCEPTANCE WALKTHROUGH

One dataset, two formats: a single WM-DAT-001 entity with two distributions, each with its own media type, byte size, checksum and download URL; one logical contract version, projected per format through `fn-project-to-target-language` with the logicalType/physicalType split. `dcterms:conformsTo` may sit on dataset or distribution (DCAT 3, cited).

Schema change: `fn-author-contract-version` → `fn-check-compatibility` against the declared mode → verdict → `fn-publish-version` (immutable). If breaking, WM-DAT-001 `issue-version` chains the new dataset version via `de-previous-version` and sets the breaking flag; retired versions keep identifiers resolvable, with DataCite tombstone practice for withdrawal.

Two things the scenario does *not* survive on base cardinalities: provenance can legally be empty (`de-derived-from`, `de-generated-by`, `de-generated-at` all optional under an optional PROV-O mix-in), and the compatibility verdict need never be published (`compatibilityCheckOutcome 0..n`). "Preserved provenance and explicit compatibility" is exactly what constraints 5, 6 and 8 buy. No step required an aggregate the bases lack.

# GAPS AND HOLDS

**Blocking.** Both bases are `publishableCanonical: false` with `adjudicationStatus: reviewable-draft` despite `status: published` — EM-DAT-01 cannot cite them as canonical normative bases. That is the hold that actually blocks; it gates the profile's normative force, not its drafting.

**Blocking specific profile statements.** DataCite 4.6 vs 4.7 contradiction blocks naming DataCite relation types for constraint 1. ODCS unpinned `latest` URLs and the `dataProduct` deprecation contradiction block naming the governed-subject binding mechanism for constraint 3. Paywalled 11179-3/-31 confine constraint 9 to an alignment hypothesis with no clause-level conformance claim. Unperformed multi-profile SHACL validation (both models) means DCAT-AP/DCAT-US conformance may only be *declared*.

**Non-blocking but must be restated as inherited.** WM-DAT-001's security gap; WM-DAT-004's spatial/data-residency gap; untested regulated-sector profile and the three unvalidated deployment contexts — so no universality claim. EUR-Lex HVD and AI Act Article 10 holds do not touch this contour provided the profile makes no obligation-shaped regulatory statement. Housekeeping: DCAT 3 (SRC-001/SRC-020), DQV, PROV-O and DataCite are double-registered, and SRC-008 pins DCAT-US v1.1 (2014) while noting v3.0 as latest.

# MINIMAL PUBLICATION RECOMMENDATION

Publish one short Enterprise profile page for EM-DAT-01: the nine constraints above as a conformance table keyed to existing base finding and data-element ids, a one-paragraph statement that identity remains with WM-DAT-001 (dataset, version, distribution) and WM-DAT-004 (contract version), an explicit non-duplication clause, and the inherited-gap and hold list verbatim. Ship it as a reviewable draft marked non-canonical until the base models clear their own holds. Do not create a new model id, a catalogue entity, or a second breaking-change flag.


## Grok study

The team agrees: the contour is a version-pinned profile over the two existing masters, not a new aggregate.

## DECISION
**PROFILE**

A thin, version-pinned Enterprise conformance layer over WM-DAT-001 and WM-DAT-004 is justified. The bases already own the subject types. What the contour adds is a small set of cross-model rules that are optional in those bases and that the acceptance scenario needs. A new aggregate would invent a runtime identity that DCAT 3, ODCS, JSON Schema and ISO/IEC 11179 do not define. Plain reuse would leave the joining rules unenforced.

## BOUNDARY CHECK
WM-DAT-001 already owns the dataset aggregate: abstract dataset identity, version identity, distribution bytes, the catalogue-record facet, fixity, asset-level provenance, rights and permitted use, quality evidence, a breaking-change flag, and a declared schema/contract reference. Field semantics, compatibility modes and producer–consumer obligations are out of scope and pointed at WM-DAT-004. The catalogue record is a registration object (`dcat:CatalogRecord`); it does not replace the dataset.

WM-DAT-004 already owns schema and contract as citable resources: independent immutable versions, structural properties, ISO/IEC 11179-style term and value-domain bindings, compatibility modes and check records, producer/owner and consumer obligations, publication status distinct from version, and a `dcterms:conformsTo` binding to a dataset or distribution. It does not own dataset identity, distribution bytes or catalogue records.

WM-DAT-008 and EM-DAT-02 own the consumer-facing data-product offering. EM-DAT-03 owns pipeline and deep lineage. EM-DAT-04 owns the quality-rule engine. EM-DAT-01 must reference those neighbours, not absorb them.

DCAT 3 separates Dataset, Distribution and CatalogRecord; adds `dcat:version` / `dcat:previousVersion` / `dcat:hasCurrentVersion`; allows `spdx:checksum` on a distribution; and uses `dcterms:conformsTo` for an external schema or profile. It has no data-contract class. DQV attaches measurements to a dataset or distribution; `QualityPolicy` is not a producer–consumer contract. PROV-O supplies `wasRevisionOf`, `wasDerivedFrom`, `wasGeneratedBy` and `wasAttributedTo` without defining Dataset. DataCite 4.6 treats Version as optional and uses relation types for major-version identity; 4.7 is a compatible vocabulary extension, not a new type. ODCS is a contract document dialect (live v3.2.0; the base is still pinned near v3.1.0). JSON Schema identifies schema resources. ISO/IEC 11179 separates data-element concept, conceptual domain, value domain and representation.

No portable standard requires a fused Dataset+Schema+Contract personality. The missing piece is constraint promotion, not a third master.

## ACCEPTANCE SCENARIO
One dataset keeps a stable abstract identifier. Two delivery formats are two Distributions of one DatasetVersion, each with its own media type, byte size and checksum. A later structural change issues a new WM-DAT-004 contract version. Dataset version advances only if content or the published compatibility outcome requires it; schema/contract version is free to move on its own. The new dataset version carries a predecessor pointer and PROV assertions. Compatibility mode and check outcome are published; the dataset breaking flag is derived from that outcome, not asserted independently. The catalogue record continues to point at the same dataset. The negative case — a new CSV minting a new semantic dataset — is already rejected by DCAT 3 and WM-DAT-001.

This path holds only if the joining rules below are required. Installed as-is, both bases allow the scenario to fail: checksum, version-pin, compatibility outcome and predecessor may all be omitted.

## PORTABLE CONSTRAINTS
Retain in the reusable Enterprise profile (pin WM-DAT-001 `0.3.0-research.1` and WM-DAT-004 `0.3.0-research.1`):

- Stable abstract dataset identifier plus a version-scoped identifier on every release.
- Checksum on every distribution of a published dataset version.
- Version-pinned contract reference and recorded comformance status.
- One contract version across all distributions of one dataset version.
- Required compatibility mode and a published compatibility-check outcome.
- Dataset breaking-change flag derived from that outcome.
- Declared consumer scope and an explicit change-notice path (existence of the path, not its SLA).
- Predecessor and provenance assertions required when a dataset version is issued.
- Authoritative term and value-domain bindings for designated critical data elements.

Deployment policy, not profile semantics: notice-period length and channel; which properties are designated critical; consumer-registration enforcement; master-system and PID-scheme choice (DOI-per-version versus abstract-plus-version, provided the policy is explicit); licence catalogue; SLA and freshness numbers; choice of ODCS dialect beyond “pin a version.”

## HOLDS
Both bases are `adjudicationStatus: reviewable-draft` and `publishableCanonical: false`. Open source holds that actually block canonical publication:

- Live re-fetch and version-pin of WM-DAT-001 sources; DataCite 4.6 versus 4.7 citation-vocabulary consistency.
- ODCS source pinning and the v3.1.0 `dataProduct` deprecation contradiction versus live v3.2.0.
- ISO/IEC 11179-3:2023 and 11179-31:2023 remain catalogue-level; clause-level evidence is hypothesis only.
- Multi-profile SHACL validation (DCAT-AP 3.0.0 and at least one further profile) is unrun.

These holds sit on the bases. They do not create a missing aggregate. A non-canonical Enterprise profile draft is still appropriate: it can pin the two research versions, state the tightening rules, and inherit the holds instead of claiming they are closed.

## PUBLICATION RECOMMENDATION
Publish EM-DAT-01 as an Enterprise profile companion, not as a new subject model and not as a silent reuse map. Version-pin both bases. Do not mint a DatasetSchemaContract identity. Keep catalogue-record, data-product, lineage and quality-engine ownership with their existing models. Ship as `reviewable-draft` with `publishableCanonical: false` until the inherited source, ODCS, 11179 and SHACL holds close. Fixture the acceptance scenario (one dataset, two distributions, later schema version, predecessor plus derived compatibility) before any canonical claim.
