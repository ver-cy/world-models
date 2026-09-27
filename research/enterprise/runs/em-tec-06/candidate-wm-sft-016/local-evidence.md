# EM-TEC-06 local synthesis

## Disposition

- Complete reserved WM-SFT-016 as one **Service Level Objective and Reliability Commitment** aggregate containing SLI specification, SLO policy/version, SLO evaluation, ErrorBudgetPolicy and effective-dated ObservabilityBinding.
- Reuse the identifier-unassigned Metric Definition candidate from EM-DAT-05 for formula, population, unit, dimensions and null semantics. WM-SFT-016 does not redefine metric semantics.
- Reuse WM-MAT-008 for raw observations, absence reasons and time/provenance. SLO evaluations cite observations and retain aggregates/evidence references without becoming a telemetry store.
- Keep contractual SLA obligations, obligees, enforceability, credits and remedies in WM-ECO-006 and its obligation boundary. SLO policy and evidence may be referenced from a contract but do not become legal obligations by themselves.
- Leave **User Journey** as an identifier-unassigned candidate because a composite, user-visible outcome across services has independent identity and lifecycle.
- Allocate no runtime or model identifier.

## Identity and mastership

SLO identity combines subject, SLI specification and purpose. An immutable policy version additionally fixes target, window definition, eligibility, exclusions, minimum coverage and error-budget policy. Changes to formula, predicates, eligibility, exclusions, target or window create a successor version.

Evaluation identity is policy version plus one concrete window instance. Evaluations are append-only; restatements preserve predecessors. Git or a policy registry masters policy versions; the metric registry masters SLI formulas; WM-MAT-008/telemetry masters observations; the evaluator masters evaluation records. An observability platform is a source, not the master of the commitment.

## SLI, SLO, evaluation and budget

SLI specification pins a Metric Definition version and adds the unit of user work, good-event predicate, valid-event predicate, observation point and ObservabilityBinding. SLO policy supplies target, window, eligibility, exclusions, coverage threshold and verdict vocabulary. Evaluation records valid, good, ineligible and indeterminate counts, coverage, attained value, evaluator identity/version and one verdict. Error-budget policy derives budget from target/window and defines reaction rules without creating contractual duties.

Commitments normally attach to a Service or User Journey. A system/application SLO is allowed for platform reliability. Instance and component indicators are diagnostic and roll up only through a declared aggregation/additivity rule.

## Missing data, windows and exclusions

Below the declared coverage threshold yields `unknown-insufficient-coverage`. Zero eligible traffic yields `no-eligible-traffic`. Unclassifiable attempts remain indeterminate and never count as good. WM-MAT-008 supplies absence and censoring semantics.

Changing window length, alignment, calendar basis or timezone creates a successor policy, closes predecessor windows and records an error-budget transition. The first incomplete successor window is partial. Cross-version comparison requires an explicit reconciliation.

Exclusions are declared before evaluation, authorized, capped, counted and reported. Retroactive exclusions create linked restatements; they never erase events or silently reduce the denominator.

## Acceptance scenario

A checkout journey crosses authentication, pricing and payment services. Its SLI measures end-to-end successful attempts within a latency bound at the user-facing edge. A 30-day rolling window changes to a calendar month, creating a successor policy and partial first window. Missing pricing spans reduce coverage below the 99% threshold, so the evaluation returns `unknown-insufficient-coverage` with counts and gap evidence. Missing spans cannot produce a false reliability success.

## Invariants

1. Every SLO names an SLI version, target and window definition.
2. No data, no eligible traffic and met are distinct outcomes.
3. Missing telemetry never becomes a good event.
4. Metric semantics are referenced, not restated.
5. Observations remain externally mastered.
6. Material policy changes mint a successor version.
7. Error budget never silently crosses a window-definition change.
8. Exclusions are prior, capped, authorized and visible; retrospective changes create restatements.
9. Instance indicators are diagnostic; commitment rollups require declared aggregation.
10. SLO and SLA have different authority bases.
11. Every evaluation records evaluator, version, coverage and offset-qualified bounds.
12. Superseded policies and restated evaluations remain resolvable.

## Holds

WM-SFT-016 now has a reviewable completion candidate with SLI/SLO policy, evaluation, error-budget and observability-binding structures, four external relations and seven fixtures. The incorrect WM-ECO-006 parent link is removed; contractual SLA authority remains external. Metric Definition and User Journey remain identifier-unassigned, while WM-MAT-008, WM-ACT-004 and WM-ECO-006 retain their own publication holds. Exact Grok comparison, one frozen semantic audit, package conversion and live verification remain required. This checkpoint makes no canonical completeness or installability claim yet.
