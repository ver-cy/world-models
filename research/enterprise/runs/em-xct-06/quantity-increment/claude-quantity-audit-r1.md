**REVISE**

This is a narrow revise. I found no defect in the affine arithmetic, the kind/dimension/anchor gating, the admission checks or the canonical encoding. The blocking items are three: one evidence label in the frozen results misdescribes what was tested, one correction restriction is undocumented and rejects ordinary corrections, and some native parameters are not type-checked. All are small fixes. Once they are fixed, or explicitly documented as limits, and acceptance is rerun, I would expect ACCEPT WITH LIMITS.

This review is by reading the supplied text only. I executed nothing and verified no digest, source clause or test result.

---

## 1. Verified correct by reading (not defects)

- **Point formula.** `result()` computes `(a_s·x + b_s − b_t)/a_t`. This is the correct inversion of `anchor = a·x + b`.
- **Scalar and difference formula.** `a_s·x/a_t` drops the offset, and `unit()` forces `b = 0` whenever `scalar` is among the roles.
- **Fahrenheit/Celsius constants.**
  - 459.67·5/9 = 45967/180, and 5463/20 = 273.15. Both fractions are already in lowest terms.
  - 32 °F as a point gives 0 °C. 18 °F as a difference gives 10 °C. 2.00 °F gives −50/3 °C, which matches `acceptance-results.json`.
- **Result bound.** The Result bound of 256 cannot be exceeded by `convert` at the schema limits.
  - Worst case is about 181 numerator digits and 162 denominator digits: 36-digit magnitude with 18 fractional digits, and 36-digit factors.
  - So the `'schema'` failure path in `convert` is unreachable for admitted inputs.
- **Validation order.** `bounds` → schema → rational → admission → replay.
  - Floats are refused before JSON Schema's `1.0`-is-integer leniency applies.
  - The `(?![\s\S])` anchor avoids Python's `$`-before-newline trap.
  - `load` rejects duplicate keys, floats, exponents, `NaN`, and integers over 5 characters. Rejections propagate as `Rejected` and are not swallowed by the `except`.
