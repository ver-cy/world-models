You are the single final frozen semantic auditor for EM-LEG-05. Use only the supplied frozen materials. No tools, browsing, external facts, invented identifiers, publication claims, or requests for another review. Reconcile Claude and Grok, decide whether the boundary is settled, then inspect every candidate/profile/fixture/policy artifact for semantic defects. Preserve the settled decision unless the supplied evidence proves it inconsistent.

Return exactly these sections:
1. Verdict on decision and artifacts.
2. Material defects and exact deterministic remediation. Number defects D1...; give literal field/value edits sufficient for a local script, including authority, identity, lifecycle, references, time, provenance, privacy/access, finance separation, incomplete reserved specs and publication holds.
3. Additional fixtures as one fenced JSON array. Each item must have id, target, kind (positive|negative), input, expect, violates, closesDefect; negative cases must also have expectedCode. Fixture IDs and codes must be unique enough for deterministic validation. Include enough positive and negative fixtures to close every defect and all provider invariants.
4. Exact final fixture counts, combining the 4 existing fixtures with your additions.
5. Freeze decision stating that deterministic remediation closes the audit without rerun.

Do not allocate any identifier. Do not promote missing WM-POL-019/020/021/022 specifications. Do not convert projections or dependent records into roots. Treat the visible Grok response as evidence; hidden reasoning and the UI sources control are excluded.

FROZEN MATERIALS

## FILE local-evidence.md
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


## FILE claude-study.raw.md
## Verdict

Reuse **WM-POL-009** as the proceeding/case aggregate under an enterprise litigation profile. It does **not** fully cover LegalCase: it is forum-docket-qualified and explicitly holds the underlying dispute as an external reference, so the cross-proceeding matter has no owner. Raise **Dispute / Matter** as an identifier-unassigned independent candidate.

Candidate decisions: **LegalCase** → reuse WM-POL-009 (profile, no new root). **Claim** → split and reject as a root: the procedural claim/counterclaim/relief sought is a case-owned dependent assertion inside WM-POL-009; a party's factual allegation is a **WM-KNW-007 profile**; an adjudicated finding is authority-owned by WM-POL-021/case. **ProceedingEvent** → case-owned dependent component of WM-POL-009; reject as root. **CaseOutcome** → view/profile over WM-POL-021 judgment plus case-held finality and remedy links; reject as root. No identifiers allocated.

## Evidence

WM-POL-009 (complete): `contains_ids` WM-POL-019;020;021; out_of_scope excludes filing content, evidence lifecycle, judgment content, remedy execution, enforcement masters; boundary flag «дело ≠ форум»; decisions already separate claims from findings, service from deadline, decision from finality. WM-KNW-007 owns truth-apt assertion, author, commitment, scope, confidence, status, and forbids projecting standing as truth. WM-KNW-008 owns reified citation with stance and locator and declares **legal admissibility and chain of custody a gap** — the precise justification for WM-POL-020. WM-KNW-010 owns decision content and rationale and assigns the binding legal instrument to WM-POL-021. WM-ECO-006 is the disputed agreement master and excludes adjudication. WM-ECO-018 owns the reported statement fact and excludes treating a fact as an authoritative position. Prior boundary work: EM-KNW-02 (claim/citation/decision/record split), EM-LEG-02 (norm vs interpretation vs applicability), EM-LEG-04 (case vs grant; authority acts only), EM-FIN-04 (run/issue/knowledge-time immutability), EM-RSK-02 (finding ≠ issue ≠ task ≠ closure).

## Identity/mastership

Distinct identities: dispute/matter; proceeding (forum-qualified docket); forum organization; party role in proceeding; pleading (WM-POL-019); party allegation (WM-KNW-007); procedural claim/counterclaim/defense; issue; evidence item (WM-POL-020); admissibility/use assertion (case-owned); procedural event/order; finding of fact; legal conclusion; judgment/award (WM-POL-021); remedy obligation; appeal/review; enforcement case; financial provision (WM-ECO-018 fact); confirmed debt (obligation master). Case number, title, party, forum, year, ECLI or file digest never identify a case. Forum masters the docket; parties master their own side; the enterprise record is a source-qualified mirror with observation and source-as-of time.

