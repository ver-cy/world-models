**REVISE**

This is a narrow REVISE. The arithmetic, kind/dimension separation, canonical encoding, rational bounds and fail-closed wire handling hold up under adversarial reading of the supplied source. One documented identity claim is contradicted by the fixed native path binding, and that gap weakens `validate_correction` in a way an adopting agent would not expect. Two evidence claims in `acceptance.py` also prove less than they say. Fixing D1 (in either form) and D2 would support ACCEPT WITH LIMITS. I did not execute anything; test and acceptance results, hashes and installed-byte checks are Codex evidence I have not verified.

---

## 1. Defects

### D1 — Medium-High: two different quantities on one host share one path, so correction can link unrelated quantities
**Files:** `quantity.py` `validate_native` and `validate_correction`; `runtime-model.reference.json`; `model-spec.md`/`spec.json` ("Quantity identity is the host's qualified subject and field/fact"); QV-Q01/QV-A01 ("field/fact binding"); `model-fields.md` ("Host objects may have many quantity facts").

- `validate_native` hard-codes the path to exactly `quantity.value` or `quantity.conversion`. No host field qualifier can be expressed.
- **Counterexample.** A RoutePlan host stores fact F1 at `quantity.value`: 12.50 km, kind `route-length`. It also stores F2 at `quantity.value`: 1.250 h, kind `service-duration`. Both pass `validate_native`.
  - Now append F3: `supersedes=[F1]`, value 2.00 h `service-duration`, same master/writer/access, with a reason.
  - `validate_correction(F1, F3, …)` accepts it. The path is equal, and no kind, dimension, anchor or context continuity is checked.
  - The route length has been "corrected" into a duration. Any host head selector keyed on subject+path now sees two competing quantity heads with no local way to tell which field each one is.
- The spec does document "No chain-wide kind continuity is inferred" and "host may change semantic context/definition/source". It does **not** document that 0.1.0 provides only one semantic slot per host per path. Its identity statement suggests field qualification exists when it does not. This is an undocumented structural limit, not a legitimate deferral.
- **Required fix (either option):**
  - **(a) Minimal.** State normatively that 0.1.0 supports one semantic quantity per host object per path. Hosts needing several quantities must use distinct host objects until a slot qualifier exists. Also make `validate_correction` refuse changes to `unit.kind`, `unit.dimension`, `unit.anchor`, `role` or `context` by default (e.g. a new reason `correction-semantics`), with semantic change requiring a separately governed workflow. This mirrors the existing master/writer/access restriction. Add a test with two quantities on one host.
  - **(b) Structural.** Allow a validated qualified path such as `quantity.value.<slot>` / `quantity.conversion.<slot>`, with a matching runtime-model pattern, and require slot equality in correction.
- Related adoption risk: a `quantity.conversion` fact embeds its own copy of the input. When the corresponding `quantity.value` is corrected, nothing links or flags the conversion as stale. Document this under host work.

### D2 — Medium (evidence): `originalBytesPreserved` does not test what it claims
**File:** `acceptance.py`, per-profile loop.
- `original=paths[0].read_bytes()` is read **after** both the first fact and the correction fact were appended. The subsequent comparison only proves that `validate_correction`, a pure function with no I/O, did not write to disk, plus that the tamper was restored.
- It does not prove that appending the correction left the predecessor's stored bytes unchanged. That is the actual claim in `invariants.md` #15 and the spec's "Synthetic acceptance verifies … original-byte preservation".
- **Fix:** capture `paths[0]` bytes immediately after the first `append`, then compare after the second `append`, after `validate_correction`, and after restoration. Report these as separate booleans.

### D3 — Low: `validate_native` treats a missing `unit`/`validTo` key as `null`
**File:** `quantity.py` `validate_native`, `native-state` check.
- `fact.get('unit') is None and fact.get('validTo') is None` accepts a fact with no `unit` or `validTo` key at all. The spec says "outer unit must be null" and "open-ended validTo=null". This currently relies on outer V3 requiring those keys, which is not stated as a dependency.
- **Fix:** `'unit' in fact and fact['unit'] is None`, and likewise for `validTo`. Add a negative test for each.

