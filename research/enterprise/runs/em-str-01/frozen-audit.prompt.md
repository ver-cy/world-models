# EM-STR-01 frozen semantic audit prompt

You are the sole final Claude Opus high no-tools auditor. This is exactly one frozen audit after an independent Claude study, local synthesis, and the exact visible Grok response. Do not browse, use tools, invent identifiers, claim publication readiness, or request another study.

Admitted evidence is limited to the initial Claude study, local synthesis, exact visible Grok response, and candidate artifacts appended below. Grok exposed a sources control despite the instruction not to browse; hidden reasoning and sources are excluded. The visible response is complete and admitted as text only.

Audit the settled boundary and artifacts:

- Strategy, Business Model, Value Stream and Strategic Scenario have independent identity and lifecycle but remain identifier-unassigned.
- Strategic Scenario is non-authoritative and hypothesis-only; it is not merged into Strategy and never masters actuals, baselines, outcomes or benefits.
- Strategic Theme is contained by Strategy; Value Proposition is contained by Business Model.
- Strategy owns choices, rejected alternatives, assumptions, horizon and review triggers, not plans, projects, initiatives, outcomes or benefits.
- Business Model owns the value mechanism, not organization identity or offer instances.
- Value Stream owns recipient-triggered value-state stages; process/workflow may realize a stage but never defines it.
- Reuse WM-KNW-011, WM-ACT-030, WM-KNW-010, WM-ACT-024 and WM-REC-010 by reference.
- Capability and Process/Workflow remain legacy-only completion dependencies.
- Outcome and Benefit Realization remains a separate identifier-unassigned candidate.
- Forecasts, outcomes and benefits remain distinct; scenario outputs never become actuals or baselines.
- No runtime or model identifier is allocated.

Return:

1. Verdict on decision and artifacts.
2. Numbered material defects, each with exact deterministic remediation.
3. A single exact JSON array of additional fixtures. Every fixture must contain id, target, kind, input, expect, violates, closesDefect; every negative must also contain expectedCode.
4. Exact final counts for prior, additional, and total fixtures, split into positive and negative.
5. Freeze decision. Do not ask for or perform a rerun.


## INITIAL CLAUDE STUDY

# EM-STR-01 — Strategy, Business Model and Value Streams

## Verdict
Four candidates require **independent model identity** (identifier unassigned): **Strategy**, **BusinessModel**, **ValueStream**, **StrategicScenario**. Two are **contained records / profiles, not roots**: **StrategicTheme** (inside Strategy), **ValueProposition** (inside BusinessModel). Five adjacent models are **reused unchanged, by reference**: WM-KNW-011, WM-KNW-010, WM-ACT-024, WM-REC-010, WM-ACT-030. Capability and value-stream→process realization stay **blocked** (WM-ACT-001, WM-ACT-003 are legacy-only, `migration-boundary-review`). Value realization is **declared-unallocated** to the EM-STR-02 Outcome/Benefit candidate. The project-list case is rejected. `boundary_decision` remains pending pending registry allocation.

## Evidence
Only the frozen dossier is used. WM-KNW-011 owns the desired-outcome record, measure binding by reference, horizon, accountability, restatement and supersession, and explicitly excludes planning of means. WM-ACT-030 owns change intent, options, appraisal, mandate and formalization, and explicitly refuses to be a synonym for Strategy. WM-KNW-010 owns question, alternatives, criteria, evaluation rounds, selection and rationale; WM-ACT-024 the approval occurrence; WM-REC-010 the authentic fixed expression. Nothing in the dossier masters market choice, value mechanism, recipient-triggered value flow or scenario space — the gap is real, not a naming artifact. The `candidate_properties_from_v1` fields (STR-01, STR-06) are marked `candidate-not-normative` and are treated as evidence of intent only.

## Identity/mastership
Strategy identity survives restatement, theme reshuffling and every initiative it spawns; it is answerable to one decision authority. BusinessModel identity survives strategy versions and outlives individual offers; one group runs several concurrently. ValueStream identity survives process redesign and reorganization; it is named by recipient need, not by organizational unit. StrategicScenario identity is independent because a scenario is cited by many strategies and must not inherit any strategy's authority. StrategicTheme and ValueProposition have revisions but no authority, no mandate and no lifecycle of their own — they are addressable children, mastered by their root. Suggested masters: strategic decisions register (Strategy), business-model register (BusinessModel), value-stream register (ValueStream), planning/analysis register (StrategicScenario).

