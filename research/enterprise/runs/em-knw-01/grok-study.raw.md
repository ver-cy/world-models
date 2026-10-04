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