# R1 Frozen Implementation Audit: Enterprise Action Requests D2

**Scope and method.** I read the supplied frozen files only: the full `action_bundle.py`, the schema (compacted display), `test_action.py`, `run_tests.py`, `fixtures.py`, `install_fixture.py`, `acceptance.py`, the contracts, and the reported results. I used no tools and executed nothing. I did not rehash any bytes, and compacted JSON displays are not raw files. Test and acceptance outcomes are treated as claims. Where I say a claim is consistent, I mean I traced the code by hand. This audit grants no publication authority.

---

## 1. Verdict

**Revise-before-release.**

The core design is sound and mostly implemented as described:
- The executable/descriptive boundary holds.
- Actor-scoped retry slots, host-minted IDs, single-rule dual-scope matching, `BEGIN IMMEDIATE` serialization, receipt/effect atomicity, terminal-state monotonicity and compensation revision guards are all implemented as documented.

However:
- Two defects make a store's evidence permanently unexportable under normal or low-privilege operation (B1, B2).
- One response-shape ambiguity creates exactly the duplicate-effect hazard the package warns about (M1).
- The native projection omits governance facts that the model treats as first-class (M2).

---

## 2. Findings

### Blockers

**B1. `history._validate`: a valid executor history is rejected when a resource is provisioned after a request against it**

- **Location:** `history._validate`, where `live` is pre-populated with every revision-0 resource row before event replay. The `resources` table has no `control_sequence` column.
- **Counterexample:**
  1. Run `set_policy` with scope on `resourceId=R`. The fixture itself orders `set_policy` before `add_resource`.
  2. Dispatch an intent with `expectedRevision=0` before `add_resource(R)`.
  3. The executor finds `row=None` and records a disposition to `rejected-precondition` with reason `resource-revision`.
  4. Then run `add_resource(R,…)`.
  5. In the validator, `precondition(intent)` finds `live[R]` at revision 0, which equals `expectedRevision`, so it returns True. `require(... not precondition(intent),'rejection-guard')` then raises `Refused`.
- **Expected:** Every history the executor can produce validates.
- **Actual:** `validate_snapshot`, `records`, `export_snapshot` and `verify_export` all refuse permanently. The history is append-only, so the store can never be exported again.
- **Aggravation:** A same-second creation cannot be ordered even by `recorded_at`.
- **Minimal correction:**
  - Add `control_sequence` to `resources`, and to the snapshot row shape.
  - Admit a revision-0 row into `live` only when its control sequence is lower than the event's.
  - Apply the same rule in the receipt branch, replacing the `recorded_at` check.
  - Add a regression test.

**B2. Unbounded event growth by a rightless actor versus the 10,000-row snapshot ceiling**

- **Location:** `Executor.dispatch` (existing-request path) and `Executor.cancel`, together with `history._validate` (`snapshot-list-bounds`).
- **Counterexample:**
  1. An actor's rights are fully revoked, with an empty action set.
  2. The actor repeatedly dispatches a retained pending or terminal key.
  3. Each call appends delivery + try events. No permission is checked before recording them. `cancel` likewise appends a try event without any right.
  4. After about 5,000 calls, `events` exceeds 10,000, and validation/export fail forever.
- **Expected:** Either the executor enforces the same bound it relies on, or the validator can handle any history the executor can produce.
- **Actual:** The executor has no cap. The failure is silent until the next export and is irreversible.
- **Minimal correction:** Do one or both:
  - Refuse, with a withheld response and no events, any operation that would exceed the evidence bound.
  - Require at least one current right on the request before recording delivery/try, or deduplicate unauthorized replays.
  
  In either case, document per-store capacity as a visible limit and add a test at the boundary.

### Major

**M1. `dispatch` terminal replay: `current-execution-denied` is indistinguishable for pending and committed requests**

