The entire brief through END STUDY BRIEF is visible.

This study is an independent design contour for a public Vercy Enterprise metamodel of sources, bindings and synchronization. It is not a code audit, not publication approval, and not evidence that any engine runs. No private connectors, local organizational files or secrets were used. No code was executed. Synthetic examples only.

---

# EM-XCT-08 — Sources, bindings and synchronization
Independent design study (team synthesis: Grok, Harper, Benjamin, Lucas)

Research assurance: reviewable draft. Public catalogue card status observed 2026-09-22: *Being researched / Queued for research*. Published card text: “Description of a master system, physical binding, extraction, snapshot, watermark and conflict. Local addresses and credentials are not published in the shared library.” Related models named on the card: WM-XCT-001, WM-XCT-012. That card is not a specification.

## 0. Verification limits

Three graphs are kept separate throughout: (1) business instances, (2) specification dependencies, (3) package delivery. Cross-references do not require executable imports.

**What was actually opened (2026-09-22):**

| Source | URL opened | Version / date observed | Digest status | Status of reading |
|---|---|---|---|---|
| WM-XCT-001 spec | https://ver.cy/models/wm-xct-001-ownership-stewardship/spec.yaml | 0.3.1-enterprise.1; synthesisSha256 `b7e519210f7cc00c…`; adjudication reviewable-draft; publishableCanonical false | Retrieved document SHA256 `fa942556a3f460729db2e94b24d1efd4d33ee2e5fb0b1deed3ce040756acf474` matches the brief-stated spec SHA. This is a hash of the retrieved document, not a second independent range GET. | Structure, purpose, scope in/out, composition, companion association, transfer/exclusivity language. Not a line-by-line legal-source re-audit. |
| WM-XCT-012 spec | https://ver.cy/models/wm-xct-012-provenance/spec.yaml | 0.3.0-research.1; synthesisSha256 `06b28867c21efe16…`; reviewable-draft | Retrieved document SHA256 `aa6155354c55a87ab837ec9bd47f796ca582309fe383f1afffb802dafff7ecb5` matches the brief-stated spec SHA and the SHA pinned by EFA/EAP semantic references. | Structure, distinctions, gaps, composition. Not the entire 28-source hold list re-verified. |
| EFA 0.1.0 | https://ver.cy/models/wm-xct-001-ownership-stewardship/profiles/enterprise-fact-authority/0.1.0/spec.json and catalogue https://ver.cy/models/enterprise-fact-authority/ | 0.1.0 companion-contract; `vr.profile.enterprise-fact-authority`; reviewable-draft | Retrieved JSON SHA256 `cf027b56d01f23e39c15ad49a728967e45e7fb8d2b34137b6bb532536f35f582` matches the brief. | Contract text, types, I01–I16, Q01–Q18, host duties, `runtimeImports: []`. |
| EAP 0.1.0 | https://ver.cy/models/enterprise-assertion-provenance/versions/0.1.0/spec.json and catalogue | 0.1.0; `vr.profile.enterprise-assertion-provenance`; reviewable-draft | Retrieved JSON SHA256 `a8f41fb65aa5892c884731c9c4d06402637bf26bc55ab53a6ad9c7fbc34a44f0` matches the brief. | Types, Capture rule, withdrawal, empty runtime imports, host admit bounds. |
| Enterprise Identity 0.1.0 | https://ver.cy/models/wm-xct-036-alias-same-as-mapping/profiles/enterprise-identity/0.1.0/model-spec.md | 0.1.0 usage profile of WM-XCT-036 | Retrieved markdown SHA256 `2cf9808893dfbf33e36d960e04fbc1ff0b1308b27d27f49187b1851fad875163` (not a brief-stated SHA). | Boundary, types, invariants 1–14, question routes. Schema/code review of the profile was not completed here. |
| WM-XCT-036 parent | — | current parent stated as 0.3.2-enterprise.1; profile semantic basis 0.3.0 | **Not read** (~1.45 MB). No whole-parent equivalence inferred. | — |
| EM-XCT-08 card | https://ver.cy/enterprise/models/em-xct-08/ and https://ver.cy/enterprise/ | Page dated 2026-09-21; status queued / being researched | n/a | Card only. No body spec. |
| W3C PROV-DM §5.1.8 | https://www.w3.org/TR/prov-dm/#term-Invalidation | Recommendation 30 April 2013 | n/a | Invalidation section opened. |
| Airbyte protocol | https://github.com/airbytehq/airbyte/blob/master/docs/platform/understanding-airbyte/airbyte-protocol.md | Moving `master`; protocol notes through v0.19.0 (2025-10-10) observed in extract | n/a | State & Checkpointing and related sections. Not an immutable standard. |
| MS Graph delta | https://learn.microsoft.com/en-us/graph/delta-query-overview | Page last updated 2025-04-30 in extract | n/a | Overview page. Resource pages not all opened. |
| Debezium PostgreSQL | https://debezium.io/documentation/reference/stable/connectors/postgresql.html | Moving “stable”; 3.6.3.Final observed in extract / 3.6 series dated 2026-09-18 in secondary release page | n/a | Snapshot, restart, PK updates, replica identity, tombstones. |
| Singer spec | https://github.com/singer-io/getting-started/blob/master/docs/SPEC.md | 0.3.0 | n/a | Message types and STATE semantics. |

**Explicitly not done:** production connector implementation; credential handling; legal-standard wholesale re-verification; running any reference validator; claiming Codex’s “HTTP bytes matched local copies and runtime digests” beyond hashing the documents retrieved in this pass; reading WM-XCT-036 parent; claiming ISO conformance.

Descriptive operational promises in reviewable drafts are not evidence of running engines. Empty `runtimeImports: []` does not prove automatic cross-package integration.

---

## 1. Recommendation in one paragraph

Publish EM-XCT-08 as a **bounded companion contract**, proposed identity `vr.profile.enterprise-source-sync` (name is a proposal, not a registry assignment), not as five independent object models and not as a business-subject model.

Export two canonicals: **RecordSubjectBinding** and **SyncCheckpoint**. Support types carry the rest of the candidate vocabulary: SourceSystemRef, ConnectorInstallation, ExtractionAttempt, LogicalBatch, RecordOccurrence, SnapshotDeclaration, AbsenceClassification, DestinationAck, QuarantineManifest, ConflictRecord.

Reuse Identity’s frozen SourceBinding *as a carrier facet*, EFA WriteGrant/MastershipRule *by semantic reference*, EAP Capture/Activity *by alignment*, and 001 control standing *only for who may authorize binding change*. Do not reuse 012 lineage-continuation tokens as checkpoints. Do not import EFA’s one-receipt-per-second serial admission as an ingestion SLA. A first increment is an executable local reference with explicit host duties. It can prove dest-ack-before-cursor-advance, attempt≠batch≠occurrence, kind-checked mapping, four absence classes, and crash/retry receipts. It cannot prove connector authenticity, distributed exactly-once, multi-host fencing, legal mastership, or cross-register transactions.

