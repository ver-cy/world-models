# R3 static audit: Enterprise Action Requests 0.1.0 candidate

## 1. Method, input completeness and verdict

### Method used

I did one manual static read of the supplied frozen fragments inside this conversation. I used no tools, browsing, code execution, subagents or prior conversations. I traced control flow in the generated `action_bundle.py`, compared it against `spec.json`, `action.schema.json` and `build_schema.py`, and hand-traced the tests and the acceptance scenario.

Beyond reading, I did two kinds of arithmetic and comparison checks:

- I summed the declared fragment lengths and compared them to the manifest byte counts.
- I compared digest strings across `bundle-build.json`, the manifest, `test-results.json`, `test-bundle-results.json` and `acceptance-results.json`. This was string equality only. I did not compute any SHA-256 values.

I did not run tests, check raw-file hashes, execute the native creator or validator, or read the hash-only files. These include `model-spec.md`, `README.md`, `adoption-limits.md`, `requirements.txt`, `model-fields.md`, `tool-pins.json`, the separate `action.py`/`history.py`/`native.py` sources and the pinned native toolchain. I treated test and acceptance reports as assertions.

### Input completeness

| File | Fragments seen | Seam and length check |
|---|---|---|
| spec.json | 17/17 | Seams continuous. Compact display, so it cannot be length-matched to the 135,989 raw bytes. |
| action_bundle.py | 9/9 | 8×6000+2259 = 50,259, which equals the manifest bytes. All eight seams are continuous mid-token (e.g. `autho`/`ritative`, `targe`/`t)`). |
| test_action.py | 6/6 | 32,804 chars, plus 3 bytes for three literal `é` characters, gives 32,807. This equals the manifest. |
| install_fixture.py | 1/1 | 4,471 equals the manifest. |
| acceptance.py | 2/2 | 6000+2706 = 8,706 equals the manifest. |
| Other required files | action.schema.json 5, build_schema 1, build_bundle 1, bundle-build 1, run_tests 1, fixtures 1, runtime-model 1, test-results 2, test-bundle-results 2, acceptance-results 2, AGENTS 1, migration 1, review 1 | All present and matching the required coverage list. |

Required functions, all seen:

- `Executor.dispatch` (fragments 3–4)
- `Executor.lookup` (4)
- `Executor.cancel` (4)
- `Executor.observe` (4–5)
- `Executor._tx` (2)
- `history._validate` (5–7), including the nested `current_policy` (5)
- `native._verify_export` (8–9)

No fragment is absent, truncated or elided.

The digest strings are internally consistent across all reports. For example, bundle `6f36…50f4`, schema `9c84…bc5` and test file `3ca1…1137` agree everywhere. I did not verify that these digests match the actual bytes.

### Verdict: accept-with-explicit-limits

The verdict covers the bounded synthetic fixture only. I found no blocker and no major contract violation in the supplied code. The minor findings below are non-blocking. If any are fixed, the candidate must be re-frozen and re-audited, because the hashes change.

The verdict does not cover the unsupplied adoption documents. Their content is unreviewed, and reviewing it remains a release precondition.

## 2. Findings

### Blockers
None found.

### Major
None found. Every R3 correction I was asked to challenge holds statically:

- **Strict grammar:** `(?![\s\S])` under jsonschema's `re.search` refuses trailing newlines. Code-side checks use `re.fullmatch`.
- **Namespace collisions:** checked in `add_definition`/`add_resource` and by `_fresh_id` across four tables. History has `object-kind-collision` and `event-object-collision`.
- **Caller projections:** `_public_event` strips `sequence` and `controlSequence`.
- **Canonical bytes:** the manifest, snapshot and record byte checks are in `_verify_export`.
- **Executor-impossible histories:** `rightless-replay`, `unreadable-denied-cancel` and `operation-incomplete` are enforced.
- **Other fixes:** binary-search `current_policy`, `request_by_id` indexing and the nine-file install with readback are all present.

### Minor: code or validator

**M1. `history._validate` has no single clock across control-sequenced tables (validator gap).**
- *Counterexample:* take a valid snapshot with an event at control 5 recorded at T+10. Insert a policy at control 6 recorded at T+5, with a later event at control 7 recorded at T+10.
- *What happens:* `policy-time` checks only the policy chain and `≤ meta.clock`, and `event-order` checks only events. So the snapshot is accepted.
- *Why it matters:* `_tx` refuses clock regression, so the executor cannot produce this history. The same gap applies to definition `recorded_at` and revision-0 resource `recorded_at`.
- *Impact:* limited, because decisions key on control sequence. But the R3 claim that history rejects executor-impossible histories is not fully general.
- *Fix:* merge `(control_sequence, recorded_at)` from definitions, policies, revision-0 resources and events, sort by control, and require `recorded_at` to be nondecreasing.

