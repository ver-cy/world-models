# Verdict

**FinanceLandscape — profile, not a new root.** It is a governed declaration plus a reproducible, exception-aware projection over existing masters (WM-ECO-012 plans, WM-ECO-016 postings, WM-ECO-017 balances, WM-ECO-018 statements). It has no identity or lifecycle independent of the masters it reads and the scope revision it pins; served output has artifact identity only (digest, inputs, knowledge cut). Allocate no identifier.

**FinanceViewPolicy — pinned policy/rule set, not an aggregate.** It is the versioned, immutable parameter revision the landscape cites: perimeter, books, framework, mapping, rates, transformation, elimination and allocation licences. Same pattern as Market Scope (EM-LND-08) and the run-pinned configuration of EM-FIN-04. Host it as a policy revision under the adopting Dimension's policy authority (prior work cites WM-KNW-012 for pinned policy revisions); do not mint a second aggregate root. Allocate no identifier.

# Evidence

All three target specs are `publishableCanonical: false`, `adjudicationStatus: reviewable-draft`. WM-ECO-012 is Codex-only under a dual waiver with **no approved outgoing relation rows at all**. WM-ECO-018 and WM-ECO-017 are Codex-only with explicit relation holds: WM-ECO-015 is "only a parent signal", WM-ECO-004 and WM-ECO-018 COMPOSE remain candidates. Mapping status in the contour is `conceptual-candidate` at `index-and-publication-metadata` depth. Nothing here supports a crosswalk claim, and the landscape must be built on referenced, version-pinned masters rather than absorbed semantics.

# Identity/mastership

Plan revisions are mastered by WM-ECO-012; postings by WM-ECO-016; balances and positions by WM-ECO-017; issued statements by WM-ECO-018; account identity by WM-ECO-015; group links by WM-ORG-012; holdings by WM-ECO-038; measurement records by WM-MAT-008. The landscape masters nothing: it stores scope revisions, input pins, derived view rows and a gap/conflict register. Corrections route to the owning master. Registry `entry_kind: standalone-mm` classifies the record plane only and must not be read as a subject kind.

# Landscape/view policy

FinanceViewPolicy revisions must declare, as required fields: book set; ledger revision per book; measurement period and cutoff; scenario; policy version; organization and responsibility-centre scope with version; accounting framework and taxonomy; chart of accounts and mapping version; consolidation scope version and run reference; presentation currency, rate set and rate-type policy; permitted transformations; elimination rule; allocation rule and run; world/knowledge cut; comparability classification; residual disclosure grain. A missing field blocks the view rather than defaulting.

# Plans/actuals

Plan, ceiling, allocation, availability, commitment, actual posting, cash and forecast remain parallel states with separate authority — WM-ECO-012 already forbids treating them as interchangeable. A plan/actual pair is comparable only when book, framework, chart mapping, responsibility scope, period, currency and recognition basis agree or an authorized transformation bridges them. Otherwise the row is emitted as **not comparable** with the divergent axis named. Forecast never overwrites authorized plan; actuals are read, never re-derived.

# Books/accounts/responsibility

Books never mix. Each row names one book and its pinned ledger revision; debits and credits from different books never offset. Ledger-account identity is ledger-plus-code-plus-effective-version (EM-FIN-02); bank-account identifiers are not ledger codes. Responsibility ownership is a reference to a Responsibility Centre version effective at accounting time (EM-FIN-01), not an organizational-unit id. Reorganization creates a successor centre version; historical rows stay pinned to the prior one.

# Consolidation/elimination

Perimeter is purpose-qualified (statutory, management, ownership, statistical) and never silently shared. Inclusion requires control basis, authority, evidence and interval; common ownership alone proves nothing. Eliminations post only to consolidation books, cite both counterparty legs and a matching key, and disclose matched, unmatched and residual amounts with reason. An unmatched leg is a visible break, never a one-sided posting. Every consolidated figure cites Consolidation Scope version and an immutable Consolidation Run.

# Currency/period/comparability

Transaction, functional and presentation currency roles stay explicit with rate, rate type, rate date, source and rate-set version. Translation happens after allocation and elimination within one book, and is recorded per row. Amounts in different currencies, periods, books, bases or scenarios are never added; the arithmetic is admitted only through a named transformation in the pinned policy, with its own provenance. Each row carries a comparability classification: comparable, bridged, or not comparable with the blocking axis.