---

## 2. Candidate vocabulary — reuse / profile / adapter / new / defer

The brief candidates are roles, not a mandate to mint five peer subject models. A connector binding is not a Company, Person or Project. A tracker board is not automatically a new business Project.

| Candidate | Decision | Why | What it is not |
|---|---|---|---|
| **SourceSystem** | **New local support type** `SourceSystemRef`, profiling Identity’s qualified assignment (scheme + issuer + scope + raw value) and EFA’s external `source` URI | Enterprises need a named source *instance* (product + tenant/instance). That identity already has a comparison rule in Identity 0.1.0. Do not invent a second Company. | Not a Company. Not a connector install. Not a credential. Not a Project. |
| **SourceBinding** | **Adapter + profile**, exported as `RecordSubjectBinding` | Identity already uses `SourceBinding` as a *frozen assertion carrier* whose source authority remains external; full source-observation revision is deferred there. EM-XCT-08 needs a *record→subject map* with kind check, purpose, mappingRevision and generation. Collapsing the two names would silently merge identifier carriage with governed mapping. Keep Identity SourceBinding as an embedded carrier; export the map under a distinct canonical name. Brief name “SourceBinding” survives as the facet role. | Not a Company/Person/Project. Not a tracker board. Not an automatic same-as. Not a merge engine. |
| **ExtractionRun** | **New, split** into ExtractionAttempt + LogicalBatch + RecordOccurrence; “ExtractionRun” may remain a grouping alias | EAP already distinguishes Capture vs Activity. Airbyte/Singer conflate attempt and batch in operations. The failure mode in D/E/J is exactly this collapse. | Not an EAP Capture. Not a business event. Not a checkpoint. |
| **SyncCursor** | **New** exported as `SyncCheckpoint` (opaque token is an inner field) | 012 traversal continuation and lineage completeness are a graph *view*, not a dest-confirmed durable checkpoint. EFA “current-root / previous snapshot” is register admission, not connector resume. Graph/Airbyte tokens are opaque and scoped. | Not a 012 continuation token. Not source-emitted state alone. Not sortable text. |
| **SyncConflict** | **New typed envelope**, profiled against EFA contested retention and Identity contested assertions | Three lifecycles, three owners. One object that “resolves sync” would smuggle fact selection into the connector layer. | Not a winner-picker. Not EFA MastershipRule. Not a mapping engine. |

Deferred by this contour: production connectors; credential objects; global same-as; automatic subject merge; distributed exactly-once; legal compliance guarantee; streaming/sub-second provenance (already a 012 gap); cross-register transactions; full source-observation revision (already deferred by Identity); partitions/global-state algebra beyond an explicit scope fingerprint.

---

## 3. Critical comparison of published predecessors

Reuse meanings at exact stated scope. Do not inherit descriptive promises as implemented behavior. A first release may reference companions semantically without importing their full histories.

### 3.1 WM-XCT-001 Ownership / Stewardship 0.3.1-enterprise.1

**Stated (opened):** reusable control facet attachable to any meta-object. Control standing, stewardship, delegated authority and register competence are distinct. Transfer/exclusivity functions require external ordering and authoritative operation. No source/destination checkpoint engine. Scope-out includes party identity, runtime authorization, data lineage, physical custody mechanics, and legal validity of a claimed right.

**Companion note (opened, not inferred from stale embed):** the live catalogue page for 001 currently shows Enterprise Fact Authority 0.1.0 as an associated English companion and states the association is not subtype conformance and does not close parent holds. The brief’s warning that embedded metadata about the companion being absent is stale is consistent with what the live catalogue now shows.

**Implication for EM-XCT-08:** 001 answers *who may authorize a binding change or an intake grant*. It does not answer *whether a page committed*. Do not subtype ControlRecord as RecordSubjectBinding. Do not treat transfer-of-control as sync.

### 3.2 WM-XCT-012 Provenance 0.3.0-research.1

**Stated (opened):** subject identity, byte binding, generation, activity, custody, assertion and verification verdict are distinct. Digest is a binding, not an identity. Traversal returns a bounded graph view with truncation and unknown-provenance markers. Streaming/sub-second provenance, production federation and sector-specific conformance are explicit gaps. Sources contain inherited verification holds. Reviewable-draft; publishableCanonical false.

**Implication:** ALIGN RecordOccurrence/Capture language and PROV invalidation (entity, not all referents). FORBID reuse of traverse-lineage tokens as SyncCheckpoint. Lineage completeness is not dest-ack.

### 3.3 Enterprise Fact Authority 0.1.0 (EM-XCT-02 companion)

**Stated (opened contract text):** FactAuthority, StewardshipAssignment, MastershipRule, WriteGrant, FactObservation. Accountable appointment ≠ stewardship ≠ source priority ≠ current WriteGrant. A source may have a grant and no rank, or a rank and no live grant. Equal-priority disagreement is contested; both observations retained; newest ingestion is not a vote (I01, I02). Serial host-internal admission, one receipt per second via strictly increasing `recordedAt`. Identical `(id,revision)` replay is a no-op after current authorization; changed payload rejects (I14). Not an import buffer, not a cross-register transaction engine, not a connector. `runtimeImports: []`. Semantic pins cite WM-XCT-001/002/012 at **0.3.0-research.1**, not automatically live 001 0.3.1-enterprise.1. Native V3 envelope validation is insufficient; companion validator is mandatory.

**Implication:** REFERENCE WriteGrant as destination intake permission and MastershipRule as fact-selection policy *outside* this contract. Do not import 1 rps as the extraction rate limit. An adapter from ExtractionAttempt/LogicalBatch onto `admit()` must be tested separately before any integration claim. Competing source facts stay in EFA; sync only preserves the observations.

### 3.4 Enterprise Assertion Provenance 0.1.0 (EM-XCT-03 companion)

**Stated (opened):** Capture, Activity, ProvenanceRecord (exact external-claim account), EvidenceLink, ConfidenceAssessment. New acquisition, version or content ⇒ new Capture. Availability unavailable→captured ⇒ new Capture. Withdrawal does not negate the external claim. Integrity/origin are declarations, not fetch or signature proof. Same bounded serial admission. `runtimeImports: []`. Empty imports do not prove automatic integration with 012.

**Implication:** ALIGN ExtractionAttempt to Activity and RecordOccurrence to Capture. A retry with identical batch + digest is not a new Capture. This contract records acquisition declarations; it does not fetch.

