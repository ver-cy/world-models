## DECISION

Three-part decision:

1. **REUSE ONLY — WM-ECO-012 for budget.** No new budget model. Identity, immutable revisions, scenarios, ceilings, funding sources, allocation/allotment, amendments, forecasts, actual references and variance are all present.
2. **PROFILE — EM-FIN-01 profile over WM-ECO-012.** A thin, non-structural profile that makes the responsibility-centre reference mandatory and version-pinned on line, allocation and availability, and that raises conservation from prose to an enforced invariant.
3. **NEW MODEL — Responsibility Centre**, cross-domain master, entry kind `entity`. No numeric identifier assigned; registry allocation is separate.

Funding allocation stays **owned by WM-ECO-012**; it does not get its own aggregate.

## BUDGET REUSE BOUNDARY

Tested capability by capability against the dossier:

| Tested | Covered by |
|---|---|
| Budget identity, owner, immutable revision | `budget-identity-purpose-and-owner`; `register-budget` |
| Period, basis, currency | `planning-horizon…`, `cash-accrual-commitment-statistical-basis-and-currency` |
| Scenarios | `baseline-economic-operational-assumptions-and-scenario` (required, 1) |
| Ceilings, envelope, allotment, availability | `ceiling-envelope-allocation-allotment-and-availability`; `set-ceiling-or-envelope` |
| Funding sources, earmarks, restrictions, release | `financing…funding-source`, `funding-source-earmark-restriction-and-release` |
| Allocation | `allocate-and-release-funds` |
| Amendments, transfers, carry-forward | `amend-transfer-or-carry-forward` |
| Forecasts | `reforecast-budget` (versioned separately from approved amounts) |
| Actual references | `bind-execution-reference` (references without importing ledger lifecycle) |
| Variance | `assess-variance-performance-and-risk` |

Nothing is missing. The one genuine gap is not a budget capability: WM-ECO-012 pins *organizational classification code-list versions*, i.e. a code list, not a governed entity with manager, basis, ledger binding and lineage. Its own boundary note already disclaims ownership of organization structure. The profile therefore adds only: (a) responsibility-centre reference as a version-pinned reference rather than a classification code; (b) a required funding-source identifier on each allocation and availability record; (c) the conservation invariant below. No new findings, no new functions.

## RESPONSIBILITY CENTRE PROOF

**Non-conflation, from dossier evidence.** WM-ORG-002 states finance is authoritative for cost centres, that unit identifiers and ERP cost-centre codes are not the same identity, and excludes cost accounting and segment reporting from scope; "cost centre" appears there only as a *unitKind* code — a classification of a unit, not centre identity. WM-ORG-004 carries `cost centre code` as a 0..1 code, explicitly "distinct from the organizational holder" — a consumer with no lifecycle. WM-ECO-016 carries cost centre as an analytical attribute on an immutable posting line and excludes budgeting; a posted dimension value is a *pin*, not a master. A legal entity is WM-ORG-001/GLEIF-scoped and, per WM-ORG-002, never issued to an internal division. A budget line is an estimate inside one revision. Catalogue search found no model and no reserved entry: consumed everywhere, mastered nowhere.

**Independent lifecycle.** Unit acts (reparent, merge, split, disband) and centre acts diverge in both directions: a unit can move with no accountability change, and accountability can move with no unit change. WM-ORG-002's own IFRS 8 note shows derived financial views must restate on reorganization — which is only possible if the centre is versioned separately from the unit.

**Fields (16).** centreId · centreVersionId + effectiveInterval (world/record) · centreType (cost/profit/revenue/investment/discretionary) · name · aliasCode[] (scheme + validity; ERP codes live here) · accountableManagerRef (position, not person) + validity · accountabilityScope (controllable cost / revenue / capital) · legalEntityRef[] + validity · ledgerRef + chart/segment binding + validity · measurementBasis (cash/accrual/commitment/statistical) · currencyRef (embeds WM-XCT-032) · parentCentreRef + hierarchyName · associatedOrgUnitRef[] (non-authoritative, dated, many-to-many) · lifecycleStatus · successionAct (predecessor/successor edges, act kind, split weights) · postingEligibilityWindow · recordAuthorityRef + evidenceRef · contentDigest.

