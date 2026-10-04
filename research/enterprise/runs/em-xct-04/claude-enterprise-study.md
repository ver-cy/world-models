# EM-XCT-04 — Time, states and versions: independent research memo

**Evidence tags used throughout:**
- **[O]** I retrieved it in this session. For sources marked [O], I read a tool-generated summary or extract, not the raw bytes.
- **[S]** A source asserts it, and I saw only that assertion, not the underlying source.
- **[R]** Remembered from training. Not retrieved.
- **[I]** My inference.
- **[P]** A design proposal.
- **[U]** Unverified.

This memo is not a publication approval, and it does not audit any future code.

---

## 0. What I actually retrieved

| Artifact | Result |
|---|---|
| WM-XCT-009 `spec.yaml` | [O] **Partial.** The extract stopped inside `calendar-system/era-and-year-numbering`. I saw bundles `time-base`, `civil-time-zone` and part of `calendar-system`. I did **not** see recurrence, holidays/working days or reference-data releases. |
| WM-XCT-021 `spec.yaml` and landing page | [O] **Partial.** The spec extract stopped in `current-state-assertion`. The landing page listed all 5 bundles and 12 layers (`validity-interval`, `record-time-and-correction`, `succession-and-deprecation`, `invalidation`, `end-of-life`, `lifecycle-operations`, `status-interoperability`, …), but not the finding IDs for bundles 3–5. |
| WM-XCT-022 `spec.yaml` and landing page | [O] **Partial.** The spec extract stopped in `change-note-text`. The landing page listed all bundles, layers and finding IDs. Its holds match your brief: partial bitemporal support, source-ID remapping, paywalled ISO sources, and the catalog-record vs resource-revision boundary. |
| **SHA-256 pins** | **Not verified.** My fetch tool returns processed text, not bytes, so I cannot confirm any digest. |
| enterprise-assertion-provenance (EM-XCT-03 0.1.0), enterprise-fact-authority (EM-XCT-02 0.1.0) | [O] Landing pages only. I did not read the `spec.json` files or the ZIP packages. |
| **enterprise-identity** | **HTTP 404** at `https://ver.cy/models/enterprise-identity/`. Its contents are unverified. |
| W3C OWL-Time | [O] Candidate Recommendation Draft, 15 Nov 2022, not a Recommendation. |
| W3C SCXML | [O] Recommendation, 1 Sep 2015, §3.3, 3.4, 3.7, 3.10, 3.11, 5.2. |
| W3C PROV-DM | [O] Recommendation, 30 Apr 2013. |
| SemVer 2.0.0 | [O] Items 1–3, 8–11 and the BNF top-level production. |
| XTDB "Time in XTDB" and SQL transactions reference | [O] |
| Microsoft Learn, "Temporal Tables" | [O] `ms.date` 2026-08-18, git commit `374edd82…`. |
| RFC 9557 §2.2 | [O] |
| Fowler, "Bitemporal History" (2021) | [O] |
| KurrentDB/EventStoreDB | [O] Search-result excerpts from the Kurrent docs; the page itself was not fetched. |
| ISO SQL:2011, ISO 8601, ISO 15489, RFC 8785, RFC 3339 full text | **Not read.** I make no conformance claims. |

Section numbers above come from tool summaries. Check them against the source before citing them normatively.

---

## 1. Boundary verdict

**Verdict [P]:** a small companion contract is justified, but only as an **executable bitemporal assertion ledger for one single-valued fact scope**. It should not be a new temporal ontology, and it should not subtype WM-XCT-021 or WM-XCT-022.

- **Why the parents are not enough [I]:**
  - All three parents are conceptual research specs with no verified executable instance contract.
  - WM-XCT-022 itself holds bitemporal support as "partial" and delegates general effective time.
  - WM-XCT-021 names valid, record and observation time, but it owns lifecycle semantics, not the value timeline of an arbitrary fact.
  - Nobody currently owns executable answers to "value at valid V as recorded by K", with idempotent and guarded writes.
- **Why it must stay small [I]:**
  - Every hard adjacent problem already has an owner: civil time (009), state meaning (021 host), revision DAG, merge and compatibility (022), authority and contest (EM-XCT-02), and evidence and truth (EM-XCT-03).
  - Repeating any of them would compete with its owner.

**Suggested identity [P]:** `vr.profile.enterprise-fact-timeline`, EM-XCT-04, `0.1.0`, with its own landing page, `spec.json` and package. Runtime imports should be `[]`. Parent relationships should be declared only as `semanticRefs`, and nothing is inherited for readiness. I did not verify the exact reference syntax the published companions use.

