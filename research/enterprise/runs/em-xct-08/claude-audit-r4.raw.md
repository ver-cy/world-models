# EM-XCT-08 R4: Delta Audit

**Verdict: ACCEPT WITH LIMITS.** Reading the patched code, H1 and M1 are closed. M2 and M4 are resolved or narrowed to disclosed residuals, M3 is managed by lowering the caps and documenting them, and the Low items are fixed or documented. I found no new blocker. The new issues are Low: one spec/code contradiction, one incomplete crash-recovery path, and some test premises that are weaker than their test names suggest.

## Input confirmation and scope

- **R3 baseline:** all 30 complete bodies from R3 fragments 1–16 are still available in this conversation.
- **Patch:** the complete R3→R4 patch (parts 1–8, marker `SYNC-R4-DELTA-20260922`) has hunks for all 17 changed files and full bodies for the 3 added files: `benchmark.py`, `benchmark-results.json` and `environment-report.json`.
- **Unchanged files:** the 21 files listed as unchanged keep their R3 bytes.
- **Out of review:** the same 8 hash-only files and the external composer/native toolchain.
- **JSON hunks:** the JSON and example hunks use line numbers from a pretty-printed layout, while my baseline copies are the minified forms supplied in R3. Every change in those hunks is a value substitution, so I applied them at the value level.

This was a static, delta-focused audit. I executed nothing, browsed nothing and verified no hash. The test report (98 tests), native acceptance report (3 profiles), benchmark and environment reports are author evidence only. I checked them for internal consistency and nothing more:
- New `buildId` values match across examples, acceptance and benchmark.
- The spec digest matches the inventory.
- The 17 added test names match the 17 new `test_sync.py` methods.
- `outcomeDigest` values are unchanged wherever derived state is unchanged, which is consistent with `buildId` entering the chain root but not the state.

## Disposition of R3 issues

**H1, attest-coverage bypass: CLOSED.** Three gates in `sync_register.py` now apply to attested rounds (source-snapshot or `visibilityCovered`):
- The `commit` round branch refuses a new terminal page unless the actor holds current attest-coverage.
- `round-seal` refuses an error-free seal without current attest-coverage.
- `round-open` still gates opening.

Both refusals return DENIED with no event. The R3 counterexample (intake-only empty terminal page, then error-free seal) is now refused at both steps. The revocation variant is covered because both gates re-check the grant at admission time. Replay stays deterministic because the gates are evaluated against the historical policy at `recordedAt`. An intake-only error-bearing seal always gives `complete=False`.

The tests `test_intake_only_cannot_complete_attested_snapshot`, `test_revoked_attester_cannot_terminally_commit_or_successfully_seal` and `test_visibility_attestation_gate_applies_to_best_effort_too` match these paths.

**M1, nondeterministic availability evidence: CLOSED.** The filter now includes `purpose`, and selection uses `max(key=(sequence, ordinal))`. Both fields exist on every occurrence. `test_availability_selection_is_roundtrip_stable_and_ordinal_ordered` builds exactly the R3 counterexample: slot-digest order is the reverse of commit order, and the test compares before and after a canonical round trip.

**M2, cross-scope oracles and governance: RESOLVED AS DISCLOSED RESIDUAL.**
- `mapping_outcome` matches only same-scope mappings, so there are no cross-scope pins or disclosure of foreign mapping IDs in receipts.
- A foreign scope/purpose collision on mapping or round IDs, and a foreign active-lineage reservation at activation, now return a uniform DENIED with no event.
- Global lineage uniqueness is kept. Moving a claim between scopes needs map rights in both scopes, which is documented and tested.
- The remaining one-bit availability inference (collision versus a fresh success) and the exposure of register-wide activity through receipt IDs are now disclosed in `model-spec.md` and `adoption-limits.md`.

**M3, full-replay cost: MANAGED BY REDUCED CAPS.** The limits are now 128 events and 512 KiB canonical size. The schema's `maxItems` of 128 agrees with `MAX_EVENTS`, and conflicts are capped at 32 total and 4 per writer. The quadratic behaviour is documented rather than removed, and the R3 limits are explicitly withdrawn.

