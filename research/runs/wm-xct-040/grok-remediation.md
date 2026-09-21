**ACCEPT WITH LIMITS.** No remaining concrete release blocker in these diffs.

**Closure function.** Claude’s two holes are closed in the supplied walk:

- `patternProperties` is refused on every schema node, including the root. `additionalProperties: false` can no longer be reopened that way.
- `type` is normalized to a list, so `["object","null"]` is treated as an object. A `properties` map with no `type` must also be closed.

Root still requires `$schema` 2020-12, `type==object` (scalar, not a list—consistent with the existing root rule), `additionalProperties is False`, and a nonempty `required`. `$dynamicRef` / `$recursiveRef` / `$vocabulary` and nested `$id`/`$schema` stay out. Pointers still allow a `$ref` target of `true`; that is now an explicit companion residual, not a silent claim of total closure.

**AI acceptance.** The companion is no longer an in-memory-only demo. The harness uses the stored V3 fact payload (`native-fact.reference.json` / `example-founder-draft.json`), writes a mutated fact through `append`, asserts V3 still accepts the bad Dimension, then reloads the **written** file and requires companion rejection. The good fact is the same check on the bytes that landed. Composer still does not execute package code. That matches the wording fix.

**Bootstrap delta.** Safer, not wider: receipt and starting lock are typed against already-read bytes; events.yaml is no longer given a synthetic native event; observation goes under `composition/`; AGENTS.md gets an explicit non-execution notice *after* the single canonical-location line rewrite; `finally` still drops the lease if temp cleanup fails. Two named location writes are unchanged.

**Limits that must stay on the label:** plan-declared closure only; untyped/`true` subschemas may remain open; companion execution is a caller duty; publisher/reviewer assertions are not signatures; NEW `commercial-company` Dimensions only; Windows rename is cooperative; examples expire 2026-12-31; 68/3+3 pass figures are Codex-reported, not re-run here.

Do not raise `reviewable-draft`.