## Dispute/case/proceedings

The dispute is the contested matter (contract, event, offense) and persists across proceedings; the proceeding is one docket in one forum. Multiple proceedings of one dispute link through the dispute root plus typed successor relations (appeal, set-aside, recognition, enforcement, consolidation, severance, transfer, remand). WM-POL-009 alone gives only pairwise successor edges and a joined/severed alias field, and it states no universal identity-continuity rule — insufficient for lineage across forums and jurisdictions. Lineage is therefore preserved by dispute membership plus append-only proceeding-to-proceeding relations, never by reusing one case identity.

## Claims/allegations/findings

Four separable assertion classes, each with author and capacity: (1) procedural claim — proponent, respondent, legal and factual basis, relief sought, amount, disposition, dependency; case-owned. (2) Party allegation of fact — WM-KNW-007 profile with claimant, commitment, scope, evidence bindings; never adjudicated status. (3) Adjudicated finding of fact — decision-maker, burden and standard applied, hearing context, credibility and weight, reasons; authority-owned. (4) Legal conclusion — pinned norm version and provision (EM-LEG-02 discipline). Counterclaim is a claim asserted by the respondent side, not a negation field. Defense is a distinct responsive assertion. Burden and standard are recorded per issue and per claim; an allegation is never upgraded by absence of rebuttal.

## Events/filings/evidence

ProceedingEvent is a dependent, append-only docket entry: actor, authority, rule, effect interval, and separate filing, receipt, acceptance and legally effective service times. Filings are WM-POL-019 children with their own identity; the case holds membership, role, receipt, supersession. Evidence provenance and chain of custody belong to WM-POL-020; the case holds submission, proponent, issue, admission, exclusion, weight and use. WM-KNW-008 supplies generic citation stance and locator only and cannot bear custody or admissibility. Evidence restrictions (sealing, protective order, redaction, confidentiality class) are order-scoped and survive the decision, the appeal and case closure.

## Decisions/outcomes/remedies

WM-POL-021 owns judgment text, deciding composition, reasons, dissent, corrections. WM-KNW-010 may carry the rationale/argument structure of a decision but confers no legal force. The case records membership, outcome, finality assertion, remedy references, publication. CaseOutcome is a projection over judgment identity, disposition, finality state, effective scope and remedy set — materializing it as a root would create a second authority for finality. Remedy (damages, declaration, injunction, costs, interest) is an ordered obligation with addressee, terms, amount, currency and operative scope; performance and satisfaction are external.

## Appeal/review/enforcement

An appeal is a successor proceeding (another WM-POL-009 instance in the appellate forum) plus a typed review relation to the challenged judgment recording route, grounds, deadline, stay and effect on finality. Set-aside or reversal is a new authority act that changes finality state and may render a judgment inoperative; it never deletes the first-instance judgment, findings, orders or evidence rulings. Enforcement and recognition are separate cases with their own jurisdiction and refusal grounds. No reserved identifier for Appeal/Review exists in this dossier.

## Finance boundary

A claimed amount is relief sought inside a procedural claim. A provision or contingent-liability disclosure is a WM-ECO-018 statement fact with measurement basis, estimate binding and disclosure class. A confirmed debt is an obligation established by a final enforceable judgment, an agreed settlement instrument or the contract itself. **Reject the negative case:** recording an исковая сумма as confirmed задолженность conflates relief sought with obligation, skips finality, and imports a litigation estimate into the ledger. Provisioning never becomes legal debt automatically; recognition, derecognition and payment each require their own authorized act.

## Time/provenance/access

Separate: dispute arising, filing, receipt, service, knowledge, hearing, deliberation, decision, correction, legal-effect, finality, publication, enforcement, observation and ingestion times. RFC 3339 with seconds and offset; service time is rule-derived and may differ from transmission and receipt. Access defaults deny; arbitration and sealed material restricted; party, forum, public, confidential, redacted and statistical views are purpose-bound with authority, expiry and re-identification control. Reversal is non-destructive: closure, withdrawal and tombstone only; no cascade to parties, filings, evidence, judgments or enforcement.

