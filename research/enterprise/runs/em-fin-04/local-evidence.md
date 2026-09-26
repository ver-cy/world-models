# EM-FIN-04 local synthesis

## Disposition

- Reuse WM-ECO-018 as Financial Statement under a consolidated-statement profile.
- Propose identifier-unassigned **Consolidation Scope** and **Consolidation Run** roots because both have lifecycles independent of a statement issue.
- Profile Elimination Entry on WM-ECO-016 and constrain it to a consolidation book and one run, with mandatory pair and residual evidence.
- Reuse accounts, journals, positions, organizations, control relationships, holdings and policy/rule masters.
- Allocate no catalogue or runtime identifier.

## Identity and mastership

Consolidation Scope persists across periods, runs, statements, management reports and disclosures. Its lifecycle follows control and perimeter changes. Consolidation Run is an immutable execution that pins scope, method, ledgers, mappings, rates and cutoff and remains reproducible after the statement that cites it changes.

WM-ECO-018 already owns report and issue identity. Elimination Entry remains a balanced WM-ECO-016 posting document with additional consolidation constraints. Source ledgers, accounts, positions, organizations, holdings and control assertions retain their own mastership.

## Statement, scope and run

Statement issue, perimeter, transformation, run, elimination and source ledger are distinct. WM-ECO-018 binds and presents consolidation outputs but does not execute consolidation or own its transformations.

The existing WM-ECO-018 service role claiming ownership of perimeter, eliminations and transformations conflicts with its out-of-scope declaration and must be narrowed to binding and citation.

## Perimeter and control

Every scope version is purpose-qualified: statutory reporting, management, ownership/control and statistical perimeters may differ and are never silently shared.

Membership declares consolidation approach, control basis, governing instrument, evidence, claimant capacity, valid time and knowledge time. Economic ownership, voting power, control and consolidation treatment remain separate assertions. Common owners alone create no membership because they establish neither control basis nor reporting authority.

Management perimeter may follow operational responsibility while statutory perimeter follows an accounting control test. One entity may validly appear in only one of them.

## Source ledgers and transformation

Source postings remain immutable in their own books. Each run enumerates contributing books and revisions, pinned trial-balance or position sets, group-account mapping, currency translation, reclassification and alignment rules.

Transformation steps record inputs, outputs and rule versions. Consolidation adjustments live only in consolidation books and never rewrite source entries.

## Elimination entry

An Elimination Entry balances within one consolidation book, currency and tolerance. It records class, both counterparty legs, book/entry/line references, matching key, matched and unmatched amounts, residual reason and authorization.

An unmatched leg becomes a visible break and never a silent one-sided posting. Intercompany revenue/cost, receivable/payable, investment/equity, unrealized profit and dividend eliminations remain distinguished.

## Currency, time and knowledge

Transaction, functional and presentation currencies remain explicit. Rate, rate type, rate date, source and rate-set version are pinned.

Reporting period, cutoff, posting, event, run, issue, filing, ingestion and knowledge times remain distinct. Reproduction at prior knowledge time resolves the run, scope, rates, mappings and ledger revisions valid at that knowledge cut rather than current configuration.

## Restatement and publication

Completed runs and issued statements are immutable. Corrections create successor runs and successor statement versions with restatement class, reason and lineage. Original and recalculated editions remain resolvable.

Approval, assurance, issue, filing and publication are independent states. None validates a figure by itself, and publication never erases a prior or recalculated edition.

## Governance and assurance

Run execution, elimination posting, scope change, post-cutoff adjustment, issue and restatement require authority. Initiator and authorizer are separated or a compensating control is recorded.

Assurance engagements remain external and pin exact run and statement versions. Method, accounting framework, taxonomy, disclosure and recalculation policies are pinned WM-KNW-012 revisions.

## Acceptance result

Group P consolidates subsidiary S from statutory EUR book L-STAT and management USD book L-MGMT. Run R1 pins scope v2, rate set FX-2026Q2, mapping M1 and cutoff T1. Elimination E1 removes a 100,000 intercompany sale and 70,000 cost, cites both legs and matching key IC-8841, and explains a 120 FX residual. Statement A1 cites R1. Scope v3 later removes a disposed subsidiary; R2 and a recalculated comparative retain a bridge for scope, method, rate and activity changes. A late adjustment enters R2 and never backdates R1. A1 remains reproducible at its original knowledge time.

## Required invariants

1. Statement, scope, run, elimination, posting and position have distinct identifiers.
2. Every statement pins scope, method/framework, taxonomy, rate set, run and ledger revisions.
3. Inclusion requires control basis, authority, evidence and interval.
4. Common ownership alone never establishes inclusion.
5. Management and statutory perimeters remain parallel and non-substitutable.
6. Eliminations post only to consolidation books.
7. Every elimination cites paired evidence and explains residuals.
8. Entries balance within one book, currency, scope and tolerance.
9. Ownership assertions state right type, class, denominator and time.
10. Event, cutoff, run, issue and knowledge times remain distinct.
11. Runs are immutable and corrected by successors.
12. Restatements append versions and preserve originals.
13. Post-cutoff adjustments are dated and authorized.
14. Scope changes produce comparability bridges.

## Holds

Consolidation Scope and Consolidation Run have no registry allocations. Chart of Accounts/Mapping, FX Rate Set, Intercompany Match and Trial Balance also lack allocated masters. WM-ECO-018 contradicts its own out-of-scope boundary, and WM-ECO-018/017 composition direction conflicts with the referenced-master boundary. WM-ORG-012 parentage and WM-ECO-038 extension semantics remain unsettled. Relations, source pins and fixtures are absent or unapproved, and bases remain non-canonical drafts. No installability or publication-readiness claim is made.
