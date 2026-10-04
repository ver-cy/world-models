ACCEPT WITH LIMITS

Static review of the supplied candidate only. Codex hashes, `test-results.json`, `acceptance-results.json`, toolchain pins and prior provider studies are evidence in the dossier, not independently executed or re-hashed here. No new registry is required. Documented deferrals are not treated as missing claimed metrology.

## Exact affine formulas — no wrong-value defect

`quantity.py` `result()` implements the contract in `model-spec.md` / `spec.json` model.scope:

\[
\text{point: }(a_s x + b_s - b_t)/a_t \qquad \text{scalar/difference: } a_s x / a_t
\]

Code: `pack((a*x+(b-d if q['role']=='point' else 0))/c)` with \(a,b\) from source and \(c,d\) from target.

Counterexamples that algebraically match fixtures, examples, tests and acceptance:

- 32 F, \(a=5/9\), \(b=45967/180\) → C \(a=1\), \(b=5463/20\) → \(0/1\)
- 18 ΔF → 10 ΔC (offsets suppressed)
- reverse 0 C → 32 F; 10 ΔC → 18 ΔF
- 2.00 F → \(-50/3\) (acceptance `ai.secondResult`)
- 0 C toward a target with \(b=-1\) → \(5483/20\)
- 1.250 h → 75 min; 12.50 km → 12500 m

UCUM post-offset normal form is used; QUDT pre-offset/finite-multiplier columns are not silently imported. Signed-zero lexical form is kept on input; rational output is unsigned `0/1`.

## Kind versus dimension — implemented as claimed

`compatible()` requires exact `kind`, `dimension` and `anchor` pin equality. Equal SI exponents with different kind pins are refused (`kind-mismatch`; energy vs torque `[2,1,-2,0,0,0,0]`). Dimension is seven integers in \([-12,12]\), not rational exponents. Scalar conversion also requires the same anchor. Kind is never inferred from code, dimension or UCUM annotation.

## Source notation, unknown states, admission

- KnownMagnitude: ASCII decimal lexical + matching scale; pattern rejects `+1`, `01`, `1e2`, grouping, `1.`, `NaN`. Max 36 digits / 18 fractional.
- MissingMagnitude `unknown` / `withheld` / `not-applicable` validates and stores; `convert` / `compare` raise `non-numeric`. Missing unit is `schema`, not unit one. Explicit unit `1` is allowed when admitted.
- `admitted` is exactly three sets/frozensets of 64-hex digests. Definition digest is the whole `UnitDefinition`; source/context digest is the whole `Pin`. `Pin.sha256` is an upstream evidence hash and is not the local admission digest. Building those sets from untrusted incoming bytes is a documented host duty.

## Rational bounds and canonical bytes

