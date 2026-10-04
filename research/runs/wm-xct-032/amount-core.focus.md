Research only currency identity and exact decimal amount representation for
WM-XCT-032 Currency / Monetary Value.

- Use the exact registry identity and output `entry_kind` `mixin`. Treat the
  subject as an embeddable monetary declaration on a host object, not as a
  currency master, payment, price, account, ledger entry, transaction,
  financial instrument or economic event.
- The `model` block must describe the complete combined WM-XCT-032 boundary,
  including amount/currency, precision/rounding, valuation/conversion and
  governance. Never mention a split, pass, sibling pass or partial delivery in
  model, coverage or adversarial prose.
- Cover authoritative currency code/list identity plus edition or snapshot;
  alphabetic and numeric codes while display symbols remain labels only;
  active, withdrawn, funds, testing and precious-metal codes; successor and
  redenomination references without owning their lifecycle; exact decimal
  coefficient and scale; canonical lexical form versus display form; sign and
  zero; host-declared meaning of negative values; amount plus currency
  inseparability; range endpoints where the host needs a monetary interval;
  explicit exact, approximate, unknown, missing and not-applicable states so
  none is silently represented as zero.
- Do not infer country, jurisdiction, locale, legal-tender status,
  exchangeability, purchasing power or accounting treatment from a currency
  code. Reject binary floating-point as the canonical amount representation.
- Target 2 bundles, 4 layers and 7-8 findings with 3-5 discriminating questions
  each. Use at least six question kinds and concise descriptions.
- Every local ID, including bundle, layer, finding, question, data element,
  artifact and function IDs, must begin with `money-core-`.
- Limit functions to parse/normalize an exact amount, validate the currency
  reference, distinguish value states and compare only exact same-currency
  representations whose policy compatibility is supplied externally. Provide
  complete valid service_layers and coverage, but the merger takes canonical
  service layers from `governance`.
- Prefer primary ISO 4217 catalogue/maintenance material, official central-bank
  or public-authority currency lists, IEEE decimal-arithmetic material and
  primary data specifications with explicit monetary semantics. Do not claim
  unseen paywalled clauses.
