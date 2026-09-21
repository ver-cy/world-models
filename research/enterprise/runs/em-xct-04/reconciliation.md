# EM-XCT-04 boundary reconciliation

Decision by Codex: implement an original **Enterprise Temporal History** companion, not a new universal WM type and not an executable subtype of WM-XCT-009/021/022. The three parents were fetched completely, recursively parsed, preserved and byte-compared with their live URLs. Boundary, composition, holds and complete structure inventory were inspected; this is not ratification of every historical citation or validator. Exact pins and retained holds are in crosswalk.json. Research used public material and synthetic requirements only.

Claude and Grok independently studied the same frozen public brief. Claude used its safe CLI with only WebSearch/WebFetch; Grok used the owner's browser with Heavy visibly selected. Both returned substantive research with retrieval limitations. Their original text and manifests are retained separately from this synthesis. Both providers read summarized/truncated parent excerpts and did not recompute source digests. Their agreement does not erase those limits.

## Decisions and disagreements

| Issue | Decision and reason |
|---|---|
| Existing temporal/lifecycle/revision models | Semantic references only; broad concepts overlap, but no verified executable instance contract is inherited |
| Proposed name | Neutral `enterprise-temporal-history`; the providers suggested different slugs without a semantic disagreement |
| Full snapshots versus event-sourced deltas | Bounded full snapshots support direct inspection and historical correction. Delta reconstruction, domain event execution and high-volume engines are deferred |
| Fact versus record versus schema versus state | Independent references/fields; the host domain fact remains external. Recorded assertion is not truth or human awareness |
| Same-second receipts | Non-decreasing UTC instants plus contiguous host sequence per timeline; exact sequence needed to keep historical content stable within one second |
| Scope hash versus opaque scope identity | Opaque governed timeline ID and explicit Dimension/subject/predicate/context. Each commit additionally hashes the immutable header; hash consistency is not identity proof or authentication |
| Optional schema pin (Grok) versus mandatory (Claude) | Mandatory exact schema tuple for every segment. Narrow numeric triplet grammar avoids treating `active` as version; no compatibility or payload conformance inference |
| Opaque payload / state vocabulary | Exact external value pin, optional one-axis state reference, current vocabulary membership for new uses. No schema compiler or statechart engine |
| Five whole-object facets | Claude substituted a different taxonomy and disclosed the gap. Rejected that substitution. Canonical identity-class, direct-properties, recognition-observation, capabilities-behaviour-actions, context-evidence were applied individually to six exported types. Grok's final study uses these for several types; synthesis completes all six |
| Rejected writes in the successful receipt stream (Grok) | Rejected. A failure does not create a successful fact snapshot. The host must keep a separate restricted conflict audit; no durable store is claimed here |
| Erasure exception in append-only history (Claude) | Deferred. In-place redaction would invalidate the exact prefix contract and needs a separately designed retention/tombstone migration. Archive preserves retained bytes and does not promise permanent retention |
| Backdated offline bootstrap | Rejected for this release. Local first receipt is the actual host admission time; sourceRecordedAt is metadata. Existing trusted archives can be checked for structural consistency only |
| Empty snapshots | Accepted as explicit removal of current assertions, returning insufficient context; the reason must explain the change. No implicit negative fact or supported withdrawal-vs-never-asserted distinction |
| Schema retirement and archive | Initial Claude audit reproduced a defect. Fixed: exact retained segments need no renewed pin acceptance; new or resegmented uses do. Archive keeps the exact previous snapshot |
| Cross-Dimension transplantation | Initial Claude audit reproduced a defect. Fixed: commit scopeDigest plus explicit expected native Dimension and envelope checks. A recomputed malicious history is still outside the trusted-host authenticity claim |
| Rebinding payload interpretation | Allowed explicitly in a new complete snapshot under a currently accepted schema/profile and attributed reason; old snapshots retain old interpretations. This is not automatic migration or validation |
| Capacity and native identity | Archive can hit the same finite limits; host freeze/rollover planning required. Immediate predecessor checks do not prove global native fact-ID uniqueness |
| Grok closed-closed example wording | One row reverses the effect verbally; its invariant and other examples require end exclusion. The implementation and boundary tests follow half-open exclusion |
| Source comparisons | Adopt only the limited claims recorded in source-verification.json. A Microsoft field named ValidFrom in SYSTEM_TIME is not automatically business-valid time. OWL-Time latest read is a CR draft. No SQL/ISO conformance |
| Incorrect identity landing URL in shared brief | Both correctly reported 404. The existing identity profile lives under WM-XCT-036; there is no runtime identity dependency in this companion. Original brief/404 evidence stays unchanged |

## Candidate dispositions

TemporalValidity becomes the narrow ValidSegment value. Revision splits into local linear TimelineCommit identity and an opaque external artifact revision. LifecycleTransition remains a host-domain/WM-XCT-021 concern; a StateReference is only a declaration. SchemaBinding becomes an immutable accepted value tuple. Timeline and TimelineAnswer provide an explicit aggregate and derived view, without creating additional universal models.

## Review scope and continuation

Claude's first frozen no-tools audit accepted with limits and identified the concrete issues above; its original response remains available. Repairs were reproduced and separately regression tested, then sent to a second frozen no-tools audit. That pass found a host/native clock claim mismatch, forward-clock recovery disclosure gap, asymmetric predecessor checks and absent direct native unit tests. These were corrected, 20 direct cases were added (86 total), and a third materially revised candidate received a separate audit. The source-host timeline axis is now expressly distinct from later native storage; validation cannot authenticate historic receipts. External clock-skew guards and governed recovery with continuity-loss disclosure are required. Grok's independent **research is complete**, but its separate code-audit prompt could not be submitted after repeated browser navigation/focus timeouts and a lost debugger connection. That is an unavailable audit, never an accepting verdict. The explicit Enterprise draft exception permits a visibly limited usable draft; the missing audit remains a recovery item and the contour remains unfinished.

No provider executes publication, grants authority, verifies real-company applicability or certifies the host. Exact audit inputs, actual verdicts and executed reports have different roles and are not interchangeable. A later Grok review must target the exact published bytes; any required implementation change needs a new immutable release.
