# Scoped follow-up — genesis-receipt timing

**Verdict: ACCEPT WITH LIMITS**  
**Publication authority: not granted.**  
This reviews only the first-registration timing fix and the five appended regressions. It is not whole-package conformance and not permission to publish.

Claude’s prior **BLOCK** (metadata revision receipts laundering an old review) targeted the pre-fix source and is **closed here**. That BLOCK write-up stays preserved; this is not vote averaging.

---

## Input integrity

| Item | Status |
|---|---|
| Final sentinel `AP-FIRST-REGISTRATION-81` | present |
| Current `provenance.py` | complete (`END CODE`) |
| Fixture helpers | complete (`END HELPERS`) |
| Five appended tests | complete (`END TESTS`) |
| Contract paragraph | complete (`END CONTRACT`) |
| Claude finding | complete |

**Truncation this payload:** none of the supplied artifacts are cut.

**Not repeated here (scoped):** the other 76 tests, schema, native harness, full spec. Those were complete in the preceding compact pass. Claimed local result is now 81 tests + three native Dimensions; that run is not reproduced here. SHA-256 banners are producer labels.

Historical disclosure (unchanged): an earlier Grok attachment truncated ~17 064 characters of `test_provenance.py`. That cut is not present in this package.

---

## The defect and the fix

Claude’s BLOCK: both timing guards used `a['recordedAt']` — the receipt of the **pinned Activity revision**. A notes-only `correct` of the same Activity keeps anchors (actor, mode, interval, inputs, method) and only restamps receipt. That made an older review look “fresh.”

This source uses the identity-genesis receipt:

```text
review_at = prior[(a['id'], 1)]['recordedAt']
old.recordedAt < review_at          # first registered after previous assessment
each explicit basis.recordedAt ≤ review_at
```

Revision 1 of that Activity id is already in `prior` if `resolve(activity)` succeeded (genesis is always admitted first). Later notes-corrects append a new row; they do not change rev1 `recordedAt`. Contract wording now matches: “first registered (revision 1 receipt).”

`new_judgement` is unchanged: non-insufficient genesis, or a change to label / basis / activity. Correction still requires a **different Activity ID**. Current-active full closure and captured / non-mismatched Captures still apply. This proves **registration order only**, not live execution or evidence relevance.

---

## Claude’s three variants — closed

**Variant 1 — older alternate review + later notes.**  
`test_old_alternate_review_metadata_cannot_refresh_execution`: mint R2, admit A1 (still on R1), notes-correct R2, promote A1 → `supported` on `pin(R2′)`. `review_at` is R2 rev1, recorded **before** A1. Raises `first registered after`.

**Variant 2 — insufficient step back to original review.**  
`test_insufficient_roundtrip_cannot_reuse_old_execution`: A1 `limited`/R1 → `insufficient`/R2 → notes-correct R1 → `limited` on `pin(R1′)`. `review_at` is R1 rev1, recorded **before** the insufficient assessment. Raises `first registered after`.

**Variant 3 — genesis whose review precedes a later basis.**  
`test_review_metadata_cannot_move_registration_after_basis`: late capture after the original review, notes-correct that review, new assessment with `pin(R′)` and basis = late capture. `review_at` is original review rev1, recorded **before** the late capture. Raises `first registered before`.

**Positive (required so the fix is not over-narrow).**  
`test_genuinely_later_registered_review_can_be_metadata_corrected`: new review ID admitted after A1, then notes-correct, then A1 → `supported` on that current pin. `review_at` is the new ID’s rev1, after A1. Admits.

**Claude’s non-blocking test-precision note.**  
`test_current_mismatched_capture_guard_isolated`: a Capture created already `integrity='mismatched'` (current head, not a superseded rev1) is used as basis. Asserts `unavailable or mismatched capture`, not the stale-head message.

Reduce-to-insufficient and same label/basis/activity metadata still skip `new_judgement` and keep historical pins.

---

## Residuals (not this bug)

**H2 — host integration.** `admit` still validates the record before the writer grant and still returns the full ledger. Generic write-only receipts/errors remain a host wrapper. Unchanged.

**Declaration, not proof.** A writer with an Activity grant can still mint a new review ID by copying content. The contract already says registration order is all this checks.

**Explicit basis receipts only.** Timing does not walk every transitive Capture receipt. Matches the excerpt.

**Unchanged host duties:** authenticate actor; own latest complete root/config/clock; serialize updates; preparse byte cap; CPU budget; rollover planning; no PKI/fetch/legal/retention/disclosure/parent/production claim.

Independence remains an overlap signal (`known-shared-origin` vs `unknown`). `view` still does not evaluate truth or infer permissions.

---

**ACCEPT WITH LIMITS** on this exact genesis-receipt candidate.  
Variants 1–3 no longer admit. Do not treat that as publication authority or as proof of real-world review execution.
