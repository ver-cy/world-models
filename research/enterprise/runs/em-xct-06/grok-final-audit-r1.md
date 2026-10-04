**ACCEPT WITH LIMITS**

Independent no-tools review of the supplied EM-XCT-06 0.1.0 text only. Tests were not executed. Declared SHA-256 values, `test-results.json`, `acceptance-results.json`, `tool-pins.json`, parent-model bytes, and live catalogue/toolchain pins are **supplied assertions**, not independently hash-verified or provider-executed facts. This verdict is review evidence, not publication authority.

The bounded slice — same-currency exact summation, explicit increment/mode/stage, residuals, immutable correction pins, fail-closed version/unknown-field handling — is internally coherent and does not invent a second monetary master. Defects below are real but fail-closed or documentary. None is a silent wrong-total or identity-overwrite path.

---

## Defects

### M1 — Medium — advertised bounds are not simultaneously satisfiable
**Where:** `monetary.py` `compute()` / `fixed()` output-capacity check; `model-spec.md` / `agent-guide.md` “36 digits / 18 fraction / 256 inputs / 42-digit output”.
**Counterexample:** one legal input `amount="9"*36`, `declaredScale=0`, `policy.increment="0.000000000000000001"` (18 places). Exact value is a 36-digit integer; lexical `roundedTotal` at increment scale is 36 integer digits + 18 fraction digits = 54 digits, which `require(..., 'output-capacity')` rejects. `256 × ("9"*36)` is already ~39 integer digits **before** a fine increment. `test_boundaries` only uses fixture increment `0.01` (~41 digits) and therefore does not witness the advertised envelope.
**Fix:** either raise the output cap to cover `36 + ceil(log10(256)) + 18` (about 57 digits plus sign/dot), or lower the jointly advertised input/count/increment-scale limits so they fit 42, and add a worst-case unit test. Until then, treat 42 as a **coupled** fail-closed cap, not an independent capacity claim.

### M2 — Medium — schema is not the closed type contract it claims to be
**Where:** `monetary.schema.json` `$defs.Policy.increment`; `model-fields.md` (“monetary.schema.json is the closed cardinality/type contract”).
**Counterexample:** increment `"-0.01"` or `"0"` is schema-valid. `compute()` then does `quantum=amount(...)` and `require(quantum>0,'nonpositive-increment')`. Same pattern for amounts: schema allows 36 integer + 18 fraction digits (and `maxLength` 55 vs a signed form that can be 56 chars); `amount()` separately caps **total** digits at 36. Instant pattern is lexical `\d{4}-...` and admits `2026-02-30T24:99:99Z`; only `stamp()` rejects it.
**Fix:** make increment a **positive** decimal pattern (no leading minus, not all zeros); align amount `maxLength`/digit grammar with the 36-total-digit rule; either tighten the instant pattern or stop calling the schema a complete closed contract. Keep the Python checks.

### L1 — Low — inverted native error code; object identity only half-bound
**Where:** `monetary.py` `validate_native()`; `acceptance.py` `native_pair()`.
**Counterexample:** the check is `recordedAt >= computedAt`, but the code is `'native-recorded-before-computed'`. `validate_native` binds `object.objectId` and `objectType`, and `factId = sha256(canonical({dimension,id,digest}))`. It does **not** check `object.recordId`, `object.recordedAt` vs `fact.recordedAt`, or `previousRecordId`. Acceptance constructs `recordId` as `sha256(dimension,id)` outside the companion.
**Fix:** rename the error; decide whether object `recordId`/clock binding is in companion scope and test it.

### L2 — Low — register bound vs “exact replay is idempotent”
**Where:** `monetary.py` `import_receipts()` `len(existing)+len(incoming)<=256`; `model-spec.md` “including replays”.
**Counterexample:** a complete 256-receipt register cannot accept one additional list item, even an exact replay or a new correction (`256+1` fails before merge). Idempotent replay at capacity only works as `import_receipts(full, [])` or by replacing the incoming list, not by appending.
**Fix:** bound **unique IDs after merge**, or state that a full register cannot be replay-checked or corrected without dropping an item from the call.

### L3 — Low — unit-test gaps vs claims
**Where:** `test_monetary.py` vs `acceptance.py` / advertised native and history behavior.
**Missing:** branching successors (two new IDs, one predecessor); issuer/subject change at import; supersedes digest mismatch as its own case; `amountRole`-only context mismatch (caught by `==` but not named); increment lexical `0.10` vs `0.1`; `validate_native` entirely; `recordedAt < computedAt`; multi-item floor/ceiling/toward-zero; 256-register +1.
Covered: per-item vs after-sum on startup, cancelled residuals still inexact, digest reseal, self-supersession, missing predecessor, same-ID conflict, version/unknown fields, currency-tuple and basis/time mismatch, 200-token single-item Decimal oracle **if** that file is later executed.
**Fix:** add those cases to the unit suite so native/history claims do not live only in an external-toolchain script.

None of L1–L3 yields a silent accepted wrong total in the supplied code.

---

## Not defects — documented host assumptions and deferred scope

