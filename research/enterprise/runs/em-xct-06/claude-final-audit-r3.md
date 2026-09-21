# Verdict: **ACCEPT WITH LIMITS**

This verdict covers a bounded, reviewable-draft, synthetic-fixture companion. I found no critical or high defect in the arithmetic, the replay/digest binding, or the immutable-merge logic. There is one medium packaging/honesty defect (M1). It is a documentation-only fix and should be made before the frozen bytes are published. The low findings are hardening or claim-precision items.

If publication policy requires every medium finding to be closed in the frozen bytes, treat this as **REVISE for M1 only**.

**What this audit is based on.** This is a no-tools reading of the supplied text. I executed nothing and verified no hashes. The following are all supplied assertions, not facts established by this audit:
- `test-results.json` and `acceptance-results.json`
- the digests in `tool-pins.json`
- the parent digests in `composition.yaml` and `crosswalk.json`
- the stated "published" status of WM-XCT-032

I did not see the external composer, skill, V3 schemas or parent spec bytes.

---

## 1. Defects

### M1 — Medium: two divergent agent contracts in one package
**Files:** `agent-guide.md` vs `AGENTS.md`

**Problem.** Both files carry the identical heading "Agent contract — Enterprise Monetary Calculation 0.1.0". They differ in substance.

`agent-guide.md` still says "Question routes in spec.json **return** insufficient-context with named gaps". That is the pre-R2 wording that R2 D10 explicitly corrected ("guidance is not an executable endpoint"). It also omits three things:
- the genesis-only `validate_native` limit
- the hard 256-per-Dimension lifetime cap
- the narrower envelope-bounds paragraph

**Counterexample.** Every contract tells an agent to "read the complete pinned package". An agent that does so and reads `agent-guide.md` will:
- treat `spec.json` questions as executable routes, and
- miss that a passing genesis record never proves current access.

The installed `AGENTS.md` says the opposite. Nothing marks either file as authoritative or superseded.

**Fix.** Delete `agent-guide.md`, or make it byte-identical to `AGENTS.md`. Alternatively, add a one-line "superseded by AGENTS.md" marker. Nothing in the tests covers doc consistency, so also add a test that `agent-guide.md` either does not exist or equals `AGENTS.md`.

### L1 — Low: loose free-text fields inside digest-bound, equality-compared tuples
**File/function:** `monetary.schema.json` (`Pin.revision`, `Currency.edition`, `Context.amountRole`, `Request.correctionReason`) and `compute`

**Problem.** IDs, keys, codes and digests have strict grammars with end guards. These four fields are `minLength:1`/`maxLength` only. The code checks only `correctionReason` for non-blankness.

**Counterexamples.** All of the following issue successfully:
- `revision: " "`
- `edition: "fixture-1\n"`
- `amountRole: "estimate\u202e"` (bidi override)

Currency and context equality are exact, so this fails closed on mismatch. However, it permits meaningless or visually spoofable pins. Two tuples that render identically but differ in bytes are refused with no explanation. `test_strict_grammar_aliases` covers none of these fields.

**Fix.**
- Give `revision`, `edition` and `amountRole` a printable-ASCII (or NFC, no-control, no-bidi) grammar with the `(?![\s\S])` guard.
- Reject whitespace-only values in code.
- Add trailing-newline and control-character negatives.

Tightening the schema changes which inputs are accepted but not outputs for already-valid inputs. It still requires a schema digest bump, so it can wait for 0.1.1 or 0.2.0 and be documented as a known limit for 0.1.0.

### L2 — Low: `validate_native` does not bind provenance source or close envelope keys
**File/function:** `monetary.py` `validate_native`, `bounded`

**Problems.**
- `fact.provenance.source` and `obj.provenance.source` are never compared with `master`.
- Extra envelope keys are not refused. That is delegated to the outer V3 validator, whose schemas are not supplied here.
- `bounded` limits string *values* to 512 characters but never checks *key* length.

**Counterexamples.**
- A fact with `provenance: {"source": "urn:other", "recordDigest": <correct>}` passes the companion check while `masterSystem` says `master`.
- An envelope key of about 1.9 MiB passes `bounded`, since only the 2 MiB total applies.

The docs say "the same closed resource bounds apply … generic strings at most 512 characters". That is true only for values.

**Fix.**
- Require `provenance.source == master` on both records, or document that the outer V3 validator owns this.
- Apply the 512 limit to keys.
- Reword "closed" to "bounded", because the envelope vocabulary is not closed by the companion.

### L3 — Low: receipt-as-source is prohibited in prose but cheaply detectable and not refused
**File/function:** `import_receipts`

