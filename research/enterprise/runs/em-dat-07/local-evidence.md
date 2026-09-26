# EM-DAT-07 local synthesis

## Disposition

- Profile WM-ACT-036 Research Study for Analytical Study. It already owns question, protocol, population, sampling, applied analysis, estimates, findings and limitations. WM-ACT-034 contributes assessment/sampling mechanics but is not the master because analytical inquiry need not have a criteria catalogue or conformity verdict.
- Keep Analysis Method as an identifier-unassigned reusable definition candidate. WM-ACT-036 records the pinned method version, parameters, software and execution used by one study.
- Reuse WM-KNW-007 for Analytical Findings and recommendation statements. A recommendation is a deontic claim with an explicit non-acceptance marker until decision authorities act.
- Reuse WM-KNW-010 for decision content and WM-ACT-024 for the decision/approval occurrence. Reports reuse WM-REC-002 and do not replace finding justification.
- Allocate no runtime or model identifier.

## Identity and mastership

Study, reusable method, method application/execution, observation, evidence citation, finding, report issue, recommendation, decision content and decision occurrence retain distinct identities. Every finding pins a study version, method version, population/sample, input snapshot and applicable time. Reports pin and render results but do not own analytical conclusions.

The reusable method definition owns estimator/formula, assumptions, admissible inputs and known failure modes. A study owns the method application: version pin, estimand, preprocessing, code/software versions, parameters, environment and deviations. Definition changes never retroactively alter issued studies.

## Finding, causality and alternatives

An estimate belongs to the study; a finding is a WM-KNW-007 claim with canonical statement, claim type, quantification, measurand, uncertainty, population/place/time scope, assumptions, defeaters, confidence and evidence bindings.

Association never becomes causation implicitly. A causal claim requires a defined measurand, comparator, design descriptor, aggregation level and competing-explanation analysis. Assumptions are declared claims with verification status; observations remain external evidence. Alternative interpretations are sibling claims over the same study, linked by typed conflict relations. Conflict is recorded rather than silently adjudicated.

Sampling records frame, inclusion/exclusion stages and reasons, achieved versus planned size, missingness, bias and generalisation limits. Unknown denominators block ratio publication.

## Recommendation and decision

A recommendation declares proposed action, addressee, supporting findings, scope, confidence and deontic modality. It has no deciding authority, disposition, effect onset or approval event. Acceptance requires WM-KNW-010 to compare alternatives and record rationale, plus WM-ACT-024 to record the authorized occurrence and effective outcome. Rejection leaves the recommendation resolvable with its ground.

## Acceptance scenario

One study observes increased ticket counts in a single opt-in support channel. Claim A attributes this to employee productivity decline; Claim B attributes it to release-driven intake-routing and logging changes. A lacks a productivity measurand and denominator, uses a biased frame and does not address the competing explanation. It can remain only a low-confidence associational claim bounded to the sample. B remains a conflict-linked alternative; neither becomes an accepted decision. The inference that ticket growth proves productivity decline is rejected.

## Invariants

1. Study, method, execution, observation, evidence, finding, report, recommendation and decision identities are distinct.
2. Every finding pins study, method, population/sample and data snapshot versions.
3. Every conclusion states its applicability scope.
4. Assumptions and observations remain structurally distinct.
5. Causal claims require measurand, comparator, design and competing-explanation analysis.
6. Association never auto-upgrades to causation.
7. Unknown denominator blocks ratio publication.
8. Exclusions record reason and stage; sampling records frame and missingness.
9. Alternative interpretations coexist as typed conflict-linked claims.
10. A report never substitutes for conclusion justification.
11. A recommendation is not a decision and has no effect without both decision content and authorized occurrence.
12. Corrections and revised inputs create successors; issued studies and findings are not rewritten.

## Holds

All bases remain non-canonical reviewable drafts with single-provider limitations and unsettled relation contracts. Analysis Method lacks registry allocation; the deontic recommendation specialization is a declared gap; source pins, crosswalks and fixtures remain incomplete. This checkpoint makes no canonical completeness, installability or publication claim.
