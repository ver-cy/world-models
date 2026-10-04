# Independent static audit: Enterprise Action Requests R2

**Tools used:** None. I made no tool, browsing, code-execution, subagent or prior-conversation calls. I read the supplied packet statically. I did not run the 63 tests or the acceptance script, did not recompute any hash, and grant no publishing authority.

## 1. Method and verdict

**Method.** I read the full text of `spec.json`, `action_bundle.py` (action/history/native), `build_schema.py`, the generated schema, the fixtures, tests, installer, acceptance script and result reports. I traced each public path (`dispatch`, `lookup`, `cancel`, `observe`, the admin methods) against `validate_snapshot`, `records`, `export_snapshot` and `verify_export`. I also cross-checked the reported acceptance counts by hand: 27 events, control sequence 16, 38 records, 40 files and `exportedAt` 2026-09-21T11:26:40Z from NOW=1789990000. They are internally consistent with the acceptance script.

**Verdict: revise-before-release (narrow).** The core invariants hold statically:
- one effect per request;
- serialized terminal outcomes;
- the exact two-scope intersection;
- the readable-denial shape;
- forward operation closure;
- per-transaction row caps.

Every R1 correction is present. However, two concrete contract violations have trivial fixes and should be corrected and retested before release: the ID grammar leak and request-ID collision poisoning. Two further gaps need either a code change or an explicit scope statement: capacity exhaustion by a low-privilege caller, and a global-counter disclosure. After those changes, accept-with-explicit-limits looks attainable.

## 2. Findings

### Contract violations

**M1 (Major). Schema ID grammar accepts a trailing newline.**
- **Where:** `build_schema.py` patterns (`ID`, `TOKEN`, `HASH`, `PIN.uri`) are enforced through `validate()` → `Draft202012Validator`.
- **Mechanism:** jsonschema applies `pattern` with Python `re.search`, and Python `$` also matches just before a final `\n`.
- **Counterexample:** `add_definition` with `definitionId: "urn:synthetic:action:replace-labels\n"`, or a rule `audience`/`purpose` ending in `\n`.
  - Expected: refused ("bounded ASCII grammar").
  - Actual: accepted. The result is a visually identical, distinct ID with a distinct digest.
- **Consistency gap:** ECMA-262 validators reject the same instance, so the "normative" schema is non-portable. Paths that use `re.fullmatch` (retry key, `create`, `add_resource`, snapshot meta/resource IDs, manifest names) are correct, which makes the behaviour inconsistent.
- **Minimal fix:** anchor with `$(?!\n)` (valid in both Python and ECMA), or fullmatch-check all ID/token/hash fields in `validate()`. Add a test.

**M2 (Major). An admin mutation the validator permanently rejects (same class as the R1 later-resource defect).**
- **Where:** `Executor.add_resource` checks only `definitions`/`resources`, and `add_definition` checks only `resources`. `_validate` refuses `set(requests) & (definition_ids|resource_ids)` as `object-kind-collision`.
- **Counterexample:** a reader learns `requestId` `req.<hex>`. The host then calls `add_resource('req.<hex>', [], now)`, for example in a "resource per request" integration.
  - Expected: refused.
  - Actual: committed. From then on every `snapshot` fails validation, so export and native evidence become impossible, with no append-only recovery.
- **Minimal fix:** also check `requests.id` (and ideally event IDs) in both admin methods. Add a test.

**m1 (Minor). The export root is not canonical.**
- **Where:** `_verify_export` never compares the manifest bytes to a regenerated `file_bytes(manifest)`. Integer fields are compared with `==`, so `16.0` and `true` pass. Unlike record files, `snapshot.json` bytes are not regenerated either.
- **Effect:** many manifest byte strings verify for one cut. That weakens the "trusted external expected root" the spec relies on.
- **Fix:** rebuild the expected manifest from the snapshot and require byte equality. Type-check integers.

**m2 (Minor). The validator is looser than the executor.**
- `validate_snapshot` accepts delivery/try groups from an actor with zero current rights, and denied cancel tries without read. The executor can produce neither.
- A fabricated snapshot therefore passes checks that correspond to the R2 "no zero-rights growth" claim.
- **Fix:** require at least one right for replay groups, and read for denied cancel tries.

