# Verdict

Reuse both target models unchanged; add no new business object. **CommercialLandscape** is a **governed profile** over WM-ORG-014 and WM-ECO-020 with profile-version identity only — no independent business identity, no write path to any master. **MarketScope** is a **versioned scope declaration owned by that profile** (seller/business perimeter, intercompany rule, segmentation scheme and version, measurement period, access scope), also without independent identity: it is the reusable, citable parameter set the v1 fields `commercial_scope`, `period`, `segmentation_rule`, `access_scope` were groping toward. Served output is an **immutable, digest-identified projection** generated from a MarketScope plus pinned master revisions, non-reimportable as source truth. This mirrors the EM-LND-02 disposition (profile + generated view) and allocates no runtime or model identifier. Neither candidate earns independent identity because neither bears standing, obligations, succession or a lifecycle of its own.

# Evidence

WM-ORG-014 is explicitly a seller-scoped CRM relationship, not party identity: one party may hold several customer relationships across seller/service scopes, and its own adversarial checks reject email-based merging, treat CRM grouping as no proof of legal control, and treat payment status as an attributed snapshot. WM-ECO-020 scopes order identifier uniqueness to the issuing seller legal entity, requires seller entities and channels to be declared, separates acceptance (commitment) from allocation and despatch, holds delivered/outstanding accounting per line, and disclaims tax determination, revenue recognition and subscription specialisation. Both are `published` but `publishableCanonical: false`, `adjudicationStatus: reviewable-draft`, with `mapping_status: conceptual-candidate` at `index-and-publication-metadata` depth — so no semantic crosswalk is established here.

# Identity/mastership

Party identity stays with WM-ORG-001 and the adopting Dimension's party authority; cross-role reuse is coordinated by EM-COM-01. Customer-relationship truth stays in WM-ORG-014; order and fulfilment truth in WM-ECO-020; opportunity/forecast in WM-ECO-026; proposal in WM-ECO-021; recurring entitlement and billing in WM-ECO-022; campaign and attribution design in WM-ECO-027; group edges in WM-ORG-012 over WM-ORG-001. The profile reads; corrections return to the owning master. Every profile record is append-only and pins an upstream revision or `asOf`.

# Market scope

A MarketScope version fixes: seller legal entities and channels in the perimeter; the intercompany rule (eliminate when both counterparties are inside the perimeter, or retain); segmentation scheme, version and correspondence-table reference; measurement period; world-time and knowledge-time as-of, pinned separately; group boundary kind and version; restatement mode; disclosure class and grain. A view is refused, not defaulted, when a pinned horizon cannot be reconstructed from sources.

# Party roles and grouping

