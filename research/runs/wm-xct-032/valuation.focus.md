Research only valuation, quotation and currency-conversion context for
WM-XCT-032 Currency / Monetary Value.

- Use the exact registry identity and output `entry_kind` `mixin`.
- The `model` block must describe the complete combined WM-XCT-032 boundary,
  including exact amount/currency semantics, valuation/conversion context and
  governance. Never mention a split, pass, sibling pass or partial delivery in
  model, coverage or adversarial prose.
- Cover amount role such as original, transaction, settlement, functional,
  presentation or reported amount through a pinned classifier; valuation date
  or instant distinct from observation/ingestion; valuation basis/method and
  market or scenario reference without implementing the method; original and
  converted amount linkage; base and quote currency; rate direction and unit
  convention; rate value with precision; rate type and source; applicable
  market/session; effective/as-of interval; publication and retrieval times;
  stale/estimated/provisional/final status; direct, inverse, cross and
  triangulated derivation; rate chain; rounding order; conversion equation;
  fees, spreads and taxes separately referenced; reproducibility evidence and
  correction/supersession of a valuation assertion.
- Keep prices, tariffs, payments, trades, market-data series, valuation models,
  accounting policies, journal entries, tax calculations and financial
  instruments in their owning models. A converted amount never overwrites the
  original and an exchange rate never becomes the identity of either amount.
- Distinguish event time, valuation time, rate effective time, publication
  time and ingestion time. Never use a current rate for a historical value
  without an explicit revaluation assertion.
- Target 2-3 bundles, 5-6 layers and 9-11 findings with 3-5 discriminating
  questions each. Use at least seven question kinds and concise descriptions.
- Every local ID, including bundle, layer, finding, question, data element,
  artifact and function IDs, must begin with `money-val-`.
- Limit functions to bind valuation context, select a declared rate under a
  caller-supplied policy, calculate a reproducible conversion, reconcile
  original and reported values and record a correction. Provide complete valid
  service_layers and coverage, but the merger takes canonical service layers
  from `governance`.
- Prefer official IFRS/IAS public material, central-bank and public-authority
  rate specifications, ISO 20022 data dictionaries, XBRL taxonomies/specs and
  primary financial-data standards. Do not claim unseen paywalled clauses.