- Factors: reduced \(n/d\), positive denominator, \(a>0\), scalar \(b=0\), component length ≤36 including sign. `rational()` rejects unreduced pairs (`2/4` → `noncanonical-rational`).
- Result schema cap is 256 characters per component. `pack()` does not enforce it locally; overflow fails later as `schema` (or `ascii-string` if a component exceeds 1024). Fail-closed, untested at the bound.
- `canonical()` is sorted-key compact ASCII JSON; slash is not escaped; only `"` and `\` are escaped in strings. Encoding vectors in `test_quantity.py` match the written byte contract. RFC 8785 / other-language compatibility is not claimed.

## Native stored binding and pairwise correction

`validate_native` binds one stored fact after outer V3 and a caller-supplied subject/master/writer/access:

- Paths: `quantity.value` ↔ QuantityDocument, `quantity.conversion` ↔ ConversionDocument.
- Outer `unit` and `validTo` keys must be present and null; status `asserted`; `authority == {source: writer, rank: 0}`; `masterSystem` and `provenance.source` equal the capture master.
- Only four host fields are companion-checked (`recordType`, `schemaVersion`, `objectId`, `accessClass`). Non-ASCII host name is out of scope and is an explicit outer-V3 concern.
- One semantic quantity per existing host, two slots, no field qualifier: host-enforced inventory; the checker does not scan sibling facts.

`validate_correction` is a supplied-pair checker: distinct nonempty IDs, `current.supersedes == [previous.factId]`, previous `supersedes` is a list, direct two-cycle refused, same path, same input kind/dimension/anchor/role/context, nondecreasing `recordedAt`, nonblank `correctionReason`, same master/writer/access, defensive copy returned. It does not authorize the write, select a head, or close a longer graph.

Acceptance text shows predecessor bytes captured before correction append and rechecked after append, pair validation and tamper restore; duplicate native append refused; outer V3 accepts a tampered nested result that the companion rejects as `replay-mismatch`. Those outcomes are Codex evidence, not re-run here.

## Limits that are real, not host assumptions

**L1 — LOW — Result length cap is schema-late, not local.**  
File/function: `quantity.py` `result()` / `pack()` / `validate()`.  
Counterexample: an admitted conversion whose reduced numerator or denominator exceeds 256 characters is not rejected inside `pack()`; `convert()` then fails `schema` (or `ascii-string` above 1024).  
Fix if tightened: check lengths in `pack()` and raise a dedicated reason already listed in the failure table, or name both possible codes next to the 256-character rule. Not a wrong-value path for the tested fixtures.

**L2 — LOW — “supersedes containing” vs singleton list.**  
File/function: `model-spec.md` / `spec.json` Native V3 paragraph vs `quantity.py` `validate_correction()`.  
Counterexample: `supersedes: [previous.factId, otherId]` matches the English “containing the exact prior fact ID” and fails `correction-link` because the code requires equality with a one-element list.  
Fix: change the prose to “exactly `[predecessorFactId]`” to match the pairwise API. Fail-closed, not a silent accept.

**L3 — LOW — correction-semantics does not freeze unit snapshot or conversion target.**  
File/function: `quantity.py` `validate_correction()` (kind/dimension/anchor/role/context only).  
Counterexample: replace km with m (same kind/dimension/anchor) and keep lexical `12.50`, or retarget a conversion; each document still has to replay, but the pair is a legal “correction.”  
Necessary adoption rule: treat unit-code / \(a,b\) / target changes as a separately governed definition revision, not a typo-fix. The preserve-list in the contract matches the code; do not read “unit-definition revision” as “same unit.code forever.”

**L4 — LOW — standalone `supersedes` is not typed in `validate_native`.**  
Only the pair function requires a list. Outer V3 / host fact schema is assumed. Not a claimed graph engine.

**L5 — LOW — example `admissionFixture` arrays.**  
`examples/startup.json`, `matrix.json`, `ai.json` carry serialized digest lists plus an explicit notice that they are not API sets. Copying them as live `admitted` is an adopting-agent footgun. Operational tests build sets from `digest()`.

**L6 — INFO — unused offset on difference-only units.**  
`scalar-offset` fires only when `'scalar' in roles`. A difference-only definition may carry nonzero \(b\); `result()` ignores it. Harmless.

**L7 — INFO — `precisionMeaning` does not change arithmetic.**  
Both `reported-digits` and `exact-by-definition` use the supplied numeral exactly, as specified. Exactness remains host evidence.

**L8 — INFO — error-code crowding on native ASCII.**  
`validate_native` runs `canonical(fact)` first. A non-ASCII subject/writer/reason can surface as `ascii-string` rather than `native-context` / `native-id`. Per-record ASCII is already a stated bound.

None of L1–L8 produce a wrong rational for admitted in-profile inputs, turn unknown into zero, equate kind with dimension, or compute on an unadmitted snapshot.

## Explicit host assumptions (not defects)

- Construction and purpose-binding of `admitted` sets; `Pin.sha256` byte convention; definition/source/context truth.
- Current read/write rights, disclosure, head selection, full supersession graph, finite `validTo`, retraction, tombstones, retention.
- Host enforcement of one-quantity slot inventory; refusal to mint dummy hosts to evade it.
- Conversion staleness between `quantity.value` and `quantity.conversion`.
- Clock plausibility and measurement time (this profile stores assertion UTC seconds only).
- Physical correctness of an admitted \(a,b\) labelled `definition-exact`.
- Outer V3 validity of the rest of the host object (name, description, objectType, unrelated fields).

## Documented deferred scope (not defects)

Multi-field native adapter; separate-actor / changed-access correction; idempotent import; UCUM parser; uncertainty / calibration; general addition (including point±difference as an affine-space operation); Price / FX / calendar / locale; other-language canonical certification; existing-Dimension migration; production catalogue publication. `review.json` is correctly absent until after this freeze. `publication-manifest.draft` is `candidate-not-yet-published` / `reviewable-draft` / contour `partial`.

## 4 / 8 / 20 / five-facet claim

Present and consistent with this bounded profile, not with a Quantity/UnitRegistry product:

- 4 bundles QV-B1–B4, 8 layers, findings QV-F01–F20, each with one question, one artifact and one action (`spec.json` `statistics` matches the tree).
- 9 embedded shapes × 5 facets in `wholeObjectFacets` and `whole-object-coverage.yaml` (identity-class, direct-properties, recognition-observation, capabilities-behaviour-actions, context-evidence). Facet statuses match the code: QuantityValue has no independent identity; Pin has no fetch behaviour; MissingMagnitude is storage-only; Result is replay, not a new observation.
- Question routes are bounded guidance. They do not grant authority. QV-ACT13 omits the “host permission” suffix because it is a local unsupported-transform refusal; that is consistent.

Five operational files (`spec.json`, `AGENTS.md`, `runtime-model.reference.json`, `quantity.schema.json`, `quantity.py`) are a usable installed contract if the host already has subject, definition, source, context and current permissions. Evidence files do not alter that contract.

## Current authority limits — documentation is sufficient if read as written

`AGENTS.md` states the order: real host subject → resolve evidence under current authority → build admission sets → outer V3 → explicit nested `validate` / `validate_native`. Failure-reason table tells the agent not to retry by widening admission or replacing bytes. Synthetic installer `publicationStatus=published` is labelled simulated. Limits in `adoption-limits.md`, `invariants.md`, `lifecycle/embedded.md` and `migration.md` agree with the executable subset.

An adopting agent who skips `AGENTS.md` and treats example admission arrays, outer V3 success, or a conversion result as authorization will misuse the profile. That is an adoption risk, not an implementation claim of those powers.

## Outstanding wider work and material adoption risks

1. EM-XCT-06 remains partial. Price, FX, working calendars, uncertainty and localization are still open; this package plus the separate monetary increment does not complete the contour.
2. Companion invocation is mandatory. Outer V3 will accept an invalid nested `result`; only `validate` / `validate_native` replay the affine identity.
3. Native slot inventory and current access are host work. This checker will validate one well-shaped fact on an old object snapshot.
4. Correction 0.1.0 is same-master / same-writer / same-access only. A changed capture actor needs another workflow; the refusal is not a tamper finding.
5. Canonical bytes and schema pin are this Python 3.12.14 + jsonschema 4.26.0 reference. Supply-chain and cross-language equivalence are not certified.
6. Three synthetic Dimensions and reviewable-draft assets are not a live company binding.
7. The 201-case Decimal oracle is a finite-precision comparison against UCUM’s pre-offset Fahrenheit formula, not physical or domain proof.

Publication authority stays with the user. This verdict is evidence only.
