Verdict: Conditionally accept the proposal. Allocate no identifier. Profile WM-POL-009 only as one forum-qualified proceeding (court or arbitration case). Give the contested matter an identifier-unassigned Dispute / Matter root. Keep procedural claim, counterclaim, defense and ProceedingEvent case-owned. Profile allegations on WM-KNW-007. Keep findings and legal conclusions authority-owned. Treat CaseOutcome as a projection over judgment, finality and remedies, not their master. Leave Appeal / Review, Enforcement / Recognition Case and Remedy Obligation unassigned pending registry adjudication.

Strongest evidence: The required scenario cannot be stored if the first-instance decision is overwritten by the appeal. One contested matter can span first instance, appeal, remand and later enforcement or recognition in another forum. An independent Dispute / Matter keeps continuity of claim, counterclaim and evidence restrictions without making WM-POL-009 the matter. CaseOutcome as projection avoids a second master of judgment text, finality and remedies.

Strongest counterexample: A single-forum matter that ends in one final judgment with no related proceeding. A Dispute root then looks like an empty wrapper. That does not defeat independent identity: later related filings must not force renumbering of the original proceeding, and collapsing matter into the case still loses the set-aside decision if an appeal appears. A worse failure is treating the claimed amount as confirmed debt.

Identity / mastership: Dispute / Matter owns cross-proceeding identity of the contested subject only (unassigned). WM-POL-009 owns one forum-qualified proceeding: forum qualifier, docket, party roles in that forum, procedural claims and ProceedingEvents. Party role is not the party. Pleading is not the claim. Allegation is a party proposition on WM-KNW-007, not a claim or a finding. Finding and legal conclusion are authority-owned. Judgment remains an authority artifact (reserved WM-POL-021, incomplete). CaseOutcome projects it. Remedy Obligation is not implied. Financial provision and confirmed debt sit outside this package.

Dispute / proceedings: A Dispute / Matter may relate to zero or more proceedings; each proceeding has one primary Dispute / Matter. Forum qualifies the proceeding and is not the matter. Parallel or sequential proceedings (trial, appeal, recognition) stay distinct instances. Do not subtype appeal or enforcement into the completed WM-POL-009 profile.

Claims / allegations / findings: Procedural claim, counterclaim and defense are owned by the proceeding that received them. An allegation is an asserted proposition, profiled on WM-KNW-007, and may support more than one claim. A finding is the authority’s determination of fact; a legal conclusion is the authority’s application of law. Neither is rewritten when a later proceeding sets the judgment aside. Do not equate allegation, claim, finding and conclusion.

Events / filings / evidence: ProceedingEvent is case-owned docket chronology, not a filing specification. WM-POL-019 Filing, WM-POL-020 Evidence Item and WM-POL-021 Judgment lack complete specs and are blockers. Evidence item, admissibility and permitted use are distinct; admissibility and use are proceeding-scoped restrictions and are not properties of the item alone. Relation contradiction: treating CaseOutcome as both projection and owner of remedies, or treating ProceedingEvent as the missing Filing spec.

Judgments / outcomes / remedies: Preserve every decision. CaseOutcome may summarize operative result, finality status and linked remedies for a point in time; it must not be the system of record for judgment text, reasons, finality event or remedy terms. Remedy Obligation remains an unassigned gap.

Appeal / enforcement: Appeal / Review and Enforcement / Recognition Case are separate proceeding kinds, unassigned. An appeal does not replace the first-instance proceeding. Enforcement does not create the debt.

Finance boundary: Reject the claimed amount as confirmed debt or automatic financial provision. A claim states a position. A judgment may award an amount. Confirmed debt and provision require separate finance recognition after finality and enforceability, not modeled here. Adjacent financial-statement drafts must not subscribe to claim amounts.

Time / access / provenance: Service time, effective time and knowledge time are distinct and retained with source provenance. Evidence restrictions remain attached to the ruling that made them. Access to a set-aside decision is not withdrawn by the later outcome.

Governance: No identifier allocation. Reserved incomplete specs stay reserved. Unassigned gaps stay unassigned until registry adjudication. Adjacent drafts (claims/propositions, citations/evidence, decision rationale, contracts, financial statements) may be profiled only where ownership above is explicit.

Scenario: Claim A and counterclaim B are filed in proceeding P1 under Dispute / Matter M. First-instance decision D1 partly grants A, dismisses B, with findings, an evidence restriction, and recorded service, effective and knowledge times. Appeal proceeding P2 sets D1 aside and remands. Later decision D2 issues. D1, its findings, the restriction, all three times and source provenance remain. A’s claimed amount never becomes confirmed debt or a provision.

Invariants:

1. A Dispute / Matter relates to zero or more proceedings; a proceeding has exactly one primary Dispute / Matter.
2. A WM-POL-009 instance is one forum-qualified proceeding, not the matter.
3. Procedural claim, counterclaim and defense are owned by the receiving proceeding.
4. An allegation is a WM-KNW-007 proposition and is not a claim, finding or judgment.
5. A finding is authority-owned and survives set-aside.
6. Setting aside a decision does not delete that decision, its findings, evidence rulings or provenance.
7. CaseOutcome projects judgment, finality and remedies and does not master them.
8. Claimed amount is not confirmed debt and does not create a financial provision.
9. Service, effective and knowledge times are distinct and retained.
10. Admissibility and permitted use are proceeding-scoped and distinct from the evidence item.
11. Appeal / Review and Enforcement / Recognition are not completions of the first-instance WM-POL-009 profile.
12. Remedy Obligation is not implied by CaseOutcome.
13. Party role is distinct from party and from pleading.
14. This review allocates no identifier.

Minimum model set: unassigned Dispute / Matter; WM-POL-009 proceeding; forum qualifier; party role; case-owned claim / counterclaim / defense; allegation profiled on WM-KNW-007; authority-owned finding and legal conclusion; case-owned ProceedingEvent; proceeding-scoped admissibility/use; CaseOutcome as projection only. Filing, Evidence Item, Judgment, Appeal / Review, Enforcement / Recognition and Remedy Obligation are outside the minimum set until specified.

Blockers: incomplete reserved WM-POL-019, WM-POL-020 and WM-POL-021; unassigned Appeal / Review, Enforcement / Recognition and Remedy Obligation; contradiction if CaseOutcome both projects and owns remedies, or if claim amount feeds finance. No publication readiness is claimed.
