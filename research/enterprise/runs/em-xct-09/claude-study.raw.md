I'll start by checking which sources I can actually access.# EM-XCT-09 S1: Independent design study of the Enterprise Classification Review boundary

## 0. Source access

This is design research only. I made no external writes, ran no validator, and computed no hashes.

**Read in this session:**
- **WM-XCT-020 spec.yaml**, truncated. I read the publication block, scope, boundary notes, sources, and the binding-foundation, binding-specification and binding-assertion bundles. The fetch stopped at the start of the authority-and-legal-effect layer, so I did not read the lifecycle, migration, dispute or protection bundles.
- **WM-KNW-018 spec.yaml**, truncated partway through the mapping bundle. I did not read its lifecycle, validation, access or projection bundles.
- **Neither predecessor's AGENTS.md.**
- **SKOS Reference**, through §10.6.5 (it cut off in §10.6.6). I did not reread §10.6.7–10.6.8 in this session. The exactMatch-is-not-owl:sameAs point therefore comes from the brief and my prior knowledge, not from this session's reading.
- **FHIR R5 §4.1**, in full.
- **XKOS**, in full.
- **OpenRefine "Reconciling"**, in full.
- **Vercy Meta-Model-Composition**, in full.
- **OWL 2 New Features**, §2.4.1.

**Not fetched:** Extension-Model.md, the XCT-040 README, SHACL, and PROF. Claims about those four below are marked **[brief/unverified]**.

I did not verify the two SHA-256 values. The fetched text is a rendered copy and may not be byte-identical to the published files.

## 1. Observations on the predecessors (source, not inference)

**XCT-020 publication status.** It is a published, reviewable draft, not canonical, produced in dual-provider mode (Claude and Grok), at version 0.3.0-research.1. Its scope explicitly includes bindings derived from cross-scheme mappings or version correspondences, and the marking of their derived status, while mapping tables themselves are out of scope and belong to a sibling.

**XCT-020 scheme version is optional.** The scheme-version data element has cardinality 0..1. A review packet that requires a pinned release is therefore a stricter local rule, not something inherited from XCT-020.

**XCT-020's OWL-DL claim needs qualification.** Its boundary note says OWL-DL prevents treating SKOS concepts as classes. The SKOS Reference, however, deliberately makes no statement relating skos:Concept to owl:Class, and shows a resource typed as both skos:Concept and owl:Class as consistent. OWL 2 DL relaxes the OWL 1 name separation (punning), and its Direct Semantics treats different uses of the same name as completely separate. The accurate statement is narrower: a shared IRI does not carry an interpretation across roles. It is not true that dual typing is forbidden.

**XCT-020 over-generalises a FHIR rule.** Its FHIR source note says external value-set bindings must pin a version. In FHIR R5 that rule appears in the list of rules for required bindings on the `code` datatype outside a Coding. It is not a general law, and the new package should not cite it as one.

**KNW-018 publication status.** It is a published reviewable draft with a single-provider waiver (Codex; Claude and Grok waived). Its boundary note calls the registry parent direction toward XCT-020 apparently reversed or navigational and holds it for review, and it claims ownership of mapping assertions and their status while leaving evidence and reviewer decisions as external records.

**KNW-018 template defects, confirmed.** Bundle and layer descriptions contain "Resource Consumption" template text. Every finding repeats the same three templated questions. Question `kind` values are mismatched: the version finding's third question is typed "security", and the mapping-status finding has a question typed "spatial". Each finding has a single opaque `object` data element. Nothing in it is executable or testable as an instance schema.

**A cross-model inconsistency.** XCT-020 points mapping ownership to a "Concept Mapping / Correspondence model (sibling)". KNW-018 claims mapping ownership itself. No separate mapping model appears in either document. The new package must not become the third claimant.

## 2. Boundary and candidate disposition

I support an independently identified companion that assesses and never asserts. I disagree with exporting all seven candidate types as local domain objects. Composition §4.2 says code references carry scheme URI and version rather than copying members, and a snapshot must be marked as such with source identifier and capture Event. That makes five of the seven candidates snapshots or references, not domain objects.

