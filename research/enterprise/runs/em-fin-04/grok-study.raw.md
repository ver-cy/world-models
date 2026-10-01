Verdict: Conditional accept of the allocation, not publication-ready. Independent roots are required only for Consolidation Scope and Consolidation Run, both identifier-unassigned. Consolidated Financial Statement is a profile of WM-ECO-018. Elimination Entry is a constrained profile of WM-ECO-016, not a new root. Source ledgers, organizations, control, holdings and accounting policy stay externally mastered. No other identifier is allocated.

Strongest evidence: The proposal separates the issued statement from the scope decision, the run, and the adjustments, and it refuses to derive membership from holdings. That is what lets two source ledgers, a later scope change, and an intercompany elimination coexist without a second chart, a second organization master, or a rewrite of the original knowledge-time result.

Strongest counterexample: An unrealized intercompany inventory profit on a sale between two ledgers, followed by a mid-period method change from full to equity, then a later restatement of control evidence. If scope is a statement attribute, or the run is not version-pinned, the post-change portion cannot be isolated and the original issue cannot be reproduced. A 60% holding with protective rights only, or de facto control below 50%, is wrongly included if membership is inferred from common owners.

Identity and mastership: Candidates that need independent roots are Consolidation Scope and Consolidation Run only. Financial Statement does not: the issued report is a specialization of the WM-ECO-018 statement master and must reference scope and run rather than absorb them. Elimination Entry does not: it is an adjustment class on WM-ECO-016, bound to one consolidation book and one run. External masters remain the source of ledger identity, organization identity, control assessments, equity holdings and policy. The consolidation model stores versioned references, not copies.

Statement, scope and run: The statement is the publication artifact. Scope is the governed membership and method decision. Run is the execution binding that consumes one scope version and emits one reproducible result. A statement may cite both; it is not their container. A scope change is a new scope version, not an edit of a statement.

Perimeter and control: Statutory and management perimeters are separate scope instances even when membership overlaps. Legal or accounting control is evidenced and dated; common ownership and equity percentage are inputs to that evidence, never inclusion rules. Automatic inclusion from common owners is rejected.

Ledgers and transformation: Source postings remain in their source ledgers. Consolidation transformations — mapping, currency translation, method application, cutoff — are run-scoped and pinned. They do not rewrite source journals. Each run names the source books, periods and cutoffs it consumed.

Elimination: An elimination is a consolidation adjustment, not a source posting. It exists only inside one consolidation book and one run, and it carries pair identity, match status, cutoff and authorization. Unmatched intercompany amounts are not silently cleared. The profile is acceptable only if WM-ECO-016 can carry a run-scoped adjustment discriminator without sharing source-journal identity. If it cannot, the profile fails; a further identifier is still not allocated.

Currency, time and knowledge: Event time of the sale is distinct from knowledge time of the elimination and of the statement issue. The run pins currency, rate version, policy, mapping, framework and taxonomy versions. A result at knowledge time T is recoverable only from pins known at T.

Restatement and publication: Original issue and restatement are distinct. Restatement is a new run, and if re-issued a new statement issue, that references the original run and does not overwrite it. Publication does not change ledger facts, scope history or elimination identity.

Governance and assurance: Scope membership, method, control evidence, cutoff and run authorization are explicit governed facts. Holdings, policy and organizations are cited, not re-decided inside the consolidation model. Assurance relies on immutability at knowledge time and on pair evidence, not on recomputation against later masters.

Scenario: Ledger A sells inventory to Ledger B. At knowledge time T1, statutory scope S1 includes both under full consolidation; run R1 pins books, period, rates, policy, mapping, control evidence and cutoff, and posts one elimination of the unrealized margin with pair evidence. At T2 a scope change moves B to equity from a mid-period effective date; run R2 pins S2 and eliminates only the post-change portion. At T3 control evidence is restated; run R3 references R1 and R2 and does not replace them. A common owner of an out-of-scope entity C creates no membership.

Invariants:
1. No entity enters a perimeter solely because a common owner or equity holding exists.
2. Inclusion requires explicit membership, perimeter type, method and control evidence valid at the run’s knowledge time.
3. Statutory and management perimeters are distinct scopes even if membership overlaps.
4. A run binds exactly one scope version.
5. A run pins source books, periods, cutoffs, mapping, policy, framework, taxonomy, currency and rate versions, transformations and authorization.
6. A run is immutable at its knowledge time; later change creates a new run.
7. Source postings are never mutated by consolidation.
8. Eliminations exist only in one consolidation book and one run.
9. Elimination requires pair and match evidence; unmatched amounts are not auto-cleared.
10. Event time, knowledge time and publication time are distinct.
11. Original issue and restatement are distinct; restatement references and does not overwrite.
12. Statement identity does not contain scope, run, transformation or ledger facts.
13. Holdings, organizations, control and policy remain externally mastered.
14. The statement known at T is reproducible from pins known at T.

Minimum model set: WM-ECO-018 profile for the consolidated statement issue; identifier-unassigned Consolidation Scope root; identifier-unassigned Consolidation Run root; WM-ECO-016 constrained profile for Elimination Entry; versioned external references for ledgers, organizations, control evidence, holdings, policy, mapping, framework, taxonomy, currency and rates.

Blockers: The elimination profile has no demonstrated adjustment discriminator, so source and consolidation identity may collapse. Scope does not yet pin control-evidence version, perimeter type and effective date as consumable facts. External references must be version-addressable or the run cannot reproduce. Restatement as a new run that cites the original, without a new identifier, is unspecified. Management and statutory perimeters must not share one membership list. Until those pins exist, the two-ledger, scope-change and intercompany-sale test cannot be assured.
