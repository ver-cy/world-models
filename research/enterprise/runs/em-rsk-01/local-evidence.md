# EM-RSK-01 local synthesis

## Disposition

- Reuse WM-KNW-015 as the Risk / Opportunity entity and lifecycle master.
- Profile WM-XCT-027 as a host-scoped Risk Assessment Context. Retain risk/revision pins, context, scale/method/horizon, inherent and residual estimates, uncertainty, control citations, appetite comparison, comparability and binding governance. Remove control authoring and effectiveness production from the mixin.
- Add one identifier-unassigned **Control** candidate because control definition, implementation state, ownership and lifecycle exist independently of any risk or assessment.
- Profile the reserved WM-ACT-034 Assessment / Evaluation candidate for control testing and effectiveness determination after a dedicated crosswalk. Do not create a second assessment model here.
- Delegate treatment plans and actions to EM-RSK-02; reference evidence, appetite/tolerance, acceptance decisions and execution telemetry from their source masters.

The Control model owns objective, mechanism, applicability, owner, implementation state, operating cadence and dependencies. It does not infer effectiveness. A Control Assessment pins control revision, criteria, method, scope, period and evidence, and produces an expiring effectiveness determination with confidence and invalidation triggers. Individual execution occurrences stay in operational systems and are cited as evidence.

Comparability is a gated verdict, not a normalization shortcut. Estimates must pin criteria set, method, expression mode, scale, scope, exclusions, horizon and as-of time. Ordinal values cannot be averaged or multiplied. Cross-horizon comparison is invalid unless a declared conversion exists. Shared cause or dependence adds correlation and aggregation caveats; it never merges risk identities.

Residual risk requires explicit grounds: relied-on controls, current effectiveness determinations, changed dimensions and causal explanation. A missing or expired determination makes reliance unknown and cannot justify reduction. Residual-risk acceptance is an authorized decision referencing the assessment, not a field set by the risk owner or engine.

## Invariants

1. Every estimate carries scale, expression mode, horizon, as-of time and criteria version.
2. Risk identity survives re-estimation, register movement and treatment changes.
3. Control existence, implementation, documentation or policy status never proves effectiveness.
4. Effectiveness requires a scoped assessment, evidence, method, conclusion time and validity.
5. Residual risk without cited grounds and current determinations is invalid.
6. Policy status never closes a risk.
7. Aggregation requires an explicit comparability verdict and preserves caveats.
8. Shared causes and common controls create dependency warnings, not arithmetic permission.
9. Event, observation/as-of and record time remain distinct.
10. Superseded risk or control revisions mark dependent assessment contexts stale.

## Scenario result

One control is cited by three risks. A failed execution changes only the assessment whose determination covers the failed population, period and claimed mechanism; it invalidates that determination and reopens residual estimation. A differently scoped risk records no causal change. A risk relying on the control without a determination remains unsupported rather than worsening by automatic rule. A green policy status closes none of the risks.

## Holds

Both bases are non-canonical single-provider reviewable drafts. WM-XCT-027's upstream ownership split is unresolved. The Control candidate lacks registry allocation; the WM-ACT-034 profile crosswalk is incomplete; treatment ownership remains with EM-RSK-02. Source pins, composition, upstream staleness, authority, evidence and scenario fixtures remain unverified. No runtime or installability claim is made.