**Invariants (12).**
1. Identity is minted; no unit id, ERP code or ledger dimension value may serve as primary identity.
2. Versions of one centre have non-overlapping, gapless effective intervals.
3. A posting resolves to the version effective at its accounting effective date; no later act rewrites that pin.
4. Unit reorganization never mutates an existing centre version — only creates a successor or a new centre with lineage.
5. Merge/split conserves: every predecessor has ≥1 successor edge, and no period amount is attributed to more than one successor without a declared split rule.
6. Alias codes are non-identifying, validity-dated, and resolve to at most one centre per instant.
7. Exactly one accountable manager position per centre per instant.
8. Currency and measurement basis are explicit on every version; changing either creates a version.
9. Ledger/legal-entity binding is version-scoped; postings into an unbound ledger are refused.
10. centreType bounds admissible measures; reclassification is an evidenced act, not an edit.
11. Acyclicity and single parent per named centre hierarchy per interval.
12. No deletion while any posting, allocation or forecast references any version; closure yields a tombstone with successor pointer.

**Functions (4).** `resolve-centre-as-of` · `apply-centre-succession-act` · `reconcile-centre-attribution` · `project-centre-dimension` (version-pinned crosswalk with fidelity/loss declaration).

## FUNDING ALLOCATION CONTRACT

Source, destination, amount/weight, basis, residual rule, effective period, restrictions and authority are all already inside WM-ECO-012's allocation/availability and funding-source findings and its `allocate-and-release-funds` and `authorize-budget` functions. A separate aggregate would split availability from the envelope that bounds it and would re-import authorization — the opposite of conservation. Allocation therefore stays with WM-ECO-012, profiled with: every allocation carries exactly one funding-source identifier; Σ allocations per source ≤ released amount for that source and period; a residual rule is mandatory and residual must reconcile to zero; destination is a centre **version** reference.

Residual risk, stated as a hold: when two sources sit in *different* budget aggregates, no single aggregate owns conservation. The profile handles this by requiring a shared funding-source identity and a source-side released-amount reference; it is not sufficient to promote allocation to its own aggregate.

## ACCEPTANCE WALKTHROUGH

Sources S1 (restricted grant) and S2 (own funds) fund project P through budget B revision r1, destination centre C@v1. Availability is computed per source, so neither amount can be released twice (profile invariant, plus WM-ECO-012 availability separation).

Reorganization at T: the unit moves under `apply-reorganization-act` in WM-ORG-002. If accountability also moves, `apply-centre-succession-act` writes C@v2 from T. Postings before T remain pinned to C@v1 (invariant 3); the negative case — past expenditure rewritten under a new centre — is structurally impossible.

Budget revision r2 via `amend-transfer-or-carry-forward`: r1 stays immutable, forecast is versioned by `reforecast-budget`, actuals are untouched. Reconciliation runs original / revised / forecast / allocation / actual on the centre dimension, rolled up across v1 and v2 by lineage. No reallocation is emitted by the reorganization, so no amount becomes available twice.

## HOLDS AND PUBLICATION RECOMMENDATION

Publish the profile and the Responsibility Centre model as **reviewable draft, publishableCanonical false** — no higher grade than its anchors. Holds: WM-ECO-012 is a single-provider waiver with an empty relationship ledger, so centre↔budget composition links stay draft pending registry governance; the centre model is cross-domain and should not repeat a single-provider waiver — dual-provider review is required before promotion; ledger and posting bindings depend on WM-ECO-015/WM-ECO-016, both unverified at field level; IFRS 8, W3C ORG, SAF-T, IPSAS and GFSM are named as **alignment only, never conformance**; jurisdictional appropriation, segment-reporting and delegated-authority rules require specialist review; no numeric identifier is assigned here.
