# Frozen semantic audit prompt — EM-WRK-04

You are the sole frozen semantic auditor for this contour. This audit is run exactly once. Use only the supplied text. Do not browse, call tools, invent identifiers, claim standards conformance or propose publication of blockers.

Audit the reconciled EM-WRK-04 boundary and allocation/profile/fixture artifacts for internal contradictions, identity or mastership leaks, unsafe inference, underspecified lifecycle/version/time/evidence semantics, non-deterministic fixtures and missing publishability holds. Preserve the intended decision unless the supplied evidence disproves it: profile Portfolio on WM-ACT-029; keep PortfolioComponent, Prioritization, InvestmentAllocation and PortfolioScenario portfolio-owned; retain one independently identified but identifier-unassigned Selection Criteria Set candidate; allocate no catalogue, model or runtime ID.

Return Markdown with: Verdict; numbered Material defects only; for each defect give exact deterministic remediation; Exact additional fixtures as a JSON array; and a final freeze decision. Be sceptical and concise. If there are no material defects, say so explicitly. Never request another provider run.

## LOCAL SYNTHESIS

```text
# EM-WRK-04 local synthesis

## Disposition

- Profile **Portfolio** on WM-ACT-029 under the mandatory Program / Portfolio discriminator; create no portfolio root.
- Treat PortfolioComponent, Prioritization, InvestmentAllocation and PortfolioScenario as addressable, effective-dated releases owned by the Portfolio aggregate.
- Propose an identifier-unassigned **Selection Criteria Set** root because a released set may be reused across portfolios and review cycles and must remain resolvable after portfolio closure.
- Reuse WM-ACT-005 for project masters, WM-ACT-030 for initiatives, the Program profile for program components, WM-ECO-012 for budget authority, WM-KNW-011 for objectives and the decision triad for scenario approval.
- Allocate no catalogue or runtime identifier.

## Identity and mastership

Portfolio identity persists through component turnover, criteria revisions, strategy changes and rebalances. Components retain their own identity, owner, lifecycle, baseline, actuals and evidence. Portfolio-owned assertions describe admission, ranking, allocation and scenario selection without changing the component master.

PortfolioComponent is a typed, source-qualified and effective-dated membership assertion. One component may belong to multiple portfolios, each with a different admission basis and declared share. Ending membership never closes or cancels the component.

The Selection Criteria Set has independent identity, version lifecycle and reuse across portfolios. Individual criteria, weights and constraints are contained in a released set. Observations and metric definitions remain external.

## Portfolio boundaries

A Portfolio selects, prioritizes and balances investments against strategy and constraints. Its components may be unrelated. A Program coordinates related components around a joint outcome and benefit hypothesis. A catalogue indexes items without mandate, reserved decisions, allocation or lifecycle. A Project owns its authorization and baseline. An Initiative remains upstream change intent; portfolio membership does not formalize it into delivery identity.

Portfolio membership creates no dependency, shared outcome or program semantics. Program and Portfolio profile changes require supersession with new identity.

## Criteria, scoring and prioritization

Criterion definition, weighting, observed score and prioritization release are separate. A criterion pins measure reference, scale, unit, preference direction and mandatory or compensatory status. A score cites source, observation period, method, denominator, quality and uncertainty.

A prioritization release pins the portfolio, criteria-set version, weighting version, candidate set, comparison period and authority. Rank belongs to that release and is never written as an intrinsic property of the component. Rankings from incompatible pins are not compared as if they shared one scale.

Alternative comparison includes constraints and a do-nothing comparator or justified exception. Product and project investments use a common period and incremental cost/value basis; continuous product investment acquires no artificial completion date.

## Allocation and funding

InvestmentAllocation is portfolio-scoped intent within an approved envelope. It is distinct from budget authority, funding availability, commitment, obligation, accounting actual and component funding.

Every allocation declares source, destination, amount or share, currency, price base, valuation basis, interval, restrictions, authority and residual rule. Allocations against one released source and period may not exceed the source amount. Residuals reconcile, and consolidated reporting counts the component once while each portfolio reports only its declared share.

## Scenarios and decisions

PortfolioScenario is an immutable hypothesis release containing candidate composition and allocations under stated assumptions, horizon and capacity constraints. It is neither an actual nor an approved baseline.

Selection requires separate rationale, authorized decision occurrence and issued record. The resulting composition-and-allocation baseline is a distinct immutable release. Capacity is tested at scenario level; the highest-ranked set need not be selected, and any divergence requires recorded rationale.

Strategic alignment is an evidence-bearing contribution claim. It does not establish causality or prove benefit realization.

## Governance, time and rebalance

Portfolio governance owns mandate, admission/removal, criteria adoption, weighting, scenario selection, allocation within its envelope, thresholds and assurance. Component authorization and internal gates remain component-owned.

Planned, decision, event, effective, observation, ingestion and knowledge times remain distinct. Memberships, criteria pins, rankings, allocations and scenarios are effective-dated and immutable after release.

Review cadence combines a declared interval with event triggers such as funding change, constraint breach, defeated assumption, strategy restatement or authority change. Rebalance is an authorized lifecycle event that produces successor composition and allocation releases without rewriting history.

## Acceptance result

PF-1 and PF-2 both admit initiative INI-1 with shares 0.6 and 0.4 from distinct released funding sources. Each membership and allocation is independent and neither converts INI-1 into a project. PF-1 selects scenario SC-3, pinning criteria set CS-v2, weighting W-v1, candidates, horizon, price base and capacity. Decision D-7 approves it and issues REC-7. Later score or criteria revisions create successors; SC-3, D-7 and REC-7 remain reproducible. Consolidated reporting counts INI-1 once and no source is exceeded. Unrelated PF-1 components do not become a Program.

## Required invariants

1. Exactly one WM-ACT-029 profile discriminator is present.
2. Portfolio components need not be related.
3. Membership never transfers component mastership.
4. Portfolio lifecycle changes never cascade to component masters.
5. One component may belong to multiple portfolios.
6. Criteria, weighting, observations and ranking releases remain distinct.
7. Rank is release-scoped, never intrinsic to work.
8. Comparisons pin criteria, horizon, price base and metric revisions.
9. Portfolio allocation is distinct from authority, commitment and actuals.
10. Released source amounts are not exceeded and residuals reconcile.
11. A scenario is neither an actual nor an approved baseline.
12. Baseline approval requires an authorized decision.
13. Alignment does not prove causal benefit.
14. Rebalance creates successors and preserves history.
15. Portfolio membership does not imply Program semantics.

## Holds

Selection Criteria Set has no registry allocation. Metric Definition, Outcome / Benefit Realization, Product, Operation, Resource / Capacity and several funding referents also remain unallocated. WM-ACT-029 records WM-ACT-005 as both parent and contained model, while WM-ACT-030's project parent conflicts with initiative-is-not-project semantics. Relation rows are unapproved and reused bases remain non-canonical drafts with source and provider holds. No installability or publication-readiness claim is made.

```

