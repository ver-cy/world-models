Research only authority, lifecycle, provenance, access, retention and
interoperability controls for WM-XCT-032 Currency / Monetary Value.

- Use the exact registry identity and output `entry_kind` `mixin`.
- The `model` block must describe the complete combined WM-XCT-032 boundary,
  including exact amount/currency semantics, valuation/conversion context and
  governance. Never mention a split, pass, sibling pass or partial delivery in
  model, coverage or adversarial prose.
- Cover accountable value owner, currency-data steward, valuation authority,
  preparer, independent reviewer and approver; authority for amount correction,
  currency/rate source selection and rounding policy; host-dependent weak
  identity; version/effective interval/supersession; currency-list and policy
  version pins; provenance of original and derived values; segregation of
  duties; evidence integrity; sensitive or commercially restricted values;
  supported bundle/layer/finding/artifact access scopes; retention, legal hold
  and tombstone; regional/accounting profiles; interoperability mappings;
  audit references and limitations.
- Roles and authorization assertions are advisory metadata. An external
  authorization component owns allow/deny decisions. Do not invent a universal
  owner or authority for every monetary value.
- Do not create independent lifecycles for a currency, price, rate feed,
  transaction, account or instrument. Lifecycle verbs govern the monetary
  binding/valuation assertion on its host unless an external record is cited.
- Target 2 bundles, 4-5 layers and 8-10 findings with 3-5 discriminating
  questions each. Use at least seven question kinds and concise descriptions.
- Every local ID, including bundle, layer, finding, question, data element,
  artifact and function IDs, must begin with `money-govctl-`.
- Functions may describe declarative lifecycle/provenance/access/retention
  checks only. External systems own policy enforcement, legal decisions,
  payment, posting, market-data acquisition and physical destruction.
- Prefer primary ISO, IFRS/IAS public material, ISO 20022, XBRL, W3C PROV,
  access-control and records-management standards. Preserve unresolved
  jurisdictional, accounting and market differences as gaps/holds.