### 3.5 Enterprise Identity 0.1.0 (EM-XCT-01 usage profile)

**Stated (opened model-spec.md):** narrower profile of WM-XCT-036, not a new subject model and not an independent runtime ID. Parent currently 0.3.2-enterprise.1; profile semantic basis archived 0.3.0. Whole parent not read. QualifiedIdentifierAssignment ≠ IdentityAssertion ≠ AssertionRevisionEvent. “A source binding is a frozen carrier value in an assertion, whose source authority remains external.” Full source-observation revision deferred. `inferencePermitted=false` even for `equivalent-in-context`; `probable-entity-match` never becomes asserted. No merge/matching engine. Exact qualified-key compare; no normalization (`"01"` ≠ `"1"`). Declared referent kind must equal target kind against a trusted scheme-kind register (invariant 3) — this checks declared semantics, not the live source system. V3-valid outer fact can contain a semantically invalid snapshot; companion validation mandatory (invariant 14). Replay of identical assertion is a no-op; divergent content or truncated history is refused (invariant 12).

**Implication:** PROFILE the identifier carrier and kind check. Do not fork an identity model. Do not treat this profile as authorization to merge subjects when two boards share a display name.

### 3.6 What the predecessors jointly refuse to be

None of them is a durable import buffer, a connector engine, a dest-confirmed checkpoint, a merge engine, or a fact-winner algorithm. EM-XCT-08 should fill the checkpoint / binding-map / attempt-accounting gap and stop there.

---

## 4. Three (plus one) external approaches

Recorded as observed / source-asserted / inference / proposal / unverified, with implications.

### 4.1 Ontology / standard — W3C PROV-DM Invalidation

- URL: https://www.w3.org/TR/prov-dm/#term-Invalidation
- Version/date: W3C Recommendation, 30 April 2013
- Section: 5.1.8 Invalidation
- **Observed:** Invalidation is the start of destruction, cessation or expiry of an *existing entity* by an activity. After invalidation the entity is no longer available for use. Generation and usage precede invalidation. Instantaneous.
- **Source-asserted examples:** a painting destroyed; a web page taken off a site; an offer that expires.
- **Inference (ours, labelled):** invalidation is qualified to the PROV entity (fixed aspects), not to every real-world referent of that entity. This matches the brief’s reading and 012’s subject-vs-byte-binding split.
- **Proposal:** source-delete / capture-invalidation withdraws the *source entity / assertion scope*. It is not Project/Person death.
- **Unverified here:** PROV-CONSTRAINTS uniqueness proofs; PROV-O encoding.

### 4.2 Actual source/connector practice — Airbyte + Graph + Debezium

**Airbyte protocol, State & Checkpointing** (moving `master`, not a standard)

- **Observed:** state is a black box except to the source. Stream state vs global state vs legacy. Sources emit state; destinations must re-emit only after writing prior records; the platform persists only source-emitted *and* destination-confirmed state. Sequential duplicate states with interleaved records are forbidden. Sources should emit state even on empty/full refresh.
- **Implication (proposal):** SyncCheckpoint states are `emitted → staged → acked → committed`. Emission without effects is not a checkpoint (case E).
- **Unverified:** whether every Airbyte connector actually obeys dest-confirm in production.

**Microsoft Graph delta query** (learn page updated 2025-04-30 in extract)

- **Observed:** `$skiptoken` / `$deltatoken` are opaque and encode query parameters. Replays occur; clients must be idempotent. 410 Gone / `syncStateNotFound` ⇒ full reinitialization. Token lifetime is resource-specific (directory/education 7 days; Outlook depends on cache size — **no universal TTL is asserted here**). `@removed.reason` is `"changed"` vs `"deleted"` and is resource-specific. Restored items appear as newly created. Deleted-before-initial-sync items are not returned.
- **Implication:** cursor is scoped to the query/filter/select. Changed filter or principal ⇒ new SnapshotDeclaration, incomparable to the previous complete snapshot (case F, H). Absence ≠ `@removed`.

**Debezium PostgreSQL connector** (moving stable docs; 3.6.3.Final observed in extract)

- **Observed:** snapshot modes `initial | always | initial_only | no_data | when_needed | configuration_based | custom`. Resume from last LSN if the replication slot persists. PK change emits DELETE(old key)+CREATE(new key) and an optional transport tombstone. Replica identity DEFAULT/FULL/INDEX/NOTHING limits before-image. Tombstone is a log-compaction transport message.
- **Implication:** transport tombstone ≠ business-subject death. Key recycle or PK change ⇒ new source generation, not a silent binding rewrite. Snapshot completeness must name the consistency boundary (LSN/slot/isolation). Missing partition ≠ deletion sweep.
- **Unverified:** plugin-specific DDL emission; every replica-identity interaction with TOAST.

### 4.3 Another integration approach — Singer 0.3.0, with Kafka Connect as a warning

**Singer spec 0.3.0** (opened SPEC.md)

- **Observed:** Tap emits SCHEMA, RECORD, STATE. STATE.value semantics are tap-defined, not specified. Destination acknowledgement is *not in the spec*. `key_properties` required (may be empty). `bookmark_properties` optional. Exactly-once and schema-change behavior are not specified. Orchestrator/caller persists the state file.
- **Contrast with Airbyte (inference):** Singer-shaped “source emitted = safe to resume” is a known footgun. Meltano/tap practice often checkpoints a window only after it is drained, which is operational wisdom, not Singer-normative.
- **Proposal:** do not adopt Singer STATE as the EM-XCT-08 commit protocol. Prefer the Airbyte *shape* (dest-ack before persist) without importing Airbyte messages.

**Kafka Connect source offsets** (secondary; not a full KIP audit — **partially verified**)

- Default source connectors are at-least-once: crash after produce and before offset commit yields duplicates. Exactly-once for sources is connector- and framework-dependent and is not available on all worker modes.
- **Proposal:** this scope does not authorize a distributed exactly-once claim. Local dest-ack + expected-head fencing is the first increment.

### 4.4 Approach verdict

| Concern | PROV | Airbyte | Graph | Debezium | Singer | Take for EM-XCT-08 |
|---|---|---|---|---|---|---|
| Entity vs referent | Strong | Absent | Absent | Weak (row vs topic key) | Absent | Adopt PROV split |
| Dest-confirmed checkpoint | Absent | Strong | Client-side | Offsets + slot | Weak | Adopt Airbyte shape |
| Opaque scoped token | n/a | Opaque state | Strong | LSN opaque-ish | Tap-defined | Opaque + scope fingerprint |
| Delete vs absence | Invalidation of entity | Connector-specific | `@removed` vs missing | WAL DELETE + tombstone | Unspecified | Four absence classes |
| Identity / key recycle | Specialization | Stream key | Resource id | DELETE+CREATE on PK | key_properties | Explicit generation |
| Exactly-once | n/a | Not claimed as EOS | Not claimed | At-least-once typical | Not claimed | Unauthorized here |

