# EM-LND-08 local synthesis

## Disposition

- Define Commercial Landscape as a governed read-only profile over customer relationships, orders and adjacent commercial masters.
- Define Market Scope as its versioned parameter set for seller perimeter, channels, intercompany rule, segmentation, period, as-of, scenario and disclosure.
- Served output is an immutable digest-identified projection. Neither candidate has independent business identity; allocate no runtime/model identifier.

## Identity and mastership

Party identity remains with the party authority and is reused across customer, supplier and partner roles. WM-ORG-014 masters seller-scoped customer relationships; WM-ECO-026 opportunity/forecast; WM-ECO-021 quote; WM-ECO-020 order/fulfilment; WM-ECO-022 subscription; WM-ECO-027 campaign; WM-ORG-012 group relationships. The landscape reads pinned revisions and sends corrections to each master.

One party can hold customer and supplier roles simultaneously. Roles remain separate and their monetary facts are never netted merely because they share a party anchor.

## Market scope and grouping

Market Scope declares seller legal entities, channels, intercompany elimination, segmentation scheme/version and mapping, measurement period, world/knowledge as-of, group-boundary kind/version, restatement mode, scenario and disclosure grain.

Grouping uses a governed ownership/control or accounting-consolidation boundary, never CRM hierarchy. Unknown-parent relationships remain reason-coded singleton buckets. Disputed group links preserve competing claims, claimant capacities and result ranges; recency never resolves them.

## Concentration

Each order line, subscription charge or observed delivery has one fact key and one attribution path. Rollups use set union of facts rather than sums of pre-aggregated subtotals. Every concentration figure reports attributed, unknown-parent and disputed shares separately.

Customer concentration and supplier dependency are different observations over the same party and are not added or netted. Intercompany facts are retained or eliminated according to the declared perimeter rule.

## Forecast versus fact

Forecast, pipeline, quote, order, subscription and observed delivery/revenue remain parallel measures. Each names method/model version, source, period, grain and uncertainty. Recognized revenue and delivered quantity come only from their respective authoritative masters.

Forecast coverage is a later assertion for a forecast unit and reconciliation window: order-backed, partially backed, unbacked-open, unbacked-lapsed or unevaluable. Unsupported does not mean false, and unevaluable does not mean unbacked. Forecast history remains immutable.

## Time, access and scenario

World time, knowledge time and measurement phenomenon/result/ingestion times remain distinct. Segmentation as-of differs from measurement period; restatement requires an explicit scope mode. Hypothetical scenarios never mix with authoritative facts.

Group membership grants no access. Cross-controller data requires WM-XCT-002 authorization and WM-XCT-003 least-disclosure shape. External views default to aggregate-only where named concentration reveals counterparty behavior.

## Acceptance scenario

Perimeter A contains seller S1; perimeter B consolidates S1 and S2. Intercompany order S1→S2 counts externally in A and is eliminated in B. Party P buys from both sellers and supplies S2; purchase and supplier facts remain separate. One customer's ultimate parent is disputed between two groups and produces a range; another is unknown and remains a reason-coded singleton. Concentration differs legitimately across the two declared perimeters.

## Invariants

1. Party identity is reused and never re-mastered by role.
2. Customer, supplier and partner roles remain separate.
3. One fact key is counted once at one grain.
4. Rollup is union of facts, not sum of subtotals.
5. Grouping cites boundary kind and version.
6. CRM hierarchy never proves control.
7. Unknown and disputed links remain typed facts.
8. Forecast, pipeline, quote, order, subscription and observed facts never merge.
9. Unsupported forecast is not automatically false.
10. Every view declares perimeter, segmentation, period and time horizons.
11. Membership never grants access.
12. Views are immutable, digest-identified and non-reimportable.

## Minimal profile shape

The profile records scope/version, seller/channel perimeter, intercompany rule, group boundary, segmentation scheme/as-of, restatement mode, period, world/knowledge times, scenario, measures and authorities, counting grain/fact-key rule, attribution buckets, coverage window/outcomes, disclosure/cohort controls, input pins, output digest and gap/conflict register.

## Holds

WM-ORG-014 and WM-ECO-020 remain non-canonical drafts with provider, relationship and entry-kind gaps. Adjacent commercial models have single-provider holds; WM-ORG-012 retains its parent/reference conflict; WM-MAT-008 has an open cardinality hold. Supplier-role master WM-ORG-015 was not frozen here. Crosswalks, segmentation methods and concentration fixtures remain unverified. This checkpoint makes no canonical completeness, installability or publication claim.

## Grok reconciliation

The accepted review confirms `newRuntimeId=false` and adds strict run identity: one grouping-boundary revision and one fact key per concentration projection. Intercompany elimination requires an accounting-consolidation boundary containing both parties; ownership/control alone is insufficient. Market Scope stores parameters only, and any parameter, access, disclosure or engine change creates a new immutable edition and projection digest.

Cross-controller facts are excluded by default. Missing authorization produces omission or typed unevaluable state without revealing existence. Cross-period comparisons require matching fact key, grouping boundary and elimination rule or an explicit pinned remapping. Two perimeters remain two projections and are only combined through set union of their facts.

## Frozen-audit reconciliation

The single frozen audit accepted the profile with five limits. The final candidate keeps disputed hypotheses inside one boundary revision, separates evidentiary `unevaluable` from hidden authorization denial, makes Market Scope authoritative over digest pins, requires external revisioned segmentation and coverage policies, and forbids cross-perimeter union across incompatible elimination semantics. No second audit was run and no identifier was added.