## Strategy and themes
Strategy records a **choice set**: markets and segments selected, those explicitly excluded, the basis of advantage asserted, the assumptions the choice rests on, the horizon, and the review triggers. Exclusions are first-class; a strategy with no rejected alternative is not a strategy. **Mission and policy are not strategic choice**: mission is standing purpose with no horizon and no rejected alternative; policy is a standing constraint on permissible choices. Both are referenced (policy referent unallocated in this dossier), never restated. **Strategy is not plan, initiative or portfolio**: sequencing, resourcing and delivery are WM-ACT-030 and portfolio referents. StrategicTheme groups choices under a stated intent and carries the alignment anchor that objectives and initiatives cite; its horizon and authority are inherited.

## Business model and value proposition
BusinessModel records the **value mechanism**: recipient segments, channels, value proposition bindings, revenue and cost logic, key partners and resources by reference. It is **not the organization**: legal entity, unit and role are party referents; one entity may run many business models and one business model may span entities. ValueProposition is the asserted benefit-to-recipient claim (job, pain, gain, alternative displaced) for one segment–channel pair. It is **not the offer**: price, terms, SKU and contract are offer/product referents outside this contour. Where a group reuses one proposition across business models, that is a **citation of a pinned VP revision**, never a second master.

## Value stream versus process
A **stage** is a change in the recipient's value state — need recognized, request qualified, value accessible, value realized — triggered by the recipient and validated from the recipient's side. A **process** is the repeatable internal realization of one or more stages, with steps, gateways, roles and states. The test: if renaming or automating the work leaves the recipient's state sequence unchanged, it is process, not stage. ValueStream owns trigger, recipient, stage sequence, stage entry/exit criteria and the value outcome referent. Stage→process and stage→capability bindings are **blocked**: WM-ACT-003 and WM-ACT-001 are `described-previous-version` with no current boundary, so the edges are declared and unenforceable.

## Scenario and hypothesis
StrategicScenario holds drivers, varied assumptions, projected states and method, each attributable and uncertainty-bearing. A scenario is a **hypothesis space**, never a source of record. Assumptions carry validity windows and defeat conditions; causal hypotheses (choice → mechanism → outcome → benefit) carry stated attribution limits and competing explanations. Promotion of a hypothesis to confirmed requires an external assessment with pinned criteria and decision rule — the assessment referent is not in this dossier and is therefore blocked. **Forecast is not outcome**: a projected figure remains a forecast until qualified observations in the realization window support it, and the observing referent is the unallocated EM-STR-02 aggregate. **Authoritative actuals and scenarios are separated**: no scenario output may become an observation, a target baseline, or a benefit realization input.

## Objectives/capabilities/initiatives/decisions
Objectives, key results and targets are **WM-KNW-011 role-coded records** citing a Strategy or StrategicTheme identity; measures bind by reference, and WM-KNW-011's own measure/metric referent is unassigned. Initiatives are **WM-ACT-030**, linked by a contribution assertion with a stated basis — membership, tag or budget line is not alignment. Capability requirements are **blocked**. Strategy approval cites **WM-KNW-010** (alternatives, exclusion reasons, criteria, rationale, dissent), **WM-ACT-024** (approval occurrence, authority, quorum) and **WM-REC-010** (fixed expression, issuance, finality). Strategy must not restate any of these; it carries references and the resulting authority basis only.

## Time/version/review
Four axes stay separate: **horizon** (the interval the choice reaches), **effective window** (when the version governs), **event vs. knowledge time**, and **review cadence**. A released Strategy version is immutable; substantive change produces a successor with a restatement note, retained prior choices and a supersession link. Review triggers are declared, not inferred: assumption defeat, scenario divergence past a stated threshold, measure breach, **segment or channel change**, authority change, horizon expiry. A BusinessModel revision is triggered by change to a named mechanism element; a ValueStream revision by change to trigger, recipient or stage sequence.

## Acceptance scenario
**Startup.** Strategy: serve segment X through direct channel, excluding marketplace; assumptions: acquisition cost and willingness to pay. One BusinessModel, one VP, one value stream (need → activated → first value). Channel moves to marketplace: because *channel* is named in the strategy's choice set, this is a Strategy restatement, a new BusinessModel revision, VP revalidation (jobs unchanged, access and effort changed) and a new stage sequence. The acquisition-cost assumption is marked defeated; prior forecasts stay as forecasts.
**Multi-industry group.** Group Strategy chooses which industries to be in and the capital-allocation logic; themes span business models. One BusinessModel per industry–segment–channel. Exiting a segment retires that BusinessModel to a terminal state (never deletes it) and restates the group Strategy only if that market was a named choice; the shared VP citation from the surviving business model remains resolvable. Value streams follow business models, not legal entities.
**Negative case.** A project list labelled strategy is **rejected**: it is a portfolio projection. It carries no rejected alternative, no recipient of value, no assumption, no causal hypothesis, no horizon and no review trigger, and its items are WM-ACT-030 records.

