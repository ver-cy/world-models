## 1. Method, completeness, verdict

**Method.** Static read-only reconstruction of the frozen R3 packet. No tools, execution, hash recomputation, browsing, or test runs. `spec.json` (17/17), `test_action.py` (6/6), `install_fixture.py` (1/1), `acceptance.py` (2/2), schema/builder/fixtures/reports, and recovered `action_bundle.py` (9/9) were read as text. Bundle fragments were concatenated in order, including mid-token splits (`autho|ritative`, `actorId':|actor`, `WHERE i|d=?`, `dimensi|on']`, `match|es and`, `targe|t).as_posix()`). Reports claiming 69/69 tests and three native installs were treated as assertions only. Behavior was taken from visible function bodies, not from test names.

**Fragment counts actually used**

| File | Fragments used | Complete? |
|---|---|---|
| `spec.json` | 17/17 | Yes (compact display) |
| `action_bundle.py` | **9/9** (recovered in this thread) | Yes, after concatenation |
| `test_action.py` | 6/6 | Yes |
| `install_fixture.py` | 1/1 | Yes |
| `acceptance.py` | 2/2 | Yes |

**Named functions — all visible after reconstruction**

| Symbol | Where |
|---|---|
| `Executor.dispatch` | bundle 3–4 |
| `Executor.lookup` | bundle 4 |
| `Executor.cancel` | bundle 4 |
| `Executor.observe` | bundle 4–5 |
| `Executor._tx` | bundle 2 |
| `history._validate` | bundle 5–7 (`validate_snapshot` wraps it) |
| `current_policy` | nested inside `_validate` (bundle 5), `bisect_right` on ordered policy control sequences |
| `native._verify_export` | bundle 8–9 (`verify_export` wraps it) |

**Verdict: accept-with-explicit-limits.**

The earlier **INPUT INCOMPLETE** finding is resolved for the implementation source. This is not publication authority. `review.json` still records `publicationDecision: not-yet-made`.

---

## 2. Findings (code contract vs fixture deferral)

No remaining **blocker** against the written 0.1.0 fixture contract was visible in the reconstructed bodies.

### Majors
None demonstrated as expected-vs-actual contradictions in the supplied source. R3 items that were independently checkable in code:

- End-anchored ID/token/hash/URI grammar lives in `build_schema.py` / `action.schema.json` (`(?![\\s\\S])`) and is applied through `validate(...)` plus `re.fullmatch` on create/resource/retry-key/export paths.
- Admin/generated collisions: `add_definition` / `add_resource` reject IDs present in requests, events, and the other object table; `_fresh_id` checks definitions/resources/requests/events; `_validate` rejects definition∩resource, request∩objects, and `eventId ∈ object_ids`.
- `_public_event` drops `sequence` and `controlSequence`; `_out` and `observe` use it; `snapshot()` keeps full events.
- `_verify_export` requires exact `file_bytes` for snapshot and manifest, file-set closure, hashed paths `records/[a-f0-9]{64}.json`, cut field equality, and regenerated native bytes.
- History refuses rightless execute replays (`rightless-replay`), cancel tries that are neither allowed nor readable (`unreadable-denied-cancel`), and incomplete tails (`operation-incomplete` / `operation-shape`).
- Installer `FILES` is the nine named assets; lock is `candidate` + `simulationOnly: true`.

### Minors (not release-blocking inside this boundary)

1. **`Executor._fresh_id`** — one UUID attempt, no retry. Collision raises `generated-id-collision` (caller endpoints become `withheld`). Expected: unique ID. Actual: rare abort rather than resample. Minimal change: loop until free or cap attempts.
2. **Unknown definition pin and descriptive-only** share `definition-not-executable` in `dispatch` before admission. Spec does not require distinct codes; a readable caller cannot tell “missing pin” from “catalogued descriptive.”
3. **`observe` correction check** loads every event body. Correct vs 10k cap, not an enterprise scan design.
4. **Live policy read** is `SELECT` by `meta.policy_revision` (`Executor._policy`). Ordered binary search is only in `_validate.current_policy`. Matches the spec’s history/native wording; do not advertise bisect on the hot path.
5. **`requirements.txt` / raw-file SHA-256** were not recomputed here (display fragments, not raw bytes).

### Explicit fixture deferrals (not code defects)
Host authentication, issuer-standing truth, rate/admission limits, disclosure timing, file isolation, external latest-history, coherent-old-store detection, WM-XCT-040 composition, erasure, quotas/rollover, distributed effects, generic fact-path composer. Event budget 3,333 pending / 2,500 first commits is arithmetic on the 10k event cap, not a separate limiter. Boundary tests seed 10k rows with SQL; they do not claim 10k public API calls.

---

## 3. Adversarial static cases and coverage limits

Cases below were checked against **function bodies**, not treated as proven by `test-results.json`.