## CLAUDE FROZEN STUDY

```text
# EM-WRK-04 — Portfolio and Investment Selection (independent adjudication)

## Verdict
- **Portfolio** — *reuse + profile*. Profile `Portfolio` on WM-ACT-029, sibling to the `Program` profile taken in EM-WRK-03, under the required discriminator. No new root.
- **SelectionCriterion** — *new, independent identity required*, as a versioned **criteria set** external to any one portfolio. Identifier unassigned.
- **PortfolioComponent**, **Prioritization**, **InvestmentAllocation**, **PortfolioScenario** — *profile as addressable, effective-dated, immutable releases contained in the Portfolio root*. None has independent identity.
- Reuse WM-ACT-005 (project), WM-ACT-030 (initiative), WM-ACT-029/`Program` (program-as-component), WM-ECO-012 (budget), WM-KNW-011 (objectives), WM-KNW-010 / WM-ACT-024 / WM-REC-010 (rationale, occurrence, issued record). No catalogue or runtime identifier allocated.

## Evidence
WM-ACT-029 (complete spec, sha256 3ce9e40…, `aggregate`, reviewable-draft) already owns membership, dependency, prioritization, allocation, lifecycle and evaluation as root-owned assertions with all masters external, and explicitly rejects portfolio-as-registry. Its `prioritize-balance-sequence-and-reallocate` function names criteria, weights, constraints and scenarios as inputs and ranking/sequence/allocation as outputs; `admit-or-remove-component` requires criteria, authority, effective interval. Its own policy states portfolio components *need not be related*. That is a complete fit for this contour; the residual work is profile rules, not a new aggregate.

## Identity/mastership
Portfolio identity persists across component turnover, criteria revisions, rebalances and strategy restatement. Component masters keep their own identifiers, owners, lifecycles, plans, baselines and evidence; the Portfolio owns only assertions *about* them. A criteria set survives the portfolios and cycles that cite it, is reused across both, and must remain resolvable after a portfolio closes — hence independent identity. Rankings, memberships, allocations and scenarios cannot exist outside the portfolio and its cycle, so they are contained. A `Program`↔`Portfolio` profile change is supersession with new identity, never an in-place update.

## Portfolio boundaries
A **Program** coordinates related components toward a joint outcome and benefit hypothesis; a **Portfolio** selects, prioritizes and balances investments against strategy and constraints, and its members may be mutually unrelated. A **catalogue** is an index: no mandate, no reserved decision rights, no benefit logic, no lifecycle. A **project** owns its own authorization and baseline; a portfolio never becomes a super-project. An **initiative** is upstream change intent; portfolio membership neither formalizes it nor mints delivery identity. Membership in one portfolio implies no program semantics, no dependency, no shared outcome and no joint governance.

## Components/membership
`PortfolioComponent` is a typed, source-qualified, effective-dated membership assertion carrying component reference and type, admission basis, criteria-set version, portfolio role, share basis and component owner. Components may be projects, initiatives, programs, products or operations; non-project components acquire no project semantics. Removal ends membership only — it does not close, cancel or delete the master. Portfolio lifecycle transitions never cascade to component lifecycle, baselines, actuals or risk facts. One component may be a member of several portfolios simultaneously.

## Criteria/scoring/prioritization
Three separable layers. (1) **Criterion definition**: measure reference (external Metric Definition — unallocated), unit, scale, preference direction, mandatory-versus-compensatory class; released immutably in a versioned set. (2) **Observed score**: a source-qualified observation with period, method, denominator, quality and uncertainty, mastered by the observation/dataset model and referenced, never rewritten into the criterion or the component. (3) **Prioritization**: an immutable release pinning portfolio, criteria-set version, weighting scheme version, candidate set, period and authority, yielding a rank. Rank is a property of that release, not of the work: it is never written onto the component master and never compared across releases with different pins. Ordinal bands and incommensurable value/harm dimensions are not netted arithmetically without a declared method.

## Allocation/funding
`InvestmentAllocation` is a portfolio-scoped intent inside an approved envelope: it is not budget authority (WM-ECO-012 authorization), not release/availability, not a commitment or obligation, not an accounting actual, and not the component's own funding. Each allocation declares funding-source reference, destination component, amount or share with currency, price base and valuation basis, effective period, restrictions, authority and residual rule. Double funding is prevented source-side: allocations drawn on one released funding source and period cannot exceed its released amount, residuals must reconcile, and aggregate reporting counts a component's cost and expected benefit once, with each portfolio reporting only its declared share.

## Scenarios/decisions
`PortfolioScenario` is an immutable hypothesis release: a candidate composition plus allocation under stated capacity constraints, varied assumptions and method, optionally citing an external strategic scenario. It is never an authoritative actual, baseline or target. A scenario becomes the **approved baseline** only through a separate authorized decision — rationale (WM-KNW-010), occurrence (WM-ACT-024), issued record (WM-REC-010) — producing a distinct composition-and-allocation release. Alternative comparison pins one criteria set, horizon, currency, price base and metric revisions, and includes a do-nothing comparator or an explicit justified exception. Capacity is checked at scenario level, not at ranking level; the top-ranked set need not be the selected set, and divergence requires a recorded explanation. Strategic alignment is a versioned contribution claim; it is not a causal benefit claim, and spending, completion or inclusion proves neither outcome nor realization.

## Governance
Portfolio governance owns mandate, reserved decision rights, admission and removal, criteria adoption, weighting, scenario selection, allocation within its envelope, thresholds, assurance and portfolio gates. Component authorization, baselines and internal gates remain component-owned. Escalation references a decision; it never transfers mastership. Product-versus-project comparison uses a common period with per-period incremental cost and expected value, a continue-at-current-level comparator for products, and no completion-based measures; product investments carry no implied end date.

## Time/version/rebalance
Planned, decision, event, effective, observation, ingestion and knowledge times remain distinct. Membership, criteria pins, rankings, allocations and scenarios are effective-dated with non-overlapping intervals per assertion class. **Review cadence** is a declared interval plus event triggers (defeated assumption, constraint breach, funding change, strategy restatement, authority change, horizon expiry); a **rebalance** is a distinct authorized lifecycle event producing successor composition and allocation releases. Released items are immutable; correction is supersession with preserved provenance and no history rewrite.

## Acceptance scenario
Portfolios PF-1 and PF-2 both admit initiative INI-1 with shares 0.6 and 0.4 from distinct released funding sources. Each admission is its own membership assertion; neither implies the other, and neither converts INI-1 into a project. PF-1 selects scenario SC-3, which pins criteria set CS-v2, weighting W-v1, the scored candidate set and capacity limits; decision D-7 approves it and issues REC-7. A later score revision or CS-v3 creates successor releases and may trigger review; SC-3, D-7 and REC-7 remain readable and reproducible as-of. Aggregate reporting shows INI-1 once, with shares attributed, and no source exceeds its released amount. Because PF-1's components share no dependency or outcome, no program is formed.

## Invariants
1. Exactly one WM-ACT-029 profile discriminator; portfolio components need not be related. 2. Membership never transfers component mastership. 3. Portfolio lifecycle never cascades to component masters. 4. One component may hold membership in several portfolios. 5. Criterion definition, weighting scheme and observed score remain distinct. 6. Rank is release-scoped, never an intrinsic work property. 7. Every comparison pins criteria, horizon, price base, metric revisions and a do-nothing comparator or exception. 8. Portfolio allocation is not authority, availability, commitment, actual or component funding. 9. Source-side released amounts are never exceeded; residuals reconcile; shares are counted once. 10. Scenario outputs are never actuals or baselines. 11. Baseline approval requires an authorized decision. 12. Alignment claims are not causal benefit claims. 13. Released assertions are immutable and superseded explicitly. 14. Profile change is supersession with new identity. 15. Unallocated and blocked referents are never silently promoted.

## Minimal model set
WM-ACT-029 (`Portfolio` profile); contained PortfolioComponent, Prioritization, InvestmentAllocation, PortfolioScenario and approved-baseline releases; one new criteria-set candidate (identifier unassigned); referenced WM-ACT-005, WM-ACT-030, WM-ACT-029/`Program`, WM-ECO-012, WM-KNW-011, WM-KNW-010, WM-ACT-024, WM-REC-010.

## Holds
Unallocated referents: criteria set, Metric Definition, Outcome/Benefit Realization, Product, Operation, Resource/Capacity, Funding Source, Commitment/Contract. Contradictions: WM-ACT-029 lists WM-ACT-005 as both parent and contained; WM-ACT-030's parent WM-ACT-005 conflicts with initiative-is-not-project; WM-ACT-029's programme/portfolio token is inconsistent across name, naming rule and identity strategies; its declared access scopes cannot express the field-level rules its default and audit clauses assume; its all-covered checklist is contradicted by its own omissions. WM-ACT-029, WM-ACT-030 and WM-ECO-012 are single-provider reviewable drafts with waived independent review; ISO support is abstract-only; relation rows are unapproved and frozen contracts empty; retention and access rules are unsourced house policy. Source pins, crosswalks, mastership confirmation and fixtures are unverified. No claim of canonical completeness, installability or publication readiness is made.

```

