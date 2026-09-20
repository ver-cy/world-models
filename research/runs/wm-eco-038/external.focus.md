# WM-ECO-038 bounded external research focus

Produce one complete schema-valid result for `WM-ECO-038 Equity / Security
Holding`.

Treat the root as a governed, identity-bearing security position held by one
holder in one declared capacity and account or register context, not as the
security instrument itself. Cover holding and version identity; holder,
beneficial owner, legal owner, registered holder, nominee, custodian,
subcustodian, account servicer and investment manager roles; instrument,
issuance, share class, listing, account, depository and register references;
direct and indirect, beneficial, registered, nominee, custody, long, short and
other position classes; quantity, unit, settled, available, blocked, pledged,
lent, borrowed, pending and encumbered balances; acquisition lots and cost-basis
references; economic, voting, control, conversion and participation rights;
restrictions and encumbrance references; acquisitions, disposals, trades,
transfers, settlement, securities lending, repo and collateral movements as
external events; correction, split, merge, account-transfer and successor
lineage; corporate-action event, record date, ex date, eligibility, entitlement,
election, instruction, status, cash or security movement and outcome references;
income, valuation, accounting, risk and disclosure views; regulatory reporting
thresholds; provenance, access, retention, reconciliation, projections and safe
agent operations.

Keep security or equity instrument, issuance, party, account, register,
custody, order, trade, settlement, payment, ledger, tax lot, valuation, price,
rating, securities-lending agreement, repo, collateral, corporate-action event,
entitlement, instruction, movement, tax, beneficial-ownership determination,
regulatory filing and records masters external. Do not conflate a holding with
the instrument, account or owner; legal title with beneficial or economic
interest; registered holder with ultimate beneficial owner; quantity with
ownership percentage, voting power or value; trade date with settlement or
effective ownership; settled with available, free, pledged, lent or entitled
quantity; corporate-action eligibility with election, instruction, acceptance,
movement or payment; valuation with contractual fact; or regulatory disclosure
with complete ownership truth.

The candidate relation ledger says `WM-ECO-038 EXTEND WM-ECO-005`, but the
former Credit / Security category is marked for split. Treat that relation as
unapproved. Preserve explicit boundaries from `WM-ECO-037 Debt Instrument`,
generic ownership and stewardship, personal-property inventories and external
equity/security instrument definitions. Consolidated portfolio views are
projections over source positions, not replacement masters.

Target 6 bundles, 12 layers, 24 findings, 72 questions, 24 artifacts and 10
functions. Prefer the BIS/ECB/IMF Handbook on Securities Statistics, ECB
Securities Holdings Statistics and its legal framework, IFRS 9 and IAS 32,
EU CSDR and Shareholder Rights rules, SEC beneficial-ownership material, ISO
6166, ISO 10962, ISO 17442, ISO 4217, OMG FIGI, FIBO security and corporate
action ontologies, ISO 20022 securities and corporate-action messages, RFC
3339, PROV-O, DQV and ODRL. Pin versions and keep jurisdiction, licensing,
reporting and conformance limits explicit.