**Problem.** The spec says: "Do not feed a receipt output into a new input as source truth unless the source-owning host explicitly re-asserts that amount under its own source-slot identity."

**Counterexample.** Receipt B has an input with `source = {id: A.request.id, revision:"1", digest: A.digest}`. B imports alongside A without complaint.

**Fix.** Within a merged register, refuse any input whose `source.id` equals a receipt ID, or whose `source.digest` equals a receipt digest. Use a typed error such as `receipt-as-source`. This does not catch aliasing through other IDs. That limit remains a host duty and should be documented as such.

### L4 — Low: "hard lifetime limit" is a precondition, not enforcement; wording is inconsistent
**Files:** `AGENTS.md`, `model-spec.md`, `spec.json` (`catalogue.limits`, MC-Q20)

**Problem.** The code enforces 256 unique IDs per `import_receipts` call only. A host that passes a partial register exceeds the lifetime cap silently. The docs describe this elsewhere as a precondition ("requires the complete Dimension-wide register"), but "hard lifetime limit" reads as enforced. Meanwhile `catalogue.limits` calls the same limits "reference bounds".

**Fix.** Say "hard lifetime limit, enforceable only when the host supplies the complete register". Make `catalogue.limits` match.

### L5 — Low: purpose-independent future `valuationAt`
**File/function:** `compute`, `model-spec.md`

**Problem.** The spec says "Future valuationAt is allowed **for an estimate**". The code allows it for `reconciliation` too. For example, a request with `purpose: "reconciliation"`, `valuationAt` = 2030 and `computedAt` = 2026 is issued.

**Fix.** Either refuse `valuationAt > computedAt` unless `purpose == "estimate"`, or reword the sentence to say future `valuationAt` is allowed for any purpose, with plausibility left to the host.

### L6 — Low: claims vs tests gaps
**Files:** `test_monetary.py`, `acceptance.py`

1. **Negatives that don't pin the error code.** Many negatives use `assertRaises(m.Rejected)` without a code. Examples:
   - `refused()` in the currency/basis/amount/date tests
   - `test_correction_branches_and_guards`
   - `test_replay_and_digest_tamper`
   - `test_correction_reason_and_identity`

   A case can pass by failing for the wrong reason. `test_replay_and_digest_tamper` does not distinguish `receipt-digest` from `replay-mismatch`; only the native acceptance does.
2. **Error codes never exercised:** `native-record-type`, `native-type`, `native-envelope-size`, and `native-object` for `objectId` specifically.
3. **Leap second** (`23:59:60`) is not tested. It is rejected by `datetime` construction, which is correct but unproven.
4. **Non-terminating quotient increments** such as `0.03` or `0.07` are outside the oracle; its increments are `0.01`, `0.05`, `2` and `1e-6`. The Fraction code is correct by inspection, but the claim of an "independent oracle" covers only terminating quotients.
5. **Valid-rehash leaf replacement is not demonstrated.** In this attack, an input is changed and the result, digest and `factId` are recomputed, and the stored fact is overwritten. The docs admit it ("trusted prior snapshot needed"). No test shows that outer validation, `validate_native` and `import_receipts` all accept it. The rehash negative covers only wrong arithmetic.
6. **Overstated test description.** R2 describes an "installed schema tamper test". `test_schema_integrity` tampers with a temp sibling copy. The acceptance run checks installed digests, not tamper refusal.

**Fix.** Assert exact codes everywhere. Add these cases:
- the missing codes and a leap-second case
- a `0.03`/`0.07` oracle using an exact-Fraction reference
- a documented "leaf replacement is undetectable without prior snapshot" test

### L7 — Low: templated whole-object and mastership contracts
**Files:** `whole-object-coverage.yaml`, `mastership-and-rights.yaml`

**Problem.**
- In `whole-object-coverage.yaml`, every value type (`Rational`, `Step`, `ReceiptPin`, …) gets the same concatenated boilerplate. `Rational` gets "context-evidence: required: inherited receipt source and policy context", which has no meaning for a numeric carrier.
- In `mastership-and-rights.yaml`, all four fact classes have identical writer, reader, time, conflict and retention text. The currency catalogue's writer is an "authenticated host-authorized actor", not the external steward.

**Assessment and fix.** Honest in direction, but not informative. Write per-type meanings, and make each fact class's writer, retention and time entries distinct.

