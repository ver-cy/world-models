# Frozen no-tools semantic audit — EM-LND-04

You are the sole final static semantic auditor. Use only this frozen packet. Do not browse, call tools, invent identifiers, grant publication authority, or ask to rerun. Audit the reconciled held PROFILE semantics, not prose style.

The proposed disposition is PROFILE/projection only: StrategyLandscape and StrategicAlignment mint no business identity. Strategy and Outcome/Benefit remain unallocated; WM-ACT-001 Capability is blocked. The profile must remain read-only, evidence-bearing, reproducible, and unable to turn tags, budgets, completion, membership, absence, scenarios or hypotheses into authoritative facts.

Return at most 1400 words with exactly these sections: Verdict (`ACCEPT WITH LIMITS`, `REVISE`, or `REJECT`); Material defects (number every real defect); Required fixes; Additional fixtures (one fenced JSON array only, each case with id, kind positive|negative, input object, expect object and expectedCode when negative); Freeze decision. State whether a runtime/model identifier is justified. Treat canonical base and registry gaps as holds unless the profile itself is unsafe. This is the one frozen audit; it will not be repeated.

## Candidate profile
```json
{"format":"vercy-enterprise-profile-candidate/v1","contourId":"EM-LND-04","name":"Enterprise Strategy Landscape and Strategic Alignment","decision":"PROFILE","newRuntimeId":false,"bases":["WM-KNW-011","WM-XCT-025","WM-ACT-001","WM-ACT-030","WM-ACT-029","WM-ACT-005","WM-ACT-034","WM-MAT-008"],"constraints":["The landscape is a read-only governed projection and mints no strategic, delivery, measurement or assessment identity.","Each referent is resolved to an authoritative model, declared unallocated with a view-local placeholder, or marked blocked.","Support links require a cited assessment, observation or attributable expert judgment; tags, budgets and membership are insufficient.","Output, outcome and benefit remain distinct, and completion or spend never proves realization.","Causal links remain hypotheses until a pinned WM-ACT-034 assessment promotes them under an explicit decision rule.","Views distinguish authoritative as-of, historical replay and scenario state; scenario results never become authoritative actuals.","Missing measurement is coded absence rather than zero, and contradicting claims remain visible.","Released views pin source revisions and carry a reproducible fingerprint."],"holds":["Strategy roots and Outcome / Benefit remain identifier-unassigned under their owning contours.","WM-ACT-001 capability semantics remain blocked pending a complete boundary and crosswalk.","Relationship contracts, causal fixtures, independent Grok review and frozen audit remain pending."]}

```

## Existing fixtures
```json
{"format":"vercy-enterprise-profile-fixtures/v1","profileName":"Enterprise Strategy Landscape and Strategic Alignment","cases":[{"id":"supported-objective","kind":"positive","input":"Initiative I links to objective O through a dated assessment citing evidence E.","expect":"The support edge retains basis, confidence, interval and provenance."},{"id":"owner-gap-question","kind":"positive","input":"Objective O has no measure binding or justified qualitative criterion.","expect":"The view emits an owner-addressed finding without inventing a value."},{"id":"parallel-scenario","kind":"positive","input":"A scenario projects higher benefit while authoritative actual observations remain unchanged.","expect":"Scenario and actual layers remain separate and reproducible."},{"id":"strategy-tag-alignment","kind":"negative","input":"A project tag named strategy automatically creates an objective-support edge.","expect":"The edge is rejected without attributable evidence."},{"id":"output-is-benefit","kind":"negative","input":"Project completion is reported as realized benefit.","expect":"The inference is rejected."},{"id":"blocked-capability-promoted","kind":"negative","input":"A view-local capability placeholder is emitted as a canonical model identifier.","expect":"Promotion is rejected while capability semantics are blocked."},{"id":"missing-is-zero","kind":"negative","input":"No measurement is recorded and the benefit value is set to zero.","expect":"The value is rejected; absence must remain explicit."}]}

```

## Local synthesis
# EM-LND-04 local synthesis

## Disposition

- Define Strategy Landscape as a governed read-only profile/projection and Strategic Alignment as an evidence-bearing edge profile. Neither receives independent subject identity.
- Reuse WM-KNW-011 for objectives/targets, WM-MAT-008 plus WM-XCT-025 for measurements, WM-ACT-030 for initiatives and hypotheses, WM-ACT-029/005 for portfolio/project context and WM-ACT-034 for assessments.
- Keep unallocated Strategy and Outcome/Benefit referents explicit. Treat reserved-but-missing WM-ACT-001 Business Capability as blocked, not as usable semantics. Allocate no runtime/model identifier.

## Identity and mastership

The view masters no strategic subject, delivery object, measurement or assessment. Each referent is resolved to an authoritative model, declared-unallocated with a view-local placeholder, or blocked. Placeholder keys are never promoted to model identifiers.

