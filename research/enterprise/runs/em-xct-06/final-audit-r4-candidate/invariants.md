# Invariants

1. Amount/currency/context inseparable; only exact state admitted.
2. Unknown/float/binary coercion never becomes an exact zero.
3. Complete currency tuple equality; no implicit conversion.
4. Basis/role/valuation instant match, plus host aggregation authority.
5. ASCII decimal limits and declared scale match; lexical input survives.
6. Increment positive, mode/stage explicit; no minor-unit default.
7. Exact integer/rational arithmetic; signed residual always retained.
8. Per-item loss remains marked even if residuals cancel.
9. Digest and replay both pass; a rehashed wrong result fails.
10. Immutable same-ID conflicts fail; exact replay is idempotent.
11. Correction has exact existing predecessor, same subject/issuer and nondecreasing computedAt.
12. Full predecessor closure and no cycle; branches do not select a winner.
13. Unknown fields/versions fail closed; no silent migration.
14. Source-slot IDs are unique inside one calculation.
15. Native object/type/path/master/digest/access/storage-time checks supplement outer validation.
16. Correct arithmetic grants no operational authority or disclosure rights.

1–15 contain local structural/arithmetic checks and explicitly named host assumptions in model-spec.md. 16 is a boundary rule enforced operationally by the host. Tests do not prove external truth or legal compliance.
