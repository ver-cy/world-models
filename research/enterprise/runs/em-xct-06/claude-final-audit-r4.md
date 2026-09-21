**Verdict: ACCEPT WITH LIMITS.** This covers a bounded, reviewable-draft, synthetic-fixture companion only. It is not publication authority, and it makes no claim about source truth, host authority, production scale or current-state validity.

I found no critical or high defect in the arithmetic, the replay/digest seal, the immutable merge or the native binding. The two medium findings (M1, M2) are documentation-sufficiency gaps that need no code change. They should be fixed before freeze or carried explicitly as listed limits. Everything below comes from reading the supplied text. I executed nothing and verified no hash. Every digest, pin, test report and provider/toolchain statement remains a supplied assertion.

---

## 1. Defects

### M1: Medium. Residual host duties are not reachable from the agent contract
- **Where:** `AGENTS.md` / `agent-guide.md` reading list, `model-spec.md`, `final-review-limits.md`.
- **Problem:** The agent contract names exactly four documents to read: model-spec, adoption-limits, spec.json and the schema. Several binding host duties exist only in `final-review-limits.md`, which is neither named nor installed:
  - escaping control/bidi characters in `revision`/`edition`/`amountRole` for display;
  - binding `provenance.source` to the master system;
  - the rule that `allowed_issuers` in `validate_native` means current *inspection* authorization, not write admission;
  - the rule that a future `valuationAt` is accepted for every purpose.
- **Counterexample:** An agent follows AGENTS.md exactly and reads the installed `spec.json`, whose scope equals model-spec. It sees "Future valuationAt is allowed for an estimate" and infers that reconciliation receipts are refused for future dates. The code (`compute`) accepts them. The same agent also passes a write-admission set to `validate_native` for historical reads.
- **Fix:** Fold these residual duties into `model-spec.md` (and so into `spec.json` scope) and the bounded native/storage contract. Alternatively, add `final-review-limits.md` to the AGENTS reading list. Correct the "for an estimate" sentence. None of this changes output.

### M2: Medium. The digest preimage encoding is not normatively specified
- **Where:** `monetary.py` `canonical`/`digest`, and model-spec "local deterministic encoding".
- **Problem:** The receipt identity (predecessor pins, `native_fact_id`, the golden digests) depends on Python's `json.dumps(sort_keys, separators, ensure_ascii=False)` byte rules:
  - code-point key order;
  - `\u00XX` versus short escapes for controls;
  - U+007F and U+2028 left unescaped.

  Free-text fields (`revision`, `edition`, `amountRole`, `correctionReason`) admit arbitrary Unicode. A conforming non-Python verifier cannot recompute a digest from the documents alone.
- **Counterexample:** `correctionReason` contains U+007F or a C0 control. A JCS/RFC 8785 or JS verifier produces different bytes and rejects a valid pin, or its own pins fail here.
- **Fix:** State the exact byte rules normatively, or say explicitly that `monetary.py` 0.1.0 is the only defined verifier and cross-implementation verification is unsupported. Optionally add a test vector with control and non-BMP characters. The implementation stays the same.

### Low findings
| # | Where | Issue / counterexample | Fix |
|---|---|---|---|
| L1 | `validate_native` (`native-object-time`) | Object and fact `recordedAt` must be *identical*. A host that appends the object, then the fact one second later, is rejected. This is not stated in `bindings/native-v3.md`. | Document it as a binding requirement, or relax it to fact ≥ object. |
| L2 | `validate_native` (`native-master`) | `authority` must equal exactly `{'source':writer,'rank':0}`. A real host's rank or extra keys are refused, and no rationale is given. | Document it or parameterize it. |
| L3 | `load` | `1e400` parses to `inf` silently. It is rejected later by `bounded` as `unsupported-json-type`, so the "rejects non-finite" claim in load is slightly broader than the behavior. | Add `parse_float` or `parse_int` guards, or reword the claim. |
| L4 | `compute` | Two different slot IDs with the same source digest are not flagged. This is a likely double count if the digest preimage is slot bytes. | Document it as a host check (optional warning). |
| L5 | `import_receipts` | A correction may be content-identical to its predecessor, or may change currency, context or purpose. The spec is silent on whether that is intended. | State the intended scope of what a correction may change. |
| L6 | `import_receipts` + retention | Revoking a compromised issuer from the *existing* set, or lawfully erasing a referenced predecessor, makes the complete register permanently unimportable. There is no quarantine or tombstone path. "No tombstone" is documented, but this consequence is not. | Spell out the consequence in adoption-limits. |
| L7 | `audit-reconciliation.md` R2 | Still says "installed schema tamper test". `final-review-limits.md` correctly says it is a temporary sibling copy. | Add a superseded note. |
| L8 | `mastership-and-rights.yaml`, `whole-object-coverage.yaml` | Templated rows. The currency catalogue gets writer "authenticated host-authorized actor", which implies the host writes the steward's catalogue. `Rational`/`ReferencePin` get "inherited receipt source and policy context". | Give per-row semantics, or mark them templated. |
| L9 | `spec.json` MC-Q13 | Kind `local-guidance`, but the answer requires complete-register import and host storage. | Change it to `mixed-guidance`. |
| L10 | `acceptance.py` negatives | Rejection cases mutate the *constructed* fact, not the stored `saved` bytes. The positive path does use stored bytes. | Mutate the stored readback. |
| L11 | `fixed` | Error code `nonfinite-result` is misnamed (it means a non-integral scaled value) and is unreachable. | Rename it; this is cosmetic. |
| L12 | `acceptance.py` tool pin check | Hashes source files only. Transitive imports, `__pycache__` and jsonschema are not hash-pinned (the last is acknowledged). | Document it. |