# Allocation/residuals

Allocation is analytical attribution, not a posting (EM-FIN-05). One run, one axis, one currency: allocated results plus materialized residual equal the source amount within tolerance; weights never exceed one. Parallel axes over the same source are non-additive. Unallocated, untagged or unmatched cost is a first-class row with reason code and share, disclosed in every total that excludes it. Residual suppression is a failure, not a rounding convenience.

# Projection/time/provenance

Event, posting, cutoff, run, issue, observation, ingestion and knowledge times stay distinct. A view answers as-of a stated world time at a stated knowledge cut and resolves the scope, mappings, rates and ledger revisions valid at that cut, not current configuration. Output is immutable, digest-identified, non-reimportable, and carries input pins, policy revision, rule versions, completeness declaration and the gap/conflict register. Timestamps use RFC 3339 with explicit offset.

# Governance

Owner: Vercy meta-model curator for the profile; finance authority for framework, chart mapping, rate policy and elimination rules; responsibility-centre steward for scope; consolidation steward for perimeter and runs; access authority for disclosure grain. Scope changes, transformation licences, post-cutoff adjustments and published projections require recorded authority with initiator/authorizer separation or a compensating control. The landscape may not approve, post, value, eliminate, allocate, file or publish autonomously.

# Acceptance scenario

Books L-STAT (functional EUR) and L-MGMT (functional USD); presentation GBP. Plan from an authorized WM-ECO-012 revision; actuals from WM-ECO-016 postings summarized through WM-ECO-017. An intercompany sale between two in-perimeter entities is eliminated in the consolidation book, citing both legs, matching key and an FX residual. One cost pool is untagged and remains unallocated with a reason code. A request for "total spend across both books in GBP" with no declared rate set and no cross-book transformation is **blocked**: the view returns per-book subtotals, the elimination and its residual, the unallocated share, the named missing policy fields, and the transformation rules that would be required to authorize the total.

# Invariants

1. Plan, actual, balance, statement and derived row identities stay distinct. 2. Every row names book and ledger revision. 3. No arithmetic across currencies, periods, books, bases or scenarios without an authorized transformation. 4. Every figure cites period, currency, basis, framework, mapping and knowledge cut. 5. Eliminations post only to consolidation books and disclose residuals. 6. Allocated plus residual equals source within one run/axis/currency. 7. Parallel axes are non-additive. 8. Residual and unallocated shares are never hidden. 9. Source facts are read-only; corrections go to the master. 10. Views are immutable and carry completeness. 11. Comparability is classified, never assumed. 12. Perimeter membership grants no access.

# Minimal model set

Reuse: WM-ECO-012, WM-ECO-015, WM-ECO-016, WM-ECO-017, WM-ECO-018, WM-ORG-012, WM-ECO-038, WM-MAT-008. Required but unallocated roots from prior work: Responsibility Centre (EM-FIN-01), Consolidation Scope and Consolidation Run (EM-FIN-04), Chart of Accounts / Accounting Policy and Mapping (EM-FIN-02), Cost Allocation rule/run/result (EM-FIN-05), Metric Definition (EM-DAT-05), plus an FX Rate Set and Intercompany Match master (EM-FIN-04). Add only the FinanceLandscape profile and FinanceViewPolicy revisions.

# Holds

Dependency gaps: all five named roots plus rate set and match remain unallocated, so chart/mapping, perimeter, run, allocation and rate pins are currently prose. Contradictions: WM-ECO-018's "Consolidation and data steward" role claims perimeter, eliminations, transformations and lineage against its own out-of-scope list; WM-ECO-018 COMPOSE WM-ECO-017 conflicts with WM-ECO-017's referenced-master boundary; WM-ECO-015 declares a CHILD relation to WM-ECO-016 while the registry asserts CONTAINS; WM-ECO-012 has no approved relation rows; WM-ORG-012 parentage remains unsettled; WM-ECO-038 extends a category marked for split; WM-MAT-008 carries an open cardinality hold. Crosswalks, immutable pins, fixtures and independent review are absent. No canonical completeness, installability or publication readiness is claimed.
