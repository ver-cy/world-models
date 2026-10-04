# Frozen no-tools semantic audit — EM-KNW-01

You are the final static semantic auditor. Use only this frozen packet. Do not browse, call tools, invent identifiers, mutate registry reservations or grant publication authority.

Disposition: PROFILE over WM-REC-001, WM-KNW-006 and WM-KNW-018; no new catalogue or runtime identifier. Audit semantics only.

Audit questions:
- Do Knowledge Article, Document Revision and Term Definition correctly remain designations or aggregate-owned parts rather than independent aggregates?
- Does the single-master rule cleanly separate intrinsic concept facts from release-scoped scheme assertions?
- Are record/version/instantiation, digest, classification and concept identity kept distinct?
- Do the fixtures cover scheme-less concepts, local withdrawal, global retirement, definitions, migration and identity failure modes?
- Which holds permit a research profile but block canonical publication?

Return at most 600 words with exactly: Verdict (ACCEPT WITH LIMITS, REVISE, or REJECT); Critical findings; Required holds; Scenario result; Identifier decisions. Registry mutation and identifier allocation remain holds.

## Profile candidate

{
  "format": "vercy-enterprise-profile-candidate/v1",
  "contourId": "EM-KNW-01",
  "name": "Enterprise Document, Knowledge and Terminology",
  "decision": "PROFILE",
  "newRuntimeId": false,
  "bases": ["WM-REC-001", "WM-KNW-006", "WM-KNW-018"],
  "constraints": [
    "Every assertion has one editable master: facts that survive removal of every scheme are concept-owned, while facts that lose meaning without a pinned scheme release are scheme-owned; all cross-model views are derived and read-only.",
    "WM-REC-001 owns stable record identity, immutable versions, instantiations, custody, retention and disposition; Knowledge Article is a documentary-form designation and Document Revision is record-owned.",
    "WM-KNW-006 owns concept IRI, intension, intrinsic definitions, designation inventory and global retirement, merge, split, redirect and tombstone semantics.",
    "WM-KNW-018 owns scheme identity, immutable releases, release-scoped membership, top-concept status, hierarchy, collections, facets, arrays, mappings and scheme-local preferred, admitted, deprecated or withdrawn designation selection.",
    "Intrinsic genus or differentia definitions remain concept-owned; scheme-local scope and editorial notes remain release-owned and cannot overwrite intrinsic definitions.",
    "A concept may exist with zero scheme memberships; later membership or withdrawal is an append-only scheme-release assertion and never changes concept identity.",
    "WM-XCT-020 classification binds subject identity, concept IRI, scheme IRI and exact scheme release; copied labels are display-only and label-only classification is invalid.",
    "Knowledge Article genre or documentary form is referenced through an exact governed vocabulary release and is never hard-coded as record identity.",
    "A URL, file, path or carrier is a location or instantiation and never record identity; a move changes neither record nor version unless a fixing event changes content or a declared significant property.",
    "Digest proves byte state and never record, version or concept identity; equal digests merge nothing and a mismatch raises an integrity event rather than silent repair.",
    "Lexical equality never establishes concept identity; identical intension may retain multiple sourced contextual definitions, while differing essential characteristics require distinct concepts.",
    "Definitions preserve source, provenance, language, context, status, access scope and dispute state; disputed never means deprecated and cannot silently redirect a concept.",
    "Concept retirement is global and preserves resolvability, tombstone and identifier non-reuse; scheme-local withdrawal affects only that release and never globally deprecates the concept.",
    "Published record versions and scheme releases are append-only, never renumbered and never silently repointed; supersession does not authorize destruction."
  ],
  "candidateRevision": 2,
  "references": ["WM-XCT-020"],
  "holds": [
    "WM-REC-001, WM-KNW-006 and WM-KNW-018 remain non-canonical reviewable drafts and this profile cannot promote ahead of them.",
    "WM-KNW-006 and WM-KNW-018 need reciprocal scope and relationship amendments that remove dual mastership of definitions, designations, membership, hierarchy and mappings.",
    "WM-KNW-006 bound-release cardinality must permit a scheme-less concept or define a concept-register release.",
    "WM-KNW-002 versus WM-KNW-018 parentage and the reversed WM-XCT-020 relationship remain unresolved registry holds.",
    "Definition-level access and dispute semantics and exact classification-release pins are not yet ratified in the base contracts.",
    "Licensed standards remain alignment evidence only until exact editions and usable clause crosswalks are pinned.",
    "Independent assertion and decision identity remains delegated to EM-KNW-02."
  ]
}