**M2. `parse` can raise a plain `ValueError` instead of `Refused` (normalization nit).**
- *Cause:* a JSON integer literal longer than 4,300 digits fits within 128 KiB. Python 3.12's `int` limit then raises `ValueError`, which is not a `JSONDecodeError`.
- *Current handling:* callers still normalize it. `dispatch` returns withheld and `validate_snapshot` raises `snapshot-malformed`. So there is no external contract violation, but `parse` is not self-normalizing.
- *Fix:* add `ValueError` to the `parse` except tuple and map it to `wire-json`/`wire-number`.

**M3. `cancel` on a retired key returns `key-retired` to a reader (undocumented).**
- The spec documents retired-key lookup and dispatch, and says observe is withheld. Cancel is unspecified.
- The behavior is benign: no event is recorded.
- *Fix:* document it in the endpoint qualifications.

### Minor: test evidence

**T1. The intent half of `test_trailing_newline_in_ids_tokens_hashes_and_uris_refused` is vacuous.**
- For `actorId`, `send` passes the non-newline actor, so the `authenticated-actor` check fails regardless of grammar.
- For `audience` and `purpose`, the changed value mismatches the policy scope, so `submit` is denied and the result is withheld under the old `$` grammar too.
- The definition and policy halves do discriminate.
- *Fix:* assert `a.validate('Intent', i)` raises `Refused` directly.
- The static code fix is correct; only its test evidence is weak.

**T2. Some claimed properties have no discriminating test:**
- History refusal of a newline-suffixed `eventId` or `requestId` inside a snapshot.
- `_fresh_id` collision refusal, which would need a patched `uuid4`.
- M1's cross-table clock case.

### Minor: specification and metadata

**S1. `factMastership` omits synthetic resource revisions.** The supporting values describe them, but no mastership entry says that revision 0 is written by trusted admin and later revisions by the executor effect.

**S2. `factMastership.readerPurpose` overstates caller access.** For Submission, Delivery, Try, Disposition and KeyRetirement events, it says "Current exact read scope for request operations". In fact callers only ever receive receipt and observation projections.

**S3. `answer_contract.permittedActionId` could be misread as an authorization grant.** This is in tension with the model's own rule against deriving permission from descriptions. The action text disclaims it, but a name such as `guidanceActionId` would be safer.

**S4. The installed `spec.json` has a dangling reference.** It cites `review.json` for release disposition, but `install_fixture.FILES` does not install that file.

**S5. The fixture lock points at canonical published URLs.** `specUrl` and `agentsUrl` use `ver.cy/.../0.1.0` for an unpublished candidate. `simulationOnly` mitigates this, but a consumer resolving the URL could retrieve different bytes.

**S6. The spec wording overstates what installation does.** It says "Each installation stores snapshot.json…", but `acceptance.py` produces the cut, not `install_fixture.install`.

**S7. `acceptance-results.json` records no runtime versions.** Unlike the unit reports, it omits the Python, SQLite and jsonschema versions. The tool pins are hash-checked only.

### Explicit fixture deferrals (not violations)

These are all declared in the spec:

- A caller with any single right can grow the shared event log. For example, an observe-only non-reader can trigger a delivery and a denied try via dispatch replay. The host must rate-limit.
- A read-only caller can materialize expiry on dispatch, and a denied cancel records a try for a reader.
- The unsalted `keyHash` is exposed in native request facets.
- A coherent old store or archive passes validation.
- There is no quota, rollover or multi-cut migration.
- The native outer validator accepts nested tampering.
- Receipt `beforeLabels` reveal resource state written under other purpose/audience contexts to anyone holding read scope for the caller's own context. This is inherent to resource read, and worth stating in `adoption-limits.md`.

## 3. Adversarial static cases

1. **Trailing newline in an ID.** An intent with `resourceId: "urn:x\n"` fails the schema lookahead in `validate('Intent')`, so the caller gets withheld and no transaction opens.
2. **Forged rightless replay.** An appended delivery and try with `allowed: false` and no rights passes `decision-outcome`, has no tail and no shape error, and is caught only by `rightless-replay`. The check discriminates.
3. **Forged unreadable denied cancel.** It is refused by `unreadable-denied-cancel`.
4. **ID collisions.**
   - Admin creates a resource with the ID of an existing receipt or request: `object-kind-collision`.
   - A snapshot whose event ID equals a definition ID: `event-object-collision`.
   - A forged request ID `resource.<64hex>` makes `records()` fail with `native-id-collision`. It is refused, not silently merged.
