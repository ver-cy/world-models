**Verdict.** Accept-with-conditions. Keep 015 for bank/custody; 016 for journal entries and posting lines; 017 for per-ledger balances with 015 position kept distinct; external payment/invoice/event as correlation only; per-ledger balancing; siblings that never offset; append-only correction; explicit hard-close exceptions; identifier-unassigned Chart of Accounts / Accounting Policy candidate. Reject Ledger Account as a profile of 015, constrained or not.

**Decisions.** Ledger Account cannot safely profile WM-ECO-015. Chart of Accounts needs an independent lifecycle.

**Strongest evidence.** 015 excludes CoA governance; 016 says 015 owns it. Both cannot hold. Reserved names do not include CoA. Ledger Account identity is (ledger, CoA node, effective interval); 015 identity is external settlement/custody. Shared type either imports CoA into 015 or leaves posting targets unmastered.

**Strongest counterexample.** One settlement against one bank Financial Account. Statutory JE-S: Dr Cash-GL / Cr AR, EUR, settlement date. Management JE-M: Dr Cash-pool / Cr Cash-received, USD presentation, notification date. Shared event-ref plus divergence reason; no offset. S hard-closes. Cash-GL should have been Restricted-Cash. Legal path: append JE-S2 next period or raise a hard-close exception; JE-S and closed 017 balances immutable; M not auto-adjusted. Profiling Ledger Account on 015 collapses those nodes and the bank account toward one identity, so correction mutates the closed book, nets S against M, or fuses treasury position with GL balance.

**Identity / mastership.** 015 masters Financial Account (issuer/custodian, external identifier, operational status). Unnamed CoA / Accounting Policy candidate masters Ledger Account and CoA versions. 016 masters Journal Entry and Posting only; entry identity is ledger-local. External event remains a correlation reference. Under the reserved 016 pairing, Financial Transaction is the bookkeeping record, not the external payment/invoice. 017 masters derived balances, not accounts or entries. No object is mastered in two reserved boundaries.

**Account boundary.** 015 = accounts you hold or settle with a counterparty. Ledger Account = nodes you post to. Intersection is a mapping, not a subtype. Clocks, CoA membership, posting eligibility, and identifier stability all diverge, so a safe 015 profile is impossible.

**Multi-ledger mapping.** One event yields N sibling Journal Entries, each bound to one ledger. Siblings share event-ref and a divergence reason when posted facts differ. They never offset. Shared 015 backing does not unify Ledger Accounts across ledgers.

**Balancing / currency.** Balance only inside (ledger × currency × scope × tolerance) from that ledger’s policy. 015 account currency is settlement currency, not journal balancing currency. Translation does not plug across ledgers. Tolerance residuals post in-ledger. 017 is per Ledger Account × ledger × currency × scope × as-of.

**Correction.** Append-only. Correction is a new same-ledger linked entry. Open ledger: reverse or adjust in the open period. Hard-closed ledger: next-period correction or explicit hard-close exception; no silent reopen; closed 017 period balances stay immutable. Correcting one sibling does not correct others.

**Scenario.** Event E received. JE-S posts statutory cash/AR in EUR on settlement date and balances in S. JE-M posts management cash-pool in USD on notification date, same E-ref, divergence = basis + FX + class. S hard-closes. Restricted-cash error found. JE-S2 appends in S next period (or hard-close exception). JE-S untouched. M unchanged if already correct; else JE-M2 in M only. Failures: mutate JE-S; net S against M; post S correction onto an M account; treat E or the bank Financial Account as the posting target.

**Invariants.**
1. Posting target is a Ledger Account, never a raw 015 Financial Account.
2. Ledger Account is mastered only by the unnamed CoA / Accounting Policy candidate.
3. At a posting instant a Ledger Account belongs to exactly one ledger and one CoA version.
4. 015 does not govern CoA membership, type, rollup, or posting eligibility.
5. 016 masters Journal Entry and Posting only; not accounts or CoA.
6. Ledger Account may reference at most one 015 account as backing; the reference is not identity.
7. A Journal Entry belongs to one ledger and balances only in that ledger’s (currency × scope × tolerance).
8. Cross-ledger siblings share event-ref plus divergence reason and must not net or offset.
9. Distinct ledgers imply distinct Ledger Account identities even if codes match or share one 015 backing.
10. Posted lines are immutable; correction appends a linked same-ledger entry.
11. Hard-close forbids mutation of closed entries, postings, and 017 period balances.
12. Sibling correction is per-ledger; closing one ledger does not freeze or auto-adjust the other.
13. Tolerance residuals post inside the same ledger, never as a cross-ledger plug.
14. External event identity is not Journal Entry identity; correlation is never the balancing key.
15. 015 operational close is not ledger period close and does not by itself block posting.
16. 017 does not net across ledgers; 015 treasury/custody position stays distinct from GL balance.

**Minimum completion shape.** 015 Financial Account (bank/custody only); unnamed CoA / Accounting Policy (versions, node catalog, mapping rules); Ledger Account as CoA node, not a 015 profile; Ledger (bound CoA version, currencies, close calendar, scope, tolerance); 016 Journal Entry (one ledger) plus Posting (one Ledger Account); 016 Financial Transaction as bookkeeping record distinct from the external event; event correlation reference; sibling group; 017 balance per ledger × account × currency × scope × period; correction link; hard-close exception.

**Blockers.** No source text for 015/016/017 this session. Financial Transaction vs Journal Entry vs external event still name-ambiguous. 017 may mix treasury position with GL balance. CoA has no reserved identifier. Tolerance unit, scope dimensions, CoA-to-ledger cardinality, currency roles, and hard-close reopen-versus-next-period policy unspecified. If CoA stays unassigned, attributes leak into 015 or 017 and recreate the contradiction.