## Fixtures

{
  "format": "vercy-enterprise-profile-fixtures/v1",
  "profileName": "Enterprise Document, Knowledge and Terminology",
  "cases": [
    {"id":"url-move","kind":"positive","input":"An unchanged record moves to a new URL.","expect":"Record and version identity persist; only the location or instantiation changes."},
    {"id":"format-migration-preserved","kind":"positive","input":"A migration creates a new format while all declared significant properties remain unchanged.","expect":"A new instantiation with provenance and digest remains attached to the same record version."},
    {"id":"transformative-migration","kind":"positive","input":"A migration changes a declared significant content property.","expect":"A fixing event creates a new immutable record version without renumbering history."},
    {"id":"same-word-different-fields","kind":"positive","input":"The same word appears in two distinct subject fields with different essential characteristics.","expect":"Distinct concept IRIs remain; lexical equality establishes no identity."},
    {"id":"same-intension-conflicting-definitions","kind":"positive","input":"Two authorities publish conflicting definitions for the same intension.","expect":"One concept may retain both sourced contextual definitions with language, status, access and dispute state."},
    {"id":"different-intension","kind":"positive","input":"Two definitions use one label but differ in essential characteristics.","expect":"Distinct concepts are required and may be related only by an authorized mapping."},
    {"id":"exact-release-classification","kind":"positive","input":"A record classification identifies the subject, concept IRI, scheme IRI and exact release.","expect":"WM-XCT-020 owns a reproducible binding; any copied label is display-only."},
    {"id":"scheme-less-concept","kind":"positive","input":"A concept exists before joining a scheme and is later withdrawn from one release.","expect":"Concept identity persists with zero memberships; entry and withdrawal remain release-local assertions."},
    {"id":"global-retirement-versus-local-withdrawal","kind":"positive","input":"One scheme withdraws an active concept and the concept is later globally retired.","expect":"The local withdrawal and global tombstoned retirement remain separate events with separate masters."},
    {"id":"scheme-local-preference","kind":"positive","input":"Different schemes prefer different designations for one concept.","expect":"The designation inventory stays concept-owned while each preference is owned by its pinned scheme release."},
    {"id":"scope-note-versus-definition","kind":"positive","input":"A scheme publishes a scope note that narrows use without changing concept intension.","expect":"The scope note remains release-owned and cannot overwrite the intrinsic concept definition."},
    {"id":"label-only-classification","kind":"negative","input":"A record is classified using only a display label.","expect":"The classification is rejected because concept, scheme and exact release pins are absent."},
    {"id":"digest-equals-identity","kind":"negative","input":"Matching bytes are treated as proof that two records or concepts are identical.","expect":"The identity inference is rejected."},
    {"id":"dual-editable-master","kind":"negative","input":"Concept and scheme stores both edit the same membership or hierarchy assertion.","expect":"Validation rejects dual mastership and requires one release-owned assertion plus derived views."},
    {"id":"identifier-reuse","kind":"negative","input":"A retired concept identifier is silently repointed to a new meaning.","expect":"Validation rejects reuse and requires the original tombstone and an explicitly new identifier."}
  ]
}


## Local evidence

# EM-KNW-01 local synthesis

## Disposition

- Create an **Enterprise document, knowledge and terminology profile** over WM-REC-001, WM-KNW-006 and WM-KNW-018.
- Do not create a new catalogue or runtime identifier.
- Treat Knowledge Article as a document/record designation and Term Definition as concept-owned descriptive content, not independent aggregate roots.
- Route independently identified assertions and decisions to EM-KNW-02 rather than expanding this contour.

## Aggregate boundaries

