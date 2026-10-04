Harper’s lane is already covered in the source reading. The three completed reviews agree. Writing the team audit now.

---

# Independent frozen implementation audit — Enterprise Action Requests D2 / R1

Review basis: the frozen packet as supplied (README, model-spec, model-fields, invariants, schema display, tests, fixtures, installer, acceptance script, claimed result JSONs, and the generated `action_bundle.py` recovered in full from the packet). JSON files in the packet are compacted for display; this review does not rehash those displays as if they were the pinned raw bytes. Test-result and acceptance-result JSON files are treated as **claims to inspect**, not as proof this review executed the suite. No publication authority is granted.

## 1. Verdict

**accept-with-explicit-limits**

No blocker was found that makes a descriptive-only definition execute, accepts arbitrary commands/SQL/URLs, reapplies a committed effect on a live coherent store, unions split policy rules, or treats a native outer V3 pass as nested semantic proof. The two-object / seven-event English model plus the closed synthetic adapter is internally coherent as a **reviewable-draft reference**. It is not a production executor, not an authenticity oracle, and not evidence of publication.

The limits below must remain on the adoption banner. They are not residual nits.

## 2. Findings

### Blockers

None. Core invariants 1–15 and 17–19 are implemented in the bundle with matching history checks. Missing host authentication, issuer-standing verification, legal mandate validation, and external continuity are **declared fixture assumptions**, not broken implementation promises.

### Major limits (must stay visible; not silent defects)

**L1. Coherent restore cannot be detected; dispatch after restore can commit again.**  
Files: `Executor.__init__` / `_tx` (`store-epoch` only), `test_coherent_restore_is_explicitly_not_detectable`.  
Counterexample: copy the SQLite file before a commit; reopen the copy with the same epoch; `validate_snapshot` accepts zero effects; `dispatch` of the same intent/key can take a first effect that a newer copy already committed.  
Expected (production): stop and reconcile to an external latest-history anchor.  
Actual: epoch+hashes accept any internally coherent generation of that store.  
Minimal correction: keep the README/AGENTS stop-the-line rule as a **release condition**, not a footnote. Do not add a local “restore safe” claim. This is specified and tested as a limit.

**L2. Installation writes `vercy.lock` `status: "published"` while the proof flag is only in a sidecar.**  
Files: `install_fixture.install` (lock `status: 'published'`), `acceptance.py`, `bindings/native-v3.md`.  
Counterexample: an operator copies `vercy.lock` without `action-fixture-installation.json`. The lock object itself has no `simulatedPublicationMetadataOnly` field.  
Expected: test lock metadata cannot be mistaken for a production publication decision (`review.json` still says `publicationDecision: not-yet-made`).  
Actual: the written lock says `published`.  
Minimal correction: write `status: "candidate"` (or equivalent) in the lock; keep the simulated flag on the lock object, not only in the sidecar.

**L3. Native files are not a complete authorization or retirement projection.**  
Files: `native.records`, `validate_native_records`, `history.validate_snapshot`.  
Counterexample: policy bodies, `available` / `retired_sequence`, and request `state` / `receiptId` / `keyRetired` are absent from native object facets. `validate_native_records` rebuilds expected records from the **sidecar snapshot**, then demands exact dict equality. A Dimension that only retained native files cannot replay scope decisions.  
Expected per some “complete projection” phrasing: native records carry the governed meaning.  
Actual: native export is deterministic evidence of objects+events at a cut; authorization replay lives in the snapshot/history validator.  
Minimal correction: keep “evidence, not master” and drop any “complete projection” wording that implies policy/retirement live in the native files.

**L4. Outer native V3 does not validate nested action meaning.**  
Files: `acceptance.py` (stored `afterLabels` tamper), `validate_native_records`, `bindings/native-v3.md`.  
Counterexample constructed by the acceptance script: mutate `payload.enterpriseActionEvent.payload.afterLabels` on a stored receipt; generic outer validate is required to remain valid; companion `validate_native_records` must raise `native-record-projection`.  
Expected: nested companion validation is mandatory after any outer pass.  
Actual: that split is the design; the outer pass is envelope structure only.  
Minimal correction: never cite outer V3 as implementation acceptance of ActionDefinition/ActionRequest semantics. Treat the acceptance JSON as a claim.