**m3 (Minor). Weak refusal codes and ID disjointness.**
- A group consisting only of `['submission']` fails via `IndexError` → `snapshot-malformed` instead of `operation-shape`. It is still refused.
- Event IDs are not checked disjoint from object IDs, so native `subjectIds` could be ambiguous in a hostile archive.

### Needs a fix or an explicit scope statement

**M3 (Major, availability). Any single-right caller can permanently exhaust the Dimension.**
- **Mechanism:** in `dispatch`, a replay by a caller holding *any* one right (read-only, observe-only, submit-only) appends delivery+try events. New submissions append at least 3 events each. The events table is global and there is no rollover.
- **Consequence:** about 5,000 read-only replays permanently halt execution for every actor. The global-revocation reserve protects the policy table, not events.
- **Effective capacity:** events bind first, so the store holds at most about 3,333 requests (about 2,500 effects) per lifetime. The 10,000-row request cap is unreachable.
- **Fix:** either limit replay event growth to execute-right holders, or list rate limiting as a trusted host duty and state the event-bound capacity in the adoption limits.

**M4 (Major, disclosure). Caller responses expose live global counters.**
- **Mechanism:** `observe` returns the new event, and a fresh commit returns its receipt. Both carry the global `sequence` and `controlSequence`.
- **Effect:** a caller with read+observe can repeatedly sample Dimension-wide activity by other actors. The spec says organizational reporting requires separately authorized projections.
- **Fix:** strip the counters from caller projections, or explicitly scope this leak out.

**m4 (Minor). Installer and AGENTS.md mismatch.** `AGENTS.md` instructs readers to consult README.md, model-spec.md and adoption-limits.md, but `install_fixture.FILES` installs none of them. The installed Dimension's agent guidance therefore points to absent files. The jsonschema dependency is also not declared in the installed binding.

**m5 (Minor). Scale.** `validate_snapshot.current_policy` is O(events × policies), and `native.records` scans requests per event, O(events × requests). Near the combined 10k boundaries this is 10⁸ Python steps. Neither combined boundary is tested.

**m6 (Minor, documentation).**
- The byte contract relies on Python's `json.dumps` escape table (control characters as lowercase `\u00xx`, short escapes, raw U+2028). A reimplementer needs that table stated.
- `Policy maxItems 128` is unreachable under the 128 KiB encoding limit (roughly 80 rules).

### Honest scope deferrals (not defects)

These are consistent with the contract:
- Compensation blocked after same-pin retirement.
- Admission while the definition is unavailable.
- Coherent-restore blindness.
- Whole-archive forgery without an external root.
- Undetectable omission of entire non-state-changing groups (for example an observation) without a trusted root.
- No hardware or power-loss claims.
- The WM-XCT-040 composer gap.

### R1 corrections rechecked

| R1 defect | Status |
|---|---|
| Later-created resource invalidated earlier rejection | Fixed (`precondition` compares resource `control_sequence`; tested at offsets 0 and 1) |
| Executor could exceed archive row bounds | Fixed (whole-transaction caps in `_tx`, rollback before COMMIT); see M3 |
| Incomplete transaction tails passed replay | Fixed (grouped expected shapes) |
| Readable denied replay omitted retained state | Fixed (`_out` adds requestState/receipt) |
| Missing companion policy/retirement evidence | Fixed via snapshot+manifest stored inside the Dimension and validated from readback |
| Nonportable raw-ID filenames | Fixed (SHA-256 names) |
| Malformed errors escaped | Fixed for caller and verification paths; admin raises `Refused` or raw `sqlite3`/`OSError` |
| Lock simulated "published" | Fixed (`candidate`/`simulationOnly`) |

## 3. Adversarial cases (static outcomes)

1. **Resource created after a rejection, same second.** The validator treats the row as future at that control sequence, so the rejection stays valid. ✓
2. **Zero-rights replay, cancel and observe, repeated.** They return withheld and add no rows. ✓
3. **Read-only caller replays about 5,000 times.** Events fill up and execution is globally halted. ✗ (M3)
4. **Admin creates a resource named with an existing requestId.** Committed; the store can never be exported again. ✗ (M2)
5. **definitionId with a trailing newline.** Accepted by the schema. ✗ (M1)
6. **Permission split across two rules (principal side in one, delegate side in the other).** `current-execution-denied`. ✓
7. **`compensatesReceiptId` pointing at a submission event.** Short-circuits to `rejected-precondition`, no KeyError. ✓
8. **Compensation after an intervening update with equal labels.** The revision check rejects it. ✓
9. **Concurrent cancel and execute.** `BEGIN IMMEDIATE` yields a single terminal outcome, and the validator matches it. ✓
10. **Policy table at 9,999 rows.** A non-empty policy is refused, an empty one lands at revision 9,999, and the next empty one is refused by the row cap. ✓
11. **Receipt deleted, or all events after submission deleted.** `operation-incomplete` or `missing-history`. ✓
    - Deleting a whole observation group and renumbering passes. This is the documented limit.
