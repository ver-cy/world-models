# Frozen no-tools semantic audit — EM-ORG-07

You are the final static semantic auditor. Use only this frozen packet. Do not browse, call tools, invent identifiers, grant publication authority or infer private attributes.

The result is a PROFILE over WM-ORG-013 Stakeholder / Interest, WM-KNW-007 Claim / Proposition, WM-ACT-034 Assessment / Evaluation and WM-ACT-008 Plan / Roadmap. Party masters remain WM-ORG-001 and WM-PER-001. No new runtime/model identifier is proposed.

Reconciled boundary:
1. Party identity is distinct from stakeholder participation. One party may have different addressable WM-ORG-013 relation instances in different project or decision perimeters.
2. Every stakeholder relation binds party, subject matter, perimeter, viewpoint, valid period, recorded/knowledge time and evidence or explicit unknown. Contextual fields never write through to the party master.
3. Stakeholder Interest profiles WM-ORG-013. Declared interests stay distinct from analyst hypotheses; conflicting interests may coexist.
4. Expectation is an attributed WM-KNW-007 claim bound to the stakeholder relation. It creates no duty, acceptance or permission.
5. Stakeholder Assessment profiles WM-ACT-034 and names the addressable stakeholder relation, never the party, as subject. Influence, impact, salience and priority are dated results with pinned method, scale, assessor, uncertainty, evidence and validity.
6. Reassessment creates a successor assessment citing the prior record and preserving its method, basis and result. It never overwrites history or propagates across perimeters.
7. Engagement Plan profiles WM-ACT-008. The engaging organization owns the plan; the stakeholder remains a referenced relation. Replanning versions the plan and preserves history.
8. Registration grants no outreach, processing, disclosure or decision authority. Execution requires a separate permission/decision boundary.
9. Representation is perimeter-, viewpoint- and period-scoped and contestable. Challenges and dissent add attributable records; aggregation never deletes or reattributes them.
10. Privacy restrictions on parties, relations, expectations and evidence survive projection, aggregation and cross-perimeter copy. A published rating cannot expose or reconstruct restricted evidence.
11. Client, owner, executor and stakeholder are independent roles. Affectedness and rights do not depend on influence or participation.
12. Missing, withheld, not-yet-heard, indeterminate and low are distinct states.

Scenario: Counterparty C is one party. Project A owns relation R-A and assessment S-A1=`low influence` with method M1, uncertainty U1 and evidence E1. Project B owns relation R-B and has no inherited rating. Reassessment in A creates S-A2=`medium influence`, cites S-A1 and preserves M1/U1/E1. C has no influence attribute. B remains unchanged. Any attempt to use C as assessment subject, overwrite S-A1, copy the rating or restricted expectation into B, or treat registration as permission fails closed.

Audit questions:
- Is there a hidden aggregate or identifier despite `newRuntimeId=false`?
- Are party, stakeholder relation, interest, expectation, assessment, plan and permission mastership unambiguous?
- Is relation addressability sufficient without creating a new master class?
- Are history, conflict, contestability and privacy preserved through projections?
- Identify any contradiction that makes even a held profile unsafe.

Return at most 500 words with exactly: Verdict (`ACCEPT WITH LIMITS`, `REVISE`, or `REJECT`); Critical findings; Required holds; Scenario result; Identifier decision. Treat base-model publication blockers as holds unless they contradict the profile.