---

## 5. Compact model: fields, cardinalities, lifecycle

### 5.1 Identity stack (never collapsed)

1. Source tenant / instance — `SourceSystemRef` (product + tenant/instance + issuer + scope + scheme)
2. Connector installation — `ConnectorInstallation` (deployment of an adapter; replaceable)
3. Credential identity — **external, never modelled, never exemplified with real values**
4. Source record key — scheme-qualified raw value; no lexical normalize
5. Source generation — increments on key recycle, restore-without-continuity, identity-field remap
6. Capture / occurrence — EAP-aligned; new bytes or version ⇒ new RecordOccurrence
7. Governed business subject — Project / Person / … owned outside this contract

Connector installation ≠ tenant ≠ subject. Binding points at (1)+(4)+(5) → (7) under purpose and mappingRevision.

### 5.2 Exported canonicals and support types

**RecordSubjectBinding** (exported canonical)

- `bindingId` (local governed id)
- embedded Identity `SourceBinding` carrier (scheme, schemeVersion, issuer, scope, rawValue)
- `sourceSystemRef`, `sourceGeneration`
- `subjectKind`, `targetSubjectRef` (external)
- `mappingRevision`, `issuer`, `purpose`
- `state` proposed | asserted | disputed | retracted
- `previousBindingRevision`, `recordedAt`, `evidenceRefs`, `policyDigest`

Cardinality: 0..1 *active* binding per `(sourceSystemRef, rawKey, generation, purpose, mappingRevision)`. Many bindings → one subject. One subject → many bindings. One source record does not become a subject.

Lifecycle: proposed → asserted | disputed | retracted (terminal). Correction = new revision; anchors (sourceSystemRef, rawKey, generation, purpose, subjectKind) do not mutate in place. Silent retarget forbidden.

**SyncCheckpoint** (exported canonical)

- identity `(scopeId, epoch, destAckSeq)`
- `opaqueToken` stored as protected locator/digest, never logged in clear
- `emissionSeq`, `destAckSeq`
- `status` emitted | staged | acked | committed | rejected
- `scopeFingerprint` (see SnapshotDeclaration)
- `expectedHead` for fencing

Lifecycle: emitted → staged → acked → committed, or rejected. Rejected-resume ⇒ `reinitRequired`. No dest-ack ⇒ cursor does not advance.

**Support types**

| Type | Identity | Essential fields |
|---|---|---|
| SourceSystemRef | product + tenant/instance + issuer + scope | scheme, authorityURI, resourceClass; no secrets |
| ConnectorInstallation | installationId | sourceSystemRef, adapterVersion, replacedBy; no credentials |
| ExtractionAttempt | attemptId | actor, installationRef, startedAt/endedAt, outcome, logicalBatchRef |
| LogicalBatch | sourceSystemRef + scopeFingerprint + generation + batchId | idempotencyKey, declaredCount, completenessFlag, contentDigest |
| RecordOccurrence | batchId + sourceKey + generation + contentDigest | payloadLocator/digest, absenceClass?, observedAt, sourceEventTime? |
| SnapshotDeclaration | fingerprint of scope tuple | tenant, resource, filter, principal, partitions, schemaRev, mappingRev, consistencyBoundary, completenessStatus |
| AbsenceClassification | per occurrence or per expected key | `not-in-page` \| `inaccessible` \| `removed-from-scope` \| `explicitly-source-deleted` |
| DestinationAck | ackId | checkpointRef, accountedIds, quarantineIds, committedAt, writer, previousAckDigest |
| QuarantineManifest | manifestId per batch | rejectedIds, reasonCodes, retryObligation |
| ConflictRecord | conflictId | class mapping \| source-fact \| checkpoint-content; owner; retainedRefs |

Cardinalities:

- SourceSystemRef 1 — n ConnectorInstallation
- SourceSystemRef 1 — n RecordOccurrence
- RecordSubjectBinding n — 1 governed subject
- LogicalBatch 1 — n RecordOccurrence
- LogicalBatch 1 — n ExtractionAttempt (retries of one batch)
- SnapshotDeclaration 1 — n LogicalBatch
- SyncCheckpoint 1 — 0..1 current DestinationAck
- LogicalBatch 0..1 QuarantineManifest
- ConflictRecord n — n retained observations

### 5.3 Four epistemic layers (do not collapse)

| Layer | Meaning | Owner |
|---|---|---|
| Proposal | binding or mapping offered, not in force | binding issuer |
| Source observation | what the source presented in a Capture/occurrence | EAP-aligned record |
| Accepted business fact | governed value under EFA authority | FactAuthority / WriteGrant |
| Downstream effect | side effect outside the register | host; out of model |

A source can be locally authentic (good digest, good cursor, acknowledged page) without being the semantic master of a field.

### 5.4 Time tuple (case N)

Keep distinct, never substitute one for another:

- `validTime` — business validity claimed
- `sourceEventTime` — only if the source supplied it
- `observedAt` — when the connector saw it
- `recordedAt` — trusted host receipt
- `committedAt` — dest-ack time

Sequence is `(epoch, destAckSeq)` plus optional source sequence if the source provides one. Source wall clocks are not a total order.

---

## 6. Design questions

**Q1. Tenant/instance vs install vs credential vs key vs generation vs capture vs subject**
Seven distinct identities listed in §5.1. Credential never enters the model. Capture is EAP-aligned occurrence, not identity continuity.

**Q2. What preserves identity; what forces a new revision or generation**
Preserve binding identity across: display rename; tracker-board move that does not change `(sourceSystemRef, rawKey, generation, kind)`; connection replacement that keeps the same source instance and key scheme (new ConnectorInstallation, same binding lineage).
New *binding revision* when: subjectKind would change; target subject is reassigned; issuer/purpose/scheme change; governed correction of a wrong map.
New *source generation* when: key recycled onto a different referent; snapshot epoch after reset/restore that cannot prove continuity; identity-field mapping becomes incompatible.
Connection replacement without source-instance continuity → new binding; old binding retained, not rewritten.

**Q3. Mapping cardinalities, kind checks, issuer/purpose, correction**
See §5.2. Kind check against the trusted scheme-kind register (Identity invariant 3). Ambiguity → proposed/disputed, never auto-pick. Correction = new revision. Silent reassignment forbidden; history retained.

**Q4. Schema / configuration / mapping change vs cursor**
- Batch-size or timeout config: no new epoch.
- MappingRevision bump: does not rewrite committed observations; new occurrences use the new revision.
- Identity-field mapping change, snapshot-scope change, or source generation change: invalidate cursor, new epoch, reinit declaration.
- Incompatible schema: new epoch + explicit reprocess; committed data stays under old mappingRevision.
Never remap committed data in place.