### Minor findings (real; not draft-gating if L1–L4 stay visible)

**m1. Spec/README tighter than dispatch on expiry.**  
File: `Executor.dispatch`. README: “each attempt requires current execute permission.”  
Counterexample: pending request, execute revoked, `now >= expiresAt`. Code takes the expiry branch **before** the `elif not allowed` return, writes `disposition` `expired`/`deadline`, and (if readable) returns `expired`.  
Expected if the README is literal: `current-execution-denied` and still pending.  
Actual: time guard wins; history accepts an execute-try expiry with `allowed=False`.  
Minimal correction: qualify the sentence — execute permission is required to **commit**; expiry may be materialized on a dispatch try without current execute. This is a documentation fix, not an effect leak.

**m2. `lookup` and `snapshot` are not read-only.**  
File: `Executor._tx` used by `lookup` and `snapshot`.  
Every call increments `meta.control_sequence` and persists `clock`. Two `snapshot()` calls at the same `now` are different cuts; that is why `test_export_changed_snapshot_does_not_overwrite` refuses the second export without a business mutation.  
Spec prose says the control sequence “orders policy changes/retirement with tries.” Implementation uses it as a global transaction serial including reads. History allows gaps.  
Minimal correction: document snapshot/lookup as cut-allocating; optionally add a true read-only snapshot path that does not UPDATE meta.

**m3. Observe after key retirement is withheld, not `key-retired`.**  
File: `Executor.observe` (`if not readable or not matches or r['keyRetired']: return dict(WITHHELD)`).  
Lookup/dispatch/cancel with read return `status: key-retired`. Observe with read+observe returns `{status: withheld}`. Untested.  
Minimal correction: return the same `key-retired` shape when readable, or document observe as closed after retirement.

**m4. Denied cancel records a try; denied observe does not.**  
Files: `Executor.cancel` vs `Executor.observe`.  
Asymmetry is unspecified. Not an invariant break.

**m5. Unknown definition pin and descriptive-only share `definition-not-executable`.**  
File: `Executor.dispatch` (`if not definition or definition['mode']!='synthetic-executable'`).  
No request row is created. Fine for withholding; coarse for a readable steward cataloging error.

**m6. History does not enforce definitionId ↔ resourceId collision.**  
Files: `history._validate` vs `Executor.add_definition` / `add_resource` and `native.records`.  
A fabricated snapshot could contain both; `records()` would then refuse. Executor-produced snapshots cannot. Align the history field set if fabricated archives are in scope.

**m7. Dead schema allowances.**  
- Disposition `tryEventId` may be null; executor always supplies an id; history requires the try.  
- Schema `anyOf` allows mode/adapter/parameterContract combinations that only `validate()` rejects. Defense in depth, not a hole.  
- Label items have no `minLength`; empty-string labels are executable.  
- `matchedRuleDigests` `maxItems: 128` vs policy `maxItems: 128` is aligned; `_bounded` still allows 256-member objects elsewhere. Pathological overflow would fail Event schema inside the transaction → WITHHELD + rollback.

**m8. Application wire bounder allows `bool`; integer-never-bool is left to jsonschema.**  
File: `_bounded` (`None` or `bool` return early). Spec: integers must never be bools. Tests claim `"expectedRevision": true` is withheld. That gate is the schema type checker, not application-layer `type(x) is int`. Keep the test; add an application check if defense in depth is required.

Honestly deferred (not listed as violations): delegation chains, impersonation, use counters, remote effects, third-party receipts, legal mandate verification, production credentials, erasure, per-field disclosure, hardware power failure, constant-time withheld, WM-XCT-040 generic composition, external continuity service, force-cancel of a committed effect.

## 3. Adversarial cases

Independently reasoned from the bundle. “Supported” means the code implements the outcome. “Tested” means a named unit or acceptance path exists in the packet. This review did not run them.