- **Canonical bytes.** `json.dumps(sort_keys, ensure_ascii, separators=(',',':'))` restricted to printable ASCII matches the normative prose exactly: only `"` and `\` are escaped, `/` is not, and keys are sorted by code point.
- **Schema `oneOf` with a closed top level.** A quantity-format document carrying `target` or `result` is rejected.
- **Kind vs dimension.**
  - Kind is compared by exact full-Pin equality, including sha256.
  - Dimension is an independent cross-check.
  - Energy vs torque is refused.
- **Unknown magnitude.** It validates and stores, but `convert` and `compare` refuse it. It is never turned into zero.
- **Test count.** The 40 test methods match `testsRun: 40`.

---

## 2. Defects

| # | Sev | File / function | Counterexample | Necessary fix |
|---|---|---|---|---|
| D1 | **Medium** | `quantity.py` `validate_correction` | One `writer`, `master` and `access` value is applied to *both* records. A predecessor written by `urn:x:capture` (`authority.source`) and a correction by `urn:x:reviewer` always fails with `native-master` on one of the two, whatever writer is passed. The same happens if the correction arrives through a new capture master, or after a reclassification from `internal` to `confidential`. `lifecycle/embedded.md` and the spec's correction paragraph list the conditions (distinct IDs, link, same host/path, chronology, reason) but never state "same writer/master/access". An adopting agent will read the rejection as tampering. | Take separate expected parameters for previous and current (e.g. `previous_ctx` and `current_ctx`). Alternatively, state explicitly in `model-spec.md`/`spec.json`, `lifecycle/embedded.md` and QV-F17 that 0.1.0 validates only same-writer, same-master, same-access corrections. |
| D2 | **Medium (evidence truthfulness)** | `acceptance.py` negatives, `acceptance-results.json` | The `('path','quantity.value','native-path')` mutation is applied to the conversion correction. `validate_native(current)` rejects it with `native-path` *before* the `correction-path` guard runs. Yet the report lists `"correction-path"` under `negativeCasesRejected`, as if that guard had been exercised. The guard (quantity fact corrected by a conversion fact on a different path) is never tested anywhere, including in `test_quantity.py`. | Rename the case to `correction-native-path`. Add a real case: a valid `quantity.value` predecessor with a valid `quantity.conversion` successor, expecting `correction-path`. Rerun acceptance and republish the digests. |
| D3 | **Low–Medium (fail-open on caller error)** | `validate_native` | `subject` is type-checked, but `master` and `writer` are not. With `master=None, writer=None` (for example, a failed host-context lookup), a fact lacking `masterSystem` and `provenance.source`, with `authority={'source':None,'rank':0}`, passes all companion checks. Whether the outer V3 schema catches this is not visible in the supplied files. | `require(type(master) is str and master and type(writer) is str and writer, 'native-context')`. |
| D4 | **Low** | `validate_correction` | `current.get('factId') != previous['factId']` is true when current has no `factId` or a non-string one, so the missing ID passes. A mutual pair where `previous.supersedes == [current.factId]` with equal `recordedAt` is also accepted. | Type-check `current['factId']` as a nonempty string. Reject a predecessor that lists the current fact ID in its own `supersedes`. |
| D5 | **Medium (usability, fail-closed)** | `validate_native` → `canonical(host_object)` | The function reads only `recordType`, `schemaVersion`, `objectId` and `accessClass`. It still runs full ASCII, size and integer bounds over the whole host object. A host named `Сервисная оценка`, or carrying any integer above 9999, makes every quantity fact on it unverifiable. The spec forbids stripping fields and ships no adapter, so the native binding is unusable for common non-ASCII hosts. | Type-check just those four fields and document that the host object's own validity comes from outer V3 validation. This reads a subset; it does not pretend a stripped object passed. |
| D6 | **Low (doc/impl mismatch)** | `quantity.schema.json` `Factor` / `Result` vs spec | `maxLength: 36` includes the minus sign. A negative `b` with 36 digits is rejected, although the spec says "at most 36 digits per component". The same applies to Result (256). | Change `maxLength` to 37/257, or reword the spec to "36 characters including sign". |
| D7 | **Low (doc)** | `spec.json` arithmetic paragraph vs `compatible()` | The prose requires equal anchor only "for a point conversion". The code, and `invariants.md` #3, also require the same anchor for scalar and difference conversions. That is stricter, but it is undocumented in the normative paragraph. The spec also never says that the anchor Pin fixes both the origin *and* the scale unit of the anchor coordinate, which `b` depends on. | State that the anchor applies to all roles and that it identifies both origin and coordinate unit. |
| D8 | **Low (doc truthfulness)** | `spec.json` `purpose`, QV-F06 | "Preserve original notation" overstates what the profile does. `12,50`, `1.25E3`, `+5`, `°F` and `µm` must be normalized into ASCII canonical decimal or ASCII code before capture, so the source's raw notation is lost. | Reword to "preserve the asserted normalized decimal lexical form and ASCII code". Route raw notation to the host or source Pin evidence. |
| D9 | **Low** | Facet matrix (`spec.json`, `whole-object-coverage.yaml`) | Factor's `recognition-observation` is `"required"` while its meaning says it "has no observation". Result and QuantityDocument have similar status/meaning tension. | Use `not-applicable` or `delegated` wherever the meaning denies the facet. |
| D10 | **Low** | Question tree QV-A*/QV-ACT* | Every artifact reads "Required evidence…", including A13, which is a *nonexistent* nonlinear extension. ACT15 ("No. Route…") and ACT19 are statements, not actions. The "Proposed action subject to authenticated host permission" suffix is appended to refusals. `answer_data` simply repeats the artifact and action text. | Mark A13 and A15 as "absent/out of scope". Rewrite ACT15 and ACT19 as imperatives. Drop the permission suffix from refusals. |

---

## 3. Test and acceptance gaps (evidence, not code defects)

- `test_quantity.py` has no unit tests for `validate_native` or `validate_correction`. All native coverage comes from the synthetic acceptance run.
- These negative cases are untested:
  - `native-provenance`, `native-version`, and an invalid `validFrom`.
  - Host-object `objectId` or `accessClass` differing from the fact.
  - A target definition that is not admitted in `convert`.
  - `compare` with a right-hand missing magnitude.
  - A genuine `correction-path` case (D2).
  - A different-writer correction (D1).
- The oracle covers only integer Fahrenheit points against a 1e-110 tolerance. There is no oracle for difference or scalar conversions or fractional inputs, and exact `Fraction` equality would have been stronger.
- `review.json` is referenced but absent, which is expected for a pre-release candidate.

---

## 4. Explicit host assumptions (legitimate, keep them documented)

- Admission sets are the entire trust gate. The host builds them from verified evidence per call. They are not scoped per subject or purpose, so a source admitted for host A is also admitted for host B within the same call.
- Revoking or omitting a historical definition makes old stored facts fail validation. This is by design as "current inspection admission", but agents must not read it as corruption.
- Other narrowings of V3:
  - `authority.rank == 0` only.
  - Fact and object `accessClass` must be equal.
  - `asserted` with open-ended `validTo` only.
  - Strict UTC seconds.
- The following are external and must be asserted by the host:
  - Object identity, the current object revision, current access, and head/winner selection.
  - Source authenticity, physical truth, sign plausibility, and whether `exact-by-definition` is justified.
- `compare` is numeric coordinate ordering only.
- Unknown *unit* is unrepresentable. The same holds for unknown kind, role, context and source, which the docs should state as explicitly as they do for unit.

## 5. Deferred scope (correctly declared; I do not treat these as defects)

The following are out of scope for 0.1.0:

- Unit-expression handling: no UCUM parser or QUDT adapter, and rational dimension exponents are not supported.
- Numeric scope: nonlinear and logarithmic transforms, uncertainty, rounding and presentation, and point±difference arithmetic.
- Commercial and locale concerns: Price, FX, calendars and localization.
- Record operations: idempotent import, head selection, retraction and finite intervals, tombstones and retention, cross-version migration, and existing-Dimension migration.
- Alternative-language canonicalization and JCS certification.

## 6. Structure: 4 bundles / 8 layers / 20 routes / five facets per shape

- **Counts are consistent.** The counts are 4 bundles × 2 layers and 20 findings, each with exactly one question, artifact and action. The statistics block, the README and the tree agree.
- **Facet coverage is complete.** All 9 schema `$defs` shapes have all 5 facets. `whole-object-coverage.yaml` and `mastership-and-rights.yaml` equal the embedded matrices.
- **The routes truthfully describe a bounded profile.** They do not overclaim (see QV-F13, F15, F18, F20).
- **They are thin, templated guidance rather than an operational decision tree** (D10). Routes an adopting agent will need are missing:
  - how to build admission sets from host evidence (only partly covered by Q03);
  - a correction by a different actor (D1);
  - what each `Rejected` reason code means;
  - what to do when kind, role or context is unknown.
- **A documentation gap for adopters:** there is no Rejected-reason table and no example native fact in `examples/`. An adopting agent has to reverse-engineer the `authority`, `provenance.source` and `correctionReason` shape from `acceptance.py`.

## 7. Outstanding wider work

- The EM-XCT-06 contour remains partial: Price/FX, calendars, localization and uncertainty are open.
- Deferred operational work: a governed admission-set builder or evidence resolver, a replay/idempotent import adapter, current-head selection, and an existing-Dimension migration path.
- A host-object projection adapter for non-ASCII hosts (D5, if it is not fixed in code).
- Cross-language canonical-encoding vectors.
- Point±difference affine arithmetic, if it is ever needed, under a separately reviewed contract.

## 8. Material adoption risks

1. **Hash-of-incoming admission.** Agents may build admission sets by hashing incoming Pins. Only prose forbids this, and nothing in the code can detect it.
2. **Superseded values presented as current.** Without a head selector, agents may display a superseded value as current.
3. **Mistaking fail-closed rejections for tampering.** Different-writer corrections (D1), non-ASCII hosts (D5) and revoked historical admission all produce such rejections.
4. **`compare` output used as tolerance or acceptance decisions.**
5. **Synthetic acceptance cited as production readiness.** It covers three new Dimensions, one toolchain pin, and in-memory negatives.

**To reach ACCEPT WITH LIMITS:**
- fix D1 (in code or in the docs);
- fix D2 and D3;
- add native unit tests for D1–D4;
- rerun and republish the test and acceptance digests.

D4 to D10 can ship as documented limits or doc edits.
