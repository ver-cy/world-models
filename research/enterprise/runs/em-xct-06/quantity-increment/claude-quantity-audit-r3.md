ACCEPT WITH LIMITS

This is an independent reading of the supplied text only. I executed nothing. I did not verify any hashes or source claims, and I did not reproduce the test or acceptance results. Hash and result statements below are Codex evidence that I checked only for internal consistency.

## 1. Basis for the verdict

The core numeric and semantic contract is implemented as documented, and I found no blocking defect.

**Affine formulas (`quantity.py:result`)**
- Point conversion is `(a_s·x + b_s − b_t)/a_t` and applies only when the role is `point`.
- Scalar and difference conversion is `a_s·x/a_t`.
- `scalar-offset` forces `b=0` on any definition that allows `scalar`, so the scalar branch cannot hide an offset.
- `a>0` preserves order, so `compare` can compare in the right-hand unit.

**Hand checks of the documented values**
- Fahrenheit coefficient: 459.67·5/9 = 45967/180, and 273.15 = 5463/20.
- 32 °F point → 0 °C. 18 °F difference → 10 °C difference.
- 2.00 °F point → −50/3 °C, which matches the acceptance `secondResult`.
- 0 °C point → 32 °F. With target `b=−1`, the result is 5483/20.
- 1.250 h → 75 min, and 12.50 km → 12500 m.

**Kind versus dimension**
- `compatible` checks kind, then dimension, then anchor, using exact Pin tuples.
- Same dimension with a different kind is refused, as in the energy/torque test.
- `compatible` never infers a kind from a dimension.

**Admission order**
- The schema is checked before arithmetic.
- The definition digest covers the whole snapshot.
- Source and context digests cover the whole Pin.
- Checks on the target definition are symmetric with the source.