**Q5. Attempt vs batch vs occurrence**
ExtractionAttempt = one process try. LogicalBatch = idempotency key. RecordOccurrence = `(batch, key, generation, digest)`. Retry of the same batch after response loss is not a new acquisition if digest matches. New digest under the same key is a new occurrence and a checkpoint-content conflict if an occurrence already committed.

**Q6. Complete snapshot scope**
A snapshot is complete only if all of these are named and unchanged: tenant/instance, resource/stream, query/filter, principal/visibility, partitions present, schemaRevision, mappingRevision, consistency boundary (LSN / as-of / snapshot-isolation as declared). Omit any ⇒ partial. Changed filter or principal ⇒ incomparable, not a later complete of the prior scope.

**Q7. Pagination, revoked visibility, inaccessible objects**
Four absence classes stay distinct. Absence may produce a *ReconciliationCandidate* only after a snapshot declared complete in an *unchanged* scope. Partial pages never delete. `explicitly-source-deleted` withdraws source availability only.

**Q8. Cursor protocol**
emitted → staged → dest-durable-ack → committed. Crash before dest commit: cursor frozen. Crash after commit before response: retry returns the committed receipt. State emission without accounted effects or an explicit empty-batch ack is not a checkpoint. Opaque token stored verbatim; order is `(epoch, destAckSeq)`.

**Q9. Out-of-order, old cursor, stale head, fencing, reset, lost continuity**
Reject unsafe resume. Compare-and-set on `(partitionScope, epoch, expectedHead)`. Concurrent writers cannot both commit one progress edge. Partition vs global scope is explicit. Source reset / restore / lost slot / 410 Gone ⇒ new epoch and `reinitRequired`. Do not sort opaque strings. Do not guess the next token.

**Q10. Idempotency vs changed payload vs collisions**
Idempotency key = `(destination-dimension, partition, bindingRevision, logicalBatchId)` plus occurrence digest. Same key + same digest = replay, return prior receipt. Same key + changed digest = checkpoint-content conflict; prior evidence kept. Collisions across tenants, partitions or mapping revisions are different keys.

**Q11. Partial record rejection**
Default: quarantine with durable QuarantineManifest; do not advance the checkpoint past unaccounted records. Explicit accept-loss is a governed action with its own receipt. Committed progress guarantees durable acknowledgement of *accounted* records in the declared scope. It does not guarantee completeness, semantic truth, downstream effect, or that quarantined records have been repaired.

**Q12. Three conflict classes**

| Class | Owner | Lifecycle | Sync may |
|---|---|---|---|
| Mapping (wrong kind, silent retarget) | binding steward / Identity policy | proposed/disputed/retracted | reject, retain history |
| Competing source facts | EFA FactAuthority + resolve-conflict steward | contested observations retained | preserve both; never pick |
| Checkpoint / content (same key, new digest; stale head) | sync operator | open → retained → closed-by-operator | block overwrite |

Newest `recordedAt` is not a vote.

**Q13. Historical correction and clocks**
See §5.4. Correction preserves what was previously known at `(validAt, knownAt)`. It does not fabricate `sourceEventTime`. EFA I09 analogue: past knowledge cuts survive later corrections.

**Q14. Authorization**
Destination WriteGrant (EFA) authorizes intake, binding change and replay. Source permission is not destination permission. Revoked writer: replay of an already-committed payload returns the existing receipt or a generic denial; no new effect; no protected receipt or register dump (EFA host rule: writer-without-read gets only a receipt or generic rejection). Rejected attempts are traced as ExtractionAttempt outcomes plus optional quarantine; they are not silent.

**Q15. Sensitive payload, endpoints, tokens**
Store locator + digest of raw payload, not the payload, in the shared model. Cursor tokens and endpoint secrets are protected locators/digests. Never place real secret values in examples or logs. Metadata that *can* leak and must be classified: endpoint URL shape, tenant id, filter text, timestamps, record counts, error codes. Disclosure of those is an EM-XCT-05 concern, referenced not implemented.

**Q16. Local profile, extension, SQLite reference**
Minimum useful profile: one Dimension, one SourceSystemRef, one installation, one snapshot scope, bindings, attempts/batches/occurrences, dest-ack, quarantine, one conflict class (checkpoint-content). Extension later: partitions and global state as first-class scope parts, retention classes, multi-writer host lock, reprocess planner.
A bounded SQLite reference can prove local invariants, crash-before-commit non-advance, idempotent replay, and visible quarantine. See §12 for what it cannot prove.

**Q17. Native V3 vs nested semantics**
Native V3 validates outer model/projection structure. Nested semantic schema and companion validator are mandatory (Identity I14, EFA FA-binding). A full register or receipt must not be smuggled into a field that generic agents treat as an authoritative business value. Pins are references + digests, not embedded ledgers.

**Q18. Routes and facets**
§7 and §8.

---

## 7. Finding → Question → Artifact → permitted Action
(at least 15; informational only — listing an action confers no permission)

1. **Connector install confused with tenant or subject.** What identity does a binding name? → SourceSystemRef + ConnectorInstallation. → Reject a binding whose source endpoint is a Company/Person/Project.
2. **Identity already has SourceBinding as frozen carrier.** What extra does sync need? → RecordSubjectBinding profile wrapping that carrier. → Reuse carrier; do not fork identity.
3. **012 continuation ≠ durable checkpoint.** May we store lineage tokens as cursors? → SyncCheckpoint. → Forbid 012 tokens as resume state.
4. **EFA 1 receipt/s is host admission, not ingest SLA.** May adapters inherit it? → spec-dependency note. → Semantic reference only; test any admit() adapter separately.
5. **Airbyte dest-confirm.** When may a cursor advance? → DestinationAck. → Invariant: no ack, no advance.
6. **Graph `@removed` vs missing page.** How many absence classes? → AbsenceClassification. → Only complete-unchanged-scope miss yields a reconciliation candidate.
7. **Debezium PK change = DELETE+CREATE.** Is that subject death? → sourceGeneration + binding revision. → New generation; no auto subject death.
8. **EAP new content = new Capture.** Is a retry a new acquisition? → ExtractionAttempt vs RecordOccurrence. → Same digest+batch = retry.
9. **EFA equal-priority contested.** Does sync pick a fact? → ConflictRecord class=source-fact. → Preserve both; defer to EFA.
10. **Lexical key normalize.** Is `"01"` the same as `"1"`? → scheme-exact compare fixture. → Refuse normalize without a scheme rule.
11. **001 has no checkpoint engine.** Who owns dest-ack? → DestinationAck + host duty list. → New type; 001 only for write standing.
12. **Identity `inferencePermitted=false`.** May sync infer same-as from equal keys? → negative fixture B. → Refuse.
13. **Graph token encodes query params.** Is a cursor valid after filter change? → SnapshotDeclaration fingerprint. → Invalidate; new epoch.
14. **Singer STATE has no dest-ack.** Adopt Singer as commit protocol? → protocol matrix. → Reject Singer-as-commit.
15. **Kafka Connect default at-least-once.** Claim EOS? → host-obligations. → Explicitly unauthorized.
16. **Replica identity NOTHING drops before-image.** Infer delete payload? → beforeImageAvailability on occurrence. → Record the limit; do not invent bytes.
17. **EFA I09 past knowledge survives correction.** May a correction fabricate sourceEventTime? → time-tuple fields. → Case N: preserve previously known.
18. **V3 outer valid ≠ nested valid.** May a fact field carry a full register? → projection rule. → Forbid smuggling register/receipt into business fields.
19. **Empty runtime imports in EFA/EAP.** Does that prove integration? → package-delivery graph. → No; adapters need their own tests.
20. **Catalogue card forbids publishing credentials.** Where do secrets live? → protected locator/digest convention. → Out of shared library; out of examples.

