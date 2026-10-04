# Frozen semantic audit — EM-FIN-01 (static, packet-only)

## Verdict

**ACCEPT WITH LIMITS.** The three-part disposition holds: WM-ECO-012 covers the budget aggregate, Responsibility Centre proves independent identity and lifecycle, and Funding Allocation correctly stays inside WM-ECO-012 (extraction would split conservation from the envelope that bounds it). The limits are specification defects below, all of which must clear at candidateRevision 3 before identifier allocation — none of them reopens the disposition.

## Critical findings

1. **Bitemporal claim exceeds the structure.** Invariant 2 requires world-effective *and* record-time evidence, but only `CentreVersion` carries `recordedAt`/`contentDigest`. `AliasBinding`, `HierarchyMembership` and `SuccessionRule` are world-time only, so a corrected alias cannot be distinguished from a genuine rebinding, and as-of resolution of a re-used ERP code is undecidable. Blocking.
2. **Carry-in is unconserved.** The profile allows `− carry-in` on the left of the ceiling and `+ carry-in` in the residual identity, but no constraint binds carry-in to the immediately prior period's reconciled residual *of the same source*. Carry-in is therefore an unbounded availability inlet — the same defect the `successor-double-availability` fixture rejects, displaced one period.
3. **Quantity terms collide.** The profile bounds allocation by "authorized amount"; local evidence and the `double-funding` fixture say "released". In WM-ECO-012 ceiling, authorization, release and allotment are distinct stages. Conservation must name one stage.
4. **Version coverage is not gapless.** Non-overlap is asserted; continuity is not. Invariant 3 then has no referent for a posting dated in a gap, before the first `effectiveFrom`, or after closure.
5. **Hierarchy cascade.** `HierarchyMembership` keys on parent and child *version* refs while a hierarchy change mints a successor version — a parent reparenting propagates new versions downward, contradicting the "no version from organizational movement alone" rule. Membership should key on `centreId` with dated intervals.
6. **`organization-move-only` is untestable.** `owns` claims organizational-unit associations, but no object holds them; the fixture's expectation cannot be evaluated against the given shape.
7. **Posting gate is doubly defined.** `status: restricted` and `postingEligibilityWindow` both govern admissibility with no stated precedence. The family lifecycle also omits `superseded`, which `identityTest.independentLifecycle` lists.
8. **Unspecified granularity and closure.** `SuccessionRule.predecessorRefs`/`successorRefs` do not state centre-vs-version scope, and weight-based splits carry no sum-to-unity rule. Separately, no rule distinguishes a rejected rewrite from a legitimate reversal-and-repost correction.

## Required holds

All seven declared holds stand. Add: (a) the cross-budget draw register has no declared master in any cited model — mastership must be resolved before the cross-budget constraint is enforceable; (b) `bases` omits WM-XCT-032 although the profile pins its quantization and residual rules; (c) the profile references a referent with no identifier, so profile and centre promote or stall together; (d) fixtures lack negatives for interval overlap, alias collision, hierarchy cycle, carry-in inflation, closed-centre posting and cross-budget double draw.

## Scenario result

All four negatives pass as written; `historical-rewrite` and `unknown-as-zero` are structurally enforced. Positives pass except `organization-move-only` (finding 6, no structure) and `split-reconciliation` (weights unconstrained). The multi-source revision passes within one aggregate and is unproven across aggregates. The carry-in variant of `successor-double-availability` **fails** — availability is recreated legitimately under current constraints.

## Identifier decisions

No allocation. `modelId` and `registryId` remain null; `allocationState` stays `unassigned`; no numeric gap inferred. `canonicalPublishable` stays false for both artefacts; the profile keeps `newRuntimeId: false`. Registry reservations unchanged; publication authority not granted. Research packaging is permitted at draft grade only.
