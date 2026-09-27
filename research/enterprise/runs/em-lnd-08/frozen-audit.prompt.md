# Frozen no-tools semantic audit — EM-LND-08

You are the final static semantic auditor. Use only this frozen packet. Do not browse, call tools, invent identifiers or grant publication authority.

The proposed result is a PROFILE over Party, WM-ORG-014 Customer Account Relationship, WM-ECO-020 Sales Order and adjacent commercial masters. No new runtime/model identifier is proposed.

Reconciled boundary:
1. Commercial Landscape is a governed read-only profile. Market Scope is a versioned parameter edition. Served output is an immutable digest-identified projection. None has independent business identity, mastership or lifecycle.
2. Party identity remains external and is reused across customer, supplier and partner roles. Role facts and monetary amounts remain separate and are never netted merely because they share a Party.
3. Market Scope declares seller/channel perimeters, one grouping-boundary revision, one fact key, intercompany rule, segmentation, time window, scenario, coverage policy, access grants and disclosure shape. It stores no party, role, account, order, revenue or measurement facts.
4. Each concentration run uses exactly one grouping-boundary revision and one fact key. Rollup is set union of source facts and never sums pre-aggregated subtotals.
5. Intercompany elimination applies only inside an explicitly declared accounting-consolidation boundary containing both parties. Ownership or control alone never authorizes elimination.
6. Unknown parents remain reason-coded singletons. Disputed group links retain claimant attribution and produce ranges, never invented parents or unqualified points.
7. Forecast, pipeline, quote, order, subscription and observed revenue/delivery are non-substitutable series. Coverage is backed, partial, unbacked-open, unbacked-lapsed or unevaluable; unsupported is not false and unevaluable is not zero.
8. The projection digest binds Market Scope edition, source revisions, fact key, grouping boundary, elimination rule, world/knowledge time, scenario, access-grant revisions, disclosure shape and calculation-engine revision. Any change creates a new immutable edition/projection.
9. Cross-controller facts are excluded by default. Missing authorization yields omission or typed unevaluable state without revealing presence or absence. Membership never grants access.
10. Cross-period comparison requires matching fact key, grouping boundary and elimination rule or a pinned governed remapping. Two perimeters produce two projections; a group view set-unions facts without merging perimeter artifacts.

Scenario: P1={S1}; P2 consolidates {S1,S2}. Party X buys from both and supplies S2. S1→S2 is external in P1 but eliminated in P2 only under its consolidation rule. Y has an unknown parent and remains a reason-coded singleton; Z has disputed G1/G2 links and yields an attributed range. Customer concentration uses customer-role facts only, never X supplier amounts.

Audit questions:
- Is there a hidden aggregate or identifier despite `newRuntimeId=false`?
- Are profile, parameter edition, projection, Party, commercial fact, boundary, grant and shape mastership unambiguous?
- Is digest/run identity deterministic and does elimination avoid false inference?
- Does the scenario preserve dual roles, two perimeters, uncertainty and access?
- Identify any critical contradiction that makes even a held profile unsafe.

Return at most 500 words with exactly: Verdict (`ACCEPT WITH LIMITS`, `REVISE`, or `REJECT`); Critical findings; Required holds; Scenario result; Identifier decision. Treat base-model publication blockers as holds unless they contradict the profile.
