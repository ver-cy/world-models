# Verdict

**Reuse with two new candidates and three profiles.**

- **ProcurementRequest** — new, identifier-unassigned candidate. Requires independent identity and lifecycle. WM-ECO-019 explicitly excludes "Requisition, budget encumbrance and internal spend approval policy"; no frozen model owns internal demand.
- **SourcingEvent** — new, identifier-unassigned candidate. Requires independent identity and lifecycle. WM-ECO-021 lists "RFQ, Negotiation, Tender" masters as external and out of scope; nothing frozen owns a procedure with versioned requirements, a submission window, sealing and opening.
- **SupplierBid** — **profile** of WM-ECO-021 (Offer/Quote), plus a submission-envelope component owned by SourcingEvent. No new identity.
- **BidEvaluation** — **profile** of WM-ACT-034 (Assessment/Evaluation), subject = a named bid version. No new identity.
- **AwardDecision** — **profile** of WM-KNW-010 (Decision/Rationale). No new identity.

# Evidence

WM-ECO-021 is an aggregate owning a versioned pre-contract proposal with issuer/recipient roles, lines, prices, validity window, immutable issued versions and attributable response events — exactly a bid, minus procurement procedure. WM-ACT-034 already carries version-pinned criteria binding with retained snapshot, declared method, evidence-to-criterion linkage, criterion outcomes with rationale, append-only serially numbered evaluation rounds, aggregation, independent review, and an explicit boundary that it "ends at the recorded conclusion". WM-KNW-010 carries decision question, alternative set, selection, disposition, outcome statement, divergence explanation, authority and mandate binding, status lifecycle, appeal and supersession. WM-ECO-019 owns the buyer-issued order; WM-ECO-006 owns the agreement record, formation and execution.

# Identity/mastership

Apply each base's stated identity priority: authoritative master-system identifier, then governed global identifier, then Dimension-assigned UUID/ULID; never a date, score, name or file path. ProcurementRequest masters in the requesting Dimension's ERP/BPM; SourcingEvent in the sourcing system; the bid's identity is the **supplier's** issued proposal identity (WM-ECO-021 issuer namespace) with a buyer-side receipt binding, never re-minted by the buyer; BidEvaluation and AwardDecision master in the evaluation and decision registers respectively. Supplier party identity resolves to WM-ORG-001; scheme-qualified supplier identifiers anchor through the WM-XCT-016 register pattern. No identifiers are allocated here.

# Process boundary

Five separable records, each with its own finalisation: demand (request) → procedure (sourcing event) → proposal (bid) → determination (evaluation) → decision (award) → commitment (contract and/or order). Approval of procurement is not an award; award is not a contract; contract is not an order. WM-KNW-010's own policy places approval execution, publication and enforcement outside the decision record.

# Request and sourcing event

ProcurementRequest owns: need statement, requested scope and quantity, budget/authority reference, requested-by and effective dates, and its own approval state. SourcingEvent owns: procedure kind (open, restricted, negotiated, single-source), **versioned requirement and criteria set** with effective-from, invited or eligible participant set, submission window, seal state, opening event, addenda, clarification register, and disposition of late or non-compliant submissions. An addendum that changes requirements or criteria mints a new criteria version and must be notified to all participants; a clarification that does not change requirements is recorded without a version bump.

# Bid and evaluation

The SupplierBid profile restricts WM-ECO-021 to a sourcing-event-scoped submission: mandatory sourcing-event and criteria-version reference, immutability of the submitted version, and receipt time recorded separately from opening time. Sealing and opening are **not** in WM-ECO-021 and are owned by SourcingEvent as submission state (sealed → opened, with witnessing authority). WM-ACT-034's embargo access exception supports pre-opening confidentiality but does not supply opening semantics.

BidEvaluation binds criteria at version with a retained snapshot, separates mandatory pass/fail screening from compensatory scoring, records per-criterion outcomes with rationale and cited evidence, permits indeterminate outcomes without coercion to a negative, and computes a composite only under a declared aggregation model. Rounds are append-only; recomputation after finalisation is prohibited.

# Award and downstream commerce

AwardDecision states the decision question, the considered bid set (each bid referenced, not restated), the evaluation round and criteria version relied upon, the selected bid, the disposition, the factors balanced and any divergence from the ranking. **Seam rule:** where a BidEvaluation record exists, the AwardDecision must not restate criterion outcomes; WM-KNW-010's evaluation-results area is used only to reference the round and the aggregation actually relied upon.

