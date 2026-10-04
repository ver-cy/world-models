**Visibility:** The entire brief is visible, from "# Independent research: Vercy EM-XCT-08" through "END STUDY BRIEF", including sections 1–5 on predecessors, the four suggested public sources, design questions 1–18, acceptance cases A–O, and the requested-answer section.

# EM-XCT-08: Sources, bindings and synchronization — independent design study

## 0. What I actually verified in this pass

I fetched the public pages below with a web-fetch tool. Separately, in a sandbox, I downloaded the five Vercy URLs with curl and computed SHA-256 digests, at 2026-09-22 04:56 UTC. That download-and-hash step is the only thing I executed. I wrote and ran no reference implementation, schema validator or fixture.

| Source | What I opened | Observed status | Limits |
|---|---|---|---|
| WM-XCT-001 spec.yaml | Downloaded 305,345 bytes and hashed only | SHA-256 matches the brief (fa94…f474) | Content not read. All semantic claims about it come from the brief. |
| WM-XCT-012 spec.yaml | Downloaded 271,531 bytes and hashed only | Matches the brief (aa61…ecb5) | Content not read. The traversal-continuation claim comes from the brief. |
| Enterprise Fact Authority 0.1.0 | Hashed, parsed the top-level structure, keyword-searched the contract | Matches the brief (cf02…f582). `runtimeImports` is empty. WM-XCT-001 is a semantic-only optional reference. `nativeBinding.path = authority.register.snapshot`, `companionRequired = true`. The contract states one receipt per second and says it is not for high-throughput concurrent ingestion. It defers durable multi-record atomic transfer. The table separates MastershipRule (source × priority × term) from WriteGrant (no priority field). | Only partially read. |
| Enterprise Assertion Provenance 0.1.0 | Hashed, parsed structure, keyword-searched | Matches the brief (a8f4…44f0). `researchContour EM-XCT-03`, empty imports, `provenance.register.snapshot`. States that a new acquisition, representation or source version gets a new ID. Integrity and origin are recorded declarations, not fetch or signature verification. There is no durable transaction service. Timestamps have second precision and receipt order is strictly increasing. | Only partially read. |
| Enterprise Identity 0.1.0 model-spec.md | Read about the first 6 KB | SHA-256 2cf98088…5163 (the brief gives no digest to compare). States that a source binding is a frozen carrier value inside an assertion. One frozen QualifiedIdentifierAssignment per assertion. Full source-observation revision is deferred. Three relation codes, all with `inferencePermitted=false`. A changed endpoint, purpose, predicate or window means a new assertion ID. | Remainder, schemas and the 1.45 MB parent were not read. |
| W3C PROV-DM REC 2013-04-30, §5.1.8 | Read | Details in §3 | Recommendation dated 2013. PROV-CONSTRAINTS not read. |
| Airbyte protocol doc (master branch) | Read in full | Details in §3 | Moving branch. Changelog top entry is v0.5.2 (2023-12-26). The changelog dates are internally non-monotonic (v0.5.1 is dated before v0.5.0), so the version history itself is unreliable evidence. |
| Microsoft Graph delta overview | Read in full | Page metadata ms.date 2025-01-15; the page says last updated 2025-04-30 | Resource-specific API pages were not read. |
| Debezium PostgreSQL connector, "stable" | Read through events and delete/truncate | Stable resolved to 3.6; examples show 3.6.3.Final | The "Behavior when things go wrong" and connector-properties sections were truncated and not read. Anything I say about crash semantics there is prior knowledge. |
| Data Vault 2.0, MDM survivorship, transactional inbox/outbox | Not opened | Prior knowledge only | Used only as a comparative approach. No conformance claims. |

