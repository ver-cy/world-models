## Verdict

**PROFILE.** No new model ID. EM-KNW-01 decomposes cleanly onto three reserved identities: **WM-REC-001** (Document/Record, its revisions, instantiations and carriers), **WM-KNW-006** (Concept, designation, definition), **WM-KNW-018** (Taxonomy/Classification Scheme, releases, in-scheme structure and mappings). The contour's fifth candidate type, `KnowledgeArticle`, needs no identity of its own: WM-REC-001 already carries `record status` with `document-not-captured | captured-record | nonrecord-copy`, so a wiki page is a document under that model until capture and an ADR is a captured record. `TermDefinition` is not an entity either — it is a designation plus definition inside WM-KNW-006. What EM-KNW-01 must produce is a binding profile with an ownership rule, not a fourth model.

## Aggregate boundaries

- **Record (WM-REC-001, aggregate).** Revisions and instantiations have no lifecycle outside the record; holds, tombstones and last-copy rules span them. Revision therefore stays inside the boundary as `versionIdentifier` / `versionSequence` / `versionState`, never as a sibling model.
- **File, URL, carrier.** Not identity. A file is an `instantiation` with `carrierType`, `mediaType` and a `storageLocation` *reference*; PREMIS's File/Bitstream-versus-Intellectual-Entity split is the governing distinction. One record may span many files; one file may carry many records.
- **Concept (WM-KNW-006, entity).** Persistent identifier independent of label, language, scheme and format. Reified designation stays subordinate (recorded reservation for a future split), because no designation is minted or resolved without a governing concept identifier.
- **Scheme (WM-KNW-018, aggregate).** Justified as a separate root only by its **release**: an immutable, digest-bound publication with its own approval gate, change set and predecessor chain. That is a lifecycle concepts do not have.
- **Document ↔ Concept** never touch directly. A document's index terms resolve through a classification binding (WM-XCT-020) that pins a concept IRI *and* a scheme release — not a label.

## Ownership reconciliation

The overlap is real and is a dual-master defect, not a wording difference: WM-KNW-006's `in_scope` claims scheme membership, top-concept status, relations and mappings, while WM-KNW-018's scope claims concepts, labels, definitions, relations, mappings and releases. Both models' own adjudications already flag it (WM-KNW-006 defers `topConceptOf`/`inScheme` system-of-record; WM-KNW-018 holds its parent direction).

**Recommended rule — master by identity dependence, not by subject area:**

> If a fact ceases to mean anything when you delete a scheme release, the **scheme** masters it. If a fact survives the deletion of every scheme, the **concept** masters it.

- **WM-KNW-006 masters:** concept identifier and IRI, intension (characteristics, delimiting characteristic, extension boundedness), definitions with their authoritative source, designations with type/rating/language/script, subject field, and the identity-level lifecycle — deprecation, merge, split, redirect, never-reuse.
- **WM-KNW-018 masters:** scheme identity and namespace, releases and change sets, and every **release-scoped assertion**: membership (`inScheme`, `topConceptOf`), in-scheme `broader`/`narrower`/`related`, collections, facets, arrays, cross-scheme mappings with method and confidence, plus the approval and validation gates that publish them.
- **Single master per assertion.** The reified membership/relation/mapping assertion is the only editable record. The concept-side view of "which schemes am I in" is **derived and marked derived**; WM-KNW-006's `membership assertion mode` already exists for exactly this and must be pinned to *derived* in the profile.
- **Standalone identity preserved.** SKOS permits zero-scheme concepts and WM-KNW-006 records that; so a concept is valid, citable and exportable with no scheme. The `maintenance scheme reference` (0..1) is the only place a scheme touches intrinsic state, and only to publish it.
- **Two deprecations, not one.** Concept retirement (global, identifier never reused, successor or advisory alternatives) belongs to WM-KNW-006. Scheme-local withdrawal — the concept leaves this taxonomy's release while staying active elsewhere — belongs to WM-KNW-018 and must not set the concept's `deprecated flag`.

## Required profile

