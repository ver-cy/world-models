## Verdict
**ACCEPT WITH LIMITS** — profile held, not published; no identifier granted.

## Critical findings

1. **Range vs. single-boundary contradiction (sharpest).** Clause 4 fixes exactly one grouping-boundary revision per run; clause 6 requires disputed Z (G1/G2) to yield an attributed *range*. A range presupposes ≥2 grouping interpretations evaluated in one run. Either clause 4 is violated or the range is produced outside governed run identity. Repairable only by declaring the dispute as a multi-hypothesis *inside* one grouping-boundary revision, so the revision is range-valued by construction.

2. **`unevaluable` is overloaded.** Clause 7 uses it as an evidentiary coverage state; clause 9 uses it as an access-denial state. If the two are distinguishable, denial discloses presence (violating clause 9); if indistinguishable, coverage semantics are corrupted (violating clause 7). No disambiguation mechanism is declared.

3. **Fact-key / boundary mastership ambiguity.** Clause 3 has Market Scope *declare* one fact key and one boundary revision; clause 8 binds both into the digest *separately* from the scope edition. Precedence on divergence, and whether a run may narrow scope-declared values, is unspecified.

4. **Segmentation as shadow master.** Clause 3 lets Market Scope declare segmentation while asserting it stores no facts. Unless segmentation *references* an external governed segmentation master by revision, the parameter edition becomes de facto mastership for customer classification — a hidden master, not a hidden aggregate.

5. **Cross-perimeter group view underspecified.** Clause 10 permits a group view to set-union facts across perimeters but imposes elimination-rule matching only for *cross-period* comparison. Unioning P1 (S1→S2 external) with P2 (S1→S2 eliminated) can reintroduce or silently suppress the same fact. Clause 5's containment test is not lifted to union operations.

6. **No hidden aggregate or identifier otherwise.** Concentration outputs are derived projections; the digest is content-addressed, derivable from bound inputs, and carries no lifecycle. `newRuntimeId=false` holds.

## Required holds

- H1: Declare disputed-link hypothesis sets within a single grouping-boundary revision; range endpoints carry claimant attribution.
- H2: Split coverage-`unevaluable` from access-`unevaluable`; the access variant must be indistinguishable from omission in the projection, with reason retained only inside the authorization boundary and governed by disclosure shape.
- H3: State precedence: Market Scope edition is authoritative for fact key and grouping boundary; digest binding is restatement, and divergence is a hard failure, not a resolution.
- H4: Require segmentation and coverage policy to be external governed references by revision; prohibit inline definition.
- H5: Extend the matching requirement (fact key, boundary, elimination rule) to cross-perimeter group views, or forbid union across differing elimination rules.
- H6: Carry forward base-model publication blockers; none contradict this profile.

## Scenario result

Preserved. X's customer-role and supplier amounts stay unnetted; concentration uses customer-role facts only. S1→S2 is external in P1 and eliminated in P2 solely under P2's declared consolidation boundary — ownership alone is not invoked. Y remains a reason-coded singleton. Z yields an attributed range, but only validly under H1. Two perimeters → two projections, no artifact merge.

## Identifier decision

No new runtime or model identifier. Profile over Party, WM-ORG-014, WM-ECO-020 and adjacent commercial masters only; parameter edition and projection digest are governed artifacts, not identities. No publication authority granted.
