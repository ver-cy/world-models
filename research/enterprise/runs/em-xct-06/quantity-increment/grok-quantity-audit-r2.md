ACCEPT WITH LIMITS

Independent implementation audit of supplied candidate text only. No execution, hash recomputation, toolchain inspection, or external source verification. Codex reports and declared digests are evidence claims, not confirmed here. Publication authority remains with the user.

The bounded profile is internally consistent: exact affine point/difference arithmetic matches the stated formulas; kind is not collapsed into dimension; unknown states do not become zero; admission is explicit; native binding and pairwise correction are narrow and fail-closed; documentation is sufficient for an adopting agent that actually reads `spec.json`/`AGENTS.md` and invokes `quantity.py`. Documented deferrals are not treated as missing implementation. The package does not create an independent Quantity or UnitRegistry instance.

## Concrete residuals (limits, not freeze-breakers)

**L1 LOW — `quantity.py` / `validate_native` / ID grammar.** `factId` and `subject` use `bool(s)`; `master`, `writer`, and `correctionReason` use `.strip()`. Counterexample: `subject=' '` and matching `objectId`/`subjectId` pass `native-subject`; `factId=' '` passes `native-id`. Contract already splits the wording (IDs nonempty, master/writer nonblank). Not an arithmetic or authority-grant bug. Fix if retouched: reject whitespace-only IDs, or document that space is a legal nonempty ID and belongs to outer V3.

**L2 LOW — `quantity.py` / `result`+`pack` / Result cap.** The 256-character Result bound is enforced by schema after computation. Overflow reason is `schema`, not a dedicated code. Fail-closed; no wrong value is accepted. Legal Factor/magnitude sizes are far below 256. Fix if retouched: raise a distinct `result-bounds` and add it to the failure table.

**L3 LOW — `quantity.py` / `validate_correction` / return alias.** `validate()` and `validate_native()` return `copy.deepcopy(...)`. `validate_correction` returns `current['value']` live. Counterexample: `v=validate_correction(prev,curr,host,**opts); v['result']['n']='1'` mutates `curr` in memory. Does not write storage. Spec promises a defensive copy only for `validate()`. Fix if retouched: `return copy.deepcopy(current['value'])`.

**L4 LOW — `quantity.py` / `validate_correction` / `correction-cycle`.** Missing `previous.supersedes` is reported as `correction-cycle` because `type(None) is not list`. Fail-closed; fixtures always supply `supersedes:[]`. Fix if retouched: type-check under `correction-link`, then membership under `correction-cycle`.

**L5 LOW — `quantity.py` / `validate_native` / `native-state`.** `fact.get('unit') is None` and `fact.get('validTo') is None` treat omitted keys as null. Spec text says those fields must be null. Unreachable if outer V3 requires the keys first, which this contract demands. Fix if retouched: require key presence and null value.

**L6 DOC — `quantity.schema.json` vs `quantity.py`.** Schema alone accepts unreduced `n/d`, non-positive `a`, scalar+nonzero `b`, and an arbitrary `result`. Replay, admission, kind/dimension/anchor, role, and native binding live in `quantity.py`. Documented, but a real adopting-agent footgun if someone validates only the JSON Schema.

**L7 DOC/TEST — coverage gaps, not wrong accepts.** Withheld/not-applicable convert/compare refusal is implied by `state!='known'` but only `unknown` is asserted in tests. Inverse C→F is algebraically 32 and untested. `AGENTS.md` cites `review.json`; that file is not in this freeze (`review.md` is). Example `admissionFixture` arrays are illustrations and are not consumed by `test_quantity.fixture()`.

**L8 DOC — failure-table presentation.** `model-spec.md` uses “Table cells:” lists; `spec.json` `model.scope` uses markdown tables. Semantics match. Authoritative executable copy is `spec.json`.

These are not reachable wrong-value defects for admitted inputs.

## Affine point/difference

`quantity.py` `result()`:

`pack((a*x+(b-d if q['role']=='point' else 0))/c)`

matches the contract: point `(a_source*x + b_source - b_target)/a_target`; scalar/difference `a_source*x/a_target`.

