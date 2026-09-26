# EM-WRK-02 — independent review

## Verdict

Reuse and profile; create no new model identifier. Allocate the seven candidate types across the four bases as follows: **Project** → WM-ACT-005 (aggregate root). **ProjectCharter** → WM-ACT-005 artifact `a-project-charter` (serial, revisioned) — an instrument, not an entity. **Baseline** → identity and approval authority in WM-ACT-005 `a-baseline-package`; schedule-component content and the forecast/actual layer in WM-ACT-008 `art-baseline-snapshot`. **Milestone**, **Deliverable**, **Acceptance** → WM-ACT-031, keeping the discriminated union rather than splitting. **ProjectChangeRequest** → a WM-ACT-032 profile, with WM-ACT-005 `f-change-control` demoted to a register projection plus baseline-transition linkage. Boundary decision: **pending → conditionally resolved**, subject to Holds.

## Evidence

All four bases carry `publishableCanonical: false` and `adjudicationStatus: reviewable-draft`. WM-ACT-005 and WM-ACT-008 are dual-provider; WM-ACT-031 and WM-ACT-032 are single-provider under an explicit owner waiver of Grok recorded 2026-08-29T09:06:27Z. Queue `boundary_decision` is `pending`; `remaining_scope` is the entire brief. Every registry `review_state` is `migration-boundary-review` or `boundary-review-required`; all six relation rows are `review_state: candidate`. Mapping status for all four targets is `conceptual-candidate`. Evidence depth is `boundary-reviewed` only for WM-ACT-005; the other three are index-and-publication-metadata. Nothing here supports a canonical or installable claim.

## Identity/mastership

Four distinct masters, one identity each. The sponsoring organisation's authoritative system masters project identity (`de-project-identifier` + `de-identifier-scheme`, issuing system recorded). WM-ACT-008 masters plan identity, versioning and derived dates. WM-ACT-031 masters the milestone/deliverable record and its acceptance criteria. WM-ACT-032 masters the change-request record; WM-KNW-010 masters the resolving decision.

Three collapse risks must be blocked. First, WM-ACT-005 `f-change-control` (`de-change-request`, `a-change-request-register`) duplicates WM-ACT-032; it must hold only the request reference, the prior/resulting baseline versions and the affected breakdown elements. Second, both WM-ACT-005 and WM-ACT-008 declare owned baseline artifacts; reconcile as one approved set (WM-ACT-005, authority-bearing, digested) containing a referenced schedule component (WM-ACT-008). Third, WM-ACT-031 `de-baseline-history` ("retained baseline series") must be a local projection of the pinned baseline version, never a second baseline master.

## Project/charter

A business project is bounded by three declared facts, none methodological: a resolvable authorization instrument (`de-authorization-instrument-ref`, `de-authorizing-body`, `de-authorization-effective-time`), a declared scope boundary with exclusions and assumptions, and a declared temporal frame with type-coded planned/actual dates. `de-delivery-approach-code` (predictive, incremental, iterative, adaptive, hybrid) and `f-tailoring-and-compliance` (`adopted_method_profile`, `conformance_claim`) are orthogonal attributes, so phases, gate sets and WBS presence are never boundary tests — ISO 21511 is guidance, not mandate, and earned value cannot be required of every project. The charter is a serial artifact keyed by project identifier + kind + monotonic revision, superseded not overwritten; re-charter that changes identity uses `de-superseded-by-project`. Continuing-operations projects with unspecified end remain a recorded variant.

## Plan/forecast/baseline/actual

Three layers, never merged. **Approved baseline**: immutable, digested, versioned, approval-time-stamped, with `de-superseded-baseline-ref`; edited in place it is invalid. **Forecast**: WM-ACT-008 `de-forecast-date` and `de-forecast-value` with derivation method, confidence and as-of date, plus `de-computed-early-start`/`de-computed-late-finish` flagged derived and bound to a `computationRunRef`. **Actual**: `de-actual-start`/`de-actual-finish`/`de-actual-cost-to-date` at a stated `statusDate`, never later than the recording time. Variance is invalid without a named baseline version. WM-ACT-031's baseline/forecast/actual triad is a per-record projection of the same pins. Event time, effective time and ingestion time stay separate; RFC 3339 with seconds and explicit offset throughout.

## Milestone/deliverable/acceptance

Keep the WM-ACT-031 union: `de-record-kind` discriminates milestone, deliverable and deliverable-linked milestone, with `de-zero-duration-flag` and `de-submission-required` handling both tested counterexamples. A milestone is not a completed task; achievement status (`scheduled`, `met`, `notMet`, `partiallyMet`) is separate from schedule status and submission status, so a deliverable submitted on time but rejected reports all three truthfully. Acceptance lives here as criteria, means of verification, recorded outcome, conditions and an **evidence reference**. The pack's `acceptance-certificate` artifact must be published reference-only: its own boundary note assigns production and retention to the approval and contract neighbours. Project-level scope confirmation in WM-ACT-005 aggregates those acceptances; it is not a second acceptance decision.

