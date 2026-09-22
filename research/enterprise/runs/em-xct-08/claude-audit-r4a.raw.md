# EM-XCT-08 R4a: Addendum Review

**Verdict: ACCEPT WITH LIMITS.** R4a closes the N1 documentation contradiction, turns N3 into a documented host duty, and adds tests for the N4 gap. The executable build is unchanged and I found no new issue. The R4 disposition stands, and nothing in this addendum raises its severity.

## Input confirmation

The final marker `SYNC-R4A-FINAL-20260922` is visible. The inputs I reviewed are:
- The R3 baseline bodies (30), still accessible in this conversation.
- The complete R4 patch.
- This addendum, which contains: the complete `model-spec.md` diff, the complete `test_sync.py` diff (three methods), exhaustive scalar replacements for `spec.json`, and full bodies for `test-results.json` and `acceptance-results.json`.

For the `spec.json` `model.scope` field, the addendum gives a reconstruction rule (R4 scope plus the `model-spec.md` diff) instead of a recopied body. The text is fully determined by what I have, but byte equality with `model-spec.md` is the author's claim, not something I checked.

The inventory is consistent with that list: exactly the five named files change, `sync_register.py`, `sync.schema.json`, the fixtures, the examples, the worker, acceptance and benchmark keep their R4 hashes, and `buildId b782bbca…` is unchanged. The 8 hash-only files and the external toolchain remain outside body review. This was static, no-tools review; the reports are author evidence only.

## N1: source-kind contradiction — CLOSED

The new `model-spec.md` sentence limits `active-pin-suspended` to catalogue reclassification or validity-window misses within the same immutable scope. A changed source-kind interpretation now requires a new scope and yields `unmapped`. That matches the R4 code: `mapping_outcome` filters to the receiving scope, and `test_source_kind_change_cannot_reuse_mapping` asserts `unmapped`.

The four `spec.json` replacements cover every occurrence of the old SS-F10 string that I can find in the R3/R4 body:
- the SS-F10 description;
- `answer_data[0]` for SS-Q19;
- `answer_data[0]` for SS-Q20;
- the SS-A10 artifact name.

The JSON paths resolve correctly: `bundles/1` is SS-B2, `layers/1` is SS-B2-L2, and `findings/1` is SS-F10. No other supplied document asserts kind-based suspension. The now-unreachable `sourceObjectKind` comparison stays in the code; the author discloses it, it has no reachable effect, and I don't treat it as an issue.

## N3: shared page slots — DOCUMENTED

The new "Shared-round coordination" paragraph states the following:
- Intake grantees can append nonterminal pages and force an errored, incomplete close.
- Page slots can be displaced by other contributors.
- The attester must review the full admitted page set before a terminal page and an error-free seal.
- The reference neither reserves page ownership nor proves that this review happened.

This matches the code and places the duty on the host.

## N4 and related tests — present and sound on reading

**`test_scope_b_only_principal_cannot_probe_or_move_scope_a_claim`.** Policy revision 2 grants WRITER rights in scope B only. I traced these results through the R4 code:
- A mapping-ID collision returns DENIED from the `existing` scope/purpose check.
- A round-ID collision passes the attest gate in scope B, then returns DENIED from the foreign `existing` check.
- Retracting `mapping:1` returns DENIED because `mapping-state` authorizes against scope A.
- Activating the fresh scope-B claim returns DENIED from the foreign active-lineage check. Both scopes share source, resource and scheme, so the lineage is identical.
- The scope-B commit yields `{'status':'unmapped','pin':None}`.
- The archive is unchanged after each DENIED.

**`test_exact_terminal_retry_after_attestation_revocation_keeps_ack`.** After revocation, the exact retry returns the original acknowledgement through the slot lookup with no event, and the error-free seal returns DENIED from the attest gate. Both match the code.

**`test_shared_nonterminal_page_and_intake_error_close_are_incomplete`.** OTHER's nonterminal page 0 is admitted. WRITER's planned page 0 raises `Invalid('page chain gap')` and rolls back. OTHER's errored seal gives `complete=False`, and `assess_rounds` returns `insufficient-context`. All match the code.

## Report consistency (author evidence)

- `test-results.json` shows 101 tests, which is 98 plus the 3 new names, all listed.
- The `test_sync.py` digest in `test-results.json` (`d270…`) matches the inventory, and the runtime digests are unchanged.
- `acceptance-results.json` pins the revised spec digest `8dbb…` (matching the inventory), with `buildId` and example digests unchanged.
- The benchmark is correctly not rerun and applies only to its unchanged inputs.

## Residual adoption limits (unchanged from R4)

- Single-host synthetic reference with a 128-event / 512 KiB budget, full replay under a lock, and no rollover. The benchmark is one run, not an SLA.
- Documented one-bit inferences on IDs, lineage and keys, plus register-wide activity exposure through receipt IDs.
- A non-empty partial bootstrap may raise a raw SQLite operational error. There is no automatic recovery.
- The trusted-clock check still runs before authorization.
- Review of shared pages is an attester and host duty.
- No latency promise beyond two writers, and no broader recursive-parser assurance.
- Host duties remain for IAM, clock, evidence custody, latest-store ownership, and head/fence coordination.
- Runtime versions are recorded but not locked.
- Native evidence depends on the unreviewed external toolchain.
- Research assurance remains reviewable-draft, and the publication metadata is synthetic. This verdict does not authorize publication.