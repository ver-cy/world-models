# Final remediation verification: WM-XCT-040 X1–X3

**Verdict: ACCEPT WITH LIMITS**

I don't have the earlier audit transcript in this session. This check is against the three blockers as you describe them, using only the diffs above, inside the bounded, trusted-input, cooperative-Windows contract. I executed nothing. Test and acceptance counts are your reported Codex results, not my observation.

## X1 Schema closure: closed

- `check_schema_closed` rejects a non-object root and `patternProperties` at any depth.
- It normalises `type` to a list. Any node that includes `object`, or has `properties` without a type, must set `additionalProperties: false`. That closes both reopen paths (`["object","null"]` and untyped `properties`).
- Subschemas inside `if`/`then`, `dependentSchemas`, `items` and `$defs` are covered by the recursive walk. `$ref` stays internal-only.
- Untyped nodes and boolean-true subschemas stay open. This is explicitly assigned to the companion, which is consistent with the bounded profile.
- False rejections, where a property named `type`, `properties` or `patternProperties` looks like a keyword, are conservative and documented.
- Both plan and policy schemas have `additionalProperties:false` on every object node. Their diffs are whitespace-only.
- Two new tests (`test_pattern_properties_reopens_root_refused`, `test_list_typed_open_object_refused`) cover the two new branches.

## X2 Linked nested evidence: closed

- The positive value now comes from the actual `native-fact.reference.json` and is asserted equal to the example draft.
- The malformed copy goes through the native `append` into a copied Dimension. That copy passes `native_validate`, and the value re-read from the written file fails `module.errors`.
- The good fact is appended to the real target and its stored value re-read and passes.
- The three renamed result flags are reached only after the asserts pass. So "passes V3 but fails companion" is now shown on stored records, not in-memory dicts.

## X3 Wording: closed

- Model-spec, the bootstrap docstring, the appended AGENTS.md trust note and the README all say the same thing: descriptors must be present, execution is a separate step-7 obligation in `composition/plan.json`, and bootstrap executes no package code.
- Closure and minimality are stated as plan-declared only, and dependencies are not extracted from spec bytes.
- These are also explicit:
  - Python 3.12+
  - `format-nongpl` extra
  - Windows/cooperating-writer scope
  - 2026-12-31 example expiry with `validate --at` for history
  - authored versus copied provenance
- The adapter observation moved out of `events.yaml`, so it is no longer presented as a native event.
- The nine upstream assets match the copied-asset claim, and the scope note excludes the authored Organization binding.
- 55 + 13 new tests = 68, which matches `test-results.json`.

## Remaining limits (non-blocking)

1. **Validator bytes not bound to evidence:** The harness loads `validate_examples.py` from `examples/assets`, not from the digest-verified copy in `target/models/composed/…`. The bytes are equivalent within one run because staging checked the digest. Loading the installed copy, or recording its digest in `nestedValidation`, would bind the evidence to the exact executed bytes.
2. **Acceptance relies on `assert`:** Under `python -O` all acceptance checks become no-ops. Document "do not run with -O", or switch to explicit raises.
3. **Stale wording in model-spec:** "Bounded file and schema profile" still says "closed explicitly typed nested object nodes". The code now also closes properties-defined nodes and refuses `patternProperties`. The later paragraph partly compensates, but aligning the sentence would remove the inconsistency.
4. **Two raw exceptions escape the error model:**
   - An unparseable `receipt.json` on the idempotent `stage` path raises a raw `JSONDecodeError`, not `TARGET`.
   - In `stamp`, the inner timezone `require` is re-wrapped as a generic "invalid timestamp". Both still fail closed.
5. **Negative-copy Dimension not in the report:** `ai-team-negative-copy` is validated in the run, but its V3 report isn't persisted in `acceptance-results.json`, only the boolean.

None of these reopens X1–X3 or contradicts the accepted bounded contract.
