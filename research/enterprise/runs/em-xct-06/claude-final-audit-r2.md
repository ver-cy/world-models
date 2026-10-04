# EM-XCT-06 audit: Enterprise Monetary Calculation 0.1.0

## Verdict: **REVISE**

This is a narrow revise, not a block. I found no critical or high defect. The arithmetic core is correct on every fixture I traced by hand, the version and closed-schema refusals hold, and the boundary claims are mostly honest.

Four medium defects need fixing before this should publish as a bounded reviewable draft. Each has a concrete counterexample:

- **D1:** the test runner overwrites the golden examples and the test report even when tests fail.
- **D2:** the installed validator trusts an unverified schema file sitting next to it.
- **D3:** `validate_native` admits issuers by substring match.
- **D4:** the reconciliation claims "head" binding that the code does not do.

Once those are fixed, I would expect **ACCEPT WITH LIMITS**.

**Scope of this review.** It is based only on the supplied text. I executed nothing and verified no hash. The declared SHA256 values, `test-results.json`, `acceptance-results.json`, `tool-pins.json`, the V3 validator and writer, the composer, and the WM-XCT-032 parent bytes are supplied assertions. None were provider-executed or independently hash-checked. The only thing I checked is that `sourceDigests` in `acceptance-results.json` matches the declared hashes of the listed files, and it does.

---

## Defects

### D1. Golden oracle and test report are regenerated unconditionally (Medium)

- **Where:** `test_monetary.py`, the `__main__` block, and `test_golden_examples`.
- **Problem:** After the test suite runs, `examples/*.json` and `test-results.json` are rewritten whether or not the tests passed.
- **Counterexample:** Suppose a change alters `compute` output, for example a different tie rule.
  - Run 1: `test_golden_examples` fails, but the examples are then overwritten with the new output.
  - Run 2: everything passes.
  - The golden reference has healed itself around the regression. The reconciliation's claim that golden bytes are "read before regenerated examples" is literally true, but it does not protect anything.
- **Second weakness:** the comparison is on parsed values (`saved == m.issue(...)`), not on bytes. The declared byte hashes of the examples are never checked by any test.
- **Side effect:** following the README's instruction to run `python test_monetary.py` mutates files inside the frozen package.
- **Fix:**
  - Never write goldens during a test run. Add a separate, explicit `--regenerate` mode.
  - Assert exact bytes: `canonical(issue(fixture)) + b'\n' == file bytes`.
  - Pin the example digests in the test.
  - Write the report only to an explicitly named output path.

### D2. Installed companion loads an unverified sibling schema (Medium)

- **Where:** module import in `monetary.py`, which reads `SCHEMA` from `Path(__file__).with_name('monetary.schema.json')`, and `acceptance.py`, which checks the digest of the installed `monetary.py` only.
- **Why it matters:** Several guarantees depend entirely on the schema, not on code:
  - unknown-field refusal (`additionalProperties:false`)
  - ID, digest and code grammar, including the trailing-newline guards
  - enum limits on `mode` and `stage`
  - the `purpose` enum
- **Counterexample:** Replace the installed schema with one that drops `additionalProperties:false` on `Request`. A receipt with an extra `executePayment:true` field then validates. `issue` and `validate` digest the extra field happily, and acceptance still reports that the installed code is identical.
- **Fix:**
  - Embed the expected schema digest as a constant in `monetary.py` and refuse at import if the file does not match.
  - In acceptance, verify all five installed assets against their release descriptors.

### D3. `validate_native` admits issuers by substring (Medium)

- **Where:** `monetary.py`, `validate_native`, in the check `q['issuer'] in allowed_issuers`.
- **Problem:** Unlike `import_receipts`, this function never checks that `allowed_issuers` is a set.
- **Counterexample:** A host passes `allowed_issuers='urn:synthetic:issuer:startup-admin'`, a string instead of a set. A receipt whose issuer is `urn:synthetic:issuer:startup` passes, because Python's `in` on strings is a substring test. Lists and dicts are also silently accepted.
- **Test gap:** the acceptance negative only covers `set()`.
- **Fix:** require `type(allowed_issuers) in (set, frozenset)` with all members of type `str`, the same rule as `import_receipts`. Also type-check `dimension`, `master` and `writer` as non-empty strings. Add negative tests for a string, a list and `None`.

### D4. Claimed object "head" binding is not implemented, and native lifecycle is frozen (Medium; claim vs code)

- **Where:** `validate_native`, and the reconciliation's D4 claim to "bind object record ID/clock/head".
- **What the code actually does:** it checks that the supplied object is the genesis record (`previousRecordId is None` and a deterministic `recordId`). It cannot see:
  - later object revisions, for example one setting `accessClass:'public'` or `state:'retired'`
  - later V3 facts that supersede or retract the receipt fact