### L8 — Low/Info: minor contract precision
- **Two admission models.** `validate_native` takes one `allowed_issuers` set, while `import_receipts` separates existing and incoming admissions. The docs never say which set to pass when inspecting a historical record from a since-removed issuer. State it, or split the parameter the same way.
- **Currency code grammar.** `Currency.code` is `^[A-Z]{3}$`, but the spec says the package is catalogue-agnostic and makes no ISO claim. Four-letter and numeric codes are silently unsupportable. Document this as an ISO-4217-shaped syntactic limit.
- **Misnamed error code.** In `fixed`, the error code `nonfinite-result` is misnamed. It is unreachable because every result is an integral multiple of the increment. Rename it to `internal-scale` or similar.
- **Overloaded field name.** `Result.declaredScale` means *increment* scale, while `Input.declaredScale` means *input* scale. The shared name invites misreading. Document the distinction; renaming needs a version bump.
- **Free-text object fields.** Object `name` and `description` are unvalidated free text on a restricted record. Say explicitly that they must carry no financial content.

---

## 2. Checked and found sound (by hand trace)

**Rounding (`round_units`).**
- `floor` computes `n//d`.
- `ceiling` computes `-((-n)//d)`.
- `toward-zero` computes `sign*q`.
- `half-away-from-zero` uses `2r>=d`.
- `half-even` uses `2r>d or (2r==d and q odd)`.

All five are correct for negative values and for zero. The tie is defined on the integral *increment count*, as the spec states. So with increment `0.05`, `0.125` rounds to `0.10`. That matches the spec, which explicitly makes no cash-rounding claim.

**Golden examples.** I re-derived:
- **startup:** per-item result `1.50`; after-sum `1.485`, which half-even rounds to `1.48`, and half-away rounds to `1.49`.
- **matrix:** `-1.025` rounds to `-1.02` (102 is even) and `2.075` rounds to `2.08` (207 is odd). The total is `1.06`, exact `21/20`, residual `-1/100`, and each step residual is `-1/200`.
- **ai:** exact total `500000000000000000001/500000`, residual `1/500000`, `inexact=true`.

All match the supplied examples and the report values. In the matrix after-sum correction, `105` is exact, giving `1.05`.

**Signs and zero.**
- `-0`/`-0.00` are refused.
- An output that rounds to zero prints unsigned (`fixed` emits no `-` for n=0).
- Per-item cancellation still reports `inexact` (`test_cancelled_residuals`).

**Precision.**
- An input has at most 36 digits and at most 18 fraction digits. The schema's `maxLength 38` is consistent.
- The output is at most 57 digits: under 2.56e38, 39 integer digits plus 18 fraction digits. The total length stays within the schema's `maxLength 64`.
- Rational numerators stay far below the 80-digit schema cap.
- No `Decimal` context and no floats are involved.
- Python `re` `[0-9]` is ASCII-only, and the `$(?![\s\S])` guard defeats the trailing-newline behaviour of `re.search`.

**Stages.** `per-item` quantizes and then sums. `after-sum` produces a single `@total` step. `@total` cannot collide with an input key because the key grammar starts with `[a-z]`.

**Same currency, different context.** Equality covers the full catalogue/edition/snapshot/code tuple plus basis pin, `valuationAt` and `amountRole`, with an exact policy-currency match. The spec explicitly says this is necessary but not sufficient for aggregation.

**Source-slot identity.** Duplicate `source.id` is refused within a request, even at a different revision. Aliasing across IDs is explicitly undetectable and documented.

**Digest and replay.** `validate` checks shape, then digest, then full replay, then self-supersession. A rehashed wrong result fails with `replay-mismatch`. The acceptance run asserts the exact code natively, and also shows the outer V3 validator accepting the bad arithmetic (`outerAloneAcceptsBadArithmetic: true`).

**Immutable correction.** The code enforces:
- a new ID
- an exact predecessor pin by digest
- a non-blank reason
- the same subject and issuer
- non-decreasing `computedAt`
- predecessor closure (typed `supersedes-unresolved`, including the transitive case)

Branches are retained. Replacing a non-leaf breaks its successor's pin and is detected. Replacing a leaf is not detected; that is documented.

**Version refusal.** `format`, `schemaVersion` (receipt and request), a code-to-schema constant cross-check, and native `1.0.0` on both envelopes are all enforced. The sibling-schema digest is checked at import.

**Issuer admission typing.** Requiring a `set`/`frozenset` blocks the substring-`in` bug that a plain `str` admission would cause (`"…:startup" in "…:startup-admin"`). This is tested.

**Wire parsing.** Duplicate keys, NaN/Infinity, BOMs, invalid UTF-8, lone surrogates (via the canonical encode) and oversized integers (via the Python digit limit) all produce typed rejections.

**Counts.** Tests: 32, matching the report. Oracle cases: 5×10×4 + 2 = 202, matching the report.

---

## 3. Documented host assumptions and deferred scope (not defects)