## Governance

Only the competent forum actor establishes orders, findings, decisions or finality. Agents may perform reversible clerical docketing and propose validations; adjudication, adverse orders, finality, sealed disclosure, restatement of a financial provision and disposition require accountable authority with separated initiation and authorization.

## Acceptance scenario

Dispute D over contract C-441 spawns proceeding P1. Claim CL-1 (seller, 100,000) and counterclaim CL-2 (buyer, 40,000) are separate claims with separate allegation sets. Evidence item EV-7 is admitted under protective order O-3; EV-9 is excluded. Judgment J-1 grants CL-1 in part, dismisses CL-2, and makes findings F-1..F-4. Appeal proceeding P2 sets J-1 aside on ground G-2. J-1, F-1..F-4, O-3 and all docket events remain resolvable; finality state changes and the remedy becomes inoperative. O-3 restrictions continue in P2. Provision PR-1 in the statement is remeasured only by an authorized act and never becomes debt through J-1 alone or through the claimed 100,000.

## Invariants

1. Dispute, proceeding, forum, party role and judgment have distinct identifiers. 2. Case number, title, party, ECLI or digest never identify a case. 3. Every assertion names author and procedural capacity. 4. Allegation, admission, finding and legal conclusion never merge. 5. Burden and standard are recorded per issue. 6. Evidence identity and custody are external to the use ruling. 7. Admissibility is an authority act, not a flag. 8. Every decision names forum authority, competence and date. 9. Issuance, correction, finality, recognition and enforcement remain distinct. 10. Appeal never erases prior decisions or findings. 11. Reversal is non-destructive and append-only. 12. Restrictions survive decision, appeal and closure. 13. Effective, service, knowledge and observation times remain distinct. 14. Claimed amount is never confirmed debt. 15. Provision recognition requires its own authorized act. 16. Multiple proceedings link by dispute membership plus typed relations.

## Minimal model set

WM-POL-009 (case profile); WM-POL-019, WM-POL-020, WM-POL-021 (must be specified); WM-KNW-007 (allegation profile); WM-KNW-008 (citation reference); WM-KNW-010 (optional rationale); WM-ECO-006 (disputed agreement reference); WM-ECO-018 (provision disclosure). Identifier-unassigned candidates: Dispute / Matter; Appeal / Review record; Enforcement / Recognition case; Remedy Obligation.

## Holds

Missing reserved specs: **WM-POL-019, WM-POL-020, WM-POL-021** are `candidate`/boundary-review-required with no specification, yet WM-POL-009 declares all three CHILD `required: true` — an unsatisfiable composition. **WM-POL-022 contradiction:** the registry records it as *Sanction / Sentence* (parent WM-POL-021), not Appeal / Review; no appeal identifier is reserved. **WM-POL-023** is referenced by WM-POL-021 for enforcement but absent from the reservations — dangling. All CONTAINS relations are `candidate` with unapproved cardinality and lifecycle contracts. WM-KNW-010 carries three conflicting edges to WM-KNW-007 (CHILD, EXTEND, ALIGN) and admits the parent relation is absent from the ledger. WM-KNW-008 declares admissibility and chain of custody a gap. WM-ECO-018 contradicts its own out-of-scope in a service role (per EM-FIN-04). WM-POL-009, WM-ECO-018 are single-provider Codex drafts with waived external review; WM-KNW-007/008/010 are Claude-only. All bases are `publishableCanonical: false`. Jurisdictional civil, criminal, administrative, arbitral and appellate profiles, Akoma Ntoso/ECLI/LegalRuleML crosswalks and fixtures are unverified. No canonical completeness, installability or publication readiness is claimed.


## FILE grok-prompt.md
# Exact unsent Grok prompt — EM-LEG-05

Independent enterprise metamodel review. Do not browse, invent identifiers or claim publication readiness.

EM-LEG-05 covers LegalCase, Claim, ProceedingEvent and CaseOutcome. Complete WM-POL-009 covers Court / Arbitration Case; adjacent drafts cover claims/propositions, citations/evidence, decision rationale, contracts and financial statements. Reserved WM-POL-019 Filing, WM-POL-020 Evidence Item and WM-POL-021 Judgment lack complete specs.