WM-REC-001 owns the stable record identity, immutable version chain, instantiations, custody, evidence and disposition. A URL, file or carrier is a location or instantiation, never the record identity. Document Revision remains owned by the record because retention, holds, supersession and last-copy rules span the full aggregate.

WM-KNW-006 owns a concept's persistent identity and intrinsic meaning: delimitation, characteristics, definitions with sources, designations with language/script/context, global deprecation, merge/split and successor continuity. A concept remains valid and citable outside any scheme.

WM-KNW-018 owns scheme identity, namespace, immutable releases and every release-scoped assertion: membership, top concept, in-scheme relations, facets, collections and mappings. It references pinned concept versions; it does not become a second master for intrinsic concept content.

## Ownership rule

If an assertion loses its meaning when the scheme release is removed, the scheme masters it. If it survives removal from every scheme, the concept masters it. Every assertion has one editable master; concept-side membership/relation views are derived and read-only.

Concept retirement and scheme-local withdrawal are different operations. Retirement preserves the globally resolvable concept identifier and successor guidance. Withdrawal removes a concept from a scheme release without deprecating it elsewhere.

## Required profile constraints

1. A document classification binding pins concept IRI and exact scheme release; a label alone cannot classify a record.
2. A new URL or storage system creates a new location/instantiation reference and, only after a fixing event, possibly a new version. It does not create new knowledge identity.
3. Content digest proves byte state, not document or concept identity.
4. Concept equality requires an authorised identity/mapping assertion with basis and context. Lexical equality never establishes same-as.
5. Definitions retain source, provenance, language, subject field, jurisdiction/audience context, status and dispute state. Disputed does not mean deprecated.
6. Scheme-less concepts are allowed; release binding must therefore be optional or point to a concept-register release rather than an unrelated scheme release.
7. Published record versions and scheme releases are append-only and never renumbered.

## Acceptance result

A migrated document keeps its record identifier and complete version sequence. The target system ID becomes an alternate identifier with assertion provenance; format conversion is a derived instantiation with its own digest and event. Existing signatures remain bound to their original bytes.

Two identical words in distinct subject fields remain two concepts. Two competing definitions may remain on one concept only when their intension is the same and each definition retains its authority and context; otherwise they identify distinct concepts. No silent merge or preferred winner is inferred.

## Holds

All three bases are reviewable drafts with `publishableCanonical: false`. WM-KNW-006 and WM-KNW-018 have independent-review waivers; WM-REC-001 retains source/version and cross-profile holds. WM-KNW-006 and WM-KNW-018 currently overlap in ownership text, their registry relationship is unresolved, and definition-level access/dispute semantics need amendment. This checkpoint is research evidence, not an installable release.


## Claude independent study

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


## Grok independent study

**Verdict: PROFILE.** No new model ID. The five tests produce no fourth identity kind. REUSE ONLY would leave WM-KNW-006 and WM-KNW-018 dual-mastering the same assertions. NEW MODEL would duplicate record-version, concept-definition, or classification-binding identity already published as reviewable drafts.

FACT: EM-KNW-01 is the contour “information object, revisions, publications, concepts and definitions; the file is a carrier; claims and decisions have their own references.” Independently identified assertions stay in the claim/decision contour (WM-KNW-007). Classification binding already exists as WM-XCT-020.

## Aggregate boundaries

**WM-REC-001 Document / Record** masters stable record identity, immutable versions, instantiations, evidence, custody, retention and disposition. File, URL, path, repository key and carrier are not record identity.

FACT (ISO 15489-1): identity characterises the record; content and metadata may coexist in multiple locations; location change does not rewrite identity. FACT (ISO 23081): identity metadata is distinct from place; classification cites an authorised scheme; title is a name, not an identifier. FACT (PREMIS / OAIS): Intellectual Entity ≠ Representation ≠ File; digest is fixity of a file or bitstream, not identity. FACT (MoReq2010): the record entity is discrete, complete and immutable; a content pointer may change without minting a new record.

**WM-KNW-006 Concept / Term** masters persistent concept identity, delimitation/characteristics, intensional definitions, the designation inventory (sign + language/script/context/acceptability), and global concept lifecycle including retirement/tombstone. A concept may have zero scheme membership.