**Authority and authentication (host duties).**
- actor-to-issuer authentication
- issuer admission
- currency "host-admitted" assertion
- source and policy pin resolution
- valuation and aggregation compatibility
- allowed signs
- read/write permission
- licensing and rights

**Storage (host duties).**
- store completeness
- append-only media / CAS
- leaf-replacement detection, which needs a prior snapshot
- current head, object revisions, retirement and native fact supersession (`validate_native` is genesis-only)
- retention, erasure and tombstones (no erasure path exists; predecessors must be preserved, which may conflict with privacy obligations)

**No automatic validator dispatch.** A V3 reader that skips the companion will trust nested arithmetic. This is the largest residual adoption risk. It is mitigated only by `accessClass: restricted` and the documentation.

**Capacity.** 256 inputs; 256 existing, 256 incoming and 256 merged records; a 256-per-Dimension lifetime; no paging. A Dimension that reaches the cap is permanently full for this model.

**Deferred features.** Quantity×price, FX, calendars/DST, localization, allocation, tolerance, migration, host adapters, a current-effective selector and withdrawal handling.

**Canonical JSON.** A local canonical encoding, not RFC 8785, with no signatures.

---

## 4. Specific questions

**Is this a duplicate monetary master?**
No, as specified:
- Inputs are snapshots of externally mastered slots.
- The result is `calculation-only`.
- The mastership file assigns slot truth to source owners.
- The anti-feedback rule is stated (L3 would make it partly enforceable).

**Residual risks:**
- The package defines its own Currency/Context/Policy schemas rather than reusing WM-XCT-032's. That is a parallel representation, mapped only by `parent-field-crosswalk.json`, and it can drift from the parent.
- Where no host calculation record exists, the receipt's `roundedTotal` can become a de facto authoritative total by default.
- "Adapt existing records rather than duplicate" is guidance only. No adapter or detection mechanism ships, which is honestly stated.

**Are the bundle, layer, question and whole-object contracts honest?**
- **Counts:** `spec.json` statistics (4 bundles / 8 layers / 21 findings / 21 questions / 21 artifacts / 21 actions) match the structure.
- **Question kinds:** Local, mixed, host and constant kinds are differentiated. The answers correctly refuse payment/posting authority and current-winner selection.
- **Missing-evidence answers:** `answer_data` is prose, not a structured missing-evidence field. That is adequate for guidance but not machine-actionable.
- **Scope text:** `spec.json`'s scope embeds `model-spec.md` verbatim, so the installed assets carry the full semantic contract even without the ZIP.
- **Weak points:** the whole-object and mastership files are the weakest parts (L7), and the stale `agent-guide.md` is the only outright contradiction (M1).

**Sufficiency for bounded use:** Sufficient for a synthetic or small single-Dimension adoption with a trusted host that:
- supplies the complete register,
- authenticates issuers, and
- calls the companion explicitly.

It is not sufficient for production scale, for multi-writer stores without CAS, or for any consumer relying on outer V3 validation alone.

---

## 5. Limitations of this audit

- **Nothing executed.** No test, acceptance or oracle run was performed, and no digest was recomputed. The pass counts, `executedAt`, Python 3.12.14 / jsonschema 4.26.0 behaviour, and all digests are unverified supplied assertions.
- **External code unseen.** I did not see the composer, bootstrap, `write_record` or `validate_dimension`, or the V3 fact/object schemas. Claims about outer V3 behaviour rest only on the supplied report.
- **Parents unread.** I did not read the WM-XCT-032/008/009/010/031 source bytes. Field correspondences and parent publication holds are taken as stated. I cannot confirm that WM-XCT-032's rounding-mode vocabulary or tie semantics match the local ones.
- **Library behaviour inferred.** jsonschema's `pattern` engine (Python `re`, `re.search`) and `datetime` leap-second rejection are inferred from known library behaviour, not observed.
- **Prior studies excluded.** The two preserved independent studies and prior audit responses are outside this review.
- **Not publication authority.** This verdict is review evidence only.

## 6. Remaining wider research (EM-XCT-06)

- Quantity/unit (008) profile and quantity×price multiplication with stage semantics
- FX observation/conversion boundaries
- Calendar and valuation-instant authority (009)
- LocalizedText (031)
- Cash-rounding jurisdiction profiles, as distinct from mathematical increments
- A reviewed host-adapter mapping for existing calculation and audit records
- Production paging and complete-history indexing beyond 256 records, including retention and erasure versus predecessor closure
- Native current-head, revision and retraction handling
- Automatic or declared companion-validator dispatch in V3
- Authenticated issuer binding (signatures)
- Live re-verification of all cited sources and parent holds