Checked against supplied fixtures and tests (algebra only):

- 1.250 h → 75 min (`3600/60`)
- 12.50 km → 12500 m
- 32.0 °F → 0/1 °C: `(5/9)*32 + 45967/180 - 5463/20 = 0`
- difference 18.0 °F → 10/1 °C: `(5/9)*18`
- 2.00 °F → `-50/3` °C
- inverse 0 °C → 32 °F: `(5463/20 - 45967/180) / (5/9) = 32`

`unit()` rejects `scalar` in `roles` when `b != 0` for the whole definition. Difference applies neither source nor target offset. `compare` converts left into the right-hand unit after context/role equality; unknown left dies in `convert` (`non-numeric`); unknown right dies in `scalar` (`non-numeric`). No kind collapse: energy vs torque with identical `[2,1,-2,0,0,0,0]` is `kind-mismatch`.

UCUM 2.2 mapping in the spec is consistent with the stored coefficients (`b_F=45967/180`, `b_C=5463/20`). The profile correctly refuses to treat QUDT pre-offset columns as this normal form. Physical truth of an *admitted* `(a,b)` remains a host assumption.

## Kind versus dimension, source notation, unknown states

Kind, dimension, and anchor are separate pins and must all match before conversion. Dimension is seven integers in `[-12,12]`; no rational exponents. Code is an opaque string; no UCUM parser.

KnownMagnitude keeps the accepted ASCII lexical string and matching scale, including trailing zeros and signed zero. `Fraction(lex)` is used for arithmetic; rational output is unsigned zero. Rejected source notation (`+1`, `01`, `1e2`, grouping, `1.`, Unicode digits, control characters, floats) fails closed at schema or `ascii-string`. Raw grouped/exponent/localized notation is required to stay in host source evidence.

`unknown` / `withheld` / `not-applicable` validate and store with the same unit/context/source contract. Arithmetic and comparison refuse them. No zero, unit-one, or confidence is manufactured. Space-only `reason` is schema-legal (`minLength: 1`); sufficiency is an explicit host check.

## Admission, rationals, canonical bytes

`admitted` must be exactly `{definitions, sources, contexts}` as `set`/`frozenset` of 64-char lowercase hex. Definition membership hashes the entire `UnitDefinition`. Source/context membership hashes the entire `Pin`. `Pin.sha256` is a different upstream evidence field. Revision drift without fresh admission is refused. Constructing those sets from untrusted incoming bytes is forbidden by the contract and is an adoption error, not an implementation hole.

Rationals are reduced `n/d` with positive denominator, canonical zero `0/1`, `a > 0`, Factor ≤36 characters, Result ≤256. `rational()` rejects unreduced pairs. Overflow of Result is fail-closed via schema.

Canonical encoding is sorted compact ASCII JSON; the supplied vector `{"z":true,"a":"\"\\","n":null,"i":-2}` matches the documented escape rules. RFC 8785 / other-language encodings are explicitly not certified. `load()` rejects duplicate keys, float/exponent tokens, oversized integer tokens, bad UTF-8, and oversize bytes.

## Native stored binding and pairwise correction

`validate_native` checks expected `subject` against both `fact.subjectId` and `object.objectId`; expected `master`/`writer`/`access` against `masterSystem`, `authority=={source:writer,rank:0}`, and both access classes; `status==asserted`, outer `unit is None`, `validTo is None`; UTC-second `recordedAt`/`validFrom`; `provenance.source==master`; path `quantity.value` vs `quantity.conversion` after nested `validate()`. Only four host-object fields are bounded by the companion; non-ASCII host `name` is intentionally left to outer V3. Rank must be 0. Inspection admission is not write authorization. An old object record is not current access.

`validate_correction` requires the same master/writer/access on both records, distinct nonempty IDs, `current.supersedes==[previous.factId]`, same path, nondecreasing `recordedAt`, nonblank `correctionReason`, and rejects a directly visible two-cycle. Separate-actor / changed-access correction is refused and documented as a compatibility restriction, not tampering. Longer cycles, parallel heads, and current-head selection are host work. Original bytes are not rewritten by the companion; acceptance claims stored tamper-restore and duplicate-append refusal via the outer append tool.

