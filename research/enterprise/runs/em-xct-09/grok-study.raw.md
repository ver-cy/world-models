# EM-XCT-09 S1 Design Memo — Enterprise Classification Review

**Document:** independent design study, revision S1 · **Date:** 2026-09-22  
**Status:** research memo only. Not a specification, not a validator run, not a publication-authority claim.  
**Team:** Grok (lead), Harper, Benjamin, Lucas.

The brief is treated as a proposal to challenge. Claims are labeled **observation**, **inference**, **proposal**, or **unverified**.

A downloadable copy of this memo is attached at the end.

## 1. Access log and claim hygiene

**Observation.** Public pages were opened through a page summarizer and saved fragments, not as byte-complete four-file packages and not as independently hashed streams.

- WM-KNW-018 `spec.yaml` / `AGENTS.md`: purpose, scope, boundary notes, composition, research adjudication. Published `synthesisSha256` on the page: `416e453789412773cfb3b0f2a163aea354d36473928dd6231b844f6f84a36433`. Single-provider Codex waiver; Claude and Grok waived.
- WM-XCT-020 `spec.yaml` / `AGENTS.md`: purpose, in/out of scope, neighbor distinctions, slot/assignment/authority/time fragments, canonicalization prose. Published `synthesisSha256`: `8672e6ca2404422f41ebdae9e319b5767fbbfeb6b117c1a707a05ff6f739cf9f`. YAML publication head: `providerMode` dual-provider, providers Claude and Grok. Reviewable-draft. The public catalogue also labels both predecessors “installable”; that label is not treated here as executable conformance.
- Vercy Extension Model and Meta-Model Composition (working drafts), XCT-040 0.1.1 README, public Enterprise card for EM-XCT-09.
- W3C SKOS Reference (Rec 18 Aug 2009) §10 / §10.6; DDI XKOS HTML §5 / §7; HL7 FHIR R5 (5.0.0) `terminologies.html`; OpenRefine reconciling manual; W3C PROF WG Note 18 Dec 2019; W3C SHACL Rec 2017 selected validation clauses; OWL 2 New Features Rec 2012 F12.

**Not accessed as normative text:** ISO 11179 / 25964; SKOS Primer body; SHACL-SPARQL appendix; PROF worked examples; KNW-018 / XCT-020 question-tree bodies, fixtures, or validators; any private account.

**Unverified.** The brief’s spec SHA-256 pins (`89cadb00…`, `47aa90ca…`) do not match the published `synthesisSha256` values above. These are different digest fields until a later audit hashes bytes. This study does not recompute SHA-256 and does not claim inherited executable conformance. “No validator or fixtures in the published four-file packages” is accepted from the brief as a labeled summary, not as an observation confirmed by opening those packages.

## 2. Boundary and candidate disposition

**Observation.** The public Enterprise card describes EM-XCT-09 as “a contract for concept schemes, codes, versions, profiles and exact/broad/narrow/related mapping relations,” queued / being researched. Candidate types listed on the card: `ClassificationScheme`, `CodeAssignment`, `SemanticMapping`, `ProfileConstraint`. Card questions (when is a mapping exact; how to carry a deprecated code; how a profile narrows without changing identity) and card invariants (similar name is not exactMatch; classifier version is pinned; a profile does not change identity silently) are usable. The type names and the blurb collide with KNW-018 and XCT-020.

**Observation from predecessors.** KNW-018 owns the scheme aggregate and leaves classified objects, bindings, and reviewer decisions outside. XCT-020 owns the reified binding and the slot specification, and leaves scheme content and correspondence-table authoring to siblings. KNW-018 records a held parent signal toward XCT-020 as reference, not subtype. Neither package, in what we could read, ships an executable instance schema.

**Proposal.** Keep the brief’s companion shape; reject the card’s master types. EM-XCT-09 is an independently identified shared contract that assesses a bounded immutable review packet. It is not a taxonomy, not a binding pattern, and not a subtype of either predecessor. Published-companion language (“associated with …; it is not its subtype”) is the right relationship.

**Exported first-class types** (own identity, owner, purpose, lifecycle): `ClassificationReviewPacket`, `ClassificationAssessment`.