## Invariants
1. A strategy states at least one explicitly rejected alternative. 2. Strategy has a horizon and a named decision authority, cited to WM-ACT-024/WM-REC-010. 3. Mission and policy constrain but never constitute strategic choice. 4. An initiative never substitutes for a strategy, and no project list creates one. 5. Every value stream starts from a recipient need and its trigger. 6. Stage is a recipient value-state change; process realization is referenced, not owned. 7. Business model is distinct from organization; neither masters the other. 8. Value proposition is distinct from offer; price and terms are never held here. 9. Assumptions and causal hypotheses are labelled hypotheses with defeat conditions until externally assessed. 10. Forecasts never overwrite outcomes; realization requires qualified observations in the window. 11. No scenario output feeds authoritative actuals, baselines or benefit realization. 12. Released strategy versions are immutable; change proceeds by successor and supersession. 13. Contribution and alignment links require a stated basis. 14. Blocked and unallocated referents are never silently promoted.

## Minimal model set
New, identifier unassigned: **Strategy** (aggregate root, containing StrategicTheme), **BusinessModel** (aggregate root, containing ValueProposition), **ValueStream** (aggregate root, containing Stage), **StrategicScenario** (aggregate root, containing assumption and projection sets). Profiles/contained only: StrategicTheme, ValueProposition, Stage. Reuse by reference: WM-KNW-011, WM-ACT-030, WM-KNW-010, WM-ACT-024, WM-REC-010. Blocked: Capability (WM-ACT-001), Process/Workflow (WM-ACT-003), assessment referent. Declared-unallocated: Outcome/Benefit Realization (EM-STR-02), metric definition, policy/mission, offer/product, party, portfolio.

## Holds
No identifier is allocated; `boundary_decision` stays pending and `target_model_ids` empty. Every reused base is `publishableCanonical: false`; WM-KNW-011, WM-KNW-010 and WM-ACT-024 are Claude-only under an owner waiver, WM-ACT-030 is Codex-only with Claude and Grok waived. Relationship contracts for the asserted references are absent or empty, so all boundary exclusions here are declared and unenforceable. Two required realization referents have no current specification and two more have no registry allocation. No semantic crosswalk, mastership confirmation, immutable refs or fixture checks have been performed. This review claims no canonical completeness, no installability and no publication readiness.



## LOCAL SYNTHESIS

# EM-STR-01 local synthesis

## Disposition

- Propose four identifier-unassigned independent candidates: **Strategy**, **Business Model**, **Value Stream** and **Strategic Scenario**.
- Keep **Strategic Theme** as an addressable child of Strategy and **Value Proposition** as an addressable child of Business Model. Neither receives root identity.
- Reuse WM-KNW-011 for objectives, WM-ACT-030 for initiatives, WM-KNW-010 for rationale, WM-ACT-024 for the approval occurrence and WM-REC-010 for the issued decision record.
- Keep Capability and Process realization blocked because WM-ACT-001 and WM-ACT-003 have legacy specifications only.
- Reference the identifier-unassigned Outcome and Benefit Realization candidate from EM-STR-02.
- Allocate no catalogue or runtime identifier.

## Identity and mastership

Strategy has identity across successive choice-set revisions and across the initiatives that implement it. Business Model has identity across strategy revisions and individual offers and may span legal entities. Value Stream has identity across process redesign and organization changes because it is defined by recipient need and value-state progression. Strategic Scenario has identity because multiple strategies can cite one versioned scenario without inheriting its authority.

Strategic Theme and Value Proposition are versioned contained records. A theme groups strategic choices and supplies an alignment anchor. A value proposition states a benefit claim for a recipient segment and channel. It is not an offer, price, SKU or contract.

## Strategy and business model

A Strategy release records selected and explicitly excluded markets or segments, choice rationale, claimed basis of advantage, assumptions, causal hypotheses, horizon, decision authority and review triggers. A mission is standing purpose and a policy is a standing constraint; neither is a strategic choice. Plans, initiatives and portfolios implement strategy but do not constitute it.

A Business Model release records the value mechanism: recipient segments, channels, value propositions, revenue and cost logic, partners and resources by reference. An organization may operate many business models and one business model may span organizations. Channel, segment or mechanism changes create successor releases and preserve prior versions.

## Value stream and realization

A Value Stream begins with a recipient need and trigger and ends with a recipient-side value outcome. Each stage is a change in recipient value state with entry and exit criteria. A Process is an internal repeatable realization of one or more stages. Renaming, reorganizing or automating internal work without changing the recipient-state sequence changes the process, not the value stream.