---

## 2. Adversarial checks that held

- **Decimal signs and ties (`round_units`).** All five modes are mathematically correct for negatives: floor is `num//d`, ceiling is `-((-num)//d)`, and half modes use `abs` then re-sign. Output negative zero normalizes in `fixed`. Input negative zero is refused. Half-even ties to an even *increment count*, not an even last digit, and this is stated.
- **Hand replay of the examples.**
  - startup: 0.495 per-item becomes 0.50 each, total 1.50, residual −3/200. After-sum gives 1.48.
  - matrix: −1.025 becomes −1.02 and 2.075 becomes 2.08, total 1.06, residual −1/100. After-sum gives 1.05.
  - ai: 1000000000000000.00, residual 1/500000.

  All match the files and the acceptance report.
- **Stages.** Per-item quantizes each input and sums. After-sum uses a single `@total` step. `@total` cannot collide with the Input key grammar. `inexact` survives cancellation, and this is tested.
- **Precision limits.** Output is at most 57 digits: sum < 256·10³⁶ gives at most 39 integer digits, plus at most 18 places. The Rational bound of 80 digits and the 64-character string bounds are never reached. Non-terminating quotients (e.g. increment `0.03`) are correct under Fraction, but untested because the Decimal oracle only uses terminating increments. This is acknowledged.
- **Same currency, different context.** The full currency tuple, the full context and the policy currency are compared by exact string equality. This fails closed on whitespace or homoglyph variation. Equal strings with different meaning remain a host duty.
- **Source-slot identity.** Uniqueness is by `source.id`, so the same slot at a different revision is also refused. That is fail-safe.
- **Immutable correction.** `import_receipts` checks, in order:
  - same-ID conflict;
  - exact digest pin;
  - subject and issuer continuity;
  - nondecreasing `computedAt`;
  - transitive closure.

  A digest cycle is infeasible, and the loop check is defensive.
- **Rehash tampering.** A rehashed *wrong* result fails replay. A rehash with *valid* arithmetic on a leaf (changed inputs, recomputed result, digest and factId) passes `validate`, `validate_native` and import. The object record ID binds only dimension and ID. This is documented ("trusted prior snapshot"), but adopters should understand it as the dominant integrity limit.
- **Version refusal.** Schema consts on receipt and request, native envelope pinned to `1.0.0`, embedded schema digest.
- **Native outer versus nested.** The acceptance design correctly demonstrates `outerAloneAcceptsBadArithmetic: true` alongside exact-code nested rejection.
- **Claims versus tests.**
  - 32 tests counted.
  - 202 oracle comparisons (200 + 2) reconcile.
  - Golden pins equal the declared example hashes.
  - Report source digests equal the declared file hashes.
  - The acceptance negative list order matches the code's check order.

---

## 3. Documented host assumptions and deferred scope (not defects)

- **Authentication and authority.** Issuer and currency admission, actor-to-issuer authentication, source, policy and catalogue resolution, digest preimages, rights, read/write permissions and aggregation authority.
- **Scale and storage.** The 256-ID lifetime cap is enforceable only against a complete host-supplied register. There is no paging, retention, tombstone, current selector, head/revision/retirement handling or existing-Dimension migration.
- **Native binding scope.** Genesis-only binding. Envelope keys are not closed. The `provenance.source` versus master check is left to the host.
- **Deferred functionality.** Quantity × price, FX, calendar/DST, localization, ISO/accounting/cash-rounding conformance and signatures.
- **Parent dependencies.** Parent WM-XCT-032 holds apply: single-provider waiver, empty relationship contract, unverified sources.

## 4. Does it invent a duplicate monetary master?

**No, in the authority sense.** The package states that inputs are pinned snapshots with source-owner mastership, the result is `calculation-only`, and reuse requires re-assertion.

**Caveats:**
- It *is* a parallel structural encoding of 032-like money fields, not a reference to 032 instances. Divergence risk is real.
- Without the parent bytes, I cannot verify the field correspondence in `parent-field-crosswalk.json`.
- A persisted `roundedTotal` can become a de facto master if a host consumes it without re-assertion. Only documentation prevents this.
- Adapting existing records remains a checklist, not an adapter. The package states this honestly.

## 5. Are the bundle, layer, question and whole-object contracts honest and sufficient?

**Honest.** The statistics (4/8/21/21/21/21) reconcile, and host-dependent answers name the missing evidence.

**Thin in places.** Descriptions and artifacts are boilerplate, and the whole-object and mastership rows are templated (L8). They are sufficient for this bounded receipt, provided M1 is addressed.

## 6. Limitations of this audit and remaining research

- **Not verified:**
  - No execution, jsonschema regex behavior or Python 3.12.14 / jsonschema 4.26.0 behavior was verified.
  - No digest or hash was verified.
  - The external V3 validator, composer and writer semantics were not reviewed (bytes not supplied).
  - The WM-XCT-032/008/009/031 content and the two prior studies were not reviewed.
- **Remaining research:**
  - Normative canonical encoding and cross-language vectors (M2).
  - Production register design: paging, index, erasure and tombstone.
  - A current-head/revision-aware native binding that commits the object to the fact digest.
  - The host adapter for existing calculation records.
  - Non-terminating-increment and leap-second tests, plus envelope-cap boundary tests.
  - Quantity/FX/calendar/localization slices.
  - Independent second-provider review of parent 032.
