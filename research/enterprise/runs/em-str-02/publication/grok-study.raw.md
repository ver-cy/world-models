# Grok independent study — EM-STR-02

## Verdict
Conditional accept of the proposed profiles; reject one identifier-unassigned Outcome and Benefit Realization aggregate. Profile WM-KNW-011 for Objective, Key Result and Target with mandatory Metric Definition revision pins. Restrict WM-XCT-025 to WM-MAT-008 observation hosts as an EM-STR-02 usage rule, not a settled catalogue fact. Profile WM-ACT-034 for Value Assessment. Reference EM-DAT-05 for metric definitions and EM-WRK-03 for work/deliverables. Outcome and Benefit should not remain one aggregate. Identity for those classes is deferred. No identifiers are minted.

## Identity / mastership
WM-KNW-011 owns the desired-end-state record but not metrics, observations, evaluation verdicts, actions, benefits or realized outcomes. Metric master is EM-DAT-05. WM-XCT-025 is a mixin with no standalone identity and its CHILD link to WM-MAT-008 is unfrozen. Value Assessment is a WM-ACT-034 profile. Outcome and Benefit have no assigned identity here. WM-ACT-029 and EM-WRK-03 are possible benefit-owner homes, so a third unassigned bag would create a third home.

## Objective / KR / target
Profile WM-KNW-011. A Key Result is a measurable-progress role under an Objective with mandatory quantitative binding. Target uses baseline, base period, value, unit, operator, horizon and milestones. Every quantitative field pins an EM-DAT-05 MetricDefinition revision. Metric change creates a successor binding and comparability note. KR hit is an external evaluation and never proves Outcome or Benefit.

## Outcome / observation
Observation is a measurement fact. Outcome is an asserted subject state-change and horizon, evidenced by observations over time. One observation or deliverable acceptance is not an Outcome. Intended end-state stays on WM-KNW-011. Realized, claimed, disputed or superseded Outcome is a separate identity whose allocation is deferred pending crosswalk to WM-ACT-029 and EM-DAT-05. Outcome cites observations; it does not embed WM-XCT-025.

## Benefit attribution
Reject packing Benefit, Disbenefit and Attribution Claim into the Outcome write boundary. Outcome and Benefit differ in identity, lifecycle, mastership and N:M multiplicity. Claims are revisable without rewriting Outcome or Observation. One Benefit is named once; Attribution Claims are benefit-owned parts with contributor, method, as-of, confidence/interval, optional share and causal limit. Shares need not total one; residual unattributed is required. Program and project must not mint duplicate realised Benefits. Disbenefit is a first-class value record, not a negative field on an intended Benefit. A Benefit may cite Outcomes or a counterfactual assumption; do not mint a fake Outcome.

## Value / anti-value
No universal formula. WM-ACT-034 Value Assessment names a version-pinned valuation profile, cites observations, and may conclude valued, anti-valued, insufficient evidence or incomparable scales. Abstention is first-class. Netting is an assessment conclusion under a declared method. Collision with WM-ACT-029 benefit-owner semantics remains a hold.

## Invariants
A goal is not a metric. Target pins metric version. Deliverable done, planned effect or KR hit does not prove realized Benefit. The same Benefit is not separately realised by program and project. Attribution revision does not rewrite Outcome or Observation. Uncertainty is mandatory on claims and assessments; residual unattributed is allowed. Net value loads related Disbenefits or declares them out of scope. WM-XCT-025 is not adopted on intent, assessment or unassigned Outcome/Benefit records.

## Scenario
Objective/KR/Target pins MetricDefinition R. Projects A and B accept deliverables, but Benefit B remains unrealised. Delayed observations show handling time down and error rate up, producing Outcome O1 and O2. B receives two uncertain claims with residual open. Program points to B rather than minting B-prime. Disbenefit D is recorded for O2. WM-ACT-034 assessment under profile P@version concludes net value with uncertainty or incomparable; delivery acceptance is not evidence.

## Blockers
Outcome and Benefit identity remain deferred until WM-ACT-029/EM-WRK-03 crosswalk. WM-KNW-011 relationships are empty; TargetValue is dual-homed; WM-XCT-025 to WM-MAT-008 CHILD is unfrozen; WM-ACT-034 lacks a published Value Assessment profile; intended versus realized Benefit and counterfactual-only Benefit remain open. Review is structural and not canonical or installable.