5. **Manifest `controlSequence: 16.0`.** The `export-cut` equality passes (16.0 == 16), but `manifest-canonical-bytes` refuses it. `True` fails at `export-cut`.
6. **CRLF `snapshot.json` with rehashed manifest.** `read_text` normalizes newlines, so parsing and validation pass, but the raw `snapshot-canonical-bytes` check refuses it. A BOM becomes `JSONDecodeError`, which maps to `export-malformed`.
7. **Receipt stripped, resource and request rewritten to pending.** The group is `[delivery, try]` but the expected tail is `receipt`, so `operation-incomplete` fires.
8. **Compensation referencing another actor's receipt, a non-receipt event or an absent ID.**
   - All three give `rejected-precondition` with reason `compensation-precondition` in both the executor and history.
   - There is no existence oracle.
   - Short-circuiting on `original['kind']=='receipt'` prevents a `KeyError` on non-receipt payloads.
9. **Capacity.**
   - A first commit at 9,997 events adds 4 rows (10,001), so the `_tx` pre-commit check rolls back the effect, request, events and control increment. The caller gets withheld.
   - A lookup still works at exactly 10,000.
10. **Cancel/execute race.** Both paths run under `BEGIN IMMEDIATE`. `_terminal` requires pending, and the history's single-terminal replay agrees.
11. **Retired-key dispatch.** It returns before the rightless check and before any event. `key-retired` is shown only to a current reader.
12. **Symlinked `records/` directory or symlinked `manifest.json`.** The `rglob` symlink check refuses both, after `is_file` follows the manifest symlink.
13. **Backdated admin row (M1).** Accepted. This is the one executor-impossible class I found that passes.
14. **Policy capacity.** A non-empty policy at revision 9,999 is refused by `policy-revocation-reserve`. An empty policy at 9,999 is accepted, and a policy at revision 10,000 fails `store-capacity`. The test seeding arithmetic (revisions 2–9,998) is correct.

**Coverage limits:**
- I assumed jsonschema uses `re.search` for `pattern`.
- I assumed SQLite `BEGIN IMMEDIATE` and AUTOINCREMENT rollback semantics.
- The behavior of the native creator, `write_record` and the outer validator is unseen.
- Nothing about hardware faults, timing channels or performance can be concluded.
- I hand-verified the acceptance counts: control 16, 27 events, 11 objects, 38 records, 40 files, and `exportedAt` 2026‑09‑21T11:26:40Z from NOW = 1789990000. All are consistent with the scenario trace.
- I counted 69 distinct `test_` methods in the file, matching the report's ID list.

## 4. Semantic scope, facets, field contracts, navigation and installation

**Semantic scope.** The scope is coherent and appropriately narrow: two canonical objects, seven Event profiles, descriptive-only minimum adoption, and one local synthetic adapter. Permission never derives from description. The spec's endpoint asymmetries match the code exactly: admission while retired, expiry by any right-holder, and cancel needing cancel authority to terminalize.

**Five-facet coverage.** All five facets are marked "required", with object-specific reasons, for both objects and all seven events. Twelve supporting values are covered, including the new `SyntheticOrderedLabelResourceObject` and `CallerEventProjection`. The mastership gap is S1.

**Field contracts.** The schema is closed (`additionalProperties: false` throughout), bounded, and matches `build_schema.py`. `model-fields.md` was not supplied, so I could not check field-level prose against the schema.

**Navigation.** The declared statistics are correct: 5 bundles, 10 layers, 26 findings, 52 questions and 26 artifacts. Four nits:
- AR-F03 (Q05/Q06) appears before AR-F02 (Q03/Q04).
- The bundle descriptions are templated and low-information ("Definition of company action requests.").
- `answer_data` duplicates `answer_contract` verbatim, which risks drift.
- `ifMissing` is identical boilerplate across all 52 questions.

The questions are correctly framed as host guidance.

**Installation.** The nine-file exact copy, pre- and post-readback, empty-path runtime assertion, candidate/simulationOnly lock, and "NOT WM-XCT-040 acceptance" labeling are sound. The concerns are S4, S5 and S7, plus the unreviewed content of the four installed documents.

## 5. Release recommendation (no authority claimed)

Statically, the implementation meets its bounded synthetic contract. I recommend treating it as accept-with-explicit-limits.

Before any release decision, the release authority should:

- Obtain the independent Grok R3 audit.
- Re-run the source, bundle and native reports against the frozen hashes, which I did not do.
- Have a reviewer read the unsupplied installed documents and `requirements.txt`.
- Complete live publication verification.

M1 and T1 are the most worthwhile follow-ups, followed by the S1–S4 wording and metadata fixes. Any fix requires a new frozen round.

This audit grants no publication authority and makes no claim about raw-file integrity.