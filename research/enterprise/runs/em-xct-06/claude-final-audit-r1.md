# EM-XCT-06 / Enterprise Monetary Calculation 0.1.0: frozen-package audit

## Verdict: **REVISE**

I found no critical defect. The core arithmetic is correct. I hand-replayed all three examples (startup 1.50/1.48, matrix 1.06/1.05, ai 1e15.00) and every step residual, and the five rounding modes are mathematically correct for negative values and ties. Digest-plus-replay does detect a rehashed wrong result.

The verdict is REVISE because several defects contradict the package's own stated invariants:
- The declared grammar is not actually enforced, so invariant 14 (source-slot uniqueness) can be bypassed.
- The issuer-admission API cannot express the "distinct historical-admission decision" that the spec requires.
- The native validation evidence does not check the stored object record.
- The "adapter contract" for existing records is claimed but not specified.

All of these are small, local fixes. Once they are fixed and tested, I would expect **ACCEPT WITH LIMITS** for the bounded use described.

---

## 1. Defects

### D1: Medium. Declared ID, key and code grammar is not enforced (trailing newline and control-character aliases)
- **Where:** `monetary.schema.json` patterns (`^…$`), enforced only through jsonschema in `monetary.py:shape`.
- **Mechanism:** Python jsonschema evaluates `pattern` with `re.search`. In Python, `$` also matches just before a final `\n`. Only `amount()` uses `re.fullmatch`. IDs, `key`, `code`, `snapshotDigest` and pin digests are checked by the schema alone.
- **Counterexample (breaks invariant 14):** Set `inputs[1].source = {**inputs[0].source, "id": inputs[0].source.id + "\n"}`. The `duplicate-source-slot` check compares exact strings, so it passes, and the same slot is counted twice. Other cases that pass:
  - `currency.code = "EUR\n"` (the Currency `code` has no maxLength);
  - `key = "item-0\n"`;
  - `request.id = "urn:x:a\n"`, which becomes a visually identical but distinct immutable identity.
- **Why the receipt digest is not affected:** The recomputed digest has no newline, so a `digest` with a trailing newline fails. The `supersedes` digest also fails the equality check in import.
- **Fix:**
  - Use `\A…\z`-equivalent anchors. In JSON Schema, prefer `^[…]{n,m}$` together with an explicit code-side `re.fullmatch` for every patterned field. Alternatively, use a `format`-free checker that rejects `\n`.
  - Add negative tests for a trailing `\n` in `id`, `source.id`, `key`, `code` and digests.

### D2: Low–Medium. Timestamps accept non-ASCII digits
- **Where:** Schema `\d` patterns and `monetary.py:stamp` (`datetime.strptime`).
- **Mechanism:** In Python `str` regexes, `\d` matches Unicode decimal digits. `_strptime` also uses `\d`, and `int()` accepts Unicode digits. This is based on standard CPython semantics; I did not execute it.
- **Counterexample:** `computedAt = "٢٠٢٦-09-21T10:01:00Z"` would likely be accepted as the same instant as the ASCII form. That creates lexical aliases, contradicts "strict UTC seconds", and breaks downstream string comparisons such as `validFrom == recordedAt`. Within one receipt, mixed forms fail closed because contexts must be string-equal.
- **Fix:**
  - Use ASCII `[0-9]` in the schema.
  - In `stamp`, also require `dt.strftime(FMT) == s` (a canonical round-trip).
  - Add a test.

### D3: Medium. Issuer admission conflates historical retention with current issuing
- **Where:** `monetary.py:import_receipts`, using one `allowed_issuers` set for both `existing` and `incoming`.
- **Spec claim:** "retention of a former issuer requires a distinct historical-admission decision by the host."
- **Counterexample:** A revoked issuer's old receipts must stay importable. To allow that, the host has to keep the issuer in `allowed_issuers`. That same set then admits *new incoming* receipts from the revoked issuer.
- **Fix:** Split the parameter into `admitted_existing_issuers` and `admitted_incoming_issuers`, or accept a per-record admission decision. Test the revoked-issuer case.

### D4: Medium (evidence gap). The native object record is never validated from storage, and the object binding is incomplete
- **Where:**
  - `acceptance.py`: `validate_native(saved, obj, …)` passes the stored *fact* but the *in-memory* `obj`.
  - `monetary.py:validate_native` does not check `obj.recordId` (which acceptance derives from dimension+id), `previousRecordId`, or `obj.recordedAt` against `fact.recordedAt`.
