**Verdict.** Conditional accept. Create identifier-unassigned Recruitment Requisition and Candidacy roots; complete and narrow WM-ORG-008 to asserted Vacancy/Opening; reuse WM-ACT-039 for campaign/process; keep Hiring Stage process-owned; profile Interview Assessment across WM-ACT-025 and WM-ACT-034; profile WM-ECO-021 as an employment offer; reuse WM-PER-001, WM-ORG-004 and WM-ORG-005. Allocate no identifier. Do not claim publication readiness. WM-ORG-008 must stop owning applications, matching and placement. The reserved collapse is the specification gap; narrowing is the close, not a new allocated root.

**Strongest evidence.** One requisition, two seats, three candidacies, a withdrawn offer and a later rehire of the same Person cannot be expressed if vacancy masters applications, match scores or placement. Complete drafts already exist for Person, Position, Employment, Recruitment/Hiring Process, Meeting/Session, Assessment/Evaluation, Decision/Approval Record and Offer/Quote. The reserved WM-ORG-008 package is the only named work item that still fuses four different identities.

**Strongest counterexample.** Internal mobility or succession with matching and a Candidacy but no asserted Opening and no posting. Also ATS practice that treats requisition ≡ vacancy ≡ posting. The model must allow a 1:1 Requisition–Opening without requiring an Opening for every movement. Employment-by-appointment without a commercial offer must remain possible; do not make an effectuated WM-ECO-021 the only birth path for Employment.

**Identity/mastership.** Person is mastered only by WM-PER-001. Position by WM-ORG-004. Employment by WM-ORG-005. Asserted Opening by narrowed WM-ORG-008. Requisition and Candidacy are recruiting-ops masters and remain unnumbered. Campaign and stage definitions by WM-ACT-039. Interview session by WM-ACT-025. Assessment result by WM-ACT-034. Hire/need acts by the Decision/Approval Record draft. Offer by a WM-ECO-021 profile. Recruiting must not mint Person or Position.

**Requisition/position/opening.** Approved need is a Decision/Approval Record, not a requisition subtype. Standing requisition is durable demand authority and may have zero current openings or campaigns. Position is structural and occupancy-independent. Derived seat vacancy is a projection of Position occupancy (no current Assignment/Employment), distinct from requisition remaining-headcount. Asserted Opening is an explicit, dated fill-intent speech-act; it is not auto-created from derived vacancy and may precede incumbent exit. Posting is channel publication of an Opening, not the Opening. One Requisition may authorize N seats and many Openings. Prefer one Opening per distinguishable seat; quantity greater than one only when seats are interchangeable. Opening may reference Requisition and Position. It must not master Candidacy, matching or placement.

**Person/candidacy.** Candidacy is time- and purpose-bounded participation of exactly one Person in a hiring effort, linked to at least one of Requisition, Opening or Campaign. Application is an originating artifact on Candidacy, not a sibling root and not a Vacancy attribute. One Person has many Candidacies. At most one active Candidacy per (Person, Opening). Rehire reuses Person and creates a new Candidacy.

**Process/stages.** WM-ACT-039 owns the campaign/process and stage definitions. Stage occurrence is Candidacy × process instance × definition, with interval and outcome. Do not hang stages on Opening or Position. Campaign ≠ Requisition ≠ Opening. Skip, reject and hold are Decision events, not silent mutation.

**Interview/assessment/decision.** No InterviewAssessment root. Interview is a WM-ACT-025 Session bound to a stage occurrence. Assessment result is a WM-ACT-034 Evaluation about a Candidacy, produced from interview or another instrument. Recommendation ≠ assessment ≠ Decision ≠ Offer. Assessors and decision-makers are distinct roles.

**Offer/employment.** Profile WM-ECO-021; do not overwrite commercial-quote semantics. Carry compensation, contingencies, expiry, accept, decline, withdraw and supersede on the profile. Offer references Candidacy plus target Position/Opening. Withdrawal is a terminal state of the same object and destroys neither Person, Candidacy, Opening nor Requisition. Offer acceptance does not create Employment, Contract or Assignment. Employment requires a distinct establishment event. Contract and Assignment remain separate. Placement is Assignment plus Employment, not a Vacancy state.

