# Verdict

**Reuse both reservations; add one thin enterprise profile; open one new model candidate.** Place `FinancialAccount` and `LedgerAccount` on **WM-ECO-015**, `JournalEntry` and `Posting` on **WM-ECO-016**, and treat `FinancialTransaction` as a **reference slot, not a new root** — the economic event is owned by the model that causes it (WM-ECO-009 for payments, WM-ECO-008 for billing) or by an unassigned economic-event model. Time-bound balances go to **WM-ECO-017**, not to either. The contour's own scope line ("Банковский счёт и счёт учёта различаются") is correct but under-specified: the distinction is not two models, it is one account record plus a *chart-of-accounts governance* concern that **neither** frozen spec owns. That gap is the only genuinely new work.

# Evidence

WM-ECO-015 `out_of_scope` excludes "Chart-of-accounts taxonomy governance and accounting policy" and "derivation of balances from [postings] (owned by WM-ECO-016)". Its `product-and-regulatory-classification` finding nevertheless lists "internal ledger account" as a regulatory category value, and SRC-001 (FIBO ClientsAndAccounts) is cited for `LedgerAccount` alongside `DepositAccount`. Its `balance-and-statement-declaration` finding carries `de-balance-observation` (typed, as-of instant, observation instant) and `q-bal-derive` ("which model derives the balance… reported or recomputed here").

WM-ECO-016 `boundary_notes` states "The account owns the chart-of-accounts record and derived balances", and `out_of_scope` excludes "Chart of accounts, account master data and derived account balances (owned by WM-ECO-015)". Its `fnd-ledger-book-context` carries `de-ledger-id`, `de-functional-currency`, `q-framework-jurisdiction` and `q-parallel-ledgers`. `q-balance-rule` makes balancing scope a *declared* level. `q-reversal-period`, `fn-reject-closed-period`, `de-period-state` and `fnd-top-side-adjustments` cover hard close.

# Identity/mastership

`FinancialAccount`: master = servicing institution; identity per WM-ECO-015 `artifact_rules` (master-system identifier first, IBAN/LEI second, Dimension ULID last; creation "cannot be keyed only on… an IBAN"). `LedgerAccount`: master = ERP/finance under the contour's owner (Финансовый руководитель); identity = ledger-scoped account code plus effective-dated version — the code alone is not an identity because it is reused and re-mapped. `JournalEntry`: master = ledger of record, identifier qualified by ledger and reporting entity (WM-ECO-016 `art-posted-entry-record`). `Posting`: identity = entry identifier plus line number; no independent master. `FinancialTransaction`: no mastership claimed here; the profile owns only the **correlation key**.

# Account boundaries

Three separations, all already latent in the dossier:

1. **Bank/custody/payment account** (WM-ECO-015 core): servicer, IBAN/BBAN/PAN schemes, holders and mandates, deposit-guarantee designation, dormancy, CRS/FATCA category. Externally addressable, party-bound.
2. **General-ledger account** (WM-ECO-015 *profile*): a code in a book of account, no holder, no servicer, no protection scheme, no reachability. It reuses 015's identity, denomination reference, state/lifecycle and effective-period machinery and **suppresses** the party, protection, switching and dormancy findings as not-applicable.
3. **Position/balance** (WM-ECO-017): time-bound measured stock, its own aggregate, `as-of` separated from observation and knowledge time. A balance is never an account attribute; 015 holds only *declared observations* with a named derivation owner.

A bank account and a GL control account are related by reconciliation, not identity: `fnd-reconciliation-completeness` (subledger tie-out) is the join, and WM-ECO-016's conflict list already warns that the servicer's statement entry and the owner's journal entry are two books' records of one transfer.

# Economic event/transaction/journal/posting

Four levels, strictly ordered: **economic event** (one, external) → **journal entry** (one per ledger, balanced, WM-ECO-016 aggregate) → **posting line** (≥2 per entry, one account each) → **balance/position** (derived, WM-ECO-017). "Financial transaction" is a homonym across ISO 20022 single-sided booked entries, FIBO BP process flows and ledger postings; WM-ECO-016 records this as a conflict and its adjudication retained `aggregate` over `event` precisely so the balancing invariant has a carrier. Do not resolve the homonym by minting a fifth root.

# Multi-ledger mapping

One event → N entries, one per ledger, linked by a **shared economic-event identifier plus reciprocal sibling references and a divergence reason** (`q-parallel-ledgers` answer_data: sibling posting identifiers, linkage mechanism, divergence reason where amounts differ). The link is a correlation edge with **no arithmetic force**. Each entry resolves its own `de-ledger-id`, framework, fiscal calendar, balancing scope and rounding rule from a ledger profile (`art-ledger-profile`). Amounts, recognition timing and even the set of accounts may legitimately differ per ledger; only the event reference is common.

# Currency and balancing

Balancing is evaluated **within one ledger, in that ledger's declared balancing currency, at that ledger's declared scope and tolerance**. Transaction currency, functional currency and group reporting currency are separate roles on the line (`de-transaction-currency`, `de-reporting-amount`), with `de-fx-rate`, rate type, rate date and `de-fx-rate-source` recorded per translation. Direction is the indicator plus unsigned magnitude; signed forms are derived. Consequently the contour's negative case — a debit in one book offsetting a credit in another — **fails by construction**: no balancing scope spans ledgers, so cross-ledger amounts never enter the same sum.

