# EM-STR-02 local synthesis

## Disposition

- Profile WM-KNW-011 for Objective, Key Result and Target. These are role- and naming-regime variants of the same governed objective identity, not separate model roots.
- Reuse WM-XCT-025 only as the observation value/method/time/uncertainty mixin on a WM-MAT-008 observation host. The mixin owns no record identity.
- Add one identifier-unassigned **Outcome and Benefit Realization** aggregate containing independently addressable Outcome, Benefit/Disbenefit and Attribution Claim records under one benefits-register master.
- Profile reserved WM-ACT-034 Assessment / Evaluation for Value Assessment. Reference the unassigned Metric Definition candidate from EM-DAT-05 and work/deliverable records from EM-WRK-03.

Objective states a desired future condition and is never a metric. Key Result is an objective-role record with mandatory measure binding. Target binds comparison operator, baseline/target periods and values to an exact Metric Definition revision. A metric revision change requires an explicit methodological restatement; it cannot silently re-baseline the target.

Outcome is an asserted change in a subject's state, distinct from a deliverable and from the observations that evidence it. Benefit is a governed expected/forecast/partially-realised/realised/reversed claim over one or more outcomes. Disbenefit uses the same lifecycle with negative polarity. Planned effects remain forecasts until final or amended observations support the change for the declared phenomenon period.

Attribution Claim belongs to the Benefit aggregate and records contributor, share with uncertainty interval, method, evidence and adjudication. Shares are reconciled against one benefit identity and period. Portfolio/programme and constituent-project claims cannot both count the same contribution for the same period.

Value Assessment declares criteria, scale, method, evidence and conclusion. Incompatible value and harm scales remain separate labelled dimensions; scalar netting requires an explicit commensuration method and preserves uncertainty.

## Invariants

1. Objective is not a metric; targets pin exact metric-definition revisions.
2. Metric change never silently changes an existing target or baseline.
3. Deliverable completion does not prove an outcome.
4. Realisation needs qualified observations whose phenomenon time falls within the realisation window.
5. Expected and realised claims coexist; realised never overwrites expected history.
6. Missing measurement is an explicit absent reason, never zero.
7. Adjudicated attribution shares per benefit and period cannot exceed one.
8. Programme and constituent-project contribution claims cannot double count.
9. Disbenefit is polarity, not a separate model, and cannot be netted without method.
10. Units, scale versions, method, observation times and uncertainty travel with every value.

## Scenario result

Two projects claim 0.6 and 0.5 of one retention benefit, so both claims remain unadjudicated until reconciled to a non-overlapping total. Delayed measurement leaves the benefit forecast with `measurement-pending`; later evidence produces partial realisation with uncertainty and preserves the late result time separately from the phenomenon period. A rise in support contacts is recorded as a disbenefit attributed to one project and remains a separate dimension because no commensuration method exists.

## Holds

Both bases are non-canonical reviewable drafts. The Outcome and Benefit aggregate lacks registry allocation; the WM-MAT-008, WM-ACT-034 and EM-DAT-05 crosswalks are incomplete; relationship contracts, metric pins, attribution authority and fixtures are absent. No runtime or installability claim is made.
