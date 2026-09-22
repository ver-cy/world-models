**ACCEPT WITH LIMITS**

Severity: Medium operational residual / Low contract. No High implementation breaker in the 30 supplied bodies.

Scope of this verdict: no-tools static reading only. No execution, no browsing, no connectors, no independent hash verification, no test rerun. Author `test-results.json` (81 passed) and `acceptance-results.json` (3 synthetic profiles) are supplied evidence, not independently reproduced. `review.json` / `review.md` are pending release bookkeeping and are not treated as acceptance.

## Input completeness

Received and read all 30 advertised bodies. END PACKAGE marker present: `SYNC-R3-EXACT-20260922`.

Body-supplied: `model-spec.md`, `adoption-limits.md`, `bindings/native-v3.md`, `sync_register.py`, `sync.schema.json`, `build_schema.py`, `test_sync.py`, `fault_worker.py`, `fixtures.py`, `run_tests.py`, `acceptance.py`, `test-results.json`, `acceptance-results.json`, `runtime-model.reference.json`, `spec.json` (including literal `model.scope`), `AGENTS.md`, `model-fields.md`, `composition.yaml`, `crosswalk.json`, `whole-object-coverage.yaml`, `mastership-and-rights.yaml`, `invariants.md`, `migration.md`, `lifecycle/transitions.md`, `README.md`, `requirements.txt`, `tool-pins.json`, `examples/startup.json`, `examples/international.json`, `examples/ai-team.json`.

Not body-supplied (8 inventory-only names; correctness not inferred from hashes): `parent-comparison.md`, `provider-roles.json`, `research-adjudication.md`, `research.md`, `source-verification.json`, `upstream/wm-xct-012-provenance/AGENTS.md`, `upstream/wm-xct-012-provenance/publication.json`, `upstream/wm-xct-012-provenance/spec.yaml`.

`tool-pins.json` inventories composer/skill/upstream bytes; those implementation bodies were not supplied. WM-XCT-040 / installed native writer / parent runtime are outside this audit. Display line endings may have normalized in transit.

Candidate publication metadata in `acceptance.py` is synthetic (`publicationStatus: published`, `researchAssurance: reviewable-draft`). That does not complete research assurance or authorize publication.

## Why not BLOCK

R3’s claimed repairs are present in the supplied reducer, schema, tests, and docs. No reproducible closed-contract counterexample was found that silently creates subjects, repins history, resumes an archive, accepts a changed build, or journals a rejected full payload.

### Identity and purpose
`SyncRegister` is a single-host metadata register. `apply()` never inserts catalogue subjects from intake. `source-deleted` / `removed-from-scope` / `inaccessible` are occurrence operations only; `test_source_delete_has_no_subject_effect` locks catalogue and mappings unchanged. Aboutness is `(sourceKind, targetKind, purpose)` against a host catalogue, not Identity same-as.

Qualified lineage in `lineage()` is exactly `[sourceId, sourceGeneration, resource, scheme, schemeVersion, key, recordGeneration]`. No case fold, numeric coercion, or Unicode normalization. `01` ≠ `1`; ZWJ-distinct keys stay distinct (`test_exact_qualified_keys`, `test_non_ascii_lexical_keys_remain_exact`). Unknown generation is non-joinable (`continuity-unknown`); mapping creation requires known generation.

Lineage omits `scopeId` and filter by written spec. Two scopes that differ only by filter share lineage+purpose uniqueness and can inherit a pin if `sourceObjectKind` still matches. That is a host interpretation duty, not a hidden subject merge.

### Closed contracts and type equality
`sync.schema.json` uses `additionalProperties: false` and required property lists. `encode()` / `decode()` refuse floats, duplicate keys, non-string keys, C0/DEL/C1, unpaired surrogates, and BOM. Schema patterns use `$` plus `(?![\\s\\S])`, so a trailing newline cannot pass (`test_schema_itself_rejects_trailing_linefeed`). Canonical comparison is sorted-key compact UTF-8 JSON; `bool` vs `int` substitution of derived state is rejected (`test_derived_state_bool_int_substitution_rejected`). `encode()` uses `type(x)==int` rather than `isinstance`, so `True` is not treated as `1`.

### Immutable pins and build binding
`BUILD_ID = sha256(sync_register.py bytes + NUL + sync.schema.json bytes)`. Bootstrap, archive, and native snapshot carry it. `replay()` requires that exact build and, after every event, `encode(result)==encode(event['result'])` and `digest(state)==event['outcomeDigest']`. Rewriting `outcomeDigest` plus the outer event digest still fails (`test_outcome_digest_cannot_be_rewritten_with_outer_hash`). A patched `BUILD_ID` refuses store open, `validate_archive`, and `archive_from_native`. No automatic migration. Hashes here are byte-consistency pins, not authorship or latest-head proof.

### Authorization and disclosure
Authorization precedes Command validation and receipt lookup. Unknown/malformed wrappers and missing mapping/round IDs used during the auth probe return `DENIED`. Bootstrap admin can declare sources/scopes/catalogue/policy/epochs/fences and is denied intake, map, and ordinary `read_receipt` (`test_admin_has_no_implicit_intake_mapping_or_read`). `attest-coverage` is a separate current grant for `source-snapshot` or `visibilityCovered=true`.

Occurrence correction: current `map` and `read` are required before `occurrence_by_id(state, oid, scope, purpose)`. Foreign scope/purpose or missing target → `DENIED`, no event. Same-scope/purpose wrong lineage → `Invalid`. Mapping `corrects` to a missing or foreign-purpose predecessor → `DENIED`; same-scope/purpose wrong lineage → `Invalid`. Those Invalid paths are steward-shaped after an in-domain grant, not a public existence oracle.