## EXACT GROK RESPONSE

```text
**Verdict.** Conditionally accept. Profile Portfolio on WM-ACT-029 only as a selection-and-allocation container that disables Program delivery, exclusive child-set, relatedness, rollup and single-owner funding. Treat PortfolioComponent, Prioritization, InvestmentAllocation and PortfolioScenario as addressable portfolio-owned releases. Keep component mastership, budget authority, observations, accounting actuals and decision records external. Allocate no other identifier. This review is not a publication decision.

**Selection Criteria Set identity.** Released set instances need independent identity so two portfolios and successive cycles can pin the same set. Binding criteria as portfolio-owned releases would duplicate sets or block reuse. EM-WRK-04 allocates no new identifier; the root stays identifier-unassigned. SelectionCriterion belongs to the set, not to a portfolio.

**Double funding vs double counting.** Two portfolios may fund one initiative at 0.6 and 0.4. That is overlapping investment intent, in-model and allowed. Double counting of budget authority, commitments, accounting actuals, capacity, outcomes or benefits is out-of-model and forbidden. Shares need not sum to 1.0; other sponsors may exist. Share basis (capital, cost, capacity, headcount) is unspecified and must not default to “fraction of the initiative budget.”

**Strongest evidence.** The 0.6/0.4 fixture works only under this split: initiative mastership stays on WM-ACT-030; two PortfolioComponent memberships; two InvestmentAllocation intent shares; budget authority and actuals stay on WM-ECO-012; a selected PortfolioScenario pins a criteria-set version and decision-evidence references without absorbing those records. Profiling on WM-ACT-029 also avoids minting a new portfolio identifier.

**Strongest counterexample.** If WM-ACT-029 already binds exclusive Program ownership or funding, one portfolio becomes “the program” and 0.6+0.4 is illegal. Separately: two portfolios share one criteria set, apply different local observations, each claims 100% of initiative benefits, and finance also books the initiative budget — selection looks valid, enterprise totals lie. Evidence is also lost if a selected scenario mutates live criteria instead of pinning a released set.

**Identity / mastership.** Portfolio instances have their own identity as a WM-ACT-029 profile. Project mastership stays on WM-ACT-005; Initiative on WM-ACT-030; budget authority on WM-ECO-012; Goal/Objective on WM-KNW-011; decisions on the decision triad. PortfolioComponent does not transfer mastership. Prioritization, InvestmentAllocation and PortfolioScenario are cycle-scoped portfolio-owned releases.

**Boundaries.** Portfolio ≠ Program ≠ catalogue ≠ project ≠ initiative. Membership ≠ mastership. Criteria ≠ observations ≠ ranking. Rank ≠ intrinsic work properties. Portfolio allocation ≠ budget authority ≠ commitment ≠ actual ≠ component funding. Scenario ≠ approved baseline. Strategic alignment ≠ causal benefit claims.

**Components / membership.** PortfolioComponent is a directed, addressable membership release from one Portfolio to one external work item. Cardinality is many-to-many. Unrelated components are permitted; membership is not a catalogue and not a type gate. No WBS parentage, no implied Program child-set, no exclusive owner. The same initiative may sit in two portfolios at once.

**Criteria / scoring / prioritization.** Three layers: reusable Selection Criteria Set (definitions, weights, scales); external observations; Prioritization as a portfolio-owned application of a pinned set to current membership. Rank is not written back onto WM-ACT-005/030. Alignment scores are prioritization outputs, not realized-value arithmetic on WM-KNW-011.

**Allocation / funding.** InvestmentAllocation states this portfolio’s intended share or amount for a component in a scenario or cycle. It is not a ledger entry, authority instrument or actual. Oversubscription is a scenario condition to flag externally, not an implicit transfer of ownership or cash.

**Scenarios / decisions.** PortfolioScenario packs membership, pinned criteria-set version, Prioritization, InvestmentAllocation set, and references to external decision records. It does not ingest decision bodies. Approval lives on the decision triad. Baseline is a governance designation of a scenario, not a second type in this package.

**Governance.** Portfolio governs membership, criteria pin, ranking application, allocation intent and scenario choice only. It does not govern execution, budget authority, commitments, actuals, observations or decision issuance. Conflicting ranks of the same work item across portfolios are allowed and unreconciled here. Criteria-set stewardship is outside any one portfolio.

**Time / version / rebalance.** Portfolio-owned releases version per cycle. Criteria-set versions are independent of cycle; a portfolio pins a released set or snapshot rather than forking it. Rebalance emits new Prioritization, InvestmentAllocation and PortfolioScenario. Prior selected scenarios remain immutable evidence. Component-master versions are not portfolio versions.

**Scenario (0.6 / 0.4).** P1 and P2 each hold a PortfolioComponent to the same Initiative. Mastership stays on the initiative. P1 share 0.6, P2 share 0.4. Each selected scenario preserves its criteria-set pin and decision-evidence refs. Unrelated third components may exist in either portfolio. Neither portfolio becomes a Program. Outcomes and actuals are not derived by summing the shares.

**Invariants.**
1. WM-ACT-029 profile does not inherit Program delivery, rollup or exclusive-owner semantics.
2. PortfolioComponent never transfers mastership.
3. A work item may belong to multiple portfolios at once.
4. Membership admits unrelated components; no automatic Program set.
5. Rank is a Prioritization output, not an intrinsic work property.
6. Criteria ≠ observations ≠ ranking.
7. InvestmentAllocation ≠ budget authority ≠ commitment ≠ actual ≠ component funding.
8. Overlapping allocations (0.6+0.4) are permitted as co-funding intent.
9. Actuals, capacity, outcomes and benefits must not be double-counted from those allocations.
10. Selected scenario pins criteria-set version or snapshot and decision-evidence refs.
11. Scenario is not the approved baseline until an external decision says so.
12. Rebalance creates new releases; it does not rewrite prior selected scenarios.

**Minimum model set.** In-model: Portfolio (WM-ACT-029 profile); PortfolioComponent; Selection Criteria Set (unassigned reusable root) + SelectionCriterion; Prioritization; InvestmentAllocation; PortfolioScenario. External refs only: WM-ACT-005, WM-ACT-030, WM-ECO-012, WM-KNW-011, decision triad, observations, actuals, component mastership, budget authority, catalogue.

**Blockers.** (1) Profiling is unsafe if WM-ACT-029 already binds exclusive ownership, child rollup or coordination — write an explicit profile constraint or do not profile. (2) Released criteria-set identity must be stated even without allocating an identifier. (3) Allocation share basis unspecified. (4) No in-model hook to WM-ECO-012 for oversubscription. (5) Decision-triad attachment point unspecified (scenario vs cycle vs portfolio). (6) Strategic-alignment slot vs WM-KNW-011 unspecified; risk of encoding causal benefit claims. (7) Observation authority unspecified; shared sets plus local observations make scores incommensurable. (8) No lifecycle rule when the initiative is cancelled, split or re-mastered.
```

