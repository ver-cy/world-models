# Scoped closure audit — Enterprise Assertion Provenance 0.1.0

**Verdict: ACCEPT WITH LIMITS**  
**Publication authority: not granted.**  
This is a scoped review of the supplied code, all 76 tests, and the contract excerpts. It is not a new global conformance claim and not permission to publish.

Earlier Claude and Grok verdicts stay as written. The previous Grok follow-up that lost ~17 064 characters of `test_provenance.py` remains disclosed below; this package is the repair of that cut.

---

## Completeness and truncation

| Item | This payload |
|---|---|
| Final sentinel `AP-CLOSURE-76-FULL-TESTS` | present |
| `provenance.py` | complete (no mid-file cut) |
| `test_provenance.py` | **complete in this payload** |
| Schema, native harness, AGENTS, full `model-spec.md` | not repeated (per instructions) |
| Contract excerpts | present |

**Prior truncation (preserved):** the previous Grok attachment cut `test_provenance.py` inside `test_shared_origin_not_independence` with `(truncated 17064 characters)`. That pass could not name all tests. **This file has no such marker.** It runs from helpers through `test_canonical_encoding_control_and_unicode_vector` and `__main__`.

**Counted here: 76 `test_*` methods** (not executed).

1–62: prior suite, including historical-pin metadata, reduce-to-insufficient, import `now`, snapshot digest, encoding cap.  
63–76:

- `test_changed_judgement_needs_fresh_review`
- `test_changed_judgement_positive`
- `test_changed_judgement_rejects_withdrawn_basis`
- `test_changed_judgement_rejects_transitive_stale_capture`
- `test_retained_pin_cannot_change_field`
- `test_import_future_receipt_rejected`
- `test_import_requires_host_clock`
- `test_assessment_genesis_rejects_mismatched_basis`
- `test_basis_swap_needs_new_review_identity`
- `test_review_metadata_revision_is_not_fresh_execution`
- `test_genesis_review_cannot_precede_basis_receipt`
- `test_prior_review_cannot_reassess_later_judgement`
- `test_expired_import_configuration_rejected`
- `test_canonical_encoding_control_and_unicode_vector`

Helpers present: `config`, `empty`, `stamp`, `row`, `capture`, `activity`, `account`, `link`, `add`, `revision`, `fixture`, `view`.  
Reported local result “76 tests + three native Dimensions pass” is not reproduced here.

Omitted by design and not re-ratified: schema bytes, `acceptance.py`, `AGENTS.md`, full spec tree, examples, tool-pins, upstream. SHA-256 banners are producer labels.

---

## The two leftover holes — closed in this source

### 1. Genesis / basis-swap quality asymmetry

```text
new_judgement =
  kind == ConfidenceAssessment
  and label != 'insufficient'
  and (old is None or label/basis/activity changed)
```

When `new_judgement` is true, retained pins are cleared and the closure walk requires every pin to be the current **active** head and every cited Capture to be `captured` with `integrity != mismatched`.

That now applies to:

- **genesis** of `supported` / `limited` (`old is None`) — `test_assessment_genesis_rejects_mismatched_basis`
- **unchanged-label basis swap** — `test_basis_swap_needs_new_review_identity`

`insufficient` genesis and reduction to `insufficient` do not take this path. That matches the excerpt.

### 2. Same-Activity-ID pseudo-fresh review

On a correction, the code requires **`r['activity']['id'] != old['activity']['id']`**, not merely a new pin/revision of the same review.

A notes-only correction of the existing review Activity produces a new pin but the **same ID**, and is rejected (`test_review_metadata_revision_is_not_fresh_execution`). Changing the label to `supported` on the old review pin is rejected (`test_changed_judgement_needs_fresh_review`). A new review ID recorded after the previous assessment, with current non-mismatched basis, admits (`test_changed_judgement_positive`).

Also enforced when `new_judgement`:

- previous assessment `recordedAt` < review Activity `recordedAt`
- each **explicit** basis row `recordedAt` ≤ review `recordedAt`

Covered by `test_genesis_review_cannot_precede_basis_receipt` and `test_prior_review_cannot_reassess_later_judgement`. Receipt order is recorder time, not authenticated real-world execution (excerpt).

Withdrawn or later-mismatched Capture in the judgement closure still fails (`test_changed_judgement_rejects_withdrawn_basis`, `test_changed_judgement_rejects_transitive_stale_capture`).

Metadata-only corrections that keep `label`, `basis`, and `activity`, and reductions to `insufficient`, still keep historical pins and view warnings (`test_correct_unchanged_historical_dependencies`, `test_correct_assessment_after_account_correction`). Moving a stale pin into `basis` on a reduction is still a new reference and needs a current head (`test_retained_pin_cannot_change_field`).

Evidence relevance and live execution remain assessor/host declarations. The walk does not invent verification or truth.

---

## Import configuration at trusted `now`

`import_snapshot` and `validate_snapshot` now call `config_check(config, now)` before ledger checks. Expired `now` is `Denied` (`test_expired_import_configuration_rejected`).

`test_import_future_receipt_rejected` still shows the intended split: offline `validate_ledger` without `now` may accept a structural future receipt; `import_snapshot` / `migrate` / `validate_extension(..., now=)` / `validate_snapshot` reject it (`Receipt follows trusted now`). Keyword `now` remains mandatory on import (`test_import_requires_host_clock`).

Encoding control/Unicode vector is present and asserted against the excerpt hex (`test_canonical_encoding_control_and_unicode_vector`). Not recomputed here.

---

## What still holds

Under trusted-host auth, current complete root/config, clock, and no concurrent writes:

- Exact local revision/digest pins; independent anchors; append-only terminal withdrawal
- Five epistemic kinds stay distinct; review does not rewrite `inferred` → `observed`
- `view` gates before ledger diagnostics; `truth` / `permissions` stay `not-evaluated` / `not-inferred`
- Labels remain purpose-qualified qualitative judgement, not probability
- Companion does not impersonate a parent model

I01–I16 hold under those assumptions.

---

## Remaining limits (not regressions of this fix)

**H2 — host integration (unchanged).** `admit` still schema-validates before the writer grant and still returns the full ledger. Unauthorized malformed writes can distinguish `Invalid` from `Denied` if the host forwards exceptions. Spec/AGENTS still require a generic write-only receipt or error. That wrapper is not in this library.

**M1.** Independence is still `known-shared-origin` vs `unknown` from cited historical digest/originRef. Overlap signal only.

**LOW / documented host duties**

- Review-vs-basis ordering uses **explicit** basis receipts, not every transitive Capture receipt (matches the excerpt).
- 8 MiB cap is on `encode()` after parse; admit may be quadratic; 10 000 / 8 MiB are not throughput claims.
- Offline `validate_ledger` / `validate_extension` without `now` are consistency only.
- Native V3 remains a separate envelope check.
- No IAM, fetch, PKI, retention, fine-grained disclosure, legal/parent, or production-volume claim.

Host must still: authenticate the actor; own the latest complete root/config/clock; serialize updates; wrap `admit`; preparse; budget CPU; plan rollover.

---

**ACCEPT WITH LIMITS** on this exact candidate.  
Genesis/basis-swap quality and same-review-ID bypasses are closed in the supplied source and in the 76 named tests. Do not treat that as publication authority or as a substitute for the host wrapper around `admit()`.
