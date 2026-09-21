# Scoped closure audit: EAP 0.1.0 genesis/basis-swap and fresh-review fixes

**Verdict: BLOCK on this exact candidate.** The fix is narrow and cheap. Everything else in scope looks acceptable with the stated limits.

## Input integrity

- **Truncation:** none observed. Both files end with their `END FILE` markers.
- **Test count:** I counted 76 test methods in `Tests`, numbered 1 `test_three_profiles` through 76 `test_canonical_encoding_control_and_unicode_vector`, plus the fixture helpers.
- **Contract excerpts:** received through `END EXCERPTS`.
- **Final sentinel:** `AP-CLOSURE-76-FULL-TESTS` received.
- **Not verified:** I executed nothing. I could not check the stated SHA-256 values or the reported 76 passes and native results.
- **Omitted context:** the schema, native harness and full contract were not re-read. This verdict does not ratify them.

## Blocking finding: fresh-review timing uses the revision receipt, so metadata revisions restore the bypass

In `semantic`, the two new timing guards compare against `a['recordedAt']`. That is the receipt of the pinned Activity *revision*, not of the review event:

```python
require(old is None or old['recordedAt']<a['recordedAt'], ...)
require(all(prior[...]['recordedAt']<=a['recordedAt'] for p in r['basis']), ...)
```

Activity anchors (actor, mode, times, inputs, method) cannot change on correction. So a metadata-only `correct` revision is the same registered event with a newer receipt. `test_review_metadata_revision_is_not_fresh_execution` states exactly this principle, but the code enforces it only when the review ID is the same.

**Variant 1: reassessment with an older alternate review.** This works directly on the `ai-team` fixture, using the same construction as `test_prior_review_cannot_reassess_later_judgement` plus one extra step:

1. Register review R2, then assessment A1 with activity R1.
2. Add `revision(R2, notes=[...])`, giving R2′ with a receipt later than A1.
3. Add `revision(A1, label='supported', activity=pin(R2′))`.

Every check passes: the IDs differ, R2′ is the current head, R2′ is recorded after A1, and the basis is recorded before R2′. It is accepted. A review registered before the previous judgement becomes "fresh" through a metadata edit.

**Variant 2: return to the original review through an insufficient step.**

1. A1 (limited, R1) → A2 (insufficient, R2). This is allowed because the label is insufficient.
2. Add R1′, a metadata revision of R1.
3. A3 (limited, R1′) passes, because the ID check compares only against A2's activity and R1′ is recorded after A2.

**Variant 3: genesis whose review precedes its basis.**

1. Register review R at t1 and capture C2 at t2.
2. Add R′, a metadata revision of R, at t3.
3. A new assessment with activity `pin(R′)` and basis `[pin(C2)]` passes the "before its evidence basis" check, even though the review event was registered before C2 existed.

**Impact:** The unchanged-label basis-swap and genesis closure checks do hold. But the same-Activity pseudo-fresh fix is only closed for a literally identical ID. The change's own claim that metadata revisions are not fresh execution does not hold.

**Minimal fix:** compare against the Activity identity's genesis receipt in both guards.

```python
review_at=prior[(a['id'],1)]['recordedAt']
require(old is None or old['recordedAt']<review_at, ...)
require(all(prior[(p['id'],p['revision'])]['recordedAt']<=review_at for p in r['basis']), ...)
```

This closes all three variants. A metadata-corrected review first registered after the previous assessment remains usable. A stricter alternative is to require `a['revision']==1` for any new judgement. Either way, update the contract wording from "recorded after" to "first registered (revision 1) after".

**Tests to add:**
- Variant 1 rejected.
- Variant 2 rejected.
- Variant 3 rejected.
- Positive case: a review first registered after A1, then metadata-corrected, is accepted for reassessment.

## Non-blocking findings (fix while re-cutting)

1. **Test precision on the capture rules.** `test_assessment_genesis_rejects_mismatched_basis`, `test_changed_judgement_rejects_transitive_stale_capture` and `test_changed_judgement_rejects_withdrawn_basis` use bare `assertRaises(p.Invalid)`. In each, the review's own closure reaches the superseded capture revision 1, so rejection comes from the stale-head rule. The "captured and not mismatched" rule on a *current* head is never exercised in isolation. Add a case where a capture is created at genesis with `integrity='mismatched'`, then used as basis, and assert on the `'unavailable or mismatched capture'` message.
2. **The Activity-ID rule is a declaration, not proof.** Any writer with an Activity grant can mint a new review ID by copying content, as `test_changed_judgement_positive` does. The contract already says execution is not verified. Keep saying that registration order is all this proves.

## Verified by reading (in scope)

- **new_judgement coverage:** the trigger covers genesis, label change (including supported → limited), basis swap and activity change. Reductions to insufficient and metadata-only corrections keep their retained pins, and view warnings remain.
- **Transitive closure:** the current-head, active and capture-state check is applied through the full closure, not just to immediate pins.
- **Pin field movement:** clearing `retained` means an existing pin moved to a different field counts as new.
- **Import/migrate/snapshot:** `import_snapshot`, `migrate` and `validate_snapshot` require keyword `now`, run `config_check` at that instant and bound inner receipts. The tests cover future receipts, expired configuration and a missing clock.
- **Encoding vector:** the hex matches sorted keys, the `\n` short escape, lowercase `\u0001` and raw U+2028/U+2029.
- **Fixture genesis:** the `ai-team` fixture assessment (limited, current closure, basis recorded before review) is a valid positive genesis under the new rules.

## Unchanged residuals

These remain as you stated: an authenticated actor, and a host-owned latest root, config and clock with serialized updates; generic write-only errors; a byte cap before parsing; a CPU budget (every `admit` revalidates the whole ledger); rollover planning; and the deferred PKI, fetch, legal, retention, disclosure and production/parent conformance work. No execution, web or publication authorization is implied.
