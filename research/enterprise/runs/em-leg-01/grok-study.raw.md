**Verdict.** PROFILE over WM-ECO-006 and WM-XCT-029. No new catalogue or runtime ID. ContractAmendment, FulfilmentEvidence and ServiceLevelAgreement stay child records or profiles of those two models. Reserved WM-SFT-016 is not promoted into this card. This is standards alignment, not legal advice and not a jurisdiction conclusion.

**Ownership boundary.** WM-ECO-006 owns agreement identity, party positions, formation, executed clause text, signed expressions, amendments, termination and contract-record governance. An amendment is a new executed instrument of the same agreement work: it produces a successor expression and never overwrites a prior signed expression. A conformed text is a derived projection with its own identifier. Rescission-and-replacement or a substitute bargain is a new 006 instance with a successor link, not an amendment.

WM-XCT-029 owns one duty: modality, obligor/obligee/enforcer, conditions, due basis, fulfilment criteria and progress, outstanding quantity, evidence status, breach, cure, excuse, waiver and per-duty consequences. Obligation identity survives amendment and is distinct from the creating instrument and from each dated occurrence.

The contract derives obligation records from stable clause work identifiers. The contract never stores obligation state. An obligation cites work-id plus expression-id and never restates normative clause text. Per-duty non-performance belongs to 029. Contract-level avoidance, termination and remedy election belong to 006.

No independent aggregates:
- ContractAmendment: child instrument of 006.
- FulfilmentEvidence: child event of 029 plus the existing WM-XCT-028 mixin for item identity, digest, custody, contest and withdrawal. Payload stays with the document or observation owner.
- SLA: executed clause set on 006 plus duties with an obligee, enforceable criteria and consequences on 029.

**SLA/SLO split.** A contractual SLA is an executed clause set plus 029 duties. An internal SLO or OLA has no contractual force unless incorporated by an executed contract or amendment. A dashboard metric is not a commitment. EM-TEC-06 already states that SLA and SLO have different grounds; that split is kept. WM-SFT-016 remains reserved, unversioned and not installed. If later written, it may own SLI specification, target, window, observations and error budgets only — never contractual obligees, enforceability, remedies or breach.

ISO/IEC 19086 supplies metric-model alignment for how a measurement is specified; it does not move obligees or remedies into a software-reliability model.

**Required constraints.**
- Every executed expression is immutable (digest, signature package, validation report). Later change is a new instrument.
- Clause work identifiers persist across amendments; expression locators pin text inside one signed expression. Renumbering redirects; it does not mutate history.
- 006 `obligations-and-performance` must stop holding live duty state, quantities, evidence status or per-duty dispute.
- 029 “statement of obligated action” is constrained to locator plus controlled-term encoding of duty content. Predecessor field `obligation_text` is not promoted.
- Execution occupancy on 006 is frozen as of signature. Current obligor is a 029 role binding that references the contract position plus current occupant.
- Delegation / third-party performance does not change 006 party-position occupancy and does not discharge the original obligor. Transfer, novation and new agreement must be typed before occupancy changes.
- Acceptance and evidence revocation are events on 029. They never amend signed clause text.
- Dual timestamps: legal-effect time versus observation time. Transition log is append-only.
- Service credits are typed 029 consequences with an open class slot {remedy | liquidated-damages | penalty | price-adjustment | other}. The slot is filled by a governing-regime profile, not by this card. Exclusive-remedy election, if any, lives on 006.
- Dispute on a duty stays on 029. Forum, claim file and decision remain EM-LEG-05 / neighbouring case models.

**Corrected invariants.**
1. Party occupancy at execution is frozen on 006; current obligor is a 029 binding.
2. An amendment is a new executed instrument of the same agreement; it never overwrites a prior signed expression.
3. A duty has obligor, obligee, subject and fulfilment criterion; it cites clause work-id plus expression-id and does not restate signed text.
4. Obligation state, outstanding quantity, evidence status and per-duty dispute never live on the contract expression.
5. Internal SLO, OLA or dashboard metric is not a contractual guarantee without incorporation.
6. Evidence revocation after acceptance appends a status event and may reopen the duty; prior acceptance remains in the log.
7. Delegation does not change party-position occupancy; transfer, novation or new agreement must be typed first.
8. Service-credit class is a regime-profile parameter, not a model-level legal conclusion.

**Scenario results.**

1. *Internal dashboard SLO presented as a contractual guarantee without incorporation.* Fail the negative case. No 006 incorporation, no 029 contractual duty, no obligee, no enforceable criterion, no consequence. The observation may exist as an SLO/SLI record under EM-TEC-06 later; it has no contractual force.

2. *Contract with two amendments, partial performance and a disputed SLA measurement.* Preserve the original expression plus two amendment instruments and two successor expressions. Obligation records persist via work-id. Partial quantities, measurement-dispute flag and provisional state sit on 029. Observations are cited, not copied. Contract-level remedy election appears on 006 only if an election is recorded. Signed text, execution-time parties, clause locators, outstanding quantities, evidence history and dispute state are all preserved.

3. *Party substituted.* Classify first. Delegation: agreement identity and execution parties unchanged; performer may be distinct; original obligor remains bound. Transfer of obligations / assignment of contract with consent: agreement continues; execution snapshot frozen; current occupant updates; discharge of the original is an explicit indicator, otherwise residual liability remains. Novation or new agreement: new 006 instance, new execution snapshot; old contract closed except surviving duties the new instrument states. Wrong class is an invariant failure.

4. *Fulfilment evidence revoked after acceptance.* Keep the evidence-item identity. Append revoked / insufficient / superseded with authorising role, reason and effective instant. 029 reopens the duty without erasing the prior acceptance event. Outstanding quantity is recomputed from the surviving accepted set. A replacement certificate is a new item bound to the same duty. Dispute remains until resolved. No mutation of 006 expressions.

5. *Service credits.* Record them as 029 secondary obligations triggered by a typed consequence. Whether a given regime treats the credit as a remedy, liquidated damages, an unenforceable penalty or a price-adjustment mechanism is a profile parameter requiring subject-matter verification of applicability. This card does not decide enforceability. 006 records only a contract-level exclusive-remedy or election clause if one was executed. SFT-016 never owns credits.

**Publication blockers.**
- 006/029 overlap is not yet written as enforceable PROFILE constraints.
- Semantic crosswalk, rights and source mastership remain open in brief.json.
- Delegation / third-party-performance type is missing on 006 change events.
- Writing-rule hold on 006 (CISG Art. 11 / 12–96 reservations versus UCC §2-201 / §2-209) stays co-recorded; it must not be collapsed.
- No fixtures for tests 1–5, especially two-amendment plus disputed measurement, and acceptance then revocation then reopen with preserved log and recomputed quantity.
- Reserved-acceptance versus unconditional discharge is untested.
- WM-SFT-016 is a stub; EM-TEC-06 must keep SLA/SLO grounds split. Do not invent a SFT-016 runtime version.
- Alignments to UBL, FIBO, ODRL, LegalRuleML and ISO/IEC 19086 are alignments only, not conformance claims.
- Primary legal sources of a chosen jurisdiction still require subject-matter verification before any regime profile is published.
