# Frozen no-tools semantic audit — EM-FIN-01

You are the final static semantic auditor. Use only this frozen packet. Do not browse, call tools, invent identifiers, mutate registry reservations or grant publication authority.

Disposition: reuse WM-ECO-012 Budget; add a thin Budget Responsibility profile; retain Responsibility Centre as an identifier-unassigned NEW MODEL; keep Funding Allocation inside WM-ECO-012. Audit semantics only.

Audit questions:
- Does Responsibility Centre prove identity and lifecycle independent of organizational unit, position, legal entity, ERP alias, budget line and journal posting?
- Are centre versioning, alias changes, bitemporal evidence, accountability, hierarchy, closure and merge/split semantics internally consistent?
- Does the Budget Responsibility profile conserve every funding source across revisions and cross-budget draws without duplicating authority?
- Do original, revised, forecast, commitment and actual states remain distinct while historical centre attribution stays immutable?
- Which holds permit research packaging but block identifier allocation or canonical publication?

Return at most 600 words with exactly: Verdict (ACCEPT WITH LIMITS, REVISE, or REJECT); Critical findings; Required holds; Scenario result; Identifier decisions. Registry mutation and identifier allocation remain holds.

## Responsibility Centre candidate

{
  "format": "vercy-model-allocation-candidate/v1",
  "contourId": "EM-FIN-01",
  "proposedName": "Responsibility Centre",
  "modelId": null,
  "registryId": null,
  "allocationState": "unassigned",
  "decision": "NEW MODEL",
  "canonicalPublishable": false,
  "identityTest": {
    "stableIdentity": "A finance-governed accountability unit survives ERP code, manager, organizational placement and budget changes while retaining historical attribution.",
    "versionIdentity": "Every accountability, ledger, legal-entity, currency, measurement-basis, hierarchy, centre-type or posting-eligibility change creates an effective-dated centre version; alias-only changes append a dated AliasBinding unless financial meaning changes.",
    "independentLifecycle": [
      "proposed",
      "active",
      "restricted",
      "closed",
      "superseded"
    ],
    "mastership": "finance master-data authority"
  },
  "boundary": {
    "owns": [
      "persistent responsibility-centre identity",
      "effective-dated immutable centre versions",
      "centre type and dated alias or ERP-code bindings",
      "accountable position reference and accountability scope",
      "legal-entity ledger chart-segment currency and measurement-basis bindings",
      "finance hierarchy and organizational-unit associations",
      "posting-eligibility window",
      "merge split and succession lineage"
    ],
    "references": [
      {
        "target": "WM-ECO-012",
        "purpose": "Budget revisions and funding allocations"
      },
      {
        "target": "WM-ORG-002",
        "purpose": "Associated organizational units"
      },
      {
        "target": "WM-ORG-004",
        "purpose": "Accountable positions"
      },
      {
        "target": "WM-ECO-016",
        "purpose": "Journal entries and historical postings"
      },
      {
        "target": "WM-XCT-032",
        "purpose": "Currency and monetary-value semantics"
      }
    ],
    "excludes": [
      "organizational-unit or position identity",
      "legal-entity or ledger identity",
      "budget line or funding-allocation lifecycle",
      "journal posting or actual transaction lifecycle",
      "person data copied from the accountable position holder"
    ]
  },
  "objects": {
    "ResponsibilityCentre": {
      "identity": [
        "centreId"
      ],
      "required": [
        "name",
        "financeAuthorityRef",
        "status"
      ],
      "optional": [
        "successorRefs",
        "closedAt"
      ],
      "lifecycle": [
        "proposed",
        "active",
        "restricted",
        "closed"
      ]
    },
    "CentreVersion": {
      "identity": [
        "centreId",
        "version"
      ],
      "required": [
        "centreType",
        "accountabilityScope",
        "accountablePositionRef",
        "ledgerBinding",
        "effectiveFrom",
        "recordedAt",
        "contentDigest",
        "status"
      ],
      "optional": [
        "effectiveTo",
        "legalEntityRef",
        "currencyRef",
        "measurementBasisRef",
        "supersedesVersion"
      ],
      "lifecycle": [
        "draft",
        "active",
        "superseded",
        "withdrawn"
      ]
    },
    "AliasBinding": {
      "identity": [
        "aliasBindingId"
      ],
      "required": [
        "centreRef",
        "codeSystemRef",
        "code",
        "validFrom"
      ],
      "optional": [
        "validTo",
        "sourceRef"
      ]
    },
    "HierarchyMembership": {
      "identity": [
        "membershipId"
      ],
      "required": [
        "childCentreVersionRef",
        "parentCentreVersionRef",
        "validFrom",
        "authorityRef"
      ],
      "optional": [
        "validTo",
        "hierarchyKind"
      ]
    },
    "SuccessionRule": {
      "identity": [
        "successionRuleId"
      ],
      "required": [
        "predecessorRefs",
        "successorRefs",
        "effectiveAt",
        "reconciliationRule",
        "authorityRef"
      ],
      "optional": [
        "weights",
        "evidenceRefs"
      ]
    }
  },
  "invariants": [
    "Centre identity is minted and is never an organizational-unit identifier, ERP code, budget-line identifier or journal dimension value.",
    "Centre versions have non-overlapping effective intervals and preserve both world-effective and record-time evidence.",
    "A posting pins the centre version effective at its accounting effective date; later reorganization never rewrites that pin.",
    "An organizational move with unchanged finance accountability does not mint a new centre identity or version.",
    "A finance-accountability, centre-type, ledger, legal-entity, currency, measurement-basis, hierarchy or posting-eligibility change creates a successor version.",
    "Merge and split lineage declares explicit weights or a reconciliation rule and never double-attributes a period amount.",
    "Alias codes are non-identifying, validity-dated and resolve to at most one centre per instant and code system.",
    "Exactly one accountable position is effective per centre version and instant; person identity is never copied into the centre master.",
    "Currency, measurement basis, legal entity and ledger/chart-segment bindings are explicit and version-scoped.",
    "Finance hierarchies are acyclic, have at most one parent per named hierarchy and interval, and may differ from organizational hierarchies.",
    "Closed and superseded versions remain resolvable for historical attribution and cannot be deleted while referenced.",
    "Posting eligibility is effective-dated and does not erase prior valid postings.",
    "Budget revision never mutates responsibility-centre history or journal facts.",
    "Unknown source authority, amount, currency, measurement basis or remainder rule never defaults to zero or unrestricted availability."
  ],
  "holds": [
    "Registry identifier allocation is pending and no numeric gap may be guessed.",
    "WM-ECO-012 and neighbouring finance models remain reviewable drafts with unapproved outgoing relations.",
    "Ledger, chart-segment and posting bindings require field-level validation against WM-ECO-015 and WM-ECO-016.",
    "Jurisdiction-specific appropriation, delegated-authority and segment-reporting controls require specialist review.",
    "IFRS 8, W3C ORG, SAF-T, IPSAS and GFSM remain alignment targets only, never conformance claims.",
    "One frozen semantic audit is pending after provider reconciliation.",
    "Package conversion and live verification are pending."
  ],
  "candidateRevision": 2
}