**Embedded snapshot value objects** (marked snapshot + source identifier + capture event + digest; never local masters): `SchemeReleaseSnapshot`, `SlotProfileSnapshot`, `AssignmentSnapshot`. `CrosswalkSnapshot` is deferred; S1 flattens to `MappingEntry[]` on the packet.

**Embeds / references, not exported masters.** `CodeReference` = `(schemeId, releaseId, code)` verbatim; display label is evidence only. `MappingEntry` = cited row plus local review fields. Scheme, concept, subject, actor, authority instrument, live binding, live mapping table, and any WM-ID / package identity remain REFERENCES.

**Closed output records** (not five-facet entities): `AssessmentOutcome`, `MappingDisposition`, `Question`.

**Reject as this contract’s types:** card candidates `ClassificationScheme`, `CodeAssignment`, `SemanticMapping`, `ProfileConstraint`. Those names would mint a third master.

**Scope critique.** The brief is slightly too broad if snapshots become editable taxonomies or if “proposed migration disposition” is readable as write-back into XCT-020 `migrate-bindings-across-scheme-versions`. It is slightly too narrow if the assessment cannot emit a concrete `Question` or an `unsupported-semantics` token — cases 5, 8 and 9 then have nowhere to land. Right-sized S1: deterministic offline `assess(packet) → assessment`. The engine never installs a meta-model, never changes a subject ID, never assigns a live code, never approves its own mapping, never grants access, and never selects current evidence. Host retains authority and custody.

## 3. Predecessor holds

**KNW-018, 0.3.0-research.1, reviewable-draft, Codex-only waiver.** Owns one governed versioned scheme (identity, releases, concepts, labels, relations, mappings, governance). Quoted out of scope: equating labels with identity, closeMatch with exactMatch, or mapping with proved equivalence. Mapping-assessment neighbor: scheme owns mapping assertions; reviewer decisions remain external; mapping never merges concept identity. XCT-020 neighbor: binding assigns an external object to a concept in a pinned release; parent direction “appears reversed or navigational and remains held for review.” Coverage text already distinguishes transitive exactMatch from closeMatch and from OWL sameAs. Question trees were not fully read; Resource Consumption template language is not copied.

**XCT-020, 0.3.0-research.1, reviewable-draft.** Owns the reified binding and the design-time slot. Out of scope: scheme internals and correspondence-table authoring. Must “never redefine or cache scheme semantics as authoritative.” Binding only records that a given assertion was derived through a mapping and with what fidelity. The old “scheme sibling unregistered” hold is partially stale; the mapping sibling and parent-direction hold remain open. No executable instance serialization in the text we read. S1 must refuse live `commit-binding`, `migrate-bindings-across-scheme-versions`, `erase-binding`, `revoke-binding`. Review proposes; host performs.

**Other holds.** XCT-020 canonicalization prose mixes NFC, IRI normalisation, a ban on case folding, and “publisher's own convention” — not a precise algorithm. S1 compares tokens verbatim as supplied; host normalization is host provenance. The OWL-DL warning needs punning qualification (§4.7); S1 runs no OWL. EU BTI / GDPR / ISO 11179 sentences are unverified alignment prose and are not adopted. Extension Model: import does not transfer semantics or authority; incompatible behavior needs a new local concept. Composition: codes are REFERENCE; snapshot copies must mark source + capture Event and must not become a local master taxonomy. XCT-040 0.1.1: byte pins; nested validators are not auto-run; no MMAS certification; no automatic Dimension upgrade. Neighbor contracts EM-XCT-01…08 and EM-XCT-10 must not be forked. EM-XCT-05 lists classification-adjacent candidate names on a disclosure/retention card; that is neighboring-card naming hygiene, not a published assignment master. WM-XCT-036 (alias / same-as mapping) is a collision risk for chain semantics; S1 states its own no-chain rule rather than inheriting one.

## 4. Primary-source comparison

Compared approaches: SKOS mapping properties (conceptual IR alignment), XKOS statistical correspondence (n:m versioning), FHIR R5 terminology binding (healthcare slot practice), and OpenRefine reconciliation (an actual open system that separates value, score and judgment). PROF, SHACL and OWL 2 are constraint / validation / identity cautions, not imported engines.

