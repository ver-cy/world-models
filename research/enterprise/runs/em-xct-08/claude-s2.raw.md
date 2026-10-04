The full S2 text is visible, from "# EM-XCT-08 S2" through "END S2 BRIEF". I used no tools, and I treat the decisions as supplied text, not as verified behaviour.

**Verdict:** This is a coherent research boundary, subject to implementation review. None of the points below is a blocker.

## How my S1 blockers are closed

| S1 blocker | Closed by | Status |
|---|---|---|
| B1: a recycled key inherits an existing mapping | Decision 1. "Unknown" cannot be joined to a lineage, active mappings need a non-null generation plus evidence, and the anchors carry both generations. | Closed |
| B2: mapping pins inside the replay digest | Decision 2. The client digest excludes computed pins, the attempt ID, the expected head and the fence. The receipt stores the original pins, and a retry never recomputes them. | Closed |
| B3: split-brain archive resume | Decision 5. Import is read-only, there is no append API, and fresh acquisition needs a new local register, epoch and baseline. | Closed |
| B4: acknowledgement as an existence oracle | Decision 4. Acknowledgements are bound to the principal who made the original commit, and a colliding writer gets a generic response. | Closed, with the residual limit noted below |
| B5: reactivating a disputed mapping | Decisions 3 and 1. Uniqueness is checked on every transition into active. | Closed |

## Limits the package text should state

1. **Order of checks at admission.** Decision 2 implies this order but does not state it:
   1. authenticate and authorize the operation;
   2. look up the stable batch key;
   3. if the retry is identical and comes from the same principal, return the stored result;
   4. only then evaluate the expected head, fence and expected mapping revision, and commit.
   
   If preconditions were checked before the lookup, an identical retry after later progress would fail with "stale head", and acceptance case D would break. Stating the order makes the retry semantics testable.

2. **One-bit existence signal.** Keeping batch keys scope/epoch-wide is the right trade-off, because it prevents a second writer recommitting the same acquisition. The consequence is that any currently authorized writer on the scope can learn that a key is already taken, since it gets "not-accepted" where a fresh key would succeed. It learns nothing else: no receipt and no protected fields. The disclosure section should state this residual rather than promise indistinguishability.

3. **Recovery needs read permission.** A replacement worker running under a different principal cannot find out whether a lost commit landed without read permission. The host runbook should make read permission, or an operator lookup, the recovery path. The alternative is a worker retrying blindly against "not-accepted" responses.

4. **What the content digest covers.** The digest covers token evidence and record descriptors as submitted. A retry must therefore resubmit byte-identical references. If a protected locator is re-wrapped or re-issued, the retry becomes a conflict rather than a replay. The digest proves consistency of the references, not that the external bytes survived. This is consistent with decision 7 and should be written next to the digest definition.

5. **Cost of a source-instance generation change.** Anchoring mappings to the source-instance generation means a restore or namespace replacement leaves every existing mapping non-operative for new occurrences until a steward re-establishes them. That is correct, but the migration notes and fixture C should show the steward workload, not just the refusal.

6. **Reclassification state.** After a target is reclassified, the existing mapping stays active for uniqueness purposes, but new pinning against it returns insufficient-context. Exposing an explicit state for this, such as `active-pin-suspended`, would help. Without one, read views may show an "active" mapping that silently yields no pins.

7. **Unknown-generation occurrences.** These can gain aboutness only through a future, separately identified reprocessing activity. The A–O dispositions should mark this as deferred, not as "tested".

This is research acceptance only. It does not approve code, test results or publication.