# Correction and period close

Posted entries are immutable; correction is a **new linked entry**, never an edit. Hard close blocks posting; `fn-reject-closed-period` permits an exception only against a recorded grant, and `q-reversal-period` requires an explicit rule for which period receives the reversal when the original is closed. Provenance is preserved by `de-corrects-entry-ref` (bidirectional), `de-correction-reason`, `fnd-top-side-adjustments` (`adjustment_class`, `original-entry-id`, `post-close-flag`, `restatement-flag`) and `art-change-audit-log`. Correction in one ledger does **not** oblige simultaneous or equal correction in another; each follows its own period state.

# Lifecycle

Ledger account: proposed → active (posting-eligible window) → restricted → closed-for-posting → retained; versions effective-dated, non-overlapping, never rewritten on reorganisation. Journal entry: draft → validated → authorised → posted (immutability point) → reversed/corrected/superseded. Period: open → soft-closed → hard-closed, with `art-period-close-record`. Positions are appended, never mutated.

# Scenario

Event **EV-1**, service completed 2026-09-28, EUR 100,000.
- **L-STAT** (IFRS, EUR functional, hard close 2026-10-15): entry S1, effective 2026-09-28, Dr receivable 100,000 / Cr revenue 100,000 EUR. Balances in EUR.
- **L-MGMT** (internal policy, USD functional, soft close): entry M1, effective 2026-09-28, ratable recognition of EUR 40,000 translated at 1.10 → Dr contract asset 44,000 / Cr revenue 44,000 USD. Balances in USD.
- Both carry `economic_event_id = EV-1`, sibling references S1↔M1, divergence reason "recognition policy and functional currency differ". No cross-ledger sum is attempted.
- **2026-11-03**: scope reduced; statutory amount should be EUR 90,000. Period 2026-09 in L-STAT is hard-closed, so S1 is untouched. Entry S2 posts to the earliest open period with `adjustment_class = prior-period correction`, `original-entry-id = S1`, reason code, restatement flag per materiality, authoriser ≠ initiator. Separately M2 corrects L-MGMT on its own timetable. S1 and M1 remain retrievable and unaltered; the event's net effect per ledger is read from each chain.

# Invariants

1. Every posting line carries exactly one ledger and one transaction currency.
2. Debits equal credits within one entry, one ledger, one balancing currency, at the declared scope and tolerance.
3. No balancing scope spans two ledgers; cross-ledger links are correlation only.
4. An economic event may have 0..N entries per ledger; each entry belongs to exactly one ledger.
5. Posted entries are immutable; every correction is a new entry referencing its original in both directions.
6. Posting to a hard-closed period requires a recorded exception grant or is rejected.
7. A posting pins the ledger-account version effective at its accounting date.
8. Balance observations on an account are reported, as-of qualified, and name their derivation owner; they are never authoritative over the entry set.
9. A bank/custody account identifier is never a general-ledger account code.
10. Initiator and authoriser are distinct unless a documented compensating control exists.

# Minimal completion shape

(a) Correct the WM-ECO-015 ↔ WM-ECO-016 boundary text: 015 owns the **ledger-account record** (identity, state, denomination, activity window) and **declared balance observations**; 016 owns **balance derivation and reconciliation**; **chart-of-accounts taxonomy and accounting policy are owned by neither** and become a registered candidate model with an unassigned identifier. 016's phrase "derived account balances (owned by WM-ECO-015)" must read "declared balance observations". (b) Add the EM-FIN-02 enterprise profile: required `economic_event_id`, reciprocal sibling-entry references with divergence reason, per-ledger balancing-scope and currency declaration, closed-period exception-grant register. (c) Register the WM-ECO-017 ↔ WM-ECO-015 edge, which the registry asserts but the relations list does not carry. (d) Reconcile the CONTAINS/CHILD vocabulary mismatch between the relations row and 015's composition block.

# Holds

Both specs are `publishableCanonical: false`, `adjudicationStatus: reviewable-draft`. WM-ECO-015 carries a single-provider waiver (Grok waived), unpinned mutable source URLs (FIBO master branch, ISO 20022 live catalogue), unread ISO 13616/20022 normative text, contested US access obligations, and coverage entries its own audit downgrades to partial. WM-ECO-016 is dual-provider but declares privacy as a gap, no conformance to any cited standard, retention periods illustrated only from US and UK instruments, and unretrieved SAF-T/camt schemas. WM-ECO-016's registry row has empty `composition_role`, `default_link_type` and `relations_ref`; the inbound WM-XCT-014 → WM-ECO-015 edge is asserted but unconfirmed. Chart-of-accounts governance, national GAAP/IPSAS/AAOIFI recognition differences, distributed-ledger immutability points and posting-rule change control are unsupported in the frozen set. This review is boundary adjudication over the dossier as frozen; it is not a completeness claim and nothing here is installable.
