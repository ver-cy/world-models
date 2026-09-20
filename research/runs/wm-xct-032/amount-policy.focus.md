Research only precision, scale, quantization, rounding and comparison policy
for WM-XCT-032 Currency / Monetary Value.

- Use the exact registry identity and output `entry_kind` `mixin`.
- The `model` block must describe the complete combined WM-XCT-032 boundary,
  including amount/currency, precision/rounding, valuation/conversion and
  governance. Never mention a split, pass, sibling pass or partial delivery in
  model, coverage or adversarial prose.
- Cover declared precision and scale versus observed digits; minor-unit
  metadata as a version-pinned currency property rather than an implicit
  storage limit; calculation precision versus settlement/display precision;
  accounting, cash and custom quantization; rounding mode, increment, stage,
  direction and tie handling; intermediate versus final rounding; residual or
  remainder and reconciliation; tolerance and materiality supplied by the
  host; exact versus approximate/bounded values; overflow/underflow and
  representability; equality, ordering, aggregation and allocation only under
  compatible currency, valuation and rounding contexts; explicit failures
  rather than hidden coercion.
- Never assume two decimal places or one universal rounding rule. Preserve
  zero-decimal, three-decimal and non-decimal cash increments, future currency
  metadata changes and calculations requiring greater precision than the
  reporting minor unit.
- Target 2 bundles, 4 layers and 7-8 findings with 3-5 discriminating questions
  each. Use at least six question kinds and concise descriptions.
- Every local ID, including bundle, layer, finding, question, data element,
  artifact and function IDs, must begin with `money-policy-`.
- Limit functions to validate a precision policy, quantize under an explicit
  rule, expose residuals, allocate with reconciliation and compare/aggregate
  compatible values without implicit conversion. Provide complete valid
  service_layers and coverage, but the merger takes canonical service layers
  from `governance`.
- Prefer primary IEEE decimal arithmetic, ISO 4217 maintenance material,
  official central-bank cash-rounding rules and primary accounting/data
  specifications. Treat programming-language/library defaults as
  implementation evidence only.