| # | Case | Outcome from the code | Status |
|---|---|---|---|
| 1 | Descriptive-only definition, scopes rewritten to its pin, dispatch | `definition-not-executable` if readable; **no** request/delivery row | Supported, tested |
| 2 | Execute without read (`submit`+`execute` only) | Resource revision commits; every caller response is `{status: withheld}`; later read can see the receipt | Supported, tested |
| 3 | Same retry key, labels reordered / duplicate order changed | `key-conflict` (if read on both contexts); original receipt kept | Supported, tested |
| 4 | Same retry key, whitespace and property-order only | Canonical digest matches; replay, no second effect | Supported, tested |
| 5 | Split grant: principal execute on rule A, delegate execute on rule B | No single-rule intersection; execute denied; no effect | Supported, tested |
| 6 | Compensation after an intervening update, even if labels happen to match | `rejected-precondition` / `compensation-precondition`; original receipt untouched | Supported, tested |
| 7 | Observation correction whose predecessor is the receipt, or a second correction of the same observation | WITHHELD; receipts and labels unchanged | Supported, tested |
| 8 | File-copy restore of a coherent older DB, same epoch, same key | Local dispatch can commit a first effect that a newer copy already has | Specified limit, tested as a limit; **broken as production safety** |
| 9 | Nested `afterLabels` tamper in a stored native receipt, snapshot unchanged | `validate_native_records` → `native-record-projection`; outer V3 claimed to still pass | Companion path supported by code; outer pass is an acceptance claim |
| 10 | Dispatch at `expiresAt` with execute revoked | Request becomes `expired`, not left pending and not `current-execution-denied` | Supported by code; spec-tension vs README; **untested** with execute revoked |
| 11 | Lookup after `expiresAt` with no dispatch/cancel | Still `pending` if readable; must not be read as permission to execute | Specified; **untested** |
| 12 | Actor B presents actor A’s retry-key string | Slot hash includes `actorId`; appears absent / WITHHELD | Supported; explicit cross-actor test **untested** |
| 13 | Complete forged export: internally consistent snapshot + records + manifest | `verify_export` accepts; no authenticity or latest-head check | Documented limit; forgery path **untested** |
| 14 | Observe after `retire_key` with current read+observe | WITHHELD, not `key-retired` / `recorded` | Code behavior; **untested** |

Additional supported guards (not numbered above): actor spoof and foreign `dimensionId` withheld with no row; same definition id/version different bytes refused; executable free-text cannot change the fixed adapter tokens; definition/resource id collision refused at admin APIs; pending key cannot be retired; concurrent duplicate dispatches serialize on `BEGIN IMMEDIATE` to one effect (claimed by unit test).

## 4. Model boundary, field quality, tests, installation evidence, production limits

**Model boundary.** ActionContract is split into immutable ActionDefinition + host-minted ActionRequest; result is Receipt Event plus separate Observation. Policy is a host fixture list, not a mandate registry. Synthetic ordered-label resource, policy snapshot, export manifest, and SQLite tables are correctly labeled as not-new metamodels. WM-XCT-001/002/029 and K1/K2 are conceptual comparisons without runtime inheritance. That boundary is held in code: no path fetches a Pin URI, interprets descriptive text, or dispatches anything except `local-sqlite-ordered-labels/1`.

**Whole-object / field quality.** Closed objects (`additionalProperties: false`) for definition, intent, snapshot, rule, scope, pin, and each event kind. Required nullable fields (`compensatesReceiptId`, `receiptId`, `legacyCrosswalk`, `correctsEventId`) preserve absent vs invented. Labels are ordered arrays; duplicates are meaningful; Unicode is not normalized. Request id is minted outside the client digest. Canonical bytes are Python `sort_keys` + compact UTF-8, explicitly not JCS. Seven event profiles match schema, writer, and history. Native request facet exports only identity/intent/admission; derived state is reconstructed from events. Field quality is high for a 0.1.0 draft.

