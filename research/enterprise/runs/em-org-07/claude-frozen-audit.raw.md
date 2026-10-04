# Frozen semantic audit — EM-ORG-07

**Verdict: ACCEPT WITH LIMITS** (held; no publication authority granted)

## Critical findings

1. **Derivable aggregate, not a stored one.** No hidden entity or identifier is introduced. But clauses 1+5 make ratings addressable per relation while the party remains a single master, so joining R-A and R-B ratings reconstructs a de facto "party influence" profile — an attribute clause 5 and the scenario explicitly deny C. The aggregate lives at the query/projection layer, not in the model.
2. **Interest mastership is ambiguous.** Clause 2 makes the relation a WM-ORG-013 instance; clause 3 also profiles Interest onto WM-ORG-013. Declared interest as relation-borne is coherent, but clause 3's "analyst hypotheses" have claim semantics (attributed, contestable, defeasible) and therefore belong with expectation under WM-KNW-007. As written, hypotheses can write into the relation master, violating clause 2's no-write-through intent.
3. **Clause 6 preservation wording is internally contradictory.** Read literally, S-A2 "preserves the result" of S-A1 while asserting a different result. The scenario's reading (S-A2 = medium, reusing M1/U1/E1) is worse: an unchanged method, uncertainty and evidence base cannot license a changed result. Either the delta has undisclosed basis, or U1 is stale and misstates confidence.
4. **Permission boundary is named but unmodelled.** Clause 8 defers execution to a "separate permission/decision boundary" with no class, master or identifier. Fail-closed is asserted, not anchored.
5. **Clause 9 ↔ clause 10 tension.** Mandatory retention of all attributable dissent under aggregation can reconstruct restricted expectations and evidence that clause 10 requires to survive projection.

## Required holds

- **H1.** Prohibit cross-perimeter rollup or join to party level in any projection; publication of >1 perimeter rating for one party requires explicit inference review.
- **H2.** Restate clause 3: declared interest = WM-ORG-013 relation content; hypothesized/imputed interest = attributed WM-KNW-007 claim. No hypothesis writes to relation or party master.
- **H3.** Restate clause 6: successor preserves the prior *record* (immutable history + citation); it must carry its own dated method, uncertainty, evidence and assessor. Reuse of M1/U1/E1 must be an explicit re-derivation statement, not inheritance.
- **H4.** Name the permission/decision master (or record explicit unknown) before any execution-adjacent use; default deny meanwhile.
- **H5.** Projection layer must redact restricted content with presence markers preserving clause 12's five distinct states (withheld ≠ missing ≠ not-yet-heard ≠ indeterminate ≠ low).
- **H6.** Base-model publication blockers on WM-ORG-013, WM-KNW-007, WM-ACT-034, WM-ACT-008, WM-ORG-001, WM-PER-001 carry forward as holds; none contradict this profile.

## Scenario result

Passes. C is not an assessment subject; S-A1 survives as cited history; B inherits nothing; restricted expectation does not cross into B; registration confers no outreach or decision authority. Residual risk only at H1 (A+B joined view) and H3 (S-A2 basis must be restated, not inherited).

## Identifier decision

`newRuntimeId=false` upheld. No new master or aggregate class. Relation addressability is sufficient via WM-ORG-013 instance keys qualified by perimeter, viewpoint and valid/recorded time — conditional on H2 confirming WM-ORG-013 supports instance-level bitemporal identity.