- **Counterexample:**
  - The stored object file could be rewritten with any `recordId` or `recordedAt`, and the companion path would not notice. Only the outer V3 validator's unknown rules would apply.
  - Invariant 15 claims "native object/type/... checks", but no negative test exercises `objectType`, object `state`/`accessClass`, `authority`, `status`, `validTo`, `recordDigest`, dimension or issuer via `validate_native`.
- **Fix:**
  - Read back the stored object and validate it.
  - Bind `recordId` in `validate_native`.
  - Add object-side negatives.

### D5: Low–Medium. Native negative tests do not assert the rejection code, so the "rehashed-invalid-nested-result" negative is not isolating
- **Where:** `acceptance.py` negative loop and the `bad` fixture. Both use `except module.Rejected` with no code check.
- **Counterexample:** The `bad` fact recomputes `value.digest` and `recordDigest` but keeps the old `factId`. If the replay check were removed, the case would still be rejected by `native-binding` because the factId no longer matches. The acceptance claim that nested arithmetic is caught at the native layer is therefore not demonstrated. The unit test `test_replay_and_digest_tamper` does isolate replay at the `validate` level.
- **Fix:**
  - Recompute `factId` in the bad fixture.
  - Assert `str(e) == 'replay-mismatch'`, and assert the expected code for every negative.

### D6: Low. `import_receipts` can raise `KeyError` instead of `Rejected`
- **Where:** The chain walk in `import_receipts`: `cursor = merged[cursor['request']['supersedes']['id']]`.
- **Counterexample:** Incoming `[A, B]` where A→B and B→C, with C absent. The outer loop visits A first, and its walk dereferences C before B's own `supersedes-unresolved` check runs. The call fails closed, but with an off-contract exception. Callers that catch only `Rejected` will crash.
- **Fix:**
  - Resolve every pin in a first pass, then walk the chains.
  - Alternatively, `require(... in merged, 'supersedes-unresolved')` inside the walk.
  - Add a test.

### D7: Medium (contract honesty). The "adapter contract" for existing calculation/audit records is claimed but absent
- **Where:** `model-spec.md` says an existing record "can instead use this as an adapter contract". `boundary-decision.md`, `crosswalk.json` and `agent-guide.md` repeat this.
- **Problem:** No mapping exists that says which host fields must supply which receipt fields, how digests or replay apply to a non-native record, or how duplication is detected. The only API emits this exact format. "Adapt rather than duplicate" is therefore advisory only.
- **Fix:** Either specify a minimal field-level adapter mapping (required evidence, replay rule, identity mapping), or reword it as "may be used as a checklist; no adapter is specified."

### D8: Low. Lesser claims-vs-tests and documentation gaps
- `test-results.json` hard-codes `oracleCases: 200` (this is true by construction: 5×10×4). The examples are *regenerated* from code and never loaded as frozen golden vectors, so a change in canonicalization would silently change digests. **Fix:** Add a test that loads `examples/*.json` and validates their digests.
- There are no tests for: legitimate branching (two successor IDs from one predecessor being accepted), issuer change in a chain, subject change, decreasing `computedAt`, or `recordedAt < computedAt`.
- `acceptance.py` reads stored envelopes with plain `json.loads`, not `m.load`. The test path does not follow its own "load before validate" contract, so duplicate keys in stored files would be last-wins.
- `load(bytes)` accepts a UTF-8 BOM and UTF-16/32 through `json` auto-detection. This does not affect digests, but the wire encoding is not strictly UTF-8.
- `model-fields.md` says "Deletion of a referenced predecessor is refused by complete-register import". This is true only when the successor is supplied. Deleting both, or deleting a leaf, is undetectable. Reword it.
- `boundary-decision.md` refers to "Case A … B/C/D", which are not defined in this package.
- Acceptance release fixture:
  - It says `role: 'core'` and `publicationStatus: 'published'` for a companion candidate.
  - `references: []` omits the 032 semantic reference that `composition.yaml` declares.
- `spec.json` question routes:
  - They say "insufficient-context with named gaps", but every `answer_data` carries the same generic gap text; no gaps are named per question.
  - Locally answerable questions (Q07, Q09, Q10, Q15) are not distinguished from host-dependent ones.
- The tested Python is 3.12.14, but the docs claim "3.11+".

---