## PROVIDER COMPARISON

```text
# EM-WRK-04 provider comparison

Claude and Grok agree on the primary boundary: profile Portfolio on WM-ACT-029; keep Program as a disjoint sibling; retain component mastership externally; keep PortfolioComponent, Prioritization, InvestmentAllocation and PortfolioScenario as portfolio-owned releases; create one independently identified but identifier-unassigned Selection Criteria Set candidate; and allocate no catalogue or runtime identifier.

Both reviews separate Portfolio from Program, catalogue, Project and Initiative; membership from mastership; criteria definitions from observations and rankings; portfolio allocation intent from budget authority, commitment, accounting actual and component funding; scenario from approved baseline; and strategic alignment from causal benefit claims. Both preserve immutable historical scenarios and criteria pins through rebalance.

Grok sharpens the allocation semantics. Overlapping portfolio shares express investment intent and need not sum to 1.0, because other sponsors may exist and share basis may be capital, cost, capacity or headcount. The share basis must be explicit and cannot default to a fraction of initiative budget. Consolidated actuals, capacity, outcomes and benefits must never be inferred or double-counted from those shares.

Grok also requires explicit profile constraints disabling Program delivery, rollup, relatedness and exclusive-owner semantics; independent identity for released criteria sets; an external WM-ECO-012 oversubscription hook; a scenario-level decision-triad attachment; explicit observation authority and comparability pins; and lifecycle rules for cancelled, split or re-mastered components.

Publication remains held by the identifier-unassigned Selection Criteria Set, unresolved WM-ACT-029 containment and profile semantics, unallocated metric/benefit/capacity/funding referents, unapproved relation rows and non-canonical base drafts. The result is a reviewable allocation-plus-profile dossier with no installability or publication-readiness claim.

```