**Minimum useful profile [P]: `fact-timeline/utc-s`**
- One FactScope.
- An append-only commit log.
- Each commit carries a full immutable snapshot of half-open `[from,to)` valid segments.
- Host-assigned receipt sequence and receipt instant.
- UTC whole-second precision only.
- Payload is opaque, pinned by digest and SchemaPin.
- Optional state-vocabulary pin, checked for membership only.

**Alternatives considered:**

| Alternative | Assessment |
|---|---|
| (a) A profile of WM-XCT-021's bitemporal layer | [I] Rejected. It would make every fact a "lifecycle state" and push state-machine governance onto non-lifecycle facts such as team assignment or a price. |
| (b) A profile of WM-XCT-022, treating each commit as a revision | [I] Partially attractive. But 022 has a DAG, merge and head semantics; this ledger needs a strictly linear chain per scope, and 022's bitemporal hold would carry over. **Reuse 022's concepts by reference** (head pointer, revision identity, compatibility-declaration). Do not profile it. |
| (c) Pure delegation to host databases (XTDB, SQL temporal) | [I] Rejected as the *contract*, because the engines differ: XTDB lets users set system time; SQL Server has only system time. These are good *adapter targets*. |
| (d) Event-sourced deltas (per-segment operations instead of full snapshots) | [I] Deferred to a later profile. Deltas make "what did we believe at K" a replay problem and make idempotency and head checks harder to specify. Bounded snapshots are simpler to verify. |

### Registry candidate dispositions

| Candidate | Disposition | Contents |
|---|---|---|
| **TemporalValidity** | **Adopt narrowly** [P] | An executable value type `ValidInterval{from: UtcSecond, to: UtcSecond\|null}`, half-open, where null means explicitly open. It carries `semanticRefs` to 009 `time-base/instant-precision-and-resolution/instant-representation` and to 021 layer `validity-interval`. Precision, calendar and zone adapters stay with 009 and are **not** implemented here. |
| **Revision** | **Split** [P] | (1) Timeline commit identity (`scopeKey`, `receiptSeq`) is **owned** here and is linear, with no branches. (2) Object and artifact revision identity is **delegated** to 022 as an opaque `objectRevisionRef` carried inside a segment payload binding. No predecessor DAG, merge or diff. |
| **LifecycleTransition** | **Delegate / defer** [P] | Not an exported type. The ledger can record a *state value* in effect during a valid segment, pinned to a host vocabulary. Transitions (trigger, guard, legality, actor) stay with 021 and the host. Evidence that a transition happened is an EM-XCT-03 assertion reference. |
| **SchemaBinding** | **Adopt minimally** [P] | An immutable `SchemaPin{schemaId, versionScheme, schemaVersion, schemaDigest, mediaType}` per segment. The contract checks pin syntax and that the pin exists in the host registry; it does **not** check payload conformance. Compatibility is never inferred; it may point to a 022 `compatibility-declaration`. |

### Assessing Option A vs Option B for schema and lifecycle binding

- **Option A** is immutable keyed schema and lifecycle records with domain state axes, enforced.
- **Option B** is opaque pinned payload, with transitions as externally governed evidence.

**Recommendation [P]:** use Option B as the executable core, and take from Option A only the part that can be checked.

| Aspect | Option A: enforce | Option B: opaque and pinned | Decision |
|---|---|---|---|
| Schema identity | Keyed record with ID, version and digest | Same pin | **Keep the pin (A).** It is cheap and checkable. |
| Payload validation | The contract validates the payload against the schema | Opaque; the host may attach a validation attestation | **B.** Otherwise the contract needs a JSON Schema, Avro or XSD engine, and that is a runtime import. |
| State axes | Enforced allowed-list per axis | Stored as data | **Membership check only**, reported as `vocabularyMember=true`. It never means `transitionValid`. |
| Transition legality | Checked against a statechart | External evidence | **B.** SCXML §3.10 `<history>` is a pseudostate that restores a configuration [O]. It is not an audit log, and SCXML specifies none [O]. |

---

## 2. Comparing schools of thought