| Candidate | Disposition | Mechanism |
|---|---|---|
| ClassificationReviewPacket | Local entity, exported | Owned here |
| ClassificationAssessment | Local entity, exported | Owned here |
| CodeReference | Value object, exported (scheme, release, code) | EMBED |
| SchemeReleaseSnapshot | Marked immutable snapshot of a KNW-018-class release | REFERENCE plus snapshot-EMBED |
| SlotProfileSnapshot | Snapshot of an XCT-020 slot profile | Snapshot |
| AssignmentSnapshot | Snapshot of an XCT-020 binding assertion | Snapshot |
| CrosswalkSnapshot / MappingEntry | Snapshot of KNW-018 mapping assertions or an external correspondence | Snapshot |

**Scope is too broad in one respect.** "Proposed migration disposition" overlaps XCT-020's claimed migration scope. The resolution: the assessment emits a disposition as a finding. Executing a migration and recording its result remain an XCT-020 host act.

**Scope is too narrow in another.** Profile-derivation checking (case 7) is valuable without any assignment present. The packet should allow a profile-only purpose.

## 3. Primary-source comparison

**SKOS Reference, W3C Recommendation 2009, §§4.6.1, 10.3–10.6.5.** SKOS declares exactMatch symmetric and transitive (S44/S45) and closeMatch intransitive. It notes there is no way to close a concept-scheme boundary, so SKOS can describe a scheme but cannot completely define it. Notations uniquely identifying a concept within a scheme is only a convention.

Design consequences:
- A "finite allowed set" cannot come from SKOS. It must come from a snapshot that explicitly declares itself a complete enumeration.
- A no-chain runtime must not say "A and C are not equivalent". SKOS entails A exactMatch C from the chain. The correct output is that chain-derived equivalence is outside this assessor's execution scope. Entailment and authorisation to act are different things.

**DDI XKOS, §5 (versioning, variants) and §7 (correspondences).** The published document describes itself as the first DDI Alliance publication, with copyright 2014–2019. Each major version of a classification is a separate concept scheme, and XKOS is agnostic about whether a new version mints new item URIs or reuses the old ones. A ConceptAssociation may relate any number of sources to any number of targets, including 0-to-n cases for created or vanished items, and multiple sources or targets are interpreted as a union.

Design consequences:
- MappingEntry must be n:m with possibly empty sides. It must never be decomposed into pairwise equivalences.
- XKOS's own example lists the same target concept twice in one association. In RDF that collapses to a single triple; in a JSON array it does not. This is a real round-trip hazard (case 9).

**FHIR R5 §4.1, Normative.** System plus code is unique, and a version may be needed where the code system lacks concept permanence. For required bindings on CodeableConcept, at least one Coding must be present and one of the Codings must come from the value set. Derived profiles over a required binding may remove codes but not add them. Preferred and example bindings let derived profiles bind any value set they choose.

Design consequence: "narrowing only reduces" is well-defined only when the base is required (or, with care, extensible). The S1 runtime should support `required` only and refuse other strengths as unsupported. It must not import FHIR's healthcare obligations as general law.

**OpenRefine reconciliation (an actual open system).** Matched cells keep the original string alongside the matched entity, and judgments, action type and timestamps are recorded. That is the right shape: original value, candidates, judgment. It also offers a bulk "match each cell to its best candidate" action and a way to apply one match to every cell with the same original string. These are exactly the two anti-patterns this package must refuse: highest score as approval (case 3), and label-keyed global reuse (case 2).

**Vercy Composition, Working Draft.** Its rubric maps codes and classifications to REFERENCE, and a connector change should trigger compatibility assessment rather than silent migration. The package should adopt that rule as its central premise.

**SHACL [brief/unverified].** I did not reread it. The intended analogue is that SHACL separates validation results from processing failures. I adopt a four-way outcome, described in §5.

**PROF [brief/unverified].** PROF is a Working Group Note. I am relying on the brief's summary that a profile description is not evidence that any instance was validated.

**Alternatives compared:**
- A FHIR terminology server using `$validate-code` and ConceptMap: mature, but online, healthcare-bound, and permissive toward chains and "equivalent" relations.
- XKOS correspondence tables: statistically honest n:m, but with no approval workflow.
- OpenRefine: good capture of evidence, but weak separation of authority.

