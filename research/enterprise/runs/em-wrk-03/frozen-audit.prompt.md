# Frozen semantic audit prompt — EM-WRK-03

You are the sole frozen semantic auditor for this contour. This audit is run exactly once. Use only the supplied text. Do not browse, call tools, invent identifiers, claim standards conformance or propose publication of blockers.

Audit the reconciled EM-WRK-03 boundary and its profile/fixture artifacts for internal contradictions, identity or mastership leaks, unsafe inference, underspecified lifecycle/version/time/evidence semantics, non-deterministic fixtures and missing publishability holds. Preserve the intended decision unless the supplied evidence disproves it: reuse WM-ACT-029 through a mandatory Program profile; keep ProgramComponent, Tranche and BenefitDependency program-owned; profile Transition Plan on WM-ACT-008; keep the Outcome / Benefit Realization dependency external and identifier-unassigned; allocate no runtime/model ID.

Return Markdown with: Verdict; numbered Material defects only; for each defect give exact deterministic remediation; Exact additional fixtures as a JSON array; and a final freeze decision. Be sceptical and concise. If there are no material defects, say so explicitly. Never request another provider run.

## LOCAL SYNTHESIS

```text
# EM-WRK-03 local synthesis

## Disposition

- Profile **Program** on the existing WM-ACT-029 Program / Portfolio aggregate and require the profile discriminator.
- Keep **Portfolio** as the sibling WM-ACT-029 profile with different admission and sequencing rules.
- Model ProgramComponent, Tranche and BenefitDependency as addressable program-owned assertions, not independent roots.
- Profile **Transition Plan** on WM-ACT-008 while WM-ACT-029 owns the program-specific readiness and handover bindings.
- Reuse WM-ACT-005 for project masters, WM-ACT-034 for acceptance and benefit reviews, WM-KNW-011 for objectives, WM-ACT-030 for upstream initiatives and WM-ORG-016 for assignments.
- Allocate no catalogue or runtime identifier.

## Identity and mastership

The Program root has independent aggregate identity. Component masters keep their own identifiers, owners, lifecycles, plans, baselines and evidence. WM-ACT-029 owns only membership, coordination, dependency, sequencing, governance and results-chain assertions.

ProgramComponent is a typed, effective-dated membership assertion. Removing it ends membership without closing or deleting the referenced component. A program lifecycle transition never cascades into component lifecycle state, and program governance cannot overwrite project baselines, actuals, task state or risk facts.

## Program, portfolio, project and initiative

A Program coordinates related components against a joint outcome and explicit benefit hypothesis. A Portfolio selects, prioritizes and balances investments; its members may be unrelated. Changing the discriminator is supersession with new identity, not an in-place conversion.

A Project owns its authorization and internal baseline. A Program coordinates across component boundaries without becoming a super-project. An Initiative is upstream change intent and mints a new identity when formalized as a program or project.

An arbitrary folder of projects fails both profiles when it has no joint benefit hypothesis, dependency graph, mandate, accountable owner, admission criteria or reserved decisions.

## Components, tranches and transition

Components may be projects, products, operations, campaigns or other governed work. Non-project components do not acquire project semantics.

A Tranche is a program-level sequencing band across components, ending in a program gate for continue, rebalance or stop. It is distinct from a project phase and cannot authorize a project phase transition.

A Transition Plan is an independently versioned WM-ACT-008 plan that binds a capability, receiving operational owner, readiness criteria, affected groups and handover. Operational acceptance is a separate authorized decision by the receiving owner. Sustainment obligations survive program closure and remain operationally mastered.

## Benefits, dependencies and attribution

Output, capability, outcome, benefit and disbenefit are separate facts. A BenefitDependency is a typed, directed, validity-bounded assertion between results-chain nodes or components. It does not become a standalone aggregate.

A joint benefit requires a falsifiable hypothesis, owner, baseline, target, indicator, period and realization plan. Attribution states method, uncertainty and causal limits. Adjudicated shares for one benefit and period must not exceed 1.0, and program-level and project-level reporting must not double count the same benefit.

The Outcome / Benefit Realization aggregate required as the external benefit master remains identifier-unassigned.

## Governance, time and closure

Program governance owns mandate, governance model, membership changes, sequencing, allocation within its envelope, thresholds, assurance and program gates. Component authorization, baselines and internal gates remain component-owned. Escalation references a decision; it does not transfer mastership.

Planned, decision, event, effective, observation, ingestion and knowledge time remain distinct. Released mandates, memberships, allocations, plans, decisions and observations are immutable and corrected by successors.

Program closure records handover, benefit owner and residual obligations. It does not imply that every component is closed or that a benefit is realized. A program may close while benefits remain forecast and under operational observation.

## Acceptance result

Program PGM-1 contains projects P-A and P-B plus transition to operation OPS-1. Benefit B-J depends on both project outputs and sustained operational adoption. P-A closes first; its membership ends, but B-J remains forecast with `measurement-pending` because project closure proves neither outcome nor benefit. P-B continues. The program tranche gate does not affect either project's phase gates. OPS-1 later accepts the pinned transition-plan release; realization observations start only after adoption. Attribution remains unadjudicated until shares reconcile, and a support-load increase is recorded separately as a disbenefit.

## Required invariants

1. Exactly one WM-ACT-029 profile discriminator is present.
2. Program components are not limited to projects.
3. Membership never transfers component mastership.
4. Program lifecycle changes do not cascade to component masters.
5. Project closure proves neither outcome nor benefit.
6. Output, outcome, benefit, disbenefit and attribution remain separate.
7. A joint benefit has an explicit falsifiable hypothesis.
8. Adjudicated attribution shares do not exceed 1.0 per benefit and period.
9. Program and project views do not double count one benefit.
10. A tranche gate is not a project phase gate.
11. Transition plan, operational acceptance and sustainment remain distinct.
12. Released assertions are immutable and superseded explicitly.
13. An arbitrary container is neither a Program nor a Portfolio.

## Holds

The external Outcome / Benefit Realization master has no registry allocation. WM-ACT-029 is recorded with WM-ACT-005 as both parent and contained model, creating a containment contradiction that must be resolved. Relevant relation rows remain unapproved, and reused bases remain non-canonical drafts with source and provider holds. No installability or publication-readiness claim is made.

```

