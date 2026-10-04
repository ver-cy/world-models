# EM-LND-04 Strategic Landscape — independent review

## Verdict

**Governed profile/projection over existing masters; no new identifier.** Both candidate types resolve without independent identity: `StrategyLandscape` is a read-only view class, and `StrategicAlignment` is an edge profile projected from assertions already mastered at their endpoints (WM-ACT-030 strategy-alignment/contribution assertions; WM-KNW-011 `fd-higher-level-alignment` and `fd-goal-refinement`). Minting a third alignment record would create the divergent second copy WM-KNW-011's measure-binding rationale explicitly forbids. This follows the EM-LND-05 disposition (landscape profile, no catalogue/runtime ID, scope owned by masters) and keeps `target_model_ids` legitimately empty.

## Evidence

Reuse is justified only where a complete spec bounds the node: WM-KNW-011 (objective/target roles, measure binding by reference, refinement, conflict declaration, accountable party), WM-MAT-008 (measurement host: phenomenon/result/valid/ingestion time, coded absence, censoring, quality flags), WM-XCT-025 (mixin only — value, unit, method, uncertainty on a WM-MAT-008 host; no record identity), WM-ACT-030 (initiative, options, hypotheses, intended-results logic, formalization), WM-ACT-029 (program/portfolio root under a mandatory profile discriminator), WM-ACT-005 (project, baselines, project-accountable benefits only), WM-ACT-034 (assessment: criteria binding at version, decision rule, determination separated from decision). Every one is `publishableCanonical: false`.

## Identity/mastership

The view masters nothing. It holds a referent table whose entries are one of three states: **resolved** (authoritative model id), **declared-unallocated** (view-local placeholder key for Strategy/BusinessModel/StrategicTheme/ValueProposition/ValueStream/StrategicScenario from EM-STR-01, which has no reserved candidate, and for the Outcome/Benefit/Attribution-Claim aggregate that EM-STR-02 already declared identifier-unassigned), or **blocked** (WM-ACT-001). Placeholder keys are view-local, never promoted, never treated as model ids; allocation stays with EM-STR-01/02/03 and the registrar.

## Strategic elements

Intent/strategy → unallocated (EM-STR-01). Objective, key result, target → WM-KNW-011 role codes with naming-regime tag; a target pins an exact measure revision. Portfolio → WM-ACT-029 with declared profile; initiative → WM-ACT-030; project → WM-ACT-005; capability → blocked. Measurement → WM-MAT-008 + WM-XCT-025. Value assessment, capability assessment and causal-confirmation verdicts → WM-ACT-034 profiles.

## Alignment and causality

Two distinct edge classes, never merged.

**Support/alignment** (initiative|project|portfolio → objective): requires a basis — a resolvable WM-ACT-034 assessment, a WM-MAT-008 observation, or an explicitly declared expert judgement with its basis stated (WM-KNW-011 permits the last only with recorded justification). Basisless edges are not stored; they become findings.

**Causal hypothesis** (output → outcome → benefit): stored as a hypothesis with assumptions, attribution limit and confidence, mastered by WM-ACT-030/WM-ACT-029 results-chain findings. Promotion to *confirmed* requires a cited assessment with declared criteria, method and decision rule. Confidence alone never promotes. Supporting and contradicting claims are both retained (WM-ACT-030); declared goal conflicts and priorities are displayed, never arbitrated (WM-KNW-011).

## Outputs/outcomes/benefits

Five separable assertion classes. **Objective** = desired end state, not a metric, not a collection. **Portfolio** = governed component collection; it may never be cited as the satisfied objective. **Initiative output** = delivered artefact, owned by the delivery master. **Outcome** = asserted change in a subject's state, distinct from the deliverable and from the observations evidencing it. **Realized benefit** = a governed claim over outcomes, supported by final or amended observations whose phenomenon time falls inside the realization window, with adjudicated attribution shares ≤ 1 per benefit and period. Expected and realized coexist; realized never overwrites expected history. Funding, completion and spend prove none of these.

## Capability constraint

