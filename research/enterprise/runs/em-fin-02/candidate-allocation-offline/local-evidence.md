# EM-FIN-02 local synthesis

## Disposition

- Reuse WM-ECO-015 for externally serviced Financial Accounts and for a constrained Ledger Account profile. A ledger account suppresses holder, servicer, protection, switching and dormancy facets and uses ledger-scoped, effective-dated account identity.
- Reuse WM-ECO-016 for Journal Entry and contained Posting lines.
- Treat Financial Transaction as a correlation reference to the external economic event, payment, invoice or other source master; do not create another transaction root.
- Reuse WM-ECO-017 for time-bound positions/balances.
- Add an identifier-unassigned Chart of Accounts / Accounting Policy candidate because neither WM-ECO-015 nor WM-ECO-016 owns taxonomy, hierarchy, permitted mappings, recognition policy or governance lifecycle.
- Add a thin identifier-unassigned Enterprise cross-ledger profile; allocate no runtime/model identifier.

## Account boundary and mastership

A bank, custody or payment account is party-bound, externally addressable and mastered by its servicing institution. A ledger account is mastered by ERP/finance and identified by ledger plus account code plus effective-dated version; account code alone is not globally stable. A balance is a separate as-of assertion in WM-ECO-017.

Correct the existing specification contradiction: WM-ECO-015 owns ledger-account identity, denomination, state and declared balance observations; WM-ECO-016 owns postings, balance derivation and reconciliation; Chart of Accounts and Accounting Policy belong to neither current model.

## Economic event, entry and posting

One external economic event can generate zero or more journal entries in each ledger. Each journal entry belongs to one ledger and contains at least two posting lines. Posting identity is entry plus line number. The source event link has correlation semantics only and never forces identical recognition, currency, accounts or dates across ledgers.

Each cross-ledger sibling link records event identity, reciprocal entry references and divergence reason. Payment, invoice and other source models retain their own lifecycle.

## Currency, balancing and period correction

Balancing occurs only inside one entry, one ledger, one declared balancing currency, scope and tolerance. Transaction, functional and reporting currency roles remain explicit with rate, rate type, date and source. Debits and credits from different ledgers can never offset each other.

Posted entries are immutable. A reversal or correction creates a linked entry with reason, original-entry reference, post-close/restatement indicators and authorization. A hard-closed period rejects posting without an explicit exception grant; a correction may post in the earliest permitted period. Each ledger corrects independently.

## Acceptance scenario

Event EV-1 is recognized in statutory ledger L-STAT as EUR 100,000 and management ledger L-MGMT as USD 44,000 under a different recognition rule. Entries S1 and M1 reference EV-1 and each other with the divergence reason; each balances independently. After statutory hard close, a scope correction creates S2 in an allowed open period and references immutable S1. Management correction M2 follows its own calendar. Original entries remain resolvable.

## Invariants

1. Financial Account, Ledger Account, Journal Entry, Posting, source event and Position identities remain distinct.
2. Every posting line belongs to one entry and one ledger.
3. Every entry balances within one ledger, currency, scope and tolerance.
4. No balancing scope spans ledgers.
5. Cross-ledger links express correlation, not arithmetic equality.
6. One event may generate zero or more entries per ledger.
7. Posted entries are immutable; correction appends a linked entry.
8. Hard-close posting requires a recorded exception grant.
9. Posting pins the ledger-account version effective on its accounting date.
10. Bank account identifiers never serve as ledger-account codes.
11. Balance observations state as-of time and derivation authority.
12. Initiator and authorizer are separated or an explicit compensating control is recorded.

## Holds

Both bases remain non-canonical reviewable drafts; WM-ECO-015 has a single-provider waiver and unverified/restricted sources, while WM-ECO-016 retains privacy, profile-validation and conformance holds. Relationship vocabulary and several registry edges conflict or remain empty. The Chart of Accounts / Accounting Policy candidate and Enterprise profile lack allocation; accounting-regime profiles, immutable pins, crosswalks and fixtures are incomplete. This checkpoint makes no canonical completeness, installability or publication claim.
