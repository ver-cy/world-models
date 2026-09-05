Research historical resolution and operational edge cases for WM-XCT-036
Alias / Same-as Mapping.

- Use the exact registry identity and output `entry_kind` `mixin`.
- The `model` block must describe the complete combined WM-XCT-036 boundary.
  Never mention a split, pass, sibling pass or partial delivery in model,
  coverage or adversarial prose.
- Cover as-of resolution with explicit event time versus observation/ingestion
  time, current versus historical answers, source/target version pins and stale,
  missing, unresolved or tombstoned endpoints.
- Cover redirect chains and loops, maximum hops, permanent versus temporary
  relocation, canonical-link hints and the rule that transport redirects do not
  by themselves prove identifier or real-world identity.
- Cover endpoint merge and split consequences, cluster re-evaluation requests,
  impacted downstream references, notifications and migration/readiness reports
  while leaving endpoint and master-data mutation external.
- Cover concurrent proposals, optimistic concurrency, idempotency keys,
  duplicate assertion detection, conflicting active assertions, compensating
  actions and emergency quarantine. Retain all prior decisions and evidence.
- Specify deterministic resolution statuses, ambiguity and no-answer outcomes;
  do not silently select a canonical endpoint or follow an unbounded chain.
- Do not own relation reasoning, redirect execution, endpoint availability,
  authorization or data merge.
- Target 2 bundles, 4-5 layers and 7-9 findings with 3-5 discriminating
  questions each. Use at least eight question kinds. Every local ID begins
  `als-res-`.
- Prefer primary IETF HTTP/link, temporal, provenance and concurrency guidance.