---

## 8. Whole-object facets
For every exported canonical and support type: identity-class, direct-properties, recognition-observation, capabilities-behaviour-actions, context-evidence.

**RecordSubjectBinding**
- Identity-class: local governed `bindingId`. Not the business subject, not the source key.
- Direct-properties: carrier, sourceSystemRef, generation, subjectKind, targetSubjectRef, mappingRevision, issuer, purpose, state.
- Recognition: exact `(sourceSystemRef, scheme, rawKey, generation, purpose)`. No name match.
- Capabilities: propose, assert, dispute, retract, revise-mapping (append-only). Never merge subjects.
- Context-evidence: mapping policy digest, kind-register pin, evidence refs. Source authority external.

**SyncCheckpoint**
- Identity-class: `(scopeId, epoch, destAckSeq)`.
- Direct-properties: opaqueToken locator/digest, emissionSeq, destAckSeq, status, scopeFingerprint, expectedHead.
- Recognition: exact scope+epoch+seq. Tokens never string-compared.
- Capabilities: stage, ack, commit, reject-resume, declare-reinit. Cannot advance without dest-ack.
- Context-evidence: DestinationAck, optional QuarantineManifest, host `recordedAt`.

**SourceSystemRef**
- Identity-class: product + tenant/instance + issuer + scope.
- Direct-properties: scheme, authorityURI, resourceClass. No credentials.
- Recognition: exact qualified id. Two tenants with key `"42"` remain distinct.
- Capabilities: identification only. Not a writer, not a subject.
- Context-evidence: optional catalogue pin. Installation id is a different object.

**ConnectorInstallation**
- Identity-class: installationId.
- Direct-properties: sourceSystemRef, adapterVersion, replacedBy.
- Recognition: deployment identity, not source identity.
- Capabilities: replace installation without implying new source instance.
- Context-evidence: adapter version pin. Credentials external.

**ExtractionAttempt**
- Identity-class: attemptId.
- Direct-properties: actor, installationRef, interval, outcome, logicalBatchRef.
- Recognition: process-try identity, not acquisition identity.
- Capabilities: start, fail, retry-same-attempt.
- Context-evidence: log locator/digest only.

**LogicalBatch**
- Identity-class: sourceSystemRef + scopeFingerprint + generation + batchId.
- Direct-properties: idempotencyKey, declaredCount, completenessFlag, contentDigest.
- Recognition: idempotency key.
- Capabilities: accept, replay-noop, conflict-on-payload-change.
- Context-evidence: receipt id, content digest.

**RecordOccurrence**
- Identity-class: batchId + sourceKey + generation + contentDigest.
- Direct-properties: payload locator/digest, absenceClass, observedAt, sourceEventTime?.
- Recognition: exact tuple. Same key, new digest = new occurrence.
- Capabilities: stage, quarantine, observe source-delete (source entity only).
- Context-evidence: EAP Capture pin. Not a business fact.

**SnapshotDeclaration**
- Identity-class: fingerprint of (tenant, resource, filter, principal, partitions, schemaRev, mappingRev, consistencyBoundary).
- Direct-properties: those components + completenessStatus complete|partial|incomparable.
- Recognition: exact fingerprint. Changed filter ⇒ new scope.
- Capabilities: declare-complete, declare-partial. Completeness does not transfer across fingerprints.
- Context-evidence: page/partition manifest.

**AbsenceClassification**
- Identity-class: attached to an occurrence or to an expected key in a declared complete snapshot.
- Direct-properties: class code, reason, scopeFingerprint.
- Recognition: class codes are disjoint.
- Capabilities: raise ReconciliationCandidate only for miss-in-complete-unchanged-scope.
- Context-evidence: page id, HTTP/error class locator, not raw tokens.

**DestinationAck**
- Identity-class: ackId.
- Direct-properties: checkpointRef, accountedIds, quarantineIds, committedAt, writer, previousAckDigest.
- Recognition: receipt.
- Capabilities: commit; return-on-retry. No ack ⇒ no cursor advance.
- Context-evidence: digest chain analogue (local).

**QuarantineManifest**
- Identity-class: manifestId per batch.
- Direct-properties: rejected occurrence ids, reason codes, retry obligation.
- Recognition: remains visible after successful sibling commits.
- Capabilities: retain, reprocess, explicit-accept-loss (governed).
- Context-evidence: durable reject evidence. Cannot hide behind cursor success.

**ConflictRecord**
- Identity-class: conflictId.
- Direct-properties: class, owner, retainedObservationRefs.
- Recognition: does not pick a winner.
- Capabilities: open, retain-both, escalate; close only by owning authority.
- Context-evidence: both sides’ pins. Newest `recordedAt` is not a vote.

---

## 9. Enforceable invariants (≥8)

I-S01 **Ack-before-advance.** A SyncCheckpoint status may become `committed` only if a DestinationAck names that checkpoint and accounts for every occurrence in the batch or points at a QuarantineManifest covering the remainder.

I-S02 **Opaque tokens are not ordered.** Comparison of resume safety uses `(epoch, destAckSeq, expectedHead, scopeFingerprint)` only. Lexicographic token order is a defect.

I-S03 **Scope fingerprint equality.** Completeness and resume are defined only against an identical SnapshotDeclaration fingerprint. A changed filter, principal, schemaRev, mappingRev or consistency boundary is a new epoch.

I-S04 **Kind check.** Asserting a RecordSubjectBinding requires `subjectKind` to equal the assignment’s declared referent kind and both to match the trusted scheme-kind register. Failure is reject + history, not coerce.

