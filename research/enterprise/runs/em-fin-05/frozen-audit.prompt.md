# EM-FIN-05 frozen semantic audit

You are the single independent frozen auditor. Use no tools and do not browse. This call is one run only and must not be repeated.

Audit the frozen Cost Allocation dossier below. The non-negotiable guards are: do not invent or allocate identifiers; preserve quoted price, invoice amount, recognized cost, usage, allocated cost and valuation as distinct; reuse WM-FLW-015 usage and WM-MAT-008 plus Metric Definition for unit-cost observations; allocation cannot mutate invoice or journal masters.

Adjudicate the central provider divergence exactly: the current candidate is one identifier-unassigned Cost Allocation aggregate containing versioned Rule, immutable Run and Results, while Grok says Rule, Run and Result each need separate model identifiers and that an unassigned aggregate cannot be cited. Decide whether independent identity/lifecycle requires three identifier-unassigned candidates, one cluster candidate with internal addressable identities, or another held shape. Distinguish a model/catalogue identifier from an object-level stable identifier. No allocation approval may be inferred.

Find material semantic, identity, lifecycle, mastership, conservation, multi-axis, currency/time, correction, residual, discount, reserved-capacity, unit-economics, naming and fixture defects. Give exact mechanical remediations. Require one normative invariant set and machine-checkable positive/negative fixtures. Return: Verdict; numbered material defects; one fenced JSON array of exact additional fixtures; Freeze decision. State that this audit is spent and must not be rerun. Do not claim publication readiness.

## LOCAL

# EM-FIN-05 local synthesis

## Disposition

- Reject WM-ECO-002 Price / Valuation as the master for costs or allocations. It remains a price/valuation comparator only.
- Reuse WM-FLW-015 for Usage Records under a FinOps profile; reuse WM-MAT-008 plus the EM-DAT-05 Metric Definition candidate for Unit Cost Observations.
- Keep billed cost in WM-ECO-008 and recognized cost in WM-ECO-016. Derived effective, amortized, accrued-unbilled and allocated cost use typed, run-scoped Cost Records and never replace their source masters.
- Create one identifier-unassigned **Cost Allocation** aggregate candidate owning versioned Allocation Rule, immutable Allocation Run and contained Allocation Results. Separate model identifiers for Rule/Run/Result are not justified before registry review.
- Reuse commercial-contract or commitment authorities for reserved-capacity instruments; do not allocate another identifier merely because the dossier lacks their binding.
- Allocate no runtime/model identifier.

## Price, cost and usage boundaries

Quoted/list price, invoice amount, ledger-recognized cost, measured usage, allocated cost and valuation are distinct facts. Invoice allowances remain invoice-owned; ledger postings remain ledger-owned; usage remains source-qualified physical or computational consumption. An allocation produces an analytical attribution and is never a posting unless an authorized journal entry is separately created.

## Allocation aggregate

Allocation Rule has stable identity, immutable versions and effective periods. It declares one allocation axis, source scope, base kind and source, weight computation, rounding/tolerance, residual policy, confidence policy and authority.

Allocation Run pins one rule version, source amount/currency, source records, base population/completeness, execution actor/time and reconciliation result. Contained Allocation Results name target, amount, weight, base value, confidence and attribution basis. Corrections create successor runs.

Conservation holds within one run, one axis and one currency: allocated results plus visible residual equal the source amount within tolerance, and total weights do not exceed one. Parallel project and product views are non-additive. A report must select one run per source amount.

Reserved capacity separates covered usage from unused commitment capacity. Unused capacity is charged to a declared shared pool, allocated by its own rule or left as residual. Discounts retain the invoice allowance identity and gain only a run-specific attribution basis.

## Unit economics, currency and time

A Unit Cost Observation is numerator over denominator: a named cost basis and allocation run divided by a versioned functional-unit definition and measured quantity. It states period, currency, target scope and excluded residual share. Changing the useful-result definition creates a new metric-definition version.

Allocation occurs in the source currency. Translation records rate, type, date and authority per result. Billing period, usage interval, posting/effective dates, commitment period, run time and observation time remain separate.

## Acceptance scenario