## Budget Responsibility profile

{
  "format": "vercy-enterprise-profile-candidate/v1",
  "contourId": "EM-FIN-01",
  "name": "Budget Responsibility",
  "decision": "PROFILE",
  "bases": [
    "WM-ECO-012"
  ],
  "newRuntimeId": false,
  "canonicalPublishable": false,
  "constraints": [
    "Every budget line, allocation, allotment and forecast line pins an exact responsibility-centre version.",
    "Every allocation identifies one funding-source base, destination centre version, amount or weight, basis, effective period, restrictions, authority and named remainder rule.",
    "For one source and applicable period, allocated plus reserved plus lapsed less carry-in never exceeds the source-side authorized amount in the same currency and measurement basis.",
    "Residual equals authorized minus allocated minus reserved minus lapsed plus carry-in and is reconciled explicitly; unknown never means zero.",
    "A successor budget version does not increase source availability unless the source authorization is amended.",
    "Cross-budget use of one source records the draw once in the source authority; receiving budgets reference that draw.",
    "Commitments and actuals consume or evidence availability and never create it.",
    "Quantization residuals follow pinned WM-XCT-032 allocation and residual rules.",
    "Original budget, revised budget, forecast, commitment and actual remain separately based states and never mutate one another.",
    "Period, currency code-list edition and measurement basis are mandatory and version-pinned."
  ],
  "candidateRevision": 2
}


