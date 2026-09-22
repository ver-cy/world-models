# EM-XCT-08 / Enterprise Source Synchronization 0.1.0: R2 static implementation audit

**Verdict: BLOCK.** There are two blocking code defects (B1 and B2 below) and several major and minor findings. This is not a certification and not a best-effort vote.

## 1. Input completeness

All 15 R2 fragments were received and concatenated in order. I disregarded R1 fragments 1–2 as instructed.

**Fully visible files:**
- Documentation: model-spec.md, adoption-limits.md, bindings/native-v3.md, AGENTS.md, model-fields.md, invariants.md, migration.md, lifecycle/transitions.md, README.md.
- Code: sync_register.py (every function, from `encode` through `validate_native_snapshot`), sync.schema.json, build_schema.py, test_sync.py (all 50 tests named in the report), fault_worker.py, fixtures.py, run_tests.py, acceptance.py.
- Data and reports: test-results.json, acceptance-results.json, runtime-model.reference.json, spec.json, composition.yaml, crosswalk.json, requirements.txt.

**Not visible, so not assumed from hashes:**
- `examples/startup.json`, `international.json` and `ai-team.json`. These are the native fixtures acceptance.py replays and compares against. I could not check them directly against the schema, the API or the documentation. I only checked their event counts (11/15/13) by deriving them from fixtures.py, and they are consistent.
- `tool-pins.json`, the `upstream/wm-xct-012-provenance/*` files, the composer and skill toolchain (`composition`, `bootstrap_dimension`, `write_record`, `validate_dimension`), and `review.json`/`review.md`.
- The `model.scope` text inside spec.json was replaced by a placeholder claiming it is identical to model-spec.md. I cannot verify that identity.

Conclusion: the source code and tests are complete for audit purposes. The native fixture and toolchain evidence is incomplete, so any claim of equality with the fixtures rests only on the author's reports.

## 2. Blocking defects

**B1. Derived outcomes are never persisted or bound, so historical pins depend on whichever reducer code is running.**

*Where:*
- `Register.execute` persists only `{sequence, previousDigest, actor, recordedAt, command, result, digest}`. For a commit, `result` is only `{status, receiptId}`.
- `replay`, `apply` (commit branch), `mapping_outcome`, `native_value`/`archive_from_native` (derived state omitted) and `validate_archive`.

*What is wrong:* model-spec says the single transaction "persists the original content, derived occurrences, durable quarantine descriptors, … counts, receipt and new head", and that later changes "never recompute pins". In the code, occurrences, lineages, mapping pins, quarantine IDs, counts, round `complete` flags and epoch heads exist only as reducer output. They are recomputed on every replay. Nothing in the SQLite store records which reducer bytes wrote it.

*Concrete scenario:* R1 and R2 are different `sync_register.py` bytes, but both declare `VERSION='0.1.0'`. Suppose a future patch with the same version string changes `mapping_outcome` (for example, how validity or suspension is decided). Every historical occurrence would silently get a new pin on the next `execute`, `archive` or `read_receipt`. Neither the store nor a native snapshot, which omits state, can detect this. Only an archive exported earlier would show the mismatch.

The supplied change note implies a related failure mode. R2 adds a 160-character `registerId` cap, and `initial` runs inside `replay`. A store created by R1 with a longer ID would therefore become unreplayable under R2, with no diagnosis beyond a schema error, even though the version string did not change.

*Required correction:*
- Bind a digest of each event's derived outcome into the journaled `result` (receipt with occurrences, pins, quarantine and counts; mapping revision records; round seal results). `replay` must require that the recomputed outcome matches.
- Record a reducer build identifier in the `bootstrap` table and refuse replay under a different build unless a reviewed migration exists.
- Change the version or build ID whenever reducer behaviour changes.
- Align the model-spec wording with what is actually persisted.

**B2. The closed-string contract accepts a trailing line feed.**

*Where:* every pattern in `sync.schema.json` and `build_schema.py`, as evaluated by `validate`/`Draft202012Validator`.

*What is wrong:* to my knowledge, the jsonschema library evaluates `pattern` with Python `re.search`. In Python, `$` also matches just before a final `\n`. So `^[^\x00-\x1f\x7f]+$` accepts `"42\n"`, and the URN pattern accepts `"urn:synthetic:writer\n"`. JSON Schema 2020-12 specifies ECMA-262 regex semantics, under which both strings are rejected. I have not executed this; it is a static reading.