### D4 — Low: `Pin.revision` accepts whitespace-only values
**File:** `quantity.schema.json` `Pin.revision`.
- There is only `minLength:1` and no pattern, so `"revision":" "` passes. The spec says "Revision must be explicit."
- **Fix:** add `"pattern":"^[!-~]+(?![\\s\\S])"` or state explicitly that revision is fully opaque. Either change alters the schema pin.

### D5 — Low: `schema` reason is overloaded for the QV-F13 refusal path
**Files:** `quantity.schema.json` (`formula`/`exactness` const); failure table in `spec.json`.
- Logarithmic, approximate or procedure units fail as `schema`. The table defines that reason as "Unsupported shape/version or changed sibling schema; check trusted release bytes". An agent following QV-ACT13 cannot tell an unsupported transform class from a corrupted release.
- **Fix:** add a table note that `formula`/`exactness` const failures surface as `schema`, or pre-check those fields to emit `unsupported-transform`.

### D6 — Low (documentation/structure)
- **Facet inconsistency.** `Result.recognition-observation` is `required` ("Reproduced from retained input, not a new independent measurement"). `ConversionDocument.recognition-observation` is `not-applicable` with essentially the same meaning. `QuantityDocument`'s `not-applicable` carries a substantive meaning. Align them; D9 in the reconciliation is not fully closed.
- **Artifact boilerplate.**
  - Every artifact is described as "Required evidence", including QV-A15, which is named "Optional…".
  - QV-ACT13 ("Refuse in this release") is suffixed "subject to authenticated host permission", although refusal needs no permission.
  - QV-A13 names a "host escalation destination" that no route defines.
- **Undocumented API helper.** The "Executable API" section does not name `digest()`/`canonical()`, yet hosts must use them to build admission sets. Name `digest` as the reference helper for admission entries.
- **Premature review claims.** `review.md` states in present tense that frozen Claude/Grok candidate audits "are preserved". `AGENTS.md` lists `review.json`, which is not in this candidate. Both must be filled in with actual verdicts, preserving disagreement, before release.
- **Synthetic plan wording.** The synthetic plan in `acceptance.py` says `publicationStatus:'published'` while `publication-manifest.draft` says `candidate-not-yet-published`. This is acceptable for a synthetic Dimension but deserves a one-line note so it is not cited as publication evidence.

### D7 — Low (test coverage gaps, no wrong value found)
Missing tests:
- Reverse direction C→F point and difference, plus a negative-`b` target.
- Scalar-role anchor mismatch.
- Two quantity facts on the same host/path (see D1).
- A Result near the component length boundary.
- Missing `unit`/`validTo` keys (see D3).

The 201-case oracle covers only integer F→C points.

---

## 2. Verified correct as supplied (not defects)

- **Affine formulas.**
  - Point: `(a_s·x + b_s − b_t)/a_t` follows from `a_s·x + b_s = a_t·y + b_t`. Difference and scalar: `a_s·x/a_t`.
  - F: `a=5/9`, `b=45967/180` (= 459.67·5/9). C: `b=5463/20` (= 273.15).
  - 32 °F → 0 °C. An 18 °F difference → 10 °C. The acceptance second result for 2.00 °F is `200/180 − 3200/180 = −50/3`, which matches `acceptance-results.json`. Startup (1.250 h → 75 min) and matrix (12.50 km → 12500 m) also match.
- **Role gating.** Source role must be in the source roles and in the target roles. `scalar` requires `b=0` on both sides, because both definitions must list `scalar`. There is no cross-role conversion.
- **Kind versus dimension.** Equal-dimension, different-kind conversions are refused; the energy/torque test covers this. Kind, dimension and anchor are all compared as exact Pin/list equality. There is no code or label inference.
- **Rational bounds.**
  - Worst-case point result: denominator about 162 digits, numerator about 180 digits, both under 256. The Result cap is not reachable by admitted inputs. Grok's reading is correct.
  - The lexical `maxLength` of 38 is consistent with 36 digits plus sign and point.