## Fixtures

{
  "format": "vercy-model-allocation-fixtures/v1",
  "proposedName": "Responsibility Centre",
  "cases": [
    {
      "id": "code-change",
      "kind": "positive",
      "input": "An ERP cost-centre code changes while finance accountability and posting semantics are unchanged.",
      "expect": "Centre identity and CentreVersion remain; a dated non-identifying AliasBinding changes."
    },
    {
      "id": "accountability-change",
      "kind": "positive",
      "input": "Ledger scope and accountable position change during reorganization.",
      "expect": "A successor CentreVersion becomes effective; historical postings remain pinned to the prior version."
    },
    {
      "id": "organization-move-only",
      "kind": "positive",
      "input": "An associated organizational unit moves while finance accountability is unchanged.",
      "expect": "No centre identity or version is minted merely from the organization move."
    },
    {
      "id": "split-reconciliation",
      "kind": "positive",
      "input": "One centre splits into two successors.",
      "expect": "Lineage records weights or an explicit reconciliation rule and preserves the predecessor for historical resolution."
    },
    {
      "id": "multi-source-revision",
      "kind": "positive",
      "input": "Two sources fund one project, then the organization and budget are revised.",
      "expect": "Postings retain the effective CentreVersion; V1, V2, forecast, commitments and actuals stay distinct; source authority is counted once."
    },
    {
      "id": "double-funding",
      "kind": "negative",
      "input": "Allocations from one source exceed its authorized released amount for the period.",
      "expect": "The Budget Responsibility profile rejects the allocation set."
    },
    {
      "id": "successor-double-availability",
      "kind": "negative",
      "input": "Budget V2 treats V1 source authorization as newly available without an amended source authorization.",
      "expect": "The profile rejects the successor revision as duplicate availability."
    },
    {
      "id": "unknown-as-zero",
      "kind": "negative",
      "input": "A source amount or remainder rule is unknown and the implementation treats it as zero or unrestricted.",
      "expect": "Validation fails closed."
    },
    {
      "id": "historical-rewrite",
      "kind": "negative",
      "input": "A reorganization rewrites prior journal attribution from CentreVersion v1 to v2.",
      "expect": "Validation rejects the rewrite and preserves the original pin."
    }
  ],
  "candidateRevision": 2
}


## Local evidence

# EM-FIN-01 local synthesis

## Disposition

- **Reuse WM-ECO-012 Budget** for budget identity, immutable revisions, scenarios, ceilings, funding sources, allocations, amendments, forecasts, actual references and variance.
- Create a thin **EM-FIN-01 Budget Responsibility profile** requiring version-pinned responsibility-centre references and source-side conservation rules.
- Research a **new Responsibility Centre entity**. Its identifier remains unassigned.
- Keep Funding Allocation inside WM-ECO-012.

## Responsibility Centre boundary

A responsibility centre is a finance-governed accountability unit whose lifecycle differs from organizational units, positions, legal entities, budget lines and journal postings. Published models already consume cost-centre codes but no authoritative centre master or reserved registry entry exists.

Owned semantics: persistent centre identity; immutable/effective-dated versions; centre type; aliases and ERP codes; accountable position; accountability scope; legal-entity, ledger, chart/segment and currency bindings; hierarchy; associated organizational units; succession and split/merge rules; posting-eligibility window; authority and evidence.

## Key invariants

