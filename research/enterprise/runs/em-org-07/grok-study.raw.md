## Verdict
**Accept with conditions.** None of StakeholderInterest, Expectation, StakeholderAssessment, or EngagementPlan requires independent party/master identity. Each rides a given type: WM-ORG-013, WM-KNW-007, WM-ACT-034, WM-ACT-008. Accept only if the WM-ORG-013 stakeholder relation is an addressable, perimeter-bound instance that can be the assessment subject. Reject any path that writes influence, impact, role, or engagement approach onto the party master, or that treats registration as permission.

## Strongest evidence
The required two-project plus reassessment test holds only when influence and impact live on dated StakeholderAssessment records whose **subject is the stakeholder relation**, not the party. Project A’s assessment (method, uncertainty, evidence, period) remains intact when A is reassessed. Project B uses a different map and therefore a different relation instance; A’s assessment cannot appear on B. The party master is unchanged. One test shows: no new identity class is required; assessments are not traits; history is preserved by WM-ACT-034 record identity.

## Strongest counterexample
Stamp `low influence` on the counterparty master, or on a reusable interest not bound to a perimeter. Open Project B: the label inherits. Reassess A by overwrite and the original method, uncertainty, and evidence disappear. Representation or contactability in A is treated as global. That is the failure the proposal must close.

## Identity / mastership
**Decision: no candidate requires independent identity.**

- Party (person or organization) is the only durable actor master.
- Stakeholder participation is a WM-ORG-013 relation instance, not a second party.
- StakeholderInterest, Expectation, StakeholderAssessment, EngagementPlan have **record/instance identity** inherited from the profiled type so they can be cited, versioned, contested, and historically preserved. That is not a new master class.
- Master of stakeholder context is the project/decision perimeter that owns the map.
- No contextual attribute may write through to the party master.
- Cross-project reuse is by party reference only.

**Collapse risk:** if WM-ORG-013 does not make the relation addressable, WM-ACT-034 has no legal subject except the party, and the rejected trait model returns. That is a relation-record gap, not a reason to mint a new identity class.

## Stakeholder context
A stakeholder record is Party × subject matter × project/decision perimeter × viewpoint × period × evidence, plus role. Different maps are different relations that share a party. Role, interest, expectation, influence, impact, and engagement approach exist only inside that tuple. Representation is a scoped mandate over a relation, not ownership of the party.

## Interest / expectation
StakeholderInterest profiles WM-ORG-013. It is a participation-and-concern record, not a person. Same party may hold multiple, including conflicting, interests in one perimeter; coexistence is allowed.

Expectation is an attributed WM-KNW-007 claim, not a synonym of Interest and not a party trait. Interest = what is at stake. Expectation = a claim about what will or should occur, with claimant, viewpoint, period, and evidence. Stakeholder statement and analyst interpretation stay distinct attributions. Registering an expectation creates no duty, agreement, or permission.

## Assessment
StakeholderAssessment profiles WM-ACT-034. Subject = the stakeholder-relation instance, never the party master. Influence, impact, attitude, and salience are dated assessment content with method, uncertainty, assessor, period, and evidence. Reassessment adds a new act that cites the prior act as basis; it does not overwrite and does not propagate across perimeters. Current-use views may show the latest in-perimeter assessment; they must not erase or export the old one.

## Engagement plan
EngagementPlan profiles WM-ACT-008. It is the engaging organization’s plan toward one or more relation instances in a perimeter and period. Plan owner ≠ stakeholder. Approach is plan content, not a role on the party. The plan may reference interests, expectations, and current assessments; it does not own them and does not grant outreach or disclosure rights. Replanning versions WM-ACT-008; the prior plan remains historical. A plan in A has no effect on B.

## Conflict / contestability
Conflicting interests and contrary expectations may coexist; coexistence is not inconsistency. A contrary expectation is another claim unless explicit supersession is recorded. Representation is scoped to perimeter, viewpoint, and period, and is contestable: a challenge is a dated claim or assessment against that representation record. Dissent stays attributable to the dissenting party. Aggregation or “consensus” must not drop or reattribute dissent. Contest adds a contrary record; it does not delete the prior basis.

## Privacy
Registration grants no outreach, processing, or disclosure permission. Execution of an EngagementPlan still requires a separate permission/decision boundary (no new code). Privacy restrictions on the party and on specific relation records survive projection, aggregation, reuse of assessments, and copy of maps into other perimeters. B must not inherit A’s contactability, representation mandate, or disclosed expectation text. Restricted evidence stays restricted even when a rating is published.

## Scenario
Counterparty C is one durable party.

- **Project A:** relation R-A; interests I-A1, I-A2 (may conflict); attributed expectations; assessment S-A1 = low influence, method M1, uncertainty U1, evidence E1, period P1, viewpoint V-A.
- **Project B:** different map, relation R-B, own interests and expectations. S-A1 does not appear. Influence is unbound until B assesses R-B.
- **Reassessment in A:** S-A2 = medium influence, M2, U2, E2, P2, subject still R-A. S-A1 remains citable. C has no influence attribute. B is unchanged.

Reject: attach `low influence` to C; inherit it into B; overwrite S-A1.

## Invariants
1. Party identity ≠ stakeholder participation.
2. Every role, interest, expectation, influence, impact, and engagement approach binds subject matter, perimeter, viewpoint, period, and evidence.
3. Influence and impact exist only as dated WM-ACT-034 records with method and uncertainty; never as party traits.
4. Assessment subject is the stakeholder relation, not the party master.
5. Assessments do not inherit across perimeters or maps.
6. Reassessment adds a record and preserves prior basis; it does not overwrite.
7. Conflicting interests and contrary expectations may coexist.
8. Expectation is an attributed WM-KNW-007 claim, not an anonymous project fact.
9. Registration ≠ outreach, processing, or disclosure permission.
10. Representation is scoped and contestable; it does not follow the party into another map.
11. Dissent remains attributable; projections may not reattribute or drop it.
12. Privacy restrictions survive projection, aggregation, reuse, and cross-perimeter copy.
13. EngagementPlan cannot authorize contact beyond recorded permission.
14. No candidate requires independent master identity.

## Minimum model set
Party (person | organization); WM-ORG-013 Stakeholder / Interest plus StakeholderInterest profile; WM-KNW-007 Expectation; WM-ACT-034 StakeholderAssessment (subject = relation); WM-ACT-008 EngagementPlan; binding tuple; method and uncertainty on assessments; supersession/history links; scoped representation and attributable dissent; privacy restriction that survives projection; permission/decision boundary distinct from registration.

## Blockers
- Influence or impact stored on Party or on an unbound reusable profile.
- Shared stakeholder profile reused across projects without a new relation instance.
- Assessment overwrite instead of dated supersession.
- Unbound interest or expectation.
- Registration treated as contact or disclosure right.
- Representation treated as a global mandate.
- Dissent folded into consensus with no attribution trail.
- Privacy flags stripped by projection.
- Minting a new identity class for any of the four candidates.
- Using the party as WM-ACT-034 subject.
- WM-ORG-013 relation not addressable as assessment subject.