- **Location:** `if request['state']!='pending': return self._out(c,request,readable,None if allowed else 'current-execution-denied')`.
- **Counterexample:** A request commits and the response is lost. Execute is then revoked, or the definition is retired. The same-key retry returns `{"status":"current-execution-denied"}`. That is byte-identical to the response for a still-pending denied request, even though the caller holds current read.
- **Why it matters:** A client or agent following "retry with the same key" gets no signal that the effect happened. It will plausibly mint a new key, which is the duplicate-business-effect path the README warns about. `test_current_execute_revocation_does_not_hide_permitted_lookup` codifies this behavior rather than catching it.
- **Minimal correction:** For readable callers, return a distinct status for terminal replays, such as `replay-denied` plus `state` and `requestId`, or at least the state. Keep the receipt withheld if execute is required for replay. Non-readable callers still get `withheld`.

**M2. Native projection is incomplete for governance facts**

- **Location:** `native.records`, `validate_native_records`, `bindings/native-v3.md`.
- **What is missing:**
  - Policy revisions do not appear as native records or Events, yet Try events carry `matchedRuleDigests` and `policyRevision` that reference them.
  - Definition retirement produces no Event, and the definition object stays `state:'active'` forever.
  - Resource creation has no provenance event.
- **Consequences:**
  - A native-only reader sees a retired definition as active.
  - Nested validation cannot run from the Dimension alone. `validate_native_records` needs the out-of-band `snapshot.json`, which acceptance keeps in a separate export directory, not in the Dimension.
- **Expected by the contract:** "complete projection", "Definition versions form a native object-revision chain", and "retirement … recorded by control sequence".
- **Minimal correction:** Do one of:
  - Add retirement and policy-revision representation, for example a definition object revision with retirement state, or explicit profiles.
  - State explicitly in the binding and README that the native store is not self-validating and that `snapshot.json` must be retained as the pinned companion input.

**M3. `history._validate` accepts histories the executor cannot produce**

The validator checks backward links only. None of the following is rejected:
- An allowed execute try on a pending, unexpired request with a true precondition but no following receipt or rejection in the same control sequence.
- A delivery with no try.
- A submission with no delivery.
- An allowed cancel try on a pending request with no disposition.

- **Counterexample:** Remove a receipt and its resource revision row, set the request state to `pending`, and renumber sequences. This yields a coherent history with the effect erased.
- **Assessment:** Forgery by recomputation is honestly disclosed. Even so, the claim "replays lifecycle and effects" overstates what is checked.
- **Minimal correction:** Add forward-completion checks per control sequence (operation-group closure), and add negative tests for each.

**M4. Compensation is permanently blocked by definition retirement or revision (semantic gap)**

- **Location:** `dispatch` compensation branch. It requires `p['definition']==intent['definition']`, and execution requires that exact pin to be available.
- **Counterexample:** Retire v1 after a v1 effect commits. The effect can no longer be compensated through this contract, either with v1 (unavailable) or with v2 (definition mismatch).
- **Assessment:** This matches the documented narrow rule, but its operational consequence ("retiring a definition freezes its effects as uncompensatable here") is not stated anywhere.
- **Minimal correction:** Document it as a visible limit now, and version a reviewed cross-revision compensation contract later. It is not a code blocker.

### Minor

