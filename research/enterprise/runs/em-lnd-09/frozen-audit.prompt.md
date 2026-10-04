# Frozen no-tools semantic audit — EM-LND-09

You are the final static semantic auditor. Use only this frozen packet. Do not browse, call tools, invent identifiers, give legal advice or grant publication authority.

The result is a PROFILE over WM-ECO-006 Commercial Contract, WM-XCT-029 Obligation/Commitment and WM-REC-001 record context. No new runtime/model identifier is proposed.

Reconciled boundary:
1. Contract Landscape is a governed read-only profile; Obligation Network is the same immutable projection rendered as a graph. Neither has business identity, lifecycle or write path.
2. WM-ECO-006 masters agreement works/expressions, clauses, amendments and party positions. WM-XCT-029 masters obligations, occurrences, lifecycle, deadlines, fulfilment, non-performance and dependency associations. WM-REC-001 or the applicable record authority masters evidence; obligations hold governed references.
3. Agreement and duty lifecycles are separate. Expiry never expires every duty. A surviving-duty binding to an expired agreement is a historical source reference only and is never deleted or treated as proof that the agreement remains live.
4. Dependency edges are typed WM-XCT-029 associations: antecedent, reciprocal performance or decomposition. Structured cycles are preserved. Reciprocal cycles may be valid; decomposition cycles are surfaced for WM-ACT-034 assessment and never silently removed or linearized.
5. Overdue, non-performance, excuse, dispute and cure are orthogonal facets. Due assessment uses duty/occurrence deadlines, never agreement expiry as substitute.
6. Cross-agreement conflicts preserve competing attributed precedence assertions and never compute a legal winner.
7. Evidence cited by a surviving duty remains addressable under its record authority; expiry does not orphan, purge or disclose it.
8. The projection digest binds exact agreement/expression revisions, obligation revisions, as-of, party lens, policy/access decision, disclosure shape and graph-engine revision. Missing pins fail closed.
9. Non-party access is deny-by-default. Governed projections may hide nodes, edges, positions or evidence but never fabricate them. Survival never broadens access.
10. Optional agreement grouping nodes are identity-less rendering constructs and cannot become portfolio, agreement or commercial masters.

Scenario: Agreement A expires at t_exp. Confidentiality duty C and evidence-retention duty R survive. R references evidence E mastered by the record authority. At t_after an authorized party lens shows A expired, C/R in force, typed dependencies and E references; E content remains shape-controlled. A non-party is denied. No duty, edge or record is deleted or remastered.

Audit questions:
- Is there a hidden aggregate or identifier despite `newRuntimeId=false`?
- Are agreement, duty, edge, record, profile and projection mastership unambiguous?
- Is the projection key deterministic and access-safe?
- Does survival preserve duties and evidence without reviving the agreement?
- Identify any contradiction that makes even a held profile unsafe.

Return at most 500 words with exactly: Verdict (`ACCEPT WITH LIMITS`, `REVISE`, or `REJECT`); Critical findings; Required holds; Scenario result; Identifier decision. Treat base-model publication blockers as holds unless they contradict the profile.