- **Counterexample:** A host appends an object revision that makes the receipt public. Validating with the original object still passes and reports `restricted`.
- **The reverse problem:** any legitimate object revision (a name fix, archival, retirement) makes the head record fail `validate_native`. As a result, retention and withdrawal cannot be expressed natively at all.
- **Fix, one of:**
  - Accept the full object record chain plus all facts at `PATH` for the subject. Verify the head, define the allowed transitions (or forbid all of them), and refuse any fact that supersedes a receipt fact.
  - Or correct the claim to "binds the genesis object record only; head, current state, later revisions and native supersession are host duties". State plainly that object revision or retirement is outside this version.

---

## Lower-severity defects

### D5. "Complete register" contract is ambiguous and caps a Dimension's lifetime (Low-Medium)

- **Where:** `model-spec.md` and `AGENTS.md` versus `import_receipts`.
- **The conflict:**
  - The docs require a complete register and say "do not silently partition history".
  - The merge cap is 256 unique receipts.
  - Taken together, a Dimension becomes unverifiable after its 257th receipt, with no retention path, because referenced predecessors must be preserved.
- **What the code enforces:** only predecessor closure. A host that partitions by chain to stay under 256 silently loses cross-partition same-ID conflict detection.
- **Acceptance gap:** acceptance builds `stored` from its own list. It never enumerates facts at `PATH` from storage, so it demonstrates no completeness.
- **Fix, one of:**
  - Declare a hard lifetime cap of 256 receipts per Dimension for this reference.
  - Or specify closed-subset import plus a host-maintained, Dimension-wide ID-to-digest uniqueness index.

### D6. `load` loses its typed error codes (Low)

- **Where:** `monetary.py`, `load`.
- **Problem:** `Rejected` subclasses `ValueError`. So `duplicate-json-key` and `nonfinite-json`, raised inside `json.loads`, are caught and re-raised as `invalid-wire-json`.
- **Why tests missed it:** they use a bare `assertRaises`.
- **Fix:** add `except Rejected: raise` before the `ValueError` clause, and assert the exact codes in tests.

### D7. Untyped crash, and no envelope version check (Low)

- **Where:** `validate_native`.
- **Untyped crash:** if `provenance` is a string or `null`, `fact.get('provenance',{}).get(...)` raises `AttributeError` instead of `Rejected`. It still fails closed, but with an untyped error.
- **No version check:** neither envelope's `schemaVersion` is checked; the code relies entirely on the outer validator.
- **Fix:** add an `isinstance` guard, require `schemaVersion == '1.0.0'` on both envelopes, and add negative tests.

### D8. Undocumented bounds applied to V3 envelopes (Low)

- **Where:** `bounded`, as applied to native envelopes.
- **Problem:** it enforces two limits the spec never mentions:
  - at most 32 keys per object
  - integer magnitude at most 9999
- **Effect:** valid V3 envelopes with, say, a size field over 9999 would be refused.
- **Fix:** document these limits, or apply `bounded` only to the nested receipt value.

### D9. Stale or templated documentation (Low)

- `migration.md` says Python 3.11+, while `model-spec.md` says 3.12.14 was tested. The reconciliation's D8 claims this was corrected, but the duplicate file is stale.
- In `crosswalk.json`, the `semanticReading` entries for 008, 009 and 031 copy the text "selected full fields/functions of 032 read". That is inaccurate provenance.

### D10. Question layer is thinner than the agent contract claims (Low)

- **The claim:** `AGENTS.md` says question routes "return insufficient-context with named gaps".
- **What exists:** `spec.json` has no route or response-status structure. All 21 `answer_data` entries use the same boilerplate.
- **Specific problems:**
  - Locally answerable questions (Q07, Q09, Q10, Q15, Q16) are still templated as host-dependent.
  - MC-Q11 ("Can this total authorize a payment or posting?") should answer "No" outright. Instead it asks for evidence of a constant field.
- **Fix:** differentiate local answers from host gaps, and reword the AGENTS claim to describe expected agent behaviour rather than an executable route.

### D11. Report fields are hard-coded (Low)

- **Where:** `acceptance-results.json` and `test-results.json`.
- **Hard-coded values:** `objects:2`, `immutableReceiptFacts:2`, `installedReplayAndImmutableImport:true` and `oracleCases:200`.
- **`failed:0`:** this is structurally unable to be anything else, because any failure aborts the run.
- **Mitigation:** the V3 `counts` field is measured, and 5×10×4 does equal 200.
- **Fix:** label the report as fail-stop, and compute the counts.

---

## Adversarial checks that passed

