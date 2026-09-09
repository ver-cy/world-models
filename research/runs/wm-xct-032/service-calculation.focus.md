Research only calculation, reconciliation and projection operation semantics
for WM-XCT-032 Currency / Monetary Value.

- Use the exact registry identity and output `entry_kind` `mixin`.
- The `model` block must describe the complete combined WM-XCT-032 boundary.
  Never mention a split, pass, sibling pass or partial delivery in model,
  coverage or adversarial prose.
- Cover validate, quantize, value/convert, reconcile, export and redact.
- Preserve original amount/currency for every derived value. Bind rate source,
  base/quote direction, reference time, retrieval time, rate chain, measurement
  basis, rounding policy, residual and derivation lineage for reproduction.
- Cover missing/stale/ambiguous/non-exchangeable rates, unsupported currency or
  policy pins, divide-by-zero or invalid inverse, precision loss, reconciliation
  outside tolerance and lossy/redacted exports as explicit outcomes.
- Functions calculate or report only. External systems own rate acquisition,
  payments, accounting posting, persistence, disclosure authorization and
  policy enforcement.
- Target 1 bundle, 2-3 layers and 4-5 findings with 3-4 discriminating questions
  each. Use at least six question kinds and concise descriptions.
- Every local ID, including bundle, layer, finding, question, data element,
  artifact and function IDs, must begin with `money-svccalc-`.
- Prefer primary ISO 4217, ISO 20022, IFRS/IAS, XBRL and public central-bank
  material. Preserve unresolved jurisdictional, accounting and market
  differences as gaps/holds.