Stage-to-process and stage-to-capability bindings remain declared but unenforceable until WM-ACT-003 and WM-ACT-001 receive current boundary-reviewed specifications. Output, outcome and benefit stay distinct; delivery completion never proves recipient value or benefit realization.

## Scenario, hypothesis and evidence

A Strategic Scenario holds versioned drivers, varied assumptions, projected states, method and uncertainty. It is a hypothesis space, never a source of record. Assumptions carry validity windows and defeat conditions. Causal hypotheses carry competing explanations and attribution limits.

Scenario results never feed authoritative actuals, target baselines or benefit realization. Forecast remains forecast until qualified observations for the phenomenon period support an outcome. Alignment and contribution links cite a rationale or evidence basis; tags, budget membership and portfolio inclusion are insufficient.

## Decision and review

WM-KNW-010 records alternatives, criteria, evaluation and rationale. WM-ACT-024 records the authorized decision occurrence. WM-REC-010 records the fixed issued expression. Strategy references these identities and never duplicates them.

Horizon, effective interval, event time, knowledge time and review cadence remain distinct. Review triggers include defeated assumptions, scenario divergence, measure breach, named segment or channel change, authority change and horizon expiry. Released versions are immutable; substantive change creates a successor with an explicit restatement and supersession link.

## Acceptance result

A startup strategy selects segment X through a direct channel and excludes a marketplace. Moving to the marketplace defeats a named assumption, restates Strategy, revises Business Model, revalidates the Value Proposition and may revise the Value Stream. Prior forecasts remain forecasts.

A multi-industry group keeps one group strategy plus distinct business models by industry, segment and channel. Exiting a named market restates the group strategy and retires the affected business model without deleting history. Shared value-proposition references remain resolvable. A project list labelled strategy is rejected because it contains no choice set, rejected alternative, value recipient, assumptions, horizon or review trigger.

## Required invariants

1. Strategy states at least one selected choice and one explicitly rejected alternative.
2. Strategy names a horizon and cites decision authority.
3. Mission and policy constrain strategy but never constitute it.
4. Initiative, project and portfolio never substitute for strategy.
5. Business Model remains distinct from organization.
6. Value Proposition remains distinct from offer and contract.
7. Every Value Stream begins with a recipient need and trigger.
8. A stage is a recipient value-state change; a process is internal realization.
9. Assumptions and causal links remain hypotheses with defeat conditions until assessed.
10. Forecast never becomes observed outcome by relabelling.
11. Scenario outputs never become authoritative actuals or baselines.
12. Alignment links require an attributable basis.
13. Released versions are immutable and superseded explicitly.
14. Blocked and unallocated referents are never silently promoted.

## Holds

Strategy, Business Model, Value Stream and Strategic Scenario lack registry allocation. Capability and Process/Workflow have legacy-only specifications. Outcome/Benefit, Metric Definition, policy/mission and several party/offer bindings are unallocated or outside the dossier. All reused current specifications remain non-canonical drafts and relationship contracts are incomplete. No crosswalk, mastership confirmation or fixtures support publication. No installability or publication-readiness claim is made.



## VISIBLE GROK RESPONSE

Verdict: Accept with a split on root status. Strategy, Business Model and Value Stream are independent master roots. Strategic Scenario keeps independent identity and lifecycle but is profiled as non-authoritative: hypothesis space only, never a source of record. Strategic Theme is contained by Strategy. Value Proposition is contained by Business Model. No identifiers are assigned. No publication-readiness claim.

Strongest evidence: A startup moving from direct sale to a marketplace changes the value mechanism (take-rate, two-sided exchange) and may recut recipient stages (onboard seller, match, settle) while the strategy choice set can stand: serve the segment, reject vertical integration. The same Decision can reference both changed roots and the unchanged choice set. A project list cannot express that split.

Strongest counterexample: A multi-industry group exiting one segment arrives as one board pack that retires a business model, sunsets a stream, and attaches a project list, all labelled “the strategy.” If that pack is allowed to be the Strategy root, identity collapses. The pack is a Decision/Approval Record referencing separate masters, not a master itself.

Identity/mastership: Strategy masters the choice set. Business Model masters the value mechanism. Value Stream masters recipient-triggered value-state stages. Strategic Scenario masters hypotheses only. Cross-links are references. No root is source of record for another’s attributes. Theme and Value Proposition have no independent lifecycle; they do not outlive their container without reassignment, which is a new containment.

Strategy/themes: Strategy owns chosen position, choice set, rejected alternatives, assumptions, horizon and review triggers. It does not own plans, projects, initiatives or organisation design. Strategic Theme is a contained classifier of choices, not a peer root. A theme without a containing Strategy is invalid.