A cloud invoice contains gross cost, discount and reserved-capacity effects. One project-axis run allocates metered usage to projects, sends unused reservation to a shared pool and leaves untagged usage as residual. One product-axis run uses a service-to-product rule and has a different residual. Each run conserves independently and cannot be summed with the other. Product unit cost cites the selected run, functional-unit definition and residual share.

## Invariants

1. Every cost assertion declares basis, period and currency.
2. Price, invoice, recognized cost, usage, allocation and valuation are never substituted.
3. Every run pins one immutable rule version.
4. Allocated results plus residual equal source amount within one run/axis/currency.
5. Total weights never exceed one; residual is materialized.
6. Parallel allocation axes over the same source are non-additive.
7. Allocation base kind and completeness are explicit.
8. Unused reserved capacity has a declared treatment.
9. Discount attribution retains the source allowance identity.
10. Allocation occurs before any currency translation of results.
11. Allocated cost is not a ledger posting.
12. Corrections append successor runs and preserve prior metric vintages.
13. Confidence separates measurement uncertainty, representativeness and residual share.
14. Unit cost pins numerator basis, allocation run and denominator definition version.

## Holds

All relevant bases remain non-canonical reviewable drafts; WM-ECO-002 has no approved outgoing relations, and usage/measurement models retain single-provider and allocation/profile holds. Cost Allocation and Metric Definition lack registry allocation; the contract/commitment binding, FOCUS/FIBO/ERP crosswalks, immutable pins and fixtures remain incomplete. This checkpoint makes no canonical completeness, installability or publication claim.


## CLAUDE STUDY

# EM-FIN-05 — Independent review

## Verdict

Reserved **WM-ECO-002 Price / Valuation is not an acceptable target** for this contour. Disposition is partial reuse plus two new candidates (identifiers unassigned):

- **UsageRecord** — reuse **WM-FLW-015 Resource Consumption** under a thin EM-FIN-05 profile; mint no new identity.
- **CostRecord** — no new master for billed or ledger-recognized cost; typed assertion with a mandatory `cost_basis` discriminator. Identity is minted **only** for derived bases (effective, amortized, accrued-unbilled, allocated).
- **AllocationRule** — **new**, independently identified and versioned, with **AllocationRun** and **AllocationResult** as separate identities.
- **UnitCostObservation** — **new** derived-metric identity; ALIGN to WM-ECO-002's amount/unit/time/provenance/uncertainty pattern, not mastered inside it.

Boundary decision: **new + profile**, not reuse of the reserved entry.

## Evidence

WM-ECO-002 `out_of_scope` names "accounting recognition, tax rules"; its Invoice/Payment boundary note states invoiced and paid amounts "are external accounting or settlement events; they may evidence price but do not become appraisal or index conclusions." Its cost bundle is replacement/reproduction cost *for valuation*, not incurred cost. A unit cost whose numerator is allocated recognized cost therefore cannot be mastered there without breaching its own stated boundary.

WM-FLW-015 already owns assertion-kind typing (metered/derived/allocated/estimated/modeled), gross/return/recovery/export/loss/net components, `shared-resource-allocation-driver-rule-basis-and-residual`, `functional-unit…normalizing-variable-and-intensity`, `allocate-shared-use` (outputs allocated assertions **plus residual**), and `reconcile-sources` rejecting last-write-wins. That is the usage side, already source-grounded.

WM-ECO-008 owns allowance/charge entries with reason code and their own tax category at line and document level, prepaid amount, document and tax-accounting currency. WM-ECO-016 owns per-ledger balancing, immutability, correction linkage and parallel-ledger divergence. WM-MAT-008 owns the measurement act.

## Identity/mastership

Independent identity and lifecycle: **AllocationRule**, **AllocationRun**, **AllocationResult**, **UnitCostObservation**, **CommitmentInstrument** (reserved capacity / savings commitment, if no contract master is available).

Reuse current masters, reference only: invoice and its allowances (WM-ECO-008), postings and recognized amounts (WM-ECO-016), measured usage (WM-FLW-015), meter observations (WM-MAT-008), market/quoted price and valuation (WM-ECO-002), allocation targets (project, product, responsibility centre — externally mastered).

AllocationRule needs its own identity because it is authored, approved, effective-dated and retired independently of any execution; AllocationRun needs its own because residual, confidence and reconciliation attach to an execution, not to the rule.