| School | Source | What it contributes | What it does *not* give |
|---|---|---|---|
| **Ontology/standard** | OWL-Time, CR Draft 2022 [O] | `Instant`, `ProperInterval` (distinct beginning and end), `hasTRS`, and `intervalMeets` (the end of T1 coincides with the beginning of T2). This matches adjacent half-open segments [I]. | No record/transaction time. No half-open or closed convention: `inside` excludes the beginning and end, but that is not a storage convention [I]. Not a Recommendation. |
| | SCXML REC 2015 [O] | Configuration = the set of active states (§3.11). `<parallel>` for concurrent axes (§3.4). `<final>` (§3.7). Shallow and deep history (§3.10). | No persistent transition log. Datamodel (§5.2) is runtime data, not a versioned schema pin. |
| | PROV-DM REC 2013 [O] | Entities have "fixed aspects" (§5.1.1). `wasRevisionOf` (§5.2.2). Invalidation (§5.1.8). A bundle is itself an entity, which enables provenance-of-provenance (§2.2.2) [O]. | Per retrieval, no valid-time vs transaction-time distinction. |
| | SemVer 2.0.0 [O] | A grammar (`<valid semver>`). A compatibility promise tied to a declared public API (items 1 and 8). Released contents immutable (item 3). | Semantic validity of data. As I recall [R/U], build metadata is ignored for precedence, so two different pins can have equal precedence. |
| **Real open/commercial systems** | XTDB [O] | Four columns: `_valid_from/_valid_to` and `_system_from/_system_to`. Null means "until further notice". Half-open in its examples. Users "have no control over system-time". `ERASE` removes data "for all valid-time, for all system-time". | Yet a transaction *may* supply `SYSTEM_TIME` as long as it is not earlier than any prior transaction [O]. That is a forgery vector this contract must close. |
| | SQL Server system-versioned tables [O] | `AS OF t` ⇔ `ValidFrom <= t AND ValidTo > t`, i.e. half-open. Time is the transaction begin time in UTC, `datetime2`. All rows in one transaction share one instant. Zero-duration rows are filtered out of `FOR SYSTEM_TIME`. | Only one axis (system time) appears on the page retrieved. Equal instants hide intermediate versions, which motivates a receipt sequence [I]. |
| **Alternative** | Event sourcing (KurrentDB docs, via search excerpt) [O] | Expected version: append only if the stream is at the expected version. Idempotency is keyed on EventId per stream and depends on the concurrency check not being disabled. | Whether "same EventId, different bytes" is detected: unverified [U]. That gap is why this design binds the request digest. |
| | Fowler, "Bitemporal History" [O] | "record history itself *is* append only", shown with a retroactive salary correction. | Informal, not a standard. |
| | WM-XCT-022 revision DAG [O] | `de-predecessor-refs` (zero for a root, more than one for a merge) and `a-merge-record`. | [I] Deliberately not used: a single-valued fact timeline must not merge. |

**Synthesis [I]:** the engines agree on half-open intervals, a system-owned record axis and null meaning open. None of them provides the combination of (i) a sequence that disambiguates equal instants, (ii) digest-bound idempotency, (iii) an unknown-vs-false result, and (iv) the source-time vs receipt split for imported history. That combination is the whole value of the companion.

---

## 3. Types, fields, cardinalities and facets [P]

### 3.1 Primitive decisions
- **`UtcSecond`**
  - Exactly `YYYY-MM-DDTHH:MM:SSZ`.
  - Reject a fractional part, any numeric offset (including `+00:00`), a date without a time, and `SS=60`. The error names the adapter requirement.
  - **Never truncate.**
  - Under RFC 9557 §2.2, `Z` means the UTC instant is known but the local offset is not [O]. That is exactly what this contract needs.
- **Receipt ordering**
  - `receiptSeq` is a uint64 that increases strictly **per ledger**, not per scope, so that one cutoff is consistent across scopes.
  - `receiptInstant` is non-decreasing along `receiptSeq`. Equal instants are **allowed and ordered by seq**.
  - A host clock that goes backwards leads to rejection with `clock-regression`, never clamping.
- **Knowledge cutoff** comes in two forms:
  - `knownAtSeq`: exact.
  - `knownAtInstant`: includes every commit with `receiptInstant ≤ cutoff`, so all equal-instant commits are included together.
- **Schema versions**
  - `versionScheme ∈ {semver-2.0.0, opaque}`.
  - For semver: must match `<valid semver>`, and build metadata (`+…`) is **forbidden in pins**.
  - For opaque: no ordering and no compatibility semantics. It must match a host-registered triple.
  - The **object revision ID is always opaque** and lives in a different field from `schemaVersion`.

### 3.2 Exported types