### 4.1 SKOS Reference — W3C Rec, 18 August 2009, §10 / §10.6

`skos:exactMatch` is transitive and symmetric, a sub-property of non-transitive `skos:closeMatch` (§10.1, §10.6.3). Example 62: A–B and B–C entail A exactMatch C. §10.6.8: `owl:sameAs` / `equivalentClass` are typically inappropriate across schemes (label and scheme membership collapse). ExactMatch is disjoint with broadMatch and relatedMatch (§10.3–10.4). Nothing in §10 forbids multiple exactMatch links from one concept.

**Inference.** “Exact mapping warranted” is not “one exactMatch ⇒ unique live assignment.” A single-eligible-target rule is a declared stricter local decision and must preserve competing entries. No-chain is application authorization, not a rewrite of §10.6.3. Say `unsupported-semantics`, not “exactMatch is not transitive.”

### 4.2 XKOS — DDI Alliance vocabulary, §5 / §7

Each major version is a `skos:ConceptScheme` (`follows` / `supersedes`, `dcterms:valid`). §7 `ConceptAssociation` is n:m, including 0-to-n when items appear or disappear. Multiple sources or targets are a union, not pairwise equivalences. Split, merge, and empty sides are first-class. Exploding a union row into silent pairwise exacts is a defect.

### 4.3 FHIR R5 (5.0.0) terminologies

Code system ≠ value set ≠ binding. Strengths: required, extensible, preferred, example. Required on `CodeableConcept` means at least one `Coding` from the value set; other Codings may be translations; text is not a substitute. Required does not mean every coding is a member. Do not import these strengths as enterprise law. Unexpanded value-set URLs are `insufficient-context`. Healthcare constraints are out of scope.

### 4.4 OpenRefine reconciliation (open system)

Original cell value is retained. Scores and “best candidate” facets exist; bulk auto-match exists. Docs still require human review. Judgment (`none` → `matched`) is distinct from score. Case 3 must keep both 0.99 and 0.98 plus method/version. Confident auto-match is a counterexample, not a pattern.

### 4.5 PROF WG Note, 18 December 2019 — not a Rec

A profile constrains or guides other specs (`prof:isProfileOf`). Role `validation` “supplies instructions about how to verify conformance.” **Inference** (not a single quoted sentence): profile description ≠ instance validation. Assessment is a separate artifact. PROF inheritance is not executed.

### 4.6 SHACL Rec 2017

A node conforms iff the result set is empty **and** no failure is reported. Failure (ill-formed shapes, unsupported entailment) ≠ invalid data. Unsupported entailment MUST fail. S1 never treats silence as conformance.

### 4.7 OWL 2 New Features Rec 2012, F12

The same IRI may be class and individual; Direct Semantics treats the uses as separate. Interpretation does not transfer. A code used as concept, class name, and assigned term does not inherit class reasoning. S1 runs no OWL reasoner.

## 5. Local invariants

I1. The engine consumes only packet bytes plus declared digests. It does not mutate the packet.  
I2. Every snapshot records source identifier, exact version/release, capture event/time (RFC 3339), digest algorithm, and digest. Unmarked copies are rejected.  
I3. Scheme, concept, and subject identifiers remain references. The engine never mints, rewrites, or replaces them.  
I4. Code identity is `(publisherScheme, release, code)` compared verbatim. No automatic IRI normalisation, Unicode fold, or case fold in increment 1.  
I5. Packet and Assessment have their own identity, owner, purpose, and lifecycle. They are not projections of referenced subjects.  
I6. A derived profile MUST pin parent profile id and parent digest, and MUST retain subject `identityClass` and slot meaning.  
I7. A derived profile MAY only reduce the allowed set and/or tighten cardinality. Adding codes, widening cardinality, changing scheme or release, changing parent digest, or changing `identityClass` is not a restriction.  
I8. Migration across code system or release is a separate review kind, never a profile restriction.  
I9. Classifier output, name similarity, and numeric confidence are proposal evidence only. `max(score)` is not approval.  
I10. Only a single approved **direct** exact correspondence, with selectable target, complete pinned releases, sufficient declared context, and no competitor, MAY emit a migration **candidate**. It MUST NOT emit a committed assignment.  
I11. Nonexact, split/merge, disputed, competing, chained, or under-specified mappings require human review. No silent tie-break.  
I12. Mapping-chain execution is unsupported in S1. Conceptual SKOS entailment is acknowledged; authorized equivalence is not emitted.  
I13. Missing release content, digest mismatch, incomplete snapshot, duplicate code in a closed set, unknown expansion, retired/nonselectable target, or missing actor/purpose/disclosure ⇒ `fail-closed` or `insufficient-context` plus a concrete Question. Absence of data is not validity.  
I14. Historical readability of an old assignment is independent of eligibility for a new assignment now.  
I15. Two approved directs to distinct targets both remain visible even if a narrower profile excludes one from eligibility.  
I16. Classification exactness cannot authorize WM-ID / model-identity replacement or package execution. Runtime refuses automatic model-ID migration.  
I17. Unsupported external semantics are rejected as `unsupported-semantics`, not implied-conformant.  
I18. Repeated identical packet import is idempotent on `(packetDigest, rulesetVersion)`. A new assessment id may be minted; it does not create a new approval.