Assess this proposal: profile WM-POL-009 as one forum-qualified proceeding; create an identifier-unassigned Dispute / Matter root for the contested matter across proceedings; keep procedural claim/counterclaim/defense and ProceedingEvent case-owned; profile allegations on WM-KNW-007; keep findings authority-owned; treat CaseOutcome as a projection over judgment, finality and remedies. Keep Appeal / Review, Enforcement / Recognition Case and Remedy Obligation unassigned gaps pending registry adjudication. Allocate no identifier.

Separate dispute, proceeding, forum, party role, pleading, allegation, claim, evidence item, admissibility/use, docket event, finding, legal conclusion, judgment, remedy, appeal, enforcement, financial provision and confirmed debt. Decide whether Dispute / Matter needs independent identity and whether any requested candidate needs another root.

Test a claim, counterclaim and first-instance decision later set aside on appeal. Preserve all decisions, findings, evidence restrictions, service/effective/knowledge times and source provenance. Reject the claimed amount as confirmed debt or automatic financial provision.

Return <=900 words with: Verdict; strongest evidence; strongest counterexample; identity/mastership; dispute/proceedings; claims/allegations/findings; events/filings/evidence; judgments/outcomes/remedies; appeal/enforcement; finance boundary; time/access/provenance; governance; scenario; at least 10 invariants; minimum model set; blockers. Flag missing reserved specs and relation contradictions.


## FILE grok-study.raw.md
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


## FILE candidate-allocation-offline/allocation-candidate.json
{"format":"vercy-model-allocation-candidate/v1","contourId":"EM-LEG-05","proposedName":"Dispute / Matter","modelId":null,"registryId":null,"allocationState":"unassigned","decision":"NEW MODEL","canonicalPublishable":false,
"identityTest":{"stableIdentity":"A contested matter persists across transfers, severance, consolidation, first instance, appeal, recognition and enforcement proceedings.","versionIdentity":"Scope, parties, issues or linkage changes append revisions while distinct forum proceedings keep their own identities.","independentLifecycle":["identified","active","partially-resolved","resolved","reopened","closed","retained"],"mastership":"authorized legal-matter management authority"},
"boundary":{"owns":["stable dispute or matter identity","subject and controversy scope","party capacity references","membership of distinct proceedings","typed successor, severance and consolidation links","resolution and retained-history state"],"references":[{"target":"WM-POL-009","purpose":"Docket-qualified proceedings belonging to the matter"},{"target":"WM-KNW-007","purpose":"Party allegations and other claims"},{"target":"WM-KNW-008","purpose":"Citation stance and locators"},{"target":"WM-KNW-010","purpose":"Structured rationale without legal-force mastership"},{"target":"WM-ECO-006","purpose":"Contract or agreement context"},{"target":"WM-ECO-018","purpose":"Separately authorized litigation provisions"}],"excludes":["forum docket identity","filing content and evidence custody","judgment or award content","remedy execution and satisfaction","financial provision or debt identity"]},
"objects":{"DisputeMatter":{"identity":["disputeMatterId"],"required":["subject","controversyScope","partyCapacityRefs","status"],"optional":["originatingInstrumentRef","successorRef"],"lifecycle":["identified","active","partially-resolved","resolved","reopened","closed","retained"]},"ProceedingMembership":{"identity":["disputeMatterId","proceedingRef"],"required":["relationKind","validFrom"],"optional":["validTo","challengedDecisionRef","grounds","effect"]}},
"invariants":["Dispute, proceeding, forum, party role and judgment remain distinct identities.","One dispute can link multiple forum-qualified proceedings.","Transfer, severance, consolidation, appeal, recognition and enforcement never merge proceeding identities.","Party identities and forum organizations remain externally mastered.","Claims, counterclaims and defenses remain proceeding-owned assertions.","Allegation, admission, finding and legal conclusion never merge.","Appeal never erases prior decisions, findings or evidence rulings.","Reversal and set-aside are append-only authority acts.","Access restrictions survive until an authorized successor changes them.","Claimed amount never becomes confirmed debt.","Financial provision requires a separately authorized accounting act.","Closure preserves filings, evidence, judgments and successor links.","Service, effect, finality, enforcement and knowledge times remain distinct.","Dispute identifiers are never recycled."],
"holds":["Registry allocation is pending and no identifier may be guessed.","Independent Grok review is pending.","Appeal / Review, Enforcement / Recognition Case and Remedy Obligation remain unadjudicated gaps.","WM-POL-019/020/021 specifications and WM-POL-022 semantics require resolution.","Frozen audit, crosswalks and source pins remain pending."]}


