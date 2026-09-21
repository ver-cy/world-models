ACCEPT WITH LIMITS

This is review evidence for the supplied 0.1.0 companion candidate, not publication authority, not independent execution of tests, and not hash-verification of original bytes. Compact-rendered JSON/YAML in this packet cannot be treated as the declared SHA256 preimages. `test-results.json`, `acceptance-results.json`, `tool-pins.json`, parent-spec digests, and “Python 3.12.14 / jsonschema 4.26.0” are supplied assertions.

The package is a bounded optional calculation receipt: exact same-currency summation plus explicit per-item or after-sum quantization. It does not invent a second monetary master if adopted as documented. Bundle/layer/question/whole-object contracts are honest enough for that bounded use and insufficient for the rest of EM-XCT-06, which they say.

---

## Defects (code/schema/docs tightness)

None found that silently accept bad arithmetic, collide immutable identity, migrate unknown versions, or treat outer V3 validity as nested proof.

**LOW — schema increment `allOf` still carries an optional-minus pattern.**  
File: `monetary.schema.json` `$defs.Policy.increment`.  
Counterexample: the intersection still forbids `-0.01` because the primary pattern has no minus and a non-zero lookahead; code also requires `quantum>0`.  
Fix: drop the copied `^-?` allOf from increment (keep it only on input amounts). No value change.

**LOW — `Result.roundedTotal` / `Step.rounded` have no decimal grammar.**  
File: `monetary.schema.json` `$defs.Result`, `$defs.Step`.  
Counterexample: a schema-only consumer could accept `"roundedTotal":"abc"`. `validate()` / `import_receipts()` / `validate_native()` recompute `result==compute(request)` and refuse.  
Fix: add the same ASCII decimal pattern used for amounts, or state in the schema `$id` description that replay is mandatory. Residual, not a compute bug.

**LOW — invariant 11 is tighter than `issue()`.**  
File: `invariants.md` #11 vs `monetary.py` `issue` / `validate` / `import_receipts`.  
Counterexample: `issue({..., supersedes:{id,digest}, correctionReason:"x"})` seals a successor whose predecessor is absent, digest-wrong, different issuer/subject, or earlier `computedAt`. Only `import_receipts` raises `supersedes-unresolved` / `supersedes-scope` / `supersedes-time`. `validate` only blocks self-supersession.  
Fix: reword invariant 11 to “import of a complete register,” matching `model-spec.md` and `final-review-limits.md`. Hosts that store `issue()` output without import can persist orphans.

**LOW — agent-guide digit wording is looser than the rule.**  
File: `AGENTS.md` / `agent-guide.md` (“36 input digits, 18 fractional digits”) vs `model-spec.md` / code (`36` total digits and `18` fraction digits).  
Counterexample: a 36-digit integer plus a fraction would be read as allowed by the guide and refused by `amount()` + schema.  
Fix: say “at most 36 total digits, of which at most 18 are fractional.”

**LOW — some unit negatives only assert `Rejected`, not a unique code.**  
File: `test_monetary.py` (`test_currency_edition_and_basis_refusal`, `test_unknown_interval_float_forbidden`, several `refused()` helpers). Native/acceptance paths do assert exact codes. Already listed in `final-review-limits.md`.

These do not justify REVISE. They do not change computed totals, identity, or native isolation.

---

## Documented host assumptions and deferred scope (not defects)

Treat the following as adoption conditions. They are stated in `model-spec.md`, `adoption-limits.md`, `AGENTS.md`, `bindings/native-v3.md`, and `final-review-limits.md`. Tests measure several of them; they do not implement the missing host duties.

1. **Host authority is asserted, not proved.** `allowed_issuers` / `admitted_*_issuers` must be `set`/`frozenset` of strings. Membership is not actor authentication. Currency `resolution` is the const `host-admitted`. Catalogue existence, eligibility, source exactness, allowed signs, aggregation purpose, rights, and digest preimages are outside this code.