- **Host-admitted currency and `allowed_issuers`:** `issue()` seals any URN-shaped issuer. Admission is only on `import_receipts` / `validate_native`. `resolution: host-admitted` is a schema const, not authentication. `adoption-limits.md`, `agent-guide.md`, invariant 16 are explicit.
- **Source truth, allowed sign, aggregation purpose, rights, CAS, retention, current status:** not implemented. Pins are opaque byte citations.
- **Same currency, different context:** refused. Currency equality is the full `{catalogue, edition, snapshotDigest, code, resolution}` tuple. Context equality is `{basis, valuationAt, amountRole}`. No implicit FX or “same EUR code” conversion.
- **Source-slot identity:** unique by `source.id` only, as specified. Same slot ID twice is refused; two slots with the same amount are allowed.
- **Correction:** new ID + exact predecessor pin + non-blank reason; old bytes unchanged. `import_receipts` checks pin digest, subject/issuer continuity, `computedAt >=`, acyclicity. Branches do not pick a current winner. `issue()` does not resolve the predecessor (no I/O) — documented.
- **Rehash tampering:** `validate()` requires digest match **and** `result == compute(request)`. Changing `roundedTotal` and resealing still fails replay. Acceptance’s `outerAloneAcceptsBadArithmetic: true` is an honest statement that outer V3 does not prove nested arithmetic.
- **Version refusal:** `schemaVersion` const `0.1.0`, `additionalProperties: false`. Unknown fields and `0.2.0` fail closed in the supplied tests’ design.
- **Native outer vs nested:** contract is honest **only if** the host actually calls `validate_native` and `import_receipts` in addition to V3. There is no automatic hook. Native fact `supersedes` is required empty; receipt supersession lives inside the nested value; correction is a new object. Intentional.
- **256/2 MiB/depth 16:** reference fail-closed caps, not production scale or a DoS certification.
- **Quantity × price, FX, calendar/DST, localization, current-selector, existing-Dimension migration, payment/posting:** unimplemented and disclaimed.

---

## Are the contracts honest and sufficient?

**Bundle / layer / question tree (`spec.json`):** 4 bundles, 8 layers, 21 findings / questions / artifacts / actions. Every question is `governed-context` and names gaps rather than inventing authority, rates, or defaults. That is sufficient for this slice (exact same-currency sum + explicit quantize). It is not a general money, ledger, or policy engine. Risk: `answer_data[0]` looks like a ready answer; an agent that treats the artifact name as resolution without host evidence would misuse it. `AGENTS.md` / `agent-guide.md` correctly say routes return insufficient-context.

**Whole-object (`whole-object-coverage.yaml`):** `MonetaryCalculationReceipt` identity is required. Nested `MoneyInput`, `CurrencyReference`, `ValuationContext`, policy snapshot, pins, `Rational`, `Step` are correctly **not-applicable** as independent masters. Matches the code: snapshots inside one receipt, no separate money lifecycle.

**Layering vs 032:** `composition.yaml` / `crosswalk.json` “narrow semantic overlap; no subtype/inherited contract” is honest. This package does not import the 032 schema, does not ship a catalogue, and tells hosts to adapt an existing calculation/audit record instead of minting a duplicate receipt for every amount.

**Does this invent a duplicate monetary master?** No, if adopted as specified. It is an optional calculation-evidence type. Embedded amounts remain source-owned snapshots. Result `authority` is const `calculation-only`. Naive installation as “the money system” would be host misuse, which the adoption docs already forbid.

---

## Arithmetic slice (signs / ties / stages)

`round_units()` on increment counts:

| Mode | Rule as implemented | Signed tie e.g. −2.5 units |
|---|---|---|
| half-even | tie → even **\|q\|**, then reapply sign | −2 |
| half-away-from-zero | `2r >= d` → away from zero | −3 |
| toward-zero | truncate \|q\| | −2 |
| floor | Python `//` toward −∞ | −3 |
| ceiling | `−((−n)//d)` | −2 |

That matches the written spec. Startup `3×0.495` half-even `0.01`: per-item `1.50`, after-sum `1.48`. Matrix `−1.025+2.075`: per-item `1.06`, after-sum `1.05`. Cancelled per-item residuals still set `inexact`. AI large+eps keeps a non-zero residual and `inexact=true` even though `roundedTotal` looks clean. Negative-zero **inputs** are refused; output zero is unsigned.

The Decimal oracle mapping (`HALF_UP` = ties away from zero, not toward +∞) matches the integer-unit rule **on paper** for the tested terminating increments. That grid was not re-run here.

---

## Remaining wider research (must stay open)

- Quantity/unit (008): quantity × price, physical conversion.
- Time/calendar (009): working-day/DST/leap-second policy; 010 is Location and is not an import.
- Localization (031): designations, formatted cash increments.
- FX observation and conversion; live catalogue authentication.
- Current-effective selector, withdrawal/tombstone, historical issuer admission as a distinct host decision.
- Production paging, retention execution, append-only/CAS storage.
- Parent WM-XCT-032 / 008 / 009 / 031 publication holds (live re-fetch, paywalled clause text, single-provider waivers, empty relationship contracts). This companion does **not** clear them.
- Independent second-provider **execution** of this slice (unit + pinned native toolchain) and hash verification of pins.

Install only as a reviewable-draft companion where the host already needs an independently addressable calculation receipt, after reading the full package including `adoption-limits.md`. Five native install assets are not a substitute for that package.