1. Centre identity is never an organizational-unit id, ERP code or journal dimension value.
2. Centre versions have non-overlapping effective intervals.
3. A posting pins the centre version effective at posting/accounting time.
4. Reorganization never rewrites historical postings.
5. Centre merge/split creates lineage with explicit weights or reconciliation rules.
6. Alias codes are dated and resolve to one centre per instant.
7. Accountability is assigned to a position/role reference, not copied person data.
8. Currency, measurement basis and ledger binding are explicit and version-scoped.
9. Hierarchies are acyclic and may differ from organizational hierarchies.
10. Referenced versions remain resolvable after closure.

## Funding allocation profile

Every allocation declares source, destination centre version, amount or weight, allocation basis, effective period, restrictions, authority and residual rule. The sum of allocations from one released source cannot exceed the released amount for that period. Residual reconciliation is mandatory. Cross-budget conservation requires a shared funding-source identity and source-side released-amount authority.

## Acceptance result

Two sources fund a project through Budget revision r1 and Centre v1. Reorganization creates Centre v2 only when financial accountability changes; previous postings remain pinned to v1. Budget revision r2 and its forecast do not mutate r1 or actuals. Reconciliation rolls up v1/v2 through centre lineage while source-side conservation prevents double availability.

## Holds

WM-ECO-012 is a reviewable draft under a single-provider waiver and lacks approved relations. The Responsibility Centre model needs independent review, registry allocation, ledger/posting field validation and jurisdiction-specific finance review. Standards remain alignment targets only.


## Claude study

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


## Grok study

## DECISION



Justified combination: **reuse WM-ECO-012** for the budget aggregate; add a **thin enterprise profile** on that model; create a **new cross-domain Responsibility Centre entity**. Reject REUSE ONLY. Do not create a separate Funding Allocation aggregate. Do not assign a numeric model identifier.



WM-ECO-012 already owns the governed plan: identity and revision, scenarios, ceilings and envelopes, funding sources, allocation and allotment, amendments, forecasts, actuals as external references, and variance. The assignment still fails if those records treat a cost-centre code as an organizational-unit alias, or if a revision can mint the same source amount twice. EM-FIN-01 states the contour directly: an organizational unit need not coincide with a financial centre. No published Vercy model masters that centre. Classifying a unit as a cost centre inside WM-ORG-002 does not close the gap.



## BUDGET BOUNDARY



Reuse WM-ECO-012 for Budget, BudgetVersion and BudgetScenario. In-scope there, and not to be forked: purpose and owner; period and recognition basis; currency and unit; ceilings, envelopes, allocation, time-phased allotment and availability; funding sources with earmark, restriction, matching and release; amendments, transfers, carryover, lapse, freeze and cancellation; forecasts held separately from the approved revision; commitment and actual bindings that preserve external mastership; plan / forecast / commitment / actual / cash variance.



Out of the budget boundary: Responsibility Centre master lifecycle; ledger posting (WM-ECO-016); organizational-unit and position masters (WM-ORG-002, WM-ORG-004); consumption and cost-allocation algorithms (EM-FIN-05). Funding Allocation stays a structured record inside the budget version (ceiling → envelope → allocation → allotment → availability). Extracting it would split conservation across two roots and recreate double availability. Cross-budget use of one source is a referenced draw on that source, not a second aggregate. EM-FIN-05 remains the consumption / charging contour; it must reference budget availability and the centre, not remaster funding.



The enterprise profile must add what the world model leaves open: every budget line, allocation, allotment and forecast line carries a version-pinned Responsibility Centre reference; period and currency are mandatory; monetary amounts use the WM-XCT-032 mixin with a pinned code-list edition and an explicit measurement basis; a plan revision must not mutate actuals or commitments; original, revised, forecast, commitment and actual remain separately based states.



## RESPONSIBILITY CENTRE BOUNDARY



Create one new entity. Cost, revenue, profit, investment and funds centres are kinds of that entity, not sibling masters. An ERP cost-centre code is a versioned alias, never the identity.



The centre has identity and lifecycle independent of:



- Organizational unit. WM-ORG-002 models internal structure. It may list “cost centre” as a unit kind and a concurrent roll-up, but finance hierarchies remain referenced masters, not owned there. Folding the centre into the unit tree forces org tree = finance tree and fails the assignment’s negative case.