## CLAUDE FROZEN STUDY

```text
# EM-WRK-03 — Independent Adjudication

## Verdict
Reuse WM-ACT-029 under a required **Program** profile; add no new model root. Disposition of candidates: **Program** → reuse WM-ACT-029 (profile-discriminated). **ProgramComponent** → membership assertion owned by WM-ACT-029; addressable, not a master. **Tranche** → program-scoped sequencing band inside WM-ACT-029's roadmap layer; addressable, not a master. **BenefitDependency** → typed link inside WM-ACT-029's results-chain; addressable, not a master. **TransitionPlan** → profile of WM-ACT-008 (plan identity and versioning) plus program-scoped readiness/handover assertions in WM-ACT-029. No identifiers allocated. Boundary decision: **reuse + profile**, with two blocking gaps (§Holds).

## Evidence
WM-ACT-029 already owns, as first-class findings, component membership and dependency, results chain with disbenefit and attribution limits, roadmap/tranche/horizon, transition and sustainment, and lifecycle/closure — the exact surface of the five candidates. Its `out_of_scope` and `policies` already state that component, benefit, operation and observation masters stay external, that profile is mandatory, and that completion or spending does not prove realization. Its declared `adversarial_checks` already reject the negative case. The contour's three proposed invariants are therefore restatements of existing WM-ACT-029 rules, not grounds for new types.

## Identity/mastership
Independent identity is required for: the Program root (source-qualified aggregate identifier), each membership/priority/lifecycle **event** (immutable, provenance-bearing), each results-chain node and link assertion, and the transition **plan** (WM-ACT-008 masters plan identity and is independently versioned per the frozen relation set). Independent identity is **not** required for ProgramComponent, Tranche or BenefitDependency as model roots: each is an assertion whose identity is `{program-id}--{artifact-kind}--{assertion-id}`, valid only inside one aggregate. Component masters (WM-ACT-005 projects, operations, products) keep their own identity, owner, lifecycle, plan and evidence; PPM/tracker masters them, not the program.

## Program vs Portfolio
One root, one mandatory profile, profile-specific rules. Program = related components coordinated for a joint outcome with an explicit benefit hypothesis and inter-component dependency; sequencing is dependency-led. Portfolio = strategy-aligned selection, prioritization and balancing; components need not be related. Profile change is supersession with new identity, never an in-place update. **Negative case rejected:** a folder of unrelated projects has no joint benefit hypothesis and no dependency graph, so it fails the program guard; absent mandate, accountable owner, selection criteria and reserved decisions it also fails the portfolio guard — it is a tracker container, not either. Against WM-ACT-005: a project has one authorization instrument and one baseline set; a program has no baseline over component internals. Against WM-ACT-030: an Initiative is pre- or cross-formal change intent whose formalization **mints new identity**; a program is a formalization target, never a renamed initiative.

## Components/membership
Membership is an appended, source-qualified event with basis, authority, effective interval and expected revision. It never absorbs or rewrites the component master. Components are not restricted to projects: operations, products, campaigns and non-project work packages are admissible, and non-project components carry no WM-ACT-005 baseline. Removal ends membership without cascading to the component's lifecycle; program termination or closure never closes, cancels or deletes a member. The program owner may not assert component baselines, task states, actuals or risk facts — those remain WM-ACT-005/WM-ACT-008 assertions referenced by identity.

## Tranches/transition
A **tranche** groups work across several components into a program-level sequencing band terminated by a program gate whose reserved decision is continue / rebalance / stop. A **project phase** is an intra-project lifecycle stage with its own entry/exit criteria and gate authority owned by WM-ACT-005. A tranche gate does not authorize a project phase transition and a completed phase does not close a tranche. A **TransitionPlan** is a versioned intention (WM-ACT-008) to hand a capability to a named operating owner: readiness, affected groups and adoption are program-scoped; **operational acceptance** is a separate decision by the receiving operation owner, evidenced via acceptance/assessment records (WM-ACT-034 profile); **sustainment** obligations survive program closure and belong to the operation master.

## Benefits/dependencies/attribution
Four separable assertion classes. **Output/capability** — delivered by a component. **Outcome** — asserted change in a subject's state. **Benefit/disbenefit** — governed claim over outcomes with owner, baseline, target, indicator, period and realization plan. **Causal claim** — hypothesis (falsifiable, in the results chain), dependency (typed, directed, validity-bounded link between chain nodes or components), and attribution (contribution share with method, uncertainty and declared causal limit). Adjudicated shares for one benefit and period must not exceed 1.0 and must not be double-counted between the program and its constituent projects. Benefit masters are external and currently **unallocated** (see Holds).

## Governance/decision rights
The program owns mandate, governance model, reserved decisions, thresholds, assurance, gates, membership changes, sequencing and allocation within its envelope. It does not own component authorization instruments, component baselines or component gate outcomes. Escalation from a component to the program is a referenced decision, not a transfer of mastership. Agent operations affecting membership, allocation, lifecycle, protected disclosure or disposition require delegated authority.

## Time/version/closure
Planned, decision, event, effective, observation, ingestion and knowledge times stay distinct. Released mandates, memberships, allocations, plans, decisions and observations are immutable; corrections are successors. Program closure is an authorized lifecycle event recording outcome, handover, benefit owner and residual obligations — it is neither project closure nor benefit realization, and a program may close with benefits still forecast.

## Acceptance scenario
PGM-1 (Program profile), components P-A and P-B (WM-ACT-005) plus transition to OPS-1. Joint benefit B-J depends on outputs from both plus sustained adoption. P-A closes at T1 with outcome classified and membership ended; B-J remains `forecast` with an explicit `measurement-pending` absent-reason — closure emits no realization assertion. P-B continues; its tranche gate is decided at program level while its phase gates stay with its own governing body. At T2 the transition plan release reaches operational acceptance by OPS-1; realization observations begin only after adoption, with phenomenon time distinguished from result time. Attribution across P-A and P-B remains unadjudicated until shares reconcile. A rise in support contacts is recorded as a disbenefit, not netted.

## Invariants
1. Exactly one profile per root; ambiguity fails validation. 2. Components are not restricted to projects. 3. Membership ≠ mastership; the program owner does not own component facts. 4. Program lifecycle changes never cascade to component masters. 5. Project closure proves neither outcome nor benefit. 6. Output, outcome, benefit, disbenefit and causal attribution are separate assertions. 7. A joint benefit requires an explicit, falsifiable hypothesis. 8. Adjudicated attribution shares ≤ 1.0 per benefit and period; no program/project double counting. 9. A tranche gate is not a project phase gate. 10. Transition plan ≠ operational acceptance ≠ sustainment. 11. Released assertions are immutable; history is never rewritten. 12. An arbitrary container is not a program.

## Minimal model set
WM-ACT-029 (Program profile) · WM-ACT-005 · WM-ACT-008 (transition/roadmap plans) · WM-ACT-034 (acceptance/benefit review) · WM-KNW-011 (objectives/targets) · WM-ACT-030 (upstream initiative, derivation only) · WM-ORG-016 (program-scoped assignments) · the unallocated Outcome/Benefit Realization and Metric Definition referents named in prior EM-STR-02/EM-DAT-05 work.

## Holds
Blocking: (a) the benefit master WM-ACT-029 externalizes is **unallocated**, so benefit logic terminates in a dangling reference; (b) the frozen registry lists `vr.wm-act-029` with `parent_ids = WM-ACT-005` **and** `contains_ids = WM-ACT-005` — a circular containment contradicting WM-ACT-005's rule that the edge is asserted parent-side only. Further: all relation rows unapproved; WM-ACT-029 and WM-ACT-030 are single-provider-waiver drafts with no independent review; `publishableCanonical` false throughout; ISO support is abstract-level only; retention/access rules are unsourced house policy; the programme/program token is unnormalized; the Program/Portfolio split remains deferred. No canonical completeness, installability or publication-readiness is claimed.

```