**Negative case rejected.** Winning does not create a signed contract. Three independent states must be separately evidenced: award recorded; agreement concluded, executed and effective (WM-ECO-006 conclusion, signature evidence, conditions precedent); order issued and accepted (WM-ECO-019, where an order is an offer and "systems must not report a contract as formed on issuance alone"). WM-ECO-021 independently rejects inferring formation from a label, acknowledgement or status, and WM-ECO-019 records that a quotation may not even be an offer capable of acceptance. Framework awards produce a WM-ECO-006 agreement whose call-offs are later WM-ECO-019 release orders against a residual balance.

# Supplier qualification

A second, separate WM-ACT-034 instance whose **subject is the supplier organization**, not a bid: competence, financial, compliance and accreditation criteria, its own validity window, surveillance obligation and re-assessment trigger. Qualification is a precondition or screening input to bid admissibility; it is never scored inside bid evaluation, and a bid score never revises qualification standing. Registration in a supplier register does not prove qualification — WM-XCT-016 states that successful lookup alone proves neither eligibility nor authorization.

# Conflict and fairness

Required: evaluator roster with declared role, mandate reference, declared interests, determination of each declared interest by a party other than the declarant, recusal with an effective instant, and restated participation figures. WM-KNW-010 supplies the interest/recusal and quorum-attestation functions. WM-ACT-034 supplies impartiality declarations and the separation of determination from decision, but its adjudication records **no function that assigns assessors or captures impartiality before determination begins** — the BidEvaluation profile must add that as a required extension. Affected criterion outcomes are marked, never deleted: WM-ACT-034 already provides contested, provisional and bias-adjusted result markers.

# Single source

Recorded as an exception, not as fabricated competition. Permit an alternative set of size one — WM-KNW-010's adversarial check explicitly admits this for mandatory determinations — with: justification ground, deciding authority and mandate scope covering the value and category, a market-test or no-action baseline where the bound profile requires one, and the stated consequences. Other exceptions (late bid admitted, criterion waived, sole compliant bid) follow the waiver pattern: waiving role, rule waived, reason, all retained.

# Time/version/scenario

RFC 3339 with seconds and explicit offset throughout. Distinguish request, publication, submission deadline, receipt, opening, criteria effective-from, determination, finalisation, award, contract effective and order issue instants; keep event, observation and ingestion times separate. Criteria and bids are versioned; bid validity windows can lapse before award.

# Acceptance scenario

Three bids. Round 1 finalised under criteria v1. A criterion changes: an addendum mints criteria v2; round 2 is opened and scored under v2 with the v2 snapshot retained; round 1 stays readable and is not recomputed. Evaluator B declares an interest in bid 2; a different party determines it disqualifying; B is recused with an effective instant; B's round-2 outcomes are marked and either excluded with re-scoring in round 3 or retained as bias-adjusted; participation figures are restated. AwardDecision names criteria v2, the round relied on, all three bids, the recusal, and any divergence from the ranking. Nothing is deleted; the choice remains re-derivable from retained values.

# Invariants

1. Criteria carry a version; every outcome cites the version it was scored under.
2. A decision references every bid considered and the evaluation round relied upon.
3. Procurement approval is not an award; award is not a signed contract; contract is not an order.
4. Bid identity belongs to its issuer; buyers hold receipts, not re-minted identities.
5. Supplier qualification and bid evaluation are separate assessments with different subjects and validity.
6. Determination and decision must be attributable to distinguishable actors.
7. Sealed bids have a recorded opening event; receipt time is distinct from opening time.
8. Requirement changes after publication require an addendum notified to all participants.
9. Recusals, exclusions and superseded rounds are retained, never deleted.
10. A single-source award requires a justification ground and a competent authority; competition is never simulated.

# Minimal model set

Two identifier-unassigned candidates (Procurement Request, Sourcing Event); three profiles (WM-ECO-021 bid, WM-ACT-034 twice — qualification and bid evaluation, WM-KNW-010 award); downstream reuse of WM-ECO-006 and WM-ECO-019; party and identity via WM-ORG-001 and WM-XCT-016.

# Holds

All six frozen bases are reviewable drafts with `publishableCanonical: false`. WM-ECO-021 and WM-XCT-016 are single-provider (Claude and Grok waived); WM-KNW-010 and WM-ACT-034 are single-provider (Grok waived). The queue's WM-ECO-019 link is `conceptual-candidate` at `index-and-publication-metadata` depth — no semantic crosswalk is verified. WM-ACT-034's relation ledger is empty and WM-KNW-010's registers only two relations, so every composition above is a proposal, not a ratified contract. Public-procurement profiles are a declared deferred gap in WM-ECO-021 and WM-KNW-010; conflict-of-interest structure is a declared gap in both WM-KNW-010 and WM-ACT-034. No registry allocation, fixture check, immutable reference, comparison-track validation, canonical completeness or installability is claimed.
