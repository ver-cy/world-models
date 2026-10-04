# WM-XCT-040 0.1.0: final static release audit

**Verdict: BLOCK, narrowly.** One implementation defect and two groups of wording/evidence fixes stand in the way. Each fix is small and local, and none reopens the boundary. Once they land, the verdict becomes **ACCEPT WITH LIMITS**.

This is a static reading of the files you supplied. I did not execute anything. The 55 tests and the three acceptance profiles are Codex-reported. I counted 55 `test_` methods, which matches `test-results.json`.

## Status of prior findings (Grok B1–B6)

| Prior | Status | Basis |
|---|---|---|
| B1 recursive object closure | **Partially closed; residual below** | `walk` closes `type=='object'` only |
| B2 historical-time bypass | Closed | `stage()` refuses when `at` is set (`composition.py`, `stage` line 1); the CLI refuses as well; `bootstrap` has no `at` |
| B3 no bootstrap tests | Closed as acceptance, not unit tests | `acceptance.py`: three profiles plus three failure checks |
| B4 broad path replacement | Closed | Exact equality check on `canonical.location` and an exact single-line match in AGENTS |
| B5 YAML acceptance | Closed | `spec_json` handles JSON plus one `#` line; `test_real_yaml_profile_refused` |
| B6 same-version changed bytes | Closed | `MIGRATION` check; `test_same_version_changed_bytes_refused` |

The boundary is still sound: one aggregate, no new kernel, and a caller-supplied policy and lock bound by digest. The plan cannot widen its own authority: allowlist, drafts, actor, purpose and reviewer are all checked against the policy.

## Blockers

### X1: the instance-schema closure gate is bypassable (implementation defect)

`check_schema_closed` contradicts the model-spec sentence "require a closed root object and closed explicitly typed nested object nodes" in two ways.

**Reproduction A: root opened through `patternProperties`**

```python
s = {'$schema': c.DIALECT, 'type': 'object', 'required': ['name'],
     'properties': {'name': {'type': 'string', 'minLength': 1}},
     'additionalProperties': False,
     'patternProperties': {'^': {}}}
```

- The root passes the closure test.
- `{}` passes `walk`.
- `check_schema` and `pointers` pass.
- The schema therefore accepts `{"name": "x", "anything": {...}}`.

`additionalProperties: false` only covers keys that `properties` and `patternProperties` do not match.

**Reproduction B: explicit type written as a list**

Take the passing `test_nested_open_object_refused` fixture and change the snapshot to `{'type': ['object']}` or `{'type': ['object', 'null']}`. The check `x.get('type') == 'object'` is false for a list, so an open object is admitted. This is still "explicitly typed", so it directly contradicts the claim.

**Fix (about six lines):**

- Treat a node as object-capable if `'object' in (t if list else [t])`, or if it has `properties`/`patternProperties` and no `type`.
- Refuse `patternProperties` in this profile, or require it to be absent whenever closure is claimed.
- Add both reproductions as tests.

**Also decide on untyped subschemas.** `{}`, `true`, and `{'type': 'array'}` with no `items` each accept arbitrary nested objects. Either refuse them or reword the claim to: "closes only nodes that explicitly declare `type: "object"` (string or list); untyped or boolean-`true` subschemas remain open and are the companion validator's responsibility."

### X2: AI-team nested evidence does not prove what the spec claims (evidence defect)

The model-spec says: "Malformed nested context must fail its companion even when the outer native record passes V3." `acceptance.py` does not show this.

- The companion runs on `example-founder-draft.json` and on a mutated copy.
- The records written into the Dimension are separate files: `native-object.reference.json` and `native-fact.reference.json`.
- Nothing asserts that the fact's `value` equals the positive example.
- The malformed variant is never written as a fact, so the "outer record passes V3" half of the claim is never exercised.

**Fix:**

- Run `module.errors(fact['value'])` on the actual stored fact.
- Write the bad variant as a fact into a throwaway copy, assert that `native_validate` passes, and assert that the companion rejects it.
- Alternatively, reword the claim to "companion rejects a malformed example; V3 accepts the well-formed stored fact."

### X3: overclaiming text (fix before publication)

1. **README, "Замкнутый состав включает все обязательные зависимости"**, and model-spec "all mandatory targets present / no extraneous packages". Closure and minimality are computed only over the edges declared in `requires` in the plan. Nothing reads dependencies out of the specification bytes. A plan that omits a real dependency passes `CLOSURE` and `MINIMAL`. Say "all *plan-declared* mandatory dependencies". Also add a one-line limit: dependency declarations are plan assertions and are not extracted from specifications.

2. **"symbolic-link/junction traversal are rejected"**, while the README requires Python 3.11+. `Path.is_junction` only exists from Python 3.12, so the check is skipped on 3.11. `resolve()` still stops junctions that escape the root on Windows, but junctions inside the root are accepted, and no test covers symlinks or junctions. Either require 3.12+ or say "escaping links are rejected; on 3.11 intra-root junctions are not detected."

