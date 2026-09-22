# Required publication adoption addendum — Quantity Values 0.1.0

This is a **post-audit Codex adoption disclosure**, prepared after both actual R3 provider audits returned ACCEPT WITH LIMITS. It is not claimed to have been reviewed by either provider. All 33 frozen candidate files, including the five operational installation assets, remain byte-for-byte unchanged. Read this addendum together with AGENTS.md, model-spec.md, adoption-limits.md and bindings/native-v3.md before using the package. The smaller operational installation set alone omits these final adoption clarifications.

## Mandatory correction workflow

After current host authorization and outer V3 validation, invoke the explicit companion validator. For **every fact with nonempty supersedes**, retain and resolve exactly one predecessor and invoke `validate_correction(previous, current, ...)` with the trusted host context before accepting the record as a correction. `validate_native()` on the head alone does not enforce correction continuity or a correction reason. The supported link is **exactly `[predecessorFactId]`**; a multi-predecessor merge is unsupported. If the predecessor or its permitted evidence is unavailable, keep the correction unresolved. Never infer acceptance from the head-only check or outer V3 success.

The pair checker does not discover predecessors, select the current head, close the full graph, resolve concurrent writes, authorize disclosure, or refresh derived conversions. Those remain host duties. The supplied native binding admits one semantic quantity per existing host, with quantity.value and quantity.conversion slots for that same quantity; do not manufacture artificial hosts to bypass this limit.

## Unit and target changes

A correction preserves the input kind, dimension, anchor, role and context. It can change the input unit snapshot or the conversion target. Govern changes to unit code, coefficients, source definition or target as an explicit definition/representation revision with a recorded reason and newly admitted evidence; do not silently interpret them as a numeral typo. **Read every result with its own retained target definition. Never compare raw result numerals across revisions.** For example, 75 minutes and 4500 seconds are different representations; the pair checker is not an equivalence or business-approval decision. Source correction may make a separately stored conversion stale; the host must check that relationship.

## Reference bounds and diagnostics

- A reduced result is limited to 256 characters per numerator or denominator. Overflow is rejected later by schema validation, normally as `schema`; the generic 1024-character wire bound can fail earlier as `ascii-string`. No separate result-overflow code or boundary execution evidence is claimed.
- The whole stored fact uses this reference's bounded ASCII wire contract. Unrelated host-object properties may use Unicode under outer V3. Canonical bytes and execution were checked only for the pinned Python reference, not certified across languages. JSON integer token -0 normalizes to 0; a quantity's decimal lexical signed zero remains preserved.
- Exception causes can retain original JSON or Unicode input. Do not log raw inputs or exception chains without a separate authorized diagnostic policy. Pair failures may not identify which revision failed; inspect individual records only under their applicable permissions.
- Example admission arrays are serialized synthetic evidence. They are not live API sets or authorization. Verify evidence and purpose first, then construct the required sets/frozensets. A digest calculated from untrusted incoming data does not establish admission.

## Evidence and remaining limits

The frozen package reports 53 tests, 201 independently calculated finite-precision Decimal comparisons, three synthetic native Dimensions and 48 native rejection cases. The Decimal comparison is not a metrology proof. Native acceptance loads a repository helper for part of its readback while asserting that installed code bytes match it. Passing checks do not cover every possible helper/boundary case, an existing production Dimension migration, source truth, current authority, supply-chain certification, or a general multi-field integration.

Both full R3 answers and earlier disagreements are retained in the public research dossier. Claude R3 D1–D3 and Grok R3 L2–L5 motivate the correction and unit/admission clarifications above; the remaining observations are carried as explicit bounds and host responsibilities. Publication readback and any additional example consistency checks are separately attributed Codex evidence, not retroactive provider execution.

EM-XCT-06 remains partial. Uncertainty, nonlinear conversion, general point/difference arithmetic, Price, FX, calendars, localization and wider native bindings require separate research and releases. This is a usable bounded reviewable draft, with no whole-parent, full UCUM/QUDT or production certification claim.