One party, several role bindings: customer → WM-ORG-014; supplier and partner → WM-ORG-015 (referenced in WM-ORG-012's boundary notes but not frozen in this dossier). Roles never merge and never net. Grouping uses a declared WM-ORG-012 boundary kind — ownership/control or accounting consolidation — never the CRM account hierarchy, which WM-ORG-014 itself says implies neither control nor data-sharing rights. Boundary kinds do not imply one another.

# Concentration

Counting rule: each measured fact (order line, subscription charge, observed delivery) carries a unique fact key and exactly one attribution path; a rollup is a set union over facts, never a sum of pre-aggregated subtotals, so it is idempotent and safe across multi-account and multi-seller-entity cases. Group attribution produces three disjoint buckets: **attributed**, **unknown-parent** (exception-coded, retained as its own singleton node — never folded into a parent or into "other"), **disputed** (shown under each competing claim with claimant attribution and capacity, reported as a range, never averaged or resolved by recency). Every concentration figure publishes the unknown-attribution and disputed-attribution shares as first-class measures. Customer concentration and supplier dependency are separate observations over the same party.

# Forecast versus fact

Six parallel measures, never summed: forecast (method, model version, calibration, as-of), pipeline (stage plus weighted projection), quote (proposal version and validity; indicative), order (accepted disposition; commitment), subscription (schedule; not invoice, not payment), and observed revenue/delivery — delivered quantity only from line-bound despatch evidence, recognised amounts only from the external invoice/revenue masters. Movement between measures is an outcome binding, not arithmetic.

Unsupported forecasts are found by a **coverage assertion** per forecast unit (pursuit × expected-close period × scope key), evaluated at a later knowledge time inside a declared reconciliation window: order-backed, partially backed, unbacked-open (still within validity — legitimate), unbacked-lapsed, or unbacked-unevaluable (identity link missing, scope key unmatchable, master unreachable). Unevaluable is not unbacked; unbacked is not false. The forecast is never rewritten or deleted — coverage is appended alongside it.

# Time/scenario

Phenomenon, result and ingestion times are distinct, per WM-MAT-008; RFC 3339 with explicit offset. Views pin world time and knowledge time separately. Segmentation-as-of is separate from the measurement period, and reclassification does not retroactively restate prior periods unless the MarketScope declares restated mode. Scenario defaults to authoritative; hypothetical facts never mix with authoritative facts, because the base models support no branching.

# Access and disclosure

Group membership grants nothing. Cross-controller reads require a WM-XCT-002 grant with purpose, duties and revocation, shaped by WM-XCT-003; aggregate-only views carry a WM-XCT-005 cohort-floor reference; field sensitivity comes from WM-XCT-020; the provenance tuple goes to WM-XCT-004; enforcement is WM-XCT-038. Named top-customer disclosure reveals a counterparty's purchasing volume, which is also their data — external publication defaults to aggregate-only. Where two perimeters or audiences meet, the least-disclosure shape governs.

# Scenario

Perimeter A = {S1}. Perimeter B = consolidated {S1, S2}. P1 buys from S1 (O1) and S2 (O2) and supplies S2; O3 is S1→S2. In A, O3 is external revenue; in B it is eliminated. P1's group counts O1 once in A, O1+O2 once each in B; its supplier spend is never netted against either. P3's ultimate parent is disputed between G1 and G2: reported as a share range under both claims. P4's parent is unknown: a reason-coded singleton in the denominator and in the concentration list. Top-3 concentration differs between A and B; both are correct under their declared scope, and neither is "the" number.

# Invariants

1. Party reused, never re-mastered; roles resolve to their owning authority. 2. One fact counted once, at one grain; rollup is union, not sum of subtotals. 3. Customer and supplier roles never summed or netted. 4. Grouping cites a boundary kind and version; CRM hierarchy is not a group boundary. 5. Unknown and disputed links are typed facts, never null, zero or "other". 6. Every view declares perimeter, intercompany rule, segmentation scheme/version, period and as-of times. 7. Forecast, pipeline, quote, order, subscription and observed facts never merge. 8. Coverage is a separate assertion; unbacked ≠ false, unevaluable ≠ unbacked. 9. Recognised revenue and delivered quantity only from their masters. 10. Measures carry unit, procedure version, grain and uncertainty. 11. Membership grants no access. 12. Multi-audience output takes the least-disclosure shape. 13. Views immutable, digest-identified, non-reimportable; no write path to masters.

# Minimal profile shape

Profile id/version; MarketScope ref/version; perimeter (seller entities, channels, intercompany rule); group boundary kind/version; segmentation scheme/version/as-of; restatement mode; measurement period; world/knowledge as-of; scenario; measure set with per-measure authority and clock; counting-unit and fact-key rules; attribution buckets with reason and claimant codes; coverage window and outcome vocabulary; disclosure class, grain and cohort-floor ref; pinned input revisions; output digest; gap and conflict register.

# Holds

Both targets are non-canonical reviewable drafts. WM-ORG-014 is Codex-only with Claude and Grok waived, an open validation gap, and an empty relationship contract. WM-ECO-020 carries an unreconciled `standalone-mm`/`aggregate` entry-kind conflict, prose-only boundary notes, a coverage-checklist restatement hold, source re-tiering, a consumer-protection evidence gap and acknowledged thin subscription coverage. WM-ORG-012's registry parent conflicts with its reference boundary. WM-ECO-021/022/026/027 are Codex-only with absence-of-external-review holds; WM-MAT-008 is single-provider with an open cardinality hold. WM-ORG-015 is not frozen here. Crosswalks are unverified at index-and-metadata depth; segmentation, attribution and probability methods need calibration and fixtures. No canonical completeness, installability or publication readiness is claimed.
