# Single frozen semantic audit — EM-OPS-02

You are the sole independent frozen auditor. No tools, browsing, standards claims, identifier invention, or registry mutation. This audit runs exactly once and will not be repeated.

Audit the reconciled EM-OPS-02 proposal and candidate artifacts below. The agreed identity decision is: Procurement Request and Sourcing Event require independent identity but remain registry-unassigned; Supplier Bid profiles WM-ECO-021; Bid Evaluation and Supplier Qualification are separate WM-ACT-034 profiles; Award Decision profiles WM-KNW-010; agreement and purchase order remain independent downstream records.

Find material internal contradictions, unenforceable invariants, missing fields, lifecycle/versioning defects, seal/opening/fairness gaps, and boundary leaks. Do not treat known registry or base publication gaps as artifact defects. Return:
1. Verdict: ACCEPT or REVISE.
2. Numbered material defects with exact evidence.
3. Required bounded fixes.
4. One JSON fenced array of additional fixtures, each with target, id, kind, input, expect and optional expectedCode. Fixtures must be directly usable and cover every material defect.
5. Explicit identifier decision.
6. Freeze decision stating that the audit is closed and must not be rerun.

Keep the response concise but complete.

## local-evidence.md
# EM-OPS-02 local synthesis

## Disposition

- Raise **Procurement Request** and **Sourcing Event** as genuine new-model candidates with identifiers unassigned. Each has identity and lifecycle absent from WM-ECO-019.
- Define **Supplier Bid** as a constrained profile of WM-ECO-021 Offer / Quote.
- Define **Bid Evaluation** and supporting **Supplier Qualification** as separate profiles of WM-ACT-034 Assessment / Evaluation with different subjects and validity.
- Define **Award Decision** as a profile of WM-KNW-010 Decision / Rationale.
- Reuse WM-ECO-006 for the concluded agreement and WM-ECO-019 for the buyer-issued purchase order. Winning, contracting and ordering remain separate events.

## Process and mastership

The chain is demand → sourcing procedure → supplier proposal → assessment → award decision → agreement/order. Procurement Request owns the internal need, scope, quantity, authority/budget references and approval lifecycle. Sourcing Event owns procedure kind, participant scope, requirement and criterion releases, submission window, sealing/opening, addenda, clarifications and bid admissibility.

Supplier Bid keeps the supplier-issued proposal identity and immutable submitted version; the buyer owns only receipt and procedure bindings. Bid Evaluation owns criterion outcomes, evidence, rationale, aggregation method, rounds and review. Award Decision owns the considered alternative set, selected bid, authority, reasons, exceptions, dissent and supersession. It references evaluation results without copying them.

## Fairness and change

Every criterion set has a version and effective time. A material post-publication change creates an addendum, a new version and equal notification to affected participants. Finalized rounds are append-only and never recomputed in place. Receipt time and opening time remain distinct; sealed content cannot be exposed before the witnessed opening event.

Evaluator conflicts are declared before determination, decided by another authorized party and recorded with recusal time. Affected outcomes remain in history and are explicitly excluded, replaced or bias-adjusted according to a declared method. Supplier qualification assesses the organization and its time-bounded standing; bid evaluation assesses a proposal version. Neither substitutes for the other.

Single-source procurement records a real one-alternative set, justification ground, competent authority, mandate scope, market/no-action comparison where required and any waiver. It never fabricates competition.

## Acceptance result

Three bids are evaluated under criteria v1. A criterion changes through an addendum, producing criteria v2 and a new evaluation round while the original round remains readable. One evaluator's declared interest is independently determined to require recusal; affected results are retained and a replacement round is issued. The award references all considered bids, criteria v2, the relied-upon round and the recusal. No history is deleted.

The selected bid does not create a contract or purchase order. Agreement conclusion, execution and effectiveness are evidenced in WM-ECO-006. A purchase order is separately issued and accepted under WM-ECO-019 semantics.

## Required invariants

