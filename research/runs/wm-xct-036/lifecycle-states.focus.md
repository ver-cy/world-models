Research assertion lifecycle states and immutable transition history for
WM-XCT-036 Alias / Same-as Mapping.

- Use the exact registry identity and output `entry_kind` `mixin`.
- The `model` block must describe the complete combined WM-XCT-036 boundary.
  Never mention a split, pass, sibling pass or partial delivery in model,
  coverage or adversarial prose.
- Cover candidate/proposed, under-review, active, disputed, superseded,
  retracted, rejected, expired and tombstoned states with allowed and forbidden
  transitions, entry/exit conditions, responsible authority and immutable
  transition records.
- Distinguish correction, supersession, retraction, endpoint deprecation,
  replacement/redirect, authority withdrawal and evidence expiry. None silently
  deletes endpoints, rewrites history or erases negative evidence.
- Cover effective intervals and separate event time from observation/ingestion
  time. Require RFC 3339 timestamps with seconds and an explicit `Z` or numeric
  offset; dates are never identifiers or serial tokens.
- Preserve prior decisions, reasons, reviewers, supporting and refuting
  evidence references, supersedes/superseded-by links and tombstones.
- Cover conflicting simultaneous states, invalid transitions, late-arriving
  events, retroactive corrections, rollback requests and authority loss. State
  what remains readable after retraction or tombstoning.
- Do not own endpoint lifecycle, redirect execution, match computation,
  authorization decisions or master-data mutation.
- Target 2 bundles, 4-5 layers and 7-9 findings with 3-5 discriminating
  questions each. Use at least eight question kinds. Every local ID begins
  `als-state-`.
- Prefer primary provenance, temporal and records-management standards.