I-S05 **No in-place retarget.** `targetSubjectRef`, `subjectKind`, `sourceSystemRef`, raw key and `sourceGeneration` do not mutate under the same `bindingId`. Correction is a new revision or a new binding after retraction.

I-S06 **Idempotent replay / conflict on mutation.** Same LogicalBatch idempotency key + same content digest ⇒ no-op + prior receipt. Same key + different digest ⇒ ConflictRecord class=checkpoint-content; prior evidence retained.

I-S07 **Four absences.** `not-in-page`, `inaccessible`, `removed-from-scope`, `explicitly-source-deleted` are disjoint. Only a miss under a complete unchanged scope may emit a ReconciliationCandidate. Partial snapshots do not delete.

I-S08 **Source delete ≠ subject death.** `explicitly-source-deleted` withdraws source-assertion availability. Project/Person lifecycle remains in its own model.

I-S09 **Equal-authority facts stay dual.** Sync does not select among EFA observations. ConflictRecord class=source-fact retains both pins.

I-S10 **Revoked writer has no new effect.** Without a current destination WriteGrant, a replay produces either the already-committed receipt or a generic denial. It does not emit a new occurrence effect or disclose the register.

I-S11 **Quarantine is durable.** A committed checkpoint that coexisted with rejected records must reference the QuarantineManifest. Success of the cursor cannot erase reject evidence.

I-S12 **Exact keys.** Comparison is scheme + issuer + scope + raw value + generation. `"01"` ≠ `"1"`; tenant A `"42"` ≠ tenant B `"42"`. No implicit normalization.

I-S13 **Time tuple integrity.** Historical correction may not invent `sourceEventTime`. `recordedAt` is host receipt. Sequence is epoch/seq, not wall clock.

I-S14 **No register smuggling.** A business-subject field may reference a receipt id or digest; it may not embed an AuthorityRegister, ProvenanceRegister or SyncCheckpoint ledger.

These are reference-contract invariants. A host that bypasses `ack`/`admit` equivalents can violate them; the contract must fail closed when invoked.

---

## 10. Synthetic acceptance cases A–O

Each case is accepted as a required outcome of the contract. Accompanying negatives are fixtures the reference must refuse.

**A. Startup, two boards, one Project.** Two RecordSubjectBindings, one target Project `P-1`. Rename or move of a board updates source locator on the same binding lineage if `(sourceSystemRef, rawKey, generation, kind)` hold. No new Project. No silent rewrite of target.
Negatives: **N1** board rename creates a Project. **N2** board move silently retargets the binding.

**B. Two tenants, key `"42"`; `"01"` ≠ `"1"`.** Occurrences and checkpoints are keyed by SourceSystemRef. Lexical identity is raw.
Negatives: **N3** cross-tenant key collapse. **N4** `parseInt`-style normalize.

**C. Dataset reuses key, new generation.** Old provenance stays on the old occurrence/Capture. New Capture does not infer continuity.
Negatives: **N5** recycled key treated as same referent. **N6** new Capture ⇒ identity continuity.

**D. Replay identical batch after response loss.** No duplicate effects; same receipt. Changed payload under same key ⇒ checkpoint-content conflict; prior evidence kept.
Negatives: **N7** second effect on identical replay. **N8** overwrite of prior evidence.

**E. Crash before dest commit / after commit before response.** Cursor does not advance without ack. Retry after commit returns committed result. Emission without effects is not a checkpoint.
Negatives: **N9** cursor advanced on source-emitted state only. **N15** ack recorded with zero accounted records and no explicit empty-batch flag.

**F. Failed page or missing partition.** Snapshot partial; no absence-based deletion. Complete snapshot under a changed filter/principal is incomparable.
Negatives: **N10** incomplete-page deletion sweep. **N14** filter-changed snapshot treated as continuation.

**G. Explicit source deletion.** Withdraws source availability/assertion scope only. Project/Person remains under its own lifecycle. PROV invalidation applies to the source entity, not all referents.
Negative: **N11** source-delete extinguishes the Project.

**H. Old epoch, reset token, mapping/schema drift, source restore.** Reject unsafe resume; declare reinitialization. Do not sort opaque cursor strings.
Negatives: **N12** lexicographic token compare. **N13** resume across restore/reset without reinit.

**I. Concurrent writers and stale expected-head.** Only one progress edge commits per `(partitionScope, epoch, expectedHead)`. Partition vs global scope is explicit.
Negatives: **N16** two writers commit the same edge. **N17** partition cursor applied as global.

**J. Quarantined malformed record.** Cannot disappear behind a successful cursor. Durable reject evidence and retry/recovery obligations stay visible (I-S11).
Negative: **N18** cursor success deletes quarantine rows.

**K. Equal-authority sources disagree.** Sync preserves both observations and defers selection to EFA. Newest ingestion time is not a winner.
Negative: **N19** last-write-wins on `recordedAt`.

**L. Binding points at wrong subject kind or silent change after a move.** Reject; retain history; require governed correction (I-S04, I-S05).
Negatives: **N20** kind coerce. **N21** in-place target rewrite after move.

**M. Revoked destination writer replays old payload.** No fresh unauthorized effect; no protected receipt disclosure (I-S10).
Negatives: **N22** revoked writer creates a new occurrence. **N23** denial response includes the register.

**N. Historical correction.** Preserves what was previously known. Does not fabricate source event time (I-S13).
Negative: **N24** correction backfills a sourceEventTime the source never sent.

**O. Export/import, upgrade/downgrade, restart.** Preserve identity, coverage (scope fingerprint) and checkpoint meaning, or refuse with a precise loss report (missing epoch, dropped quarantine, collapsed tenant, unreadable token protection).
Negatives: **N25** downgrade that drops generation and still claims resume safety. **N26** import that merges two SourceSystemRefs because display names match.

Ten-plus meaningful negatives across A–O: N1–N26 above. First increment should ship at least N1–N15 as executable fixtures.

---

## 11. Specification dependency graph
(semantic only — not executable imports)

```
EM-XCT-08 / vr.profile.enterprise-source-sync   (proposal)
  REFERENCE  WM-XCT-001 Ownership/Stewardship     who may authorize binding/intake
  REFERENCE  EFA 0.1.0                            WriteGrant, MastershipRule, contested facts
  ALIGN      EAP 0.1.0                            Capture / Activity / withdrawal
  PROFILE    Enterprise Identity 0.1.0            SourceBinding carrier, kind check, exact keys
  ALIGN      WM-XCT-012                           generation, invalidation-of-entity, byte digest
  ALIGN      W3C PROV-DM §5.1.8                   entity invalidation ≠ referent death
  OUT OF SCOPE (referenced, not imported)
    WM-XCT-002 access contract                    destination permission engine
    WM-XCT-003 / EM-XCT-05 disclosure             raw payload / token disclosure
    WM-XCT-036 parent 0.3.2-enterprise.1          unread; no whole-parent claim
    production connector SDKs                     Airbyte/Graph/Debezium/Singer as evidence only
```

