# EM-XCT-08 S1 reconciliation response

I used no tools in this pass. I treat the S1 excerpts as supplied evidence, and I verified none of them. No code exists, and I claim no tests.

## 1. Accept/revise per decision

| # | Decision | Verdict | Concrete condition or objection |
|---|---|---|---|
| 1 | Companion boundary; aboutness mapping; local QualifiedSourceKey; kind and pair-policy admission | **Accept with limits** | The mapping must record the target-catalogue revision it checked `expectedTargetKind` against. If the target is later reclassified, a candidate is raised; the mapping is not silently invalidated and not silently kept as active truth. `sourceObjectKind` must come from the scope's connector interpretation, not from the operator per call. |
| 2 | Three distinct generations | **Accept, revise one gap** | Unknown RecordGeneration needs an operational rule, not just a label. See §3 and blocker B1. |
| 3 | Mapping identity; one active per (lineage, purpose) across kinds and revisions | **Revise** | (a) The uniqueness predicate must hold on every transition into `active`, including `disputed → active` (B5). (b) An occurrence must pin (mappingId, stateRevision), not just mappingId. (c) "In one governed transaction where applicable" must become: the new mapping cannot become active while the old one is active. Retract-then-activate may leave a visible zero-active interval, but never a two-active one. |
| 4 | Acquisition scope separate from mapping application; replay identity includes pins | **Revise** | The decision does not say who produces the pins. If the register computes them, they cannot be part of the operator-compared body (B2). |
| 5 | SnapshotRound coverage; per-round token is evidence only | **Accept with limits** | This corrects my original wording. Rounds in different epochs of an unchanged scope may be compared. Explicit removal or deletion occurrences between the rounds take precedence over absence. Rename the absence result to `not-observed-in-comparable-rounds`, because visibility loss is indistinguishable from absence (C6). |
| 6 | Checkpoint equals receipt-linked edge; one local transaction; `received = accepted + quarantined`; accept-loss refused | **Accept** | Also state that a non-terminal page batch advances progress without implying round completeness. Round completeness belongs only to SnapshotRound. |
| 7 | Head CAS separate from fence revision; admin fence advance; closed epoch allows lookup only | **Accept with limits** | The fence check and head CAS must run in the same BEGIN IMMEDIATE transaction. Fence advances need their own audited record. A changed-body replay into a closed epoch must not append to that epoch (C8). |
| 8 | Authorization first; generic denial; minimal own-operation ack | **Revise** | "Own" must be bound to the authenticated writer principal of the original commit. Otherwise the acknowledgement becomes an existence oracle between co-authorized writers (B4). |
| 9 | Occurrence identity is (committed batch, input ordinal); correctionOf; separate clocks | **Accept with limits** | `correctionOf` must record who asserted it: source-asserted or steward-asserted. An operator cannot assert a source correction. |
| 10 | Opaque protected refs; no HMAC service; restricted exports; validation is not resumption | **Revise** | "Refuse resume until it independently establishes … latest head" is unsatisfiable for a copied archive. The importing host cannot know whether the origin committed later (B3). |
| 11 | Minimal reference; no persistent attempt ledger; three fixtures; A–O dispositions | **Accept with limits** | The package must state the retained terminal attempts precisely: the committing attemptId on each receipt, and the attemptId on each canonical conflict. Failed-before-commit attempts are host telemetry only. "Tested" must not appear in any disposition until checks exist. Until then, use `specified`/`refused`/`deferred`. |

## 2. Scope versus round comparability

After decision 5, a remaining contradiction is gone. My original "every component digest equal" was only safe because my SyncScope excluded the per-round token. S1 now makes that explicit, and I accept it.

Three residual issues remain:

1. **Epoch is not a comparability component.** A 410 reset under an unchanged scope keeps round comparability. A SourceInstanceGeneration change alters the scope and breaks comparability. The package should state this directly, so implementers do not add epoch to the comparison key "for safety". Adding it would make every post-reset round incomparable with every pre-reset round forever.
2. **Round ordering.** An absence candidate needs the later round to have been admitted later by local sequence, and its declared consistency point must not be claimed earlier than the first round's. Consistency evidence should carry a source-declared "not earlier than" relation when the source provides one. When it does not, the result is `insufficient-context`.
3. **Principal visibility is declared, not observed.** The scope fingerprint fixes the principal, but per-object permission can change without the principal changing. Two complete comparable rounds can therefore hide a revoked object. The candidate must never be labelled deletion. That is already required, and the rename in row 5 makes it unambiguous.

## 3. Unknown key generation

Decision 2 names unknown continuity but does not say what mapping application does with it. The key danger is that a lineage anchored at (key, generation-unknown) silently inherits the active mapping when the key is recycled. That is case C.

Proposed rule:

- Each scheme in the scope's trusted interpretation declares a `recyclePolicy`, one of `never-reused` (source-guaranteed), `may-reuse` or `unknown`.
- A mapping anchors a lineage that includes a generation value or `unknown`.
- A pin is applied only if the occurrence's generation equals the anchored generation, or if the generation is unknown and the scheme is `never-reused`.
- Otherwise the occurrence is admitted with status `continuity-unknown`. It is unmapped for propagation, but still committed and counted.
- If generation evidence later appears and splits a lineage, earlier pins are not rewritten. A `possible-continuation` or split candidate goes to the steward.

## 4. Mapping correction across history

Accept, with these specifics:

- Pins are (mappingId, stateRevision). A later retraction of the same mappingId leaves old pins historically true: "at admission, this claim was active".
- A read view may annotate them as "claim since retracted", but must never re-point them.
- A new mapping whose valid time is retroactive does not repin old occurrences. Only a separately identified future reprocessing activity can produce new derived rows, and those rows carry their own identity.
- `knownAt` queries return the pin as admitted, plus the correction chain known at `knownAt`.

