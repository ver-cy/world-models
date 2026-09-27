# EM-PRD-03 local synthesis

## Disposition

- **Complete and reclassify reserved WM-REC-006** from view-candidate to a Requirement aggregate with stable identity and immutable revisions.
- Keep Acceptance Criterion, Requirement Baseline and Trace Link as independently addressable records contained by the aggregate for the first completion. They receive no new model identifiers; future extraction requires separate mastership and lifecycle evidence plus registry allocation.
- Reuse WM-KNW-013 by pinned revision reference for reusable formal or formalizable rules. Remove its candidate parent signal to WM-REC-006; Rule is also issued by policies, standards and controls.
- Keep stakeholder need, feature/design, implementation task, test case/result, observation/evidence, waiver and decision in their source masters.

A stakeholder need preserves the stakeholder's problem or desired outcome. A requirement is an authoritative, verifiable statement derived from one or more needs. A feature or design claims how the requirement may be realized. A task records implementation work. A test case defines verification; a test result and evidence may support a satisfaction claim. Closing a task has no evidential weight for requirement satisfaction.

Requirement revisions are immutable. An acceptance criterion belongs to one exact requirement revision and may bind a pinned WM-KNW-013 rule revision to the requirement subject, operands, units, tolerance and verification method. One-off criteria may remain local expressions and must not silently create reusable rules.

A baseline is a sealed, named set of exact requirement revision references plus authority, effectivity and digest. Any membership or revision change creates a new baseline. A trace link is a reified, attributable, typed assertion whose endpoints are revision-pinned. Conflict records preserve all alternatives; a resolution adds an authority-scoped decision and baseline selection without deleting losing alternatives.

## Invariants

1. Acceptance and verification cite an exact requirement revision.
2. Requirement revisions and sealed baseline membership are append-only.
3. Every trace link pins both endpoint revisions and records asserter and time.
4. Task state, including Done, never proves implementation correctness or requirement satisfaction.
5. Satisfaction needs a qualified test result and evidence for the same revision; absence is never pass.
6. Failed and superseded results remain visible.
7. Rule text is not copied when a pinned WM-KNW-013 reference can express the reusable rule.
8. Verification does not transfer to a changed revision; only byte-identical revisions may be explicitly reaffirmed.
9. Conflict alternatives remain resolvable after selection.
10. Waiver, exception and approval never rewrite the source requirement or rule.

## Scenario result

One requirement revision is traced to three Done tasks and a failed test. It remains not verified and blocks its baseline; a later passing result does not erase the failure. A changed tolerance creates a new requirement revision and a new baseline. The previous test is stale for the new revision, while the prior baseline remains sealed and comparable by revision-set diff.

## Holds

WM-REC-006 now has a reviewable completion candidate with stable identity, immutable revisions, acceptance criteria, baselines, trace links and conflicts, plus five external relation contracts and seven fixtures. Its view classification is replaced with a governed aggregate classification and the WM-KNW-013 parent signal is removed. WM-KNW-013 and WM-SFT-015 retain their own publication holds. Exact Grok comparison, one frozen semantic audit, package conversion and live verification remain required. No canonical or installability claim is made yet.