The benchmark design is reasonable: large state is present from early in the history, it measures near the cap, and it runs two real processes. It is one Windows run, though, so its roughly 1.4 s per operation is an observation, not a bound. `writerTimeouts` is hard-coded to `0`; it is truthful only because the worker exit-code assertions gate report generation.

**M4, transport versus canonical size: CLOSED.** `decode` enforces `MAX_TRANSPORT_BYTES` (8 MiB) on raw input, and `encode` enforces the 512 KiB canonical budget. The pretty-printed and ASCII-escaped test covers the R3 counterexample.

**Low issues:**
- **L1:** closed on the main path. `RecursionError` is converted to `Invalid` in both `encode` and `decode`.
- **L2:** documentation now states that only jsonschema is pinned, and `environment-report.json` records the rest.
- **L3:** partially closed; see N2.
- **L4:** head and fence coordination is now a documented host duty.
- **L5 (clock check before authorization):** unaddressed. It is Low severity and relies on a trusted host input.
- **L6:** the ai-team scheme is corrected, and the example chain is consistently regenerated.

## New findings

**N1 (Low, spec/code contradiction).** `model-spec.md` and `spec.json` `model.scope` still say that a "changed source-kind interpretation … suspends new pins with active-pin-suspended". Because pins are now same-scope only and scopes are immutable, that path cannot occur. A changed kind means a different scope, which yields `unmapped`, and `test_source_kind_change_cannot_reuse_mapping` now asserts `unmapped`. The `sourceObjectKind` comparison in `mapping_outcome` is dead code, and `spec.json` SS-F10/SS-Q19 still mentions a source-kind check. **Required:** correct the text, or remove the dead comparison and keep the text, so that specification, code and test agree.

**N2 (Low, recovery).** The new guard refuses only 0-byte stores. If a crash happens after SQLite has written pages but before COMMIT, the file is non-empty and a hot journal is left behind. Reopening passes the size check, SQLite rolls back, and `SELECT … FROM bootstrap` then raises a raw `sqlite3.OperationalError` instead of the documented refusal. The specification's catch-all ("other corrupt/partial store errors remain host recovery events") covers this, but the test only exercises a `touch()` file. **Suggested:** check for the tables' existence after connecting, and add a test that crashes during the bootstrap transaction itself.

**N3 (Low, residual semantics).** An intake-only writer can still take nonterminal page slots in an attested round, which displaces a page the attester planned (the attester then gets `page chain gap` or a stale-head error). The attester's terminal page and seal therefore vouch for pages it did not write. An intake-only writer can also force an attested round to an errored, incomplete seal. Neither can produce a false absence, since added pages only add keys or make the round incomplete. They do make the attester's review of the full page set a host duty, which is not documented.

**N4 (Low, test premise).** In `test_foreign_mapping_and_round_id_collision_is_uniform_refusal` and `test_cross_scope_pin_requires_explicit_stewardship_move`, WRITER holds grants in both scopes. The code path does not depend on the caller's rights in the foreign scope, so the logic holds, but the tests do not exercise the privacy premise: a principal with rights in scope B only.

## Missing meaningful tests

1. A principal with grants only in scope B, for foreign mapping/round ID collisions and for foreign active-lineage activation (N4).
2. A crash inside the bootstrap transaction that leaves a non-empty file with a hot journal (N2).
3. An intake-only nonterminal page displacing an attester's planned page, and an intake-only errored seal of an attested round (N3).
4. A test tying the specification sentence on source-kind suspension to actual behaviour (N1).
5. Contention with more than two writers near the cap, confirming that busy errors surface as `OperationalError` and not as DENIED.
6. Deep nesting that survives `json.loads` but reaches jsonschema or other recursive paths inside `inspect_import`.

## Residual adoption limits

This remains a single-host synthetic reference with a very small budget: 128 events, 512 KiB, and no rollover. Every operation replays the full history under a lock, and the benchmark is one run, not an SLA. The documented one-bit inferences about identifiers, lineage and keys, plus the register-wide activity sequence, remain. Head and fence coordination, busy-error handling, bootstrap recovery, IAM, clock, evidence custody and latest-store ownership are host duties. The runtime is recorded but not locked.

Native and acceptance evidence depends on an unreviewed external toolchain. Research assurance remains reviewable-draft, the publication metadata is synthetic, and this verdict grants no publication authority. `review.json` and `review.md` are pending release bookkeeping, not acceptance.