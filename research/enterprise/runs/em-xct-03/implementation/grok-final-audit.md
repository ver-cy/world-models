# Final follow-up audit — Enterprise Assertion Provenance 0.1.0

**Verdict: ACCEPT WITH LIMITS**  
**Publication authority: not granted.**  
This is a bounded trusted-host draft. It is not permission to publish, and not parent / PROV / SLSA / full-enterprise-production conformance.

Preceding audits stay as written (initial BLOCK elsewhere; two Grok ACCEPT WITH LIMITS passes). This disposition applies only to **this** source.

---

## Completeness, sentinel, truncation

| Item | Status |
|---|---|
| Final sentinel `AP-FINAL-69-HOST-CLOCK-FIELD-PINS` | present |
| `provenance.py`, `provenance.schema.json`, `model-spec.md`, `AGENTS.md`, `acceptance.py`, `requirements.txt` | present, not mid-file truncated |
| `test_provenance.py` | **truncated** |

**Truncation (must not be papered over):** `test_provenance.py` is cut inside `test_shared_origin_not_independence` with `(truncated 17064 characters)` and resumes at a `validate_snapshot` / `trusted now` assertion plus `test_import_requires_host_clock`. This audit **cannot** independently name or trace all 69 method bodies. The claim “69 tests pass” is taken as a local-execution report, not reproduced here.

**Not in this payload / not independently reviewed:** `examples/*.json`, `tool-pins.json`, upstream bytes, `spec.json` tree (including the stated AP-ACT05 clarification), other spec.json fields, `runtime-model.reference.json`, `test-results.json`, whole-object facets. SHA-256 banners are producer labels, not recomputed.

---

## New rules — present in code and contract

These are implemented, not only described.

**1. Field-keyed retained pins (closes role-swap)**  
`ref_slots()` groups pins by field (`inputs`, `activity`, `evidence`, `account`, `basis`). Retention is `{(field, encode(p))}`. `resolve` treats a pin as current-head-required when `(field, encode(p))` is not in that set. Same bytes moved to another field are a **new** reference. Matches: “A pin moved to a different field is a new reference, even if its bytes were already present elsewhere.”

**2. Label promotion vs metadata / reduction**  
`new_judgement` holds only when all of: there is a previous row, kind is `ConfidenceAssessment`, `label` changed, and the new label is not `insufficient`. Then:

- retained set is cleared
- `activity` pin must differ from the previous activity pin
- every immediate and transitive pin must equal the current **active** head
- a cited Capture must be `availability==captured` and `integrity!='mismatched'`

Reducing a label to `insufficient`, or keeping the label and editing notes/limitations, still keeps historical pins. View still reports `requiresReview` / `sourceGaps`. The extra walk does **not** certify the new judgement or proposition truth.

**3. Mandatory import clock (closes future-receipt import)**  
`import_snapshot`, `migrate`, and `validate_snapshot` take keyword-only `now`. `validate_ledger(..., now)` rejects any `recordedAt > now` (`Receipt follows trusted now`). `admit` and `view` always pass `now`. `validate_ledger` / `validate_extension` may omit `now` for offline consistency only. Visible tail: `test_import_requires_host_clock` expects `TypeError` if `now` is omitted; the resumed snapshot test expects `Invalid` / `trusted now`.

**4. Snapshot identity**  
Successor `factId` must differ from previous. Previous `recordType` must be `fact`.

**5. Contract alignments that remove older spec/code splits**

- File-acquisition / live-observation: “one or more inputs, all matching captured Captures.” Former M3 tightness is now the written rule, not a leftover mismatch.
- Digests use named **vercy-python-json-v1** (`json.dumps(..., sort_keys=True, separators=(',',':'), ensure_ascii=False, allow_nan=False).encode('utf-8')`). Explicitly not RFC 8785.
- Inputs are a retrospective recorder account, not proof of actor knowledge at `endedAt`.
- Independence uses **historically pinned** Capture digest/originRef; corrected origin is not substituted.
- Quadratic admit cost, 10 000-record / 8 MiB ceilings, deferred rollover: documented as not production capacity.

Prior remediations remain in this source: unchanged same-field historical pins on metadata correction; no same-id transitive self-derivation; ASCII+calendar instants; `type(v) is int` revisions; `encode()` prefix/replay; `currentCaptureState`; scheme id/revision from the embedded object; uniform `Read denied` for config-window denial on `view`.

I01–I16 still hold under the stated host assumptions (authenticate caller, supply complete current root/config and clock, no concurrent mutation). `view` still emits `truth: "not-evaluated"` and `permissions: "not-inferred"`. Review still does not rewrite `inferred` → `observed`. Reader gate still runs before ledger diagnostics. Companion id remains `vr.profile.enterprise-assertion-provenance` (no parent impersonation).

