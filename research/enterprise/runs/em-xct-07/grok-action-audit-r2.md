**Tools used:** team chatroom coordination only (Harper, Benjamin, Lucas). No test execution, no code execution, no browsing, no hash recomputation from displayed bytes, no publishing authority. Reports in the packet were inspected as assertions, not rerun.

---

## 1. Method and verdict

**Method.** Independent frozen static read of the supplied R2 packet. Implementation reasoning is limited to displayed `action.py`/`history.py`/`native.py` fragments, `build_schema.py`, `action.schema.json`, tests, fixtures, install/acceptance scripts, and `spec.json`. `action_bundle.py` is truncated mid-`Executor._slot` (~24.5k characters omitted), so `dispatch` / `lookup` / `cancel` / `observe` / `retire_key` / `snapshot` and the start of `validate_snapshot` are **not** independently source-visible. JSON is compacted for display; raw-byte hashes were not verified.

**Verdict: accept-with-explicit-limits.**

Not reject. Not revise-before-release. Not a production execution service. Not a publication grant. Descriptive-only adoption is the profile that is actually reviewable as a metamodel today. The synthetic executor is a bounded reference binding whose public-contract R1 fixes are test-witnessed; they are not fully source-verified in this packet.

---

## 2. Remaining issues

### Blockers
None confirmed from displayed text. No demonstrated R1 regression that still lets a public caller rewrite history, exceed the 10k commit cap, grow events with zero rights, leak a non-withheld disclosure shape, publish a non-candidate lock, or treat native export as a second master.

### Major (not honest deferrals)

**M1. Packet truncation prevents source verification of the R1-fix surface.**  
Exact gap: `action_bundle.py` after `_slot`. Expected for an implementation audit: complete `dispatch`/`lookup`/`cancel`/`observe`/`snapshot` and `validate_snapshot` prologue. Actual: those functions exist only as tests + spec. Minimal correction: freeze an untruncated companion in the next audit packet. This is an audit-evidence defect, not a demonstrated runtime break.

**M2. Capacity fixtures are raw SQL, not Executor-built 10k histories.**  
`test_action.py` `test_resource_capacity_rolls_back_whole_new_request_and_effect`, `test_policy_capacity_reserves_final_global_revocation`, `test_event_capacity_blocks_new_effect_but_allows_read`. Expected if claiming “seeded as valid retained histories”: rows produced by public/`Executor` operations and then replayed. Actual: `executemany` inserts; event-capacity copies the original successful delivery+try pair onto later `controlSequence`s. That pair is a **legal terminal-replay shape** (delivery + current-policy try, no second receipt), so it is not the R1 incomplete-first-effect hole. It still does not prove a semantically rich 10k history. Minimal correction: one Executor-built cap test per table, or label these tests COUNT+rollback only.

**M3. Specified readable-denied field set is only partly asserted.**  
Spec: readable denied dispatch reports `current-execution-denied` plus `requestState`, `requestId`, `intentDigest`, and any prior receipt.  
`test_current_execute_revocation_does_not_hide_permitted_lookup` asserts status.  
`test_reader_sees_terminal_state_on_denied_replay` asserts `requestState` / `requestId` / `receipt`.  
`intentDigest` is not asserted. Pending-denial body fields are also unasserted. Minimal correction: assert the full specified object.

### Minor (test/spec hygiene, not release-blocking)