Objective, key result and target are WM-KNW-011 roles. Portfolio is a WM-ACT-029 profile, initiative WM-ACT-030 and project WM-ACT-005. Strategy/business-model concepts remain unallocated. Outcome/Benefit remains an unassigned aggregate candidate from EM-STR-02. Capability remains blocked pending a complete WM-ACT-001 boundary and crosswalk.

## Alignment and causality

Support links from initiative/project/portfolio to objective require a cited basis: assessment, observation or attributable expert judgment with justification. A tag, budget line or membership does not create alignment.

Causal links from output to outcome to benefit remain hypotheses with assumptions, attribution limits, confidence and contradicting evidence. Promotion to confirmed requires a WM-ACT-034 assessment with pinned criteria, method and decision rule. Supporting and contradicting claims coexist; the landscape does not arbitrate them.

## Outputs, outcomes and benefits

Objective is a desired state, portfolio a governed collection, initiative output a delivery artifact, outcome an asserted state change and realized benefit a governed claim about valued outcomes. Completion, spend or output delivery does not prove outcome or benefit.

Realized benefit cites qualified observations within its realization window and an adjudicated attribution. Attribution shares cannot exceed one per benefit and period. Expected and realized states coexist; realization never overwrites expected history.

## Capability constraints, time and scenarios

Until capability identity is resolved, the view can only show blocked capability referents and candidate constraints. A candidate constraint links an objective path, required level and a method-bound capability assessment below that level; it cannot rank capabilities authoritatively.

Views are authoritative as-of, historical replay or scenario. Node/edge effective intervals, assertion knowledge time and measurement phenomenon/result/ingestion times remain separate. Scenario results never feed authoritative actuals or benefit realization. Missing measurement is coded absence, never zero.

## Gap questions and acceptance scenario

Findings are attributable claims addressed to source owners: initiative without supported objective, objective without measurement or justified qualitative criterion, unresolved capability owner, and causal hypothesis without assessment. Each carries rule, subject, as-of, evidence and severity.

The acceptance map contains an initiative with no supported objective and an objective with no measure binding or justification. Both remain visible and produce owner questions. A project tagged `strategy` creates no support edge, outcome or benefit without basis, assessment and observations.

## Invariants

1. Every support link has an attributable evidence basis.
2. Objective and portfolio remain distinct.
3. Output, outcome and benefit remain distinct.
4. Tags, funding and completion never prove alignment or value.
5. Causal hypotheses require assessment before confirmation.
6. Contradicting claims remain visible with provenance.
7. Realized benefit requires qualified observations in its window.
8. Attribution shares do not exceed one per benefit and period.
9. Missing observations are coded absence, never zero.
10. Scenario results never become authoritative actuals.
11. Blocked or unallocated referents are never silently promoted.
12. The landscape mints no business identity and writes no source facts.

## Minimal profile shape

The view records class, as-of, horizon, scenario, referents with resolved/unallocated/blocked state, typed edges for support/contribution/constraint/measurement/causal hypothesis, evidence basis, confidence, interval and contradictions, plus owner-addressed findings and degradation reasons. Released views pin inputs and carry a reproducible fingerprint.

## Holds

All reused bases remain non-canonical drafts and several rely on single-provider waivers. Relationship contracts are absent. Strategy types and Outcome/Benefit are unallocated; WM-ACT-001 lacks a usable specification and its capability meaning may not meet EM-STR-03. Causal and attribution fixtures are missing. This checkpoint makes no canonical completeness, installability or publication claim.


## Initial Claude study
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


## Exact Grok response
Verdict: Accept the proposal with the constraints below. Neither the Strategy candidate nor the Outcome/Benefit candidate requires independent identity. Both are read-only profile/projection constructs. EM-LND-04 covers StrategyLandscape and StrategicAlignment and supplies no target model IDs; allocating a new business ID would invent mastership the landscape does not have.

Strongest evidence: The proposal treats tags, budgets, completion, and portfolio membership as non-probative for alignment and benefit, and it keeps unallocated and blocked referents visible. Missing measurements become owner-addressed findings rather than zeros. Alignment and causal confirmation are tied to assessment, observation, or attributable justified expert judgment, not to membership.

Strongest counterexample: A project that is tagged strategy, budgeted, completed, and a member of a portfolio, with no objective link and no assessment. If a view treated that tag, budget, completion, or membership as alignment or benefit, the proposal would fail. Under the proposal it remains visible and unaligned, and any output→outcome→benefit edge stays a hypothesis.

Identity/mastership: Neither candidate requires independent identity. StrategyLandscape and StrategicAlignment project existing masters only: objectives and targets on WM-KNW-011; measurements on WM-MAT-008 and WM-XCT-025; initiatives and hypotheses on WM-ACT-030; portfolio and project on WM-ACT-029/005; assessments on WM-ACT-034. Strategy and Outcome/Benefit remain unallocated. Reserved WM-ACT-001 Capability has no usable specification and is not a usable master. A profile element has no business identifier distinct from its source master element.