## ALLOCATION CANDIDATE

```json
{"format":"vercy-model-allocation-candidate/v1","contourId":"EM-WRK-04","proposedName":"Selection Criteria Set","modelId":null,"registryId":null,"allocationState":"unassigned","decision":"NEW MODEL","canonicalPublishable":false,"identityTest":{"stableIdentity":"A governed selection-criteria set remains identifiable across portfolios, candidate populations and review cycles while its criteria, weights and constraints evolve through released versions.","versionIdentity":"Changes to criterion semantics, measure bindings, scales, directions, mandatory constraints or weighting create immutable set versions; a materially different selection purpose creates a separate set.","independentLifecycle":["draft","reviewed","approved","effective","suspended","superseded","retired"],"mastership":"portfolio governance or investment-methodology authority"},"boundary":{"owns":["persistent criteria-set identity","selection purpose and applicability","contained criterion definitions","measure, scale, unit and preference-direction bindings","mandatory versus compensatory constraints","weighting and normalization rules","approval, effective period and reuse policy","supersession and retirement history"],"references":[{"target":"WM-ACT-029","purpose":"Portfolio profile and prioritization release"},{"target":"WM-ECO-012","purpose":"Budget authority and funding envelope"},{"target":"WM-KNW-011","purpose":"Objective or strategic contribution reference"},{"target":"WM-ACT-034","purpose":"Assessment or evaluation boundary"},{"target":"WM-ACT-030","purpose":"Initiative candidate identity"},{"target":"WM-ACT-005","purpose":"Project candidate identity"}],"excludes":["portfolio, component, project, program or initiative identity","observed metric value or evidence","candidate score, rank or prioritization release","scenario, decision or approved baseline","budget authority, funding availability, commitment or accounting actual","benefit realization or causal attribution"]},"objects":{"SelectionCriteriaSet":{"identity":["selectionCriteriaSetId"],"required":["name","selectionPurpose","ownerRef","status"],"optional":["successorRef","retiredAt"],"lifecycle":["draft","reviewed","approved","effective","suspended","superseded","retired"]},"CriteriaSetVersion":{"identity":["selectionCriteriaSetId","version"],"required":["criteria","validFrom","contentDigest","status"],"optional":["weights","constraints","normalizationRule","applicability","validTo","supersedesVersion"],"lifecycle":["draft","approved","effective","superseded","withdrawn"]}},"invariants":["Every prioritization release pins one exact criteria-set version and weighting version.","Criterion definition, weighting, observation, score and rank remain distinct.","Every criterion declares measure reference, scale, unit, preference direction and mandatory or compensatory status.","Observed scores cite source, period, method, denominator, quality and uncertainty.","Rank is scoped to one prioritization release and never becomes an intrinsic component property.","Rankings with incompatible criteria, horizon, price base or metric revisions are not directly compared.","Criteria-set reuse never transfers portfolio or component mastership.","Changes to criterion semantics or weighting create immutable successor versions.","Selection includes constraints and a do-nothing comparator or a recorded exception.","Strategic alignment is an evidence-bearing contribution claim and never proves benefit realization.","A criteria set never owns allocation, funding, commitment, actual or decision records.","Retired and superseded versions remain resolvable for historical decisions."],"holds":["Registry namespace and identifier allocation are pending and no identifier may be guessed.","Independent Grok review and one frozen semantic audit are pending.","Metric, benefit, capacity and funding referents require canonical reconciliation.","WM-ACT-029 containment and WM-ACT-030 parent conflicts remain unresolved.","Package conversion and live verification are pending."]}

```