1. **Zero-rights replay.** `dispatch`: if a request exists and no submit/execute/read/cancel/observe match, return `WITHHELD` before delivery. `_tx` still commits a clock/control increment (spec: no event growth; admin sequence may advance). History rejects a forged delivery+denied execute try with no rights (`rightless-replay`).
2. **Unreadable denied cancel.** `cancel` writes a try only if cancel-matched or readable; otherwise `WITHHELD`. History `unreadable-denied-cancel` matches. Denied observe writes nothing.
3. **Expiry vs lookup.** `lookup` never calls `_terminal`. `dispatch`/`cancel` expire pending at `now >= expiresAt`. History requires expiry disposition guards. Passive post-deadline lookup can remain `pending` — specified, not a bug.
4. **Key conflict disclosure.** Readable is AND of new-intent read and stored-intent read; else `WITHHELD`. Status `key-conflict` only when both reads pass.
5. **Execute without read.** `allowed` uses execute matches + availability; `_out` redacts to `WITHHELD`. Effect can persist; caller cannot see it. Not constant-time (specified).
6. **Compensation.** New request must reuse actor/principal/purpose/audience/dimension, receipt kind, resource, definition pin, `afterRevision == expectedRevision`, `beforeLabels ==` new labels. Intervening revision or retired pin fails (`rejected-precondition` or `current-execution-denied`). No cross-version path.
7. **Operation tail.** Groups per `controlSequence` must be exactly one of the closed shapes; execute try must be preceded by same-CS delivery; missing receipt/disposition when the validator predicts a tail → `operation-incomplete`. Admin CS and event CS cannot overlap.
8. **Export bytes.** Trailing space on snapshot/manifest, float/bool `controlSequence` in the file, extra path, missing file, symlink, torn retry on same directory → `Refused`. Resume only identical bytes; changed cut needs a new directory.
9. **ID poisoning.** Definition/resource IDs equal to existing request/event IDs refused at admin write; generated `req.*` / `evt.*` checked across tables; history also rejects event/object ID overlap.
10. **Projection misuse.** Caller receipt/observation omit global counters; embedding those projections as schema `Event` would fail `oneOf` (sequence/controlSequence required). Native export keeps full events inside `enterpriseActionEvent`.

**Coverage limits.** No runtime, no raw-hash verification, no hardware crash, no multi-cut native migration, no host identity proof, no load test. Concurrent race outcome is serialized by `BEGIN IMMEDIATE` in `_tx`, not proven here. Coherent older DB with the same epoch still validates — explicit non-goal.

---

## 4. Semantic scope, facets, fields, navigation, installation

**Scope.** Two objects (versioned `ActionDefinition`, immutable `ActionRequest`), seven Event profiles, descriptive catalog vs one synthetic adapter (`local-sqlite-ordered-labels/1`). One SQLite master; native files are evidence. Permission is current exact dual-scope intersection, never inferred from text, steward, capability, or K2 name overlap.

**Five-facet map.** `spec.json` marks all five facets required for both objects, seven events, and supporting values (`Intent`, `DefinitionRef`, `AuthorityRuleAndScopes`, `CallerEventProjection`, `ExportManifest`, …). Code carries those fields through schema `$defs` and native facets `enterpriseActionDefinition` / `enterpriseActionRequest` / `enterpriseActionEvent` / `syntheticLabels`. Native object `state: active` is existence, not availability — consistent with spec.

**Field contracts.** Closed objects (`additionalProperties: false`); IDs vs tokens vs 64-hex hashes; half-open integer UTC windows; labels ordered, duplicable, max 32×200; wire bounds 128 KiB / depth 24; digest = SHA-256 of Python compact sorted-key UTF-8, **not** JCS (`encoded` docstring). Policy revisions 0..9998 plus reserved empty 9999. Caller `_out` may add `requestState` on readable denial while leaving stored state pending or terminal.

**Navigation.** 5 bundles, 10 layers, 26 findings, 52 host-guidance questions with if-missing → `insufficient-context`. Not an authority engine.

**Installation.** Visible installer creates a **new** Dimension, writes nine assets, empty runtime `paths`, candidate/simulationOnly lock, then acceptance text claims stored companion cut under `data/action-exports/cut-*`, outer + nested validation, nested tamper rejected (`native-record-projection`) while generic outer may still pass. That last split is a documented platform gap, not companion acceptance of WM-XCT-040.

---

## 5. Release recommendation

Treat 0.1.0 as a **bounded synthetic candidate** suitable for continued review and descriptive or local-label fixture use under a trusted host, with the limits already written in `adoption-limits.md` / spec / `AGENTS.md`.

Do **not** treat passing asserted unit/acceptance JSON, an internal `validate_snapshot` cut, or a native outer envelope as: production authorization, latest-history authenticity, composer publication, or a mandate registry.

Before any publication decision (still open in `review.json`): keep host rate/admission controls outside this code; do not run dispatch after an unreconciled restore; do not edit `action_bundle.py` except by regenerating from `action.py` / `history.py` / `native.py`; keep the candidate/`simulationOnly` lock until a separate release gate changes it.

No publication authority is granted or implied by this audit.