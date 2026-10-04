# EM-XCT-04 — Time, states and versions
Independent research for Vercy’s public Enterprise model program  
Assignment contour: Time, states and versions · queued research card  
Proposed companion (not published, not approved): `vr.profile.enterprise-time-states-versions`  
Working title: Enterprise Time, States and Versions  
Suggested research edition: `0.1.0-research`  

This document is research. It does not authorize publication, does not complete parent holds, and does not audit future code. An implementation later receives a separate frozen no-tools audit.

Claim grades used below: **retrieved** (page fetched this run), **source-asserted** (the retrieved text says it), **Codex-pin** (SHA given in the assignment as structural inspection, not recomputed here), **inference**, **proposal**, **inaccessible**.

---

## Retrieval ledger

**Retrieved this run (summarizer-mediated; raw bytes and SHA not independently recomputed):**

| Artifact | Edition / date | URI |
|---|---|---|
| WM-XCT-009 Time / Calendar `spec.yaml` | `0.3.0-research.1`, published / reviewable-draft | https://ver.cy/models/wm-xct-009-time-calendar/spec.yaml |
| WM-XCT-021 Lifecycle / Status `spec.yaml` | `0.3.0-research.1` | https://ver.cy/models/wm-xct-021-lifecycle-status/spec.yaml |
| WM-XCT-022 Version / Change History `spec.yaml` | `0.3.0-research.2` | https://ver.cy/models/wm-xct-022-version-change-history/spec.yaml |
| EM-XCT-02 Enterprise Fact Authority | `0.1.0`, `vr.profile.enterprise-fact-authority` | https://ver.cy/models/enterprise-fact-authority/ |
| EM-XCT-03 Enterprise Assertion Provenance | `0.1.0`, `vr.profile.enterprise-assertion-provenance` | https://ver.cy/models/enterprise-assertion-provenance/ |
| EM-XCT-04 research card | queued; brief pending | https://ver.cy/enterprise/models/em-xct-04/ |
| Enterprise registry | live JSON | https://ver.cy/enterprise/registry.json |
| OWL-Time | W3C CR Draft 15 Nov 2022 | https://www.w3.org/TR/2022/CRD-owl-time-20221115/ |
| PROV-DM | W3C Rec 30 Apr 2013 | https://www.w3.org/TR/2013/REC-prov-dm-20130430/ |
| SemVer 2.0.0 | spec page | https://semver.org/spec/v2.0.0.html |
| SCXML | W3C Rec 1 Sep 2015 | https://www.w3.org/TR/2015/REC-scxml-20150901/ |
| XTDB “Time in XTDB” + SQL txs | current public XT2 docs, retrieved 2026-09-21 | https://docs.xtdb.com/about/time-in-xtdb.html |
| Microsoft system-versioned temporal tables | Learn, `sql-server-ver17` | https://learn.microsoft.com/en-us/sql/relational-databases/tables/temporal-tables |
| Datomic data model + filters | current public docs | https://docs.datomic.com/data-model.html · https://docs.datomic.com/reference/filters.html |

Assignment SHA pins (Codex inspection, **not recomputed here**):  
009 `sha256:060511804c09ed5992e3fdf222839f97a0d340db0a2cba3c4c08aded7767e90d` · 021 `sha256:87c8c50f6f4c2eb3478751f01a08c6c37c6a85f97f4c056505b13cdf561314e9` · 022 `sha256:40ced88212f4c90690bdbb35bf2429fe627d11793bee5e587b5b10b99f49fe85`.  
Lucas observed a different `synthesisSha256` on the 022 landing page (`e97a0b44…`). Those are different objects. Keep the distinction.

**Inaccessible this run:**  
https://ver.cy/models/enterprise-identity/ returned **404**. Observed elsewhere: enterprise-identity `0.1.0` is described as a bounded profile under WM-XCT-036, “identity references, not identity proofs.” Treat the prompt description as assignment text, not a retrieved page.  
Not retrieved: ISO 8601-1/2 (paywalled), SQL:2011 full text, EventStoreDB server internals, raw parent YAML bytes, live SHA recomputation, full `enterprise/AGENTS.md` body (summarizer returned insufficient content).

Do not claim ISO or SQL:2011 conformance.

---

## 1. Boundary verdict

### What the assignment actually needs

Companies must ask two different questions and keep their answers apart:

1. **What was effective at a date?** — valid / application time of a fact.  
2. **What did this Dimension know at a date?** — knowledge cutoff / record / receipt time.

They must correct late information without rewriting past knowledge; bind each object revision to an exact schema pin; and retain domain-specific state vocabulary. A startup must not be forced into an ERP. An international group may have several scopes and masters. An AI organisation must separate model-artifact versions, deployment states, and *records about* those states.

Parents already own large pieces of this and must not be re-implemented:

- **WM-XCT-009 0.3.0-research.1** is a mixin plus governed reference model for scales, zones, calendars, recurrence, holidays, working days, and embeddable value shapes (instant, interval, duration, precision, binding mode, open bounds). It is storage-neutral. It excludes clock synchronisation, calendar participation, jurisdiction geometry, legal entitlement, and domain deadline policy. It does **not** define valid / record / observation as query axes for a fact.
- **WM-XCT-021 0.3.0-research.1** already separates valid time, record time and observation time; requires append-only correction as a new record; and states that domain state meaning is owned by the host. It excludes versioning, general provenance, IAM, workflows, calendars, and formal state-machine verification. It aligns with SCXML for behavioural machines; it does not inherit an SCXML processor.
- **WM-XCT-022 0.3.0-research.2** already separates opaque revision identity from series identity and version designation; models a predecessor DAG; and **delegates general effective time**. Bitemporal support is **partial**. It excludes host domain attributes, IAM, legal retention engines, and distributed convergence.

Adjacent published companions already occupy neighbouring seams:

- EM-XCT-02 `vr.profile.enterprise-fact-authority` 0.1.0 — authority declarations, write grants, contested-no-winner, preserve competing records. Not IAM. Already mentions fact-valid time, knowledge cut, and receipt.
- EM-XCT-03 `vr.profile.enterprise-assertion-provenance` 0.1.0 — evidence and assertion records; **correction versus a new domain event**; occurrence / capture / receipt kept separate. Not automatic truth.

