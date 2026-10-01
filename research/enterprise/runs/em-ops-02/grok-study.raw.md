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