The proposed package takes XKOS's cardinality, FHIR's derivation rule, and OpenRefine's evidence shape, and removes every automatic commit.

## 4. Invariants

1. **Qualified codes.** A CodeReference is the triple (scheme, release, code). All three are required and compared byte-exact, with no case folding, Unicode normalisation or IRI normalisation. Display text is never part of identity.
2. **Local conservative identity across releases.** Codes in different releases are not assumed identical unless the release snapshot declares concept permanence. This is stricter than FHIR, which treats system plus code as unique when permanence holds.
3. **Content addressing.** Every snapshot carries a source reference, a capture event (actor, instant, method) and a SHA-256 digest over an RFC 8785 JCS canonical form. The packet ID is the digest of its canonical body. A digest mismatch produces `rejected-input`.
4. **Closed-world membership only from declared completeness.** Membership is decided only against a snapshot declaring `completeness = complete-enumeration`. Otherwise the result is `insufficient-context`. Absence of data never validates.
5. **Duplicate code entries** within one release snapshot or allowed set produce `rejected-input`. They are never silently deduplicated.
6. **Narrowing preserves the parent.** A narrowing profile must pin its parent by (ID, version, digest) and carry the same subject identity class, slot ID and slot-meaning digest. The allowed set must be a subset of the parent's; the minimum cardinality may only rise and the maximum only fall; the scheme release must be unchanged. Any violation produces `rejected-input` with disposition "explicit migration required".
7. **Supported binding strength.** Narrowing is defined only over a base strength of `required`. Other strengths produce `unsupported`.
8. **No subject identity change.** The assessment never outputs a subject ID, never proposes a subject-ID change, and never writes to a subject.
9. **Scores are evidence.** Candidate scores, name similarity and model confidence are recorded as evidence and never order, filter or select a disposition.
10. **Approval is external.** Only mapping entries with review status `approved` and an attributed approval authority are eligible to produce a candidate target. The assessment cannot approve anything.
11. **Directness.** Only entries whose source set contains the assigned CodeReference are considered. Any inference through an intermediate concept produces `unsupported` (chain), with the chain recorded.
12. **Single-target gate.** A candidate target is produced only when exactly one applicable, approved exactMatch entry with a single-element target set survives. Two or more distinct surviving targets produce `human-review-required`, with every one preserved.
13. **Profile exclusion is not refutation.** When a narrowing profile excludes a competing target, that alternative is annotated as "excluded by profile P". It is not deleted, and its presence still blocks automatic disposition unless the parent-profile policy explicitly delegates tie-breaking. S1 has no such delegation.
14. **Two separate temporal questions.** Historical conformance is evaluated against the release pinned at the assignment's assertion time. Current eligibility is evaluated at the packet's `evaluationInstant` against the target release. Neither result implies the other.
15. **Retired targets.** A retired, deprecated or not-selectable target is never eligible for a new assignment. A historical assignment to it stays readable and historically assessable.
16. **Model-ID migration is refused.** Any CodeReference or mapping whose scheme is a Vercy model-identifier namespace produces `unsupported`, "manual semantic and installation migration required", regardless of mapping strength.
17. **Idempotence.** Identical packet bytes and the same assessor version produce byte-identical assessments. `generatedAt` equals the `evaluationInstant`, not the wall clock.
18. **Authority context is mandatory.** Missing actor, purpose or disclosure basis produces `rejected-input`. The assessor never infers authority.

## 5. Fields, relations and cardinalities

**ClassificationReviewPacket**

| Field | Cardinality | Notes |
|---|---|---|
| packetId | 1 | Digest |
| packetSchemaVersion | 1 | |
| purpose | 1 | {conformance-check, migration-review, profile-derivation-check} |
| requestedBy | 1 | |
| onBehalfOf | 0..1 | |
| disclosureBasis | 1 | |
| evaluationInstant | 1 | RFC 3339 |
| supersedesPacket | 0..1 | |
| schemeReleases | 1..n | |
| baseProfile | 1 | |
| narrowingProfile | 0..1 | |
| assignment | 0..1 | Required unless purpose is profile-derivation-check |
| targetRelease | 0..1 | Required for migration-review |
| mappingEntries | 0..n | |
| context | 1 | {jurisdiction 0..1, tenant 0..1, usage 0..n} |