3. **Upstream scope.** `upstream-verification.json` covers only the three `spec.yaml` files. The README says "копии опубликованных пакетов", and the model-spec says "published … model with its explicit reference binding". The AGENTS, runtime, instance-schema and companion descriptors carry `sourceUrl`s that were not verified. If any of these assets, such as the Organization "reference" binding, were authored by this package, state that. Their `sourceUrl` must not imply ver.cy published them unless it did.

4. **"mandatory nested checks for structured snapshots"** (Key requirements) and the bootstrap docstring "Nested semantic validation remains mandatory". The code only requires that the schema and companion *descriptors are present*. Nothing executes them, and the bootstrapped registry row does not reference them. Say "presence mandatory; execution is a separate step-7 obligation, recorded only in `composition/plan.json`."

5. **"failure cannot replace an existing target"**. On POSIX, `os.rename(dir, existing_empty_dir)` succeeds. An empty target directory created by a non-cooperating process between `require(not target.exists())` and `os.rename` would be replaced silently. Windows raises an error in this case. Qualify the claim as "on the tested Windows filesystem; cooperating writers only", which matches the "no adversarial isolation" limit already stated.

6. **Minor wording:**
   - The README's "не модель сотрудников OpenAI" names an unrelated third party for no reason. Remove it.
   - The example plans expire on 2026-12-31. After that, `acceptance.py` and the README quick-start fail with `TIME` by design. State "reproducible until 2026-12-31; regenerate policy and plan afterwards."

## Non-blocking implementation defects (should fix; all fail closed)

- **Unstable error category.** The CLI catches `Invalid, ValueError, OSError, KeyError, TypeError, RecursionError` but not `AttributeError`. For example:
  - A spec asset with bytes `[]` and a correct digest makes `spec.get` raise `AttributeError`.
  - `"metaModel": "x"` does the same.
  - A `receipt.json` that is a list, or a bootstrap lock that is not an object, also crashes with a traceback.

  Nothing is written, but this contradicts "return a stable error category". A naive `--at` value surfaces as an uncategorized `TypeError`. Fix: add `isinstance(..., dict)` requires, or map these to `SPEC`/`LOCK`/`TIME`.
- **Cleanup ordering.** In both `finally` blocks, `shutil.rmtree(temporary)` runs before `shutil.rmtree(lockdir/lease)`. If the first fails (common on Windows when AV or indexers hold file handles), the lease survives a *normal* exception and the original error is masked. Guard each cleanup step separately.
- **B4 hardening.** After patching, assert that `str(temp)` no longer appears in any file in the new Dimension. Today only two known fields are checked.
- **Format checking.** `FormatChecker` silently skips `uri` and `date-time` unless the jsonschema format extras are installed. Patterns mitigate this, but an out-of-range date such as month 13 reaches `stamp()` as a `ValueError`. Either pin `jsonschema[format-nongpl]` or stop implying format validation.
- **`registries/events.yaml`.** Confirm that this file holds event instances and is not an event-type catalogue. Acceptance reports `events: 0` after the bootstrap appends an entry, which suggests V3 does not treat that entry as an event.
- **Executable companion in the Dimension.** Bootstrap copies the companion `.py` into `models/composed/…`, but the Dimension's own AGENTS.md carries no "untrusted package text, never execute without explicit approval" note. The staging AGENTS.md has that note.
- **Test gaps behind claimed categories.** No tests exist for:
  - an expired or not-yet-effective policy;
  - a reviewer not on the allowlist;
  - a plan that expands the model allowlist;
  - a future `recordedAt`;
  - duplicate or overlapping required/optional edges;
  - a malformed lock.

  `test_alias_path_collision` uses an *identical* path, so it does not test case-insensitive collisions. Add `Test.Company/AGENTS.md` against `test.company/AGENTS.md`.
- **Fail-closed false refusals.** `walk` treats every dict as a schema, including values inside `const`, `enum`, `default`, `examples` and property names such as `"$ref"`. It can therefore refuse valid schemas. This is acceptable in this profile; document it.

## Explicitly deferred scope (not defects)

- Compatibility, publication status, `role`, reviewer and publisher assertions are policy-checked but not cryptographically authenticated. A compatibility decision is not bound to a release digest.
- There is no range solver, MVS, ELMM runtime, online discovery, or dependency extraction from specification bytes.
- There is no migration or upgrade of existing Dimensions; `NEW-ONLY` and `MIGRATION` refuse by design.
- There is no IAM or read-side enforcement, power-loss durability, distributed or adversarial locking, or automatic companion execution.
- Only JSON and JSON-with-header specifications are accepted; general YAML is out.
- Only the commercial-company preset is supported.
- Research assurance stays `reviewable-draft`, separate from `published`.
- Caller trust and filesystem permissions are external.

The model-spec and README already state all of these honestly, apart from the X3 items.

## Minimum path to ACCEPT WITH LIMITS

1. Fix X1 by closing list-typed objects and refusing `patternProperties`, add the two reproductions as tests, and state whether untyped or `true` subschemas are open.
2. Fix X2 by adding the linked positive and negative nested acceptance run, or reword the claim.
3. Apply the six X3 wording corrections.

No re-architecture is required.