FACT (ISO 1087:2019): concept = unit of knowledge created by a unique combination of characteristics; concepts are not bound to a natural language; designation = sign denoting a concept in a domain/subject; definition = descriptive statement that differentiates a concept. FACT (ISO 704:2022): objects are abstracted into concepts; concepts are represented by designations and/or definitions; homonymy = identical designations for different concepts. FACT (ISO 11179): a definition is a representation of a concept in a context. FACT (ISO 30042 TBX): definition sits under the concept/language set; term sections hold designations, not definitions.

**WM-KNW-018 Taxonomy / Classification Scheme** masters scheme identity, immutable releases and change-sets, release-scoped membership, top-concept, hierarchy/collection/facet/array as published in that release, notations, scheme-local notes, and mappings pinned to source and target releases.

FACT (SKOS): Concept and ConceptScheme are disjoint; `inScheme` is optional and not transitive; concept URIs stay stable across scheme versions; version URIs are separate; `prefLabel` uniqueness is per resource per language tag, not global. FACT (ISO 25964): the identifier designates the concept; preferred-term uniqueness is per language inside one thesaurus; mapping is concept-to-concept, pinned to vocabulary versions.

**WM-XCT-020** (already published, not this contour) masters the binding: subject + concept IRI + scheme IRI + exact release. Display labels are never identity. REC-001 may store the binding reference; it must not store an orphan label as classification.

## Correction to the 006 / 018 overlap

Proposed single-master rule, accepted with one terminology tightening:

> If an assertion loses its meaning when a scheme release is removed, the scheme masters it. If it survives removal from every scheme, the concept masters it.

Apply it as follows (INFERENCE on published scopes; FACT against ISO/SKOS):

- **006 masters:** concept IRI, delimitation, intensional definitions, designation inventory, global lifecycle.
- **018 masters:** scheme identity, append-only releases, release-scoped membership, top-concept, hierarchy/collection/facet as published in that release, notations, scheme-local scope/editorial/history notes, mappings pinned to releases, and which designation is preferred/admitted/deprecated *inside that release*.
- Scheme-local preference is 018; the sign itself remains 006. That is how two subject fields may prefer the same string without collapsing two concepts.
- Not every text called “definition” is concept-owned. A genus-differentia definition that still describes the concept after every scheme is gone is 006. A scope note that dies with the release is 018.
- Concept-side `inScheme` / broader / mapping views are derived and read-only.
- Concept retirement ≠ scheme-local withdrawal. Zero-scheme existence is permitted.

Both published scopes currently violate this: 006 in-scope still names membership, hierarchy and mappings; 018 purpose/in-scope still names concept identity, labels and definitions; neither composition ledger references the other. That overlap is the PROFILE correction, not a reason for NEW MODEL. Do not collapse 006 into 018 (that would forbid concept-without-scheme). Do not let 006 edit release graphs.

## Knowledge Article, Document Revision, Term Definition

**None needs a separate aggregate.**

- **Knowledge Article** is a documentary-form designation of a REC-001 record (draft/publish/archive + append-only versions). Genre is a scheme value, not an identity kind. Claims inside an article, if independently asserted, belong to the deferred claim contour.
- **Document Revision** is owned by the record as an immutable version (sequence, fixing event, issuing agent, supersession). Instantiation and location stay off the version identifier. A change-history mixin may supply mechanics; it is not an EM-KNW-01 identity.
- **Term Definition** is concept-owned descriptive content on 006, each value carrying source, language, context and status. TBX and ISO 1087 treat definition as an element of the concept entry, not an independently identified object. If the same text is published as a glossary page, that publication is a REC-001 record of those bytes — two roles, not two identity kinds. Conflicting authorities are multiple definition values, or two concepts when delimitation differs.

## Scenario results

1. **New URL or system move.** Record identity unchanged. Version identity unchanged unless the move also fixes a new content state (authorised amendment or significant-property change). Instantiation/location changes. Format migration that preserves significant properties → new instantiation of the same version. Transform that alters significant properties → new version plus new instantiation; prior version remains append-only. A reminted local key is a qualified alias, not a new master. Matching digest evidences same byte state, not same record identity.

