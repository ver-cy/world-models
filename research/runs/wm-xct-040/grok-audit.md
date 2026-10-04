# WM-XCT-040 0.1.0 implementation audit

Static review of the supplied package only. Tests were not executed here. Codex’s 45/45 report is their evidence, not mine. Published-package acceptance is still open.

## Verdict

**Conditional accept** as a bounded *exact-closure-v1* pattern plus an offline staging reference. It is **not** a new mandatory kernel, **not** ELMM/MVS, **not** an authenticity service, and **not** installation-tested for Dimension bootstrap or live catalogue YAML.

Ship the composer (`composition.py` + plan/policy schemas + fixtures) with the blockers below fixed or explicitly scoped. Keep `bootstrap_dimension.py` as an experimental adapter until it has its own tests.

## Boundary decision

**Accept the published boundary.** It matches the smaller EM-KRN-01 contour:

- One contract aggregate: `ResolutionPlan` owns release refs, edges, descriptors, compatibility, authority snapshot.
- `RuntimeBinding` is a separate URI/version pinned to `forSpecificationDigest`.
- Staging `InstallationReceipt` is not a second lock.
- `KernelBoundaryDecision` is a memo, not an installable type.
- Existing ResolutionRequest/API UUID is reused; this package starts after exact selection.
- Semantic-only rows go to `registries/semantic-models.yaml`; only explicit native bindings enter `registries/meta-models.yaml`.
- NEW Dimensions only; existing pins require a separate migration.
- Package/companion code is not executed; V3 type+unit remains a later gate.

Employee, SoftwareProduct, Contract, and Enterprise Landscape are not kernel imports. Selecting them is a caller policy choice, not a type-system ban.

---

## Prioritized blockers

### B1 — Nested “closed schema” is enforced only at the root

`check_schema_closed` requires `type=object`, `additionalProperties: false`, and nonempty `required` on the **root** only. The walk blocks `$dynamicRef`, `$vocabulary`, and `$ref` outside `#/$defs/`. Nested object nodes may stay open.

Reproduction (static): native binding, a path with `valueTypes: ["object"]`, instance schema

```json
{
  "$schema": "https://json-schema.org/draft/2020-12/schema",
  "type": "object",
  "additionalProperties": false,
  "required": ["snapshot"],
  "properties": { "snapshot": { "type": "object" } }
}
```

Root is closed; `snapshot` accepts any keys. `test_permissive_nested_schema` only feeds a root missing `type`/`required`. Spec text says “closed JSON Schema 2020-12”.

**Fix:** recurse the closed-object rule into every `type=object` node, or narrow the spec sentence to “root closed”. Until then, do not claim nested-instance conformance.

### B2 — Library `stage(..., at=)` will write; only the CLI refuses history

`main()` rejects `stage` with `--at`. `stage()` itself still calls `validate(..., at)` and then `os.rename`.

Reproduction: plan whose `validUntil` is in the past relative to now; call `stage(plan, assets, policy, lock, target, at=plan["createdAt"])`. Validation can pass on the historical clock and the target is created.

**Fix:** `require(at is None, "TIME", "historical evaluation cannot authorize staging")` inside `stage()`, not only in CLI.

### B3 — Bootstrap is an untested second product

`test_composition.py` never imports `bootstrap_dimension`. The 45 tests cover `validate`/`stage` only. `test-results.json` scope already says native runtime acceptance is separate.

Bootstrap is the only writer of `semantic-models.yaml`, native `meta-models.yaml`, and composed lock pins. Spec step “Dimension bootstrapped” is therefore **specified, not demonstrated**.

**Fix:** add a fake trusted skill fixture (create_dimension + validate stubs) and assert: empty starting lock, semantic/native split, no companion execution, target absent beforehand, rename commit. Until that exists, do not call bootstrap implementation-validated.

### B4 — Bootstrap mutates every generated file with a global path replace

After `create_dimension.py`:

```python
text = f.read_text(encoding="utf-8")
text = text.replace(json.dumps(str(temp))[1:-1], json.dumps(str(target))[1:-1]).replace(str(temp), str(target))
```

over `temp.rglob("*")`.

Reproductions: (a) any non-UTF-8 file from the skill → `UnicodeDecodeError`; (b) temp path appearing in a hash, comment, or unrelated string → silent rewrite; (c) JSON-escaped Windows paths are guesswork.

Also hardcodes `--preset commercial-company` for every profile.

**Fix:** pass the final target into `create_dimension` if the skill allows it; otherwise patch named fields (`dimension.yaml`, storage bindings). Make preset a caller argument.

### B5 — Specification parser is JSON-only

```python
if text.startswith("#"):
    text = text.split("\n", 1)[1]
return json.loads(text)
```

`mediaType` allows `application/yaml`. Fixtures write JSON objects to `*/spec.yaml`. A real catalogue `spec.yaml` (`id:`, `---`, unquoted keys) raises `SPEC`.

This is consistent with “JSON-compatible Vercy profile” and with the prompt that published-package acceptance is pending. It is still a **publication-acceptance blocker**.

**Fix:** keep the limit in the README/spec in one sentence (“this profile accepts JSON or JSON-with-one-leading-`#` line only”), and add one fixture that is genuine YAML so the refusal is tested—or implement the declared json-compatible-yaml profile.

