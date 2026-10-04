**ACCEPT WITH LIMITS**

Independent static R2 audit only. No tools, no execution, no URL fetch, no connectors, no hash recomputation. Displayed SHA-256 values are supplied pins, not independently verified. Author `test-results.json` (50 passed) and `acceptance-results.json` (3 profiles) are author evidence of separately executed tests, not this review’s execution. This is not certification, publication authorization, or production-connector approval.

## Input completeness

All **15/15 R2 fragments** were received. R1 was withdrawn and was not used.

**Visible in full (source/docs/tests/reports):** `model-spec.md`, `adoption-limits.md`, `bindings/native-v3.md`, `sync_register.py` (all listed functions), `sync.schema.json` (minified; fragments 5–6 join at `op` and match `build_schema.py` `OPS`), `build_schema.py`, `test_sync.py` (all 50 `SyncTests` methods named in the author report), `fault_worker.py`, `fixtures.py` (including `generate_profiles`), `run_tests.py`, `acceptance.py`, `test-results.json`, `acceptance-results.json`, `runtime-model.reference.json`, `spec.json` (fragments 11–13 join at `applicable` / `explicit`), `AGENTS.md`, `model-fields.md`, `composition.yaml`, `crosswalk.json`, `invariants.md`, `migration.md`, `lifecycle/transitions.md`, `README.md`, `requirements.txt`.

**Not visible — not inferred from hashes:** `examples/startup.json`, `examples/international.json`, `examples/ai-team.json` bodies; `tool-pins.json`; `review.json` / `review.md`; upstream composer/skill bytes. Native fixture event bodies therefore cannot be checked here.

Schema/API/docs/native-acceptance **source** was visible. Example **data** used by `acceptance.py` was not.

## Verdict

Visible R2 code implements the stated 0.1.0 closed contract tightly enough to accept as a bounded companion reference, with residual contract gaps and documented host duties. The R1 long-register-ID and event-limit retry defects are addressed in visible R2 (`registerId` max 160, `event_id` derivation, `test_maximum_register_id_remains_replayable`, `test_exact_retry_at_event_budget`, `test_denied_at_event_budget_is_uniform`, pre-persist `JournalEvent` validation and archive byte-budget encode).

No visible reducer path silently double-activates a lineage/purpose, repins a historical occurrence, breaks conservation, resumes an archive, or treats native outer validity as nested history.

## Findings (non-blocking unless noted)

### 1. `Register.execute` + `apply` (`op=commit`) — retained conflict at event cap
**Scenario.** Store already has `len(events)==MAX_EVENTS`. Exact own retry: `retained=False`, returns original ack. Unauthorized caller: `DENIED`, no event. New first-admission or authorized **conflict** (`principal-collision`, `changed-content`, `stale-head`, `stale-fence`) sets `retained=True`, then `require(len(events)<MAX_EVENTS)` raises `Invalid` instead of uniform `not-accepted`.
**Correction.** Either persist a no-event uniform `not-accepted` for those collisions at cap, or state in `model-spec.md` that conflict diagnostics are new retained events and are refused with `Invalid` at the demonstration budget.
**Limit.** Spec only promises exact retries and unauthorized refusals at the cap. Not a pin/retry-identity break.

### 2. `time` — schema-valid, calendar-invalid timestamps
**Scenario.** Authorized `commit` / `mapping` / host `now` with `2026-13-01T00:00:00Z` (or `T24:00:00Z`). Schema pattern `^20[0-9]{2}-[0-9]{2}-[0-9]{2}T[0-9]{2}:[0-9]{2}:[0-9]{2}Z$` accepts it; `datetime.strptime` raises `ValueError`, not `Invalid`. Transaction rolls back; no persist.
**Correction.** Parse inside `time()` and raise `Invalid` on calendar failure.
**Limit.** Host clock/observedAt are trusted inputs; this is error-shape, not silent accept.

### 3. `apply` (`op=mapping`) — `corrects` need not share lineage/purpose
**Scenario.** Steward creates mapping B with `corrects=A` where A is a different lineage or purpose. Create succeeds (`proposed`). Activation only requires A to be `retracted`.
**Correction.** Require predecessor lineage+purpose identity (or an explicit “unrelated predecessor allowed” sentence).
**Limit.** Activation uniqueness still prevents two actives for one lineage/purpose.

### 4. `mapping_outcome` — validity-window miss shares `active-pin-suspended`
**Scenario.** Active mapping exists; item `observedAt` is outside `[validFrom, validTo)`. Same branch as catalogue/kind failure returns `active-pin-suspended` with `pin=None`. Spec names that status for reclassification / source-kind change; the window check is specified but the status is not named for expiry.
**Correction.** Distinct status or an explicit spec sentence. Add a test.
**Limit.** Active claim still reserves uniqueness; historical pins are not rewritten.

### 5. `native_records` vs `Bootstrap.registerId` — slash and short IDs
**Scenario.** Schema pattern allows `urn:` + `/`; `native_records` requires `r'[A-Za-z0-9][A-Za-z0-9._:-]{2,159}'` (no slash; min 3). A slash `registerId` can be stored and journaled, then native export refuses without rewrite (`bindings/native-v3.md`).
**Correction.** Align schema pattern with the native-safe class, or reject non-projectable IDs at `Register` bootstrap.
**Limit.** Documented refuse-without-rewrite. Fixtures use slash-free IDs.

