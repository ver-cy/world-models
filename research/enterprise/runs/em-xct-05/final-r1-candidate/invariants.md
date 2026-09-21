## Sixteen semantic invariants

1. Each embedded member names exactly one source object; package membership can span objects but a projection cannot silently do so.
2. Qualified ID, record revision, source/schema revision, lifecycle/applicability and digest remain distinct.
3. All local reference occurrences of an ID agree on revision/digest; the reference cannot carry two purported current versions of that ID in one record.
4. No undeclared source value or nested/wildcard field is accepted by the metadata-only grammar.
5. A missing classification binding or evidence set cannot become an empty/public/clear default.
6. A review pins exactly the proposal identity/revision/digest; membership, shape, audience or any bound context change invalidates that match.
7. A current snapshot pins the proposal itself and independently declares all current member/context values.
8. The complete supplied review set equals the active pin set; duplicate or competing active revisions are invalid.
9. Active and withdrawn sets are disjoint; an active successor cannot leave its superseded target active.
10. Review assessment does not predate proposal capture; applicability uses `[validFrom, validTo)` and future capture is stale.
11. Current author/reviewer catalogs and authority pin are applied; segregation is explicit and actor-alias identity remains a host duty.
12. Conflicting eligible verdicts cannot silently select a winner. Excluded verdicts retain their pin, result and reason in restricted diagnostics.
13. Every returned report identifies its proposal, snapshot digest, evaluation time and counted/ignored records, and explicitly conveys no serving authorization.
14. Same stored identity/revision cannot be repointed; repeat import is idempotent and a failed merge leaves the caller's store unchanged.
15. Local review/proposal and supersession links resolve by exact pin/type, preserve proposal identity and nondecreasing assessment time, and do not cycle.
16. Pin equality, a human clearance and any custody-context reference establish no source truth, inference guarantee, current grant, legal conclusion, completed delivery or destruction.

Invariants 1–15 combine local checks with clearly named host attestations; invariant 16 is a semantic boundary and is not a proof produced by unit tests. The final 24 question routes are in spec.json; each names local checks versus host/deferred responsibility.