`read_receipt` is current read+purpose. `archive`, `assess_rounds`, `historical_cut`, and native projection helpers are privileged. `native_records` / `validate_native_snapshot` / `assess_rounds` take no actor; the host must wrap disclosure. Competing authorized writers can infer key unavailability from `DENIED` vs success on a fresh key; that side channel is documented.

### Mapping lifecycle
Proposal requires issuer==actor, known generation, catalogue/pair eligibility. Transitions: proposed→{active,disputed,retracted}, active→{disputed,retracted}, disputed→{active,retracted}, retracted terminal. Activation re-checks eligibility, one active claim per lineage+purpose, and retracted predecessor when `corrects` is set. In-place retarget of an existing ID is refused. Historical occurrence pins are not rewritten after later retract/correct (`test_retry_after_mapping_change_and_progress_retains_pin`). Catalogue reclassification or source-kind change yields `active-pin-suspended` on new pins while the active claim still reserves uniqueness.

### Retry, conflicts, atomicity
Batch slot is `digest([scopeId, epochId, batchKey])`. Content identity is the canonical batch content; `attemptId` / `expectedHead` / `fence` / computed pins are outside it. Exact own retry returns the original `{status:committed, receiptId}` and retains no event, even after later progress, fence change, or mapping correction. Digest match with unequal `encode(content)` returns `DENIED` without a diagnostic.

Admitted collisions journal `conflict-observation` + `ConflictRecord` only (key, attempt, preconditions, supplied digest, reason). Full rejected items are not stored (`test_conflicts_are_compact_bounded_and_do_not_advance_head`). Bounds: 128 total, 8 per actor/scope/epoch. Replay re-derives the reason and checks `outcomeDigest`. Submitting a stored conflict command as a client op hits `apply()`’s unknown-op branch and returns `DENIED` with no event.

One SQLite writer transaction (`DELETE` journal, `synchronous=FULL`, `BEGIN IMMEDIATE`). Conservation `received == accepted + quarantined` is required. Closed epoch: every `commit` is `DENIED` before key lookup; authorized read remains (`test_closed_epoch_commit_refused_read_allowed`). Process-exit tests cover before-COMMIT and after-COMMIT; they are not power-loss or lying-hardware certification.

### Snapshots and absence
`complete` is local key-accounting: terminal page, no seal errors, no quarantine, all snapshot-read with known generation. `assess_rounds` requires two complete `source-snapshot` + `visibilityCovered` rounds, increasing seal sequence, and an explicit earlier/not-earlier witness. Results are `steward-review-only` proposals or separately listed availability observations; `effects` is always `[]`. Best-effort, failed, quarantined, unknown-order, or filter-changed rounds are `insufficient-context`. Orphan-round close requires an explicit current intake grant to some operator, including admin.

### Native binding
Root schema closes `vercy-source-sync-journal-snapshot` (no derived `state`). `archive_from_native` replays to reconstruct the archive. Fact profile is a closed field set; extra keys and `authority.rank=false` fail. `factId` is `registerId + ':snapshot:' + root`. Same journal cut at a later `captured_at` keeps `factId` and may change envelope bytes. Only a strict event-prefix extension of a host-trusted predecessor is accepted. Outer native validity is intentionally not nested semantic proof.

## Required changes

None required for ACCEPT WITH LIMITS.

Optional tightenings, not conditions of this verdict:
- Align spec “same refusal” language with code: authorized new persist at event/byte cap raises `Invalid`; conflict overflow and conflict-at-byte-cap return `DENIED`.
- Emit `build_schema.py` bytes identical to shipped minified `sync.schema.json`, or add a pin test. Regenerating the pretty-printed schema changes `BUILD_ID` and refuses old stores.
- Document that `native_records` refuses Bootstrap URNs containing `/` without rewriting.

## Missing meaningful tests

Not blockers; behavior is in `apply()` / schema:

- `source-nonreuse-guarantee` generation basis (schema-legal; reducer treats attribution like other non-steward bases).
- Multi-page complete rounds (helpers commit a single terminal page).
- `assess_rounds` for `removed-from-scope` and `inaccessible` (only `source-deleted` is tested).
- Grant `now == validTo` boundary; month=13 calendar (Feb 30 is tested).
- Steward-asserted correction with `assertedBy` spoofed to another actor.
- Native export of a schema-legal registerId containing `/`.
- Generator output vs frozen `sync.schema.json` identity.

`test_duplicate_declarations_and_configuration_revisions` already covers duplicate source tuple and duplicate scope fingerprint via new IDs with default identity fields.

## Residual adoption limits

Documented host duties, not package defects: authenticate actors; verify source/steward declarations; supply current catalogue/policy/clock; keep the evidence store; establish current owned SQLite (clones and coherent old backups are undetectable); wrap privileged export/analysis/native APIs with current disclosure; classify secrets that look like identifiers.

Deferred by contract: live connectors, IAM, distributed exactly-once, source authentication, writable archive resume, automatic quarantine resolution/erasure, EFA/EAP adapters, partitioned streams, production-scale indexing, universal bitemporal remapping, cross-register comparison.

Hard reference budgets: 2,000 events, 256 descriptors/batch, 256 catalogue/policy entries, 8 MiB canonical archive, 128/8 compact conflicts. Full history is replayed per operation. Compact diagnostic loss at limits is explicit. SHA pins detect silent drift of installed bytes, not adversarially re-signed histories. Runtime/dependency pins (`Python 3.12+`, `jsonschema==4.26.0`) are separate host prerequisites.

Only exact installed companion semantics are claimed. Composer, native writer, and parent provenance implementations were not in the body set. This verdict does not authorize publication and does not complete the broader research contour.