| Area | Result |
|---|---|
| Decimal signs and ties | `round_units` is correct for all five modes on negative values; -2.5 and -3.5 under half-even give -2 and -4. I hand-checked all three fixtures: startup 1.50 per-item, 1.48 after-sum, 1.49 half-away, and 1.47 / 1.50 / 1.47 for floor / ceiling / toward-zero; matrix 1.06 with steps -1.02 and 2.08, exact 21/20, residual -1/100; ai 1000000000000000.00 with exact 500000000000000000001/500000. |
| Negative zero | Refused on input. Output cannot be `-0.00` because `fixed` signs only when n < 0. |
| Stages | Per-item and after-sum are correct. `inexact` stays true when per-item residuals cancel. `@total` cannot collide with an input key under the key grammar. |
| Precision limits | The 57-digit output bound holds for the worst case (256 × 36 digits plus an 18-place increment, and for large integer increments under ceiling). Rational patterns (80 digits) and the 64-character rounded strings have headroom. |
| Grammar | The `$(?![\s\S])` guard closes the trailing-newline hole for `re.search`. The code uses `re.fullmatch` and ASCII `[0-9]`. Leap seconds, year 0000 and Feb 30 are rejected by `strptime`/`datetime`. |
| Same currency, different context | The full currency tuple and full context (basis pin, `valuationAt`, `amountRole`) are compared by exact equality. The policy currency must match. |
| Rehash tampering | Changing the result and rehashing gives `replay-mismatch`, tested in both unit and native runs. Changing a predecessor breaks its successor's pin. |
| Immutable correction | Requires a new ID, an exact id+digest pin, a nonblank reason, the same subject and issuer, and a nondecreasing `computedAt`. Self-supersession is refused. Branches are kept without choosing a winner. |
| Version refusal | Top-level and request `schemaVersion` consts, plus closed objects. |
| Outer vs nested validation | Acceptance honestly demonstrates `outerAloneAcceptsBadArithmetic:true` and documents the need for explicit companion calls. |

---

## Documented host assumptions and deferred scope (not defects)

These are disclosed. Where noted, the wording should be sharpened.

- **Issuer authenticity.** `issuer` is self-declared, and the native binding records a single fixed `writer` for all issuers. The promise that "a retained former issuer cannot write new records" is therefore only as strong as the host's authentication of the issuer field at write time. Any writer can relabel a record with a currently admitted issuer. *Sharpen the wording*, or bind the authenticated actor into `authority` or `provenance`.
- **Source-slot aliases.** `slot:01` versus `slot:1` would be double counted. The docs say no alias equivalence is inferred. The preimage of `Pin.digest` (which bytes are hashed) is unspecified, so digests cannot be independently verified or used to detect duplicates. The host must pin that convention per source.
- **Correction scope.** A correction may change `purpose`, currency or context. That is allowed and unchecked, which is reasonable, but the host must decide whether it is a correction or a new subject.
- **Algorithm version.** `schemaVersion` implicitly pins the arithmetic semantics. State that any output-changing fix requires a version bump.
- **Other host duties.** `recordedAt` format compatibility with real V3 writers (fractional seconds would be refused), deletion of leaf records (undetectable without a trusted snapshot), current/withdrawn selection, retention, CAS, read permission, and source, policy and catalogue resolution all remain host duties.
- **Unpinned library.** jsonschema is pinned by version in `requirements.txt` but not by hash, and runtime behaviour depends on it.
- **Deferred scope:** quantity × price, FX, calendar/DST, localization, existing-Dimension migration, host adapters, and production scale.

## Duplicate monetary master?

**No, by contract.** The result is `authority:'calculation-only'`, inputs carry source pins, and `mastership-and-rights` assigns the amounts to their source owners.

There are still residual risks, all enforced only by prose:

- The native `masterSystem` is named `monetary-register`, which reads like a money master. Rename it to something like `…:monetary-receipt-register`.
- Nothing stops one receipt's `roundedTotal` being fed into another receipt as a "source slot", which would create a shadow derived master. Add a rule that a receipt output needs host re-assertion before it can be used as an input.
- The "use only where no equivalent host record exists" rule is not enforceable.

## Are the bundle, layer, question and whole-object contracts honest?

**Honest and adequate for bounded use, but thin.** The statistics are internally consistent: 4 bundles, 8 layers, 21 findings, questions, artifacts and actions. The limitations are stated. The question and whole-object entries are heavily templated, with repeated `meaning` strings and uniform `answer_data`. They work as a checklist, not as operational guidance (see D10).

---

## Test gaps to close alongside the fixes

- `validate_native` has no unit tests; it is exercised only in acceptance.
- No test for a whitespace-only `correctionReason`.
- The decimal oracle only covers single inputs. Add a multi-input per-item case.
- No check of lexical sign or scale on outputs; the oracle compares Fractions only.
- No tests asserting exact error codes from `load`.
- No negatives for `allowed_issuers` given as a string or list, for envelope `schemaVersion`, or for a non-dict `provenance`.
- No test of a partitioned import missing a cross-partition ID conflict (D5).

## Remaining wider research (outside this slice)

- A production store design: paging, a Dimension-wide ID index, and retention that is compatible with keeping predecessors.
- A V3 object/fact lifecycle binding: head, retirement, and native supersession semantics.
- An authenticated issuer-to-actor binding.
- Source-pin preimage conventions for each source system.
- A host adapter specification for existing calculation and audit records.
- Quantity/Unit (008), Time/Calendar (009), Localization (031) and FX boundaries.
- Live re-verification of the WM-XCT-032 parent holds: the single-provider waiver, 53 unverified URLs, and the empty relations contract.

This verdict is review evidence only. It is not publication authority.