Business model/value proposition: Business Model owns how value is created, delivered and captured: who pays, exchange logic, channel economics. It does not own organisation structure or the offer catalogue. Value Proposition is a contained claim of offered value to a recipient class. A stream may reference the proposition it realises; it does not master it.

Value stream/process: Value Stream owns outside-in stages: start state, intermediate value states, end state received by the stakeholder. Legacy Process/Workflow remains reference-only and may realise a stage. Process change does not force a stream version unless the recipient value-state changes. Profiling the stream onto process would import inside-out churn and fail the channel-shift test.

Scenarios/hypotheses: Strategic Scenario is a named hypothesis space (assumptions, option bundles, forecast ranges) with its own version lifecycle, so a set can be branched, reused across strategy reviews, or closed without a Strategy version bump. That is why it is not merged into Strategy. It is profiled as non-authoritative because promotion of its outputs to actuals, baselines or benefits would launder hypotheses into facts. Attachment-only under Strategy was considered and rejected for the reuse case; the promotion ban is an invariant, not a reason to erase identity.

Objectives/capabilities/initiatives/decisions: Reuse Goal/Objective, Initiative, Decision/Rationale, Decision/Approval Activity and Decision/Approval Record by reference. Objectives state ends; Strategy chooses among them. Initiatives realise change and are not constituents of Strategy. Decisions authorise a choice; they do not own the choice set. Capability remains legacy-only. Outcome and Benefit Realization stay the separate identifier-unassigned candidate. Forecasts stay inside Scenario. The three are distinct types.

Time/version/review: Each root versions on its own change driver. Strategy advances on choice, horizon or trigger change. Business Model advances on mechanism change. Value Stream advances on stage or recipient-state change. Scenario versions are branches, never current state. Review triggers live on Strategy and fire a review; they do not rewrite other roots. No shared baseline across roots.

Scenario: Startup, direct to marketplace — new Business Model version; stream stages may gain match and settle; Strategy choice set unchanged unless the segment thesis changes; a Decision cites the affected roots; the project list is not the Strategy. Group exit of one segment — Strategy retires that choice and records the rejected continuation; related Business Model and Value Stream are retired or archived; other segments’ models stay; any scenario that assumed continued presence is closed, not baselined.

Invariants:

1. Strategy is not a project list, roadmap or initiative portfolio.
2. Rejected alternatives stay attached to the choice set that rejected them, or an explicit none-considered rationale is recorded.
3. Strategy does not own Benefits or Outcomes.
4. Business Model does not master organisation or offer instances.
5. A Value Proposition is contained by exactly one Business Model at a time.
6. A Strategic Theme is contained by a Strategy.
7. Value Stream stages are recipient-triggered value states, not process tasks.
8. A process may realise a stage; it does not define the stage.
9. Strategic Scenario is never source of record.
10. Scenario output cannot be written as actual, baseline or realised benefit.
11. Forecast, Outcome and Benefit Realization remain distinct types.
12. Initiative realises a choice; it is not the choice.
13. Decision and Approval Record reference the roots; they do not replace them.
14. Horizon and review triggers are mandatory Strategy attributes.
15. Scenario retirement does not retire Strategy, Business Model or Value Stream.
16. A channel or segment change requires a Decision referencing the affected roots; relabeling a project list is invalid.

Minimum model set: Strategy, Business Model, Value Stream, and non-authoritative Strategic Scenario, plus contained Strategic Theme and Value Proposition, plus references to Goal/Objective, Initiative, Decision/Rationale, Decision/Approval Activity and Decision/Approval Record. Outcome/Benefit Realization stays candidate. Capability and Process stay legacy references.

Blockers: Identifier assignment is out of scope. Outcome/Benefit remains unassigned, so benefit linkage is reference-only. No coupling rule yet between Business Model version and Strategy version beyond the Decision reference. The stream-to-process link must be realisation, not merge; that rule is not yet drafted. Scenario leakage into baselines is the main integrity risk and is held only by invariant, not by an identifier scheme.

Independence decision: Do not merge any of the four. Strategy, Business Model and Value Stream are true master roots because choice, mechanism and recipient value-state have different owners and change drivers; merging any collapses the channel-shift and segment-exit cases. Strategic Scenario is independent in identity and lifecycle but profiled as non-authoritative, because a hypothesis space must be versionable and reusable without becoming a fact master. Theme and Value Proposition stay contained.



## ARTIFACT candidate-allocation-offline-strategy/allocation-candidate.json