Strategic elements: Objectives and targets come from WM-KNW-011. Initiatives and hypotheses come from WM-ACT-030. Portfolio and project come from WM-ACT-029/005. A project tagged strategy is a tagged project, not a strategic element and not an alignment. An initiative with no objective remains an initiative and is shown as unlinked.

Alignment/causality: An alignment edge exists only when an assessment, an observation, or an attributable justified expert judgment names the pair. Absent that source, the landscape shows the elements as unassessed or unaligned. Causal output→outcome→benefit edges remain hypotheses until a method-bound assessment states the method, the evidence, and the result. Confirmation does not rewrite prior knowledge time. Tags, budgets, completion, and portfolio membership prove neither alignment nor benefit.

Output/outcome/benefit: Output is what an initiative or project produces on WM-ACT-030 or WM-ACT-029/005. Outcome is a change relative to an objective or target on WM-KNW-011. Benefit is a valued consequence of that outcome. None of the three is created by the profile. Outcome and Benefit stay unallocated projections. An unconfirmed chain is shown as a hypothesis, not as an established benefit.

Capability constraint: A constraining capability that points at reserved WM-ACT-001, which has no usable specification, remains visible and blocked. The constraint is not enforceable, not satisfied, and not dropped. No substitute specification is assumed.

Time/scenario: Views separate effective time, knowledge time, and measurement time, and separate authoritative, replay, and scenario classes. Replay reconstructs what was known at a knowledge time; it does not create alignment. A scenario may show a hypothesized alignment or benefit and must not overwrite the authoritative landscape or backdate knowledge.

Findings: An initiative without an objective is a visible gap, not an implied strategy link. An objective without a WM-MAT-008 or WM-XCT-025 measurement produces an owner-addressed finding, never a zero or an inferred score. A strategy-tagged project without an assessment is a non-alignment finding. Unallocated Strategy and Outcome/Benefit referents, and the blocked WM-ACT-001 referent, remain visible findings in every class.

Scenario: Initiative I has no WM-KNW-011 objective link. Objective O has no measurement. Capability C is constraining but blocked because WM-ACT-001 has no usable specification. Project P is tagged strategy, budgeted, completed, and a portfolio member, with no assessment. Expected: all four remain visible; none of tag, budget, completion, or membership creates alignment or benefit; the missing measurement is an owner-addressed finding, not zero; the capability constraint is blocked and unenforceable; any benefit edge stays a hypothesis; a scenario view may hypothesize a link but does not change the authoritative class.

Invariants:

1. Neither Strategy nor Outcome/Benefit profile allocates a new business ID.
2. A profile element has no business identifier distinct from its source master element.
3. Unallocated Strategy and Outcome/Benefit referents remain visible as unallocated.
4. A WM-ACT-001 referent with no usable specification remains visible as blocked.
5. An alignment edge exists only if sourced from an assessment, an observation, or an attributable justified expert judgment.
6. A tag does not prove alignment or benefit.
7. A budget does not prove alignment or benefit.
8. Completion does not prove alignment or benefit.
9. Portfolio membership on WM-ACT-029/005 does not prove alignment or benefit.
10. An output→outcome→benefit edge remains a hypothesis until a method-bound assessment confirms it.
11. An initiative on WM-ACT-030 may exist with no WM-KNW-011 objective and is then shown unlinked, not implicitly strategic.
12. An objective with no WM-MAT-008 or WM-XCT-025 measurement yields an owner-addressed finding, never a zero.
13. A constraining-but-blocked capability is recorded as unenforceable and is not deleted.
14. Effective time, knowledge time, and measurement time are distinct and are not collapsed.
15. Authoritative, replay, and scenario classes are distinct; scenario does not overwrite authoritative status.
16. Confirmation of a hypothesis does not rewrite history at an earlier knowledge time.

Minimum profile shape: A read-only projection that references only the listed master elements; an optional alignment slot typed as assessment, observation, or attributable justified expert judgment; a causality slot typed as hypothesis until a method-bound assessment confirms it; a visibility flag for unallocated and blocked; a time triple of effective, knowledge, and measurement; a class of authoritative, replay, or scenario; and a finding list. No independent Strategy or Benefit identifier.

Blockers: EM-LND-04 has no target model IDs, so the profiles cannot be bound to a new master. Strategy and Outcome/Benefit are unallocated, so a confirmed benefit has no master to land on beyond the confirming assessment. WM-ACT-001 is reserved and has no usable specification, so capability constraints cannot be evaluated. Any consumer that treats tag, budget, completion, or portfolio membership as proof violates the proposal.