Labels used below: **[O]** observed in an opened source, **[SA]** source-asserted (a document's claim about its own behavior), **[B]** brief-asserted and not independently reverified, **[PK]** prior knowledge, **[I]** my inference, **[P]** my proposal.

## 1. Boundary decisions per candidate

None of the five candidates should become an independent object model under its own name. Two of them collide with, or duplicate, published meanings.

| Candidate | Decision | Rationale |
|---|---|---|
| **SourceSystem** | **Split.** The product kind becomes a controlled vocabulary value. **New:** `SourceInstance`, the source tenant/instance identity. **External reference only:** connector installation and credential. | "Salesforce" is a kind. "Tenant T-9 of vendor V, production, instance generation 2" is an identity. An installation or credential is host operational configuration and is never a Company or Person. [P] |
| **SourceBinding** | **Do not reuse the name. New:** `RecordSubjectMapping`, a revisioned lifecycle adapted from the Identity profile. **Reuse:** QualifiedIdentifierAssignment carries the source record key. | Critical finding: the Identity profile already defines a source binding as a frozen carrier inside an assertion [O]. A second revisable "SourceBinding" would give generic agents two incompatible meanings for one term. The mapping is also an aboutness claim ("this record is used as evidence about subject S for purpose P"), not identity. Modeling it as `equivalent-in-context` would wrongly equate a board with a Project. [I] |
| **ExtractionRun** | **Split.** `ExtractionAttempt` is a profile of the EAP Activity meaning. `IntakeBatch` is new and is the idempotency and commit unit. `RecordOccurrence` is a profile of the EAP Capture meaning. | This separates retry from new acquisition (Q5). EAP's rule that a new acquisition gets a new identity is reused at meaning level [O]. The EAP register is not the intake log because of its 1/s serial admission and second-precision timestamps [O]. |
| **SyncCursor** | **New, restructured.** The opaque source token is a sensitive value held by locator and digest, never ordered. Canonical progress is a `SyncCheckpoint` edge inside a `SyncEpoch`, scoped by `SyncScope`. | Progress is a destination-committed fact, not a source token [O Airbyte]. The token is evidence attached to that fact. |
| **SyncConflict** | **Split three ways.** Mapping ambiguity is routed to mapping governance (reuses the Identity lifecycle's `disputed` pattern). Competing source facts are routed to Enterprise Fact Authority, and sync only preserves the observations. **New:** `IntakeConflict`, covering idempotency collision, stale head and epoch mismatch. | These three have different owners and lifecycles (Q12). One generic "conflict" object would let a checkpoint operator resolve a business-fact dispute. |

Other new support types: `IntakeRejection` (the durable quarantine entry) and `ReconciliationCandidate` (a derived proposal, never an effect). Explicitly out of scope: global same-as, subject merge or creation, connector code, credentials, legal compliance claims, and distributed exactly-once.

## 2. Three graphs, kept separate

**Business-instance graph.** Governed subjects such as Project P-1 remain mastered outside EM-XCT-08. EM-XCT-08 instances point at them by reference (`subjectRef` = register ID + subject ID + expected kind) and never write their fields. Four layers are distinguished:

1. **Source observation:** a `RecordOccurrence`.
2. **Proposal:** a `ReconciliationCandidate` or a proposed mapping.
3. **Accepted business fact:** decided in EFA or the subject's own register.
4. **Actual downstream effect:** a receipt from the destination register.

A committed occurrence is not an accepted fact.

**Specification-dependency graph.** EM-XCT-08 holds semantic references (not imports) to EAP 0.1.0 (Capture/Activity meaning), the Identity 0.1.0 profile (QualifiedIdentifierAssignment, lifecycle pattern), EFA 0.1.0 (routing target for competing facts), and WM-XCT-012 (identity/generation distinctions, with holds inherited as holds). WM-XCT-001 is referenced only for the steward and WriteGrant vocabulary. There are no references to the 1.45 MB WM-XCT-036 parent beyond the profile's own statement.

**Package-delivery graph.** `vr.profile.em-xct-08-sync` ships its own schema, code, fixtures and README with empty `runtimeImports`, following the pattern observed in EFA and EAP. Adapters (sync→EAP Capture, sync→EFA observation, mapping↔IdentityAssertion) are separate packages, each with its own tests. No integration claim is made until those adapter tests exist.

## 3. Source matrix and comparison of approaches

### 3.1 Ontology/standard: W3C PROV-DM §5.1.8 [O]

PROV-DM defines invalidation as the beginning of the destruction, cessation or expiry of an existing entity by an activity, after which the entity is no longer available for use. Its examples include a changing attribute, such as a traffic light going from green to red, producing a different entity.

Implications [I]:
- Invalidation applies to a PROV entity, which is a thing "with some fixed aspects". Invalidating "board B as observed with name X" says nothing about Project P-1.
- PROV supports multiple co-existing accounts (bundles) and specialization/alternate relations.
- PROV has no notion of commit, checkpoint, idempotency, scope completeness or authorization.

Use it for occurrence and invalidation meaning only.

### 3.2 Connector practice

**Airbyte [O, moving doc].**
- The protocol states that a source emitting a record is not enough to skip it next time. A state should be passed back only if it was emitted by both the source and the destination. A destination echoing a state means the preceding records are committed.
- State contents are a black box interpreted only by the source; the only inference allowed outside it is that null state means "start from the beginning".
- Stream state is isolated per stream. Global state carries shared state across streams and prevents per-stream parallel replication.
- Destinations must return states in order, per stream or globally depending on type.
- For unsorted streams, sources are advised to emit state even with "bogus resumability". So the presence of state does not imply resumability.
- **Divergence:** Airbyte tells destinations to persist best-effort matching fields and ignore unknown ones, and says catalog mismatches should never block replication. EM-XCT-08 deliberately does the opposite for mapped fields: a silently dropped mapped field is an explicit, recorded loss (see J).

**Microsoft Graph delta [O].**
- State tokens are opaque and encode the initial query parameters, such as `$select`. A token therefore embeds scope, which makes it both a comparability key and a disclosure risk.
- Ordering is not guaranteed and an item may appear anywhere in the sequence. Replays are possible.
- A 410 Gone response signals a required full resync.
- Removed items carry a reason: `changed` means deleted but restorable, `deleted` means not restorable. Restored items show up as new creations.
- Token validity is documented as seven days for directory and some education objects, and cache-dependent for Outlook entities.
- The "sync from now" mode (`$deltatoken=latest`) yields a token with no resource data. Such a token carries no baseline, so no completeness claim can rest on it [I].
- **Nuance to the brief:** durations do exist, but they are resource-specific. The model stores source-declared expiry evidence, never a universal constant.

**Debezium PostgreSQL 3.6 [O].**
- The initial snapshot reads a log position, scans, commits and then records completion. If the connector stops before completion, it starts a new snapshot on restart.
- Logical decoding can publish changes during commit, so consumers may see changes that are later lost if the primary dies. An observed event is therefore not guaranteed source-committed truth.
- `pgoutput` does not capture generated columns, so "complete" is only complete for the captured projection.
- A primary-key update is emitted as a delete for the old key and a create for the new key, linked by headers. The update-event note elsewhere also mentions a tombstone, so the page is internally inconsistent about the exact event sequence [O].
- The tombstone exists to support Kafka log compaction. It is transport housekeeping, not subject death.
- Truncate events have no key, and ordering across partitions is not guaranteed.
- Before-images depend on REPLICA IDENTITY.
- Restart and at-least-once duplicate semantics after a crash are [PK]; that section was not read.

### 3.3 Other data-integration approaches [PK, not reverified]

**Data Vault style (hub/link/satellite with record source and load date).** It agrees with this design on per-source satellites and on insert-only history. The failure mode is that hubs keyed by a "business key" often end up being the source key, and load date becomes the de facto ordering. Both are rejected here: the source key is not the business key (A, B), and load time is not a selection criterion (K).

**MDM golden record with survivorship rules.** "Most recent wins" or "trusted source wins" rules are exactly what K forbids inside sync. Survivorship belongs to EFA's MastershipRule, and even there equal priority stays a retained conflict [O EFA].

**Transactional inbox pattern** (dedupe table plus effects plus offset committed in one destination transaction). This is adopted as the core of the reference contract, because it gives effectively-once effects inside one destination store without claiming distributed exactly-once.

### 3.4 Disagreements and rejected assumptions

1. **Rejected:** "SourceBinding" as the EM-XCT-08 mapping name, because of the collision with the Identity profile.
2. **Rejected:** a sync conflict owning fact selection.
3. **Rejected:** "delete event ⇒ subject withdrawn". A Debezium PK change deletes a key, and a Graph `changed` removal is restorable.
4. **Rejected:** "complete snapshot" without projection, principal, filter and consistency boundary.
5. **Rejected:** comparing or sorting opaque tokens, including lexical ordering of LSN strings as delivered.
6. **Rejected:** using the EAP/EFA registers as the ingestion buffer. Their serial 1/s admission and second-precision receipt are explicit limits [O].
7. **Nuanced, disagreeing with a strict reading of Airbyte:** destination "confirmation" must be the same transaction as the effects. A separate acknowledgement write after effects reopens the E-window.

## 4. Answers to design questions 1–17 (compact)

**Q1: Identity layers.**

| Layer | Identity rule |
|---|---|
| `SourceInstance` | (issuer/vendor namespace, source-tenant ID as issued, environment, `instanceGeneration`) |
| Connector installation | External ref (locator + digest). Many installations can serve one instance. |
| Credential | External secret locator only. Never an identity input. |
| Source record key | QualifiedIdentifierAssignment: (scheme, schemeVersion, issuer = SourceInstance, scope = resource type/container, exact lexical value) |
| Key generation | `keyGeneration` plus `generationEvidence` ∈ {source-immutable-id, creation-stamp, declared-by-steward, unobserved} |
| Capture | `RecordOccurrence`, one per acquired representation |
| Governed subject | External `subjectRef` |

**Q2: Persistence under change.**
- **Rename:** the same lineage, with a new occurrence.
- **Move** that keeps the key within the same SourceInstance: the same lineage, and containment is an observed attribute. If the move reissues the key, the old lineage becomes `removed-from-scope` and the new one is unmapped. A `ReconciliationCandidate(kind=possible-continuation)` is raised and needs a governed decision.
- **Connection replacement:** same SourceInstance and lineages. If the principal or visibility changed, a new `SyncScope`, and therefore a new epoch.
- **Source restore to an earlier state:** `instanceGeneration` increments if key-space continuity is not source-guaranteed. All epochs close with `ReinitRequired`.
- **Key recycling:** a new `keyGeneration` when evidence exists. When evidence is `unobserved`, no continuity inference is made, and occurrences after a detected discontinuity (such as a creation-stamp change) start a new lineage.
- **New mapping revision** is required for: a subject change, a purpose change, or a validity-window change.
- **New source generation** is required for: a restore, a tenant migration, or a vendor key-space reset.

**Q3: Mapping cardinality and correction.** Many records may map to one subject (case A). For one (lineage, purpose, subjectKind), at most one mapping may be `active` at a time. A second active mapping means a mapping dispute, and that lineage's propagation is blocked until governance resolves it. The subject kind is checked against the governed subject's register at admission. Every mapping records an issuer and a purpose. Correction is always "retract old + create new with `corrects` link". The subject field of a mapping revision is immutable.

**Q4: Schema, config or mapping change.** A cursor is bound to (scopeDigest, schemaFingerprint, mappingRevisionSetDigest, epoch).
- A change to scope or schema closes the epoch and requires reinitialization.
- A change to mapping only does not invalidate the source cursor. It starts a new mapping-application generation, and already-committed occurrences keep the mapping revision they were committed under. Re-derivation is an explicit, separately authorized reprocessing job that produces new derived rows and never rewrites old ones.

**Q5: Attempts, batches and occurrences.**
- `ExtractionAttempt`: every process run or retry. Many attempts can deliver one batch.
- `IntakeBatch`: a logical unit with `batchKey`, which is a source- or extractor-deterministic key such as scope + epoch + page-token digest + sequence.
- `RecordOccurrence`: one per (batch, record position).
- A retry reuses the batchKey. A new acquisition of changed content produces a new occurrence, even for the same record key.

**Q6: Completeness scope.** A snapshot is `complete` only if all of the following hold: all declared partitions and pages have terminal markers, the principal and visibility digest is recorded, the filter or query digest is recorded, the projection (column set) is recorded, the schema fingerprint is recorded, the mapping revision set is recorded, and the consistency boundary is declared as {source-transactional-snapshot, token-bounded-round, best-effort-window}. Two complete snapshots are comparable only if every component digest is equal.

**Q7: Four distinct states.**
- `absent-in-complete-comparable-snapshot`: can produce only a ReconciliationCandidate.
- `inaccessible`: permission error or partial page. No inference.
- `removed-from-scope`: the filter or containment changed.
- `source-deleted`, with a source reason and restorability, such as Graph's changed/deleted.

Only the last one withdraws availability of the source assertion, and none of them touches the subject.

**Q8: Commit protocol.** Steps: stage (non-durable or durable scratch) → validate → one destination transaction {occurrences + rejections + manifest + batch receipt + checkpoint edge (CAS on expected head)} → respond.
- Crash before commit: nothing is visible and the head is unchanged.
- Crash after commit: a retry finds the receipt.
- The source token stored in the edge is the token that was current after the last committed page.

**Q9: Order, fencing and reset.** Ordering comes from a local `commitSeq`, never from tokens or source clocks. Writers carry a `fenceToken` (monotonic per scope lease). The CAS is on `(scope, epoch, expectedHeadId)` with a unique successor. Source reset (410, a missing offset, an unavailable log position) closes the epoch as `continuity-lost`.

**Q10: Idempotency key.** The key is (sourceInstance, scope, epoch, batchKey). The payload digest is taken over canonical bytes of the batch.
- Same key and same digest: return the original receipt.
- Same key and a different digest: `IntakeConflict(kind=payload-mismatch)`. Both digests are retained and nothing is overwritten.
- Keys never collide across tenants, partitions or mapping revisions, because those are key components.

**Q11: Partial rejection.** The policy is declared per scope, from one of three options:
- `block`: any reject fails the batch.
- `quarantine`: the default. The reject is durable in the same transaction, and progress still advances.
- `accept-loss`: requires a policy reference and an explicit loss count.

Committed progress guarantees that every received record is accounted for as committed, rejected or declared loss. It does not guarantee source completeness, correctness, or downstream fact acceptance.

**Q12: Owners.**
- Mapping conflict: owned by the mapping steward (the Identity-style lifecycle).
- Competing facts: owned by the EFA governor or evaluator, with sync as a passive supplier.
- Intake or checkpoint conflict: owned by the sync operator, with its own lifecycle (open → resolved-by-replay | resolved-by-reinit | accepted-as-divergent).

**Q13: Times.**
- `sourceEventTime`: nullable, carries a provenance label (source-asserted | unknown), never backfilled.
- `sourceCommitPosition`: an opaque source position.
- `observedAt`: when the extractor received the record.
- `recordedAt` and `commitSeq`/`committedAt`: local.
- Business valid time belongs to the fact layer, not to sync.

Historical correction appends. Queries use `knownAt` against `recordedAt`.

**Q14: Authorization.** Checks happen at intake, binding change and replay against grants current at that moment. Source permission, meaning what the principal could read, is recorded as scope, not as destination write permission. Revocation stops new admission. Denied attempts go to a restricted audit, and the response is uniform so it reveals nothing about prior existence (see M).

**Q15: Sensitive values.** Raw payloads, endpoint URLs, cursor tokens (which encode query parameters [O Graph]) and credentials are held by external locator. Digests of low-entropy values, such as a key "42" or an email address, must be keyed (HMAC with a host key). Otherwise the digest is an oracle.
- Trade-off: keyed digests are not comparable across hosts, so export carries a key-epoch reference, and cross-host comparison requires re-keying by an authorized host.
- Metadata that still leaks: counts (existence), timing, scope digests (filter shape), rejection reasons, and SourceInstance tenant identifiers.

**Q16: Minimum local profile.**
- In scope: one host, multiple SourceInstances, stream-scoped checkpoints only, full snapshot plus incremental opaque token, and quarantine.
- Budgets: max batch bytes, max records per batch, max open quarantine per scope (beyond which intake blocks), and retention classes per type.
- Later: partitions and global state.

**Q17: Native V3.** Expose the register as a companion (`nativeBinding.path = sync.register.snapshot`, `companionRequired = true`), matching the observed EFA/EAP pattern. The outer projection validates structure only. Checkpoint heads, mappings and receipts must never be projected into subject fields such as `Project.externalIds` or `Project.lastSyncedAt`. Only derived, explicitly non-authoritative read views (`authority: none`) may be surfaced to generic agents.

## 5. Types, fields, cardinalities and lifecycle (compact)

Every type has an `id` that is issuer-qualified and a `schemaVersion`. All objects are closed. `null` means explicitly unknown.

| Type | Key fields | Cardinality | Lifecycle |
|---|---|---|---|
| **SourceInstance** | kindCode (vocabulary), issuerNamespace, sourceTenantId (exact lexical), environment, instanceGeneration, installationRefs[] (locator + digest), stewardRef | 1 → n SyncScope, 1 → n record lineages | declared → active ⇄ suspended → retired. Restore creates a new generation linked via `continuationOf` with continuity ∈ {guaranteed, unknown} |
| **SyncScope** | sourceInstanceRef + generation, resource, filterDigest, projectionDigest, principalDigest, partitionSet, schemaFingerprint, consistencyBoundary, scopeDigest | Value object, content-addressed | Immutable. Any change produces a new scope. |
| **SyncEpoch** | scopeRef, epochNo, openedBy (full snapshot or declared bootstrap), baselineCompleteness, closeReason ∈ {reset, continuity-lost, scope-change, schema-drift, restore, operator} | 1 scope → n epochs, at most 1 open | open → closed (terminal) |
| **SyncCheckpoint** | epochRef, predecessorId (null for genesis), batchReceiptRef, tokenLocator + tokenDigest (keyed), sourcePositionEvidence, commitSeq, fenceToken | Linear chain per epoch. UNIQUE(epoch, predecessorId). | Immutable |
| **ExtractionAttempt** | scopeRef, epochRef, attemptNo, actor or installationRef, startedAt, endedAt, outcome ∈ {committed, failed-before-commit, duplicate-of-receipt, denied, conflict} | n attempts → 0..1 batch | running → terminal |
| **IntakeBatch** | scope, epoch, batchKey, payloadDigest, recordCount, rejectPolicy, pageTerminal? (bool), manifestDigest, receiptId, committedAt | UNIQUE(scope, epoch, batchKey) | committed only. Staged state is never exported. |
| **RecordOccurrence** | batchRef, position, recordRef (QualifiedIdentifierAssignment + keyGeneration + generationEvidence), op ∈ {upsert, source-deleted(reason, restorable), removed-from-scope, snapshot-read}, contentLocator + contentDigest, times per Q13, mappingRevisionSetDigest | n per batch | Immutable. Later withdrawal is a new occurrence. |
| **RecordSubjectMapping** | recordLineageRef, subjectRef (register, id, expectedKind), purpose, issuer, validFrom/To (half-open), state, corrects?, evidenceRefs | n:1 to subject. At most 1 active per (lineage, purpose, kind). | proposed → active ⇄ disputed → retracted (terminal). A subject change is only possible via a new mapping. |
| **IntakeRejection** | batchRef, position, reasonCode, contentLocator + digest, retryObligation ∈ {none, fix-mapping, fix-schema, steward-review}, resolvedBy? | 0..n per batch | open → resolved-by-reingest or resolved-as-loss (with policy reference). Never deleted. |
| **IntakeConflict** | kind ∈ {payload-mismatch, stale-head, epoch-mismatch, fence-violation, token-reuse}, both sides' digests, scope/epoch | Independent | open → resolved(action) |
| **ReconciliationCandidate** | kind ∈ {absent-in-comparable-snapshot, possible-continuation, kind-mismatch, restore-divergence}, basis (snapshot IDs, scope digest), target mapping or lineage | Derived | open → accepted-into-governance (routes out) or dismissed. Never an effect. |

## 6. Enforceable invariants

1. **Exact qualified keys.** A record key is (sourceInstance, generation, scope-resource, scheme, schemeVersion, exact lexical value). "01" ≠ "1" unless the scheme version declares a normalization rule. Tenant is never inferred.
2. **Atomic progress.** A `SyncCheckpoint` exists only in the same transaction as its batch's occurrences, rejections, manifest and receipt. Source-emitted state alone never creates one.
3. **Single successor.** UNIQUE(epochId, predecessorId), plus a fence token that must be at least the lease high-water mark. At most one of two concurrent writers commits.
4. **Epoch binding.** A token is usable only with equal epoch, scopeDigest, schemaFingerprint and open epoch state. Tokens are never compared or sorted. Order is `commitSeq`.
5. **Idempotency.** For each (scope, epoch, batchKey), exactly one receipt. A differing payload digest yields an `IntakeConflict` and no mutation.
6. **Conservation.** For each committed batch: received = occurrences + rejections + declaredLoss, and declaredLoss > 0 requires policy `accept-loss` and a reference.
7. **Mapping immutability and kind.** A mapping's subjectRef and expectedKind never change. Admission rejects a subject whose governed kind ≠ expectedKind. At most one active mapping per (lineage, purpose, kind).
8. **No subject effects.** No EM-XCT-08 operation creates, merges, retires or edits a governed subject or its fields.
9. **Absence discipline.** An absence-derived output is only a `ReconciliationCandidate`, only when both snapshots are `complete`, and only when all component digests are equal.
10. **No fact selection.** Sync outputs carry no winner. Ingestion or observation time is not an input to any selection it forwards.
11. **Authorize before lookup.** Authorization with a current grant precedes any idempotency or receipt lookup. Denials are uniform and audited in a restricted log.
12. **No secret material.** Exported rows contain no raw token, credential, endpoint secret or payload. Low-entropy identifiers appear only as keyed digests or under a sensitivity class.
13. **Time honesty.** `sourceEventTime` is null unless source-asserted. It is never derived from observed, recorded or committed time.
14. **Round-trip or refuse.** Export→import and upgrade/downgrade either preserve ids, digests, epochs, heads, mapping states and rejection states, or refuse with an itemized `LossReport`.

## 7. Acceptance cases A–O

| Case | Disposition | Fixture(s) |
|---|---|---|
| **A** | Two board lineages each have an active mapping to P-1 (n:1 is allowed). A rename produces a new occurrence with an unchanged mapping. A move that keeps the key produces an attribute occurrence only. A move that reissues the key leaves the old lineage `removed-from-scope`, leaves the new lineage unmapped, and raises a `possible-continuation` candidate. No new Project is created and no mapping is rewritten. | A+ positive. **N1**: an attempted in-place edit of `subjectRef` after a move is rejected (INV 7). |
| **B** | Keys `(T1,"42")` and `(T2,"42")` are distinct lineages with separate scopes, epochs and checkpoints. "01" and "1" are distinct under scheme v1. | **N2**: a lookup by the bare value "42" is refused as ambiguous. **N3**: collapsing "01" into "1" without a scheme rule is rejected. |
| **C** | A generation change with creation-stamp evidence starts a new lineage, and the old occurrences and provenance stay with the old lineage. A new capture alone implies nothing: when evidence is unobserved, continuity is recorded as `unknown`. | **N4**: an attempt to attach a new capture to the old lineage on key equality alone, with changed generation evidence, is rejected. |
| **D** | Replaying the same batchKey and digest after response loss returns the original receipt, with zero new rows. The same key with a changed payload produces a payload-mismatch conflict, and both digests are retained. | **N5**: a changed-payload overwrite is attempted; the assertion is that the prior occurrence bytes and digest are unchanged. |
| **E** | A crash before commit leaves the head unchanged, and a retry recommits. A crash after commit but before the response makes the retry return the committed receipt. Source state without committed effects is not a checkpoint. | **N6**: a checkpoint row without a batch in the same transaction is rejected. **N7**: fault injection kills the process between staging and commit; the head must be unchanged. |
| **F** | A failed page or missing partition makes the snapshot `partial`, and no absence candidates are created. A complete snapshot under a changed filter or principal produces a new scope and is marked not comparable. | **N8**: absence inference from a partial snapshot is rejected. **N9**: a cross-scope comparison is refused. |
| **G** | A source deletion produces a `source-deleted` occurrence (with reason and restorability), the mapping's availability becomes source-withdrawn, and the mapping and subject are untouched. A Debezium PK-change delete and a tombstone are classified as key-change or transport, not deletion. | **N10**: a delete event that attempts subject retirement is rejected (INV 8). |
| **H** | An old-epoch token, a 410-style reset, schema drift, a mapping-only change or a restore is handled as follows. For token, reset, drift or restore, the epoch is closed and `ReinitRequired` declares scope and reason. A mapping-only change produces a new application generation (Q4). Tokens are never sorted. | **N11**: resuming with a closed-epoch token is rejected. **N12**: a fixture where the lexically larger token is the older one; the implementation must not choose by string order. |
| **I** | Two writers submit the same expected head: one commits, the other gets a stale-head conflict. Stream scopes are independent. Global or partitioned state is not supported in the MVP and is refused explicitly. | **N13**: double commit on one predecessor is rejected. **N14**: a stale fence token is rejected. |
| **J** | A malformed record becomes a durable `IntakeRejection` in the same transaction. The cursor may advance under the quarantine policy, but the manifest shows the reject and a retry obligation. Under the block policy, the batch fails. | **N15**: a batch whose manifest count excludes a reject is rejected by conservation (INV 6). |
| **K** | Both observations are retained with attribution. The forwarded package to EFA carries no winner. EFA's equal-priority rule keeps the conflict. | **N16**: a "newest ingestion wins" selection inside sync is rejected. |
| **L** | Wrong subject kind at admission is rejected. A silent subject change after a move is impossible (the field is immutable). Correction goes through retract plus a new mapping with `corrects`, and history is retained. | N1 (above), plus **N17**: a Person mapped under a Project-kind mapping is rejected. |
| **M** | A revoked writer is denied before the idempotency lookup. The response is uniform and identical whether or not a receipt exists. The denial is logged in the restricted audit. | **N18**: the revoked writer's response must be byte-identical for existing and non-existing batch keys. |
| **N** | A correction appends a new occurrence. `sourceEventTime` stays null if not source-asserted. A `knownAt` query before the correction returns the old view. | **N19**: filling `sourceEventTime` from `observedAt` is rejected. |
| **O** | An export bundle carries ids, digests, epochs, heads, states and the key-epoch reference for keyed digests. Import into a host with a different digest key, or a downgrade that lacks a type, refuses with a LossReport. Restart preserves heads. | **N20**: a downgrade dropping IntakeRejection must refuse, not drop silently. |

That is twenty negative fixtures, covering every case except K's positive path, which has N16 as its negative.

## 8. Whole-object facets for every exported type

| Type | identity-class | direct-properties | recognition-observation | capabilities-behaviour-actions | context-evidence |
|---|---|---|---|---|---|
| SourceInstance | Issuer-qualified tenant plus generation. Not an org or agent. | kindCode, tenantId, env, generation, installationRefs | Declared by a steward from source admin evidence. A restore produces a new generation. | declare, suspend, retire, continue-as-new-generation | Steward attestation, installation locators |
| SyncScope | Content-addressed value | Component digests, boundary | Computed from extractor config plus principal | none (immutable), compare | Config digest evidence |
| SyncEpoch | (scope, epochNo) | baseline, closeReason | Opened by a snapshot or bootstrap; closed on reset or drift | open, close | Reset signal (such as a 410 or missing offset) |
| SyncCheckpoint | Chain node | predecessor, receipt, tokenDigest, fence | Created only by a committing transaction | resume-from (read-only) | Batch receipt, source position evidence |
| ExtractionAttempt | Occurrent (activity) | actor, times, outcome | Host process record | none after terminal | Logs by locator |
| IntakeBatch | (scope, epoch, batchKey) | digest, counts, policy | Extractor-assigned deterministic key | commit, replay-returns-receipt | Manifest digest |
| RecordOccurrence | Capture-like representation | recordRef, op, content digest, times | Acquired from source | withdraw-by-new-occurrence | Source position, generation evidence |
| RecordSubjectMapping | Issuer + purpose claim of aboutness | subjectRef, kind, purpose, window, state | Proposed by a steward or matcher (proposal only) | activate, dispute, retract, correct | Review decision, source record evidence |
| IntakeRejection | (batch, position) | reason, content locator, obligation | Validation failure | resolve-by-reingest, resolve-as-loss | Validator version, policy reference |
| IntakeConflict | Conflict record | kind, both digests | Detected at commit | resolve (replay, reinit, divergent) | Both receipts |
| ReconciliationCandidate | Derived proposal | kind, basis snapshots | Computed only from comparable complete snapshots | route-to-governance, dismiss | Snapshot IDs and digests |

## 9. Finding → Question → Artifact → permitted Action routes

| # | Finding | Question | Artifact | Permitted action |
|---|---|---|---|---|
| 1 | Snapshot `partial` | Can absence be inferred? | Snapshot manifest | Rerun the snapshot. No candidate. |
| 2 | Absent in a comparable complete snapshot | Is the record gone for this purpose? | ReconciliationCandidate | Route to the mapping steward. Never delete. |
| 3 | Payload mismatch on the same batchKey | Which bytes are true? | IntakeConflict | Operator investigation. Both retained. |
| 4 | Stale head | Who won? | IntakeConflict + checkpoint chain | Loser re-reads the head and re-stages. No force-write. |
| 5 | Token for a closed epoch | Can we resume? | Epoch close record | Declare reinit and open a new epoch by snapshot. |
| 6 | Source 410 or offset unavailable | Is continuity lost? | Epoch close (continuity-lost) | Full resync. Old occurrences retained. |
| 7 | Schema fingerprint drift | Is the mapping still valid? | ReinitRequired + drift report | Steward updates the mapping, then reinit. |
| 8 | Mapping-only revision | Must committed data change? | Mapping revision | An optional authorized reprocess creates new derived rows only. |
| 9 | Two active mappings for one lineage and purpose | Which subject? | Mapping dispute | Steward retracts one. Propagation blocked meanwhile. |
| 10 | Kind mismatch | Wrong target? | Rejected admission + candidate | Governed correction only. |
| 11 | Key reissued on move | Same board? | possible-continuation candidate | Steward creates a new mapping or declines. |
| 12 | Generation evidence changed | Key recycled? | New lineage | No action on old provenance. |
| 13 | Quarantine growing past budget | Is intake safe? | Rejection manifest | Block intake for the scope. Steward fixes. |
| 14 | Equal-authority disagreement | Which value holds? | Retained observations package | Forward to EFA. No selection. |
| 15 | Revoked writer replay | Is there disclosure risk? | Restricted denial audit | Security review. No receipt disclosed. |
| 16 | Source-deleted, restorable | Is the subject retired? | source-deleted occurrence | Mark source availability only. Subject lifecycle is external. |
| 17 | Restore detected | Are old tokens valid? | New instance generation | Close all epochs, reinit, continuity = unknown. |
| 18 | Import into a host with a different digest key | Are digests comparable? | LossReport | Refuse, or re-key under authority. |

## 10. Mastership and disclosure

| Item | Master |
|---|---|
| Source content | Source (locally authentic, not semantic master) |
| Record keys | Source issuer (reuses the Identity profile rule that the importer cannot reinterpret) |
| Mappings | Mapping steward per purpose |
| Checkpoints, batches, rejections, intake conflicts | Sync register (host) |
| Business facts | EFA or the subject register |
| Subjects | Their own registers |

Disclosure tiers:
- **Public/model:** type definitions and fixtures (synthetic only).
- **Tenant-operational:** counts, states, digests.
- **Restricted:** locators, rejection content, and the denial audit.

Tokens are treated as secret-grade because they can encode query scope [O Graph].

## 11. Increments

**Increment 1 (minimum viable, the reference contract):**
- SourceInstance, SyncScope, SyncEpoch, SyncCheckpoint (stream scope only), ExtractionAttempt, IntakeBatch, RecordOccurrence, RecordSubjectMapping, IntakeRejection, IntakeConflict, ReconciliationCandidate.
- Quarantine policy default.
- Keyed digests.
- Export/import with LossReport.
- Fixtures A–O with N1–N20.
- No adapters.

**Increment 2:** partitions, shared (global) state with global ordering, per-stream reset inside a global epoch, and consistency-boundary evidence for CDC positions.

**Increment 3:** separately tested adapters: occurrences → EAP Captures (batched, respecting its serial admission), retained observations → EFA, mapping ↔ IdentityAssertion (predicate choice needs review, because aboutness is not equivalence).

**Increment 4 (production host):** distributed leases and fencing, KMS-keyed digests and key rotation, retention and erasure (with erasure of content preserving digest-only tombstones and a disclosure review), streaming latency, and multi-register transactions if ever justified.

**Deferred indefinitely under this scope:** same-as, merge, subject creation, connector code, exactly-once claims.

## 12. Smallest coherent reference implementation, and what it cannot prove

**Proposal [P]:** a single-file SQLite package with `BEGIN IMMEDIATE` transactions and WAL mode. Tables mirror §5, with UNIQUE(epoch, predecessor), UNIQUE(scope, epoch, batchKey) and CHECK conservation via a trigger. A monotonic `commitSeq` is used for ordering. An in-process "source simulator" emits tokens deliberately non-sortable, and fault-injection points sit between staging, commit and respond. Fixtures are pure JSON.

**It could demonstrate:** single-host atomicity of effects plus checkpoint, idempotent replay, CAS and fencing among local processes, quarantine conservation, epoch refusal, uniform denial ordering, and round-trip/refusal on export.

**It cannot establish:**
- Distributed exactly-once between a real source and destination.
- A source's actual token, expiry or restore behavior.
- Truth or authenticity of source data (it records declarations only, like EAP).
- Clock correctness.
- Fencing across hosts or network filesystems, since SQLite locking there is unreliable [PK].
- Durability if storage lies about fsync.
- Real IAM.
- Confidentiality at rest.
- Throughput.
- Legal retention or erasure compliance.
- Correctness of any adapter.

None of this code exists yet. This study approves nothing.

## 13. Migration and production host obligations

**Migration:**
- Existing ad-hoc "external ID" fields on subjects migrate into proposed (not active) mappings, requiring steward activation.
- Legacy cursors migrate into a synthetic epoch with `baselineCompleteness = unknown`. Absence inference is disabled until a fresh complete snapshot.

**Host duties:**
- Authenticate actors.
- Supply current grants and a trusted clock.
- Hold secrets and locators.
- Hold digest keys.
- Provide durable storage with honest fsync.
- Enforce byte budgets before parsing.
- Operate leases and fences.
- Enforce retention.
- Keep the restricted audit.
- Never project register rows into subject fields.
- Report version observations for moving upstream docs (Airbyte master, Debezium stable).

## 14. Critical counterexamples and open holds

1. **Delete ≠ death.** A Debezium PK change is emitted as a delete for the old key plus a create for the new one [O]. A naïve absence or delete handler would retire a live subject.
2. **Restore looks like create.** Graph reports restored items as new creations [O]. A creation-based identity model would split one board into two.
3. **Observed ≠ source-committed.** Logical decoding can expose changes that are lost on primary failure [O]. Occurrences must be revisable by later withdrawal occurrences, never assumed final.
4. **"Complete" hides projection.** `pgoutput` omits generated columns [O]. Completeness without a projection digest is false.
5. **State ≠ resumability.** Airbyte explicitly allows state with bogus resumability for unsorted streams [O].
6. **Name collision.** "SourceBinding" already means something frozen in the Identity profile [O]. Keep the names apart.
7. **Throughput trap.** Routing intake through EAP/EFA admission would cap ingestion at about one receipt per second [O].

**Open holds:**
- WM-XCT-001 and WM-XCT-012 content, and the WM-XCT-036 parent, were hash-verified but not read by me.
- The Identity profile schemas were not read.
- The Debezium failure-behavior section was not read.
- Data Vault and MDM claims are prior knowledge.
- Whether the mapping adapter to IdentityAssertion needs a new predicate code is an unresolved review question.
- The per-host key design for low-entropy digests needs a security review before any export format is frozen.

This study does not complete publication review.