| Type | Key fields (cardinality) | Identity | Lifecycle |
|---|---|---|---|
| **FactScope** | `dimensionRef` 1, `subjectRef` 1 (identity reference, opaque), `predicateRef` 1, `context` 0..1 (declared keys only), `cardinality="single"` 1, `schemaPolicy` 1, `stateVocabularyPin` 0..1, `status ∈ {open, archived}` 1 | `scopeKey` = digest of the canonical `{dimension, subject, predicate, context}` (canonicalisation profile pinned) | Registered by host config. `open → archived` only; no reopen in 0.1. |
| **TimelineCommit** | `scopeKey` 1, `receiptSeq` 1, `receiptInstant` 1, `expectedHeadSeq` 1 (null only for the first commit), `idempotencyKey` 1, `requestDigest` 1, `snapshot` 1 (0..N segments, N ≤ `maxSegments`, default 1024), `reasonCode ∈ {initial, late-information, error-correction, domain-change, retraction, import}` 1, `authorityDecisionRef` 1, `sourceMeta` 0..1, `origin ∈ {local, imported}` 1 | (`ledgerId`, `receiptSeq`) | Immutable once written. |
| **ValidSegment** (value) | `from` 1, `to` 0..1, `payload{digest, mediaType, bytes\|ref}` 1, `schemaPin` 1, `stateAxes` 0..N (`axisId → code`), `objectRevisionRef` 0..1, `validationAttestationRef` 0..1 | Position within its commit | Immutable. |
| **SchemaPin** (value) | `schemaId`, `versionScheme`, `schemaVersion`, `schemaDigest` (sha256), `mediaType` (all 1) | The whole tuple | Immutable. Registry membership is checked at write. |
| **StateVocabularyPin** (value) | `profileId`, `profileVersion`, `profileDigest`, `axes[{axisId, codes[]}]` | The tuple | Immutable. Meaning is host-owned (021). |
| **ConflictRecord** | `conflictId`, `scopeKey`, `kind ∈ {head-conflict, idempotency-conflict, authority-reject, contested}`, `rejectedRequestDigest`, `observedHeadSeq`, `hostDecisionRef`, `recordedInstant` | Host-assigned ID in a separate conflict log | Append-only. **Never changes the timeline.** |
| **ErasureRecord** | `scopeKey`, `targetSeqs[]`, `segmentsErased`, `erasureBasisRef`, `executedInstant` | Host-assigned ID | Append-only. |
| **TimelineAnswer** (derived, never stored) | `status ∈ {value, unknown, denied, erased}`, `unknownReason ∈ {before-first-receipt, uncovered-valid-time, scope-not-registered, insufficient-context, pre-local-receipt}`, `segment` 0..1, `answeredFromSeq` 0..1, `openConflicts` 0..N | — | — |

### 3.3 Snapshot rules
- Segments are sorted by `from`, and `from < to`.
- No two segments overlap. `[a,b)` followed by `[b,c)` is legal, which matches `intervalMeets`.
- Gaps are allowed and mean unknown.
- At most one segment may have `to = null`, and it must be last.
- An empty snapshot is legal only with `reasonCode=retraction`, and it means "we no longer assert anything" (unknown), **never false**.
- An explicit negative is a domain value, e.g. `"unassigned"` with its own schema.

### 3.4 The five whole-object facets per type

**Assumption:** I could not retrieve Vercy's definition of the "five whole-object facets". The mapping below uses **Identity, Lifecycle, Ownership/Mastership, Disclosure and Provenance**. Replace it with the canonical five if they differ.

| Type | Identity | Lifecycle | Ownership/Mastership | Disclosure | Provenance |
|---|---|---|---|---|---|
| FactScope | `scopeKey` | open → archived | Host names the mastering system per scope. Multi-master means separate scopes, not a merged scope. | Scope existence itself may be sensitive; the host decides at query time. | Registration config ref |
| TimelineCommit | ledger + seq | Immutable; only erasure can redact payload | Write authority is a host precondition (EM-XCT-02 ref) | Evaluated per query, now, not with historic permissions | `sourceMeta` (source-asserted), `origin`, `authorityDecisionRef` |
| ValidSegment | Commit + index | Immutable | Inherits from the commit | Payload may be withheld separately from time bounds | `validationAttestationRef` (claim, not proof) |
| SchemaPin | Tuple | Immutable | Schema owner is the registry authority | Public by default | Registry release ref |
| StateVocabularyPin | Tuple | Immutable | Host domain model (021) | Public by default | Profile release ref |
| ConflictRecord | conflictId | Append-only | Host | Restricted: contains rejected request digests | hostDecisionRef |
| ErasureRecord | ID | Append-only | Host records officer | The fact that an erasure happened is itself retained; its contents are not | erasureBasisRef (legal basis is external) |