## FILE candidate-allocation-offline/profile-candidate.json
{"format":"vercy-enterprise-profile-candidate/v1","contourId":"EM-LEG-05","name":"Enterprise Legal Case, Claim and Outcome Binding","decision":"PROFILE","newRuntimeId":false,"bases":["WM-POL-009","WM-POL-019","WM-POL-020","WM-POL-021","WM-POL-022","WM-KNW-007","WM-KNW-008","WM-KNW-010","WM-ECO-006","WM-ECO-018"],"constraints":["WM-POL-009 owns one docket-qualified proceeding, forum assignment, roles, events, schedules, hearings, rulings, finality and closure.","Procedural claims, counterclaims, defenses and proceeding events remain case-owned assertions.","Party allegations profile WM-KNW-007 while adjudicated findings and legal conclusions remain authority-owned.","Filing content, evidence custody and judgment content remain external masters even when the case records docket use.","Case Outcome is a projection over judgment, finality and remedy references rather than another root.","Provisioning, recognition, derecognition and payment never follow automatically from a claimed or judgment amount."],"holds":["Dispute / Matter remains identifier-unassigned.","Required child specifications and enforcement references are incomplete.","Independent Grok review and frozen audit remain pending."]}


## FILE candidate-allocation-offline/fixtures.json
{"format":"vercy-enterprise-allocation-fixtures/v1","candidateName":"Dispute / Matter","cases":[{"id":"first-instance-appeal","kind":"positive","input":"Dispute D has first-instance proceeding P1 and appeal P2 challenging J1.","expect":"D links both proceedings while P1, P2 and J1 retain separate identities."},{"id":"protected-evidence","kind":"positive","input":"Evidence EV7 is admitted under protective order O3 and the case later closes.","expect":"The restriction survives closure and appeal until an authorized successor order changes it."},{"id":"reversal-history","kind":"positive","input":"Appeal P2 sets judgment J1 aside.","expect":"J1 and its findings remain resolvable while remedy effect changes append-only."},{"id":"claim-is-debt","kind":"negative","input":"A pleaded amount is booked as confirmed debt.","expect":"The inference is rejected without an enforceable decision, settlement or contract basis."},{"id":"appeal-overwrites","kind":"negative","input":"An appellate reversal deletes the first-instance judgment.","expect":"Deletion is rejected."},{"id":"case-owns-evidence","kind":"negative","input":"A docket-use ruling replaces evidence custody and integrity history.","expect":"The substitution is rejected."},{"id":"case-number-global-id","kind":"negative","input":"A local case number alone is used as global proceeding identity.","expect":"The identity is rejected without forum-qualified authority."}]}


## FILE candidate-allocation-offline/validation-policy.json
{
  "format": "vercy-allocation-validation/v1",
  "requirements": {
    "modelIdMustBeNull": true,
    "registryIdMustBeNull": true,
    "allocationState": "unassigned",
    "minimumInvariants": 8,
    "minimumReferences": 3,
    "minimumFixtures": 3,
    "requiresPositiveAndNegativeFixtures": true,
    "requiresStableIdentityStatement": true,
    "requiresIndependentLifecycle": true
  }
}


## FILE candidate-allocation-offline/README.md
# EM-LEG-05 Dispute / Matter delta

Profiles existing proceeding, claim and outcome boundaries and preserves Dispute / Matter as an identifier-unassigned root spanning multiple proceedings. No identifier is allocated.