## EXACT GROK RESPONSE

```text
**Verdict.** Conditionally accept the proposal as a modeling stance. Do not allocate a new identifier. Do not claim publication readiness. Profile Program on WM-ACT-029 with a mandatory discriminator; retain Portfolio as the sibling profile on the same root; treat ProgramComponent, Tranche and BenefitDependency as addressable program-owned assertions; profile TransitionPlan on WM-ACT-008; keep readiness/handover bindings on WM-ACT-029; keep component mastership external.

None of the five candidates needs an independent root. The Outcome / Benefit Realization master remains unresolved. The WM-ACT-029↔WM-ACT-005 relation is membership-via-assertion, not identity containment. If adjacent WM-ACT-029 text still says a program “contains” projects, that wording is the contradiction to break, not authority. EM-WRK-03 does not rewrite WM-ACT-005.

**Strongest evidence.** Program and Portfolio share a governed-collection envelope (authorization, strategy binding, collection of work). The difference is organizing principle — joint outcome coordination versus investment balance — which a mandatory discriminator can carry without a new type family. External mastership is the only reading that preserves WM-ACT-005 Project identity when a project participates in a program. ProgramComponent, Tranche and BenefitDependency have no commissionable life outside a Program instance. The required test scenario is expressible with the named roots plus those owned assertions.

**Strongest counterexample.** If WM-ACT-029 inherits or declares identity containment of WM-ACT-005, then “profile Program on 029” and “component mastership stays external” cannot both be true. Profiling cannot cancel inherited containment. Secondary stress: a project in two programs. Dual ProgramComponent rows can record membership; BenefitDependency attribution cannot be inferred from dual membership. An arbitrary folder of unrelated projects is not a counterexample against the proposal; it is a rejection target the proposal must pass.

**Identity / mastership.** Program identity is a WM-ACT-029 instance with discriminator=Program, in the same identity space as Portfolio. The discriminator is mandatory, not nullable, and not silently flipped. Project identity is mastered only under WM-ACT-005; Initiative under WM-ACT-030; Goal/Objective under WM-KNW-011; Assessment/Evaluation under WM-ACT-034. WM-ORG-016 Work Assignment binds actors; it confers neither program nor component identity. Program masters its profile record; its ProgramComponent, Tranche and BenefitDependency assertions; and the WM-ACT-029 bindings that attach a TransitionPlan and readiness/handover conditions. Program does not master Project, Initiative, Goal/Objective, Assessment, operational service, or sustainment organization. ProgramComponent identity is not component identity: the assertion is owned by the Program and points at an external master.

**Independent root.** None. Program is a WM-ACT-029 profile. TransitionPlan is a WM-ACT-008 profile. The three assertions are owned parts of the Program profile. Promoting Tranche onto WM-ACT-008 was considered and rejected: a tranche slices capability delivery and membership; the schedule is a different object. Creating a root for BenefitDependency to stand in for the missing Outcome/Benefit Realization master would be a category error.

**Outcome / Benefit Realization master.** Unresolved, and must stay unresolved inside EM-WRK-03. BenefitDependency is not that master. If Program mastered realization, realization could not outlive program closure — contradicting program-closure ≠ benefit-realization. If Project mastered realization, a joint benefit across two projects would have no home — failing the test scenario. WM-KNW-011 holds intended aims, not realized benefit. WM-ACT-034 holds evaluation events, not durable benefit identity. Realization evidence may reference WM-ACT-034; intended aims may reference WM-KNW-011. A durable benefit identity is out of scope and absent from the adjacent set.

**WM-ACT-029↔WM-ACT-005 containment.** There is no containment. Lawful relation: a ProgramComponent assertion owned by the Program, referencing an externally mastered WM-ACT-005 (and, if asserted, WM-ACT-030). No minting, no nesting, no exclusive default. Containment would transfer mastership or lifecycle to the Program, make Program an arbitrary folder, prevent a project from closing while the program stays open, cascade program closure onto projects, and forbid a shared contributor. The test scenario requires the opposite.

**Program vs Portfolio.** Shared root, disjoint profiles. Program is a temporary outcome-delivery vehicle: intended-benefit targets, tranche sequence, transition bindings, membership assertions. It ends when the program is closed (realized, curtailed, or absorbed), not when the last project ends. Portfolio is the sibling profile: standing or cyclic investment-balance structure. It selects and prioritizes work. It does not own a single joint benefit, a tranche-of-change, or a single operational transition. Portfolio membership is not ProgramComponent. Program ≠ Project (WM-ACT-005 masters outputs). Program ≠ Initiative (WM-ACT-030 is the authorized change thrust, not the multi-component delivery vehicle). Program ≠ arbitrary container.

**Components / membership.** ProgramComponent records membership, role-in-program, and contribution window. Membership ≠ containment ≠ mastership. Dropping membership does not close the component. Closing the component does not erase the historical assertion. A project may sit in a Portfolio and a Program at once; neither assertion moves WM-ACT-005 mastership. The program cannot rewrite project scope, schedule, or closure state except by reference.

**Tranches / transition.** Tranche is a program-owned assertion: a planned increment of program capability/outcome. It may span several members. It is not a WM-ACT-005 project phase and not a WM-ACT-008 activity. TransitionPlan profiles WM-ACT-008 for sequence, dates and predecessors. Program-specific readiness and handover bindings stay on WM-ACT-029 so the plan profile is not overloaded with program authority. TransitionPlan ≠ operational acceptance (evaluative decision, WM-ACT-034). TransitionPlan ≠ sustainment (post-handover BAU ownership, outside program mastership). Existence of a plan is not handover. Bindings are references, not a second copy of the plan.

**Benefits / dependencies / attribution.** Output (component deliverable) ≠ outcome (changed operational state) ≠ benefit (measurable advantage). BenefitDependency is a program-owned assertion that an intended benefit requires specified members, outputs, other benefits, or a tranche increment. It is not the benefit, not a causal hypothesis, and not attribution. Causal claims sit at most with WM-KNW-011 as target statements. Attribution is an after-the-fact WM-ACT-034 judgment. Membership does not imply attribution.

**Governance.** Program authority ≠ project authority ≠ portfolio authority. WM-ORG-016 assigns roles to program, member, tranche or transition work and never transfers mastership. Program gates: tranche authorization, transition readiness binding, program-closure decision. These are distinct from WM-ACT-005 stage gates and from Portfolio investment gates. Readiness, acceptance and realization assessments are WM-ACT-034 instances pointing at program assertions; they are not ProgramComponents.

**Time / version / closure.** Program lifecycle is independent of each member’s lifecycle. Component closure ≠ program closure ≠ benefit-realization closure. Tranche completion ≠ program completion. Program closure does not close remaining members and does not require benefits realized. After program closure, realization tracking cannot hang on the closed Program as master. Version the Program profile, each assertion kind, and each TransitionPlan independently. Historical assertion rows survive member closure and program closure.

**Scenario — accept.** Program Omega, WM-ACT-029 discriminator=Program. Joint benefit: cycle-time reduction (not an output). Project Alpha (WM-ACT-005): intake service. Project Beta (WM-ACT-005): rules engine. ProgramComponent assertions owned by Omega point at Alpha and Beta; mastership remains WM-ACT-005. Tranche T1 = Alpha delivery plus partial operational handover. Tranche T2 = Beta delivery plus joint enablement. T1 is not an Alpha phase. TransitionPlan (WM-ACT-008 profile) schedules handover; operational acceptance and later sustainment are distinct events. BenefitDependency D: joint benefit requires Alpha output and Beta output and operational adoption. D is a dependency assertion, not a causal hypothesis and not attribution. At Alpha close: Alpha closed; Omega open; D unsatisfied; TransitionPlan incomplete; benefit unrealized. This shows program closure ≠ component closure ≠ benefit realization, and output ≠ outcome/benefit.

**Scenario — reject.** Label “Digital Stuff” grouping a website refresh and a warehouse move. No joint benefit, no BenefitDependency, no tranche spanning a shared outcome, no TransitionPlan binding. Discriminator may say Program; invariants fail. Not a Program. Not a Portfolio substitute either: no investment-balance thesis. Route the bag out of Program.

**Invariants.**
1. Every WM-ACT-029 Program instance has discriminator=Program; the Portfolio sibling has discriminator=Portfolio; the profiles are disjoint.
2. A Program is not a WM-ACT-005 Project, not a WM-ACT-030 Initiative, and not an unlabeled collection.
3. ProgramComponent never masters the member; member identity remains on its own root.
4. WM-ACT-029 does not contain WM-ACT-005 as child identity.
5. A Program must reference at least one intended outcome/benefit target; absent that target it is not a Program.
6. BenefitDependency asserts required contribution, not realized attribution and not a causal hypothesis.
7. Tranche is not a project phase and need not coincide with any member’s lifecycle.
8. TransitionPlan profiles WM-ACT-008; readiness/handover bindings remain on WM-ACT-029.
9. Existence of a TransitionPlan does not equal operational acceptance or sustainment.
10. Closure of one member does not close the Program or close benefit realization.
11. Program closure does not close remaining members and does not imply benefits realized.
12. Portfolio membership does not create Program membership, and vice versa.
13. WM-ORG-016 assignment does not move mastership.
14. Historical ProgramComponent, Tranche and BenefitDependency rows survive member closure and program closure.
15. Joint benefit may remain open after a contributing project has closed.
16. Membership does not imply attribution, including when a member appears in two programs.

**Minimum model set (no new ID).** WM-ACT-029 Program profile and sibling Portfolio profile with mandatory discriminator. Program-owned addressable assertions: ProgramComponent, Tranche, BenefitDependency. WM-ACT-008 TransitionPlan profile. WM-ACT-029 readiness/handover bindings. External member minimum: WM-ACT-005 Project. Referenced, not mastered here: WM-KNW-011 (intended targets), WM-ACT-034 (readiness, acceptance, realization evidence), WM-ORG-016, WM-ACT-030 as origin only.

**Blockers.**
1. Hard: WM-ACT-029↔WM-ACT-005 containment. Adjacent 029 text must be read, or rewritten in its own draft, as membership/participation. Until that is explicit, external mastership is fiction.
2. Hard: Outcome / Benefit Realization master remains missing. Do not assign it to WM-ACT-029, to BenefitDependency, or to any candidate in this set. Do not invent a code.
3. Soft: “Addressable program-owned assertions” must mean owned identifiable parts of the 029 Program profile, not new WM-* roots. A later reading that addressability requires new codes violates “do not allocate a new identifier.”
4. Soft: TransitionPlan structure on 008 plus bindings on 029 works only if both are addressable from the same governance gate and bindings are references, not a duplicate plan.
5. Soft: Program vs Initiative (WM-ACT-030) needs the stated rule — Initiative = change intent; Program = coordinated multi-component delivery vehicle — or the same work is double-booked.
6. Soft: discriminator-only is too weak if adjacent WM-ACT-029 still treats Program and Portfolio as the same unconstrained bag. Disjoint invariants must sit in the profiles, not only in a flag.
```