## PROFILE CANDIDATE

```json
{"format":"vercy-enterprise-profile-candidate/v1","contourId":"EM-WRK-04","name":"Enterprise Portfolio Selection and Allocation","decision":"PROFILE","newRuntimeId":false,"bases":["WM-ACT-029","WM-ACT-005","WM-ACT-030","WM-ECO-012","WM-KNW-011"],"constraints":["Portfolio profiles WM-ACT-029 with the mandatory discriminator and remains distinct from Program, catalogue, Project and Initiative.","PortfolioComponent, Prioritization, InvestmentAllocation and PortfolioScenario are addressable effective-dated portfolio-owned releases.","Membership never transfers component mastership and one component may belong to multiple portfolios with independently declared shares.","Portfolio allocation is intent within an approved envelope and remains distinct from authority, commitment, actual and component funding.","Scenario is an immutable hypothesis release and becomes no baseline without a separate authorized decision and issued record.","Rebalance creates successor composition and allocation releases and preserves prior criteria, ranking, allocation and decision history."]}

```

## FIXTURES

```json
{"format":"vercy-enterprise-allocation-fixtures/v1","candidateName":"Selection Criteria Set","cases":[{"id":"reused-across-portfolios","kind":"positive","input":"Two portfolios use the same approved criteria-set version with different candidate sets.","expect":"The set is reused without merging portfolios, candidates or prioritization releases."},{"id":"successor-weighting","kind":"positive","input":"A later review changes weights while criterion semantics remain stable.","expect":"A successor version or separately pinned weighting release is created and old rankings remain reproducible."},{"id":"shared-initiative-funding","kind":"positive","input":"Two portfolios admit one initiative with shares 0.6 and 0.4 from distinct released sources.","expect":"Memberships and allocations remain independent and consolidated reporting counts the initiative once."},{"id":"rank-intrinsic","kind":"negative","input":"A rank from one review is written as an intrinsic property of the initiative.","expect":"The write is rejected."},{"id":"compare-incompatible-ranks","kind":"negative","input":"Ranks using different criteria versions and price bases are compared directly.","expect":"The comparison is rejected."},{"id":"criteria-own-observations","kind":"negative","input":"Observed metric values are stored as mutable properties of the criteria definition.","expect":"The ownership merge is rejected."},{"id":"scenario-is-baseline","kind":"negative","input":"The highest-ranked scenario becomes approved automatically.","expect":"The transition is rejected without authorized decision and issued baseline."}]}

```