### Verdict

**Mint a small original companion contract. Do not mint a fourth world-model mixin and do not subtype 009 / 021 / 022.**

The missing executable unit is not another time ontology, not another statechart, and not another revision DAG. It is:

> one governed **single-valued fact scope** (Dimension + subject + predicate + context), with an **append-only commit log**, each commit carrying an **immutable full snapshot** of the current assertion timeline, addressable by a host-assigned knowledge cutoff.

That contract is independently discoverable (`vr.profile.enterprise-time-states-versions`), downloadable under `/models/enterprise-…`, and associated with the three parents by **exact semantic reference**. Runtime imports stay **empty**. Conceptual composition is not executable inheritance. This matches the published EM-XCT-02 / 03 pattern.

### Minimum useful profile

Call it **UTC-second snapshot timeline, single-valued scope**.

| Decision | Choice |
|---|---|
| Scope | Exactly one (Dimension, subject, predicate, context). Single-valued. |
| Write | Append-only `TimelineCommit`. Host assigns `receiptSequence` (strictly increasing per scope) and `receiptInstant`. |
| Snapshot | Each commit stores a complete `KnowledgeSnapshot` of the current assertion timeline. Prior snapshots remain queryable. |
| Valid interval | Half-open `[validFrom, validTo)`. Null `validTo` = open. Query at exact `validTo` **excludes** the ended segment. |
| Overlap / gap | Overlap inside one snapshot is illegal. Gaps are **unknown**, not false. |
| Correction | Replace the *current* assertion timeline with a new complete snapshot. Do not mutate prior snapshots. |
| Payload | Opaque pinned artifact. Optional `SchemaPin` and `LifecycleProfilePin` are immutable attachments, not engines. |
| Clock | Absolute UTC, whole seconds, explicit `Z`. Reject floating / local / unknown-zone / `:60` leap-second / undeclared sub-second. Never silent truncate. |
| Equal instants | Allowed iff `receiptSequence` differs and increases. Sequence is the total order. Instant is audit metadata. |
| Caller-set record time | Forbidden, except a named offline-bootstrap import tagged `importedSourceHistory ≠ firstLocalReceipt`. |
| Conflict | Expected-head + idempotency key. Reject persists a `ConflictArtifact`. No silent winner. Compose EM-XCT-02 write authority as a host precondition. |
| Pre-first-receipt query | Return **unknown / insufficient-context**, never current data, never Boolean false. |
| Archive | Must not destroy addressable snapshots. Erasure is a separate retention sibling and cannot promise eternal retention against local rules. |
| Security | Read access is evaluated at query time. A reference callable that receives host-trusted policy decisions is not a security boundary. |

### Alternatives rejected for v0.1 (recommend reuse / profile / defer instead)

| Alternative | Why not now |
|---|---|
| New universal `TemporalValidity` WM type | 009 already owns interval shapes; 021 already owns the three times. A new ontology duplicates both and does not give an executable knowledge-cutoff. |
| Wrap XTDB / SQL temporal tables as the contract | Those are engines. Adapters later, with declared loss. XTDB portion-upsert silently overwrites; MS tables are system-time only and can delete history. |
| Event-sourced fold as the fact | Expected-head and opaque bytes are useful. Reconstructing “effective at / known at” is host work, not this contract. |
| Embed SCXML / 021 transition executor | Forbidden: no universal domain lifecycle, no statechart engine. History pseudostates are pause/resume, not audit. |
| Per-segment mutable schema compiler | Collapses revision identity with schema identity; invites a schema engine. |
| Multi-valued / contested timeline inside one scope | International matrix needs **separate contested scopes** (EM-XCT-02), not a silent merge. |
| Closed-closed intervals | Query-at-end would include the ended segment. XTDB and the assignment both require closed-open. |
| Default “now / best-known” query | Hides unknown-before-first-receipt. |

### Four registry candidates — explicit dispositions

The research card names `TemporalValidity`, `Revision`, `LifecycleTransition`, `SchemaBinding` as candidates. None of them should be exported as a new WM type from this companion.

**1. TemporalValidity — PROFILE / shared-contract facet. Do not mint a new WM type.**

009 supplies instant / interval / duration / precision / bindingMode / openEndpoint. 021 already names valid / record / observation and as-of / as-at reconstruction. 022 delegates general effective time. OWL-Time gives Instant / Interval / Allen topology and **does not** resolve valid time as a knowledge axis (2022 CRD Appendix E, requirement 5.56: “not resolved explicitly”).

This companion **binds** those shapes onto one fact scope:

- `validFrom` / `validTo` — 009 interval shape, companion convention half-open, null end = open  
- `receiptInstant` — 009 instant shape, UTC-second profile, host-assigned record time  
- `receiptSequence` — **not a time field**  
- `observationTime` / `sourceEventTime` — optional; cannot alter receipt  

Do not collapse domain event, transition, revision identity, schema version, status code, record time, valid time and observation time into one field.

**2. Revision — DECOMPOSE / REFERENCE 022. Do not call the companion commit `Revision`.**

022 already owns opaque revision identity, series vs designation, predecessor DAG, fixity, expected-current-revision. PROV-DM §5.2.2 defines Revision as “a derivation for which the resulting entity is a revised version of some original.” That is derivation of an *entity*, not a knowledge-cutoff.

Companion object: `TimelineCommit` / `KnowledgeSnapshot`, keyed by `(factScopeId, receiptSequence)`. Optional `predecessorCommitId`. Optional alignment: snapshot entity `prov:wasRevisionOf` predecessor snapshot; `prov:generatedAtTime` may annotate artifact creation in the world. **Host receipt is not `prov:generatedAtTime`.**

**3. LifecycleTransition — DELEGATE / DEFER to 021 + host domain profile.**

021 already owns the governed machine, axes, append-only transition history, and host-owned domain meaning. SCXML Rec 2015 §3.10 `<history>` records active descendant configuration for **resume**, shallow or deep. It is not an audit log, not valid-time, not record-time.