- No dedicated 10k tests for `definitions` or `requests`.
- Spec: passive lookup after `expiresAt` remains `pending`. No test. If lookup materializes expiry, that would be a contract break; unseen.
- Spec: admission may precede availability (already retired / outside `validFrom`–`validUntil`). Tests retire or expire **after** a pending exists. Admit-against-already-retired is unseen.
- Denied cancel with read-but-no-cancel should retain a try; denied observe retains no event. Only the zero-rights (no try) side is tested.
- Observe on a retired key must withhold. Untested with read+observe.
- Compensation after definition `validUntil` (not just retirement) untested.
- `purpose ∈ definition.purposes` is required by the admission sentence; cannot confirm in truncated `dispatch`. Scope-mismatch tests change purpose without updating policy, so they do not isolate this check.
- Visible `validate_snapshot` observation arm: `matching_rules(..., 'read')` and `observerId == intent['actorId']`. Observe rights may be inside `trial_for(e, 'observe')`. Binding is actor/key scoped; spec’s “another independent observation can coexist” cannot be exercised through this API. List as a binding limit.
- Visible expiry arm: `trial_for(e, action, allowed=(action=='cancel'))`. Execute-at-deadline therefore implies `allowed=False` if that flag is stored-decision equality. `test_expiry_no_first_effect_at_boundary` plus claimed `validate_snapshot` pass is the only witness. Semantic smell, not a demonstrated break.
- Idempotent `add_definition` of identical bytes after retirement is a no-op on `available` (cannot reactivate) but still consumes a control sequence. Untested.
- `_fault` / `_fail_after` hooks ship in the companion. Privileged-host only; keep them out of any production wrapper.

### Honest scope deferrals (do not treat as defects)

No command/network effects; no distributed exactly-once; no automatic restore reconciliation; no mandate registry; no legal conformance; no WM-XCT-040 composition acceptance (empty `paths` still rejected by the published composer); no hardware-fault tests; unsalted retry hash is not secrecy; execute-without-read **does** mutate the resource and always returns `withheld` (in-contract; host must isolate the store); coherent older same-epoch SQLite is accepted (`test_coherent_restore_is_explicitly_not_detectable`); native object `state=active` is existence, not availability; retirement/policy live in the companion snapshot, not in native facets; fixtures are self/direct-representation sketches, not org or AI governance.

---

## 3. Adversarial cases (static outcomes) and omissions

1. **Zero-rights flood after commit.** Dispatch/cancel/observe ×3 with empty policy. Expected: `withheld`, no growth of definitions/policies/resources/requests/events. Actual (test-asserted): tables unchanged. Control sequence may still advance. **In-contract pass.**

2. **Later-created resource vs old rejection.** Missing resource → `rejected-precondition`; then `add_resource` at offset 0 and 1; old request stays rejected; new key can commit. Expected: historical rejection not rewritten. **R1 fix, pass.** Same-second offset=0 still `validate_snapshot`-passes, so replay cannot be “load every rev-0 up front.”

3. **Readable committed denial vs pending denial vs zero-rights.** After commit, execute revoked / read kept: `current-execution-denied` plus retained state/id/receipt. Then all rights removed: `withheld`. Pending denial remains retryable once execute returns. **Pass**, with M3 field-set gap.

4. **Execute without read.** `['submit','execute']` only. Expected: resource changes, every public response `withheld`, lookup `withheld`, effects=1. **In-contract pass. Named limit:** confidentiality of the response is not prevention of the effect.

5. **Torn export vs changed cut.** Partial write or torn record: same-directory retry refuses and leaves torn bytes; identical snapshot can resume only intact files; changed cut needs a fresh directory. **R2 claim holds on displayed `native.py`.**

6. **Coherent older same-epoch store.** Copy DB before commit; open copy with the same epoch; dispatch “succeeds” again. Expected by spec: internal checks cannot see this. **Documented host-continuity hole, not a safety success.**

7. **Nested native tamper.** Stored receipt `afterLabels` forged after install. Expected: outer Dimension validate still passes; `validate_native_records` raises `native-record-projection`; duplicate native append refused. **Acceptance-asserted. Platform split, not a companion hole.**

8. **Retired same-pin compensation.** Commit, retire definition, new key restoring before-labels. Expected: `current-execution-denied`, effects stay 1. **By-design pass.** (Validity-window expiry of the same pin is untested.)

9. **Split-rule scopes.** Rule A grants principal execute / delegate submit+read; rule B the reverse. Expected: no combined intersection, no effect. **Pass.**