- **Canonical bytes.**
  - Python `json.dumps(sort_keys, ensure_ascii, compact)` over printable-ASCII-only strings escapes exactly `"` and `\`, and not `/`, as specified.
  - bool/int confusion is handled: `type(v) is int` excludes bool, the rank check uses `type() is int`, and jsonschema's `integer` excludes bool.
  - Subclassed containers fail closed.
- **Wire handling.**
  - Floats and exponents go to `parse_float` and are rejected. `NaN`/`Infinity` are rejected. Duplicate keys and oversized input are refused.
  - `RecursionError` on deep nesting is caught. Patterns use `(?![\s\S])` rather than `$`, which avoids the trailing-newline bypass.
- **Unknown magnitudes.** `unknown`, `withheld` and `not-applicable` validate and are stored. `convert` and `compare` refuse them on either side. Zero is never produced.
- **Native binding.** Subject, master, writer, rank, access, status, path, provenance and time checks match the spec text. Correction requires distinct IDs, the exact predecessor link, a direct two-cycle refusal, path equality, nondecreasing `recordedAt` and a nonblank reason.

---

## 3. Explicit host assumptions (documented, not defects)

- Evidence resolution before admission; admission sets are inspection gates, not credentials.
- Admission is a flat membership test, so any admitted source can pair with any admitted definition and context. The spec correctly warns against sharing broad sets.
- Current access, head selection, full supersession graph, parallel-head detection, and concurrent assertion policy.
- Outer V3 validation of all host-object fields other than the four bound ones.
- The same access class on object and fact, and `rank: 0` only.
- ASCII-only for the whole quantity fact.

---

## 4. Legitimate deferred scope (documented, not rejected)

- UCUM parsing.
- Uncertainty and rounding.
- Logarithmic, procedure or material-dependent units.
- Rational exponents.
- Point±difference arithmetic.
- Price, FX, calendar and localization.
- Idempotent import.
- Retraction and finite `validTo`.
- Cross-actor or cross-access correction.
- Version migration.
- Tombstones.
- Independent-language canonicalization and JCS compatibility.

---

## 5. Structure: 4 bundles / 8 layers / 20 routes / facets

- **Counts are consistent.** There are 4 bundles × 2 layers. Findings per layer are 2+2+3+3+3+2+3+2 = 20, each with exactly one question, artifact and action; this matches `statistics`. `whole-object-coverage.yaml` and `mastership-and-rights.yaml` match the embedded `spec.json` matrices. There are 9 shapes × 5 facets.
- **Routes are truthful bounded guidance.** They do not overclaim a workflow. QV-F17 correctly carries the same-master/writer/access restriction.
- **Missing route after D1.** No route covers "which host field does this quantity occupy / can one host hold several quantities?" QV-F16 answers "which native record", not "which slot".
- **Facets are usable.** The remaining problems are boilerplate and the Result/ConversionDocument inconsistency in D6. The native fact envelope, the shape adopters actually construct, has no facet entry; it is covered only in prose. That is acceptable but worth noting.

---

## 6. Material adoption risks and outstanding wider work

1. **Slot collision (D1).** This is the most likely real-world misuse: several quantities on one host object, or silent semantic "correction".
2. **ASCII-only facts.** A non-ASCII `correctionReason`, provenance text or objectId is rejected as `ascii-string`. Operators writing reasons in Russian or other scripts will hit this. It is documented, but it will be a frequent operational friction point.
3. **Admission-set construction** has no reference builder. Agents will be tempted to hash incoming Pins, which the documentation forbids. A per-subject, per-purpose host builder is needed before a live binding.
4. **Stale conversion facts** after the underlying value is corrected.
5. **Access coupling.** Object access must equal fact access, so sensitive quantities on less-restricted host objects need a different design.
6. **Same master/writer/access correction.** Real review workflows, where a different actor corrects a value, have no path yet.
7. **Wider EM-XCT-06 work** remains partial: Price/FX, working calendars, uncertainty, localization, a governed conversion receipt if ever justified, a live-Dimension migration, and the review.json/review.md release record.

Publication authority remains with you; this verdict is evidence only.
