**Verdict.** Accept both candidate types as specified; neither is a new root. FinanceLandscape is a governed profile declaration plus an immutable reproducible projection. FinanceViewPolicy is a pinned policy/rule revision. Operational close of the prescribed test is blocked by required-but-unallocated dependencies. Do not claim publication readiness.

**Candidate types.** FinanceLandscape: ACCEPT, non-root. FinanceViewPolicy: ACCEPT, non-root. Identity of each is compositional over pins and revisions. Mastership stays with reused objects.

**Dependency gaps.** Required but not allocated: Responsibility Centre; Consolidation Scope; Consolidation Run; Chart of Accounts; Chart of Accounts Mapping; Cost Allocation; Metric Definition; FX Rate Set; Intercompany Match. Reuse of WM-ECO-012/015/016/017/018, WM-ORG-012, WM-ECO-038, and WM-MAT-008 is necessary and covers the completed-draft domains (budget/plans, accounts, journal postings, balances, financial statements, organization relationships, holdings, observations) as a bundle. That reuse is not sufficient to execute the test.

**Strongest evidence.** A finance view is a function of already-mastered facts under pinned revisions. Separating profile-plus-projection from the rule freeze, refusing new roots, and listing the pin set (books, ledger revisions, periods, scenarios, framework, mapping, responsibility scope, consolidation run, rate set, transformations, allocation, knowledge cut, residual policy) makes the two-book / three-currency / plan–actual / intercompany-elimination / unallocated-cost test reproducible without duplicating books, ledgers, or statements. Preserve-source-facts and expose-residuals follow from “projection, not root.”

**Strongest counterexample.** A group total that adds Book A USD plan to Book B EUR actual, silently drops the unallocated cost, and nets an intercompany pair without pinned Intercompany Match, Consolidation Run, and FX Rate Set. That figure is not a landscape fact. Giving FinanceLandscape root identity would let identical pin-sets drift as separate masters. Treating WM-ORG-012 units as Responsibility Centres, or writing eliminations, translations, or allocations back as source postings, is the same class of error.

**Identity / mastership.** Landscape identity equals governed profile plus the complete pin set; same pins yield the same projection. ViewPolicy identity equals policy family plus revision; an edit is a new revision. Monetary and observational mastership remain on source facts in the reuse bundle. Landscape is not a second book. Projection rows are derived and addressable to source.

**Landscape / policy.** Landscape declares what is in view and holds the frozen projection artifact. ViewPolicy declares how the projection is computed. The same profile under two policy revisions yields two landscapes. Do not collapse declaration and rules into one object: a policy change would rewrite the landscape identity contract. Neither object owns Chart of Accounts/Mapping, FX Rate Set, Consolidation Scope/Run, or Responsibility Centre; those are required pins, not types allocated here.

**Plan / actual.** Plans, forecasts, postings, balances, statements, observations, and derived rows stay separate. Plans and forecasts are scenario-bound intended amounts, not journal postings. Actuals flow posting → balance → statement. Comparison is a derived projection, valid only when both sides share pinned period, mapping, responsibility scope, and currency policy. Raw side-by-side difference is allowed under matching pins; governed variance metrics remain a gap until Metric Definition is allocated.

**Books / responsibility.** Landscape pins books and responsibility scope; it does not own them. The two-book test keeps Book A and Book B distinct. Cross-book totals require authorized cross-book transformations on the pinned ViewPolicy. Responsibility Centre is required and unallocated. WM-ORG-012 organization relationships are not implicit responsibility centres. An RC may sit inside one book or span books; that relation is declared, not inferred.

**Consolidation / elimination.** Perimeter, match set, elimination rows, source postings, and statement lines stay separate. The two-book intercompany test requires pinned Consolidation Scope, Consolidation Run, and Intercompany Match—all unallocated. Elimination is a derived transformation under authorized cross-book rules. Unmatched intercompany items stay visible; they are not netted into silence.