1. Criteria and requirements are versioned; every outcome pins its governing release.
2. Bid identity belongs to the issuing supplier; the buyer records receipt and procedure context.
3. Evaluation and award are distinct attributable acts.
4. Supplier qualification and bid evaluation have different subjects and validity.
5. Procurement approval, award, signed agreement and purchase order are separate states.
6. Sealed receipt, opening and evaluation times are distinct.
7. Addenda and notifications are append-only and participant-equitable.
8. Recusals, exclusions, waivers and superseded rounds are never erased.
9. Single-source justification does not simulate competition.
10. Purchase-order issuance alone never proves contract formation.

## Holds

All reused models remain `publishableCanonical: false`; several rely on single-provider waivers. Relation ledgers do not yet ratify the proposed compositions. Conflict-of-interest and public-procurement semantics are acknowledged gaps. Procurement Request and Sourcing Event require registry allocation, source research, crosswalks and fixtures. No runtime identifier or installable release is created.

## claude-study.raw.md
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

## grok-study.raw.md
Verdict: Accept with conditions. The separations hold. ProcurementRequest and SourcingEvent need independent identity. SupplierBid profiles WM-ECO-021. BidEvaluation and SupplierQualification are distinct WM-ACT-034 profiles. AwardDecision profiles WM-KNW-010 and does not create WM-ECO-006 or WM-ECO-019. Conditions: retain versions, rounds, seals, openings, and recusal history so the award stays explainable, and reject any path from award to a signed agreement or order.

Strongest evidence. The required case — three sealed bids, a criterion change after publication, one conflicted evaluator — cannot be reconstructed from an offer payload, an assessment score, or a decision rationale alone. Explainability needs a request that authorized the procedure, an event that owns publication version, rounds, addenda, witnessed opening and procedure type, immutable bids, evaluations bound to one version, and a decision that cites that chain without executing it.

Strongest counterexample. Collapse SourcingEvent into WM-ECO-021 or WM-KNW-010. Round-1 publication, sealed hashes, the addendum, round 2, the opening witness, the conflict determination and the recusal then have nowhere to live that is independent of one supplier’s offer or of the final rationale. Re-scoring round-1 bids on the unpublished criteria makes the award unexplainable from retained versions. Collapse of AwardDecision into WM-ECO-006 falsely treats selection as signature.

Identity and mastership. ProcurementRequest needs independent identity: it is internal demand and authorization to source, not an offer, contract, order, assessment or decision. SourcingEvent needs independent identity: it is the multi-party, multi-round procedure container. Neither is covered by the given masters. SupplierBid does not need a new master; it is a constrained profile of WM-ECO-021, with immutability and seal as profile obligations. BidEvaluation and SupplierQualification do not need new masters; each is a separate WM-ACT-034 profile with its own scope. AwardDecision does not need a new master; it is a WM-KNW-010 profile that references the retained chain. Parties use WM-ORG-001; identifiers use WM-XCT-016. Conflict determination is retained separately from the award; it is an assessment finding, not the decision.

Boundaries. A request may exist, be rejected or withdrawn with no event. An event cites one authorizing request and owns rounds. A bid is one supplier’s offer in one round, not the event and not a score. Evaluation scores one opened bid against the criteria version of that round. Award selects among evaluated alternatives and records rationale. Qualification, determination, award, agreement and order remain distinct records.

Supplier qualification. Qualification is a WM-ACT-034 profile scoped to the supplier organization. It may gate invitation. It is not a bid score, not reused as BidEvaluation, and not implied by submission.

Criteria change. Requirements and criteria are versioned. A material change after publication creates an addendum and a new round. Prior submissions stay immutable and are not silently re-scored against the new version. Further scoring uses only the version published for that round.

Conflict and fairness. Conflicts are declared, independently determined, and retained with recusal history. The conflicted evaluator does not score the affected bid or any comparison that depends on it. Recusal remains even if the award later changes. Determination is not the award.

Single source. The event records a justified one-alternative procedure. It does not invent dummy bids or a simulated competitive round. The justification is retained on the event and cited by the award.

Downstream contract and order. Award does not create, sign, or imply WM-ECO-006 or WM-ECO-019. Agreement acceptance and order issuance are later, independent acts with their own identity. Winning is not execution.