{"format":"vercy-model-allocation-candidate/v1","contourId":"EM-STR-01","proposedName":"Strategy","modelId":null,"registryId":null,"allocationState":"unassigned","decision":"NEW MODEL","canonicalPublishable":false,"identityTest":{"stableIdentity":"A governed strategic choice set remains identifiable across revisions and independently of initiatives, plans and portfolios.","versionIdentity":"Choice, exclusion, advantage, assumption, horizon or authority changes create immutable successor releases.","independentLifecycle":["draft","reviewed","approved","effective","underReview","restated","superseded","retired"],"mastership":"authorized strategy authority"},"boundary":{"owns":["strategy identity","immutable strategy releases","selected and excluded choices","advantage claims","assumptions and causal hypotheses","horizon and review triggers","contained strategic themes"],"references":[{"target":"WM-KNW-011","purpose":"Objective"},{"target":"WM-ACT-030","purpose":"Initiative"},{"target":"WM-KNW-010","purpose":"Decision rationale"},{"target":"WM-REC-010","purpose":"Issued decision"}],"excludes":["mission","policy","initiative","project or portfolio","objective","observed outcome"]},"objects":{"Strategy":{"identity":["strategyId"],"required":["name","ownerRef","status"],"optional":["successorRef"]},"StrategyRelease":{"identity":["strategyId","version"],"required":["selectedChoices","excludedChoices","horizon","decisionRef","contentDigest"],"optional":["themes","assumptions","reviewTriggers","supersedesVersion"]}},"invariants":["Each release selects at least one choice.","Each release explicitly rejects an alternative.","Horizon and authority are explicit.","Mission and policy never constitute strategy.","Initiatives and portfolios never substitute for strategy.","Assumptions carry defeat conditions.","Forecast never becomes observed outcome by relabelling.","Released versions are immutable.","Restatement links a successor.","Themes remain release-owned children.","Alignment requires attributable basis.","Blocked referents are never silently promoted."],"holds":["Registry allocation is pending and no identifier may be guessed.","Independent Grok review and one frozen semantic audit are pending.","Capability and process realization remain blocked on legacy specifications.","Package conversion and live verification are pending."]}



## ARTIFACT candidate-allocation-offline-strategy/profile-candidate.json

{"format":"vercy-enterprise-profile-candidate/v1","contourId":"EM-STR-01","name":"Enterprise Strategy and Value Realization","decision":"PROFILE","newRuntimeId":false,"bases":["WM-KNW-011","WM-ACT-030","WM-KNW-010","WM-ACT-024","WM-REC-010"],"constraints":["Objectives, initiatives and decisions retain their own masters.","Strategic Theme remains a Strategy-owned child.","Value Proposition remains a Business Model-owned child.","Capability and process realization remain blocked pending current specifications.","Outcome and Benefit Realization reuse the EM-STR-02 candidate boundary."]}



## ARTIFACT candidate-allocation-offline-strategy/fixtures.json

{"format":"vercy-enterprise-allocation-fixtures/v1","candidateName":"Strategy","cases":[{"id":"choice-set","kind":"positive","input":"A strategy selects direct sales and rejects marketplace distribution.","expect":"Both choice and exclusion are explicit."},{"id":"restatement","kind":"positive","input":"The channel changes after an assumption is defeated.","expect":"A successor release is created."},{"id":"project-list","kind":"negative","input":"A project list is labelled strategy without choices or horizon.","expect":"The record is rejected."},{"id":"forecast-as-fact","kind":"negative","input":"A scenario projection is relabelled as achieved outcome.","expect":"The assertion is rejected."}]}



## ARTIFACT candidate-allocation-offline-strategy/validation-policy.json

{"format":"vercy-allocation-validation/v1","requirements":{"modelIdMustBeNull":true,"registryIdMustBeNull":true,"allocationState":"unassigned","minimumInvariants":8,"minimumReferences":3,"minimumFixtures":3,"requiresPositiveAndNegativeFixtures":true,"requiresStableIdentityStatement":true,"requiresIndependentLifecycle":true}}



## ARTIFACT candidate-allocation-offline-business-model/allocation-candidate.json

