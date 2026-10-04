# Frozen no-tools semantic audit — EM-LND-03

You are the final static semantic auditor. Use only this frozen packet. Do not browse, call tools, infer missing catalogue text, invent identifiers or grant publication authority.

The proposed result is a PROFILE over WM-PER-001 Person, WM-ORG-005 Employment, WM-ORG-016 Work Assignment, WM-ORG-004 Position and WM-ORG-002 unit snapshots, governed by WM-XCT-002 access and WM-XCT-003 disclosure shape. No new runtime/model identifier is proposed.

Reconciled boundary:

1. Workforce Scope is a versioned rule artifact containing explicit population predicates, party-role filters, measure definitions, time conventions, deduplication, consolidation, access and disclosure rules. Workforce Landscape is the immutable result projected from one Scope revision and its pinned inputs.
2. Neither construct masters persons, employment, assignments, positions, units or statuses. Scope ids and Landscape fingerprints are non-registrable artifact identifiers for citation and replay only and cannot be person, party, employment, assignment, position or organization keys.
3. Every released view pins immutable revisions of WM-PER-001, WM-ORG-005, WM-ORG-016, WM-ORG-004, WM-ORG-002, WM-XCT-002 and WM-XCT-003 that it uses, plus Scope and calculation-engine revisions. Missing required pins fail closed. Any pin, predicate, shape or engine change creates a new immutable version and fingerprint.
4. Unique persons, legal headcount, distinct employed persons, active relationships, assignments, positions, FTE and capacity are distinct named measures. Each declares grain, denominator, time convention, inclusion predicate, source object, null policy, consolidation and deduplication rules.
5. FTE uses exactly one named class and source: allocated supply FTE from WM-ORG-016, authorized demand FTE from WM-ORG-004, or explicitly defined employment FTE from WM-ORG-005. Different classes are never coalesced into an unnamed total.
6. Capacity is typed as person-available, assignment-available, position-authorized or unit-planned and never substitutes for headcount or FTE.
7. Contractors and agency workers may contribute assignments, allocated FTE or capacity without host legal headcount. Vacancies may contribute position or authorized-demand FTE without a person.
8. Consolidated employment publishes legal relationship headcount and anchor-deduplicated distinct employed persons separately. One person employed by A at 0.6 and B at 0.5 yields one unique person, two active legal relationships, employer headcount 1 for A and 1 for B, consolidated distinct employed persons 1 and allocated supply FTE 1.1. It is not clipped across employers.
9. Person anchors are resolved inside population calculation and never emitted. The pinned disclosure policy governs small counts, release deltas, cross-tabs, unusual FTE, unique affiliation patterns and release-set linkability with explicit suppression or aggregation actions.
10. Unknown, suppressed and zero remain distinct. Scenario results remain separate from authoritative results. Active status is asserted by its source master and is never inferred from badge, payroll, assignment or contract dates.

Audit questions:

- Does this reconciliation introduce a hidden aggregate or identifier despite `newRuntimeId=false`?
- Are Scope rules, Landscape results, source facts, access and disclosure mastership unambiguous?
- Are the pins and FTE/capacity source rules deterministic enough for a held reviewable profile?
- Does the dual-employment scenario preserve person identity, legal headcount, allocation and privacy semantics?
- Identify any critical contradiction that makes even a held reviewable profile unsafe.

Return at most 500 words with exactly: Verdict (`ACCEPT WITH LIMITS`, `REVISE`, or `REJECT`); Critical findings; Required holds; Scenario result; Identifier decision. Treat base-model edits and publication blockers as holds unless they contradict the profile itself.