Package delivery is a third graph: schema + companion validator + fixtures + host-duty doc. EFA and EAP already demonstrate `runtimeImports: []`. EM-XCT-08 should do the same. Any adapter that calls EFA `admit()` or EAP Capture creation is a separately tested package.

Semantic pins, if this contour later publishes, should pin exact companion versions. Note the existing hazard: EFA 0.1.0 pins WM-XCT-001 at 0.3.0-research.1 while the live 001 catalogue is 0.3.1-enterprise.1. Do not silently float.

---

## 12. Minimum viable first increment vs later

### First increment (bounded executable reference contract)

Deliverable: closed schemas, companion validator, host-duty document, synthetic Dimension fixtures covering A–H and selected I–O, ≥10 negative fixtures.

In scope to *prove locally*:

- identity stack and binding ≠ subject
- dest-ack before cursor advance
- attempt ≠ batch ≠ occurrence
- four absence classes
- opaque epoch cursor; reject old-epoch / reset
- kind-checked mapping; no silent remap
- quarantine visible after sibling commit
- idempotent replay vs payload conflict
- export/import refuse-or-preserve for identity/coverage/checkpoint

Host duties the reference *requires but does not implement*: authenticate actors; hold current WriteGrant/config; supply trusted `now`; persist DestinationAck atomically with occurrence accounting; protect token bytes; call the companion validator; never expose the ledger to a writer-without-read.

What the SQLite (or equivalent) reference **cannot establish**:

- that a live source was actually fetched
- that credentials were handled safely
- signature proof of source bytes (EAP already refuses this)
- multi-process fencing without a host lock
- distributed exactly-once
- legal mastership or compliance
- cross-register transactions
- 012 streaming provenance
- that V3 outer validation implies nested validity
- automatic integration with EFA/EAP merely because both exist

### Later increments (explicit)

1. Partition and global-state algebra as first-class scope parts.
2. Host-provided multi-writer fence across processes.
3. Schema-drift reprocess planner (declared, not silent).
4. Disclosure projections for raw payload and cursor tokens (with EM-XCT-05).
5. Tested adapters onto EFA `admit()` and EAP Capture — after separate test evidence.
6. Retention/disposition of occurrences vs checkpoints.
7. Resource budgets and back-pressure (not modelled now).

---

## 13. Mastership, disclosure, migration, production host obligations

**Mastership.** This contract does not assign semantic mastership of a business field. EFA MastershipRule does that, and even there priority is not truth. A source may be locally authentic and still unranked. Sync that “wins” because it arrived last is a defect.

**Disclosure.** All-or-deny at the register layer (EFA I11 analogue). Writers without read rights receive a receipt or generic rejection. Tokens, endpoints and raw payloads are locators/digests in the shared model. No real secrets in examples.

**Migration.** Stage legacy matcher scores and denormalized “board = project” columns as *proposals* outside the operative register (EFA FA-migration analogue). Do not import an existing merge as accepted truth. Version change requires explicit semantic comparison; unknown versions refused. Downgrade that cannot preserve generation, quarantine or scope fingerprint must emit a loss report and refuse resume.

**Production host obligations** (first increment, still not a production connector):

1. Authenticate actor and current WriteGrant independently of this schema.
2. Supply monotonic trusted receipt time.
3. Atomically persist DestinationAck with accounted/quarantined ids.
4. Enforce expected-head compare-and-set inside the host’s concurrency boundary.
5. Invoke companion validator; do not treat V3 envelope OK as semantic OK.
6. Classify and protect token/endpoint/payload bytes.
7. Pin companion versions; do not float 001 0.3.0-research.1 against 0.3.1-enterprise.1 without a recorded decision.
8. Test any adapter to EFA/EAP as its own package.

---

## 14. Smallest coherent reference implementation
(description only; not an approval of nonexistent code)

One Dimension. One SourceSystemRef. One ConnectorInstallation. One SnapshotDeclaration. Tables equivalent to the types in §5.2. API surface (names are illustrative):

- `propose_binding` / `assert_binding` / `retract_binding`
- `start_attempt` / `stage_batch` / `quarantine`
- `ack_and_commit` (the only path that advances SyncCheckpoint)
- `resume_or_reject` (checks epoch, fingerprint, expectedHead)
- `replay_batch` (I-S06)
- `export_snapshot` / `import_snapshot` (refuse-or-preserve)

End-to-end guarantees it **cannot** establish are listed in §12. Shipping this reference does not complete publication review, does not close 001/012 holds, and does not authorize production connectors.

---

## 15. Critical counterexamples and rejected assumptions

**Counterexamples the design is built to survive**

- Two Jira boards both labelled “P-1 launch” — display equality is not a Project.
- HRIS tenant EU and tenant US both use employee key `"42"`.
- A Graph 410 after a tenant migration; operator pastes the old deltaLink.
- Debezium slot dropped during restore; LSN reused in a new epoch.
- Singer tap writes STATE after emitting records the target never fsynced.
- Replica identity NOTHING: delete event has no before-image; operator invents one.
- EFA two sources, equal priority, different lexical values; a “sync resolver” picks the newer file mtime.
- V3-valid outer fact whose nested field contains a forged AuthorityRegister.

**Assumptions rejected**

- Global same-as or automatic subject merge.
- Source authenticity ⇒ semantic mastership.
- Newest ingestion time selects the fact.
- Lexical key equality across tenants or schemes.
- Sorting opaque cursor strings.
- Transport tombstone = business-subject death.
- Singer/source-emitted state = committed checkpoint.
- Universal Graph token TTL.
- Debezium “stable” URL = frozen standard.
- EFA one-receipt-per-second as extraction SLA.
- 012 lineage completeness as a synchronization checkpoint.
- Empty runtime imports as integration proof.
- Native V3 validation as nested semantic proof.
- Distributed exactly-once.
- Legal or compliance guarantee.
- Silent remap of already-committed data.
- Credentials or local addresses in the shared library.

---

This study recommends a bounded companion contract that accounts for acquisition, mapping, replay, reconciliation and checkpointing without becoming a Company model, a merge engine, or a fact authority. Existing published predecessors already own standing, provenance vocabulary, fact selection and identifier carriage. EM-XCT-08 should fill only the gap they all refuse: dest-confirmed progress over explicitly scoped source observations, with bindings that can be wrong, corrected and historically replayed without rewriting the business graph.

It does not approve nonexistent code and does not complete publication review.