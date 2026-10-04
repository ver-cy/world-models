# Exact unsent Grok prompt — EM-FIN-06

Independent enterprise metamodel review. Do not browse, invent identifiers or claim publication readiness.

EM-FIN-06 covers Investment, FinancialInstrument, InvestmentTransaction and Valuation. Complete adjacent drafts cover WM-ECO-038 Equity / Security Holding, WM-ECO-002 Price / Valuation, WM-ECO-016 Financial Transaction / Journal Entry, Organization, Inter-organizational Relationship and Governance Body.

Assess this proposal: reuse WM-ECO-038 only as the security/equity position master; reuse/profile WM-ECO-002 for Valuation with mandatory subject-kind; reuse event and WM-ECO-016 posting boundaries for InvestmentTransaction; create identifier-unassigned Financial Instrument and Investment roots. Allocate no identifier.

Separate investee/underlying asset, instrument, investment participation, holding, acquisition/disposal event, settlement, posting, valuation, conversion right, conversion event, ownership, voting, control and consolidation. Decide whether Investment truly needs identity beyond portfolio membership and whether a unified Financial Instrument root conflicts with WM-ECO-037 Debt Instrument and the unassigned Share Class candidate.

Require immutable instrument terms and versions, issuer/holder capacities, position lots and restrictions, effective/observation/knowledge times, valuation method/basis/currency, assumptions, inputs, model version, evidence, uncertainty, review and supersession. Contingent conversion rights must not count as current votes or ownership. Conversion must create explicit predecessor/successor position and posting lineage.

Test one convertible instrument and two same-date valuations under different methods/currencies. Preserve divergence and provenance. Reject the latest company valuation as a source of voting or control rights.

Return <=900 words with: Verdict; strongest evidence; strongest counterexample; identity/mastership; instrument/investment/holding; transactions/postings; valuation; conversion; ownership/voting/control; time/currency/provenance; governance; scenario; at least 10 invariants; minimum model set; blockers. Explicitly decide which candidates need independent roots.