## Price/cost/usage boundaries

Six distinct facts, never interchangeable:

1. **Quoted/list price** — WM-ECO-002 price observation (advertised, quoted, administered).
2. **Invoice amount** — WM-ECO-008 line/document totals net of invoiced allowances.
3. **Ledger-recognized cost** — WM-ECO-016 posting in a named ledger, under that ledger's recognition policy.
4. **Measured usage** — WM-FLW-015 quantity with quantity kind, unit and net-component treatment.
5. **Allocated cost** — AllocationResult; derived, run-scoped, never a posting.
6. **Valuation** — WM-ECO-002 appraisal conclusion.

A rate card is (1), not (2). An invoice is not (3): commitment amortization, credits landing in later periods and accruals make them legitimately unequal. Allocated cost (5) is never posted back as (3) unless an explicit allocation posting is authorized as its own journal entry.

## Allocation rule and execution

AllocationRule declares: version and effective interval; **allocation axis** (the target dimension set, e.g. project *or* product); source scope (invoice, invoice group, cost pool, posting set); **allocation base** (metered usage, derived usage, headcount, revenue, fixed key, equal split) with the base's own assertion kind; base source binding; weight computation; rounding rule and tolerance; **residual policy**; confidence policy; authority and approval.

AllocationRun is immutable and records rule version, source amount and currency, base population and its completeness, execution time, actor, results, residual and reconciliation outcome. AllocationResult carries target reference, amount, weight, base value, confidence and the run reference.

**Duplication control (the negative case).** Conservation holds *within one run and one axis*: `Σ allocated + residual = source amount`, and `Σ weights ≤ 1`. Project-axis and product-axis runs over the same source are parallel views, each independently conserving. Cross-axis results are declared **non-additive**: any report summing allocated cost must name exactly one run per source amount, and summing two runs of the same source is a rejected operation. This is what prevents 100% of a shared invoice appearing against every product.

**Shared/reserved capacity.** Reserved or committed capacity is allocated in two layers: (a) covered usage attracts the commitment rate; (b) **unused reserved capacity** is an explicit cost with no consuming target and is allocated by a declared rule (spread, charged to a shared pool, or left in residual) — never silently absorbed into consumers' unit cost.

**Discounts.** Invoiced discounts are mastered in WM-ECO-008 as allowance entries with reason codes; EM-FIN-05 owns only their **attribution**: whether a discount follows the line it was granted against, is spread across the axis on the same base, or is held in a shared pool. Attribution basis is recorded per result so gross and net allocated views are both reproducible.

## Unit economics

