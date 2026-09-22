ACCEPT WITH LIMITS

Independent text-only review of the supplied 0.1.0 bytes. Hashes, installed-byte checks, test-results.json, acceptance-results.json and source-verification.json are Codex evidence and were not re-executed or rehashed. No registry is proposed. Documented deferrals are not treated as missing metrology.

## Defects

**Low — `quantity.py` / `validate_correction` / `correction-link`.** `previous.factId` must be a `str`, but `current.factId` is only required to differ. Counterexample: `current` omits `factId` (`None`) or sets `factId=""` / `factId=123` while `supersedes == [previous.factId]` and every other native field is legal — the pair is accepted. Necessary fix: require `type(current.get('factId')) is str and bool(current['factId']) and bool(previous['factId'])` (and optionally the same non-empty string rule on `validate_native`). Outer V3 is documented to run first and likely already demands IDs; this is a companion-alone hole, not a wrong-number path.

**Low — `quantity.py` / `validate_native`.** `factId` is never inspected on a single fact. Companion-alone, same class as above. Fix: non-empty string `factId` after the documented outer V3 check, or state explicitly that fact identity is solely an outer-envelope concern.

**Low — `quantity.schema.json` `$defs/Factor.n` vs `model-spec.md` / `spec.json` model.scope.** Spec says “at most 36 digits per component.” Schema `maxLength: 36` counts the leading minus, so a negative offset may only carry 35 digits. `b` for affine points can be negative. Necessary fix: align the bound (pattern that excludes the sign from the digit budget, or spec text “36 characters”). No wrong-value path; `rational()` still demands reduced form.

**Low — `quantity.py` / `result`.** The 256-digit `Result` cap is not enforced at pack time. A theoretically oversized reduced fraction would fail later in `validate`/`convert` as `schema`. Fail-closed. Fix: reject inside `pack`/`result` with an explicit reason if desired. One-hop size from 36-digit factors plus a 36-digit/18-fraction magnitude stays well under 256 after reduction.

**Low — test/acceptance coverage, not contract.** `acceptance.py` stores only `quantity.conversion` facts. `quantity.value` plus `MissingMagnitude` is implemented and unit-tested, not natively installed. The acceptance negative that mutates `path` to `quantity.value` on a conversion fact raises `native-path` before `correction-path`. Label issue only; `correction-path` is reachable when previous and current have different nested formats each on their matching path.

None of the above changes a computed coordinate, collapses kind into dimension, turns unknown into zero, or creates a Quantity/UnitRegistry identity.

## Explicit host assumptions (not defects)

- `admitted` is caller-supplied. Hashing the incoming payload and calling that “admission” is forbidden by AGENTS.md / Q03; the API cannot detect the cheat.
- Current read/write rights, Dimension identity, object revision, fact head, source authenticity, definition authority and physical truth stay outside `quantity.py`.
- `validate_native` arguments `subject` / `master` / `writer` / `access` come from authenticated host context, not the record.
- `Pin.sha256` is an upstream evidence digest under a host byte convention; local admission hashes the whole Pin or the whole `UnitDefinition` with this package’s encoding. Different values.
- A host may admit an internally inconsistent catalogue (kind vs dimension vs formula). Conversion still requires exact kind + dimension + anchor equality on the pair.
- `precisionMeaning` and `exact-by-definition` are host assertions. Arithmetic uses the supplied numeral exactly.
- Space-only `MissingMagnitude.reason` is schema-legal; sufficiency is a host check. `correctionReason` is stricter (`strip()` nonempty).
- Real host objects with non-ASCII names, more than 32 keys, nested depth, or integers outside ±9999 cannot be passed whole into `validate_native` / `canonical`. Spec already forbids silent field-stripping and requires a separately specified adapter.
- Duplicate-ID refusal lives in the pinned `write_record` tool, not in this module.
- Fixture host types (`ServiceEstimate`, `RoutePlan`, `ThermalSample`) are synthetic, not published metamodels.
- Python 3.12.14 + jsonschema 4.26.0 are the tested runtime; other languages are not certified.

## Deferred scope (not defects)

No UCUM parser, QUDT adapter, uncertainty, rounding policy, nonlinear/log units, ordinal/nominal scales, rational dimension exponents, general addition/subtraction, point±difference algebra, price/FX/calendar/locale, independent conversion receipt, current-head selector, idempotent import, finite `validTo`, retraction, tombstones, existing-Dimension migration, or automatic companion dispatch. `logicalKind=embedded-value-profile` and catalogue `kind=companion-contract` match the code: delivery envelope, not instance classes. MonetaryCalculationReceipt is correctly left unpublished here.

## Focus checks

**Affine point / difference / scalar.** `result()` implements the spec: point `(a_s·x + b_s − b_t)/a_t`; scalar and difference `a_s·x/a_t`. `unit()` requires `a > 0` and `scalar ∈ roles ⇒ b = 0`. Difference-only snapshots may carry a leftover `b`; it is ignored, which matches “suppress offsets,” not “b must be zero.” Hand checks on the supplied fixtures: 32 F point → 0/1 C; 18 F difference → 10/1 C; 2.00 F point → −50/3 C; 1.250 h → 75/1 min; 12.50 km → 12500/1 m. UCUM 2.2 post-offset mapping `a=5/9`, `b=45967/180` and Celsius `a=1`, `b=5463/20` is the stated normal form, not a silent QUDT pre-offset copy. Target role must be declared on the target snapshot.