## 5. Acknowledgement and disclosure

The order is: authenticate, then authorize for the requested operation, then look up.

- **Writer with current write grant on an open epoch, same principal as the original committer, identical body:** receives the minimal own-operation acknowledgement (receipt id, commit status, no register contents).
- **Different co-authorized principal presenting an existing batchKey:** receives the same generic `not-accepted` response used for any non-committable request. The collision is recorded as a restricted canonical conflict.
- **Idempotency namespace:** should include the writer principal (a service identity, not a process instance), so that legitimate failover retries still deduplicate.
- **Historical receipt reads:** require current read permission on the scope, independent of write permission.
- **Denials of unauthenticated or revoked callers:** go to host telemetry only, with one response shape.

## 6. Replay after epoch close

| Replay into a closed epoch | Result | Record |
|---|---|---|
| Identical body, previously committed, caller has current read or own-operation permission | Original receipt, no effect | None |
| Identical body, never committed | `epoch-closed` | Host telemetry |
| Changed body under a committed key | Generic refusal | Restricted conflict in a scope-level diagnostic register, not appended to the closed epoch |

A closed epoch's history must stay immutable, including conflicts. Otherwise the export of a closed epoch changes after close.

## 7. Smallest safe archive import and resume boundary

Import produces a read-only historical register:

- Every imported epoch is marked `foreign-closed`, whatever its state on the origin host.
- The new host may validate structure, digests-as-declared and conservation.
- It may never append to an imported epoch in 0.1.0.
- Resumption means opening a new local epoch in the same acquisition scope, bootstrapped by a fresh complete SnapshotRound.
- Continuing an imported epoch from its imported token requires a separately defined origin-host handover. The origin would close the epoch with a transfer anchor attested outside the archive. That handover is deferred, and 0.1.0 refuses it.

This makes "validation is not resumption" enforceable rather than aspirational.

## 8. Original recommendations these amendments replace

1. **Record key representation.** My proposal to reuse QualifiedIdentifierAssignment as the executable source-record key is replaced by the local QualifiedSourceKey. My increment-3 mapping↔IdentityAssertion adapter is withdrawn; a semantic crosswalk at most remains.
2. **Mapping uniqueness.** Uniqueness per (lineage, purpose, kind) becomes per (lineage, purpose).
3. **ExtractionAttempt.** As an exported canonical type it becomes host telemetry plus attemptIds on receipts and conflicts.
4. **Loss policy.** The `accept-loss` policy option (Q11, INV 6) is refused in 0.1.0.
5. **Digests.** Keyed HMAC digests, the per-host re-keying route (Q15, route 18) and the "re-key under authority" import path are replaced by opaque protected references with no confidentiality claim.
6. **Fencing.** My "lease high-water fence token" becomes an admin-advanced, epoch-local fence revision with no clocks.
7. **Snapshot comparison.** "Complete snapshots comparable only if every digest equal" becomes SnapshotRound identity plus acquisition-scope equality, with round tokens as evidence only.
8. **Candidate naming.** `absent-in-comparable-snapshot` is renamed (row 5).
9. **Mapping-only changes.** A "new mapping-application generation" becomes per-occurrence pins plus separately identified reprocessing.

My restore, 410 and PK-change rules are retained and now aligned with decision 2.

## 9. Counterexamples

**B1 (blocking): recycled key inherits mapping.** A dataset key "d-7" has scheme `may-reuse` and no generation evidence. The old record maps to Dataset S1. The source deletes it and reissues "d-7" for an unrelated dataset. Under S1 as written, the lineage (d-7, unknown) keeps its active mapping, and new occurrences are pinned to S1. Case C fails. The §3 rule fixes this.

**B2 (blocking): pins inside the replay digest.** Batch K commits with pins to mapping M rev 3, and the response is lost. A steward then retracts M. If the register recomputes pins on retry and includes them in the compared body, the identical source retry becomes a false payload conflict and D fails. If it excludes them from the comparison, the returned receipt must carry the original pins. Required fix: the compared digest covers only operator-supplied content, and pins are receipt data. If operators ever supply expected pins, those are a precondition, like the expected head, not body.

**B3 (blocking): split-brain archive resume.** Host A exports while epoch E is open. Host B imports, "establishes" token access and the head it sees, and commits E+1. Host A, still running, also commits a successor to the same head. Two databases now hold divergent successors of one predecessor, and neither CAS can detect it. The §7 rule fixes this.

**B4 (blocking): acknowledgement as existence oracle.** Writers W1 and W2 are both authorized on scope S, and W2 lacks read permission. W2 probes batchKey values and receives "already committed" acknowledgements for W1's batches. The response leaks W1's activity cadence and page structure. The §5 principal binding fixes this.

**B5 (blocking unless specified): dispute reactivation.** Mapping M1 (lineage L, purpose P) goes active → disputed. M2 for (L, P) activates, which is permitted because M1 is not active. The dispute on M1 is then resolved as disputed → active, and two mappings are active. The uniqueness check must run on every transition into active.

**C6 (non-blocking): visibility revocation looks like absence.** An object is hidden from the principal between two complete comparable rounds. The candidate is correct only if it is named and treated as not-observed, never as deleted.

**C7 (non-blocking): target reclassification.** A Project is reclassified in its own register after the mapping activated. Admission-time kind equality said nothing about later kinds, so the mapping must record the catalogue revision it checked.

**C8 (non-blocking): conflict recorded into a closed epoch.** A changed-body replay after close appends a conflict row and alters a closed epoch's export digest. The conflict should be recorded outside the epoch.

B1–B5 are blocking. With the fixes stated in §§3–7, I would expect the result to be a coherent research boundary subject to implementation review, but this S1 text as written is not yet that.