Scenario. Request R authorizes competitive sourcing. Event E publishes criteria V1. Bids B1, B2 and B3 are submitted, hashed and sealed. Evaluator X declares a conflict involving B2’s supplier; an independent determination records the conflict and recusal; X scores neither B2 nor comparisons that depend on B2. A material criterion change issues an addendum, creates V2 and round 2. Round-1 bids are not re-scored on V2. Suppliers may submit round-2 responses. Opening of round 2 is witnessed before any evaluation read. Evaluations bind only to V2. AwardDecision cites R, E, V2, the opening witness, the opened round-2 bids, evaluations net of recusal, and the conflict record. No contract and no purchase order exist. A single-source variant uses the same event type with a one-alternative justification and no dummy bids.

Invariants.
1. ProcurementRequest identity is independent of any event, bid, award, contract or order.
2. SourcingEvent identity is independent of any single bid, evaluation or award.
3. A rejected or withdrawn request may exist with no event.
4. A submitted SupplierBid is immutable; correction is a new bid or a formal withdrawal, never an in-place edit.
5. Sealed bids are unreadable for evaluation until a witnessed opening is recorded against that round.
6. Evaluation binds only to the criteria version published for that round.
7. A material post-publication change creates an addendum and a new round; prior bids are not re-scored on the new version.
8. SupplierQualification is distinct from BidEvaluation and does not constitute a bid score.
9. Conflict determination is retained separately from AwardDecision, with recusal history.
10. A conflicted evaluator does not score the affected comparison.
11. Single-source is a justified one-alternative procedure, not simulated competition.
12. AwardDecision does not create, sign or imply WM-ECO-006 or WM-ECO-019.

Minimum model set. New ProcurementRequest; new SourcingEvent, with rounds, addenda, opening witness and procedure type as event structure, not extra masters; SupplierBid as a WM-ECO-021 profile; two WM-ACT-034 profiles (qualification, bid evaluation) plus a retained conflict-determination finding; AwardDecision as a WM-KNW-010 profile; parties via WM-ORG-001 and WM-XCT-016. Contract and purchase order stay outside this set except as non-created references.

Blockers. Refusing independent identity for the request or the event; allowing the award to instantiate a contract or order; scoring before witnessed opening; re-scoring old bids on new criteria without a new round; a conflicted evaluator scoring their own conflict; simulating competition for single source.

## candidate-allocation-offline-procurement-request/allocation-candidate.json
{"format":"vercy-model-allocation-candidate/v1","contourId":"EM-OPS-02","proposedName":"Procurement Request","modelId":null,"registryId":null,"allocationState":"unassigned","decision":"NEW MODEL","canonicalPublishable":false,"identityTest":{"stableIdentity":"An internal procurement need remains identifiable across approval, sourcing, award, contracting and ordering while its authorized scope evolves through revisions.","versionIdentity":"Changes to requested scope, quantity, delivery constraints, authority or funding references create immutable request versions; a materially distinct need creates a new request.","independentLifecycle":["draft","submitted","reviewed","approved","rejected","withdrawn","fulfilled","closed"],"mastership":"requesting organization procurement-demand authority"},"boundary":{"owns":["persistent procurement-request identity","internal need and business justification","requested scope, quantity and delivery constraints","requesting unit and accountable owner","authority and budget references","approval, rejection and withdrawal history","sourcing-event and downstream trace links","fulfilment and closure status"],"references":[{"target":"WM-ECO-019","purpose":"Downstream purchase-order master"},{"target":"WM-ECO-006","purpose":"Downstream commercial agreement master"},{"target":"WM-ORG-001","purpose":"Requesting organization identity"},{"target":"WM-ACT-034","purpose":"Qualification or evaluation assessment"},{"target":"WM-KNW-010","purpose":"Approval or award decision"}],"excludes":["sourcing procedure or participant scope","supplier bid or offer identity","supplier qualification or bid evaluation","award decision, agreement or purchase order","budget authority, commitment or accounting actual","supplier or organization identity"]},"objects":{"ProcurementRequest":{"identity":["procurementRequestId"],"required":["requestingOrganizationRef","need","scope","ownerRef","status"],"optional":["quantity","deliveryConstraints","authorityRef","budgetRef","successorRef"],"lifecycle":["draft","submitted","reviewed","approved","rejected","withdrawn","fulfilled","closed"]}},"invariants":["Every request identifies one requesting organization, accountable owner and internal need.","Approval authorizes sourcing activity only within the recorded scope and never creates an award, agreement or order.","Scope, quantity and delivery changes create traceable request revisions.","Budget reference never substitutes for budget authority, availability, commitment or actual.","A request never owns supplier bid, evaluation or qualification identity.","Sourcing, award, contract and order states remain independent.","Withdrawal preserves prior approvals, revisions and downstream trace links.","A fulfilled request may reference several agreements or orders without merging them.","A rejected request cannot silently enter a sourcing event.","Request closure never proves contract performance or delivery acceptance.","Single-source justification remains procedure evidence and never fabricates competing alternatives.","Historical request versions remain resolvable after fulfilment or closure."],"holds":["Registry allocation is pending and no identifier may be guessed.","Independent Grok review and one frozen semantic audit are pending.","Authority, budget and downstream relation contracts require canonical reconciliation.","Public-procurement and conflict-of-interest profiles remain adopter-specific."]}