## PROVIDER COMPARISON

```text
# EM-WRK-03 provider comparison

Claude and Grok agree on the primary boundary: reuse WM-ACT-029 through a mandatory Program discriminator, retain Portfolio as a disjoint sibling profile, keep ProgramComponent, Tranche and BenefitDependency as addressable program-owned assertions, profile Transition Plan on WM-ACT-008, preserve every component master and allocate no new identifier.

Both reviews separate Program from Portfolio, Project, Initiative and an arbitrary tracker container. They also agree that membership never transfers mastership; a tranche is not a project phase; a transition plan is not operational acceptance or sustainment; outputs, outcomes, benefits and attribution are different assertions; and component closure, program closure and benefit realization are independent lifecycle facts.

Grok sharpens two constraints. First, the WM-ACT-029 to WM-ACT-005 edge must be membership through ProgramComponent, never child-identity containment. A profile cannot cancel inherited containment, so the frozen registry contradiction remains a hard canonical hold. Second, BenefitDependency cannot substitute for the missing durable Outcome / Benefit Realization master. The prior EM-STR-02 checkpoint supplies an identifier-unassigned candidate, but EM-WRK-03 must treat it as an external unresolved dependency and must not allocate or master it.

The reconciled profile therefore requires a non-null immutable discriminator, at least one intended outcome or benefit target, non-cascading membership, historical assertion retention, independent versioning of program assertions and transition plans, and explicit references rather than duplicated plan or component facts. Readiness, acceptance and realization judgments reuse WM-ACT-034; role assignments reuse WM-ORG-016 without changing authority or mastership.

Publication remains held by the parent/containment contradiction, the unallocated Outcome / Benefit Realization dependency, unapproved relation rows and non-canonical base drafts. The result is a reviewable no-ID profile dossier with no installability or publication-readiness claim.

```

