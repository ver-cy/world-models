# Frozen no-tools semantic audit — EM-LND-02

You are the final static semantic auditor. Use only this frozen packet. Do not browse, call tools, infer missing catalogue text, invent identifiers, or grant publication authority.

The proposed result is a PROFILE over WM-ORG-001 Organization and WM-ORG-012 purpose-qualified inter-organizational relationships, with WM-XCT-001/002/003/040 authority, grant, disclosure and composition references. No new runtime/model identifier is proposed.

Reconciled boundary:

1. Group Landscape is a governed profile revision with an operator name, purpose set, inclusion predicates and six parallel graphs: legal ownership/control, accounting consolidation, management, operational perimeter, brand affiliation and franchise/network participation. It is not a party, asset owner, contract party or authority holder.
2. Group Scope View is an immutable generated projection. Its citation identity is the digest of landscape revision, world time, knowledge time, scenario, graph rules, source revisions, grant set, disclosure shape and generated projection. Identical pins and projection yield the same digest; any change yields a new digest. It has no business-object master and is never updated in place or re-imported as source truth.
3. WM-ORG-001 masters subjects and independent standing. WM-ORG-012 masters each relationship fact, purpose, owner, claimant capacity, uncertainty, evidence and interval. A statutory or pre-incorporation body with independent standing is WM-ORG-001; naming convenience alone never promotes a landscape.
4. The six graphs remain parallel and non-substitutable. Security trust is unowned in this contour. Access is not a graph: membership never implies WM-XCT-001 authority, WM-XCT-002 grant or WM-XCT-003 shape.
5. Each cross-organization fact included in a view requires an authorized WM-XCT-002 grant and WM-XCT-003 disclosure shape. Grants and shapes remain external and are not stored on the view. Different grant sets or shapes produce different digests.
6. Typed unknown, disputed and unverified assertions, fact owner and claimant capacity survive composition. A pinned graph rule or disclosure shape may exclude them only when the exclusion is visible in the pins; source assertions are never collapsed or mutated.
7. The profile name is an operator label, not a surrogate organization, party, ledger or contract key. Federation shares WM-ORG-001 identities and WM-ORG-012 claims, not a landscape identity.

Scenario: H legally controls S1/S2/S3; accounting consolidates H/S1/S2; management includes franchisee-operated F1; operations includes S1/S2/F2; brand includes S1/F1/F2/F3; franchise includes H/F1/F2/F3. F3 is unverified in one source and disputed in another and both claims persist. A consolidation view at world T, knowledge K and scenario Base contains H/S1/S2. Cross-company figures appear only under fact-specific grant and shape. Changing graph rules, grant set, shape or excluding disputed F3 creates a new digest and leaves prior views immutable.

Audit questions:

- Does the reconciliation introduce a hidden new aggregate or identifier despite `newRuntimeId=false`?
- Are profile, subject, relationship, grant, shape and projection mastership unambiguous?
- Is digest identity deterministic and complete without storing authorization on the view?
- Does the scenario preserve parallel graphs, source claims, access controls and time/scenario pins?
- Identify any critical contradiction that makes even a held reviewable profile unsafe.

Return at most 500 words with exactly: Verdict (`ACCEPT WITH LIMITS`, `REVISE`, or `REJECT`); Critical findings; Required holds; Scenario result; Identifier decision. Treat base-model edits and publication blockers as holds unless they contradict the profile itself.