**SchemeReleaseSnapshot**

| Field | Cardinality | Notes |
|---|---|---|
| schemeRef | 1 | |
| releaseId | 1 | |
| capture | 1 | |
| digest | 1 | |
| completeness | 1 | {complete-enumeration, partial, unknown} |
| conceptPermanence | 0..1 | |
| concepts | 0..n | Each: code 1, status 1 ∈ {active, deprecated, retired, not-selectable}, definitionDigest 0..1 |

**SlotProfileSnapshot**

| Field | Cardinality | Notes |
|---|---|---|
| profileId | 1 | |
| version | 1 | |
| digest | 1 | |
| parent | 0..1 | {id, version, digest} |
| subjectIdentityClass | 1 | |
| slotId | 1 | |
| slotMeaningDigest | 1 | |
| strength | 1 | |
| allowedSet | 1..n | CodeReference |
| cardinality | 1 | {min, max} |

**AssignmentSnapshot**

| Field | Cardinality | Notes |
|---|---|---|
| sourceBindingRef | 1 | |
| subjectRef | 1 | Opaque |
| subjectIdentityClass | 1 | |
| slotId | 1 | |
| value | 1 | CodeReference; single coding only in S1 |
| origin | 1 | {human, model-suggested, mapping-derived, imported} |
| method | 0..1 | {id, version}; mandatory when origin is model-suggested |
| score | 0..1 | |
| assertionTime | 1 | |
| validTime | 1 | |
| sourceRevision | 1 | |
| capture | 1 | |
| digest | 1 | |

**MappingEntrySnapshot**

| Field | Cardinality | Notes |
|---|---|---|
| entryId | 1 | |
| mappingSetRef | 1 | |
| sources | 1..n | |
| targets | 0..n | |
| relation | 1 | {exactMatch, closeMatch, broadMatch, narrowMatch, relatedMatch, union-association, unspecified} |
| reviewStatus | 1 | {candidate, approved, rejected, contested, superseded} |
| approvalAuthority | 0..1 | Required when approved |
| contextScope | 0..1 | |
| capture | 1 | |
| digest | 1 | |

**ClassificationAssessment**

| Field | Cardinality | Notes |
|---|---|---|
| assessmentId | 1 | Digest of packetId plus assessor version |
| packetId | 1 | |
| assessor | 1 | {id, version} |
| checks | 1..n | Each: checkId, outcome ∈ {conforms, does-not-conform, insufficient-context, unsupported, rejected-input}, findings 0..n {code, path, evidenceRefs, question 0..1} |
| migrationDisposition | 0..1 | {not-needed, candidate-target, human-review-required, blocked} |
| candidateTarget | 0..1 | |
| preservedAlternatives | 0..n | |
| nonClaims | 1..n | Fixed list: not an assignment, not an approval, no chain semantics, no access grant |

**Relations.** There are three separate graphs:
- Instance relations: packet → snapshots, and assessment → packet.
- Specification dependencies: the package cites XCT-020 and KNW-018 but imports neither.
- Delivery graph: the host submits the packet and receives the assessment.

**Fact governance.** The host is owner and master of every snapshotted fact. The package is the writer only of the assessment. The read purpose is `packet.purpose`. Conflicting source revisions are preserved as separate snapshots, never merged. Retention follows the host.

## 6. Lifecycle, time and authority

The packet has two states. Host-side drafting is out of scope. Once the digest is computed the packet is sealed and immutable. A correction is a new packet with `supersedesPacket`; history is never edited.

The assessment is issued once and is immutable. Supersession is recorded by the host, never by the package.

There are four distinct times: capture time, assertion time, valid time and evaluation instant. A historical correction to an assignment arrives as a new AssignmentSnapshot with a higher `sourceRevision`. When two snapshots claim the same `sourceBindingRef` with different revisions and both are authoritative, the result is `insufficient-context`, with the question "which revision is authoritative for this review?". The package holds no authority; its outputs are advice to a host workflow.

## 7. Decision tables

**Profile narrowing**