## 6. Fields, relations, cardinalities

Closed syntax. Finite enumerations. No executable expressions. No inherited OWL entailment.

`ClassificationReviewPacket`: `packetId` 1; `ownerRef` 1; `purpose` 1; `actorRef` 1; `disclosureAuthority` 1; `schemeSnapshots` 1..n; `baseProfile` 1; `narrowingProfile` 0..1; `assignmentSnapshot` 0..1; `mappingEntries` 0..n; `context` 1 (may record `none-declared`); `packetDigest` 1; `sealedAt` 1.

`SchemeReleaseSnapshot`: `sourceSchemeIRI` 1; `releaseId` 1; `capturedAt` 1; `capturerRef` 1; `digest` 1; `members` 0..n as packet content, not master; selectable/retired flags per member.

`CodeReference`: `schemeIRI` 1; `releaseId` 1; `code` 1; `conceptIRI` 0..1 (cannot replace scheme+code); `displayLabel` 0..1 (non-identity).

`SlotProfileSnapshot`: `profileId` 1; `parentProfileId` 0..1; `parentDigest` 0..1; `schemeIRI` 1; `releaseId` 1; `identityClass` 1; `slotMeaning` 1; `allowedCodes` 0..n; `minCard` 1; `maxCard` 1. Empty allowed set is valid only if `minCard = 0`.

`AssignmentSnapshot`: `subjectRef` 1; `identityClass` 1; `codeRef` 1; `assertedBy` 0..1; `methodRef` 0..1; `validFrom`/`validTo` 0..1; `status` 1.

`MappingEntry`: `sourceRef` 1; `targetRef` 1; `predicate` 1 ∈ {exact, close, broad, narrow, related, split, merge, unspecified}; `approvalState` 1; `authorityRef` 0..1; `confidence` 0..1; `methodRef` 0..1; `competingEntryIds` 0..n.

`ClassificationAssessment`: `assessmentId` 1; `packetRef` 1; `packetDigest` 1; `rulesetId` 1; `assessedAt` 1; `outcome` 1; `findings` 1..n; `questions` 0..n (≥1 when outcome ∈ {insufficient-context, human-review-required, fail-closed}); `proposedMigrationCandidate` 0..1 and only if outcome = `propose-migration-candidate`; `committedAssignment` MUST be absent.

`Question` embed: `{id, kind, missingEvidence, blocking}`.

Fact envelope on Packet and Assessment (referenced to host models, not re-owned): owner, master=host, writer, read-purpose, valid-time, provenance, conflict, retention.

Outcome tokens (one vocabulary; `MappingDisposition` uses the same set): `pass-conforming` | `fail-closed` | `insufficient-context` | `unsupported-semantics` | `human-review-required` | `propose-migration-candidate` | `reject-not-a-restriction` | `refuse-model-id-migration`. Historical readability is a finding flag on an assignment snapshot, not a ninth outcome.

## 7. Lifecycle, time, authority

Packet states: assembled → sealed (digest frozen) → assessed → superseded-by-new-packet. Assessment states: computed → recorded. Assessment never transitions a packet into “approved mapping” or “assigned.”

