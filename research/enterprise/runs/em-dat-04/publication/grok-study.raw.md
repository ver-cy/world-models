# Grok independent review — EM-DAT-04

Source conversation: https://grok.com/c/16c983bd-7369-422f-a401-8f02f4ff0333

## Verdict

Accept the proposed completion of reserved WM-DAT-007 with holds. WM-DAT-007 owns the purpose-qualified quality evaluation and verdict. Reusable rules, metric definitions and formulas, observations and issues remain externally mastered. CoverageAssessment does not need independent model identity; it is a QualityEvaluation kind with additional mandatory completion constraints. WM-DAT-007 may bind metric formula revisions but must not author or master formulas.

## Identity and mastership

One evaluation has one purpose, one subject, one evaluation-as-of time and at most one current verdict. A changed frame version creates a distinct evaluation. WM-KNW-013 owns reusable rules, WM-MAT-008 owns observations, WM-KNW-014 owns issues, the identifier-unassigned Metric Definition candidate owns formulas, and WM-ACT-034 supplies the generic assessment shape. A frame is a referenced versioned subject rather than a WM-DAT-007-owned entity. CoverageAssessment is a kind discriminator plus mandatory frame and denominator fields.

## Dimension and denominator findings

Completeness, accuracy, validity, freshness and coverage are pairwise non-substitutable. Accuracy requires independent reference truth. Freshness requires a data-as-of clock, an evaluation/purpose-need clock and a purpose-owned latency budget. Coverage compares the evaluated population with a versioned intended frame; sample rate is not coverage.

Denominator states are exact, estimated or unknown. Exact alone supports an unqualified population ratio. Estimated requires a disclosed estimation method and uncertainty and remains estimate-qualified. Unknown blocks ratios and population claims that require the denominator. Any ratio-bearing evaluation, not only coverage-kind, must cite a versioned frame and explicit denominator state. Sample observations do not become population denominators without a declared expansion method.

## Lifecycle and scenario

Lifecycle is draft, bound, observed, evaluated, verdict/deferred and superseded. Corrections and remediation retests create successor evaluations; predecessor identity, evidence and verdict remain immutable. External issues survive supersession.

A fully populated but stale dataset may pass completeness and validity while freshness fails and accuracy remains unevaluable without independent truth. Scores are not netted. A 4% sample may support sample-conditioned accuracy only; it neither establishes population completeness nor coverage. Population inference is estimated only with a design-based method and frame size, otherwise unknown. Population claims require a separate evaluation and never inherit the sample verdict.

## Blockers

Metric Definition remains identifier-unassigned, leaving formula mastership without a canonical home. Frame-versioning authority is not named. Parent and relation rows remain research-only. No new identifier or canonical-completeness claim is justified.