### 3.5 Reference worked example

Timeline in the ledger:

| Commit | Received | Snapshot |
|---|---|---|
| seq 1 | 2026-01-10T09:00:00Z | `[2026-01-01T00:00:00Z, null) A` |
| seq 2 | 2026-02-10T09:00:00Z | `[01-01, 01-20) A`, `[01-20, null) B`; reason = late-information |

Expected answers:

| Valid time | Known at | Answer |
|---|---|---|
| 02-01 | 01-31 | A |
| 02-01 | 02-11 | B |
| 01-15 | 02-11 | A |
| 01-20T00:00:00Z | 02-11 | B (the A segment's end is excluded) |
| any | 01-09 | `unknown/before-first-receipt` |
| 2025-12-31 | 02-11 | `unknown/uncovered-valid-time` |

"January 1" appears here only as a UTC instant. Turning a civil date into an instant is an adapter's job; see counterexample C2.

---

## 4. Question routes (Bundle → Layer → Finding → Question → Artifact → Allowed action) [P]

Proposed bundles:
- B1 `scope-and-binding`
- B2 `bitemporal-timeline`
- B3 `write-integrity`
- B4 `access-retention`
- B5 `adoption`

| # | Route | Question | Artifact | Allowed action | Unknown / missing behaviour |
|---|---|---|---|---|---|
| 1 | B2/valid-time/half-open-segment | What value was effective at V, per the latest record? | TimelineAnswer | Read | Gap → `unknown/uncovered-valid-time` |
| 2 | B2/record-time/host-receipt | What had this Dimension *recorded* by K? | Commit ≤ K | Read | K before first receipt → `unknown/before-first-receipt` |
| 3 | B2/correction/snapshot-supersession | Which commit replaced the belief held at K₁? | Commit chain | Read | None later → report head |
| 4 | B2/correction/correction-vs-domain-change | Was this commit labelled a correction or a domain change? | `reasonCode` | Read. The label is host-asserted, not verified. | Missing → reject the write (required field) |
| 5 | B2/record-time/source-time-metadata | When did the source say the event or observation happened? | `sourceMeta` | Read as source-asserted | Absent → "not provided", never inferred from receipt |
| 6 | B2/record-time/bootstrap-import | Was this history imported or first received here? | `origin` + import config | Read; the `source-knowledge` view needs explicit opt-in | K before the import receipt → `unknown/pre-local-receipt` |
| 7 | B1/scope-identity/scope-key | Is this the same fact scope as another system's? | `scopeKey` | Compare only. Cross-system identity equivalence is delegated to identity refs. | Unregistered → `unknown/scope-not-registered` |
| 8 | B1/scope-identity/single-valued | Can two values hold at once? | FactScope.cardinality | No; split scopes by context | Missing context key → `insufficient-context` |
| 9 | B1/schema-binding/schema-pin | Which exact schema bytes govern this segment? | SchemaPin | Read and resolve via the registry | Pin not registered → write rejected |
| 10 | B1/schema-binding/version-grammar | Are v1.2.0 and v1.3.0 compatible? | 022 compatibility-declaration ref | Read the declaration only | None declared → `compatibility-undeclared`, **never inferred from SemVer** |
| 11 | B1/lifecycle-binding/vocabulary-pin | Is `serving` a known code on axis `rollout`? | StateVocabularyPin | Membership check | Not a member → reject. A member ≠ legal transition. |
| 12 | B1/lifecycle-binding → 021 | Did the transition to `serving` legitimately occur? | EM-XCT-03 assertion ref | **Out of contract** → route to 021 or host | Return `delegated` |
| 13 | B3/idempotency/request-digest | Was this retry already applied? | Commit by key | Return the original result | Same key, different digest → `idempotency-conflict` + ConflictRecord |
| 14 | B3/concurrency/expected-head | Is my correction based on the current head? | Head seq | Commit if equal | Unequal → `head-conflict` + ConflictRecord |
| 15 | B3/authority-precondition/conflict-artifact | Why wasn't a competing claim applied? | ConflictRecord | Read (restricted) | None → no conflict recorded |
| 16 | B4/read-decision/query-time-auth | May this caller read the history as of K? | Host decision (now) | Read or deny | Decision absent → `denied` (fail closed) |
| 17 | B4/archive/write-freeze | Can this scope still be written? | FactScope.status | Archived → reads only | — |
| 18 | B4/erasure/tombstone | Why did this historic answer disappear? | ErasureRecord | Read | Returns `erased`, never the old value or `unknown` |
| 19 | B5/adapters/loss-declaration | What is lost exporting to a single-axis system? | Adapter manifest | Export with declared loss | No manifest → refuse the export |
| 20 | B5/migration/version-downgrade | Can a 0.1 reader consume a 0.2 ledger? | Ledger header | Refuse | — |

---

## 5. Invariants and negative tests [P]

### Invariants
| ID | Invariant |
|---|---|
| I1 | Commits are never modified or deleted. The only exception is erasure, which replaces segment payloads with a tombstone and keeps seq, instant, scopeKey, reasonCode and ErasureRecord ref. |
| I2 | `receiptSeq` strictly increases per ledger. `receiptInstant` is non-decreasing along seq. Both are host-assigned only. |
| I3 | For all K₁ < K₂, `answer(V, K₁)` computed after commit c₂ equals `answer(V, K₁)` computed before c₂ (the past knowledge view is stable), except for erased payloads. |
| I4 | Every snapshot is sorted, has no overlapping segments, has `from<to`, has at most one open segment and that segment is last. |
| I5 | `answer` never returns a value from a commit with seq > cutoff, and never returns `false` or "absent" for a gap or an empty snapshot. |
| I6 | Segment membership: `from ≤ V < to` (or `to=null`). |
| I7 | `(ledger, idempotencyKey)` maps to at most one requestDigest and at most one commit. |
| I8 | A commit is applied only if `expectedHeadSeq == head(scope)` at application time. |
| I9 | Every segment has a SchemaPin present in the registry snapshot at the time of the write. `schemaVersion`, `objectRevisionRef`, `stateAxes` and `reasonCode` are distinct fields and are never inferred from one another. |
| I10 | Every rejected write that reaches the authority, head or idempotency check leaves exactly one ConflictRecord and zero timeline changes. |
| I11 | `sourceMeta` never affects the ordering, the cutoff or the chosen segment. |
| I12 | Archive changes no existing commit and makes no answer unavailable. |

### Negative tests
| ID | Input | Expected |
|---|---|---|
| N1 | Correction commit seq 2 as in §3.5; query V=02-01, K=01-31 | A (history not rewritten) |
| N2 | Query V=01-20T00:00:00Z at K=02-11 | B, not A (end excluded) |
| N3 | Query K=2026-01-09 | `unknown/before-first-receipt`, not the current value |
| N4 | Retry the same key with the same bytes after head moved | Original result; no new commit |
| N5 | Same key, one payload byte changed | `idempotency-conflict`; ConflictRecord; no commit |
| N6 | Two writers, both `expectedHeadSeq=1` | First commits; second gets `head-conflict` with `observedHeadSeq=2` |
| N7 | Caller supplies a `receiptInstant` or `receiptSeq` field | `forged-record-time` rejection. **Not silently ignored.** |
| N8 | `from="2026-01-01T00:00:00.500Z"`, `"2026-01-01T02:00:00+02:00"`, `"2026-01-01"`, or `"2016-12-31T23:59:60Z"` | `unsupported-precision` / `offset-requires-adapter` / `date-requires-adapter` / `leap-second-requires-adapter`. Nothing truncated. |
| N9 | Segments `[01-01,01-21) A` + `[01-20,null) B` | `overlap` rejection |
| N10 | Segments `[01-01,01-10) A` + `[01-20,null) B`; query V=01-15 | Accepted; answer `unknown/uncovered-valid-time` |
| N11 | SchemaPin `schemaVersion="active"` (semver), or a digest mismatch with the registry, or a `+build` suffix | `invalid-schema-version` / `schema-digest-mismatch` / `build-metadata-forbidden` |
| N12 | Host read decision = deny, for a caller who *had* access in January | `denied`. Historic permissions are not replayed. |
| N13 | Write to an archived scope; then read history | `scope-archived` on the write; the read still returns A/B as before |
| N14 | Host clock produces a receiptInstant earlier than the head's | `clock-regression`; no clamping |
| N15 | A 0.1 reader opens a ledger header declaring 0.2, or an adapter exports to a system-time-only target without a loss manifest | `unsupported-contract-version` / `loss-undeclared`. No partial read. |
| N16 | State code `serving` is in the vocabulary, but the host has no transition evidence | Write accepted with `vocabularyMember=true`. No `transitionValid` field exists to set. |
| N17 | Erase seq 1 payload; query K=01-31 | `erased`, never A and never `unknown` |

---

## 6. Synthetic profiles

**Startup (no ERP) [P]**
- One ledger, run by a lightweight service or embedded library. Sources are a SaaS HR tool and spreadsheets, brought in through an import adapter.
- Import adapter duties:
  - Convert civil dates to UTC using one declared company zone and a pinned tz release.
  - Record `sourceMeta.adapterRef`.
  - Mark imported rows `origin=imported`.
- Loss limits: no pre-import knowledge. Spreadsheet edits made before import collapse into one receipt.
- No mandatory ERP, registry service or IAM. SchemaPins can point at files in the repo, hashed.

**International matrix group [P]**
- Multiple masters: `context` includes `legalEntity` and `masterSystem`, so each master writes its **own scope**.
- A "group view" is a derived reconciliation owned by EM-XCT-02 authority rules, never a write that merges scopes.
- Data residency leads to separate ledgers. `knownAtInstant` across ledgers compares host clocks that are not synchronised (009 excludes synchronisation), so cross-ledger cutoffs should be labelled *approximate*, and the answer must list each ledger's seq.
- Local "effective from 1 April" dates need per-jurisdiction adapters that pin a tz release. Changing the adapter release changes the instants, which should be a new commit with `reasonCode=error-correction`, not a silent recomputation.
- Loss limits: a matrix manager relation with two values at once is not single-valued. Split it by context (`axis=functional` / `axis=legal`), or reject it.

**AI release organisation [P]** — three different scopes, never one field:

| Scope | Content | Owner |
|---|---|---|
| (1) `predicate=model-artifact` | `objectRevisionRef` (opaque, 022) + artifact digest + SchemaPin of the model card format | Artifact registry |
| (2) `predicate=deployment-state`, `context={environment, region}` | `stateAxes{rollout: staged\|canary\|serving\|withdrawn}` pinned to a host vocabulary, plus `objectRevisionRef` of the deployed artifact | Deployment host |
| (3) Records about states | Eval results, approvals and incident reports as EM-XCT-03 assertions, referenced by `validationAttestationRef` | Evidence owners |

Two kinds of later commit look alike but must be kept apart:
- A rollback is a **domain change**: a new segment from the rollback instant.
- Discovering that the wrong model served from time X is a **late-information correction**: it replaces the past segment.

Loss limits: canary traffic percentages or concurrent serving of two models make the scope multi-valued. Model them per variant scope.

**Adapters (none silently executable) [P]**

| Adapter | Behaviour |
|---|---|
| SQL Server temporal import | System time becomes `sourceMeta.sourceRecordedAt` (source-asserted). Valid time is absent, so the adapter needs a declared rule. Local receipt = import time. |
| XTDB import | `_system_from` is source-asserted, because XTDB lets transactions set system time. Microsecond precision is rejected, or rounded only under an explicitly declared rule with the loss recorded. |
| SCD2 export | Loses the knowledge axis. Needs a loss manifest. |

Each adapter is a separate signed artifact referenced by digest. The contract never auto-invokes one.

---

## 7. Counterexamples, holds and acceptance criteria

### Strongest counterexamples to the tentative design [I]
- **C1. "What the Dimension knew" ≠ "what it recorded".**
  - HR may have learned of Team B on Feb 3 by email and recorded it on Feb 10. The contract can only answer *recorded knowledge*.
  - Proposal: name the axis `recordedAt`/`knownAtRecord` and never call it "knowledge". Awareness time goes in `sourceMeta.observedAt`, source-asserted.
- **C2. Civil-date validity.** "Effective January 1" in Tokyo is not `2026-01-01T00:00:00Z`. UTC-second forces an adapter, and adapter or tz-release drift silently shifts instants unless pinned. This is the largest real-world defect risk.
- **C3. Full snapshots serialise writes.** Two corrections to disjoint periods conflict on the head, and bulk payroll back-dating causes contention. Accepted for 0.1; a delta profile is deferred.
- **C4. Erasure breaks I3.** "Every previous snapshot remains queryable" cannot survive erasure law. The `erased` status must be a first-class answer, and the contract must not promise permanent retention.
- **C5. Query-time authorisation cannot reproduce "what the approver saw".** That needs access-audit logging, which WM-XCT-022 excludes as operator audit [O]. Declared out of scope.
- **C6. SchemaPin integrity ≠ payload validity.** A host can pin the right schema to a payload that does not conform. Only an attestation (a claim) exists, not proof.
- **C7. Per-ledger seq is a single-writer assumption.** Multi-region active-active ledgers would need consensus, which is excluded. So: one sequencer per ledger, or separate ledgers.
- **C8. A single `reasonCode` per commit is coarse.** A snapshot can mix a correction to January with a domain change in March. Either forbid mixed intent (one reason per commit) or add optional per-segment reasons. I recommend forbidding it in 0.1.
- **C9. `opaque` version schemes can still accept `"active"`** if the host registers it. Only registry governance prevents that.

### Unresolved holds (kept, not fixed)
- **Parent holds carried over [S]:**
  - 022: bitemporal support partial, no normative SQL:2011 source.
  - 021: all edition checks and profile validations.
  - 009: live editions, jurisdiction rules, uncertain dates.
- **This memo's gaps:**
  - All three parent specs were only partly retrieved, and no SHA-256 pin was verified.
  - enterprise-identity returned 404.
  - EM-XCT-02 and EM-XCT-03 spec bodies were not read, so I did not verify that ConflictRecord and `authorityDecisionRef` fit their exported types.
  - The five-facet definition was unavailable.
  - The canonicalisation profile for `scopeKey` and `requestDigest` needs a decision; RFC 8785 is cited by 022 [S], but I did not read it.
  - Whether KurrentDB detects same-EventId-different-bytes is unverified.

### Implementation acceptance criteria (for the future frozen audit)
1. All of N1–N17 pass, using fixtures with byte-exact expected answer JSON.
2. A property test: random append sequences keep I1–I8 true, and I3 is checked against saved answers from before each append.
3. Timestamp parsing is table-driven. It has zero lossy conversions and no code path that truncates or clamps.
4. The write API schema has no caller-settable receipt field (N7 must fail closed).
5. The reference library runs with an empty runtime import list, and passes after removing network access.
6. The package states: "Reference callable is not a security boundary; host decisions are trusted inputs."
7. `maxSegments` and payload byte limits are enforced before digesting, with a stated upper bound on commit size.
8. The loss manifest is mandatory for every adapter, and export without one fails.
9. The spec lists semantic refs to 009, 021 and 022 by exact published ID and version, marked `conceptual`, with no readiness inheritance.

### Research limitations
- I read summaries produced by a fetch tool, not raw bytes. Quotations and section numbers can be wrong, and all three Vercy parent specs were cut off before the end.
- No paywalled ISO or SQL text was read. Claims labelled [R] are from memory.
- I did not execute or audit any code, did not check the pins, and did not consult any workspace material.
- The profiles are synthetic and not validated against real organisations.
- This memo does not authorise publication.

Sources:
- [WM-XCT-009 spec.yaml](https://ver.cy/models/wm-xct-009-time-calendar/spec.yaml)
- [WM-XCT-021 spec.yaml](https://ver.cy/models/wm-xct-021-lifecycle-status/spec.yaml), [landing page](https://ver.cy/models/wm-xct-021-lifecycle-status/)
- [WM-XCT-022 spec.yaml](https://ver.cy/models/wm-xct-022-version-change-history/spec.yaml), [landing page](https://ver.cy/models/wm-xct-022-version-change-history/)
- [Enterprise Assertion Provenance](https://ver.cy/models/enterprise-assertion-provenance/)
- [Enterprise Fact Authority](https://ver.cy/models/enterprise-fact-authority/)
- [Enterprise Identity (404)](https://ver.cy/models/enterprise-identity/)
- [W3C OWL-Time (CR Draft 2022)](https://www.w3.org/TR/owl-time/)
- [W3C SCXML (REC 2015)](https://www.w3.org/TR/scxml/)
- [W3C PROV-DM (REC 2013)](https://www.w3.org/TR/prov-dm/)
- [SemVer 2.0.0](https://semver.org/spec/v2.0.0.html)
- [XTDB — Time in XTDB](https://docs.xtdb.com/about/time-in-xtdb.html)
- [XTDB — SQL transactions](https://docs.xtdb.com/reference/main/sql/txs.html)
- [Microsoft Learn — Temporal Tables](https://learn.microsoft.com/en-us/sql/relational-databases/tables/temporal-tables)
- [RFC 9557](https://www.rfc-editor.org/rfc/rfc9557.html)
- [Fowler — Bitemporal History](https://martinfowler.com/articles/bitemporal-history.html)
- [Kurrent Docs — Appending events](https://docs.kurrent.io/clients/tcp/dotnet/21.2/appending)
- [Kurrent Discuss — Idempotency and expectedVersion](https://discuss.kurrent.io/t/indempotency-and-expectedversion/160)