**Currency / comparability.** Source facts stay in original currency. Translation produces derived rows only. Combined totals across the three test currencies are blocked unless an authorized FX Rate Set and translation method are pinned. Cross-book plus cross-currency totals require both authorized rate and authorized cross-book transformations. FX Rate Set is required and unallocated, so comparability is a dependency gap, not something Landscape can invent.

**Allocation / residual.** Cost Allocation is required and unallocated. Allocation yields derived rows only. The test’s unallocated cost remains an explicit residual under the pinned residual policy. Unmatched and unallocated residuals are first-class projection outputs, not plug figures. Residual policy is a ViewPolicy pin, not an implicit close.

**Time / provenance.** Period, ledger revision, and knowledge cut are mandatory pins. The projection is as-of the knowledge cut, not wall clock. Source posting time stays on source facts. Derived rows carry provenance to source fact, rule revision, and transformation step. Restatement is a new projection under new pins or a new ViewPolicy revision. Issued projections are immutable.

**Governance.** Declaring a landscape profile and pinning a ViewPolicy are governed acts. Combined totals are unauthorized unless both an authorized FX Rate Set and authorized cross-book transformations are pinned. Residuals must remain visible; suppression is a governance defect. No silent consolidation, currency restatement, or allocation.

**Scenario.** Scenario is pinned separately from book, period, and ledger revision. Plan, forecast, and actual remain distinct fact classes. Plan/actual comparison is a projection over two pinned scenarios, not a third mixed book. A scenario change without a new landscape or policy pin must not rewrite source postings.

**Invariants.**
1. Landscape identity equals governed profile plus the complete pin set; incomplete pins cannot issue a landscape.
2. Issued projections are immutable; restatement requires new pins or a new ViewPolicy revision.
3. Source postings, balances, holdings, and observations remain masters; landscape rows are derived and addressable to source.
4. ViewPolicy is a revision freeze; rule change is a new revision, never an in-place mutate.
5. Plan, forecast, and actual streams stay disjoint; comparison is a projection over pinned scenarios, not a merged ledger.
6. Plan/actual comparison requires shared pinned period, mapping, responsibility scope, and currency policy.
7. Books remain distinct pinned references; organization units from the reuse bundle are not implicit Responsibility Centres.
8. Cross-book totals require authorized cross-book transformations pinned on the ViewPolicy.
9. Cross-currency combined totals require a pinned authorized FX Rate Set and translation method; source currency is preserved on source facts.
10. Elimination is admissible only against pinned Consolidation Scope/Run, Intercompany Match, and authorized cross-book transformation; unmatched intercompany items stay visible.
11. Allocation emits derived rows only; unallocated cost remains an explicit residual under pinned residual policy.
12. Knowledge-cut and ledger-revision pins are mandatory; combined totals that absorb residuals or lack authorized rate and cross-book transforms are blocked.

**Minimum model set.** FinanceLandscape; FinanceViewPolicy; two books with pinned ledger revisions; three currencies; plan scenario and actual scenario; period; framework; mapping; responsibility scope; consolidation run; FX rate set; authorized cross-book transformations; intercompany match; cost allocation; residual policy; knowledge cut; source postings and balances; plus the reuse bundle WM-ECO-012/015/016/017/018, WM-ORG-012, WM-ECO-038, WM-MAT-008. Holdings and observations are included when those facts are in the perimeter.

**Blockers.** The unallocated required types listed under dependency gaps. Any combined multi-book or multi-currency total lacking pinned authorized FX Rate Set and cross-book transformations. Missing Intercompany Match (elimination test cannot run). Missing Cost Allocation or residual policy (unallocated cost cannot be exposed). Missing Consolidation Scope/Run (no governed perimeter). Missing Chart of Accounts/Mapping (books not comparable). Missing Responsibility Centre (responsibility-scope pin fails). Missing Metric Definition (statement metrics ungoverned). Treating Landscape or Policy as new roots. Silent absorption of unmatched or unallocated amounts.