Times stay distinct (RFC 3339 if present; missing is a Question, not default-now): subject-state time, assignment-asserted-at, snapshot-captured-at, packet-sealed-at, assessed-at, optional valid-from/valid-to. A pass at time *t* does not authorize assignment after scheme, profile, or authority change. Historical assignment readable at captured-at does not imply eligible-at assessed-at.

Required on packet context: `actorRef`, `read-purpose`, `disclosureAuthority`. Missing any is I13, not anonymous pass. Authority to classify, to map, to narrow a profile, and to install a model package are four different host authorities. This companion has none of them. Conflicting authoritative revisions: preserve both; `conflict=true`; disposition `human-review-required`. Lossful downgrade (dropped digest, capture, or authority fields) fails closed. Snapshot round-trip must preserve verbatim `CodeReference` and digest.

## 8. Decision tables

### 8.1 Profile narrowing

| Condition | Outcome |
|---|---|
| Parent missing or parent digest ≠ digest(base) | `fail-closed` / invalid packet |
| Scheme or release differs | not a restriction; open migration review |
| `identityClass` differs | `refuse-model-id-migration` |
| Slot meaning differs | `reject-not-a-restriction` |
| Allowed set ⊆ parent AND cardinality ≤ parent AND pins unchanged | accept as narrowing |
| Allowed set adds a code OR cardinality wider | `reject-not-a-restriction` |
| Narrowing excludes one of two competing exact targets | eligibility may drop one; evidence of both remains |
| Retired/nonselectable code listed as allowed | `fail-closed` |

### 8.2 Mapping / migration disposition

| Evidence | S1 disposition |
|---|---|
| Single approved direct exact; target selectable; context sufficient; no competitor | `propose-migration-candidate` (not assignment) |
| Two or more approved exacts to distinct targets | `human-review-required`; preserve both; no tie-break |
| ExactMatch chain A–B–C | `unsupported-semantics`; do not emit A ≡ C |
| Broad / close / related / name-similarity only | `human-review-required`; not an exact candidate |
| Split 1→N, merge N→1, or 0-side association | `human-review-required` + evidence Question; historical assignment remains readable |
| AI candidates 0.99 / 0.98 | suggestion-only; preserve ambiguity + method/version |
| Retired / nonselectable target | not eligible now; historically readable |
| Missing scheme, version, or digest | `insufficient-context`; do not resolve from label |
| Literal code reused across schemes | distinct `CodeReference`s; contextual map is not global |
| Legacy WM-ID name match | `refuse-model-id-migration` |

Exact correspondence is warranted only when all of: direct (not chained), approved by a named authority, single target after profile filter, target selectable in the pinned release, context explicit, pair not marked disputed. Even then the output is a candidate.

## 9. Minimum versus deferred

**Minimum usable S1 publication:** Packet + Assessment as exported types; three snapshot embeds plus `MappingEntry`; closed enums; invariants I1–I18; tables 8.1–8.2; synthetic fixtures for cases 1, 2, 3, 4, 5, 7, 8, 10; explicit non-conformance to SKOS/SHACL/FHIR/PROF as executable engines; explicit refusals in §2. A companion validator may be specified later. This memo does not claim one was executed.

**Deferred:** mapping-chain policy; intensional value-set expansion; polyhierarchy / broader-closure; confidence calibration; multilingual label negotiation; post-coordination; negative classification; legal-effect bindings; correspondence authoring; `CrosswalkSnapshot` as a separately governed object; live XCT-020 write-back; automatic model-ID / package installation; any ERP replacement.

## 10. Bundle → Layer → Finding → Question → Artifact / Action

Invented structure. Not copied from KNW-018 question trees.

**B1 Review boundary and custody.** L1 companion is not a scheme — Q: does this object mint scheme or concept identity? Expected: no. L2 snapshots are not master taxonomies — Q: is every embedded code list marked snapshot + source + capture + digest? L3 actor, purpose, disclosure — Q: which host authority supplied this packet, for what read-purpose?

**B2 Pinned scheme and profile.** L4 release integrity — Q: does declared digest match captured bytes? L5 restriction versus migration — Q: allowed set ⊆ parent AND cardinality tightened AND scheme/release/`identityClass`/parent digest unchanged?