Gaps: native envelope `actorId` is the host issuer, not the request actor or observer (those remain inside `enterpriseActionEvent`). `tryEventId` is not a native subject. Control sequence is a global serial, not only policy/try/retirement. Those are mapping/doc issues, not missing fields.

**Semantic usefulness of profiles.**  
- *Startup* (self, actor = principal): this is the real unit-test surface and a usable descriptive+synthetic demo.  
- *Matrix* and *ai-service*: the same direct-representation fixture with different names. `test_three_distinct_profiles` only checks `actorId != principalId` and one commit. There is no AI subjecthood, tool-call, model-output, or multi-agent delegation model. “AI-service” is a naming profile. Useful as “a non-human actor ID under direct-representation with no further delegation,” nothing more.

Minimum useful adoption stated in README — one descriptive definition, one steward, one parameter-document pin — is actually implemented and is the honest enterprise use. Executable adoption is a local fixture.

**Tests and installation-evidence limits.** Claimed 50/50 source and 50/50 bundle, plus three synthetic Dimensions (2 definitions, 5 requests, 27 events, 3 effects each). Those counts are internally consistent with `acceptance.py`’s scripted path; they remain claims. Unit tests do not call `validate_native_records` (that path lives in acceptance). No unit test covers lookup-after-deadline, expiry-with-execute-revoked, observe-after-retire, missing resource (as opposed to stale revision), compensation-of-compensation, or cross-actor key strings. Hardware power failure is explicitly out of suite. `review.json` still says frozen implementation audit “not started”; this packet is the audit input, not a completed publication record.

Review-set limit: several manifest-pinned files (`adoption-limits.md`, `lifecycle/transitions.md`, standalone `action.py`/`history.py`/`native.py`, `build_schema.py`, `tool-pins.json`, S1 notes) are not in the supplied body. Limits in README/model-spec were used instead. Compacted JSON displays were not treated as raw pinned bytes.

**Production limitations that must remain visible**

- Trusted fixture inputs: authenticated actor, host time, issuer standing, policy basis, file isolation. No login, signing, IdP, or network server.  
- Only effect: replace an ordered label list in the same SQLite transaction that stores the request and receipt. No remote, financial, HR, or shell effect.  
- Not exactly-once distributed execution. SQLite/OS durability is assumed; process rollback is tested; disk/power failure is not.  
- After any restore or uncertain continuity: **stop dispatch** and reconcile externally. Epoch does not detect a coherent old generation.  
- A new retry key is a new intent. Automatic key replacement after a lost response can duplicate a business effect.  
- Native export and `verify_export` prove internal closure at a cut, not authenticity, authority, completeness against the world, or latest head. A hostile complete archive can be coherent.  
- Outer native schemas do not validate nested action meaning.  
- No erasure: retired keys retain full intent and receipt.  
- No delegation chains, quotas, impersonation, third-party receipts, or force-undo of a committed effect.  
- Simulated lock `published` is test setup, not a release. WM-XCT-040 composition acceptance is explicitly open.  
- `lookup`/`snapshot` allocate control sequence and take write locks.

## 5. Release recommendation

Ship this as a **reviewable-draft 0.1.0 candidate with the limits above printed on the first page**, not as a production action authority and not as a published Vercy composition.

Do not treat this audit as permission to publish. `review.json` holds remain in force until a separate publication decision, live HTTP verification, and a lock that does not say `published` unless it is actually published.

Practical bar for an eventual 0.1.0 tag:

1. Keep L1 (restore), L3 (native ≠ master), and L4 (outer ≠ nested) in README/AGENTS/adoption text without softening.  
2. Fix L2 so fixture locks cannot be copied as `published`.  
3. Apply the one-line spec clarification in m1.  
4. Leave descriptive-only cataloguing as the supported enterprise path; keep the synthetic adapter named as a fixture.  
5. Do not claim matrix/ai-service as distinct AI or matrix-organization semantics.

If those limits stay visible, the package is usable as an English metamodel plus a closed local reference. If any later edit narrows the restore warning, implies outer V3 proves action semantics, or treats the simulated lock as release evidence, the verdict should drop to **revise-before-release**.