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