**Kind versus dimension.** Separate fields, separate errors (`kind-mismatch`, `dimension-mismatch`, `anchor-mismatch`). Kind is exact Pin equality, not URI equality and not inference from `code` or from the seven integer exponents. Energy vs torque with identical `[2,1,-2,0,0,0,0]` is refused. Integer exponents −12..12 only.

**Source notation.** `KnownMagnitude.lexical` and `scale` are preserved on the retained input, including signed zero (`-0.00`). Scale must equal the actual fractional-digit count (companion rule; schema does not encode it). Result is a reduced unsigned rational; original decimal is not rewritten into the result.

**Unknown states.** `unknown` / `withheld` / `not-applicable` validate as `QuantityDocument` after unit/role/context/source admission and never become 0, unit one, or a fabricated precision. `convert` / `compare` / `ConversionDocument` fail `non-numeric`. Missing unit is `schema`, not substitution of `1`.

**Admission.** Exact three set/frozenset keys; members are 64 lowercase hex local digests. Lists and raw strings are rejected. Definition revision and source/context Pin revision change the hashed object. Same current sets are used for a correction pair, which is “inspect historical snapshots under current admission,” not write authorization.

**Rational bounds and canonical bytes.** `rational()` requires `str(Fraction.numerator|denominator)` to match the supplied strings. `pack()` emits reduced form, sign on numerator, zero as `0/1`. `canonical` / `digest` / `load` match the written ASCII contract (sorted keys, `separators=(',',':')`, only `"` and `\` escaped, slash unescaped, lowercase literals). The supplied vector `{"z": true, "a": "\"\\", "n": null, "i": -2}` is the correct byte string. `load` rejects duplicate keys, float/exponent/nonfinite tokens, oversized wires, and then applies bounds. RFC 8785/JCS compatibility is correctly not claimed.

**Native stored binding and pairwise correction.** After caller-supplied host parameters: subject triple match; `masterSystem` + `authority == {source: writer, rank: 0}`; accessClass on object and fact; `status=asserted`; outer `unit` null; `validTo` null; capture `provenance.source == master` distinct from the nested source Pin; path tied to nested `format`; UTC-seconds stamps. Correction is a supplied pair: distinct IDs (with the Low hole above), exact predecessor list, same path, nondecreasing `recordedAt`, nonempty stripped reason. Original bytes are not rewritten by the companion. Outer V3 accepting a tampered nested `result` while the companion raises `replay-mismatch` is implemented in `acceptance.py` and is invariant 17, not an accident.

**Current authority limits and adopting-agent docs.** AGENTS.md is an adequate entrypoint if the agent actually reads pinned `spec.json`: five operational files, no independent Quantity, do not hash untrusted input into `admitted`, outer V3 then explicit nested validation, synthetic install is not a live company binding, question tree when evidence is missing, never manufacture zero/unit/confidence/approval. `model-spec.md` and `spec.json` `model.scope` carry the same contract. `factMastership` matches `mastership-and-rights.yaml`. Publication manifest stays `candidate-not-yet-published` / contour `partial`.

## Four bundles, eight layers, twenty routes, five facets

The tree is honest, not decorative.

- QV-B1 Embedding + Definition (F01–F04), QV-B2 Magnitude + Compatibility (F05–F10), QV-B3 Formula + Result (F11–F15), QV-B4 Storage + Adoption (F16–F20): 4 bundles, 8 layers, 20 findings, each with one question, one artifact, one action.
- Host-only routes (F01, F02, F12, F15, F18–F20) are labeled host-guidance and do not pretend the companion authorizes billing, access, or import skip.
- Local routes (F05, F08, F13, F14) match code (absence preserved, kind≠dimension, nonlinear refused, replay required).
- Nine `$defs` shapes × five facets. `identity-class: not-applicable` on embedded values, magnitudes, factors, results and wire wrappers is true. `UnitDefinition` and `Pin` require identity-class as external snapshot tuples, not a local master. That is a usable bounded profile for an adopting agent, provided they follow AGENTS.md and do not stop at jsonschema.

Schema without the companion will accept a `ConversionDocument` whose magnitude is non-numeric and whose `result` is an arbitrary canonical rational. That is why Q14, invariant 17 and AGENTS.md make nested validation mandatory. An agent that ignores those sentences is out of contract.

## Material adoption risks

1. Outer V3 alone accepts tampered nested arithmetic. Production must invoke `validate` / `validate_native` on stored bytes.
2. Caller-built admission sets and caller-supplied access parameters are not evidence and not authorization.
3. `canonical(host_object)` bounds will reject ordinary enterprise objects; an adapter must be specified, not improvised by stripping fields.
4. Pairwise correction is not a history engine, not a head selector, and not an authorization to change kind/source.
5. Rank 0, `validTo` null, `status=asserted` only. Finite intervals and retraction need a later mapping.
6. Three synthetic Dimensions and fixture pins prove installation shape only. They do not authenticate a live binding.
7. Independent implementations of the digest encoding are uncertified.
8. Exactness of admitted `a`/`b` is not physically checked. Admitting a QUDT pre-offset snapshot as `definition-exact` will compute a different number with no companion warning beyond “you admitted it.”

## Outstanding wider work

Already named in Q20, adoption-limits.md, research.md and the parent contour: Price/FX, working calendars, localization, uncertainty/calibration, nonlinear units, existing-Dimension migration, idempotent replay adapters, rights/head selection, and the rest of EM-XCT-06. Parent WM-XCT-008 remains a semantic reference (digest declared in `composition.yaml` / `spec.json`); this package does not inherit it at runtime and does not claim UCUM/QUDT/ISO conformance. Publication authority remains with the user.