**Canonical bytes**
- The code uses `json.dumps(sort_keys, ensure_ascii, (',',':'))` after `bounds`, which restricts input to printable ASCII, excludes DEL, and rejects bool-as-int and floats.
- This produces exactly the normative encoding: only `"` and `\` are escaped, `/` is not escaped, and ASCII sort order equals code-point order.

**Schema details**
- `(?![\s\S])` correctly closes the Python `$`-before-newline loophole under `re.search`.
- The `oneOf` branches are mutually exclusive by `format` and by `state`.
- jsonschema excludes bool from `integer`, and `bounds` excludes floats, so the "1.0 as integer" gap is closed.

**Unknown states**
- `MissingMagnitude` validates and can be stored.
- Arithmetic and `compare` refuse it with `non-numeric`, on either side.
- No zero or unit is ever substituted.

**Rational bounds**
- Factor components are limited to 36 characters and Result components to 256, both counting the sign.
- My estimate of the worst case is about 165 characters per component, so the 256 cap is unreachable, as claimed.

**Reason codes**
- Every `Rejected` reason emitted by the code appears in the failure table.
- I found no uncaught non-`Rejected` exception path for malformed inputs (non-dict, missing keys, bad types). The `and` guards short-circuit correctly.

**Documentation claims that match the code**
- The R3 reconciliation claims I checked (items D3/D4 of R1–R2, blank IDs, defensive copy, explicit null keys, the two-cycle check, and the four correction-semantics fields) match `quantity.py`.
- The test count of 53 matches the `test_` methods.
- The declared digests are consistent across `test-results.json`, `acceptance-results.json`, `SCHEMA_SHA` and the file headers.

## 2. Defects

| # | Sev | File / function | Counterexample | Necessary fix |
|---|---|---|---|---|
| D1 | **Medium** | `quantity.py:validate_native`; `AGENTS.md`; spec §Native | A stored fact with `supersedes:["…:quantity:0"]` and no `provenance.correctionReason` passes `validate_native`. So does one whose kind, role or context differs from its predecessor, if its definition is admitted. AGENTS.md prescribes only "outer V3 + explicit nested validation" and never names `validate_correction`. An agent that validates a head record alone therefore bypasses `correction-reason`, `correction-semantics`, `correction-time` and the link guards. | Add a normative rule to both AGENTS.md and the spec: any record with non-empty `supersedes` is unusable until `validate_correction` passes against each retained predecessor. Optionally, have `validate_native` also check that `supersedes` is a list of nonblank strings, and that a non-empty list carries a nonblank `correctionReason`. |
| D2 | Low–Med | `validate_correction`; spec "Pairwise correction preserves the input…"; QV-F17 | The previous record converts 1.250 h to 75 min. The "correction" converts 1.250 h to 4500 s (target `s`, same kind and anchor). Kind, role and context are unchanged, so the pair is accepted. The single `quantity.conversion` slot then silently changes its coordinate unit between revisions, and a reader comparing results sees 75 → 4500. | Decide the rule, then state and test it. Either require an identical target (by full digest, or at least by reference and code) and reject a change as `correction-semantics`, or state explicitly that the target may change and each result must be read only with its own target. |
| D3 | Low | spec §correction ("supersedes containing the exact prior fact ID") vs code `== [previous['factId']]` | Merging two parallel heads with `supersedes:[A,B]` fails with `correction-link`, but the word "containing" suggests a superset is allowed. | Reword to "exactly one element, equal to the predecessor ID", and list multi-predecessor merge as deferred. |
| D4 | Low | `quantity.py:load` (and `stamp`) | `raise Rejected('wire-json') from e` keeps `__cause__`. A `JSONDecodeError` carries `.doc` (the entire decoded input) and a `UnicodeDecodeError` carries `.object` (the raw bytes). A diagnostic logger that serializes the chain can disclose restricted or withheld content, which conflicts with "Permission and disclosure govern diagnostics". | Use `raise … from None`, or document that exception chains must not be logged. |
| D5 | Low | `validate_correction` | Native failures from the predecessor and from the current record raise identical codes, for example `native-master`. An adopter cannot tell which record needs rechecking. | Document this, or distinguish the two, for example by validating the predecessor in a separate call before the current record. |
| D6 | Low | `examples/*.json` | No test regenerates `fixture()` output or admission digests and compares them with the shipped examples. Stale examples would still pass all 53 tests. | Add a byte and digest comparison test for the three examples. |
| D7 | Low | `test_quantity.py` | The unit tests never exercise `wire-json`, `admission-shape`, `native-shape`, `object-bounds`, `array-bounds`, `integer-bounds`, `bytes` or `schema-pin`. No test accepts the upper bounds: a 36-character Factor, an 18-digit fraction, or a 36-digit lexical. The oracle uses a 1e-110 tolerance even though an exact `Fraction` oracle is available. | Add refusal and boundary-acceptance vectors, and make the oracle exact. |
| D8 | Low | `acceptance.py` | `read()` uses the repository `q.load`, not the installed module. Several report fields are literal `True`, including `storedMissingQuantityValidated` and `nonAsciiHostNameValidatedByOuterV3`. These are sound only because the run is fail-stop. | Use `module.load`, and derive the booleans from the checks themselves. |
| D9 | Low | `AGENTS.md`, `review.md` | AGENTS.md (a frozen operational asset) points to `review.json`, which is absent from the frozen candidate and is "added after freeze". | At release, confirm that the post-freeze diff is limited to evidence bookkeeping and that the digests of the five operational assets are byte-identical to this candidate. If they are not, re-freeze. |
| D10 | Info | `load` | The wire integer token `-0` is silently normalized to `0`. This has no semantic effect on the fields that can hold it. | Optional: reject `-0`, or document the normalization. |

## 3. Explicit host assumptions (correctly documented, not defects)

**Admission and evidence**
- The admission sets are truthful, current, and scoped to a subject and purpose.
- The API has no way to bind a source Pin to the asserted magnitude, role or context. That binding is entirely a host step performed before the call.
- Admitted definitions that share a kind and anchor must have mutually consistent coefficients. No cross-definition coherence check exists.
- Exactness claims (`definition-exact`, `exact-by-definition`) are host evidence.

**Native records**
- Current access, the head or winner, full supersession closure, longer cycles, the slot inventory, and clock plausibility are all host responsibilities.
- The profile supports only same-master, same-writer, same-access corrections with `rank=0` and `validTo=null`.

**ASCII restriction**
- The whole quantity fact must be printable ASCII, including `correctionReason` and `MissingMagnitude.reason`.
- For hosts that write reasons in other scripts, for example Cyrillic, this is a real adoption constraint. It is documented, but adopters should be warned plainly.

**Toolchain and runtime**
- jsonschema 4.26.0 must be present in the host runtime. It is not one of the five installed assets.
- The unqualified runtime paths `quantity.value` and `quantity.conversion` must not collide with other installed models. I cannot assess this from the supplied bytes.

## 4. Legitimate deferred scope (not rejected)

- UCUM parsing and annotations, uncertainty and rounding, rational exponents, ordinal and nominal scales.
- Affine point±difference arithmetic.
- Multi-field native binding, cross-actor or cross-access correction, retraction and finite intervals.
- Idempotent replay, a current-head selector, staleness detection, version migration.
- Price, FX, calendar, localization, and independent conversion receipts.

## 5. Structure and documentation sufficiency

**Counts**
- The 4 bundles, 8 layers and 20 findings/questions/artifacts/actions are internally consistent (2+2+3+3+3+2+3+2 findings per layer), with unique IDs.
- QV-ACT13 deliberately omits the permission suffix, per R2.

**Facets**
- There are 9 shapes × 5 facets, matching the 9 schema `$defs`.
- `whole-object-coverage.yaml` and `mastership-and-rights.yaml` match the corresponding `spec.json` blocks as rendered.
- **Limit:** facet `status: required` does not say whether the package enforces the facet locally or the host must supply it (for example, UnitDefinition recognition is "required" yet entirely external). Question kinds carry host, local or mixed, but facets do not. Add a responsibility tag.

**Routes**
- The routes are truthful bounded guidance.
- **Gaps:**
  - No route covers a stale `quantity.conversion` after `quantity.value` is corrected; this is in the spec but not in F16–F18.
  - No route covers the pair-validation duty in D1.
  - Reason codes are not cross-linked to question IDs.

**Overall usability**
- An adopting agent reading the full `spec.json` has enough to use the pure API safely.
- The weakest point is AGENTS.md's omission of `validate_correction` (D1).

## 6. Outstanding wider work and material adoption risks

1. **Narrow native binding.** Most real hosts carry several quantities, for example a route plan with both distance and duration. Until a multi-field adapter exists, native use is narrow, and hosts may be tempted into the prohibited "artificial host" workaround.
2. **Misreading a successful validation.** A passing `validate` can be misread as source-verified truth. Admission-set construction is the real trust boundary, and nothing enforces it.
3. **No pairwise-to-history mechanism.** The profile has no head selector or chain closure. Parallel heads, and ties from equal `recordedAt` values, stay silent.
4. **No conversion staleness detector.** Retained conversions can be presented as current after the underlying value is corrected.
5. **Release integrity.** The post-freeze evidence additions (D9) require a digest re-check of the five operational assets before publication.
6. **Contour status.** EM-XCT-06 remains partial: Price/FX, calendars, localization and uncertainty are open, and the monetary package is separate.

**Recommended before publication:** D1 (a documentation rule at minimum) and D2 (decide and state the rule). D3–D10 can follow as tracked items.

This verdict is evidence only. Publication authority remains with the user.