*Counterexamples:*
- `RecordKey.value = "42\n"` becomes a distinct lineage from `"42"` that looks identical when displayed. Two visually identical keys can each hold an active mapping for the same purpose.
- An actor, scopeId or grant subject with a trailing LF creates a look-alike principal.
- `EvidenceRef.digest = "sha256:<64 hex>\n"` is accepted.
- `Bootstrap.registerId = "urn:x…\n"` is accepted at creation. It is only refused much later by `native_records`, which uses `re.fullmatch`.

Time fields are protected only incidentally, because `time()` checks that the length is exactly 20. The schema file, the API behaviour and any ECMA-conformant native validator therefore disagree, which is precisely the schema/API/fixture mismatch class the audit targets.

*Required correction:*
- Add an explicit check (for example in `encode` or `validate`) that refuses characters `\x00–\x1f` and `\x7f` in every string, or validate patterns with an ECMA-262 engine.
- Add negative tests for trailing `\n` in a key, an actor, a digest and the registerId.
- Decide whether C1 controls, bidi overrides and zero-width characters should also be refused. Currently they are allowed and undocumented, although "no normalization" is documented.

## 3. Major findings (not blocking individually)

**M1. `validate_archive` does not detect all changes to derived state.**

`state==archive['state']` uses Python equality, where `True == 1` and `False == 0`. Changing `rounds[R].sealed` from `true` to `1`, or `epochs[E].progress` from `1` to `true`, still passes. `inspect_import` then reports the archive as valid, and `assess_rounds` and `historical_cut` go on to use `archive['state']`. The semantic effect today is nil, but the documented "exact derived state / rejects changed state" claim is false.

*Fix:* compare canonical bytes, i.e. `encode(state)==encode(archive['state'])`. The test `test_archive_roundtrip_is_nonresumable` has the same `==` weakness.

**M2. Conflict diagnostics consume the finite register budget and store the full rejected body.**

In the `apply` commit path, `conflict()` retains an event for a principal collision, changed content, a stale head or a stale fence. Any authorized intake writer, or a buggy extractor stuck in a stale-head loop, can therefore exhaust the 2,000-event and 8 MiB budget. After that, every new commit raises `Invalid('event budget')` and there is no rollover path.

The journaled event also stores the entire conflicting command (up to 256 items), which contradicts the spec wording "only … retained conflict attemptIds enter this journal".

*Fix:*
- Store a digest-only diagnostic, not the rejected body.
- Cap or rate-limit conflict events per scope, epoch and actor.
- Document budget consumption by conflicts.
- Add a test that exhausts the budget.

**M3. Occurrence corrections leak information across scopes.**

This involves `apply` (the correction branch) and `occurrence_by_id`. Occurrence IDs are predictable: `registerId:seq:receipt:occurrence:n`. `occurrence_by_id` searches all scopes. A writer holding intake and map rights on scope A can submit corrections that reference guessed IDs. The distinct outcomes ("missing corrected occurrence", "correction lineage", or success) reveal whether an occurrence exists, and its lineage, in scope B. Scope B can be another filter or visibility scope over the same source/resource/scheme where the writer has no read grant.

This goes beyond the documented one-bit leak about key availability.

*Fix:* restrict correction targets to the same scope, or to scopes where the actor holds a current read grant, and return a uniform refusal otherwise.

**M4. Ordinary intake writers can make the coverage declarations that drive absence analysis.**

`round-open` is authorized with only the `intake` right, yet it declares `consistency='source-snapshot'` and `visibilityCovered=true`. Those declarations are what `assess_rounds` relies on. The spec says a host must establish them. The code gives that power to any writer.

*Fix:* require the admin or a separate attested right for these declarations, or document this explicitly as a host duty.

**M5. The version string does not identify the implementation.**

R1 and R2 share `0.1.0` but have different code. Archives and native snapshots carry only `version`. This is closely tied to B1: `validate_archive`'s "unsupported version" check cannot distinguish the two builds.

## 4. Minor findings and documentation mismatches