## candidate-allocation-offline-procurement-request/profile-candidate.json
{"format":"vercy-enterprise-profile-candidate/v1","contourId":"EM-OPS-02","name":"Enterprise Sourcing, Evaluation and Award","decision":"PROFILE","newRuntimeId":false,"bases":["WM-ECO-021","WM-ACT-034","WM-KNW-010","WM-ECO-006","WM-ECO-019"],"constraints":["Supplier Bid profiles WM-ECO-021 and retains supplier-issued proposal identity and immutable submitted versions.","Bid Evaluation and Supplier Qualification are distinct WM-ACT-034 profiles with different subjects and validity.","Award Decision profiles WM-KNW-010 and references evaluation results without copying them.","Award, concluded agreement and purchase order remain separate acts and records.","Criteria changes create addenda and successor rounds with equal participant notification.","Conflicts, recusals, exclusions, waivers and superseded rounds remain append-only and explainable."]}

## candidate-allocation-offline-procurement-request/fixtures.json
{"format":"vercy-enterprise-allocation-fixtures/v1","candidateName":"Procurement Request","cases":[{"id":"approved-need","kind":"positive","input":"An internal need with scope, quantity, owner and budget reference is approved.","expect":"The request may initiate sourcing but creates no supplier, contract or order fact."},{"id":"split-fulfilment","kind":"positive","input":"One approved request is fulfilled through two independently issued orders.","expect":"The request retains one identity and references both orders without merging them."},{"id":"withdrawn-request","kind":"positive","input":"A request is withdrawn after review but before sourcing.","expect":"Its revisions and approval history remain resolvable."},{"id":"approval-is-award","kind":"negative","input":"Internal request approval is treated as supplier award.","expect":"The inference is rejected."},{"id":"budget-ref-is-funding","kind":"negative","input":"A budget reference is treated as committed and available funding.","expect":"The inference is rejected."},{"id":"request-is-order","kind":"negative","input":"The approved request is issued to a supplier as a purchase order.","expect":"The identity conversion is rejected."}]}

## candidate-allocation-offline-procurement-request/validation-policy.json
{"format":"vercy-allocation-validation/v1","requirements":{"modelIdMustBeNull":true,"registryIdMustBeNull":true,"allocationState":"unassigned","minimumInvariants":8,"minimumReferences":3,"minimumFixtures":3,"requiresPositiveAndNegativeFixtures":true,"requiresStableIdentityStatement":true,"requiresIndependentLifecycle":true}}