1. Demote WM-KNW-018's "owns concept definitions, labels" to *pins concept versions by reference*; demote WM-KNW-006's membership/relation/mapping `in_scope` claims to derived views plus assertion references. Both are text amendments, not model changes.
2. Relax WM-KNW-006's `bound release reference` from cardinality **1** to **0..1**, or define a concept-register release. As frozen it is unsatisfiable for a scheme-less concept — the exact case the ownership rule must preserve.
3. Resolve in the registry whether WM-KNW-018 *is* WM-KNW-006's declared parent WM-KNW-002 or a distinct scheme model. The profile must not assume it; WM-KNW-006's relationship contract is empty and `contains_ids` blank.
4. Require the classification binding to carry concept IRI + scheme release; forbid label-based indexing in WM-REC-001's `fn-classify-record`.
5. Add the record-part access scope WM-KNW-006's own audit demands, so a licensed or disputed definition can be restricted below finding level.
6. Add a **dispute state at definition level** (attributable, readable, non-resolving). Disputed ≠ deprecated, and a disputed concept is never redirected.
7. State in both models that a content digest is evidence of byte state, never identity.

## Invariants

1. No version without a fixing event; every revision carries generating activity, issuing authority and change note.
2. Lexical equality never implies same-as. `exactMatch` requires an authorised assertion with a basis note and is disjoint from `broadMatch` and `relatedMatch`.
3. An accepted term holds only in its stated subject field, language and region; no designation without a BCP 47 tag.
4. Carrier change never changes identity: a new URL, file or format yields at most a new instantiation or version. Identifiers are never reused after disposition or migration; tombstone plus migration map survive.
5. Digest ≠ identity. Two instantiations of one version may differ by digest; one digest shared by two records merges nothing. A mismatch raises an integrity incident, never a silent repair.
6. Exactly one master per assertion; concept-side membership and relations are derived and read-only there.
7. Issued versions and published releases are append-only; sequences are never renumbered.
8. Supersession does not authorise destruction, and deprecation preserves resolvability under a stated guarantee.
9. Concepts need no scheme; multiple definitions on one concept require a context discriminator plus source, and differing intension forces two concepts.

## Scenario walkthrough

**Negative case — rejected on both limbs.** A page republished at a new URL changes a `storageLocation` on an instantiation. Identity is `recordIdentifier` with declared `identifierGranularity`; no fixing event, no new version; no new knowledge. Conversely, identical `preferred labels` do not merge: the duplicate test is intensional (delimiting characteristic, definition comparison, notation, shared authoritative source), homographs are separated by subject field and qualifier, and merge requires a decision record with a survivorship rule. "Bank" in finance and hydrology stays two concepts whose designations are lexically equal and semantically unrelated.

**Acceptance case — passes.** Migration keeps `recordIdentifier`; the target system's local id is recorded as `alternateIdentifier` with equivalence basis and assertion datetime. `versionSequence` is never renumbered; the append-only version history, fixity values, custody transfer receipt (verify before dispatch, re-verify on receipt) and exchange package manifest let the receiver reconstruct identity, version chain, fixity and events. Renormalisation for the new store is a derivative instantiation with its own provenance, and any signature bound to the old digest is invalidated rather than migrated. The two conflicting definitions survive as two concepts under distinct subject fields, each with its own language-tagged definition and authoritative source; if intension is in fact identical and only the authority differs, one concept carries both definitions with a context discriminator and a precedence rule — never a silent winner.

## Gaps and publication holds

All three models are `reviewable-draft` with `publishableCanonical: false`; two rest on owner-authorised single-provider waivers (WM-KNW-006 Claude-only, WM-KNW-018 Codex-only), and WM-REC-001's ISO, eIDAS and RiC/C2PA version holds stand. No semantic crosswalk between the contour and any reserved ID has been verified, so blocking decision two is unmet and this verdict is a boundary decision only. Assertion- and decision-level identity — the contour's claim that statements and decisions have their own references — is covered by none of the three; route it to EM-KNW-02 rather than minting anything. Evidentiary tiers route to EM-LEG-01. Publication of the profile stays held until the crosswalk is completed, the WM-KNW-002/WM-KNW-018 parentage is resolved, the release-cardinality and access-scope amendments land, and both scenarios above are run as executable fixtures.
