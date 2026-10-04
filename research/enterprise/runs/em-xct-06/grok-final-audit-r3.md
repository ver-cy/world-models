**ACCEPT WITH LIMITS**

Independent no-tools static semantic audit of Enterprise Monetary Calculation 0.1.0 (EM-XCT-06 companion). This verdict is review evidence, not publication authority. Declared SHA256 values, `test-results.json`, `acceptance-results.json`, and `tool-pins.json` are supplier assertions: they were not executed, hash-verified, or independently reproduced here. Compact-rendered JSON/YAML is treated as semantic evidence of intended values only. External toolchain and parent-spec bytes are not in this candidate and are not reviewed.

Four independent static reviews (this lead plus Harper, Benjamin, Lucas) agree: no HIGH defect, no MEDIUM defect that changes arithmetic, identity, native isolation, or contract honesty enough to REVISE or BLOCK.

---

## Defects (low / residual)

These are optional tightenings. They do not accept wrong money, mutate sealed bytes, grant authority, or bypass digest/replay.

**L1 — low.** `monetary.schema.json` `Result.roundedTotal` / `Step.rounded`  
Structural `maxLength: 64` only; no ASCII decimal grammar.  
Counterexample: a schema-valid garbage total such as `"1.50 "` or `"999"` still fails `validate()` on `receipt-digest` or `replay-mismatch`, because `issue()`/`validate()` require `result == compute(request)` after the digest check.  
Necessary fix if tightened: reuse the amount decimal pattern and scale rule. Safe to leave if replay remains mandatory (current contract).

**L2 — low.** `monetary.py` `validate_native`  
`native-disclosure-digest` bundles `accessClass == 'restricted'` and `provenance.recordDigest == receipt digest`.  
Counterexample: `accessClass='public'` raises `native-disclosure-digest` (acceptance lists that exact mapping).  
Necessary fix if tightened: split `native-access-class` from `native-record-digest`. Behavior is fail-closed and tested in the supplied suite text.

**L3 — low.** `agent-guide.md` vs `AGENTS.md`  
Same title; `agent-guide.md` omits the hard 256-ID lifetime cap, genesis-only object binding, and narrower envelope bounds that `AGENTS.md`, `adoption-limits.md`, `bindings/native-v3.md`, and `model-spec.md` state. It also says “question routes” where `AGENTS.md` says questions are guidance, not executable routes.  
Necessary fix: make `agent-guide.md` identical to `AGENTS.md` or replace it with a pointer. The installed operational file is `AGENTS.md`.

**L4 — low.** `monetary.py` `validate_native`  
Object `provenance` is only type-checked as a dict. Fact `masterSystem` / `authority` / `recordDigest` are bound; object `source` is not bound to `master`.  
Counterexample: an object whose provenance source is unrelated still passes if the other genesis checks pass.  
Necessary fix if tightened: bind object provenance source to the admitted master. Documented genesis-only scope already requires the host to inspect full native history before access.

**L5 — low / documented residual.** `monetary.py` `issue()` / `validate()` vs `import_receipts`  
`issue()` will seal a well-formed successor whose `supersedes` pin names a missing, wrong-digest, or different-subject predecessor. Only `import_receipts` enforces pin resolution, subject/issuer continuity, chronology, and acyclicity. Isolated `validate_native` on one genesis pair also does not walk the chain.  
Counterexample: `issue({..., supersedes: {id: absent, digest: ...}, correctionReason: "x"})` is locally valid; `import_receipts([],[that])` raises `supersedes-unresolved`.  
Necessary fix: none in this version if hosts follow AGENTS (`import_receipts` on the complete register before store). A host that stores after `validate()` alone can persist a dangling correction.

**L6 — low.** Envelope resource bounds vs tests  
`MAX_BYTES` 2 MiB, depth 16, 32 keys/object, list 256, generic string 512, JSON-int magnitude 9999 are enforced by `bounded()` / `load()` / `shape()`. Dedicated unit tests shown in `test_monetary.py` cover register cardinality, 256 inputs, output width 57, and typed wire errors, not these generic envelope caps.  
Necessary fix if tightened: add explicit boundary tests. Docs already say the caps are fail-closed bounds, not DoS certification.