{"format":"vercy-model-allocation-candidate/v1","contourId":"EM-STR-01","proposedName":"Business Model","modelId":null,"registryId":null,"allocationState":"unassigned","decision":"NEW MODEL","canonicalPublishable":false,"identityTest":{"stableIdentity":"A governed value mechanism remains identifiable across strategy revisions, offers and participating legal entities.","versionIdentity":"Segment, channel, proposition, revenue, cost, partner or resource changes create immutable successor releases.","independentLifecycle":["draft","reviewed","approved","effective","revised","superseded","retired"],"mastership":"authorized business-model authority"},"boundary":{"owns":["business-model identity","immutable releases","recipient segments and channels","contained value propositions","revenue and cost logic","partner and resource references","successor history"],"references":[{"target":"WM-ORG-001","purpose":"Participating organization"},{"target":"WM-ECO-021","purpose":"Offer boundary"},{"target":"WM-ECO-002","purpose":"Price and valuation boundary"},{"target":"WM-REC-010","purpose":"Authorizing decision"}],"excludes":["organization identity","offer or SKU","price","contract","strategy choice set","observed revenue"]},"objects":{"BusinessModel":{"identity":["businessModelId"],"required":["name","ownerRef","status"],"optional":["successorRef"]},"BusinessModelRelease":{"identity":["businessModelId","version"],"required":["segments","channels","valuePropositions","valueMechanism","contentDigest"],"optional":["revenueLogic","costLogic","partnerRefs","resourceRefs","supersedesVersion"]}},"invariants":["Business Model remains distinct from organization.","One organization may operate many business models.","One model may span organizations.","Value propositions are release-owned children.","Value Proposition is not an offer or contract.","Revenue logic is not observed revenue.","Partner and resource identities remain external.","Channel changes create successors.","Released versions are immutable.","Retirement preserves prior offers and agreements."],"holds":["Registry allocation is pending and no identifier may be guessed.","Independent Grok review and one frozen semantic audit are pending.","Capability and process realization remain blocked on legacy specifications.","Package conversion and live verification are pending."]}



## ARTIFACT candidate-allocation-offline-business-model/fixtures.json

{"format":"vercy-enterprise-allocation-fixtures/v1","candidateName":"Business Model","cases":[{"id":"multi-model","kind":"positive","input":"One group operates distinct models by industry.","expect":"Each model retains independent identity."},{"id":"channel-change","kind":"positive","input":"A direct model adds a marketplace.","expect":"A successor release is created."},{"id":"organization-collapse","kind":"negative","input":"Organization identity is used as business-model identity.","expect":"The conflation is rejected."},{"id":"proposition-offer","kind":"negative","input":"A value proposition is treated as a priced offer.","expect":"The inference is rejected."}]}



## ARTIFACT candidate-allocation-offline-business-model/validation-policy.json

{"format":"vercy-allocation-validation/v1","requirements":{"modelIdMustBeNull":true,"registryIdMustBeNull":true,"allocationState":"unassigned","minimumInvariants":8,"minimumReferences":3,"minimumFixtures":3,"requiresPositiveAndNegativeFixtures":true,"requiresStableIdentityStatement":true,"requiresIndependentLifecycle":true}}



## ARTIFACT candidate-allocation-offline-value-stream/allocation-candidate.json

{"format":"vercy-model-allocation-candidate/v1","contourId":"EM-STR-01","proposedName":"Value Stream","modelId":null,"registryId":null,"allocationState":"unassigned","decision":"NEW MODEL","canonicalPublishable":false,"identityTest":{"stableIdentity":"A recipient-value progression remains identifiable across process redesign, automation and organization change.","versionIdentity":"Changes to recipient need, trigger, value-state stages or terminal outcome create immutable successor versions.","independentLifecycle":["draft","reviewed","approved","effective","revised","superseded","retired"],"mastership":"enterprise value architecture authority"},"boundary":{"owns":["value-stream identity","recipient need and trigger","immutable stream versions","recipient value-state stages","entry and exit criteria","terminal recipient outcome","realization bindings"],"references":[{"target":"WM-ACT-003","purpose":"Process realization"},{"target":"WM-ACT-001","purpose":"Capability realization"},{"target":"WM-KNW-011","purpose":"Objective alignment"},{"target":"WM-MAT-008","purpose":"Outcome observation"}],"excludes":["internal process","organizational unit","project plan","output","observed outcome","benefit realization"]},"objects":{"ValueStream":{"identity":["valueStreamId"],"required":["name","recipientNeed","trigger","status"],"optional":["successorRef"]},"ValueStreamVersion":{"identity":["valueStreamId","version"],"required":["stages","terminalOutcome","contentDigest"],"optional":["realizationBindings","supersedesVersion"]}},"invariants":["Every stream begins with recipient need and trigger.","Every stage changes recipient value state.","Entry and exit criteria are explicit.","A process is internal realization, not the stream.","Reorganization alone does not change stream identity.","Automation alone does not change stream identity.","Output, outcome and benefit remain distinct.","Completion never proves recipient value.","Realization bindings are attributable.","Blocked capability and process references remain non-enforceable."],"holds":["Registry allocation is pending and no identifier may be guessed.","Independent Grok review and one frozen semantic audit are pending.","Capability and process realization remain blocked on legacy specifications.","Package conversion and live verification are pending."]}