## PROFILE CANDIDATE

```json
{"format":"vercy-enterprise-profile-candidate/v1","contourId":"EM-WRK-03","name":"Enterprise Program and Benefit Coordination","decision":"PROFILE","newRuntimeId":false,"bases":["WM-ACT-029","WM-ACT-005","WM-ACT-008","WM-ACT-034","WM-KNW-011","WM-ACT-030","WM-ORG-016"],"constraints":["Program profiles WM-ACT-029 with a mandatory discriminator and remains distinct from its Portfolio sibling.","ProgramComponent, Tranche and BenefitDependency are effective-dated program-owned assertions and never independent roots.","Membership never transfers component mastership or cascades program lifecycle state into a project, product or operation.","Transition Plan profiles WM-ACT-008 while operational acceptance and sustainment remain separately authorized and mastered.","Output, capability, outcome, benefit, disbenefit and attribution remain distinct; Outcome / Benefit Realization reuses the existing EM-STR-02 candidate.","Project closure, program closure and benefit realization never imply one another.","A tranche gate coordinates program sequencing and never authorizes a project phase transition.","Released mandates, memberships, allocations, plans, decisions and observations are immutable and superseded explicitly."],"holds":["WM-ACT-029 and WM-ACT-005 parent/containment contradiction requires canonical resolution.","Relevant relation rows and reused non-canonical bases remain under review.","Independent Grok review and one frozen semantic audit are pending."]}

```

