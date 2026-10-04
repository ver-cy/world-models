# Scoped audit: EAP 0.1.0 genesis-receipt fix

**Verdict: ACCEPT WITH LIMITS.** The fix closes all three variants from the preceding BLOCK. I found no new laundering path that the per-identity contract does not already disclose.

## Input integrity

- **Truncation:** none observed. `END CODE`, `END HELPERS`, `END TESTS` and `END CONTRACT` are all present.
- **Final sentinel:** `AP-FIRST-REGISTRATION-81` received.
- **Tests:** I counted exactly five appended tests.
- **Not verified:** I executed nothing. I did not check the SHA-256 value, the 81 passes or the three native Dimensions.
- **Not re-read:** the other 76 tests, the schema and the harness were not supplied this time. This verdict does not re-ratify them or claim whole-package conformance.

## The fix, checked against each variant

`review_at=prior[(a['id'],1)]['recordedAt']` always resolves. Revision chains start at 1, and `a` has already been resolved from `prior`. Both guards now use this genesis receipt, so a `correct` revision of an Activity can no longer move it.

| Variant | Why it is now rejected |
|---|---|
| 1. Older alternate review, metadata-corrected after A1 | R2's genesis precedes A1, so Guard 1 fails |
| 2. Insufficient round-trip back to R1′ | R1's genesis precedes A2, the immediate previous revision, so Guard 1 fails |
| 3. Genesis with a review registered before its basis | The basis receipt is later than R's genesis, so the basis guard fails |

- **Equality edges:** receipts strictly increase ledger-wide, so `<` versus `<=` can only matter for the same row. The basis types exclude Activity, so that cannot happen.
- **Contract wording:** the paragraph now says "first registered (revision 1 receipt) after" and "no earlier than its explicit basis revisions". This matches the code exactly.

## The five regressions

I traced each test by reading.

1. **`old_alternate_review_metadata_cannot_refresh_execution`**
   - Every earlier check passes: the IDs differ, the closure is current, and the actor, method and account are in the inputs.
   - Guard 1 fires first, so the regex `first registered after` targets the right rule.
2. **`insufficient_roundtrip_cannot_reuse_old_execution`**
   - The insufficient step is not a new judgement, and its new `activity` pin to r2 is current.
   - The final step fails only on Guard 1.
3. **`review_metadata_cannot_move_registration_after_basis`**
   - This is a genesis case, so Guard 1 is skipped. The closure is current.
   - The basis guard fires, and `first registered before` matches its message.
4. **`genuinely_later_registered_review_can_be_metadata_corrected`**
   - This is a valid positive case: A1's receipt is earlier than new-review's genesis, and the basis receipt is earlier still.
   - The assertion on the single assessment's label is sound.
5. **`current_mismatched_capture_guard_isolated`**
   - This closes the precision gap I raised earlier.
   - The capture is a current, active genesis row, and a capture with `captured` + `mismatched` passes the capture rules.
   - Every other closure node is current, so only the capture-state rule can fire. The regex confirms it.

## Residuals (non-blocking; document them)

1. **Identity rotation.** Guard 1 applies per assessment identity. A writer can withdraw A1, or leave it active, and create a new assessment ID that reuses the old review R1 with a stronger label. This passes because genesis only checks review-after-basis.
   - This conforms to the contract, which scopes freshness to "such a correction".
   - It adds no power beyond the already-disclosed ability to mint a fresh review ID by copying content.
   - The contract should state it explicitly: freshness is enforced per assessment identity. Parallel or successor assessments may cite any review first registered no earlier than their basis. The view surfaces them side by side.
2. **Conservative false rejections, not holes:**
   - Guard 1 compares against the immediate previous assessment revision, so a metadata-only correction of A resets the bar. A review registered between A1 and A1′ can no longer be used for a label change.
   - Correcting a basis capture after the review's genesis forces a new review.
   - Re-pinning to a metadata-corrected revision of the *same* review, with the label unchanged, is rejected by the ID rule.
   - All three are acceptable. Say so if users will hit them.
3. **Uncovered positive case (optional test):** a genesis assessment citing a metadata-corrected review whose revision 1 is at or after its basis.
4. **Unchanged from before:**
   - The rules prove registration order only. They do not prove real-world execution, evidence relevance or truth.
   - The host still owns authentication, the current root, config, clock and serialized concurrency, and returns only generic write-only receipts and errors.
   - Still open: the byte cap before parsing, the CPU budget for full revalidation on each `admit`, rollover, and the deferred PKI, fetch, legal, retention, disclosure and production/parent conformance work.

This grants no execution, web or publication authorization.