Not adopted as findings: Policy.increment `allOf` optional-minus copy (AND with the positive primary pattern; `quantum>0` also refuses); unused module-level `VALIDATOR` (shape builds a `$defs` subschema instead); error name `native-recorded-before-computed` (fires only when `recordedAt < computedAt`; exact-code test exists; R1 already declined a rename).

---

## Not defects — documented host assumptions and deferred scope

- Host-admitted currency, issuer sets, source/policy/catalogue pins: trusted caller assertions, not authenticated evidence, catalogue proof, or license.
- Actor-to-issuer binding, digest preimage convention, source re-assertion before reuse of a derived result.
- Current object head, later revisions, retirement, retraction, fact supersession, read/write IAM, CAS, append-only media.
- Production paging, indexing, retention, erasure, current-winner selection, tombstones.
- FX, quantity×price, allocation, tolerance, calendar/DST, localization, existing-Dimension migration, signatures, payment/posting/staffing.
- ISO/SI/accounting/cash-settlement conformance.
- `jsonschema==4.26.0` is version-pinned; no supply-chain hash.
- Parent WM-XCT-032 / 008 / 009 / 010 / 031 research holds and unpaid live source re-fetch remain.
- Five installed native assets ≠ the complete package; `adoption-limits.md` and AGENTS require the full pinned ZIP.
- Fixture `role=core` and `publicationStatus=published` in `acceptance.py` are synthetic delivery artifacts; `researchAssurance=reviewable-draft` and compatibility.scope say they are not live publication or ontology inheritance.
- `test-results.json` (32 tests, 202 oracle cases, Python 3.12.14) and `acceptance-results.json` (3 profiles, fail-stop) are internally consistent with the supplied test text (32 `test_*` methods; 5×10×4+2 oracle loops; golden file hashes match `GOLDEN_DIGESTS`). That is textual consistency, not independent execution.

---

## Adversarial checklist

**Signs / ties / stages.** Five explicit modes. `half-even` ties to an even increment count (`2*r==d and q%2==1`). `half-away-from-zero` uses `2*r>=d` on abs, then sign. `toward-zero` truncates abs. `floor` / `ceiling` use signed `//`, not the abs path. Startup `0.495×3` increment `0.01` half-even: per-item `1.50`, after-sum `1.48`; half-away after-sum `1.49`. Matrix `-1.025+2.075`: per-item `-1.02+2.08=1.06`, after-sum `1.05`. Examples’ rationals match those traces (`297/200`, `21/20`, signed residuals). Negative-zero input refused; output zero is unsigned in `fixed()`. Per-item residuals that cancel still set `inexact=true`.

**Precision limits.** ASCII lexical amounts, no exponent/group/float/leading-plus; 36 total digits / 18 fraction; `declaredScale` must match lexical scale. Increment must be positive (schema lookahead + `quantum>0`). Output cap 57 matches 256 maximal 36-digit inputs formatted at an 18-place increment; `test_boundaries` asserts that width. JSON `integer-bound` 9999 does not clip rationals (string numerators/denominators). Increment lexical form owns result scale (`0.10` vs `0.1`: same Fraction, different `roundedTotal`; tested).

**Same-currency-but-different-context.** Equality is the full Currency tuple (catalogue, edition, snapshotDigest, code, `resolution=host-admitted`) plus exact Context (basis pin, `valuationAt`, `amountRole`). Policy currency must match. Same `EUR` with a different edition/catalogue/digest is refused. Same currency with a different valuation instant, basis, or role is refused.

**Source-slot identity.** `source.id` unique per request; input `key` unique; one slot used twice is refused rather than double-counted. Identical amounts from different slot IDs are allowed.

**Immutable correction.** New ID, exact predecessor pin, non-blank non-whitespace reason, same subject and issuer, `computedAt >=` predecessor. Self-supersession refused. Missing / wrong-digest / transitive-missing pin → `supersedes-unresolved`. Branches retained; no current-winner selector; old receipt bytes unchanged. Status `issued` is implicit; `current` / `superseded` / `withdrawn` are external.

**Rehash tampering.** `validate` pops `digest`, recomputes it, then requires `result == compute(request)`. Changing `roundedTotal` and resealing the digest still fails `replay-mismatch`. Acceptance writes a rehashed nested `999`; outer V3 stays valid; companion rejects. Honest (`MC-Q16`, `outerAloneAcceptsBadArithmetic: true`).

