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