- Position. WM-ORG-004 asks whether the cost centre that bears a seat differs from the holding unit, and treats budget and funding as bindings onto the seat.

- Legal entity, ledger and journal. WM-ECO-016 treats cost centre as an analytical dimension with an external dimension owner. Posted entries are immutable; correction is reversal, not rewrite.

- Budget line. Classification of an amount is not mastership of the centre.



Consumers already point at codes they do not own: budget classification, journal dimensions, position placement, work-assignment scope. EM-LND-10 names responsibility centres as a landscape object alongside plans, actuals and consolidation perimeters.



Required shape: stable family identity; immutable, effective-dated versions (world time and record time); predecessor / successor edges for merge, split, reparent and code change; version-scoped bindings to manager or accountability seat, organizational unit, legal entity, ledger and chart segment, currency, measurement basis, and hierarchy parent. Historical journals and budget lines store the centre version effective when recorded. Reorganization may apportion current-period authority only. It must not cascade-rewrite past attribution.



## FUNDING CONSERVATION



WM-ECO-012 names sources, earmarks, release gates, envelopes and allocations. It does not yet state the assignment invariant that an allocation has a base and a remainder rule. The profile must.



Every allocation cites a source base on a named funding source in a named budget version, and a named remainder rule (lapse, carryover, return-to-source, residual-to-unallocated, or prohibited reallocation). In one revision, the sum of allocations from one source cannot exceed that source’s authorized amount in the same currency, pinned code-list edition and measurement basis. Residual is computed: authorized − allocated − reserved − lapsed + carry-in. Unknown is not zero.



A successor budget version does not increase source availability unless the source authorization itself is amended. Cross-budget use of one source is allowed only if the source register records the drawn amount once; receiving budgets reference that draw. Commitments and actuals consume availability; they do not create it. Quantization residuals follow WM-XCT-032 allocation-and-residual rules rather than silent absorption.



## ACCEPTANCE SCENARIO



T0. Project P is financed by grant Source A (earmarked) and own-funds Source B. Budget version V1 allocates 60 from A and 40 from B to Responsibility Centre X version 1 (manager M1, ledger L1, segment S1). Remainder: A lapses unused; B returns to the unallocated pool. Commitments and actuals reference centre X v1 and budget V1. Plan, forecast, commitment and actual are stored as distinct states.



T1. Reorganization moves the department. Centre X v1 remains frozen. Centre X v2 binds the new unit and manager M2 under the same family identity. Historical journal lines keep X v1. The negative case — moving a department rewrites past expenses onto the successor centre — is a failed implementation.



T2. Budget revision V2 supersedes V1. V2 may re-split 50 A + 50 B. Source A’s authorized amount is unchanged unless the grant is amended, so V2 cannot make the original 60 available again beside the new 50. Forecasts attach to V2 without mutating V1 or actuals. Variance compares V1, V2, forecast, commitment and actual on the centre versions pinned at record time. Two sources never become available twice; history reconciles.



## HOLDS AND PUBLICATION RECOMMENDATION



Do not treat this card as publication-ready. WM-ECO-012 is a reviewable draft with independent review waived and an empty approved relationship ledger. Conservation fixtures, jurisdiction recipes and chart-of-accounts crosswalks remain deferred. Neighbouring models used here are likewise reviewable drafts.



Before publication: specify the Responsibility Centre entity with fixtures for reorg, merge, split and code change; add conservation fixtures for multi-source and cross-budget draws; approve relation-ledger rows from the budget profile and the centre to WM-ORG-002, WM-ORG-004, WM-ECO-016 and WM-XCT-032; declare seams so EM-FIN-05, EM-ORG-04 / WM-ORG-002 and EM-FIN-02 do not remaster the centre or funding availability; keep period, currency and measurement-basis pins mandatory. Until the centre is registered, consumers should continue to carry an explicit external dimension-owner reference rather than treat a live ERP code as identity.



Research-protocol form of result: reuse plus profile plus new subject, not a mechanical majority vote. One broken scenario — rewrite of historical centre attribution — is enough to require the split.