---

## Remaining defects (this candidate)

### HIGH — host API, not an I-invariant break

**H2. `admit()` still validates the record before the writer grant and still returns the full ledger.**

Order is unchanged: `config_check` → kind → `validate(record)` → grant → `recordedAt == now`. An unauthorized malformed write can still surface `Invalid` rather than `Denied` if the host forwards exceptions. The function still returns `candidate` / `previous`.

This is a **host integration requirement**, not a missing companion invariant. Spec and AGENTS already say: return only a receipt or a generic rejection to write-only callers. The library does not wrap that. I11 still holds on `view` (gate first).

### MEDIUM

**M1. Independence is still only an overlap signal.**  
`known-shared-origin` vs `unknown`. The group fixture still shares the default digest and `originRef` and only changes `sourceRef`. The new paragraph correctly uses historical cited origin/bytes and does not treat that as independence proof. Easy to over-read.

**M-genesis-quality.** The extra current-head + captured/non-mismatched walk runs only on **label change** (`old is not None`). A *new* `ConfidenceAssessment` with label `supported` or `limited` may pin a current mismatched or unavailable Capture as basis. `resolve` only demands current active head and type. `view` still emits `sourceGaps` / `requiresReview` and does not evaluate truth. The contract sentence is under correction (“Any other label change…”), so this is an unstated genesis asymmetry, not an I10 collapse (judgement quality remains external).

**M-promo-same-id.** `new_judgement` only requires `r['activity'] != old['activity']` (pin inequality). A notes-correction of the **same** review Activity id produces a new pin (digest includes notes/revision) while `inputs` / actor / mode / interval stay anchors. That satisfies the code and still runs the current+active+non-mismatched walk. The spec sentence is “different review Activity” / “a new execution gets a new ID.” The library does not demand a new Activity id. Promotion over withdrawn or mismatched basis remains rejected.

### LOW — documented bounds, not missing invariants

- Unauthorized + malformed `now` still raises `Invalid` from `instant()`; only config-window `Denied` is remapped to `Read denied`. Trusted-host clock.
- Omitting `now` on `validate_ledger` / `validate_extension` is consistency only: it does not authenticate a root or reject future receipts.
- `validate_snapshot` is companion pin/lineage only. Native V3 remains separate. Latest-root discovery remains the host’s.
- 8 MiB cap is on `encode()` after parse. `load()` has no byte cap. Admit may be quadratic in history length. Host must preparse, budget CPU, and plan archive/rollover before the ceilings.
- `context-available` includes `proposed`. Not a rely verdict.
- URIs are opaque; no normalize/alias merge.
- `requirements.txt` pins `jsonschema==4.26.0` plus RFC 3339/3986 format validators. Format-checker presence is still fail-closed in code.
- acceptance still stamps `publicationStatus: "published"` with `researchAssurance: "reviewable-draft"`. Synthetic candidate-installation metadata only.

---

## Host requirements (explicit; do not treat as implemented here)

The companion assumes, and does not provide:

1. Caller authentication  
2. The complete current register root and configuration  
3. A trusted receipt/`now` clock  
4. Exclusion of concurrent mutation  
5. Generic write-only receipts/errors (do not forward `admit`’s ledger or raw `Invalid`/`Denied` text)  
6. Preparse byte limits and an execution budget  
7. Passing keyword `now` into import / migrate / `validate_snapshot`, then native V3 on the envelope  
8. Treating offline `validate_*` without `now` as consistency only  

If those are missing, this reference is not a public service.

---

## Tests and native harness (traced, not executed)

Visible in this payload: fixture helpers; start of the original suite through the truncated `test_shared_origin_not_independence`; tail `validate_snapshot(..., now=NOW)` future-receipt reject; `test_import_requires_host_clock`.  
Reported locally, not verified here: 69 tests; three native new-Dimension profiles; snapshot digest tamper; nested malformed value companion-rejected while native stays valid; truncation rejected.

`acceptance.py` now passes `now='2026-09-21T12:00:00Z'` into `validate_snapshot`. It still calls `validate_extension` without `now` (allowed offline consistency). Distinct per-profile dimension URIs and package-local upstream `sourceUrl` remain.

---

**ACCEPT WITH LIMITS** on this exact revised candidate.  
Field-keyed retention, promotion-over-bad-basis on correction, and mandatory import `now` are in the source. Do not treat that as publication authority, as a truth engine, or as a substitute for the host wrapper around `admit()`.
