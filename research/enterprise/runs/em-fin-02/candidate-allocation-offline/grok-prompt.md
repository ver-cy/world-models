# Exact unsent Grok prompt — EM-FIN-02

Independent enterprise metamodel review. Do not browse, invent identifiers or claim standards conformance.

EM-FIN-02 covers FinancialAccount, LedgerAccount, JournalEntry, Posting and FinancialTransaction. Reserved boundaries are WM-ECO-015 Financial Account, WM-ECO-016 Financial Transaction / Journal Entry and adjacent WM-ECO-017 Position/Balance. Resolve the contradiction that WM-ECO-015 excludes Chart of Accounts governance while WM-ECO-016 says 015 owns it.

Assess this proposal: use WM-ECO-015 core for bank/custody accounts and a constrained profile for effective-dated ledger accounts; use WM-ECO-016 for journal entries and posting lines; keep the external economic event/payment/invoice as a correlation reference; use WM-ECO-017 for balances; introduce an identifier-unassigned Chart of Accounts / Accounting Policy candidate. Each entry belongs to one ledger and balances only within that ledger, currency, scope and tolerance. Cross-ledger sibling entries share an event reference plus divergence reason but never offset. Corrections append linked entries and hard-close exceptions are explicit.

Test one event represented differently in statutory and management ledgers, then corrected after one ledger hard-closes. Return <=900 words with: Verdict; strongest evidence; strongest counterexample; identity/mastership; account boundary; multi-ledger mapping; balancing/currency; correction; scenario; at least 10 invariants; minimum completion shape; blockers. Explicitly decide whether Ledger Account can safely profile WM-ECO-015 and whether Chart of Accounts needs an independent lifecycle.