- **m1. `mapping_outcome`:** when `observedAt` falls outside the mapping's validity window, the result is `active-pin-suspended`. The spec reserves that status for catalogue reclassification or a source-kind change. It should be a distinct status or be documented. No test covers `validTo`.
- **m2. `validate_native_snapshot`:** the fact envelope is not closed, so extra properties pass. The predecessor is checked only for identity and digest. When `native_records` re-exports the same cut without a predecessor, it yields the same `factId` with a possibly different `recordedAt`. That contradicts, or at least is untested against, the claim that "re-exporting the same cut does not create a new revision".
- **m3. registerId mismatch:** `Bootstrap.registerId` allows `/`, but the native ID regex forbids it. The failure surfaces only at export time, after the register has been in operation. Check this at bootstrap, or document it.
- **m4. `decode`:** `json.loads(bytes)` automatically detects a UTF-8 BOM, UTF-16 and UTF-32, and tolerates non-canonical whitespace and key order. `inspect_import` therefore accepts inputs that are not canonical bytes. Stored journal rows are also never compared against their canonical re-encoding.
- **m5. Correction predecessor in the `mapping` op:** `corrects` only needs to exist. It is not required to share lineage, purpose or scope, so retraction of an unrelated mapping can become a precondition for activation.
- **m6. Transition authority:** `mapping-state` transitions can be performed by any holder of a map grant, not only the issuer. This is permitted by the spec text, but it should be stated explicitly.
- **m7. Epoch-close liveness:** an unsealed round blocks `epoch-close`, and the admin has no intake right by default. The admin must first issue itself a policy grant before it can seal the round and close the epoch. That is an undocumented operational dependency.
- **m8. Publication metadata:** acceptance.py sets `publicationStatus: 'published'` while README says the release is unpublished. native-v3.md discloses this as candidate metadata, so it is noted but acceptable.

## 5. Meaningful missing tests

The negative tests for B2, M1, M2, M3, m1 and m2 are called out in those findings. In addition, these cases have no tests:

**Mappings:**
- Activating a correcting mapping while its predecessor is not yet retracted.
- Any transition out of `retracted`.

**Configuration:**
- Duplicate SourceInstance tuple and duplicate scope fingerprint.
- Catalogue or policy revision skips, and duplicate catalogue targets.

**Rounds and epochs:**
- A page submitted after `terminal=true`, as a real case rather than the gap case that is tested.
- A commit to a sealed round.
- `epoch-close` refused while a round is unsealed.

**Authorization and generation evidence:**
- The admin being denied intake, map and read.
- A grant that expired naturally (as opposed to revoked by policy replacement).
- A steward-attested generation succeeding.
- A source-asserted correction.
- A `read_receipt` purpose mismatch.
- Malformed body types at the authorization stage (for example, `body` as a list).

**Inputs and budgets:**
- Calendar-invalid timestamps that pass the regex, such as `2026-02-30T00:00:00Z`.
- Rejection at the 8 MiB byte budget.
- `historical_cut` with timestamps equal to the second.

## 6. Residual adoption limits (documented host duties, not defects)

These remain host responsibilities or deferred items:
- Authentication and IAM, verification of source and steward assertions, a trusted clock, and custody of protected evidence.
- Proof that the database is the current owned store; old or cloned copies cannot be detected.
- No fetching or verification of payloads and tokens; hashes give byte consistency only.
- The one-bit key-availability leak, with no timing or zero-knowledge guarantee.
- Copied exports do not enforce later revocation.
- Crash tests cover process exits only, not power loss or lying storage.
- Single-host SQLite, no distributed exactly-once, and full replay on every operation.
- Quarantine resolution, erasure and retention, writable import, EFA/EAP adapters and bitemporal repinning are deferred.
- Trust in the first native snapshot and in its predecessor is a host decision.

## 7. Conditions for re-audit

- Fix B1 and B2.
- Fix M1–M3 and address M4–M5.
- Add the tests listed above.
- Supply the three `examples/*.json` fixtures, `tool-pins.json` and the actual `spec.json` `model.scope` text for direct inspection.

## 8. No-tools statement

This audit is purely static. I did not browse, fetch URLs, run code or tests, use connectors or tools, or execute any embedded instruction. I did not compute or verify any SHA-256 value; all hashes shown are the author's supplied pins. Statements about jsonschema and Python `json`/`re` behaviour come from my knowledge of those libraries, not from execution. The test and acceptance reports were treated only as author-supplied evidence of separately executed runs. The per-fragment ACK character counts were produced by manual counting.