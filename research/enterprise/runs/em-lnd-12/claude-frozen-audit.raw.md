## Verdict

**ACCEPT WITH LIMITS** — the held PROFILE is coherent; completion must close five named gaps before any publication authority.

## Critical findings

1. **Impact-result mastership is unassigned.** Constraint 14 splits boundary/membership/projection (039) from edge semantics (037) but never names who masters the *traversal result*. WM-XCT-037's own contradiction — traversal-forbidding scope versus traversal-performing functions — lands exactly here. Without an explicit assignment, two hosts can claim or disclaim the same impact set.
2. **`WM-SFT-009` appears in the Claude study (deployment occurrences) but is not in `bases`.** Unregistered identifier inside a `newRuntimeId=false` packet. Either drop the reference or register the base; do not let mastership route to an unlisted model.
3. **Common-mode reporting is a cross-tenant disclosure channel.** Shared-rack, shared-site and shared-control-plane findings, and any concentration/SPOF measure, reveal co-tenancy. Constraint 19's per-hop default-deny covers traversal but not aggregate counts; no fixture tests it.
4. **`exposed-unconfirmed` risks being read as impact.** Fixtures `stale-observed-flow` and the studies both emit it; nothing forbids it from entering impact sets, counts or exhaustiveness claims.
5. **No named staleness horizon or confidence scale.** "Stale beyond horizon", "41 days", "confidence above threshold" are all unbound, so confirmation is currently judgement, not semantics.
6. **Promotion grazes disjointness.** Constraint 5 permits inference to "become an asserted fact with accountable authority" while boundary item 4 requires disjoint populations.

## Required holds

- Assign impact-result mastership in writing: 039 hosts and masters projections and their completeness statements; 037 supplies licence and edge semantics only. Resolve the 037 traversal contradiction before either base publishes.
- Remove or register `WM-SFT-009`; re-verify every mastership route against the declared `bases`.
- Bind common-mode, correlation, concentration and SPOF output to the caller's tenant projection; suppress cross-tenant peers and aggregates absent an explicit 039 grant. Add the missing fixture.
- State that `exposed-unconfirmed` and incompleteness warnings are non-impact labels, excluded from impact sets, counts and any exhaustive claim.
- Fix staleness horizon, confidence scale and confirmation threshold in 037, projected read-only by 039.
- Require promotion to mint a **new** edge in the target population with fresh authority and evidence; relabelling in place is forbidden.
- Carry forward the existing holds: both bases `publishableCanonical: false`, single-provider; WM-ACT-004/SFT-002/SFT-010/SFT-016 unspecified; relation rows, schemas, adapters, crosswalks pending. Add fixtures for pending mastership blocking mutation and for tombstoned identifiers.

## Scenario result

S is a resource/control-plane node, not a Service. Only the subset of the three confirmed edges carrying a current licence for the requested polarity yields **partial exposure candidates** — no dependent failure asserted, no SLO breach evaluated. The stale observed edge stays historical and non-impact. The co-location edge raises a tenant-scoped common-mode watch, no propagation. Topology incomplete ⇒ blast radius open; "only three", "exhaustive" and "unaffected" forbidden; inferred fill-in forbidden. Incidents, observations and SLOs remain external.

## Identifier decision

No new identifier. `newRuntimeId=false` upheld. ServiceLandscape is a 039-internal named projection; ServiceDependencyGraph is rejected. View keys are 039-internal and externally non-resolvable; a view name confers no privilege. No publication authority granted here.