### B6 — Same-version changed bytes is implemented, not tested

```python
require(item.get("version")==r["version"] and item.get("digest")==r["specification"]["digest"], "MIGRATION", ...)
```

`test_implicit_upgrade_refused` only changes `0.9.0` → `1.0.0`.

**Fix:** lock pin `test.company` `1.0.0` digest A; plan `1.0.0` digest B → `MIGRATION`.

---

## What the composer actually holds

| Concern | Against the bounded claims |
|---|---|
| Authority | Holds. Caller policy bytes; `policyDigest` bind; plan cannot widen allowlist or draft flag; actor/purpose/owner/dimension must match; `allowInstall` ∧ `decision=allow`. Compatibility is reviewer-id allowlisting, not review truth. |
| Time | Holds for CLI. Naive datetimes fail SCHEMA. `--at` is validate-only at the CLI. See B2 for the library hole. |
| Immutable releases | Holds in code: one version per id; lock version or spec digest mismatch → `MIGRATION`. See B6. |
| Closure | Holds for exact-closure-v1: required DAG, `CYCLE`, missing exact target `CLOSURE`, extra nodes `MINIMAL`. `references` do not pull. |
| Path safety | Holds in Python: no abs/`..`/`\`/`:`/DOS reserved/symlink-junction; resolve stays under root; casefold collisions. Schema path pattern is weaker (`x/../../escape.md` is schema-legal). Keep the Python check mandatory. |
| Atomicity / idempotency | Holds on same-filesystem `os.rename`. Lease is cooperative mkdir; stale lease stays `BUSY` until inspected. Repeat stage with same plan digest and intact assets returns `changed=False` **after** `validate()` (so a revoked policy file bound to a new digest cannot sneak through). No power-loss or cross-device claim—and none is made. |
| Nested schemas | Holds as a **binding-contract** check, not instance conformance. Empty `paths: {}` refused. `object`/`array` requires both instance schema and companion descriptor. Companion is never imported or run. Receipt stamps `nativeRuntimeValidated=false`, `nestedSemanticsValidated=false`. See B1. |

Other matches: https origins only, no userinfo; sourceUrl is not fetched (trust is `--assets`); kernel-role node cannot `requires` packages; semantic-only XOR binding; NEW-ONLY empty lock; existing target without matching receipt is refused and left untouched.

---

## Nonblocking gaps

- `publicationStatus=draft` always `LIFECYCLE`; `allowReviewableDrafts` only allows `researchAssurance=reviewable-draft` on a **published** coordinate. Tighten the spec sentence so those are not read as one gate.
- No schema for receipt, composition lock, or `semantic-models.yaml`.
- `$recursiveRef` is not denied (only `$dynamicRef` / `$vocabulary`).
- `mediaType` is not checked against bytes. Companion `text/x-python` is copied under `models/composed/` on bootstrap—composer does not run it; later agents might.
- Lease `owner.json` is written **outside** the `try/finally` that removes the lease; a failed write after `mkdir` leaves a permanent `BUSY`.
- `evaluatedAt` calls `now()` again and can differ from the TIME clock by one second.
- `test_optional_cycle_does_not_import_packages` does not build a cycle.
- Missing tests: two natives sharing a fact path; `allowReviewableDrafts=False`; successful `#/$defs/` `$ref`; policy/lock mutation between evaluate and commit (re-read exists, untested); empty AGENTS; kernel role with zero requires (allowed).
- Fingerprint is preserved, never computed or compared—correct.
- Crosswalk defers ELMM/PLMM and does not import WM-XCT-037. Digests there are package-asserted, not recomputed here.

---

## Profile applicability

**Startup (one company model, no HR/ERP).** Composer: yes, on synthetic JSON-compatible semantic packages (`test_startup_semantic_only`). No Employee type is required or invented. Bootstrap: untested, preset-locked to `commercial-company`, cannot ingest current catalogue YAML (B3–B5). Fit for a lab NEW Dimension under a trusted policy. Not a claim that Organization facts exist.

**Group (two families, scoped namespaces).** Composer: yes—two roots, unique namespaces, one version per id, collision refused. Selection does not create reporting lines or legal subsidiaries. Same YAML/bootstrap limits.

**AI organization (nested snapshot + companion).** Composer: yes for the contract split—object/array paths require instance schema + companion descriptor; composer does not run the companion; V3 remains envelope/type/unit. That is the right split. It does **not** prove a malformed nested case fails (B1 + companion never executed + no instance records written). Do not present this as a production WM-ORG-017 binding.

---

## Source limitations

Read in full from the attachment: `model-spec.md`, `composition-plan.schema.json`, `policy.schema.json`, `composition.py`, `bootstrap_dimension.py` (recovered; the user prompt truncated it), `test_composition.py` (45 methods), `field-catalog.json`, `whole-object-coverage.json`, `crosswalk.json`, `test-results.json`.

Not read: `create_dimension.py`, `vercy.py`, live `spec.yaml` of WM-ORG-001/002/017, GitHub ELMM. Neighbor `specDigest` values are source-asserted. No unittest run in this review. No certification, no legal guarantee, no claim that Codex’s 45 tests were reproduced here.
