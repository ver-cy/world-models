END OF TEST SUPPLEMENT is visible. This is a review of the previously unread tests against the already-accepted 0.1.0 companion. No execution. Implementation, schema, spec, and native acceptance are unchanged.

# Supplemental test review

53 `test_*` methods. That matches the frozen `test-results.json` count. `schema_negatives` / `graph_negatives` are single methods with subtests.

## Previously unread cases

**Successor writer (`test_rotated_source_writer_can_retract`).** Governor correction replaces source-`a` writers with `urn:synthetic:new-writer`. That writer retracts `observation:1` (`change=retraction`, `state=retracted`). Current evaluate is `preferred` because source-`b` / `B` remains. `observations[0].writer` is still the original `W`. Matches M3: writer is per-revision attribution; source stays fixed; prior attribution survives.

**Closure (`test_closure_cannot_change_accountable`, `test_transfer_preserves_valid_history`).** Closure plus a new `accountable` is rejected. Transfer now closes the old term (`change=closure`, clipped part ends) and mints a successor authority with new part ids. Query at `NOW` keeps `urn:synthetic:owner`; query at `cutoff` names the successor. Matches M5: closure may only shorten the end.

**Extension (`test_restamped_retry`, `test_snapshot_truncation`, `test_snapshot_rewrite`, `test_snapshot_extension`).** Restamp-only retry returns the original ledger and receipt. A truncated candidate can still pass `validate_ledger` and still fail `validate_extension` against the fuller previous snapshot. In-place rewrite of a historical row fails extension. An `admit` append passes extension. Matches M1/M2 and adoption-limit 1: extension does not prove the supplied previous root is current.

**Retention / negatives.** `test_no_authority_retains_evidence` is the missing half of `test_no_authority`: empty authorities → `unknown` with both observation ids and both evidence refs, no selected value. `test_part_is_not_party` rejects a stewardship id equal to its party. Denied still matches `^Read denied$` on a garbage ledger. Graph/schema negatives still reject broken digests, mutated anchors, part-party/source edits, part interval outside the authority, and part id colliding with the record id.

No test in this file invents a selected value on unknown or contested authority. No test treats envelope operator or parent 001 as domain precedence.

## Coverage holes (disclosed, not defects)

Adoption-limits 2 and 3 are not unit-tested: closure that would clip a part to an empty interval, and revival of a retracted row by explicit correction. Limit 1 is tested only in the reject direction; `validate_extension(x, x)` is not asserted and must not be treated as a currency proof. Those are documentation, not hidden behavior.

## Verdict

**ACCEPT WITH LIMITS — unchanged.**

The unread tests confirm the remediations they were written for. They do not reopen B1/B2 and they do not add rights. Adoption-limits.md 1–8 stay as host/publication deferrals. This is not publication authorization.