## ARTIFACT candidate-allocation-offline-value-stream/fixtures.json

{"format":"vercy-enterprise-allocation-fixtures/v1","candidateName":"Value Stream","cases":[{"id":"process-redesign","kind":"positive","input":"Internal work is automated without changing recipient stages.","expect":"The stream identity remains stable."},{"id":"recipient-change","kind":"positive","input":"The terminal recipient outcome changes.","expect":"A successor stream version is created."},{"id":"process-collapse","kind":"negative","input":"A workflow diagram is treated as the value stream.","expect":"The conflation is rejected."},{"id":"completion-benefit","kind":"negative","input":"Process completion is treated as realized benefit.","expect":"The inference is rejected."}]}



## ARTIFACT candidate-allocation-offline-value-stream/validation-policy.json

{"format":"vercy-allocation-validation/v1","requirements":{"modelIdMustBeNull":true,"registryIdMustBeNull":true,"allocationState":"unassigned","minimumInvariants":8,"minimumReferences":3,"minimumFixtures":3,"requiresPositiveAndNegativeFixtures":true,"requiresStableIdentityStatement":true,"requiresIndependentLifecycle":true}}



## ARTIFACT candidate-allocation-offline-strategic-scenario/allocation-candidate.json

{"format":"vercy-model-allocation-candidate/v1","contourId":"EM-STR-01","proposedName":"Strategic Scenario","modelId":null,"registryId":null,"allocationState":"unassigned","decision":"NEW MODEL","canonicalPublishable":false,"identityTest":{"stableIdentity":"A versioned hypothesis space remains identifiable independently of strategies, forecasts and authoritative actuals.","versionIdentity":"Driver, assumption, method, uncertainty or projected-state changes create immutable successor versions.","independentLifecycle":["draft","reviewed","approved","published","active","invalidated","superseded","retired"],"mastership":"authorized strategic foresight authority"},"boundary":{"owns":["strategic-scenario identity","immutable scenario versions","drivers and varied assumptions","projected states","method and uncertainty","validity and defeat conditions","successor history"],"references":[{"target":"WM-KNW-007","purpose":"Hypothesis and claim"},{"target":"WM-KNW-010","purpose":"Decision rationale"},{"target":"WM-MAT-008","purpose":"Observation comparison"},{"target":"WM-REC-010","purpose":"Approval decision"}],"excludes":["authoritative actual","target baseline","observed outcome","benefit realization","strategy authority","causal fact"]},"objects":{"StrategicScenario":{"identity":["strategicScenarioId"],"required":["name","ownerRef","status"],"optional":["successorRef"]},"ScenarioVersion":{"identity":["strategicScenarioId","version"],"required":["drivers","assumptions","projectedStates","method","uncertainty","contentDigest"],"optional":["validityWindow","defeatConditions","supersedesVersion"]}},"invariants":["A scenario may be cited by many strategies.","Scenario authority never transfers to a citing strategy.","Assumptions have validity windows.","Assumptions have defeat conditions.","Competing explanations remain explicit.","Uncertainty is recorded.","Scenario output never becomes authoritative actual.","Scenario output never becomes target baseline silently.","Forecast remains forecast until qualified observation.","Published versions are immutable.","Invalidation preserves history.","Scenario state never mutates baseline status."],"holds":["Registry allocation is pending and no identifier may be guessed.","Independent Grok review and one frozen semantic audit are pending.","Capability and process realization remain blocked on legacy specifications.","Package conversion and live verification are pending."]}



## ARTIFACT candidate-allocation-offline-strategic-scenario/fixtures.json

{"format":"vercy-enterprise-allocation-fixtures/v1","candidateName":"Strategic Scenario","cases":[{"id":"shared-scenario","kind":"positive","input":"Two strategies cite one scenario version.","expect":"The scenario remains independently governed."},{"id":"defeated-assumption","kind":"positive","input":"A market assumption fails.","expect":"The scenario is invalidated without rewriting prior decisions."},{"id":"actual-feed","kind":"negative","input":"Projected revenue is loaded as authoritative actual.","expect":"The feed is rejected."},{"id":"baseline-mutation","kind":"negative","input":"Scenario divergence rewrites a target baseline.","expect":"The mutation is rejected."}]}



## ARTIFACT candidate-allocation-offline-strategic-scenario/validation-policy.json

{"format":"vercy-allocation-validation/v1","requirements":{"modelIdMustBeNull":true,"registryIdMustBeNull":true,"allocationState":"unassigned","minimumInvariants":8,"minimumReferences":3,"minimumFixtures":3,"requiresPositiveAndNegativeFixtures":true,"requiresStableIdentityStatement":true,"requiresIndependentLifecycle":true}}