Companion may carry an optional immutable `LifecycleProfilePin` (`profileId`, `profileVersion`, `digest`, optional axis-code annotations). It does **not** execute transitions, store SCXML, or treat an allowed-state list as proof that a domain transition occurred, was legal, or was authorized. No universal domain lifecycle.

**4. SchemaBinding — LOCAL BINDING in v0.1; later profile may promote it.**

Two options assessed:

- **A. Per-segment immutable keyed SchemaBinding records** (schemaId, version, digest, domain-state axes). Richer. Duplicates 022 designation + 021 axes. Invites a schema engine the assignment forbids.
- **B. Recommended for first executable contract:** payload is opaque bytes + media type + content digest. Snapshot **MAY** carry `SchemaPin { schemaId, versionGrammar, version, digest }`. The contract checks pin presence, grammar declaration, and digest conflict. It does **not** prove semantic validity. SemVer 2.0.0 item 3 (released version contents MUST NOT be modified) is an immutability rule for a *package*, not a validity proof of bound content. SemVer item 1 requires a declared public API. Digest integrity ≠ semantic validity. State string `active` is not a schema version. Object revision identifier remains opaque.

---

## 2. Three schools

### School A — Primary standards / ontologies

**OWL-Time**, W3C Candidate Recommendation Draft 15 November 2022 (latest published URI https://www.w3.org/TR/owl-time/; dated https://www.w3.org/TR/2022/CRD-owl-time-20221115/). A 19 October 2017 Recommendation exists; cite the 2022 CRD as current published latest. CR publication “does not imply endorsement by W3C and its Members.”

Gives: `time:Instant` (zero extent), `time:Interval`, `time:ProperInterval` (non-zero extent, beginning ≠ end, disjoint Instant), `time:Duration`, `time:TemporalEntity`; `hasBeginning` / `hasEnd` / `before`; Allen relations on ProperInterval; `inXSDDateTimeStamp` (timezone mandatory). Does **not** give: valid vs record vs observation; as-of / as-at; half-open `[from,to)` as a first-class type; unbounded end; host receipt sequence; leap-second handling (lexical forms ignore leap seconds); schema binding; lifecycle.

**W3C PROV-DM / PROV-O**, Recommendation 30 April 2013. Entity, Activity, Agent; Generation (§5.1.3) and Invalidation (§5.1.8); optional times; `prov:generatedAtTime` / `prov:invalidatedAtTime` range `xsd:dateTime` (offset **not** mandatory — weaker than 009 / OWL-Time `dateTimeStamp`); Revision as a derivation subtype. Does **not** give knowledge cutoff, schema binding, domain lifecycle, or host receipt sequence. Generation time is entity-existence time, not “when the Dimension learned.”

**SemVer 2.0.0.** Grammar `X.Y.Z[-pre][+build]`. MAJOR / MINOR / PATCH encode a **declared public API** compatibility promise. Item 3: released package contents MUST NOT be modified. Does **not** give object revision identity, schema semantic validity, temporal validity, or a mapping from status string `active`.

**SCXML**, W3C Recommendation 1 September 2015, §3.10. History pseudostates remember configuration for re-entry. Not audit history. Not bitemporal. Not schema versioning.

**Parent mixins 009 / 021 / 022** (retrieved above) are the Vercy-local members of this school: conceptual composition, no resolved runtime imports, holds left standing.

**What this school contributes:** vocabulary discipline. Instants ≠ intervals. Valid ≠ record ≠ observation. Revision ID ≠ version designation ≠ schema version ≠ state code. History-for-resume ≠ history-for-audit.  
**What it does not contribute:** an executable fact-scope knowledge-cutoff with expected-head and opaque payload.

### School B — Real open-system temporal implementations

**XTDB (current public XT2 docs).** Two axes: `_system_from` / `_system_to` (database-owned; “Users (rightly) have no control over system-time”) and `_valid_from` / `_valid_to` (user-editable). Closed-open. Default query is system-time “as best known”, valid-time “as of now”. `FOR SYSTEM_TIME AS OF` reconstructs belief without later corrections. `FOR VALID_TIME AS OF` reconstructs current corrected belief about a real-world instant. `FOR PORTION OF VALID_TIME` updates a slice; INSERT on an existing id upserts and **overwrites** the specified valid-time range. Observation time is not a third axis. Repeatability needs both a snapshot token and clock time. XTDB notes that defaulting UPDATE/DELETE to now→∞ **deviates** from SQL:2011’s “all valid time” default — cited only as XTDB’s own documentation, not as SQL:2011 text.

**Microsoft system-versioned temporal tables** (Learn, SQL Server / Azure SQL, `sql-server-ver17`). **System-time only.** Period columns are `GENERATED ALWAYS`; callers cannot set them. Columns are often named `ValidFrom` / `ValidTo` — a naming collapse. `FOR SYSTEM_TIME AS OF` uses `ValidFrom <= t AND ValidTo > t` (closed-open on system time). `HISTORY_RETENTION_PERIOD` **permanently deletes** aged history rows; documentation warns not to rely on business logic that reads history beyond the retention period. Cannot express the synthetic assignment (learn on 10 Feb that Team B applied from 20 Jan) as a valid-time correction. Zero-duration rows from multiple updates in one transaction are filtered from `FOR SYSTEM_TIME`.

**What this school contributes:** closed-open works; system time must be engine/host-owned; as-of-system ≠ as-of-valid; portion-upsert is convenient and dangerous.  
**What it collapses:** observation time; contested writes (XTDB last portion-write wins); schema / lifecycle pins; explicit receipt sequence (hidden in the log); and, in the Microsoft case, valid time itself plus history under retention.

### School C — Event-sourcing / records / revision DAG

**Datomic** (retrieved data-model + filters). Datom = `(E A V Tx Op)`. Transactions are fully serialized; `t` / tx id is a total order. `:db/txInstant` is wall-clock and **can collide** in the same millisecond; Datomic best practice is to as-of by `t` / tx, not by Date. `as-of` ignores later transactions — knowledge cutoff. `history` includes retractions. Correction is a new transaction that retracts and asserts; the old `as-of` still sees the old value. Valid time is not first-class (it would be just another attribute).

**EventStore / Kurrent append API** (Benjamin retrieved appending docs). Append-only stream; `ExpectedVersion` / `expectedRevision` is optimistic concurrency — maps to expected-head. Events are opaque bytes + type + metadata. Reconstructing “effective at date / known at date” is an **application fold**, not a store primitive. Recorded position ≠ domain event time unless the payload says so.

**WM-XCT-022 predecessor DAG** (retrieved) is the Vercy-local member: multi-parent merges allowed; revision identifier immutable and never reused; expected-current-revision precondition; general effective time delegated.

**What this school contributes:** append-only; expected-head; opaque payload; correction without rewriting the past; sequence (not wall-clock) as the knowledge-cutoff total order.  
**What it does not contribute:** a valid-time interval algebra. That remains host work unless this companion stores snapshots.

### Synthesis across schools (inference)

The tentative design is a **hybrid that refuses to become an engine**:

- From School A: keep the fields uncollapsed; reuse 009 shapes and 021 three-time words; schema version grammar optional SemVer; revision id opaque.  
- From School B: closed-open; host-owned record time; as-of-known ≠ as-of-valid; **reject** XTDB-style portion overwrite and MS-style destructive retention as *the* model.  
- From School C: append-only commits, expected-head, idempotency key, opaque payload, sequence as total order.

Correction is a **new complete snapshot** (School C + assignment), not a portion upsert (School B XTDB) and not an in-place edit (forbidden by 021).

---

## 3. Types, identity, lifecycle, fields, facets

Exported types are **companion-local**. They are not subtypes of WM-XCT-009 / 021 / 022 and not the four registry candidate names.

Ownership rule for every type: the **host Dimension** is master of record. The companion defines shape and invariants. Write authority is a trusted host precondition (EM-XCT-02 `WriteGrant`). Disclosure of a snapshot or conflict artifact follows the host’s current projection policy, evaluated at query time.

### 3.1 `FactScope`

Identity of one governed single-valued fact.

| Field | Card. | Notes |
|---|---|---|
| `factScopeId` | 1 | Opaque host identifier. Not a time, not a digest. |
| `dimensionRef` | 1 | Identity reference (EM-XCT-01 style), not a proof. |
| `subjectRef` | 1 | Same. |
| `predicateId` | 1 | Governed predicate in the host namespace. |
| `contextRef` | 0..1 | Scope qualifier (legal entity, book, environment, model-family). Absence is part of the key, not a wildcard. |
| `valueCardinality` | 1 | Fixed `single`. Multi-valued / contested facts are other scopes. |
| `masterSystemRef` | 1 | Who may mint receipt sequence for this scope. |
| `clockProfileId` | 1 | For v0.1: `utc-second-absolute`. |

Lifecycle: opened / closed-to-writes / archived (archive ≠ erase). Closing writes does not delete snapshots.

**Five facets**

1. **Identity / class** — one scope key; class is “governed single-valued fact”, not a domain entity.  
2. **Direct properties** — the four-part key, cardinality, master, clock profile.  
3. **Recognition / observation** — a scope is recognised by exact key match. Partial keys are insufficient-context.  
4. **Capabilities / actions** — `open`, `commit`, `queryAsOf`, `archive`, `exportHistory`. Not `mergeContested`, not `executeTransition`.  
5. **Context / evidence** — mastership and write-grant live in EM-XCT-02; this type only carries the refs.

### 3.2 `TimelineCommit`

One append-only receipt.

| Field | Card. | Notes |
|---|---|---|
| `commitId` | 1 | Opaque. 022-style revision identity of *this commit*, not of the host subject. |
| `factScopeId` | 1 | |
| `receiptSequence` | 1 | Host-assigned integer / ULID-seq. Strictly increasing per scope. Total order. |
| `receiptInstant` | 1 | Host-assigned UTC second. Caller cannot set, except tagged bootstrap. |
| `predecessorCommitId` | 0..1 | Expected head. Required on all commits after the first. |
| `idempotencyKey` | 1 | Digest of the original request. |
| `requestDigest` | 1 | Canonical bytes of this request. |
| `commitKind` | 1 | `assert` \| `correct` \| `importBootstrap` \| `rejectConflict` |
| `actorRef` | 1 | Authenticated by host; companion does not authenticate. |
| `snapshotId` | 1 | The immutable snapshot produced (or, for `rejectConflict`, the unchanged head plus a conflict artifact). |
| `sourceEventTime` | 0..1 | Optional metadata. Cannot alter receipt. |
| `observationTime` | 0..1 | Optional. 021 / EM-XCT-03 sense. |
| `importTag` | 0..1 | Required when `commitKind = importBootstrap`. Distinguishes imported source history from first local receipt. |

Lifecycle: committed (terminal). No in-place edit. A later correction is a new commit.

**Five facets**

1. **Identity** — `commitId` opaque; sequence unique per scope.  
2. **Direct properties** — the receipt pair, kind, digests, optional source/observation times.  
3. **Recognition** — recognised as the knowledge-cutoff atom. Two commits with the same instant are distinct iff sequences differ.  
4. **Actions** — none after commit except `query` and `export`.  
5. **Context / evidence** — actor is a reference, not a proof; evidence of the *domain* fact lives on the snapshot payload and/or EM-XCT-03.

### 3.3 `KnowledgeSnapshot`

Immutable complete assertion timeline as believed at a commit.

| Field | Card. | Notes |
|---|---|---|
| `snapshotId` | 1 | Opaque. |
| `commitId` | 1 | 1–1 with the producing commit. |
| `segments` | 0..N | Ordered by `validFrom`. Bounded by host `maxSegmentCount` / `maxSnapshotBytes`. |
| `schemaPin` | 0..1 | See §3.5. |
| `lifecycleProfilePin` | 0..1 | See §3.6. |
| `snapshotDigest` | 1 | Digest of canonical snapshot bytes. |
| `completeness` | 1 | `complete-for-scope`. Partial snapshots are illegal in v0.1. |

Lifecycle: immutable from birth. Addressable forever unless a *separate* erasure disposition runs.

**Five facets**

1. **Identity** — snapshot of a scope at a receipt, not a version of the subject.  
2. **Direct properties** — segment list, pins, digest.  
3. **Recognition** — retrieved by `(factScopeId, receiptSequence)` or `(factScopeId, receiptInstant+sequence)`.  
4. **Actions** — `queryValidAt`, `export`, `diffAgainst(otherSnapshot)`. No mutate.  
5. **Context / evidence** — pins declare *which* schema/profile were claimed, not that the payload is semantically valid.

### 3.4 `ValidSegment`

One half-open interval inside a snapshot.

| Field | Card. | Notes |
|---|---|---|
| `validFrom` | 1 | UTC-second instant. Inclusive. |
| `validTo` | 0..1 | Exclusive. Null = open. |
| `payloadRef` | 1 | Opaque artifact (bytes or content-addressed blob). |
| `payloadDigest` | 1 | |
| `payloadMediaType` | 1 | |
| `domainStateAnnotation` | 0..1 | Host code + code-system pin. Annotation, not a transition proof. |

Invariants: `validFrom < validTo` when `validTo` present; no overlap with another segment in the same snapshot; adjacency (`meets`) allowed; gaps allowed.

**Five facets**

1. **Identity** — identity is position in a snapshot, not a durable world object.  
2. **Direct properties** — interval + opaque payload + optional state annotation.  
3. **Recognition** — a query instant `t` matches iff `validFrom ≤ t < validTo` (or `validTo` null). `t == validTo` does not match.  
4. **Actions** — none independently; only via snapshot query.  
5. **Context / evidence** — payload may point at EM-XCT-03 evidence; the segment does not infer truth.

### 3.5 `SchemaPin`

| Field | Card. | Notes |
|---|---|---|
| `schemaId` | 1 | Host schema identifier. |
| `versionGrammar` | 1 | e.g. `semver-2.0.0` \| `opaque` \| `host-named`. Must be explicit. |
| `schemaVersion` | 1 | Must match the declared grammar. |
| `schemaDigest` | 1 | Digest of the schema document the writer claims. |
| `compatibilityClaim` | 0..1 | Writer-asserted. Not verified by this contract. |

Not a schema registry. Not a WM type. Digest match ≠ semantic validity. SemVer compatibility claim ≠ payload valid.

### 3.6 `LifecycleProfilePin`

| Field | Card. | Notes |
|---|---|---|
| `profileId` | 1 | Host / 021 lifecycle definition id. |
| `profileVersion` | 1 | |
| `profileDigest` | 1 | |
| `axisAnnotations` | 0..N | `{ axisId, stateCode, codeSystemId, codeSystemVersion }` |

Enforcing that `stateCode` is in a published list is a **pin check**, not proof of a legal transition.

### 3.7 `ConflictArtifact`

Persisted when a write is refused.

| Field | Card. | Notes |
|---|---|---|
| `conflictId` | 1 | |
| `factScopeId` | 1 | |
| `reason` | 1 | `expected-head-mismatch` \| `idempotency-bytes-conflict` \| `overlap-in-snapshot` \| `clock-rejected` \| `schema-pin-conflict` \| `authority-denied` \| `snapshot-overflow` \| `unsupported-downgrade` |
| `attemptedRequestDigest` | 1 | |
| `headCommitId` | 0..1 | |
| `receiptInstant` | 1 | Host time of the *rejection*. |
| `receiptSequence` | 1 | Rejections consume sequence so the refusal is itself history. **Proposal.** Alternative: store conflicts off-sequence; rejected because it would let a later reader miss the refusal. |

Compose with EM-XCT-02: do not fabricate a winner; preserve competing records.

### 3.8 `AsOfQuery`

| Field | Card. | Notes |
|---|---|---|
| `factScopeId` | 1 | |
| `validAt` | 0..1 | Required for “what was effective”. |
| `knownAtSequence` | 0..1 | Knowledge cutoff by sequence (preferred). |
| `knownAtInstant` | 0..1 | Allowed only together with sequence, or as an upper bound that the host resolves to the greatest sequence with `receiptInstant ≤ knownAtInstant`. Instant-only cutoff is **imprecise** when instants collide (Datomic lesson). |
| `result` | 1 | `value` \| `unknown-before-first-receipt` \| `unknown-gap` \| `insufficient-context` \| `denied` |

Empty or uncovered scope is `insufficient-context`, not evidence the fact is false.

### Ownership, mastership, disclosure

- Master of receipt sequence and snapshots: the host system named on `FactScope.masterSystemRef`.  
- Multiple international masters: **multiple scopes**, not one scope with two masters.  
- Competing sources: EM-XCT-02 contested scope + this contract’s conflict artifact.  
- Disclosure: current reader rights, current projection policy. Historic permission is not replayed. Denied historical read returns `denied`, not a filtered-as-complete snapshot (EM-XCT-02: “Never disclose a selectively filtered register as complete”).

---

## 4. Question routes

Bundle → Layer → Finding → Question → Artifact → allowed action.  
Unknown / missing context is an explicit action, not a guessed default.

**B1 Fact-scope identity**

1. **L** Scope key · **F** Four-part identity · **Q** Which Dimension, subject, predicate and context is this fact? · **A** `FactScope` record · **Act** If any part missing → `insufficient-context`. Do not wildcard context.  
2. **L** Cardinality · **F** Single-valued · **Q** Is more than one current value claimed for this exact key? · **A** second `FactScope` or `ConflictArtifact` · **Act** Refuse to merge. Open a contested scope (EM-XCT-02) or reject.

**B2 Receipt and knowledge cutoff**

3. **L** Record time · **F** Host-assigned receipt · **Q** What did this Dimension know at cutoff *K*? · **A** snapshot whose `receiptSequence` is max `≤ K` · **Act** If no commit yet → `unknown-before-first-receipt`. Never return later current data.  
4. **L** Record time · **F** Instant vs sequence · **Q** Two commits share a UTC second; which is later knowledge? · **A** `receiptSequence` · **Act** Order by sequence. Do not invent a later timestamp.  
5. **L** Clock profile · **F** UTC-second absolute · **Q** Writer sent a local date, offset-without-zone, `:60`, or sub-second? · **A** clock-rejected `ConflictArtifact` · **Act** Reject. Never truncate. Adapter required, loss recorded.  
6. **L** Bootstrap · **F** Imported ≠ local · **Q** Is this offline history or first local receipt? · **A** `importTag` on `TimelineCommit` · **Act** If tag missing on bootstrap → reject. If tag present on ordinary commit → reject.

**B3 Valid time**

7. **L** Interval convention · **F** Half-open · **Q** Does a query at exact `validTo` include the ended segment? · **A** `AsOfQuery` · **Act** No. Include iff `validFrom ≤ t < validTo`.  
8. **L** Topology · **F** Overlap illegal, gap unknown · **Q** Do two segments overlap inside this snapshot? · **A** rejected snapshot + `overlap-in-snapshot` conflict · **Act** Refuse commit.  
9. **L** Topology · **F** Gap · **Q** No segment covers `validAt`? · **A** `unknown-gap` · **Act** Not Boolean false. Not “use neighbouring segment”.

**B4 Correction**

10. **L** Correction vs new event · **F** New snapshot, old snapshots kept · **Q** We learned on 10 Feb that Team B applied from 20 Jan. What is valid 1 Feb / known 31 Jan? valid 1 Feb / known 11 Feb? valid 15 Jan / known 11 Feb? · **A** three `AsOfQuery` results against two snapshots · **Act** A, B, A respectively. Prior snapshot remains addressable. (Worked in §7.)  
11. **L** Correction vs provenance · **F** Align EM-XCT-03 · **Q** Is this a metadata correction or a new domain event? · **A** `commitKind` + optional EM-XCT-03 activity pin · **Act** If identity of the activity would change, mint a new event in 03; do not silently retitle a correction.

**B5 Concurrency and authority**

12. **L** Expected head · **F** Lost update · **Q** Writer’s `predecessorCommitId` ≠ current head? · **A** `expected-head-mismatch` conflict · **Act** Reject. Persist artifact. Do not apply.  
13. **L** Idempotency · **F** Request digest · **Q** Same key, different bytes? · **A** `idempotency-bytes-conflict` · **Act** Reject. Same key + same digest → return original success.  
14. **L** Write authority · **F** Host precondition · **Q** Is the actor granted on this scope? · **A** EM-XCT-02 `WriteGrant` (not this contract) · **Act** If host says no → `authority-denied` conflict. Companion callable is not a security boundary.

**B6 Schema and lifecycle pins**

15. **L** Schema pin · **F** Grammar explicit · **Q** `schemaVersion = active` with no grammar, or digest mismatch? · **A** `schema-pin-conflict` · **Act** Reject bind. Success still ≠ semantic validity.  
16. **L** Lifecycle pin · **F** Annotation ≠ proof · **Q** Segment annotated `active`; did a legal transition occur? · **A** pin + optional 021 transition record (elsewhere) · **Act** Do not infer legality. Do not run SCXML.

**B7 Access, archive, migration**

17. **L** Disclosure · **F** Query-time rights · **Q** May this reader see history as of *K*? · **A** current projection decision · **Act** If no → `denied`. Do not replay 2024 ACLs. Do not return a filtered snapshot labelled complete.  
18. **L** Archive · **F** History retained · **Q** May archival delete snapshots older than N days? · **A** archive job record · **Act** No. Tombstone visibility ≠ delete. Erasure is a separate disposition and cannot promise eternal retention.  
19. **L** Adapter / downgrade · **F** Loss declared · **Q** Project onto MS system-versioned tables or XTDB portion-upsert? · **A** adapter loss report · **Act** Not silently executable. Unsupported downgrade → refuse or emit explicit loss (valid-time dropped, observation dropped, history deletable, conflicts auto-resolved).

---

## 5. Invariants and negatives

### Eight (plus) testable invariants

**I1 Half-open exclusion.** For snapshot *S* and instant *t*, segment *G* contributes iff `G.validFrom ≤ t` and (`G.validTo` is null or `t < G.validTo`). A query with `t == G.validTo` must not return *G*.

**I2 No overlap in one snapshot.** For any two segments of *S*, they are disjoint or they *meet* (`A.validTo == B.validFrom`). Overlap ⇒ commit refused.

**I3 Gaps are unknown.** Absence of a covering segment at `validAt` yields `unknown-gap`, never a Boolean false and never a borrowed neighbour.

**I4 Append-only knowledge.** Commit *n* does not mutate snapshot *n−1*. Query `(validAt, knownAtSequence=n−1)` after commit *n* returns the pre-correction belief.

**I5 Sequence total order.** Per `factScopeId`, `receiptSequence` is strictly increasing. Equal `receiptInstant` values are legal iff sequences differ. Caller cannot assign `receiptInstant` on ordinary commits.

**I6 Expected-head.** A non-bootstrap commit with `predecessorCommitId ≠ currentHead` is refused and a `ConflictArtifact` is persisted. No silent winner.

**I7 Idempotency.** Same `idempotencyKey` + same `requestDigest` → original result. Same key + different digest → conflict, no apply.

**I8 Clock profile.** Instants that are not UTC-second absolute under the declared profile are refused. No silent truncation, no leap smear, no drop of binding mode.

**I9 Pins are claims.** Accepting a `SchemaPin` or `LifecycleProfilePin` checks presence, declared grammar, and digest conflict only. It does not prove semantic validity, SemVer compatibility of meaning, or that a domain transition occurred.

**I10 Archive ≠ erase.** An archive operation must leave every previously addressable snapshot addressable or explicitly tombstoned. Destructive retention (MS `HISTORY_RETENTION_PERIOD` style) is not archive.

**I11 Pre-receipt unknown.** A knowledge cutoff before the first successful commit on the scope yields `unknown-before-first-receipt`, not current data.

**I12 Query-time authorization.** `denied` is computed from rights at query time. Historic grants are not replayed.

### Ten meaningful negatives

**N1 Historical correction rewrite.** After the Team-B correction, a query valid 1 Feb / known 31 Jan returns Team B. — Fail I4.

**N2 Idempotency collision.** Same idempotency key, different payload bytes, second write accepted as a new head. — Fail I7.

**N3 Head conflict swallowed.** Stale writer omitted `predecessorCommitId` or sent an old one; server applies and overwrites. — Fail I6. XTDB portion-upsert is this failure mode if used as the model.

**N4 Denied historical read disguised.** Reader lacks current history right; server returns a redacted snapshot labelled complete, or returns current public value as if it were the historical value. — Fail I12 + EM-XCT-02 completeness rule.

**N5 Incompatible schema binding accepted as valid.** Pin says `schemaVersion=2.0.0` / digest *D1*; payload was produced against digest *D2*; commit accepted and treated as semantically valid because “2.0.0 is SemVer-compatible with 1.x”. — Fail I9.

**N6 Clock misuse / forged knowledge.** Writer sets `receiptInstant` to last year on an ordinary commit, or sends `2026-01-01T00:00:00` with no zone and the host assumes UTC. — Fail I5 / I8.

**N7 Overlap inside a snapshot.** Segment `[2026-01-01, 2026-02-01)` Team A and `[2026-01-20, ∞)` Team B in the *same* snapshot. — Fail I2. (Correction puts them in *different* snapshots.)

**N8 Gap treated as false.** No segment covers 15 Jan in the current snapshot; query returns “not assigned” as a negative fact. — Fail I3.

**N9 Archive destroys history.** Compaction deletes snapshots older than 90 days so known-at-January is unanswerable. — Fail I10. Direct counterexample: Microsoft history retention delete.

**N10 Unsupported downgrade executed silently.** Host projects the timeline onto a system-versioned table named `ValidFrom`/`ValidTo`, dropping valid-time and observation-time, then answers “as of valid 1 Feb” from system-time columns. — Fail adapter rule. Also: treating SCXML `<history>` as audit history; treating state `active` as schema version; including the ended segment at exact interval end (closed-closed).

---

## 6. Three synthetic profiles

These are synthetic. They are not facts about named companies.

### 6.1 Startup — no mandatory ERP

**Need.** A ten-person company records role assignments and subscription states in Markdown / a single store. One Dimension, one master, manual source.

**Profile use.** One `FactScope` per assignment predicate. Manual commits. `SchemaPin` optional; payload can be a JSON object pinned by digest. No lifecycle engine. EM-XCT-02 write grant is “founder + ops”. EM-XCT-03 capture is a dated note.

**Migration / loss.** Later adoption of an HRIS is an **adapter**: import tagged `importBootstrap`; HRIS `updated_at` is not `receiptInstant`. Loss if the HRIS cannot answer as-of-known. Do not auto-fold HRIS rows into valid-time portions.

**What they must not do.** Install an ERP to satisfy this contract. Treat “current row” as history.

### 6.2 International matrix group — multiple scopes / masters

**Need.** Legal entity A (EU) and legal entity B (US) both assert the same person’s cost-centre. Different masters, different valid-time rules, possible contest.

**Profile use.** Two `FactScope`s, differing by `contextRef` (legal entity) and `masterSystemRef`. If a group Dimension wants a single predicate without context, that is a **third** scope whose write authority is contested (EM-XCT-02). This contract does not silently merge A and B.

**Migration / loss.** Cross-scope query is a projection with declared precedence. Loss: a “group as-of” that hides which master spoke. Time zones: each master still writes UTC-second; local pay-calendar arithmetic stays in 009 working-day profiles, not here.

**What they must not do.** One scope, two masters, last-write-wins.

### 6.3 AI organisation — artifact version ≠ deployment state ≠ record about state

**Need.** Model weights `sha256:…` (artifact revision, 022), endpoint status `serving` / `draining` (021 host lifecycle), and the *record* “as of 1 Sep / known 3 Sep, prod-us-east was serving build 12”. Those three must not share a field.

**Profile use.**

- Artifact bytes: 022 revision + digest. Not this contract.  
- Deployment state machine: 021 profile. Not executed here.  
- Fact “environment E runs artifact R”: this companion. Payload pins `artifactRevisionId` + digest. `LifecycleProfilePin` may annotate `serving`. `SchemaPin` pins the release-manifest schema. Observation time may record when a probe saw the endpoint; it does not move receipt.

**Migration / loss.** Promoting “the model is active” as both schema version and state fails N10. Shipping a new weight under the same revision id fails 022. Treating registry “yank” as history delete fails I10.

**Adapters, not silently executable**

| Target | Loss that must be declared |
|---|---|
| XTDB | Portion overwrite; no observation axis; receipt sequence hidden in log token; default now/best-known hides pre-receipt unknown. |
| MS temporal tables | Valid time dropped; observation dropped; pins dropped; history may be deleted by retention; `ValidFrom` is system time. |
| EventStore stream | Valid-time becomes a fold; as-of-valid not primitive; event-type string is not `SchemaPin`. |
| Datomic | Valid-time must be modelled as attributes; as-of by Date loses order when `txInstant` collides. |
| OWL-Time RDF | No knowledge cutoff; ProperInterval cannot encode open end without an extension; leap seconds ignored. |
| SCXML document | No audit, no bitemporal, no schema pin. |

An adapter that cannot preserve I1–I12 must refuse or emit a machine-readable loss list. It must not present the target engine as this companion.

---

## 7. Worked synthetic assignment, counterexamples, holds, acceptance

### Worked timeline (assignment)

Host records on **10 Jan** that a role assignment is effective **1 Jan onward** to Team A.  
On **10 Feb** it learns Team B actually applied **20 Jan onward**.

| Query | Snapshot used | Result |
|---|---|---|
| valid 1 Feb / known 31 Jan | 10 Jan commit (seq 1) | Team A, segment `[2026-01-01, ∞)` |
| valid 1 Feb / known 11 Feb | 10 Feb commit (seq 2) | Team B, segment `[2026-01-20, ∞)` |
| valid 15 Jan / known 11 Feb | seq 2 | Team A, segment `[2026-01-01, 2026-01-20)` |
| valid 20 Jan / known 11 Feb | seq 2 | Team B (`20 Jan` is included; half-open start inclusive) |
| valid 20 Jan / known 11 Feb if someone stored Team A as `[1 Jan, 20 Jan]` closed-closed | — | Would wrongly exclude 20 Jan from A and depend on B; this is why end is exclusive |
| query at exact end of A (`validAt = 20 Jan` against `[1 Jan, 20 Jan)`) | seq 2 | A does **not** match; B does |
| valid 1 Feb / known 9 Jan | none | `unknown-before-first-receipt` |
| uncovered context (no `FactScope` for that Dimension) | — | `insufficient-context`, not false |

Correction snapshot seq 2 is complete: `[[2026-01-01, 2026-01-20) A], [[2026-01-20, ∞) B]`. Seq 1 remains queryable. Observation that “HR emailed on 8 Feb” may sit in `observationTime`; it does not become `receiptInstant`.

### Strongest counterexamples to the tentative design

1. **Snapshot-size blow-up.** A high-churn fact (price every minute, corrected often) makes “full snapshot per commit” expensive. **Acceptance:** host `maxSegmentCount` / `maxSnapshotBytes`; overflow → `snapshot-overflow` conflict, not silent truncation. Later profile may allow bounded delta snapshots with a declared reconstruction method (022 already knows snapshot vs forward-delta). Do not pretend v0.1 is cheap at tick frequency.  
2. **XTDB portion-upsert used as the write API.** Last writer wins a contested valid-time range with no conflict artifact. Violates EM-XCT-02 and I6.  
3. **Microsoft `ValidFrom` treated as valid time.** Naming collapse; late valid-time correction becomes inexpressible; retention may delete the audit.  
4. **Datomic as-of by wall-clock.** Two commits in one second; order lost.  
5. **Caller-supplied system time as ordinary write.** Forges knowledge cutoff. XTDB allows monotonic backfill; this contract is stricter: bootstrap-only and tagged.  
6. **Default now/best-known query.** Hides `unknown-before-first-receipt`.  
7. **Lifecycle pin as legality proof.** Allowed-state list ≠ authorized transition. SCXML history ≠ audit.  
8. **SemVer + digest as semantic validity.** Spec does not support that inference.  
9. **Single scope for matrix masters.** Silent merge.  
10. **Closed-closed intervals.** Query at exact end includes the ended segment — fails the assignment.

### Unresolved holds (keep; do not claim to fix parents)

From 009: live editions / claim support; jurisdiction-specific zone and holiday rules; uncertain dates; calendar reform; clock provenance; leap-smear algorithms; paywalled ISO 8601.  
From 021: live source-edition checks; clinical / workflow / release / records profile validation; formal SM verification out of scope.  
From 022: live source pins; inaccessible / paywalled standards (PREMIS, OAIS, ISO 10007/15489); **bitemporal support partial** (no normative SQL source read this run either); source-ID remapping; catalog-record vs resource-revision boundary.  
From this run: enterprise-identity landing 404; parent SHA pins not recomputed; SQL:2011 and ISO 8601 texts not retrieved; EventStore internals not retrieved.

Erasure vs retention remains a sibling. This companion can say “archive must not destroy addressable history” and cannot promise eternal retention against local law.

### Implementation acceptance criteria (for a later frozen audit)

A candidate implementation **passes** only if all of the following are demonstrated with fixtures, not prose:

1. The Team-A / Team-B matrix above, including pre-receipt unknown and exact-end exclusion.  
2. Correction does not mutate snapshot seq 1.  
3. Expected-head mismatch persists a conflict artifact and leaves head unchanged.  
4. Idempotency key same/different bytes behaves as I7.  
5. Caller-set `receiptInstant` on a non-bootstrap commit is refused.  
6. `:60`, floating local, unknown-zone, undeclared sub-second refused with no truncation.  
7. Equal `receiptInstant`, distinct sequences, order by sequence.  
8. Overlapping segments refused; gaps return `unknown-gap`.  
9. `SchemaPin` digest mismatch refused; accepted pin still documented as unproven semantically.  
10. `stateCode = active` cannot be stored in `schemaVersion`.  
11. Historical read without current right returns `denied`.  
12. Archive job cannot physically delete seq 1.  
13. Adapter to MS temporal tables either refuses or emits a loss document that names dropped valid-time and deletable history.  
14. Runtime import list is empty; parents appear only as semantic references.  
15. Catalogue identity is `vr.profile.enterprise-time-states-versions` (or the published slug chosen at issuance), not `vr.wm-xct-009` / `021` / `022`.  
16. Offline bootstrap carries `importTag` and does not share identity with first local receipt.  
17. Snapshot overflow hits the configured bound and refuses.  
18. Reference callable that receives a host “allow” decision is documented as not a security boundary.

Claim grade for these criteria: **proposal**. They are not observed in running code in this run.

---

## Research limitations

- Parent `spec.yaml` bodies were retrieved through a page summarizer, not as raw verified bytes. Assignment SHA pins are Codex structural inspection. Lucas noted a different synthesis hash on the 022 landing page.  
- https://ver.cy/models/enterprise-identity/ was 404.  
- OWL-Time 2022 CRD, PROV-DM 2013 Rec, SCXML 2015 Rec, SemVer 2.0.0, XTDB current docs, Microsoft Learn temporal tables, and Datomic current docs were retrieved as public HTML; several bodies were truncated by the summarizer. Fine-grained clause numbers that do not appear in the extracts should be treated as unverified.  
- SQL:2011 and ISO 8601-1/2 were not read. No conformance claim.  
- EventStore / Kurrent was used only at the public append / expected-version layer.  
- No executable companion was built. No future implementation was audited.  
- Dual-provider parent syntheses (Claude + Grok on 009 / 021 / 022) are themselves reviewable drafts; this research does not re-adjudicate them.  
- Team notes were produced in parallel from the same public URLs; disagreements on slug (`enterprise-time-states-versions` vs `enterprise-fact-timeline`) are naming, not semantics. The recommended slug is `vr.profile.enterprise-time-states-versions` to sit beside EM-XCT-02 / 03.

This research does not authorize publication.
