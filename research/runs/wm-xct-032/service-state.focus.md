Research only state-changing and state-reading operation semantics for
WM-XCT-032 Currency / Monetary Value.

- Use the exact registry identity and output `entry_kind` `mixin`.
- The `model` block must describe the complete combined WM-XCT-032 boundary.
  Never mention a split, pass, sibling pass or partial delivery in model,
  coverage or adversarial prose.
- Cover read/effective-time resolution, create/bind to a host, update/correct by
  supersession, review/approve evidence, and delete/tombstone readiness.
- Specify resolvable host binding, authorization references, idempotency,
  optimistic concurrency, immutable originals, version/effective intervals,
  referential integrity, legal hold and explicit failure semantics.
- Authorization functions report advisory eligibility only. The external
  authorization component owns allow/deny; the external host owns persistence;
  the records authority owns disposition and physical destruction.
- Do not create a lifecycle for a currency, price, transaction, account, rate
  feed or instrument. Operations act only on the monetary assertion bound to
  its host.
- Target 1 bundle, 2-3 layers and 4-5 findings with 3-4 discriminating questions
  each. Use at least six question kinds and concise descriptions.
- Every local ID, including bundle, layer, finding, question, data element,
  artifact and function IDs, must begin with `money-svcstate-`.
- Functions own declarative resolution, precondition checks, correction plans,
  review evidence and disposition-readiness reports. They perform no external
  side effects.
- Prefer primary provenance, access-control and records-management standards.
  Preserve jurisdictional and accounting differences as gaps/holds.