### 6. Schema vs reducer tightness
**Scenarios.**
- `SnapshotRound`: schema does not encode `(previousRoundId is None) == (notEarlierEvidence is None)`; `apply` (`op=round-open`) does.
- `BatchContent`: `roundId` set and `pageIndex` null is schema-valid; `apply` (`op=commit`) then `require(pageIndex==len(pages))` raises `Invalid`.
**Correction.** Mirror the pair/page rules in schema `oneOf`/`dependent` constraints so invalid envelopes fail `validate('Command')` before reducer semantics.
**Limit.** Invalid input is still refused; not an admit path.

### 7. `apply` auth-before-schema — authorized malformed → `DENIED`
**Scenario.** `commit` / `mapping-state` / `round-seal` with missing `body.id` / `content` keys: `KeyError`/`TypeError` returns `{'status':'not-accepted'}` before `validate('Command')`, same shape as no grant or unknown mapping/round id.
**Correction.** After a successful grant check, raise `Invalid`/`ValidationError` for malformed authorized input; keep uniform `DENIED` only for auth failure.
**Limit.** Documented: unauthorized and some invalid envelopes share `not-accepted`. Not a receipt-lookup leak for revoked callers (`test_revoked_writer_cannot_probe_receipts`).

### 8. Packaging / disclosure nits (not reducer defects)
- `composition.yaml` contains JSON.
- `spec.json` / acceptance `publicationStatus: published` vs README / `model-spec.md` “unpublished implementation candidate” — metadata, not runtime.
- `inspect_import` `LossReport.detail=str(error)` can echo privileged exception text. Host disclosure duty.

## Contract points that hold in visible code

- Semantic boundary: no Company/Project/Person/Dataset factory; aboutness is catalogue+pair gated; source-deleted / removed-from-scope / inaccessible do not edit catalogue or mappings (`test_source_delete_has_no_subject_effect`).
- Auth precedes receipt lookup; unauthorized `commit` appends no event.
- Batch identity `(scopeId, epochId, batchKey)`; content digest excludes `attemptId` / `expectedHead` / `fence` / computed pins; exact own retry short-circuits stale fence/head and does not repin (`test_retry_after_mapping_change_and_progress_retains_pin`).
- Closed epoch: every `COMMIT` returns `not-accepted` with no event; `read_receipt` remains separately granted.
- Conservation `received == accepted + quarantined`; `empty` must match `len(items)==0`; quarantine remains `open`.
- Activation uniqueness on complete lineage+purpose; disputed confers no pin (falls through to `unmapped`).
- Unknown generation is non-joinable; `01` ≠ `1`; new source-instance generation is a new lineage (`unmapped` until a new mapping).
- `assess_rounds`: proposals only, empty `effects`; best-effort / `visibilityCovered=false` / errors / quarantine / unknown order → `insufficient-context`.
- `resume_archive` always refuses; `validate_archive` replays and compares derived state/root; `validate_native_snapshot` requires nested replay and strict event prefix.
- Tokens are opaque evidence refs; head is local receipt id, not token sort order.

## Documented host duties / deferrals (not code defects)

Authentication, source/steward verification, catalogue/policy competence, current time, owned-current SQLite (clones/backups undetectable), protected evidence custody and fetch, current disclosure wrapping of archives/native copies, no IAM/wildcards, no live connectors, no partitions, no erasure or quarantine-resolution API, no writable import, no EFA/EAP adapter, no distributed exactly-once, no bitemporal repin/reprocess, no production-scale index. Authorized writers can infer key unavailability. Digests are byte-consistency declarations, not authenticity or latest-head proofs.

## Tests missing (meaningful, not executed here)

- Authorized conflict at `MAX_EVENTS` (finding 1)
- `mapping.corrects` cross-lineage (finding 3)
- `observedAt` outside mapping window (finding 4)
- Explicit disputed-claim → no operative pin
- Intake-only actor submitting a correction
- `epoch-close` with an unsealed round
- Bootstrap admin `commit` without intake grant
- Two purposes, same lineage, both active (should succeed)
- `read_receipt` with wrong purpose
- Slash / 1–2 char `registerId` vs `native_records`
- Grant expiry vs exact retry
- Calendar-invalid timestamp error type (finding 2)
- Byte equality of `examples/*.json` to `generate_profiles` (bodies not in fragments)

## Residual adoption limits

Version 0.1.0 remains a local metadata register: 2,000 events, 256 descriptors/batch, 8 MiB canonical archive, full replay per operation. Process-crash tests are not power-loss/hardware certification. Native snapshots are restricted historical projections. Copied archives do not enforce later revocation. Startups may use source/scope/descriptive mapping governance only with host-supplied actors, grants, clock, evidence store, and owned current database. The three synthetic profiles are not named companies. Research assurance stays reviewable-draft.

**No-tools statement:** this verdict is a static reading of the concatenated R2 PAYLOAD texts only. No code was run, no URLs fetched, no connectors used, no hashes computed, no fixture databases opened.