Outer V3 validity does not prove nested arithmetic. Acceptance itself records `outerAloneAcceptsInvalidNestedResult: true` and requires companion `replay-mismatch` on a tampered stored result. That isolation is correct and must not be ignored by adopters.

## Authority limits and adopting-agent documentation

Current authority limits are explicit and consistent across `model-spec.md` / `spec.json` `model.scope`, `AGENTS.md`, `lifecycle/embedded.md`, `mastership-and-rights.yaml`, `adoption-limits.md`, and the failure table: no inferred rights, no source authenticity from pin shape, no physical measurement proof, no billing/conformity authorization from a coordinate, no latest-head selector, no idempotent import, no existing-Dimension migration.

`AGENTS.md` is a usable entrypoint if the agent reads the pinned `spec.json` and then calls outer V3 plus explicit nested validation on stored bytes. Question routes tell the agent which host evidence to request. Suggested actions all carry the host-permission caveat.

## 4 bundles, 8 layers, 20 routes, five facets

Present and accurate as a bounded guidance map, not a workflow engine:

- QV-B1 Host and reference — Embedding, Definition (F01–F04)
- QV-B2 Numeric meaning — Magnitude, Compatibility (F05–F10)
- QV-B3 Transformation — Formula, Result (F11–F15)
- QV-B4 Operation and evolution — Storage, Adoption (F16–F20)

Twenty findings, each with one question, one artifact, one action. Nine embedded shapes × five facets (`identity-class`, `direct-properties`, `recognition-observation`, `capabilities-behaviour-actions`, `context-evidence`) match `whole-object-coverage.yaml`. Identity is correctly `not-applicable` for embedded values; UnitDefinition/Pin identity is the external revision plus local digest, not a new registry master. Counts are not theater. They do not authorize operations.

## Host assumptions (not defects)

Current read/write rights; host object identity and current revision; head resolution and full supersession graph; definition/source/context truth and applicable revision; physical correctness of admitted `a`/`b` and `definition-exact`; clock plausibility and measurement time; reason-string adequacy; kind/role pairing that is domain-meaningful; normalization of raw source notation into this lexical form; outer V3 fact grammar beyond the companion subset; production load.

## Deferred scope (not defects)

Independent Quantity / UnitRegistry / ConversionReceipt / Observation objects; UCUM parser; uncertainty; general addition/subtraction; point±difference as implemented operations; Price/FX/calendar/locale; ordinal/nominal scales; rational dimension exponents; separate-actor correction; current-head selector; idempotent import adapter; existing-Dimension migration; retraction and finite `validTo`; non-Python canonical encodings; production or standards certification. Companion-contract is a shared delivery envelope; `logicalKind=embedded-value-profile` is the instance semantics. EM-XCT-06 remains partial.

## Material adoption risks

1. Building `admitted` by hashing untrusted incoming documents.
2. Treating outer V3 success as nested arithmetic success.
3. Schema-only integration without `quantity.py`.
4. Presenting the three synthetic Dimensions as an authenticated live company binding.
5. Treating `compare()` as interchangeability, tolerance, aggregation permission, or safety.
6. Relabeling a catalogue finite decimal as `definition-exact` without independent authority.
7. Assuming Python 3.12.14 + jsonschema 4.26.0 plus the pinned sibling schema is a hermetic supply chain.

## Outstanding wider work

`deepcopy` on `validate_correction`; dedicated Result overflow reason; withheld/not-applicable arithmetic tests and C→F/K identity tests; whitespace ID grammar alignment if the host ID policy is stricter; separate-actor correction workflow; current-head selector; idempotent import adapter that inspects existing bytes before skip; existing-Dimension migration maps; non-Python encodings; uncertainty / Price / FX / calendar / locale increments; production certification. None of that is required to treat this 0.1.0 embedded profile as a usable bounded candidate.

Review verdict is evidence only.