UnitCostObservation = numerator (a stated CostRecord basis, one run, one axis) ÷ denominator (a functional unit taken from WM-FLW-015's normalizing variable). It must state numerator basis, run reference, denominator definition and version, period, currency, target scope and the unallocated share excluded. "Unit of useful result" is a declared, versioned choice (request, transaction, active tenant, delivered item), not a discovered fact; changing it creates a new definition version, not a restated metric.

## Currency/time

Allocate in the **source amount's currency**, then translate results with rate, rate type, rate date and source recorded per result. Never allocate a translated amount and re-translate. Residual carries its own currency. Where the source is an invoice, transaction currency and any tax-accounting currency are read from WM-ECO-008 and not re-derived.

Separate: billing period (invoice), usage interval (WM-FLW-015), accounting effective and posting dates (WM-ECO-016), commitment amortization period, allocation run execution instant, and metric as-of. Every cost and usage assertion states period and currency explicitly; date-only periods are not widened to instants.

## Reconciliation/correction

Three independent ties, each recorded with variance and reason rather than forced to zero: allocated total ↔ source invoice total; allocated/amortized total ↔ ledger-recognized cost for the period; allocation base ↔ measured usage population completeness. Unallocated remainder is reported, never suppressed.

Corrections are append-only: a superseding AllocationRun referencing its predecessor with reason (restated usage, corrected invoice, credit note, rule defect, base completeness fix). Prior runs and prior UnitCostObservation vintages remain resolvable. Invoice corrections arrive as WM-ECO-008 credit/corrective documents; ledger corrections as WM-ECO-016 reversing entries. Neither rewrites a run.

**Confidence** stays decomposed: measurement uncertainty (from usage/observation), base representativeness, commitment-coverage certainty, and unallocated share. No single collapsed score.

## Lifecycle

AllocationRule: draft → approved → effective → superseded → retired. AllocationRun: executed → reconciled → superseded (immutable throughout). AllocationResult: immutable, lives and dies with its run. UnitCostObservation: issued → superseded/withdrawn, preserving vintages. CostRecord: basis-dependent — billed and recognized follow their masters; derived bases are revisioned locally.

## Scenario

One shared cloud invoice: gross 100,000 EUR, invoiced volume discount 10,000, billed 90,000; plus a reserved-capacity commitment whose period amortization is 20,000, of which 4,000 is unused reservation.

- Amortized cost basis for the period: 90,000 + 20,000 − (commitment prepayment already invoiced, per prepaid amount) = a stated effective pool, recorded as one derived CostRecord with its computation.
- **Project run** (axis = project), base = metered compute usage: Project A 48,000, Project B 31,000, unused reservation 4,000 to shared pool, **residual 7,000** (usage from untagged resources, base incomplete). Σ = pool. Confidence: metered for A and B, estimated for the untagged share.
- **Product run** (axis = product), same pool, base = derived usage mapped via service-to-product rule v2: Product X 55,000, Product Y 29,000, **residual 6,000**. Σ = pool.
- Both runs conserve independently. Neither is summed with the other. A cross-axis report must name one run; the project+product sum of 174,000 against a 90,000-billed invoice is a rejected operation, which is precisely the negative case.
- Unit cost: Product X effective cost 55,000 ÷ 11.0m billable requests, with residual share 6.7% declared and run reference pinned.

## Invariants

1. Every cost assertion states `cost_basis`, period and currency.
2. Quoted price, invoice amount, recognized cost, measured usage, allocated cost and valuation are separately typed and never substituted.
3. AllocationRule is versioned; every run pins one rule version.
4. `Σ allocated + residual = source amount` within one run, one axis, one currency, to a declared tolerance.
5. `Σ weights ≤ 1`; the unallocated remainder is materialized and visible, never zero by default.
6. Allocated results from different axes/runs over the same source are non-additive.
7. Allocation base assertion kind and completeness are recorded per run.
8. Unused reserved capacity is an explicit cost with a declared treatment.
9. Discount attribution basis is recorded per result; gross and net views are both reproducible.
10. Allocation occurs in source currency; translation records rate, type, date and source.
11. Allocated cost is not a ledger posting unless an authorized allocation journal entry is created in WM-ECO-016.
12. Runs and metric vintages are immutable; correction supersedes with reason and preserves predecessors.
13. Confidence remains decomposed, not collapsed.
14. Unit cost states numerator basis, run reference, denominator version and excluded unallocated share.

## Minimal completion shape

EM-FIN-05 profile over WM-FLW-015 (usage, with allocation-axis and base-completeness constraints) + new AllocationRule / AllocationRun / AllocationResult + new UnitCostObservation + new CommitmentInstrument + typed references to WM-ECO-008 (invoice, allowances, prepaid), WM-ECO-016 (recognized cost, allocation postings), WM-MAT-008 (measurement evidence), WM-ECO-002 (price comparator only). Target masters (project, product, responsibility centre) referenced, never governed here.

## Holds

All four adjacent specifications are non-canonical reviewable drafts. WM-ECO-002, WM-FLW-015 and WM-MAT-008 carry single-provider waivers with external review explicitly waived; WM-ECO-002 has no approved outgoing relation rows, so a WM-ECO-002 edge cannot be relied on. WM-FLW-015 holds allocation, profile, measurement and impact items open; WM-MAT-008 is `boundary-review-required` with unverified cardinalities and an entry-kind mismatch between its registry record plane and its subject kind. Semantic crosswalks, registry allocation for the new candidates, immutable source pins, comparison-track validation (FIBO, UBL/FOCUS, XBRL/ERP policy) and fixtures are all absent. Jurisdictional cost-allocation, transfer-pricing and tax treatment are out of scope and unreviewed. This review makes no claim of canonical completeness, publication readiness or installability.


## GROK STUDY

Verdict: Conditional accept. Keep quoted price, invoice amount, recognized cost, usage, allocated cost, and valuation as distinct facts. Reuse WM-FLW-015 for usage and profile unit cost onto WM-MAT-008 plus Metric Definition. Reject an identifier-unassigned allocation aggregate. Rule, Run, and Result need separate model identifiers. UnitCostObservation can profile the existing observation and metric models and must not become a second observation master.

Strongest evidence: the six facts have different lifecycles and different masters. Quoted price is a commercial offer under WM-ECO-002 and is outside accounting recognition. Invoice amount is billed fact on WM-ECO-008 and can be disputed after usage is already recorded. Recognized cost posts only through WM-ECO-016 at period close. Usage quantity is operational and mastered by WM-FLW-015. Allocated cost is a derived view of a source amount. Valuation is not recognition. Collapsing any pair hides a dispute, a close, or a double count. The cloud case needs all six: a discount changes billed versus list, reserved capacity can be unused, and untagged usage must stay visible.

Strongest counterexample: one shared cloud invoice, list 1,200 in currency C for period T, invoice-level discount 120, billed 1,080. Reserved commitment 600, of which part is unused; on-demand covers the rest. Project A consumes part of the reserved pool and some on-demand. Product B attributes an overlapping slice of the same reserved pool by SKU. Ten percent of on-demand is untagged. If the project view and the product view are added, reserved cost is counted twice against the invoice and against WM-ECO-016. If unused reserved capacity is dropped, allocated plus residual no longer equals the source. If the discount is applied only to tagged usage, the untagged residual no longer reconciles to the billed net. A single run cannot be both axes at once.

Identity and mastership: do not mint masters for usage or unit cost. UsageRecord is a profile of WM-FLW-015 Resource Consumption; allocation never creates usage. UnitCostObservation profiles WM-MAT-008 Observation plus Metric Definition: subject, time, unit, and value stay with the observation; the profile adds cost numerator, usage denominator from WM-FLW-015, currency, window, and allocation-run context. It does not store allocation keys as a new identity. Billed amount stays on WM-ECO-008. Recognized amount stays on WM-ECO-016. WM-ECO-002 remains price and valuation only. Cost Records are typed derived facts pointing at a Result, not a new master and not a journal.

Allocation aggregate boundary: one Cost Allocation aggregate, root = Run. Rule is a versioned policy, referenced by version, reusable across runs, not exclusively owned. Run is the immutable execution identity that Cost Records and audit cite. Result lines are stable derived facts (target, amount, residual flag, source invoice reference, usage references) so a later explanation can point at a line. Leaving the aggregate identifier-unassigned blocks citation from derived Cost Records. Results never mutate Invoice or Journal Entry.

Unit economics: unit cost is computed, not mastered. Numerator is a stated cost basis (source slice, allocated amount, or recognized amount — named, not mixed). Denominator is usage from WM-FLW-015. A Metric Definition fixes the ratio. Discount timing is a versioned rule attribute: reduce the source before allocation, or carry discount as its own residual. Both are legal; silent netting is not. Unused reserved capacity is an explicit waste or residual result on the commitment, never omitted. Untagged usage stays in an unassigned residual. No implicit default tag.

Currency and time: each Run has one axis and one currency, equal to the source invoice slice. No implicit FX inside a run. Cross-currency lines are out of scope until a conversion rule exists. The run window is the source period. Rule version is pinned at run close. A closed run is immutable; a correction is a new run.

Scenario: source commitment 600 plus on-demand 400 = 1,000 list; discount 100; billed 900. Rule version: discount pro-rata on billed usage before allocation; unused reserved is residual waste; untagged is residual unallocated. Project-axis run allocates Project A and leaves residual for unused reserved and untagged. Product-axis run allocates Product B from the same source and leaves its own residual. Each run satisfies allocated plus residual equals source. The two runs are alternative partitions and must not be summed. Unit-cost observations profile WM-MAT-008 for each result basis. Neither run posts to WM-ECO-016.

Invariants:
1. Quoted price, invoice amount, recognized cost, usage quantity, allocated cost, and valuation are distinct facts.
2. Usage quantity is mastered only by WM-FLW-015.
3. Recognition posts only through WM-ECO-016; allocation does not post journals.
4. WM-ECO-002 does not perform accounting recognition.
5. Each Run has exactly one allocation axis and one currency.
6. Allocated amount plus residual amount equals source amount in the run currency.
7. Project-axis and product-axis results are alternative views and are non-additive.
8. Discount treatment is explicit on the pinned rule version.
9. Unused reserved capacity is an explicit residual or waste result.
10. Untagged usage remains residual or unassigned; no implicit tag.
11. Run is immutable after close; rule version is pinned on the run.
12. A Result never updates Invoice or Journal Entry masters.
13. Unit cost is a profiled observation over a Metric Definition, not a second usage record.
14. Cost Records are typed and derived; they cite a Result.

Minimum completion shape: aggregate specification with separate identifiers for Rule, Run, and Result; root = Run; rule referenced by version; conservation equation; non-additivity of parallel axes; explicit discount and unused-capacity result types; typed derived Cost Records; unit-cost profile on WM-MAT-008 plus Metric Definition; the shared-invoice scenario as the acceptance test.

Blockers: an identifier-unassigned aggregate cannot be cited by Cost Records. A new UnitCostObservation master would duplicate WM-MAT-008. Multi-currency source without a conversion rule breaks one-currency-per-run. Residual policy for discount versus unused capacity must be stated on the rule, not inferred. No model identifiers are assigned here.


## ALLOCATION

{
  "format":"vercy-model-allocation-candidate/v1",
  "contourId":"EM-FIN-05",
  "proposedName":"Cost Allocation",
  "modelId":null,
  "registryId":null,
  "allocationState":"unassigned",
  "decision":"NEW MODEL",
  "canonicalPublishable":false,
  "identityTest":{
    "stableIdentity":"A governed allocation remains identifiable across source-record corrections, rule revisions, allocation axes and reporting views.",
    "versionIdentity":"Rule changes create immutable effective-dated revisions; executions create immutable runs and corrections create successor runs.",
    "independentLifecycle":["draft","approved","effective","executed","superseded","retired"],
    "mastership":"cost-governance and finance-analytics authority"
  },
  "boundary":{
    "owns":["stable allocation-rule identity and immutable versions","immutable allocation runs pinned to one rule version and source population","contained allocation results and visible residuals","axis, base, rounding, tolerance, residual and confidence policy","run reconciliation and successor lineage"],
    "references":[
      {"target":"WM-ECO-002","purpose":"Price or valuation comparator only"},
      {"target":"WM-FLW-015","purpose":"Source-qualified usage records and allocation bases"},
      {"target":"WM-MAT-008","purpose":"Measured quantities and unit-cost observations"},
      {"target":"WM-ECO-008","purpose":"Billed amounts and invoice allowances"},
      {"target":"WM-ECO-016","purpose":"Recognized cost and journal postings"},
      {"target":"WM-ECO-012","purpose":"Budget or commitment context without replacing its mastership"}
    ],
    "excludes":["quoted or list price identity","invoice and allowance identity","journal-entry or posting identity","usage-event identity","valuation identity","metric-definition identity"]
  },
  "objects":{
    "CostAllocationRule":{"identity":["allocationRuleId"],"required":["axis","sourceScope","baseKind","baseSourceRef","residualPolicy","authorityRef","currentRevisionRef"],"optional":["successorRef"],"lifecycle":["draft","approved","effective","suspended","superseded","retired"]},
    "CostAllocationRuleRevision":{"identity":["allocationRuleId","revision"],"required":["weightComputation","roundingPolicy","tolerance","confidencePolicy","effectiveFrom","contentDigest"],"optional":["effectiveTo","supersedesRevision"]},
    "CostAllocationRun":{"identity":["allocationRunId"],"required":["ruleRevisionRef","sourceAmount","currency","sourceRecordRefs","basePopulation","baseCompleteness","executedAt","reconciliation"],"optional":["successorRunRef","actorRef"]},
    "AllocationResult":{"identity":["allocationRunId","resultId"],"required":["targetRef","amount","weight","baseValue","confidence","attributionBasis"],"optional":["residualReason"]}
  },
  "invariants":[
    "Every cost assertion declares basis, period and currency.",
    "Price, invoice, recognized cost, usage, allocation and valuation remain distinct facts.",
    "Every allocation run pins exactly one immutable rule revision.",
    "Allocated results plus visible residual equal the source amount within one run, axis and currency tolerance.",
    "Total allocation weights never exceed one and any remainder is materialized as residual.",
    "Parallel allocation axes over the same source are non-additive.",
    "Allocation base kind, source and completeness are explicit.",
    "Unused reserved capacity has an explicit shared-pool, separate-rule or residual treatment.",
    "Discount attribution retains the source invoice allowance identity.",
    "Allocation occurs in source currency before any translated result is derived.",
    "Allocated cost is an analytical attribution and never a ledger posting.",
    "Corrections append successor runs and preserve prior results and metric vintages.",
    "Confidence distinguishes measurement uncertainty, representativeness and residual share.",
    "Unit cost pins numerator basis, allocation run and denominator metric-definition version.",
    "Retired rule and run identifiers remain resolvable and are never recycled."
  ],
  "holds":["Independent Grok review is pending.","Registry namespace and identifier allocation are pending and no identifier may be guessed.","Metric Definition remains an unassigned EM-DAT-05 candidate.","Contract and commitment bindings, immutable pins, crosswalks and frozen audit remain incomplete.","All referenced bases remain non-canonical reviewable drafts."]
}


## PROFILE

{
  "format":"vercy-enterprise-profile-candidate/v1",
  "contourId":"EM-FIN-05",
  "name":"Enterprise Cost, Usage and Unit Economics Binding",
  "decision":"PROFILE",
  "newRuntimeId":false,
  "bases":["WM-ECO-002","WM-FLW-015","WM-MAT-008","WM-ECO-008","WM-ECO-016","WM-ECO-012"],
  "constraints":[
    "WM-ECO-002 remains a price or valuation comparator and never masters allocated cost.",
    "WM-FLW-015 owns source-qualified usage while WM-MAT-008 owns measured observations.",
    "WM-ECO-008 owns billed amounts and allowances; WM-ECO-016 owns recognized postings.",
    "Derived effective, amortized, accrued-unbilled and allocated costs retain typed source references and never replace source masters.",
    "Unit-cost observations pin a cost basis, allocation run, metric-definition version, measured quantity, period, currency and residual share.",
    "Parallel allocation views are selected independently and never summed as distinct costs."
  ],
  "holds":["Cost Allocation and Metric Definition registry allocation is pending.","Independent Grok review and frozen audit are pending.","Base canonical and relationship holds remain unresolved."]
}


## FIXTURES

{
  "format":"vercy-enterprise-allocation-fixtures/v1",
  "candidateName":"Cost Allocation",
  "cases":[
    {"id":"project-axis-conservation","kind":"positive","input":"A cloud invoice has a discount, reserved-capacity effects, tagged project usage and untagged usage.","expect":"One project-axis run retains invoice allowance identity, allocates tagged usage, routes unused reservation by policy, exposes untagged residual and reconciles to the source amount."},
    {"id":"product-axis-independent","kind":"positive","input":"The same invoice is allocated by a separate service-to-product rule.","expect":"The product run reconciles independently and is explicitly non-additive with the project run."},
    {"id":"unused-capacity-shared-pool","kind":"positive","input":"Reserved capacity exceeds measured covered usage.","expect":"The unused share is charged to the declared shared pool, allocated by a separate rule or materialized as residual."},
    {"id":"weights-over-one","kind":"negative","input":"Allocation weights total 1.08 and no residual or correction exists.","expect":"The run is rejected because weights exceed one and conservation fails."},
    {"id":"missing-base-completeness","kind":"negative","input":"A usage-based run omits whether its meter population is complete.","expect":"The run is rejected because base population and completeness are mandatory."},
    {"id":"translate-before-allocation","kind":"negative","input":"Invoice components are converted independently before allocation, producing inconsistent rounding.","expect":"The run is rejected; allocation must occur in source currency before translated results are derived."},
    {"id":"allocation-posting-overwrite","kind":"negative","input":"An analytical allocation is treated as a ledger posting and a later correction overwrites the run.","expect":"Both actions are rejected; posting requires a separate authorized journal entry and correction requires a successor run."}
  ]
}