**Version refusal.** Schema and request `schemaVersion` const `0.1.0`; `additionalProperties: false`; code ties SCHEMA const to `VERSION`. Unknown fields (`executePayment`, `minorUnit`) refused. Sibling schema SHA256 checked at import — integrity relative to trusted code, not a signature (documented).

**Native outer vs nested.** Outer V3 does not prove nested arithmetic. `validate_native` calls `validate()` on `fact.value`, binds genesis only (`previousRecordId is None`, `state=active`, `accessClass=restricted`), binds `recordId=hash(dimension,id)` and `factId=hash(dimension,id,digest)`. It does not discover current head, later revisions, or fact supersession. `recordedAt == validFrom == object.recordedAt` and `recordedAt >= computedAt`. Native timestamps are `stamp()`-checked UTC seconds, no fractional seconds.

**Real host authority.** `issuer_set` requires `set`/`frozenset` of `str`; `host_string` requires non-blank `str`. Distinct existing vs incoming admission sets; historical membership does not authorize incoming, including exact replay of an existing row as incoming. Membership is not actor authentication. Result `authority` is const `calculation-only`. No payment, posting, or access grant exists in code.

**Retention / complete-register bounds vs tests.** Hard lifetime 256 unique receipt IDs per Dimension, including corrections. Each call: existing ≤256, incoming ≤256, unique merged ≤256. Exact same-ID replay does not consume a new slot; a new ID at 256 fails `register-bound`. Partitioned registers cannot prove global uniqueness (`test_partition_cannot_prove_global_uniqueness`). An omitted unreferenced leaf is locally undetectable; a trusted prior snapshot is required. No paging, erasure, or tombstone. This is a bounded adoption fixture, not a production store. Those claims match the tests that are present in the supplied text.

---

## Contracts: honest and sufficient for this bounded use?

Yes, for an optional same-currency summation/quantization receipt.

- `spec.json` statistics (4 bundles / 8 layers / 21 findings / 21 questions) match the structure tree.
- Questions are typed local / host / mixed / constant guidance with named gaps. They are not payment routes. No question router ships.
- `whole-object-coverage.yaml` gives `identity-class: required` only to `MonetaryCalculationReceipt`. `MoneyInput`, `CurrencyReference`, `ValuationContext`, `RoundingPolicySnapshot`, and `CalculationResult` are `not-applicable` as independent masters.
- Native path vocabulary in `runtime-model.reference.json` is the single fact path `monetary.calculation.receipt`.
- Lifecycle admits only `issued` internally; external current/superseded/withdrawn have no selector.
- Five-file native install is explicitly not the whole adoption documentation.

Drift to watch: `agent-guide.md` (L3) and the duplicated model-spec text inside `spec.json` / `migration.md`. Operational contract is `AGENTS.md` + `model-spec.md` + `adoption-limits.md`.

## Duplicate monetary master?

No. This is an optional independently addressed calculation receipt. Embedded amounts remain source-slot snapshots. `composition.yaml` has `runtimeImports: []` and cites WM-XCT-032 as “narrow semantic overlap; no subtype/inherited contract.” `parent-field-crosswalk.json` is correspondence only. `Result.authority` is `calculation-only`. Feeding a result back as source truth is forbidden unless the source-owning host re-asserts it under its own slot. Existing host calculation/audit records should be adapted; no adapter ships.

---

## Limitations of this audit

No execution, no filesystem, no network, no hash recomputation, no toolchain bytes, no parent-spec bytes. Golden example arithmetic was checked by inspection of the published traces, not by running `issue()`. Provider studies outside this candidate were not re-read.

## Remaining wider research

EM-XCT-06 quantity / unit, quantity×price, FX observation and conversion, time/calendar, and localization slices remain open. Production complete-history / paging / retention design is unscoped. A separately reviewed adapter is still required where a host already has calculation or audit records. Parent 032/008/009/031 source pins need live re-verification; 032/031 still carry the recorded single-provider waiver. jsonschema supply-chain pinning is absent. Any output-changing algorithm fix needs a new package/schema version and new receipt IDs, preserving old bytes.
