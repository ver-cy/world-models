# Frozen no-tools semantic audit — EM-WRK-02

You are the final static semantic auditor. Use only this frozen packet. Do not browse, call tools, infer missing catalogue text, invent identifiers, or grant publication authority.

The proposed result is a PROFILE over WM-ACT-005, WM-ACT-008, WM-ACT-031 and WM-ACT-032 with no new runtime/model identifier.

Reconciled boundary:

1. WM-ACT-005 masters Project identity, serial ProjectCharter revisions, immutable approved baseline packages, predecessor transitions and the current-package pointer.
2. WM-ACT-008 masters working plan/schedule content, forecasts, actuals and computation provenance. A baseline package pins immutable WM-ACT-008 revisions or embeds an immutable snapshot; it never resolves live heads. Variance names the baseline-package identifier and reads its pins.
3. Charter, baseline-package and working-plan revision series are independent. A baseline transition is governed from frozen selection through package creation to pointer switch; predecessor packages remain immutable. Package grain must declare whether scope, schedule and cost move atomically or independently.
4. WM-ACT-031 remains the shared aggregate for discriminated Milestone, Deliverable and Acceptance records. Their identities, relations and lifecycles are distinct. Acceptance is a separate immutable record, not the milestone/deliverable row, and pins object revision, criteria revision, baseline package, verification method, authority, decision time, conditions and evidence.
5. WM-ACT-032 masters ProjectChangeRequest. WM-ACT-005 exposes only a projection and optional baseline-transition link. Approval authorizes but never itself performs a transition; after initial BL-1 only an approved rebaseline-class request may add a package.
6. Project-product and project-tracker-container relations are many-to-many. Sharing either subject cannot share project charter, package, register or acceptance identity. Tracker items remain project-attributable.
7. Project closure does not close a product, erase open changes or remove residual obligations.

Acceptance scenario: projects P1 and P2 share tracker T and product X. P1 BL-1 pins plan revision PR-7. Its working plan advances to PR-8. An approved P1 request creates BL-2. BL-1 and historical variance still resolve PR-7; P1 acceptances remain pinned to their original object/criteria/package basis; P2 is unchanged; T and X retain one external identity each.

Negative cases reject mutable-head baselines, in-place baseline overwrite, a deliverable row overwritten by its acceptance, tracker identity treated as project identity, task completion inferred as milestone achievement, and project closure propagated to product closure.

Provider comparison: Claude supported the shared WM-ACT-031 union. Grok supported the reuse map but required immutable 008 pins and challenged the union. The reconciliation keeps one aggregate while separating the three record identities and lifecycles, especially immutable Acceptance. Both providers state that the bases remain reviewable drafts and that relation/source/base corrections are still holds.

Audit questions:

- Does the reconciled profile introduce a new independent aggregate identity despite `newRuntimeId=false`?
- Are baseline authority, plan content, change request and acceptance mastership unambiguous?
- Does the P1/P2 scenario preserve BL-1, acceptance bases and project isolation?
- Does the WM-ACT-031 reconciliation actually preserve the provider disagreement without silently collapsing identities?
- Identify any critical contradiction that makes even a held reviewable profile unsafe.

Return at most 500 words with exactly: Verdict (`ACCEPT WITH LIMITS`, `REVISE`, or `REJECT`); Critical findings; Required holds; Scenario result; Identifier decision. Treat unresolved base-model edits and publication blockers as holds unless they contradict the profile itself.
