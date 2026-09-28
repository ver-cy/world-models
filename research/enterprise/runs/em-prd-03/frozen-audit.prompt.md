# Frozen no-tools semantic audit — EM-PRD-03

You are the final static semantic auditor. Use only this frozen packet. Do not browse, call tools, invent identifiers or grant publication authority.

The result completes and reclassifies reserved WM-REC-006 as a Requirement aggregate. No new runtime/model identifier is proposed. Acceptance Criterion, Requirement Baseline, outbound Trace Link and Requirement Conflict are contained records with local scoped addresses, not catalogue models.

Reconciled boundary:
1. Requirement has stable family identity and immutable revisions. Title, ticket, filename and statement are not identity.
2. Need preserves stakeholder-authored wording; Requirement is authority-issued and verifiable; feature/design proposes realization; task records work; test/result and evidence support proof.
3. Requirement Revision contains its statement, Acceptance Criterion set, exact Rule pins and outbound Trace assertions. Change appends a revision; supersession never overwrites.
4. Acceptance Criterion is contained by one exact Requirement revision. It is distinct from reusable Rule, Test, Task and work-order-local acceptance findings.
5. WM-KNW-013 owns reusable Rule identity, operands, units, tolerance and evaluation contract. Criteria reference exact Rule revisions or hold a one-off informal condition.
6. A reusable tolerance change revises and re-pins the Rule. A local-only tolerance change revises the criterion and Requirement without mutating the Rule.
7. Requirement Baseline is a sealed population-level collection artifact of the WM-REC-006 repository/model boundary, never a child of one Requirement instance.
8. A Baseline pins exact Requirement revisions, criteria and Rule revisions with authority, purpose, effectivity and digest. Changes create a successor; predecessors remain readable.
9. Product/configuration baselines containing design, software, tests or evidence remain external.
10. Trace Link is a contained outbound association whose owned source is one Requirement revision and whose external target is revision-pinned. Inbound and endpoint-independent trace fabrics remain external.
11. Link presence never proves satisfaction. Revision of either endpoint makes the old link suspect; it is not silently retargeted.
12. Task state including Done never proves implementation correctness, criterion satisfaction or Requirement satisfaction.
13. Satisfaction requires a qualified external test result and evidence pinned to the same Requirement revision. Absence is never pass; failures remain visible after later passes.
14. Waiver, exception and external decision never rewrite Requirement, Rule, result or evidence and never become a silent pass.
15. Equal-authority conflicts preserve alternatives and cite an external resolution decision.
16. Access to contained results is the intersection of permissions across every referenced record, with non-disclosing redaction.
17. No new public model/runtime identifier is allocated. The WM-KNW-013 parent signal, external-master joins and held bases remain publication holds.

Scenario: R@rev1 has AC1, three Done tasks and failed test F. It stays unsatisfied or inconclusive. B1 freezes R@rev1, AC1, Rule pins and traces. A tolerance change yields R@rev2, AC2 and, if reusable, a new Rule revision pin. B2 freezes the new set. B1 is unchanged; diff reports revision/criterion/tolerance/Rule-pin changes; F remains visible against B1 and must be re-evaluated for B2.

Audit questions:
- Is there a hidden aggregate or identifier despite `newRuntimeId=false`?
- Can a population-level Baseline safely remain contained by this model boundary?
- Are Rule/criterion, outbound/inbound trace and Requirement/work-order acceptance boundaries unambiguous?
- Do revision, satisfaction, failure, waiver, conflict and access semantics avoid false proof or evidence loss?
- Identify any contradiction that makes even a held completion candidate unsafe.

Return at most 500 words with exactly: Verdict (`ACCEPT WITH LIMITS`, `REVISE`, or `REJECT`); Critical findings; Required holds; Scenario result; Identifier decision. Treat base-model publication blockers as holds unless they contradict the candidate.