## candidate-allocation-offline-sourcing-event/allocation-candidate.json
{"format":"vercy-model-allocation-candidate/v1","contourId":"EM-OPS-02","proposedName":"Sourcing Event","modelId":null,"registryId":null,"allocationState":"unassigned","decision":"NEW MODEL","canonicalPublishable":false,"identityTest":{"stableIdentity":"A governed sourcing procedure remains identifiable across addenda, submission rounds, evaluations and award decisions while participants and criteria evolve through controlled releases.","versionIdentity":"Changes to procedure kind, requirements, criteria, window, participant scope or opening rules create immutable event releases and rounds rather than rewriting finalized history.","independentLifecycle":["planned","published","open","sealed","opened","evaluating","awarded","cancelled","closed"],"mastership":"buyer procurement procedure authority"},"boundary":{"owns":["persistent sourcing-event identity","procedure kind and participant scope","requirement and criteria release bindings","submission window and receipt rules","sealing and witnessed opening records","addenda, clarifications and equal notifications","bid admissibility and evaluation-round bindings","cancellation, award linkage and closure history"],"references":[{"target":"WM-ECO-021","purpose":"Supplier-issued bid or offer"},{"target":"WM-ACT-034","purpose":"Bid evaluation and supplier qualification"},{"target":"WM-KNW-010","purpose":"Award decision and rationale"},{"target":"WM-ECO-006","purpose":"Downstream agreement"},{"target":"WM-ECO-019","purpose":"Downstream purchase order"},{"target":"WM-ORG-001","purpose":"Buyer and supplier organization identity"}],"excludes":["internal procurement-request identity","supplier proposal content ownership","assessment or award-decision identity","agreement formation or execution","purchase-order issuance or acceptance","supplier organization or identity-register mastership"]},"objects":{"SourcingEvent":{"identity":["sourcingEventId"],"required":["buyerRef","procedureKind","authorityRef","status"],"optional":["requestRefs","successorRef","closedAt"],"lifecycle":["planned","published","open","sealed","opened","evaluating","awarded","cancelled","closed"]},"SourcingRound":{"identity":["sourcingEventId","roundId"],"required":["requirementsRef","criteriaSetRef","submissionWindow","contentDigest","status"],"optional":["participantScope","openingRule","addenda","clarifications","supersedesRound"],"lifecycle":["draft","published","open","sealed","opened","finalized","superseded"]}},"invariants":["Every sourcing event names one buyer authority and procedure kind.","Requirements and criteria are versioned and every outcome pins its governing releases.","Supplier bid identity and immutable submitted versions remain supplier-owned.","Receipt time, sealing time and opening time remain distinct.","Sealed content is not exposed before the authorized witnessed opening.","A material post-publication change creates an addendum, equal notification and a successor round.","Finalized rounds are append-only and never recomputed in place.","Supplier qualification and bid evaluation retain different subjects and validity.","Evaluation and award remain distinct attributable acts.","Conflicts are declared before determination and recusals remain in history.","Single-source sourcing records a real one-alternative set and justification without simulated competition.","Winning never creates an agreement or purchase order automatically."],"holds":["Registry allocation is pending and no identifier may be guessed.","Independent Grok review and one frozen semantic audit are pending.","Conflict-of-interest, sealing and public-procurement relation contracts require canonical reconciliation.","Package conversion and live verification are pending."]}

## candidate-allocation-offline-sourcing-event/fixtures.json
{"format":"vercy-enterprise-allocation-fixtures/v1","candidateName":"Sourcing Event","cases":[{"id":"criterion-addendum","kind":"positive","input":"Three bids arrive under criteria v1 and a material criterion change is published.","expect":"An addendum and criteria v2 create a successor round while the v1 round remains readable."},{"id":"conflicted-evaluator","kind":"positive","input":"An evaluator discloses an interest and is independently recused.","expect":"Affected results remain, exclusions are explicit and a replacement round is attributable."},{"id":"single-source","kind":"positive","input":"One supplier is considered under an authorized single-source ground.","expect":"A real one-alternative set, justification and waiver are recorded without simulated competition."},{"id":"open-before-witness","kind":"negative","input":"A sealed bid is exposed before the witnessed opening event.","expect":"The disclosure is rejected."},{"id":"rewrite-finalized-round","kind":"negative","input":"Criteria v1 outcomes are recomputed in place after criteria v2 publication.","expect":"The mutation is rejected."},{"id":"winner-is-contract","kind":"negative","input":"Selecting a winning bid automatically creates a signed contract and order.","expect":"Both transitions are rejected."}]}

## candidate-allocation-offline-sourcing-event/validation-policy.json
{"format":"vercy-allocation-validation/v1","requirements":{"modelIdMustBeNull":true,"registryIdMustBeNull":true,"allocationState":"unassigned","minimumInvariants":8,"minimumReferences":3,"minimumFixtures":3,"requiresPositiveAndNegativeFixtures":true,"requiresStableIdentityStatement":true,"requiresIndependentLifecycle":true}}