| Condition (checked in order) | Outcome |
|---|---|
| Parent missing, or parent digest mismatch | rejected-input: explicit migration |
| Base strength ≠ required | unsupported |
| Identity class, slot ID or slot-meaning digest changed | rejected-input: new profile, not a narrowing |
| Any release pin differs from the parent | rejected-input: migration review |
| Allowed set ⊄ parent set, or duplicates present | rejected-input |
| min falls or max rises | rejected-input |
| Subset with min ≥ 1, and removed codes include a residual or "other" code | conforms, with a coverage-loss warning finding |
| Otherwise | conforms |

**Mapping to disposition**

| Condition | Disposition |
|---|---|
| Assigned code in a Vercy model-ID namespace | blocked: manual model migration |
| Assigned code active in the target release, and the target release is the same scheme with declared permanence | not-needed |
| Any applicable entry is contested, or competing revisions exist | human-review-required |
| No applicable approved entry | human-review-required ("no approved direct correspondence") |
| Only a chain would connect source and target | unsupported (chain), with the chain listed |
| Surviving approved exactMatch entries yield more than one distinct target | human-review-required, all preserved |
| One surviving entry, but n:m, union, close, broad or narrow | human-review-required |
| One approved, direct, 1:1 exactMatch, target active and selectable, and allowed by the effective profile | candidate-target |
| The single target is retired or not selectable | blocked, with the question "which successor?" |

## 8. Bundle > Layer > Finding > Question > Artifact/Action

**Example 1**
- Bundle: Migration review
- Layer: Correspondence evidence
- Finding: A split successor cannot be chosen automatically
- Question: "Which evidence about subject S distinguishes successor B1 from B2 under release r2's scope notes?"
- Artifact: Assessment check `MIG-SPLIT`
- Action: the host routes the case to a steward. No write occurs.

**Example 2**
- Bundle: Profile derivation
- Layer: Constraint monotonicity
- Finding: The derived profile widens the maximum cardinality
- Question: "Is this a new profile rather than a narrowing?"
- Artifact: check `PRF-CARD`, outcome rejected-input
- Action: none.

## 9. Five-facet coverage

| Type | Identity/class | Direct properties | Recognition | Capabilities | Context/evidence |
|---|---|---|---|---|---|
| Packet | Content digest; class ReviewPacket | §5 | Schema version plus digest recomputation | Submit (host); assess (package) | Requester, purpose, disclosure basis, evaluationInstant |
| Assessment | Derived digest | Checks, disposition, non-claims | Assessor ID/version; reproducible from packet | Read-only; none mutating | Packet ref, evidence refs per finding |
| CodeReference | Value equality over the triple | scheme, release, code | Byte-exact match | Compare only | Carried by its enclosing snapshot |
| Snapshot envelope | sourceRef + revision + digest | Captured payload | Digest verification | None (frozen) | Capture event, source, completeness |

## 10. Tests by context

**Startup**
- Positive: scheme `proj-cat` release r1 is complete; the base profile allows {DESIGN, BUILD, OPS}; the narrowing allows {BUILD, OPS}; an assignment to BUILD conforms. `subjectRef` is identical in the packet and the assessment.
- Negative: an assignment to DESIGN does not conform under the narrowing profile, while still conforming under the base profile. Both results are reported.
- Negative (case 7): a narrowing that adds MARKETING, pins r2, or changes the identity class is rejected-input.

**International group (case 2)**
- `A` exists in both `schemeDE|2026` and `schemeFR|2026` with different definition digests.
- Negative: an assignment carrying only code `A` plus the display text "A — Agriculture" is rejected-input (missing scheme and release); the display is never used for lookup.
- Negative: a mapping entry scoped to `jurisdiction=DE` is not applied in a packet whose context is FR; the result is human-review-required with the reason "context mismatch".
- Positive: a fully qualified `schemeDE|2026|A` conforms.

**AI team (case 3)**
- Two model-suggested candidates score 0.99 and 0.98, both carrying method `clf@4.2`.
- The assessment preserves both with their scores and flags them as unapproved, and the disposition is human-review-required.
- Negative: a model-suggested assignment with no method version is rejected-input.
- The fixtures contain no personnel or eligibility subjects; the synthetic subjects are documents.