12. **Manifest re-serialized, or `"controlSequence":16.0`.** `verify_export` passes. ✗ (m1)
13. **Torn record, then re-export to the same directory.** `export-existing-content`; a fresh directory succeeds. ✓
14. **Conflicting body where the old context is readable but the new one is not.** Withheld. ✓ statically, but untested.
15. **Case-distinct IDs (`urn:case:A` / `urn:case:a`).** Hashed names do not collide. ✓
16. **A second correction of the same observation (fork).** Refused by both the executor and the validator. ✓
17. **NaN, duplicate keys, bool integers or lone surrogates on the wire.** Withheld, no rows. ✓
18. **Forged snapshot containing zero-rights replay groups.** The validator accepts it. ✗ (m2)

**Important test omissions:**
- Trailing-newline IDs.
- Admin creating a resource or definition with a requestId.
- Low-privilege capacity exhaustion.
- Non-canonical manifests.
- The validator refusing executor-impossible events.
- Expiry materialized by a caller holding only a non-execute right.
- Conflict with the old context readable and the new one unreadable.
- Export and validation performance at combined 10k boundaries.
- Multi-cut or incremental native installation (re-appending an earlier cut's identical records to the Dimension).
- The definitions table at its cap.

## 4. Semantic boundary, coverage, navigation, installation

**Semantic boundary.** The boundary is sound and honestly stated:
- description is kept separate from permission;
- descriptive-only definitions are unexecutable;
- a single SQLite master, with native records as projection;
- observer claims are kept separate from receipts;
- the non-JCS encoding is clearly labeled.

Trusted host duties are explicit, but rate limiting should be added to them (M3).

**Per-field and whole-object coverage.**
- Five-facet coverage is supplied for all nine canonical types and ten supporting values, which is adequate.
- Gap: the native object type `OrderedLabelResource` with its `syntheticLabels` facet is emitted as native records but is covered only as a supporting value.
- Gap: `factMastership` omits policy and retirement, even though the spec calls them mandatory companion evidence.

**Bundle→Layer→Finding→Question usefulness.**
- All 52 questions have distinct evidence and derivation text.
- `ifMissing`, `status` and action suffixes are identical boilerplate.
- Each bundle has exactly one layer, so the Layer tier adds no discrimination.
- Answers are prose guidance rather than machine-checkable output shapes.
- Q14 (who verified standing) and Q46 (external root) will usually return insufficient-context, which is honest.

This is useful for host guidance, not for automated evaluation.

**Installation evidence.** The acceptance script, as written, performs these steps; I have not verified that it actually ran:
- verifies tool pins;
- installs exact bytes;
- executes the installed bundle;
- validates from the stored snapshot readback;
- appends native records;
- demonstrates an outer-pass/nested-reject tamper;
- confirms duplicate refusal;
- keeps the lock at candidate status.

The reported counts are consistent with the script. Limits:
- The route is not WM-XCT-040.
- Only one cut per Dimension is exercised.
- The installed AGENTS.md references files that are not installed (m4).

## 5. Release recommendation

Do not release R2 as frozen. Minimal path forward:
1. Fix M1 and M2 and add tests.
2. For M3 and M4, either change the code or add explicit limit text covering host rate limiting, the event-bound capacity (about 3,333 requests), and counter disclosure in caller responses.
3. Canonicalize the manifest check (m1).
4. Regenerate the bundle, rerun the source, bundle and native acceptance suites, and re-freeze.

**Limitations that would remain after those fixes:**
- Synthetic local fixture only.
- Internal consistency is not authenticity or latest state.
- No distributed, exactly-once or external effects.
- No restore reconciliation.
- No mandate registry or legal conformance.
- Same-pin-only compensation.
- Full retention with no erasure.
- A fixed reference capacity.

This review cannot waive the owner's process or authorize publication. Release remains subject to the owner's decision and live publication verification.