10. **Malformed wire / corrupt row / malformed archive.** Duplicate keys, floats, bool-as-int, surrogates, NaN, `{bad`, corrupt `requests.body`, bad manifests, extra directory. Expected: public `withheld` or admin `Refused('export-malformed')`, no escaped diagnostics. **Pass on displayed wrappers.**

11. **Event-capacity copied delivery+try.** Raw pairs after an existing commit, then `snapshot()`/`validate_snapshot`. Expected if grouping is state-aware: accepted as replays, new effect withheld, lookup of original still works. **Not an incomplete first-effect tail.** Weak as a 10k semantic-history proof (see M2).

**Important omissions:** lookup-after-deadline still pending; admit against already-retired or out-of-window definition; denied-cancel try retention for a reader; observe-on-retired-key; compensation after `validUntil`; second independent observer (cannot be addressed through actor-scoped keys); Executor-built definitions/requests cap; `intentDigest` on readable denial; `purpose ∈ definition.purposes` isolation; cancel-at/after-deadline; admin+event sharing one control sequence in a **forged** snapshot.

---

## 4. Semantic boundary, coverage, navigation, installation

**Boundary.** Spec purpose matches the binding: describe governed actions, keep immutable intent, validate a bounded local history, and **do not** derive permission from descriptions. Two objects (`ActionDefinition`, `ActionRequest`) and seven Event profiles. Only executable action is ordered-label replacement in one synthetic SQLite resource. Descriptive-only definitions are cataloguable and non-invocable (`definition-not-executable`, no request row). Host duties stay outside the code: authentication, issuer standing, monotonic time, store/export isolation, external continuity. Native export is evidence, not a second master.

**Per-field / whole-object.** Nine canonical types and ten supporting values each have the five required facets in `spec.json`. Policy/Intent/DefinitionRef/Decision/ExportManifest are values, not extra subjects. Schema and `validate()` tighten executable vs descriptive pairs. Byte contract is explicit Python encoding, **not** RFC 8785 JCS.

**Bundle → Layer → Finding → Question.** 5 / 5 / 26 / 52 / 26. Q01–Q52 each have a distinct `requiredEvidence` + `derivation` + `ifMissing` contract. Useful as host-guidance navigation. It is not an executor and must not be read as one.

**Installation evidence.** Inspected as assertions: 63/63 source and 63/63 bundle reports; three new synthetic Dimensions (startup self, matrix/ai-service direct-representation); lock `candidate` + `simulationOnly: true`; companion `snapshot.json` + `manifest.json` stored under `data/action-exports/cut-<controlSequence>/` and read back; nested tamper rejected after outer pass; duplicate native event refused; route is pinned native creator/validator, **not** WM-XCT-040. Empty runtime `paths` is intentional and documented. No production publication is implied.

---

## 5. Release recommendation

**Release as a reviewable-draft English Vercy metamodel and bounded synthetic reference, with the limits above written into the adoption surface.**

Shipable now, under those limits:
- descriptive-only ActionDefinition catalog and the 52-question navigation;
- candidate / `simulationOnly` companion install into a **new** synthetic Dimension;
- local ordered-label executor as a fixture, not as enterprise workflow.

Do not ship as:
- a production authority service,
- a published WM-XCT-040 composition,
- a restore/continuity product,
- an org- or AI-governance implementation.

R1’s eight concrete defects are addressed at the **public-contract and test-witness** level (resource order, 10k whole-tx caps with reserved empty revocation row, zero-rights no event growth, operation-closure tests, readable denied terminal state, snapshot+manifest inside the Dimension, hashed filenames, normalized malformed errors, candidate lock, torn export → fresh directory). They are **not** fully source-verified in this truncated packet.

A reviewer cannot waive the owner’s process or authorize release. Remaining owner gates stay exactly those in `review.json`: live publication verification, current acceptance on the owner’s pinned toolchain, and an untruncated implementation freeze if a later audit is expected to certify the executable profile rather than the metamodel.