2. **Lineage is import-time only.** Correction needs a new id, exact pin, and non-blank reason at `issue()`. Predecessor presence, digest match, same subject/issuer, nondecreasing `computedAt`, and acyclicity are `import_receipts` only. Branches are retained; no current winner.

3. **Complete 256-ID register is a caller promise.** Bounds: 256 inputs; 256 existing; 256 incoming; 256 unique merged IDs per Dimension including corrections. Exact replay of an already-merged id does not consume a new slot. `test_partition_cannot_prove_global_uniqueness` shows two different same-id receipts each import alone and conflict together. Splitting or omitting leaves loses conflict detection. Not a production store.

4. **`validate_native` binds genesis only.** `previousRecordId is None`; `recordId = sha256(dimension, request.id)` (no digest); `factId = sha256(dimension, id, digest)`. It does not discover current head, later object revisions, fact supersession, retirement, or current ACL. `provenance.source` is not bound to `master`. Extra envelope keys are not closed (32-key / depth-16 / list-256 / string-512 / int≤9999 / 2 MiB still applied). Passing an old genesis record does not prove current access.

5. **Outer V3 ≠ nested arithmetic.** Acceptance explicitly sets `outerAloneAcceptsBadArithmetic: true`. A rehashed wrong `roundedTotal` with rewritten `digest` / `factId` / `recordDigest` still fails companion `replay-mismatch`. MC-Q16 is correct. Both validators must be invoked; there is no automatic hook.

6. **Historical inspection ≠ incoming write.** Retaining an issuer in `admitted_existing_issuers` does not admit new or replayed incoming records from that issuer. Covered by `test_historical_issuer_does_not_authorize_new`.

7. **Time/plausibility.** Instants are strict UTC seconds, no fractional seconds, no leap seconds. `datetime.strptime` rejects impossible calendar dates the schema digit pattern would allow (`2026-02-30`). Future `valuationAt` is accepted for any purpose. `recordedAt >= computedAt`; equality allowed. Compute-before-valuation is not locally forbidden.

8. **Opaque strings.** `revision`, `edition`, `amountRole` may contain whitespace or bidi. Currency codes are `[A-Z]{3}` syntax only. Visually equal labels are not authority.

9. **Receipt-as-source.** Reusing `roundedTotal` as a later input requires explicit source-owner re-assertion under a new source-slot identity. Code does not detect receipt-as-source.

10. **No operational authority.** `result.authority` is `calculation-only`. No payment, posting, staffing, disclosure grant, ledger, tax, FX, quantity×price, calendar, or localization.

11. **Install surface.** Native install copies five assets (`spec.json`, `AGENTS.md`, `runtime-model.reference.json`, `monetary.schema.json`, `monetary.py`). That is not the adoption package. `role=core` in the synthetic composer release is delivery, not ontology inheritance. Fixture `publicationStatus=published` is synthetic only.

12. **Versioning.** Unknown fields/versions fail closed (`additionalProperties: false`, schema `const` 0.1.0, `code-schema-version`). Sibling schema digest is checked at import (`SCHEMA_DIGEST`). That is not a signature or supply-chain pin for `jsonschema`.

---

## Adversarial checklist

**Decimal signs / ties / stages.**  
`round_units` matches the spec: floor/ceiling use signed integer division toward −∞ / +∞; toward-zero truncates abs; half-away ties on `2*r>=d` then reapplies sign; half-even ties to an even increment count. Startup `3×0.495` half-even `0.01`: per-item `1.50`, after-sum `1.48`, half-away after-sum `1.49`. Matrix `-1.025→-1.02`, `2.075→2.08`, total `1.06`, signed residuals retained. Input `-0` / `-0.00` refused; output zero is unsigned. Inexact stays true when per-item residuals cancel. Scale-only lexical change does not set inexact. Increment `0.10` vs `0.1` changes `roundedTotal` scale, not the Fraction.

**Precision limits.**  
ASCII lexical amounts, no exponent/grouping/float. Code + schema: 36 total digits, 18 fraction digits, negative-zero refused, leading zeros refused. Output cap 57 digit characters is the tight worst case: `256 × (10^36-1)` plus an 18-place increment. `fixed()` demands a terminating decimal at the increment’s lexical places; a decimal increment makes that hold. Rational wire fields allow 80 digits; computed worst-case numerators stay under that.

