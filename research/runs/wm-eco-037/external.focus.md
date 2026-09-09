# WM-ECO-037 bounded external research focus

Produce one complete schema-valid result for `WM-ECO-037 Debt Instrument`.

Treat the root as the governed, identity-bearing contractual debt claim and
obligation definition, not as a holder position or a payment. Cover instrument
identity and version lineage; loan, note, bond, bill, debenture, certificate of
deposit, commercial paper and other debt classes; issuer, borrower, obligor,
creditor, lender, investor, trustee, agent and guarantor roles; governing legal
basis; currency, original principal or notional and issued amount; issue,
effective, accrual-start and maturity dates; fixed, floating, zero-coupon,
indexed and capitalizing interest; reference index, spread, cap, floor,
compounding, day-count and business-day conventions; contractual principal,
interest and fee schedules; amortization, redemption, prepayment, call, put,
conversion, exchange and extension options; ranking and subordination;
security, collateral and guarantees as references; covenants, conditions,
waivers, events of default and acceleration; program, series and tranche
context; amendments, restructurings, novations and successors; identifiers,
provenance, access, retention, projections and safe agent operations.

Keep party, agreement, prospectus, issuance and allocation, holding or
position, ownership, payment or cash transaction, ledger posting, market
listing and trade, price or valuation observation, rating opinion, collateral
asset and security interest, guarantee, benchmark, default case, dispute,
enforcement, insolvency, tax, regulatory filing and record masters external.
Do not conflate the instrument definition with an issuance event or a holding;
the holder's asset view with the issuer's liability view; scheduled cashflow
with an amount due, actual payment or accounting posting; original principal
with outstanding principal, carrying amount, fair value or market price;
secured status with collateral identity, value, perfection or priority;
covenant term with compliance observation, breach or default decision; rating
with fact; or amendment with novation, restructuring, refinancing or
derecognition.

The candidate relation ledger says `WM-ECO-037 EXTEND WM-ECO-005`, but the
former Credit / Security category is marked for split. Treat the candidate as
unapproved and preserve a clear boundary from equity instruments and security
holdings.

Target 6 bundles, 12 layers, 24 findings, 72 questions, 24 artifacts and 10
functions. Prefer IFRS 9, the BIS/ECB/IMF Handbook on Securities Statistics,
ISO 6166, ISO 10962, ISO 4217, ISO 17442, OMG FIGI, EDM Council FIBO,
ISO 20022, XBRL 2.1, RFC 3339, PROV-O, DQV, ODRL, OWL-Time and SKOS. Pin
versions where possible and state licensing, jurisdiction and conformance
limits.