## FIXTURES

```json
{"format":"vercy-enterprise-profile-fixtures/v1","profileName":"Enterprise Program and Benefit Coordination","cases":[{"id":"two-project-transition","kind":"positive","input":"A program contains two projects and an operational transition tied to one joint benefit.","expect":"Membership, project mastership, transition acceptance and benefit observation remain distinct."},{"id":"project-closes-first","kind":"positive","input":"One project closes while the other continues and the joint benefit is measurement-pending.","expect":"Project closure ends its membership as appropriate but proves neither outcome nor benefit."},{"id":"post-program-benefit","kind":"positive","input":"The program closes after handover while operational benefit observations continue.","expect":"Residual ownership and realization remain externally mastered and observable."},{"id":"arbitrary-folder","kind":"negative","input":"An unrelated folder of projects is labelled a program without mandate, joint hypothesis or dependency graph.","expect":"The Program profile is rejected."},{"id":"membership-transfers-mastership","kind":"negative","input":"Adding a project lets program governance overwrite its baseline and actuals.","expect":"The mutation is rejected."},{"id":"tranche-gate-closes-project-phase","kind":"negative","input":"A program tranche decision automatically advances a project phase.","expect":"The cascade is rejected."},{"id":"double-count-benefit","kind":"negative","input":"The same realized benefit is counted in both project and program totals.","expect":"The duplicate attribution is rejected."}]}

```
