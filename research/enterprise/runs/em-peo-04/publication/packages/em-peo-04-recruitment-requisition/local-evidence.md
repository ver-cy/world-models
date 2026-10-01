# EM-PEO-04 local synthesis

## Disposition

- Propose identifier-unassigned **Recruitment Requisition** and **Candidacy** roots.
- Complete and narrow reserved WM-ORG-008 to the asserted Vacancy / Opening; do not persist derived seat vacancy there.
- Reuse WM-ACT-039 as the recruitment campaign/process aggregate. Hiring Stage remains process-owned.
- Profile Interview Assessment as a typed pair over WM-ACT-025 Meeting / Session and WM-ACT-034 Assessment / Evaluation.
- Profile WM-ECO-021 Offer / Quote for an employment offer.
- Reuse WM-PER-001 Person, WM-ORG-004 Position and WM-ORG-005 Employment; keep assignment external in WM-ORG-016.
- Allocate no catalogue or runtime identifier.

## Identity and mastership

The approved need, requisition, position, derived vacancy, asserted opening, posting, person, candidacy, recruitment process, stage definition, stage occurrence, interview, assessment result, selection decision, offer, contract, assignment and employment remain separately identified.

The employer authority masters requisitions and openings. The position steward masters positions. WM-PER-001 remains the person anchor. The assessor masters assessment results, the decision authority masters the selection record, the offer issuer masters issued offer versions, and employment remains bilateral. ATS records never become the universal person or employment master.

## Requisition, position and opening

Recruitment Requisition is a standing, versioned authorization to recruit one or more seats. It owns requested headcount, reason, budget and target start plus draft, approval, funding, partial-fill, closure and cancellation states. WM-REC-010 records each approval act; it does not replace the authorization.

WM-ORG-004 derives vacant capacity from authorized capacity and occupancy at an as-of instant. WM-ORG-008 must instead own an asserted opening: the governed decision to recruit against a position or requisition, with opening count, scope, effective interval and status. A posting is a time-bounded projection and may reference zero, one or many positions.

The current WM-ORG-008 purpose collapses vacancies, applications, matching and placement. Completion must narrow it to openings. Candidacy moves to its own root, matching becomes a purpose-qualified scored assertion, and placement resolves through assignment and employment.

## Person, candidacy and process

Candidate is a purpose-scoped role over a WM-PER-001 anchor. A provisional sourced record carries assurance and remains a proposed link until authorized evidence resolves it. Name, email or name plus birth date never justify an automatic merge.

Candidacy binds one person, one opening and one recruitment process. It owns submission and receipt times, supplied documents, declarations, status history, withdrawal and outcome. A later application creates a new candidacy while preserving the same person anchor and lineage to the earlier case.

WM-ACT-039 owns the campaign/process. A frozen process-design release owns ordered stage definitions and criteria. Each per-candidacy stage occurrence cites that exact release. Ranking and recommendation outputs are not selection decisions.

## Interview, assessment, decision and offer

WM-ACT-025 owns the interview session, participants, presence, accommodations and recording notice. WM-ACT-034 owns separately finalized assessment results with pinned criteria, method, evidence, scale, assessor competence, impartiality and moderation. WM-REC-010 owns the selection decision with author, authority, reasons, dissent, recusal, validity and challenge route.

The employment-offer profile reuses WM-ECO-021 immutable issued versions, contingencies, expiry and attributable response or withdrawal events. Product-specific price-line fields are not applicable. Offer acceptance, contract formation, employment and assignment remain distinct events and authorities.

## Privacy and retention

Possession of a CV is never unlimited consent. Each candidacy records controller, purpose, lawful basis, notice version and rights route. Cross-company reuse requires a separate basis or explicit scoped talent-pool grant. Retention triggers are data-class specific and include process closure, rejection plus challenge window, withdrawal, consent expiry and vetting-data destruction. Legal hold suspends disposition; disposition never cascades to person, position or employment masters.

## Required invariants

1. One candidacy binds one person, one opening, one process and an interval.
2. One requisition may authorize several openings.
3. Asserted opening is not derived vacant capacity.
4. Posting is a projection, not an opening master.
5. Candidate identity is not a second person identity.
6. Stage occurrence pins the process-design release.
7. Score, recommendation and decision remain distinct assertions.
8. Every selection decision identifies author, authority, pinned criteria and reasons.
9. Issued offer versions are immutable.
10. Offer acceptance does not itself create contract, employment or assignment.
11. Consent is qualified by purpose, controller and period.
12. Withdrawal and rehire preserve lineage without duplicating Person.

## Acceptance result

One approved requisition authorizes two seats and associated openings. Three candidacies reference three people without creating duplicate person anchors. A withdrawn offer remains resolvable as an immutable issued version with an attributable withdrawal. A later rehire creates a new candidacy, offer and employment while reusing the prior person anchor and preserving historical lineage.

## Holds

WM-ORG-008 has no current specification, source or approved relations and remains a previous-version migration record. WM-ACT-039, WM-ECO-021 and WM-ORG-005 are non-canonical drafts; WM-ACT-034 and WM-ACT-025 retain boundary and evidence gaps. WM-ORG-016 is referenced but absent from the frozen reservations. Recruitment Requisition and Candidacy lack allocations. Required relations, jurisdictional review, fairness and assessment-science review, interoperability crosswalks, source pins and round-trip fixtures remain absent. This checkpoint is not an installable release.
