# EM-LEG-01 local synthesis

## Disposition

- Create an **Enterprise contract, obligation and SLA profile** over WM-ECO-006 and WM-XCT-029.
- Do not create a catalogue/runtime identifier.
- Contract Amendment, Fulfilment Evidence and Service Level Agreement remain owned structures; none proves an independent lifecycle here.

## Ownership boundary

WM-ECO-006 masters the agreement instrument: identity, party positions, formation, execution, clause tree, authentic signed expressions, amendments, termination and contract-record governance. WM-XCT-029 masters each duty: modality, obligor/obligee, antecedent, due basis, fulfilment criteria, progress, evidence status, breach, cure and consequence obligations.

The contract derives obligation records from stable clause work identifiers. It never writes obligation state. The obligation references its source clause but never becomes a second store for normative clause text.

Per-obligation non-performance belongs to WM-XCT-029. Contract-level fundamental breach, avoidance, termination and remedy election belong to WM-ECO-006 and reference the underlying determinations.

## SLA/SLO rule

A contractual SLA is an executed clause set plus directed obligations with an obligee, enforceable performance criteria and contractual consequences. An operational SLO is a target sourced from internal policy or operational governance. It has no contractual force unless an executed agreement or amendment incorporates it.

Reserved candidate WM-SFT-016 may later own metric/SLO definitions, observations and error budgets. It must not own contractual obligees, enforceability, remedies or breach. EM-LEG-01 cannot depend on it while its boundary remains under review.

## Invariants

1. Party identity and authority evidence are pinned at execution time; later changes never overwrite history.
2. An amendment creates a new expression and preserves signed predecessors.
3. Amendment, novation and a new contract are distinct: term change, released party substitution and new agreement identity respectively.
4. Every obligation has an obligor, action/forbearance and fulfilment criterion.
5. Partial fulfilment accumulates and leaves an explicit outstanding quantity.
6. Evidence revocation appends a reopening transition; it never edits prior acceptance or fulfilment findings.
7. Contested performance is explicit, blocks disposition and cannot auto-resolve.
8. No target becomes a contractual guarantee without a source clause, obligee and enforcing party.

## Acceptance result

Expressions E1, E2 and E3 preserve the original agreement and two amendments. Changed clauses invalidate and rederive affected obligations without erasing prior versions. Partial performance remains measurable and incomplete. A disputed SLA observation stays provisional with its evidence and challenge history. The internal-SLO negative case is rejected because it lacks contractual incorporation and counterparty enforcement.

## Holds

Both parents remain `publishableCanonical: false`. SLA semantics rely on an under-grounded performance-standard finding; the WM-SFT-016 boundary is unresolved; relations and field-level crosswalks across obligation, breach/remedy, amendment and evidence remain unapproved. Jurisdiction-specific treatment of implied terms, service credits, set-off and penalties requires legal review. This checkpoint is not an installable release.