**B3 Qualified assignment.** L6 assignment versus suggestion — Q: is any numeric score being treated as approval? L7 historical versus current — Q: is this a readability check on an old release or an eligibility check for a new assignment?

**B4 Crosswalk evidence.** L8 direct entries — Q: which predicate token applies? L9 competing and chained — Q: if two approved exact targets exist, were both retained with no tie-break? Q: is any A–B–C path being executed?

**B5 Assessment and refusals.** Artifact: assessment record + question list + optional non-committed candidate. L11 model-ID refusal — Q: does any name-similar WM-ID trigger automatic replacement? Expected: `refuse-model-id-migration`.

**Permitted actions:** `assess-packet`, `reassess-identical-packet`, `refuse-unsupported`, `refuse-model-id-migration`.  
**Forbidden actions:** `install-meta-model`, `assign-live-code`, `approve-own-mapping`, `migrate-bindings`, `execute-package`.

## 11. Five-facet coverage

Applied fully to the two exported types. Snapshot types receive a shorter note so the companion does not inflate into a registry.

**ClassificationReviewPacket.** Identity/class: `packetId`, local class, never a scheme or subject. Properties: purpose, owner, pinned snapshots, optional narrowing, optional assignment, mapping entries, context, digest. Recognition: capture event, completeness flags, digest match. Capabilities: assess, archive, supersede-by-new-id; forbidden assign/install/approve/migrate. Context/evidence: actor, purpose, disclosure, jurisdiction note, conflict flags, retention.

**ClassificationAssessment.** Identity/class: `assessmentId` bound to `packetId`+digest. Properties: outcome token, findings, questions, optional candidate, refused-actions, ruleset version. Recognition: assessed-at, engine version, input digest verified, unsupported-semantics flags. Capabilities: emit, reassess-idempotent-on-digest; forbidden live write or access grant. Context/evidence: method, rule citations, competing evidence retained, historical-versus-current split.

**Snapshots.** Identity is local snapshot id plus external source reference. Properties are the frozen allowed set, members, or mapping rows. Recognition is digest + capture event. Capabilities are compare and subset-test only. Context is source, capturer, time, integrity algorithm. `CodeReference` and `MappingEntry` are embeds, not five-facet exports.

## 12. Tests for three contexts, plus remaining cases

Invented vocabularies only. No production identifiers.

**Startup +.** Scheme `AcmeCat@rel1` members `{BILLABLE, INTERNAL}`; base profile card 1..1; narrowing allows `{BILLABLE}`; assignment `BILLABLE` on subject `S1` class `Project`. Expect `pass-conforming`; subject id unchanged.  
**Startup −.** Same packet, assignment `INTERNAL`. Expect `fail-closed`; subject id still `S1`. IdentityClass rewrite `Project→WorkItem` is `refuse-model-id-migration`, not a profile pass.

**International +.** Two snapshots, `CA-NAICS@2022` code `A` and `FR-NAF@2021` code `A`, distinct concept IRIs. Context names jurisdiction CA. Expect resolution only of the CA pin; FR mapping is not reused.  
**International −.** Display label `A`, scheme and release omitted. Expect `insufficient-context` and Question: which publisher scheme and release minted this code?

**AI +.** Method `clf-v3`, candidates T1 0.99 and T2 0.98, no governed assignment, no personnel field. Expect `human-review-required`; both candidates and method/version retained.  
**AI −.** Engine commits T1 because it is highest, or drops T2. Expect `fail-closed` against I9.

**Remaining required fixtures.** (4) Split OLD→{NEW-P, NEW-Q}: historical readable; successor needs extra evidence; nearest-name rewrite forbidden. (5) Approved exact A→B and B→C plus close/broad links: chain is `unsupported-semantics`; close/broad ≠ exact. (6) Two approved exacts A→T1 and A→T2; narrowing allows only T1: both entries remain; eligibility may drop T2; no tie-break. (7) Profile that changes parent digest, `identityClass`, allowed-set, cardinality, or scheme release: `reject-not-a-restriction` or `refuse-model-id-migration`, never silent pass. (8) Retired target, missing members, digest mismatch, missing capture event, duplicate code, unexpanded value-set URL: `fail-closed` or `insufficient-context` + Question; never validate-by-absence. (9) Missing actor/purpose/disclosure; conflicting revisions preserved; identical sealed packet reimport idempotent on digest; lossful downgrade fails; round-trip preserves verbatim codes. (10) Label “WM-KNW-018” matched by name to `vr.wm-knw-018` with a request to install the package: `refuse-model-id-migration`. Classification exactness is not specification-compatibility review and does not authorize package execution.