**Same currency, different context.**  
Equality is the full currency tuple and the full context (`basis` pin, `valuationAt`, `amountRole`) plus policy currency. Same `EUR` with another edition, catalogue, digest, role, or instant is `mixed-currency-or-edition` / `incompatible-valuation-context`. Same currency is not compatible accounting meaning.

**Source-slot identity.**  
Unique `source.id` and unique input `key` inside one request. Same id with a different revision/digest is still a duplicate slot. Identical amounts from different slots are allowed.

**Immutable correction / rehash / version.**  
New id + pin + non-blank reason. Old bytes stay. Same-id different bytes: `immutable-identity-conflict`. Result-only edit: `receipt-digest`. Result+rehash: `replay-mismatch`. Self-supersession refused. Unknown version/field refused. No valid-rehash omitted-leaf replacement test is claimed.

**Native outer vs nested / real host authority.**  
See documented items 4–6. Synthetic master/writer/issuers in acceptance are fixtures, not real authority.

**Retention / complete-register claims vs tests.**  
Unit tests exercise 256-input output capacity, 256-record replay, 257th unique refusal, and partition non-uniqueness. Acceptance enumerates stored facts on three fresh synthetic Dimensions and checks installed asset digests inside that fixture. Neither is production paging, retention, or current-head proof. Reports of those runs are assertions in this audit.

---

## Contracts: honest for this slice, not for the contour

- `spec.json` statistics (4 bundles / 8 layers / 21 findings / 21 questions) match the tree. Questions are guidance, not routes. Constant answers match the code (no payment, outer≠nested, no migration, pin≠truth, 256 cap, no FX/qty/calendar). Mixed answers name missing host evidence.
- Supplied `model-spec.md` and `spec.json` `model.scope` are the same contract text in this packet. `AGENTS.md` and `agent-guide.md` are declared byte-identical.
- `composition.yaml` / `spec.json` composition: `runtimeImports: []`; WM-XCT-032 is a semantic reference only (`0.3.0-research.1`, cited digest). `parent-field-crosswalk.json` says narrower correspondence, not inheritance.
- `whole-object-coverage.yaml` requires all five facets only on `MonetaryCalculationReceipt`. Embedded money/currency/context/policy/pin/result types mark identity-class and capabilities `not-applicable` and say there is no independent master. Shared boilerplate is sloppy, not a second catalogue.
- `lifecycle/transitions.json`: local state is `issued` only; current/superseded/withdrawn are external.
- `mastership-and-rights.yaml`: source, catalogue, and policy owners stay external; the receipt owner masters evidence, not source truth.

That is sufficient for one optional same-currency receipt. It is not a host adapter, not V3 current-selection, and not EM-XCT-06 completeness.

---

## Limitations of this audit

No tools, no execution, no filesystem, no live fetch, no contact with issuers or publishers. Source bytes of the pinned composer/skill toolchain and of WM-XCT-008/009/010/031/032 were not in this packet and were not reviewed. Declared SHA256s are internally cross-cited and unverified here. Two prior provider studies are outside this candidate and were not re-read.

---

## Remaining wider research

Still open, and correctly not shipped: quantity/unit (008), time/calendar (009), localization (031), quantity×price, FX observation/conversion, working-calendar/DST, designation assertion, existing-Dimension migration, host adapter for already-existing calculation/audit records, actor-to-issuer binding, source byte preimages and re-assertion, production paging/index/retention, current-head and permission inspection, object revision/retirement/native retraction, leap-second policy, supply-chain hashes for `jsonschema` and the toolchain, and live re-verification of parent publication holds (paywalled ISO texts, catalogue editions, waived second-provider review on 032/031). Parent models keep their research holds. No whole-parent inheritance is claimed.

Any output-changing arithmetic fix needs a new package/schema version and new receipt ids, with old bytes preserved.