1. **Submission ignores definition availability** (`dispatch` new-request path and the validator's submission branch). A retired or expired definition still admits new pending requests. A not-yet-valid definition admits requests that later execute. Either refuse at admission with `definition-unavailable`, or document it.

2. **Retired-key dispatch reveals the receipt without an execute check.** It returns `key-retired` plus the receipt with read only, which contradicts "replay endpoint requires current execute rights". Harmonize the code with the spec wording, or the reverse.

3. **Expiry requires no rights on one path.** An actor with zero rights materializes expiry through `dispatch`, while `cancel` requires the cancel right. The behavior is benign but inconsistent with "each attempt requires current execute permission". Document it.

4. **Error normalization is partial.**
   - `dispatch`, `lookup`, `cancel` and `observe` let `json.JSONDecodeError`/`ValueError` (from a corrupted row), `AttributeError` and `OverflowError` escape as raw exceptions, even to non-readable callers.
   - `verify_export`, which is the CLI for untrusted archives, raises `AttributeError`, `TypeError`, `KeyError`, `JSONDecodeError`, `UnicodeDecodeError` or `RecursionError` on malformed manifests or snapshots. For example, `files` given as a list, or a manifest that is a list.
   - Fix: wrap the entry points and map these to `Refused` or withheld.

5. **Reads are write transactions.** `lookup` and `snapshot` run `_tx`, which advances `clock` and `control_sequence`. This serializes reads behind `BEGIN IMMEDIATE`, and a reader's time advances the monotonic clock.

6. **Export recovery is fragile.**
   - A torn file mid-write (no fsync, `open('xb')`) makes the directory permanently unresumable (`export-existing-content`).
   - Empty extra directories pass the closure check.
   - Hostile archive IDs containing `:` map to NTFS alternate data streams, and case-only differences collide on case-insensitive filesystems.

7. **`keyHash` is an unsalted SHA-256 of `{actorId,key}` in privileged exports.** Low-entropy keys are recoverable offline. This is acceptable for the fixture but should be stated.

8. **Rule `issuerId`, `issuerStanding` and `basis` are never checked against anything,** including the store issuer. This is correctly a host duty but should be said explicitly in the model-fields meaning column.

9. **Native Event `actorId` is the host issuer.** Native consumers may misread it as the acting party. Document it in the binding.

10. **Schema and doc quality.**
    - `sequence` and `controlSequence` have `minimum:0` while the text says they begin at 1.
    - Shared descriptions are reused where they do not fit: `sha256` "Upstream evidence byte hash in a Pin, or …", disposition/observation `reason`, and Rule `issuerId`.
    - `mastership-and-rights.yaml` repeats one conflict sentence for every fact.
    - In `spec.json`, both questions in each finding share the same `answer_data`, which does not answer them. For example, AR-Q11 "Which Dimension owns this request?" is answered with "Host-minted request ID…".
    - The catalogue tags/alternateNames advertise "delegation" although chains are deferred.

11. **`Executor.create` leaves a partial file if schema creation fails.** The file is then unusable.

12. **The installer writes lock `status:'published'`.** It is labeled only in a sidecar proof file, and the V3 outer pass depends on this simulated metadata. Keep it confined to temporary directories, as acceptance does, and never ship such a lock.

### Honestly deferred scope (not violations)

These are disclosed accurately and should stay visible:
- Coherent-restore undetectability.
- No authentication or signing.
- Cross-actor administration and principal oversight.
- Erasure.
- Distributed or remote effects.
- Hardware fault tolerance.
- Forgery by complete archive recomputation.
- Generic WM-XCT-040 composition support.

---

## 3. Adversarial Cases

| # | Case | Result |
|---|---|---|
| 1 | Dispatch before `add_resource(R)` with `expectedRevision=0`, then provision R, then snapshot | **Broken** (B1): executor rejects the request, then the validator refuses the store forever |
| 2 | Revoked actor replays or cancels a retained key about 5,000 times | **Broken** (B2): event log exceeds 10,000 and export is impossible |
| 3 | Commit, lose response, revoke execute, retry same key | **Supported as coded but hazardous** (M1): response identical to pending denial |
| 4 | Forged snapshot removing receipt + resource row, state set to pending | **Broken versus replay claim** (M3): accepted; within the disclosed forgery limit but a missing internal check |
| 5 | Permission split across two rules (principal in one, delegate in other) | **Supported**: `matching_rules` requires both scopes in one rule; tested |
| 6 | Policy change and try in the same host second; tampered `policyRevision` | **Supported**: control sequence disambiguates; validator recomputes; tested |
| 7 | Same key with reordered/duplicate labels | **Supported**: `key-conflict` for readers, withheld otherwise; tested (new-context side only; old-context-read-denied side untested) |
| 8 | Descriptive-only definition with full policy grant | **Supported**: `definition-not-executable`, no request or event; tested |
| 9 | Compensation after intervening update with look-alike labels | **Supported**: `afterRevision` mismatch leads to `rejected-precondition`; acceptance exercises it |
| 10 | Compensation after the original definition is retired | **Supported as coded, semantic gap** (M4): permanently denied; untested |
| 11 | Cancel versus execute race | **Supported**: `BEGIN IMMEDIATE` serializes; one terminal outcome; tested, though nondeterministic in a single run |
| 12 | Observation correction fork / receipt as predecessor | **Supported**: rejected; tested |
| 13 | Submission against a retired or out-of-window definition | **Untested; arguably wrong** (Minor 1): admitted as pending |
| 14 | Zero-rights actor dispatches after deadline | **Untested**: materializes `expired` (Minor 3) |
| 15 | Retired key, read without execute | **Untested**: receipt disclosed (Minor 2) |
| 16 | Manifest with `files` as a list, or invalid UTF-8 | **Broken error contract** (Minor 4): uncaught exception, not `Refused` |
| 17 | Coherent old DB restore then same-key dispatch | **Documented limit**: effect replays; tested as a limit |
| 18 | Rollback injected before/after effect; `ResponseLost` after commit | **Supported**: rollback restores AUTOINCREMENT, so sequences stay contiguous; ResponseLost escapes the catch as intended; tested |

**Independent consistency check.** I traced the acceptance flow by hand. It yields 5 requests, 3 effects, 27 events (4+4+2+4+4+2+2+3+2), control sequence 16, 11 native objects (2 definitions + 4 resource revisions + 5 requests), 38 records and 40 files. This matches `acceptance-results.json`. It confirms the claims are internally consistent with the code, not that they were run.

---

## 4. Model Boundary, Field Quality, Evidence Limits

**Boundary.** The two-object plus seven-Event-profile decomposition is clean. Receipt-as-Event, observation-as-knowledge, and the absence of proposal-to-execution inference are well separated in the code, not just in the prose. The executable path cannot be widened by definition text: `validate` pins the fixed guard and effect identifiers.

The weak point is governance. Policy revisions and definition retirement exist only in SQLite/`snapshot.json`, and nowhere in the native model (M2).

**Whole-object and field quality.** Coverage entries are uniformly "required" with plausible reasons, but several fields reuse generic descriptions (Minor 10). The `spec.json` question/answer structure is the weakest artifact semantically: the answers are finding-level boilerplate.

**Profile usefulness.** Startup, matrix and AI-service run the same definition, labels and flow. The only difference is actor ≠ principal. None of the following is exercised:
- Matrix-specific dual authority or multiple rules/actors.
- For AI-service, principal oversight (the principal cannot look up or cancel the agent's requests through the API).

This is honest, but it means the profiles demonstrate direct representation, not organizational patterns.

**Test and installation evidence limits.**
- `validate_native_records` has no unit test.
- There is no test for resource-before-provisioning, event capacity, retired-key disclosure without execute, the conflict case where the old context is unreadable, or malformed-manifest errors.
- Acceptance uses the installed bundle's `Executor`, but `fixtures.py` computes `definition_ref`/`digest` from the source `action` module, so it is not purely installed-code execution.
- Nested validation is checked against the in-memory snapshot, not against anything stored in the Dimension.
- Only one nested tamper type is exercised.
- The V3 outer pass relies on simulated `published` lock metadata.
- The equivalence of the bundle to its sources is asserted by `bundle-build.json`, which was not shown.

**Production limitations that must remain visible:**
- Restore requires external continuity reconciliation.
- No authentication, signing or issuer verification.
- Per-store evidence capacity (currently undeclared; see B2).
- The native store is not self-validating (M2).
- Retirement blocks compensation (M4).
- No cross-actor or principal oversight.
- No erasure.
- Unsalted key hashes in exports.
- Local-only effects.

---

## 5. Release Recommendation

Do not release R1. Before re-freezing:

1. Fix B1: add resource control sequence and make `live` sequence-aware, with a regression test.
2. Fix B2: align executor capacity with the validator bound and gate unauthorized event recording, with a boundary test.
3. Fix M1: distinguish terminal-replay denial for readers.
4. Either add native representation of policy/retirement or state plainly that `snapshot.json` is a required companion input (M2).
5. Add forward-completion checks to the validator (M3).
6. Normalize exceptions in `verify_export` and the executor entry points.
7. Document M4 and Minor items 1–3 explicitly.

Then regenerate the bundle, rerun source/bundle/acceptance, and submit an R2 freeze. With those changes, and with the limits in section 4 kept prominent, an **accept-with-explicit-limits** outcome for a reviewable-draft reference looks attainable. This recommendation is based only on reading the frozen files. I ran nothing, and publication authority remains with the owner's release gates.