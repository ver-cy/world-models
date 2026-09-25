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