**Privacy/retention.** CV possession is neither unlimited consent nor indefinite retention. Legal basis, purpose and schedule are distinct intervals. Candidacy close, withdrawal or fill starts the retention clock unless a recorded legal hold applies. Purge or minimize CV without erasing Person or Decision records. Assessment notes and recordings follow the same or a stricter schedule and attach to Candidacy, not to Person-as-dossier. Standing requisition does not grant an indefinite pipeline. Rehire does not resurrect a purged CV.

**Time/provenance.** Valid and transaction time on requisition, opening, candidacy state, stage occurrence, offer state and employment intervals. Provenance on who asserted the opening, assessed, decided and withdrew. Later Employment must not rewrite a prior employment interval of the same Person.

**Governance/fairness.** Version stage definitions and criteria. Bind assessments to declared criteria. Decisions must be attributable without retaining the CV. Fairness audit uses Decision and Assessment records, not retained biographies.

**Scenario.** Requisition R authorizes two seats of Position P. Derived vacancy is computed from occupancy. Asserted openings O1 and O2 (or one Opening with quantity two if seats are interchangeable) plus postings as artifacts. Campaign K from WM-ACT-039 owns stage definitions. Persons A, B, D yield candidacies C1–C3. Offer F1 to A is approved then withdrawn; C1 records the withdrawal; no Employment. B and D fill the seats. Later rehire of A: same Person, new Candidacy C4, new Offer F2, new Employment E2. Prior C1/F1 remain. No second Person.

**Invariants.**
1. Rehire must not create a second Person.
2. Each Candidacy references exactly one Person; a Person may have many Candidacies.
3. Approved need ≠ standing requisition ≠ Position ≠ derived seat vacancy ≠ asserted Opening ≠ Posting.
4. Standing requisition may have zero openings and zero campaigns.
5. WM-ORG-008 owns neither Candidacy nor matching nor placement/Employment.
6. Campaign owns stage definitions; Candidacy owns stage occurrences.
7. Interview ≠ assessment result ≠ recommendation ≠ Decision ≠ Offer.
8. Withdrawn offer persists and creates no Employment.
9. Offer acceptance does not create Employment, Contract or Assignment.
10. Matching is an evaluation/process result (Candidacy–Opening), not an Opening attribute.
11. Placement is Assignment plus Employment, not a Vacancy state.
12. CV possession grants neither unlimited consent nor retention beyond purpose and schedule.
13. Candidacy close or CV purge must not delete Person or Decision records.
14. Later Employment must not rewrite a prior employment interval of the same Person.
15. At most one active Candidacy per (Person, Opening).
16. Requisition authorized seats must not be exceeded by non-cancelled fills plus outstanding accepted offers unless a change event raises the cap.

**Minimum model set.** WM-PER-001 Person; WM-ORG-004 Position; WM-ORG-005 Employment; WM-ORG-008 narrowed to asserted Opening; unassigned Recruitment Requisition; unassigned Candidacy; WM-ACT-039 process; WM-ACT-025 interview profile; WM-ACT-034 assessment and matching-evaluation profile; Decision/Approval Record; WM-ECO-021 employment-offer profile. Posting and Application remain dependent artifacts, not allocated roots.

**Blockers.** WM-ORG-008 has no current specification and must be written as asserted Opening only—assertion/close/cancel, links to Requisition and Position, seat cardinality, explicit non-ownership of application/candidacy/matching/placement, distinction from derived vacancy and posting—without allocating an identifier in this review. Matching must be housed under WM-ACT-034/WM-ACT-039, not left homeless. WM-ACT-025 plus WM-ACT-034 profile rules are unwritten. Consent, purpose and legal-hold types may be absent from the named drafts. WM-ECO-021 employment-profile constraints (statutory terms, equity, withdrawal, effective date) are unwritten. Assignment mastership versus WM-ORG-005 is not settled here. Opening quantity versus seat-level remains an open modeling choice. Internal mobility must not be forced through an asserted Opening. No identifier is allocated.