WM-ACT-001 (`vr.wm-act-001`, legacy K1, `described-previous-version`, `migration-boundary-review`, spec unavailable) is the only reserved capability candidate and is not usable. Two problems: no spec to crosswalk, and a semantic gap — its purpose is "what an agent is able to do", while EM-STR-03 requires a capability surviving reorganisation and independent of realisation means. Capability nodes are therefore **blocked referents**: the landscape renders them, marks the view degraded, and answers "which capability constrains strategy" only as a candidate list — capabilities on the support path of ≥1 objective whose assessed level (WM-ACT-034 profile, method-bound) is below the level those objectives require. Ranking is not asserted while the master is unresolved.

## Time/scenarios

Three view classes: authoritative as-of, as-of replay, scenario. Every node and edge carries an effective interval; assertion knowledge time stays separate from the event time it describes, and measurement phenomenon/result/ingestion times stay separate per WM-MAT-008. Goal horizons come from WM-KNW-011; `horizon`, `scope`, `scenario`, `review_cadence` from LND-04 v1 remain **candidate-not-normative**. Scenario views bind a scenario code plus WM-ACT-030 options/hypotheses and any unallocated StrategicScenario referent. Scenario output may never feed authoritative actuals or benefit realization. Contradictions are retained with both sides' provenance and confidence, not netted. Missing measurement is a coded absence reason, never zero.

## Gap questions

Findings are addressed to the accountable party resolved from the master, never to the view: goal owner (WM-KNW-011 accountable party), initiative sponsor (WM-ACT-030), portfolio owner (WM-ACT-029), project sponsor (WM-ACT-005), capability owner (unresolvable — escalates to the registrar). Each finding carries rule id, subject, as-of time, evidence pointer and severity, and is a claim about the record, not about the enterprise. A goal with a recorded non-practicability justification and qualitative criteria is **not** a defect; only an unjustified missing measure binding is.

## Scenario

The map contains an initiative with no basisless-free support edge to any objective, and an objective with no resolvable measure binding and no justification. It emits two findings — "initiative without stated goal" to the initiative sponsor, "objective without measurement or justification" to the goal owner — and renders both nodes as present-but-unaligned/unmeasured rather than dropping them.

**Negative case tested and refuted.** A project tagged `strategy`: the tag is not an authorization instrument, not an alignment basis, and not evidence. It creates no support edge (no basis), no outcome (WM-ACT-034 verdict absent), and no realized benefit (no qualified observation, no adjudicated attribution). The view shows three distinct nulls — unaligned, unevidenced, unrealized — and emits one finding. Benefit is never inferred from a label, budget line, completion or linked project state.

## Invariants

1. A support link has a recorded basis or it is not stored.
2. An objective is not a portfolio; a portfolio is never the satisfied objective.
3. A delivered output is not automatically a benefit.
4. The view stores no monetary, benefit, membership or measurement fact and mints no identifier.
5. A causal hypothesis becomes confirmed only by a cited assessment; confidence does not promote it.
6. Realization requires qualified observations inside the declared window; absence is coded, never zero.
7. Adjudicated attribution shares ≤ 1 per benefit and period; portfolio and constituent claims never double-count.
8. Scenario results never feed authoritative actuals or realized benefit.
9. Capability nodes are degraded while WM-ACT-001 is unresolved.
10. A tag never creates an edge.

## Minimal profile shape

`view_id` (view-local); `class` ∈ {authoritative, as-of-replay, scenario}; `as_of`; `horizon`; `scenario_code`; `referent[]` {kind, state ∈ {resolved, declared-unallocated, blocked}, master_ref | placeholder_key}; `edge[]` {type ∈ {supports, contributes, constrains, measures, causal-hypothesis}, from, to, basis_ref, confidence, effective_interval, contradicts[]}; `finding[]` {rule, subject, owner_ref, as_of, evidence_ref, severity}; `degradation[]`.

## Holds

Every reused base is a reviewable draft with `publishableCanonical: false`; WM-ACT-030, WM-ACT-029 and WM-ACT-034 are single-provider results with waived independent review, and WM-ACT-030's registry Project parent link is itself held against its own invariant. Relationship contracts are empty across all seven bases, so the ownership boundaries this profile depends on are narrative and unenforced. WM-ACT-001 is unavailable; EM-STR-01's strategy types and the Outcome/Benefit aggregate are unallocated; the EM-STR-03 capability crosswalk is unproven. No canonical completeness and no installability is claimed, and no identifiers were allocated.