**Remaining cases**

| Case | Scenario | Expected result |
|---|---|---|
| 4 | r1 `X` split into r2 {X1, X2} via one 1:n union association | Historical conformance of the r1 assignment passes; disposition is human-review-required; X1 and X2 are both listed; no name-similarity ranking |
| 5 | Chain A→B→C, plus B broadMatch D | unsupported (chain) for C. Findings state that SKOS would entail A exactMatch C, but this assessor does not act on entailments. broadMatch is never a candidate |
| 6 | Two approved exactMatch entries A→T1 and A→T2 | human-review-required. A narrowing excluding T2 annotates T2 as excluded, and the result remains human-review-required |
| 8 | Retired target; release with `completeness=unknown`; altered digest; duplicate code; value set given by rule without expansion | blocked; insufficient-context; rejected-input; rejected-input; unsupported, respectively |
| 9 | Missing disclosure basis | rejected-input |
| 9 | Two authoritative revisions | insufficient-context |
| 9 | Same packet imported twice | Byte-identical assessment |
| 9 | JSON → RDF → JSON round trip of an entry with a repeated target | Digest mismatch detected, never "equal" |
| 9 | Downgrade dropping `release` | rejected-input |
| 10 | Legacy ID "Taxonomy Scheme v0" name-matched to WM-KNW-018 | blocked, regardless of relation or approval |

## 11. Minimum versus deferred scope

**S1 minimum:**
- JSON packets only.
- Strength `required` only.
- Single-coding assignments.
- Direct entries only.
- The five outcomes and two decision tables above.
- Synthetic fixtures for every row.

**Deferred:**
- Extensible bindings with the FHIR "no applicable code" judgment.
- Multi-coding CodeableConcept-style assignments.
- Chain execution under an explicit, authorised policy.
- RDF/SKOS ingestion with set semantics.
- Value-set expansion by rule.
- Level-aware XKOS checks.
- A FHIR projection.

## 12. Pitfalls and strongest counterexamples

**"This is just a FHIR terminology server."** This is the strongest objection. The reply: this package is offline, domain-neutral and assertion-free, and it keeps a FHIR projection possible. If Vercy hosts already run FHIR, the package should wrap `$validate-code` output rather than compete with it.

**"Exact-only migration almost never fires."** Statistical correspondences are routinely n:m, so the automatic path covers mostly renames and permanence-preserving releases. The value lies in structured questions, not automation. That should be stated plainly rather than implied otherwise.

**Semantic drift under an unchanged code.** When the same code in the same release is re-published with an edited definition, only `definitionDigest` catches it. Without that digest the assessor silently passes.

**Narrowing can create unclassifiable subjects.** Removing a residual code from an exhaustive slot with min ≥ 1 does exactly that. This is why the narrowing table includes a coverage-loss warning.

**Implementation leaks.** UI sorting by score is an implicit tie-break. Canonicalisation must avoid NFC normalisation and locale-dependent number formatting.

## 13. Disagreements with the brief

1. Five of the seven candidate types should be marked snapshots or value objects, not exported domain objects.
2. "Code identity includes release" is a deliberate local rule that is stricter than FHIR. Document it as such.
3. The finite-set closure must come from declared snapshot completeness. SKOS cannot close a scheme.
4. Narrowing semantics must be restricted to `required` strength.
5. The migration disposition must not duplicate XCT-020's migration ownership.
6. The XCT-020 OWL-DL warning and its external-version rule both need correction before anything cites them.

**Smallest usable publication:** Packet and Assessment schemas, the CodeReference and snapshot-envelope schemas, the 18 invariants, the two decision tables, and roughly 30 synthetic fixtures. It should carry no conformance claims beyond "passes its own fixtures".

## 14. Research limitations

- Both predecessor specifications were read only partially, and their AGENTS.md files were not read.
- SHACL, PROF, Extension-Model and XCT-040 were not read. Anything about them comes from the brief.
- SKOS §10.6.7–10.6.8 were not reread in this session.
- I verified no digests and executed nothing; all tests above are designed, not run.
- XKOS section numbers follow its own table of contents. The rendered page did not number its headings.
- I made no legal or ISO claims and adopted none from the predecessors.