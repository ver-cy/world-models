# Independent review request: EM-LEG-01 Contract, obligation and SLA

Review this Enterprise boundary independently. Use public contract, obligation and service-level practice where useful, but separate standards alignment from legal advice and jurisdiction-specific conclusions. Do not invent a Vercy model/runtime identifier.

Current candidates:

- WM-ECO-006 Commercial Contract owns agreement identity, party positions, formation, executed clause text, signed expressions, amendments, termination and contract-record governance.
- WM-XCT-029 Obligation / Commitment owns one duty's modality, parties, conditions, due basis, fulfilment criteria/progress, evidence status, breach, cure and consequences.
- WM-SFT-016 Service Level / SLO is reserved but remains a candidate under boundary review.

Proposed decision: **PROFILE** over WM-ECO-006 and WM-XCT-029, no new ID. A contract derives obligation records from stable clause work identifiers. The contract never stores obligation state; an obligation never restates normative clause text. Per-duty non-performance belongs to WM-XCT-029; contract-level avoidance, termination and remedy election belong to WM-ECO-006.

A contractual SLA is an executed clause set plus obligations with an obligee, enforceable criteria and consequences. An internal SLO has no contractual force unless incorporated by an executed contract or amendment. WM-SFT-016 may later own metric definitions, observations and error budgets, but never contractual obligees, enforceability, remedies or breach.

Test:

1. An internal dashboard SLO is presented as a contractual guarantee without incorporation.
2. A contract has two amendments, partial performance and a disputed SLA measurement.
3. A party is substituted: distinguish delegation, novation and a new agreement.
4. Fulfilment evidence is later revoked after acceptance.
5. Service credits may be remedies, liquidated damages or penalties depending on the governing regime.

Check preservation of signed text, party identity at execution, stable clause locators, outstanding quantities, evidence/reopening history and dispute state. Decide whether Contract Amendment, Fulfilment Evidence or SLA needs an independent aggregate.

Return at most 1000 words with: Verdict; ownership boundary; SLA/SLO split; required constraints; corrected invariants; scenario results; publication blockers.
