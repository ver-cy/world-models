# WM-XCT-040 0.1.0 — release audit

**Verdict: ACCEPT WITH LIMITS.**  
This is a publishable *reviewable-draft* shared contract plus an offline exact-closure reference. It is not a new kernel, not ELMM/MVS, not an authenticity service, and not a general installer. No remaining implementation defect in the supplied composer/tests/spec breaks the bounded claims. Research assurance stays `reviewable-draft`. Tests were not executed in this review.

## Boundary

**Accept.** One `ResolutionPlan` aggregate over the existing Vercy kernel. Exact declared `(modelId, version)` closure from the plan’s `requires`. Caller supplies trusted policy, lock, assets, and (for bootstrap) a local skill. NEW `commercial-company` Dimensions only. Semantic-only rows stay out of the V1–V3 registry. Package code is not executed by the composer. Existing Dimensions are refused. That is the product.

## Prior findings — disposition

| Prior | Status |
|---|---|
| B1 nested object closure | **Fixed in visible code.** `type==object` ⇒ `additionalProperties is False`; `$recursiveRef` and nested `$id`/`$schema` refused. `test_nested_open_object_refused`. Spec now says closed root + closed *explicitly typed* object nodes, not semantic completeness. Residual: untyped nodes / `$ref` → `true` — **limit**, not a defect. |
| B2 library `stage(..., at=)` | **Fixed.** First line of `stage()` refuses `at`. `test_library_historical_write_refused`. |
| B3 bootstrap untested | **Addressed by package artifacts**, not by this review’s execution. `acceptance.py` + Codex `acceptance-results.json`: three profiles, V3 counts, three activation-failure checks, existing Dimension preserved. |
| B4 global temp-path rewrite | **Claimed patched** to two named location fields. `bootstrap_dimension.py` is **not in this file set**; not re-read here. |
| B5 JSON-only spec parser | **Deferred scope, documented.** `test_real_yaml_profile_refused`. General YAML is refused by design. |
| B6 same-version different digest | **Fixed.** `test_same_version_changed_bytes_refused`. |

Also visible in `composition.py`: lease `owner.json` is inside `try/finally`; `evaluatedAt` uses the same `clock` as TIME checks; extra tests for internal `$ref`, draft assurance, empty AGENTS, shared fact path, kernel leaf, policy mutation before commit.

## Blockers

**None that should stop this bounded release.**  
Compatibility, publisher, and reviewer fields are policy-allowlisted assertions, not signatures — that is stated scope, not a hidden hole.

## Limits (keep these visible)

1. **Trust model.** Digest + `allowedOrigins` + reviewer URI allowlist ≠ publisher or reviewer authentication. A plan cannot self-authorize; it also cannot prove the review is true.
2. **Closure model.** `exact-closure-v1` walks the plan’s declared `requires`. It does not extract edges from spec text and is not SemVer/MVS.
3. **Spec bytes.** JSON, or JSON with one leading `#` line. That is the declared Vercy JSON-compatible projection. Arbitrary YAML is out of profile (`SPEC`).
4. **Adapter width.** NEW Dimensions, `commercial-company` preset only. No upgrade, downgrade, byte replacement, or in-place migration.
5. **What V3 accepted.** Codex report: startup 1 native / 1 object / 1 name fact; group 1 native + 1 semantic Unit / 1+1; AI-team 2 native / 2+2, with companion pos/neg run **only** in `acceptance.py` via `exec_module`. Composer still never runs companion or package hooks. This is not Organization, Unit, or performance-domain completeness, and not an employment decision.
6. **Activation.** Directory rename on a cooperating local filesystem. No power-loss durability, no cross-device rename, no adversarial multi-user isolation. Stale lease stays `BUSY` until inspected.
7. **External trust.** Policy file, lock bytes, `--assets` tree, filesystem permissions, and the caller-chosen Vercy skill are outside this package.

## Overclaim watch

Do not say:

- that this implements ELMM, MVS, context budgeting, or ARCH/FED;
- that compatibility evidence is an authenticated review;
- that the composer “validated nested snapshots” (the harness did; the composer only required descriptors + a closed schema);
- that published-package acceptance covers the catalogue beyond the three pinned example specs;
- that a successful bootstrap proves company data or legal form (zero or one synthetic name fact is a control test);
- that `allowReviewableDrafts` installs `publicationStatus=draft` (it only admits `researchAssurance=reviewable-draft` on an already published coordinate).

README “publication available for use and further review” is acceptable **with** `reviewable-draft` and the table of scenario bounds. Spec language on authenticity, exact-closure, JSON-compatible specs, and commercial-company-only adapter is now aligned with the code.

## Profiles

- **Startup** — fit for a NEW Dimension plus Organization spec and an optional name binding. No Employee/HR/ERP required or invented.
- **Group** — fit for two-root closure: native Organization + semantic-only Unit, separate namespaces. Selection does not create a reporting line.
- **AI team** — fit as a composition and structure demo: Performance package bound, V3 envelope/type/unit, nested rule exercised in the acceptance harness. Not a personnel-evaluation system.

## Source limits

Reviewed here: `model-spec.md`, visible `composition.py` (tail truncated in the packet), `policy.schema.json` fragment, `test_composition.py` (55 methods), `acceptance.py`, `test-results.json`, `acceptance-results.json`, `upstream-verification.json`, `README.md`.

Not re-read in this pass: `bootstrap_dimension.py`, `composition-plan.schema.json` (not relisted), field catalog, whole-object coverage, example plans/assets. Codex reports of 55 passing unit tests, 3/3 acceptance profiles, three failure checks, and three ver.cy spec byte-matches are **their** evidence. Neighbor digests in those reports were not recomputed here.

**Ship as reviewable-draft with the limits above on the label.** Do not raise assurance, and do not describe it as a certified or enterprise-complete platform.