## 13. Pitfalls, disagreements, publication

**Pitfalls.** Snapshot member list edited as a local taxonomy; SKOS §10.6.3 chain treated as authorization; XCT-020 NFC/IRI mix inherited as “the” algorithm; passing review used to invoke `migrate-bindings`; FHIR required-binding copied as enterprise law; OpenRefine-style confident auto-match; profile exclusion deleting competing mapping evidence; pass-by-absence when digest or members are missing; assessment accepted without actor/purpose/disclosure; name-matched WM-ID installer.

**Strongest later-audit counterexamples:** (a) SKOS-valid double exactMatch used as automatic unique target; (b) review-pass treated as live migration authority; (c) snapshot list promoted to master scheme; (d) normalisation changing a publisher code; (e) “narrowing” that actually changes release or `identityClass`.

**Disagreements with this brief, and team choices.**

1. The public card’s types overclaim ownership. Publish snapshot/packet/assessment types, not `ClassificationScheme` / `CodeAssignment` / `SemanticMapping`.
2. Brief SHA-256 pins disagree with published `synthesisSha256` values we retrieved. Treat both as unverified until a frozen audit hashes bytes.
3. Exact mapping is not one-to-one and is not authorization. SKOS allows multiple exactMatches; XKOS associations are n:m with empty sides. A local single-eligible-target rule must be labeled stricter-than-SKOS.
4. No-chain is an application refuse rule. Do not deny SKOS §10.6.3. Say unsupported.
5. `CodeReference` and `MappingEntry` are not exported five-facet types. `Question` and disposition tokens exist as closed records so case 8 can fail with a concrete question.
6. `CrosswalkSnapshot` as a separately governed object is deferred; `MappingEntry[]` on the packet is enough for S1.
7. XCT-020 already owns live migration. S1’s refusal is a deliberate subtraction, not inherited silence. Neighbor WM-XCT-036 is a collision risk; do not fork chain execution here.
8. “No automatic URI normalisation” is kept, against XCT-020’s underspecified canonicalization mix.
9. FHIR strengths are analogized, not imported. PROF/SHACL/SKOS are cited, not claimed as conformance targets.
10. Historical legal and ISO sentences in XCT-020 are not adopted. KNW-018 Resource Consumption stray language is not copied.
11. Case 9 records-management depth is larger than a minimum increment. S1 only classifies those failures.
12. Team outcome vocabularies were merged into one enum in §6. Catalog “installable” on reviewable-draft predecessors is not executable conformance.

**Smallest usable publication.** This memo; a later frozen packet/assessment JSON schema with the fields in §6; closed enumerations; ten synthetic packets covering the cases above; a one-page “what this engine will not do” list. Title the card **Classification Review (companion assessment contract)** so it cannot be read as a third taxonomy master. Associate with KNW-018 and XCT-020 by REFERENCE; do not EXTEND either. A separate frozen no-tools implementation audit should re-hash predecessor bytes, open the four-file packages, and test the fixtures. That audit is not this document.

## 14. Research limitations

Full predecessor YAML bodies and question trees were summarizer-mediated, not clause-complete human reads. Brief SHA pins and published synthesis hashes were not recomputed. ISO 25964 / 11179 and EU BTI/GDPR obligations were not independently verified and are not adopted. PROF does not contain a single sentence “this is not a validator”; that reading is inference from Note status and the validation-resource role. The OWL 2 punning page was accessed; Direct Semantics separation is taken from the Rec text retrieved. XKOS is a DDI Alliance vocabulary, not a W3C Recommendation. OpenRefine score ranges are service-specific and not standardized. No validator was executed. No private data, personnel example, weight, secret, or production identifier was used. This is S1 design research only.