## Change request

One request-side record (WM-ACT-032) with: baseline reference, affected items, `instrument_kind` (change, deviation, waiver — a waiver alters no approved documentation), impact/risk assessment pinned to the assessed proposal revision, routing facts only, and disposition as an outcome value plus a version-pinned WM-KNW-010 reference. WM-ACT-032 explicitly never releases a baseline. Approval therefore triggers, but does not perform, `fn-establish-baseline` in WM-ACT-005: the new baseline cites the request identifier, the prior version and the effectivity basis (`unit`, `serial`, `lot`, `version`, `date`, `event`). Reversal is a new outcome bound to a new decision, never an edit.

## Product/tracker relations

Project↔product and project↔tracker-container are both many-to-many typed edges, keyed by source identifier, link type and target identifier, with explicit parent/child edge types rather than nesting. Neither product nor tracker container has a model identifier in this dossier; both are unregistered neighbours and no identifier may be minted here. A tracker project, board or epic tree is a tooling container only; it becomes a project reference when each work item resolves to an authoritative project identifier — binding is per item, never per container. Cost is asserted once by the project for a pinned baseline, period, currency and data date; product or team views apply declared allocation shares after deduplication and are not summed across orthogonal decompositions.

## Lifecycle

Project state comes from a declared, version-pinned vocabulary with permitted transitions, effective time separate from recorded time, and suspension/cancellation/abandonment distinct from completion. Closure classifies its outcome, hands over, assigns the post-closure benefit owner and records residual obligations (warranty, archive, liability) that outlive operational close. Product lifecycle is out of scope: closing a project closes no product, and open change requests must be dispositioned or transferred before closure, not deleted.

## Scenario

Projects P-A and P-B share tracker container T and product X. Each work item in T carries its own project resolution, so T yields no shared project identity and no merged baseline. Product X holds two `delivered-by` edges; X's lifecycle is unaffected by either closure. A change request raised against P-A cites baseline BL-1, is assessed on a pinned proposal revision, and on approval causes P-A to issue BL-2 with `supersedes → BL-1`, a content digest and an effectivity basis. BL-1 stays retrievable, so the original promise and all variance computed against it remain reproducible. A milestone already accepted keeps its acceptance basis: the criteria version pinned at BL-1, with its evidence digest and accepting-authority reference untouched. Only deliverables whose criteria the request actually changed rebind to BL-2. P-B's baseline, forecast and actuals are unchanged.

## Invariants

1. A project may hold many tracker containers; a tracker container is not a project identity.
2. A milestone is not a completed task; achievement, schedule and submission status stay separate.
3. Project closure does not close a product.
4. Approved baselines are immutable; variance without a named baseline version is invalid.
5. Forecast, approved baseline and actual are three fields, never one.
6. Derived dates carry a derivation flag and a computation-run reference.
7. An approved change request causes a new baseline; it never issues one.
8. Acceptance requires criteria version, accepting authority and an evidence reference; closure is not acceptance.
9. Earlier acceptance bases survive re-baselining unchanged.
10. Project↔product and project↔tracker-container remain many-to-many.
11. Cost is asserted once; allocation shares are view-side and deduplicated.
12. Charters, baselines, assessments and dispositions are superseded, never overwritten.
13. No date, name or period is ever an identifier.

## Minimal completion shape

Register relation rows for product, tracker container, the WM-ACT-032↔WM-ACT-021 parent edge and WM-ACT-031's seven unregistered neighbours; resolve the WM-ACT-005/WM-ACT-008 baseline-artifact ownership and the WM-ACT-005/WM-ACT-032 change-register duplication in writing; state the divergence rule for a cached disposition outcome whose WM-KNW-010 decision is later amended; declare serial-identity scope for WM-ACT-031's three artifacts and the roll-up consistency boundary; re-scope WM-ACT-032's mapping table and status extract off per-request serial keys; add the criteria-version pin that makes invariant 9 testable; run the shared-tracker, shared-product and re-baseline fixtures.

## Holds

No canonical completeness and no installability is claimed. Two of four bases lack independent corroboration under the recorded waiver. Paywalled ISO 21500-series text was read at abstract level only; GAO-16-89G, NARA GRS 5.1 and OCDS `/latest/` citations are unverified or version-drifting. Privacy and security coverage ship as declared gaps. This is a boundary recommendation on a frozen dossier, not a publication decision.