## 2. Documented host assumptions (not defects, but the adopter must satisfy them)
- `issuer` is self-declared, and `allowed_issuers` is string membership, not a credential. In the acceptance and unit evidence, `allowed_issuers = {q['issuer']}` is derived from the receipt itself, so real host authority is never exercised.
- The `masterSystem`, `writer` and `authority.rank=0` checks compare caller-supplied strings. Native `recordedAt` is declared, not proven storage time, and the V3 writer's handling of it is unknown to me.
- Replacing a leaf record, or rehashing a whole register consistently, is detectable only against a trusted prior snapshot. There are no signatures. This is stated honestly.
- Currency code existence, catalogue truth, exactness, allowed signs, aggregation permission and the policy authority's applicability all belong to the host.
- Source-slot uniqueness is exact-ID equality. Genuine aliases (two IDs for one slot) are the host's problem. D1 is a separate, fixable grammar hole.
- V3 objects stay `state: active` after correction. A generic V3 consumer may see two "active" receipts for the same nested subject. Current selection is external by design, so the host must not let V3-native readers treat the receipts as current values.
- Complete-register semantics:
  - Import cannot know whether `existing` is complete.
  - Beyond 256 records, including replays, the function cannot be used at all.
  - Closure-scoped import (a receipt plus its predecessor closure) would validate lineage but not ID conflicts. This is worth stating explicitly.
- Canonical JSON is Python `json.dumps` semantics, not RFC 8785. Any non-Python host adapting receipts must replicate Python's escaping exactly to reproduce digests. This is an interoperability risk that the package discloses.

## 3. Deferred scope (honestly declared)
- Quantity × price, FX, allocation and tolerance.
- Calendars and DST, localization and designations.
- A current selector, withdrawal and tombstones, a retention engine, paging/production scale, existing-Dimension migration, and automatic validator dispatch.
- Cross-version migration.

## 4. Specific adversarial questions
- **Decimal signs, ties and stages:** Correct.
  - Negative zero input is refused, and output zero is unsigned.
  - `inexact` survives cancelling residuals.
  - Scale-only changes are not treated as inexact.
  - Per-item and after-sum stages are distinct and traced.
- **Precision limits:** Enforced consistently between the regex and the digit count, and they fail closed. A large magnitude with a fine increment hits `output-capacity`. Step strings are bounded only by the schema's 64 characters, not by the 42-digit output cap. That is harmless but inconsistent.
- **Same currency, different context:** Full currency-tuple and context equality is enforced, along with policy-currency equality. It fails closed on case or normalization variants.
- **Version refusal:** Correct. `const` is used at both receipt and request level, and unknown fields fail closed.
- **Outer vs nested validation:** The documentation is honest that outer V3 validation does not validate nested arithmetic. The evidence is weaker than claimed (D4, D5).
- **Duplicate monetary master?** No, conditionally.
  - The receipt holds input snapshots with source pins, plus a result marked `calculation-only`, under one restricted fact. No field projection exists.
  - Risk: `masterSystem` covers the embedded amounts, so hosts must not project nested amounts as mastered facts.
  - I cannot verify the claimed narrow semantic reuse of WM-XCT-032. There is no field-level mapping to 032 field IDs, and this package re-implements quantization that 032 reportedly also describes. **Recommend** a field crosswalk (Currency, Context, Policy, mode names mapped to 032 fields) so that "reuse, not duplication" can be audited.
- **Bundle, layer, question and whole-object contracts:** The statistics (4/8/21) match the structure. The contracts are adequate for bounded use, but templated. `whole-object-coverage.yaml` uses boilerplate reasons (for example, Rational "inherits receipt source and policy context"), and the question gaps are not named (D8).

## 5. Limitations of this audit
- I used no tools. I did not execute any code, and I did not verify any SHA-256 value, tool pin, test report or acceptance report. The internal consistency of the declared digests across files was checked by reading only.
- The V3 composer, writer and validator source, the WM-XCT-032 bytes, and the two preserved provider studies were not supplied or reviewed. Where Python standard-library behavior is asserted (jsonschema `re.search`, `$` before a newline, `strptime` with Unicode digits, BOM detection), it is from knowledge of CPython and jsonschema, and should be confirmed with the tests recommended above.
- This verdict is review evidence, not publication authority.

## 6. Remaining wider research
- WM-XCT-032 field-level alignment and the vocabulary for quantization declarations.
- A cross-language canonicalization decision (JCS or an explicitly specified encoding).
- A production register design: paging, closure-scoped import, CAS, trusted snapshots, and signature or attestation for issuer authenticity.
- A current-status projection and a V3 relation for supersession that generic readers can see.
- The deferred neighboring profiles: quantity/unit (008), time/calendar (009), localization (031) and FX observation, along with their own publication holds.
