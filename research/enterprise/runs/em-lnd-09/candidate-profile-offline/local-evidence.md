# EM-LND-09 local synthesis

## Disposition

- Define Contract Landscape as a governed read-only profile over WM-ECO-006 agreements and WM-XCT-029 obligations.
- Define Obligation Network as the dependency/deadline graph rendering of the same profile, not another aggregate.
- Served output is immutable and digest-identified. Neither candidate has independent business identity; allocate no runtime/model identifier.

## Identity and mastership

WM-ECO-006 masters agreement work/expression identity, party positions, formation, clauses, amendments, assignment/novation, termination, survival and evidence governance. WM-XCT-029 masters each obligation, occurrence, parties, action, antecedent, due basis, recurrence, lifecycle, fulfilment, non-performance, excuse and consequence.

Obligations cite stable clause work identifiers and expression versions; the contract never owns obligation state, and the obligation never duplicates normative clause text. Amendments preserve historic expressions and re-derive only affected duties.

## Parties, versions and scope

Execution-time party positions and verification evidence remain immutable. Later organization changes, succession and contractual assignment/novation are separate histories. Delegation preserves obligation identity; release-and-substitute novation creates a successor obligation.

The profile covers agreement perimeter, derived obligations, dependency/precedence edges, deadline inputs, fulfilment evidence, dispute/non-performance facets and as-of/access parameters. It does not author clauses, validate signatures or decide legal precedence.

## Dependencies, survival and deadlines

Typed dependency edges distinguish antecedent/detachment, reciprocal order-of-performance and parent-child decomposition. Every edge names the dependent obligation and supporting evidence. Cycles and unresolved dependencies are reported and never silently ordered.

Contract term and obligation term are separate. Termination/expiry can release primary duties while confidentiality, evidence retention, dispute and wind-down duties survive. A due schedule preserves due basis, recurrence version, trigger instant, time zone and business-day convention; legally relevant local civil time is retained alongside derived instants.

Fulfilment evidence binds to a specific occurrence and discharged quantity. Elapsed time never proves discharge. Evidence revocation appends reopening rather than editing history.

## Dispute, non-performance and conflict

Overdue, declared non-performance, excused and disputed are independent facets. Dispute does not imply lateness, and overdue does not imply an authorized breach determination. Cure/additional-period state can suspend remedies without discharging the duty.

Within an agreement, declared document precedence is displayed. Across agreements, contradictory duties, deadlines, exclusivity or governing-law declarations create an attributed conflict record containing each agreement's own precedence assertions and no computed winner. The landscape surfaces questions to a responsible legal reviewer.

## Time, access and acceptance

World/event time, observation/ingestion time, knowledge/as-of and reporting period remain distinct. Historical views reconstruct what was known at the requested horizon. Non-party access is deny-by-default and uses WM-XCT-002 authorization plus WM-XCT-003 least-disclosure projection.

When Agreement A expires, primary delivery duties can be released while confidentiality and evidence-retention obligations remain active under their own survival clocks. Their source clauses and evidence stay resolvable. A later confidentiality breach can be recorded against the surviving duty; agreement expiry never deletes it.

## Invariants

1. Contract term is not the term of each obligation.
2. Execution-time party positions are never overwritten.
3. Agreement work persists across amendments; expressions remain citable.
4. Obligations cite source clauses without duplicating their authority.
5. Delegation and novation have different identity effects.
6. Due basis and trigger are explicit and reproducible.
7. Fulfilment requires evidence or an explicit discharge mode.
8. Dependency edges name their counterpart obligations.
9. Dependency cycles remain visible.
10. Overdue, non-performance, excuse and dispute remain separate.
11. Conflicts carry attributed assertions and no automatic winner.
12. Surviving duties and evidence remain after contract expiry.
13. Views are immutable, digest-identified and non-reimportable.

## Minimal profile shape

The profile records scope/version, agreement perimeter, clause/expression and derivation pins, world/knowledge as-of, dependency graph with cycles/gaps, deadline inputs, survival register, independent lifecycle/overdue/excused/disputed/cure facets, evidence pointers and revocation, conflict/precedence assertions, disclosure projection, input revisions and output digest.

## Holds

Both targets remain non-canonical reviewable drafts with boundary and source-verification gaps. Their composition is not ratified in the relationship ledger. Reciprocal withholding, insolvency effects, obligations-register operations and some statutory-source boundaries remain unresolved. No verified semantic crosswalk or fixtures exist. This checkpoint is not legal advice and makes no canonical completeness, installability or publication claim.