2. **Same preferred label, different subject fields.** Two concept IRIs. Lexical equality never proves same-as. Each 018 release may prefer the same string locally. 006 holds two designation records, each qualified by subject field/context.

3. **One word, two conflicting definitions.** Do not key identity on the word. Same intension → one concept with two definition values, each with source/language/context/status. Different essential characteristics → two concepts sharing a designation (homonymy). Authority is provenance, not identity.

4. **Document classified.** Binding must cite concept IRI + scheme IRI + exact release. Copied label is display only. Binding master is WM-XCT-020; scheme release is 018; record is REC-001.

5. **Concept outside any scheme, then enters and leaves a release.** 006 identity, definitions and designations persist throughout. 018 records membership only in releases that include it. Withdrawal is scheme-local, not retirement. Re-entry is a new membership assertion in a new append-only release. Identifiers remain resolvable.

## Required constraints

1. One assertion, one editable master (rule above).
2. Lexical equality of label, title or filename never proves same-as.
3. Digest evidences byte state of an instantiation, never identity of record or version.
4. Every definition carries source + language + context + status.
5. Preferred-in-scheme is 018; designation inventory is 006.
6. Published record versions and scheme releases are append-only; in-place edit after fixing is forbidden.
7. Identifiers remain resolvable after deprecation or disposition (tombstone, no reuse, no silent repoint).
8. Classification binding cites concept IRI + scheme IRI + exact release; label copy is not identity.
9. Concept-side membership/relation/mapping projections are read-only.
10. File, URL, path, repository key and carrier never equal record identity.
11. Do not invent a catalogue or runtime identifier for this contour.

## Gaps and publication blockers

Primary blocker: dual mastership 006↔018 with empty relationship contracts. PROFILE must rewrite both in-scope/out-of-scope statements and add REFERENCE composition both ways before either draft can go canonical.

All three candidates remain reviewable drafts under single-provider waiver, live-source and paywalled-ISO holds (704, 1087, 25964, 15489, 23081 unread at clause level). No clause-level conformance claim is licensed from secondary descriptions.

WM-XCT-020 is still a candidate with a reversed-parent hold against 018; scenario 4 cannot close until that joint review. 006 currently states preferred-designation uniqueness per language as concept-global; that collides with ISO 25964 per-scheme uniqueness and must be split as above. Definition versus scope note is not distinguished in either published scope. Documentary-form vocabulary for “Knowledge Article” is not pinned; PROFILE must cite a scheme/release rather than hard-code a genre. Independent records, terminology and library-science review remains open. Claims and decisions stay out of this contour.

## Provider comparison

# EM-KNW-01 provider comparison

Claude and Grok independently select **PROFILE** over WM-REC-001, WM-KNW-006 and WM-KNW-018 with no new catalogue or runtime identifier. Knowledge Article is a documentary-form designation, Document Revision is record-owned and Term Definition is concept-owned. Independently identified assertions and decisions remain outside this contour and route to EM-KNW-02.

Both providers apply one ownership rule: an assertion that survives removal of every scheme is concept-owned; an assertion that loses meaning without an exact scheme release is scheme-owned. WM-KNW-006 therefore masters concept identity, intension, intrinsic definitions, designation inventory and global lifecycle. WM-KNW-018 masters immutable releases and release-scoped membership, hierarchy, mappings, notes and designation preference. Cross-model concept views are derived and read-only.

Both keep record identity separate from URL, path, file, carrier and digest. A move changes only location or instantiation; a declared significant-property change creates a fixing event and new version. WM-XCT-020 classification must pin subject, concept IRI, scheme IRI and exact release. Lexical equality and byte equality establish no semantic identity.

Grok sharpened the distinction between intrinsic definition and scheme-local scope note, made preferred designation release-scoped, and confirmed that scheme-local withdrawal differs from global concept retirement. It also requires definition-level source, language, context, access and dispute state.

Canonical publication remains held by non-canonical bases, overlapping WM-KNW-006/018 authority, optional scheme-binding cardinality, unresolved WM-KNW-002/018 and WM-XCT-020 parentage, and unratified definition access and dispute semantics. Standards remain alignment evidence until exact editions and usable crosswalks are pinned.

