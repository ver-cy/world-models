# EM-LEG-05 local synthesis

## Disposition

- Reuse/profile WM-POL-009 as Legal Case / Proceeding.
- Propose identifier-unassigned **Dispute / Matter** because the contested matter persists across distinct forum-qualified proceedings.
- Keep procedural claim, counterclaim, defense and proceeding event as case-owned assertions.
- Profile party allegations on WM-KNW-007; keep adjudicated findings and legal conclusions authority-owned by the judgment/case boundary.
- Treat Case Outcome as a projection over judgment, finality and remedy references, not a root.
- Leave Appeal / Review, Enforcement / Recognition Case and Remedy Obligation as identifier-unassigned gaps pending missing-spec and registry adjudication.
- Allocate no catalogue or runtime identifier.

## Identity and mastership

WM-POL-009 owns one docket-qualified proceeding: case identity, forum assignment, procedural roles, docket events, schedules, hearings, use rulings, child membership, finality and closure. It does not own the underlying dispute, filing content, evidence custody, judgment content, remedy execution or enforcement.

A Dispute / Matter survives transfer, severance, consolidation, first instance, appeal, recognition and enforcement across forums and jurisdictions. Multiple proceedings retain separate identities and link through dispute membership plus typed successor relations.

Forum organizations remain external. Parties master their identity; the forum masters the docket; the enterprise case record is a source-qualified mirror.

## Claims, allegations and findings

A procedural claim records proponent, respondent, legal and factual basis, relief sought, amount, disposition and dependencies within a case. Counterclaim and defense are distinct responsive assertions.

A party allegation is a WM-KNW-007 profile with author, capacity, commitment, scope and evidence bindings. An adjudicated finding records the deciding authority, issue, burden, standard, credibility, weight and reasons. A legal conclusion pins the applied norm and provision version. These states never upgrade one another implicitly.

## Events, filings and evidence

Proceeding Event is an append-only docket component with actor, authority, rule, effect and distinct filing, receipt, acceptance, service and knowledge times.

WM-POL-019 must own filing identity and content; the case owns docket membership and role. WM-POL-020 must own evidence identity, custody and integrity; the case owns submission, admission, exclusion, weight and use. WM-KNW-008 supplies citation stance and locator only.

Evidence restrictions, protective orders, sealing and redaction survive decision, appeal and closure unless an authorized successor order changes them.

## Decisions, remedies and appeals

WM-POL-021 must own judgment or award identity, text, deciding composition, reasons, dissent and corrections. WM-KNW-010 can structure rationale but never confers legal force. Case Outcome is a view over judgment identity, disposition, finality, operative scope and remedy set.

Appeal is a successor proceeding with a typed review link to the challenged decision, including route, grounds, deadline, stay and effect. A reversal or set-aside appends a new authority act and never deletes the prior decision, findings or evidence rulings.

Recognition and enforcement use distinct proceedings and jurisdictions. Remedy execution and satisfaction remain external.

## Finance boundary

A claimed amount is relief sought, not confirmed debt. A litigation provision is a WM-ECO-018 statement fact with its own estimate and authorization. A debt requires a final enforceable decision, settlement instrument or contractual basis. Provisioning, recognition, derecognition and payment never follow automatically from a claim or judgment amount.

## Time, provenance and access

Dispute arising, filing, receipt, service, hearing, deliberation, decision, correction, legal effect, finality, publication, enforcement, observation, ingestion and knowledge times remain distinct.

Access defaults deny. Party, forum, public, confidential, sealed, redacted and statistical views are purpose-bound and authority-scoped. Non-destructive closure preserves parties, filings, evidence, judgments and successor proceedings.

## Acceptance result

Dispute D over contract C-441 has proceeding P1. Claim CL-1 seeks 100,000; counterclaim CL-2 seeks 40,000. EV-7 is admitted under protective order O-3 and EV-9 excluded. Judgment J-1 partly grants CL-1 and dismisses CL-2. Appeal P2 later sets J-1 aside. J-1, its findings, O-3 and all docket events remain resolvable; the remedy becomes inoperative while O-3 continues. Financial provision PR-1 is remeasured only by a separately authorized accounting act and never becomes debt from the claimed amount.

## Required invariants

1. Dispute, proceeding, forum, party role and judgment have distinct identities.
2. Case number, title, party, ECLI and digest never identify a case alone.
3. Every assertion names author and procedural capacity.
4. Allegation, admission, finding and legal conclusion never merge.
5. Burden and standard are recorded per issue.
6. Evidence identity and custody remain external to case-use rulings.
7. Admissibility is an authority act.
8. Decisions identify forum authority, competence and date.
9. Issuance, correction, finality, recognition and enforcement remain distinct.
10. Appeal never erases prior decisions or findings.
11. Reversal is append-only.
12. Access restrictions survive until an authorized successor changes them.
13. Service, effect, knowledge and observation times remain distinct.
14. Claimed amount is never confirmed debt.
15. Financial provision recognition requires its own authority.
16. Multiple proceedings link through dispute membership and typed relations.

## Holds

Reserved WM-POL-019, WM-POL-020 and WM-POL-021 have no complete specifications, yet WM-POL-009 requires them as CHILD components. WM-POL-022 is reserved as Sanction / Sentence, contradicting the apparent Appeal / Review expectation; WM-POL-023 enforcement references are incomplete. Candidate CONTAINS relations lack approved lifecycle and cardinality contracts. WM-KNW-010 has conflicting CHILD, EXTEND and ALIGN edges to WM-KNW-007. Evidence custody/admissibility remains a declared gap. Crosswalks, source pins and fixtures are unverified. Base drafts are non-canonical, so no installability or publication-readiness claim is made.

## Provider reconciliation and frozen audit

Grok confirmed the independent Dispute / Matter boundary and the WM-POL-009 proceeding profile. The frozen audit preserved the boundary and supplied 69 exact fixtures. Twenty-four artifact defects were remediated deterministically without rerun. Final fixtures: 76 (29 positive, 47 negative).
