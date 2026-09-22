# EM-XCT-08 R3: Independent Static Audit

**Verdict: BLOCK.** There is one High-severity finding (H1). Coverage attestation, a gate R3 claims to separate, can be satisfied by a principal that does not hold the attestation right. Everything else I found is Medium or Low. If H1 were fixed and tested, and the Medium items were fixed or explicitly documented and tested, I would expect to reach ACCEPT WITH LIMITS.

## Scope and input completeness

I read all 30 body-supplied files in full. That includes the literal `spec.model.scope`, all three example archives and the `tool-pins.json` inventory. On reading, `spec.model.scope` appears text-identical to `model-spec.md`, but I did not compare them byte for byte.

These are the 8 inventory-only paths, not supplied and not read:
- `parent-comparison.md`
- `provider-roles.json`
- `research-adjudication.md`
- `research.md`
- `source-verification.json`
- `upstream/wm-xct-012-provenance/AGENTS.md`
- `upstream/wm-xct-012-provenance/publication.json`
- `upstream/wm-xct-012-provenance/spec.yaml`

The composer and skill implementation bodies pinned in `tool-pins.json` were also not supplied. `review.json` and `review.md` are pending release evidence and I do not treat them as acceptance.

This was a no-tools audit. I executed nothing, browsed nothing and verified no hash. `test-results.json` (81 tests) and `acceptance-results.json` (3 profiles) are author-supplied reports; I checked only that their digests and counts are consistent with the inventory and example files, not that they are true. Native outer validation depends on WM-XCT-040 code I did not see. Each conclusion below rests on reading the supplied source.

## R3 fixes confirmed by reading

These R3 claims are implemented as described:
- Build binding: `BUILD_ID` covers the source bytes, a NUL and the schema bytes. It is checked in `Register.__init__`, `replay` and `archive_from_native`, and the chain root binds `{config, buildId}`.
- Per-event full-state `outcomeDigest` is verified in `replay`, and `validate_archive` compares canonical bytes, which closes the bool/int loophole.
- Control characters: `encode` rejects C0/DEL/C1 and surrogates, and every schema pattern ends in `$(?![\s\S])`.
- Conflict journaling is compact: `compact_conflict` stores no items or content. On replay, `record_conflict` re-derives the reason from prior state, and its budgets are enforced before any append.
- Correction lookup is scoped by scope and purpose in `occurrence_by_id`, requires map and read, and returns a uniform DENIED for foreign or missing targets.
- Mapping `corrects` refuses a foreign scope or purpose uniformly and requires the same lineage. Activation requires the predecessor to be retracted.
- `round-open` requires attest-coverage for source-snapshot or `visibilityCovered`.
- The native snapshot profile is closed and checks the authority by canonical bytes.

## Findings

### H1 (High, blocker): coverage completion bypasses attest-coverage

The attest-coverage right is checked only in `apply` op `round-open`. Committing a round page (the `commit` branch with `roundId`, including `terminal=True`) and `round-seal` need only `intake`. `round-seal` then sets `complete`, and `assess_rounds` treats `complete` together with the open-time declaration as sufficient for absence comparison. A principal holding intake alone can therefore end an attested snapshot early and make it absence-eligible.

Counterexample using the fixtures (WRITER holds all rights, OTHER holds intake only):
1. Run `h.round('urn:synthetic:round:1',['a','b'])`.
2. WRITER opens R2 as `source-snapshot`, `visibilityCovered=True`, `previousRoundId=R1`, with `notEarlierEvidence`.
3. OTHER commits `h.batch('p0',[],round_id=R2,page=0,terminal=True)`, which is an empty terminal page.
4. OTHER calls `round-seal {id:R2, errors:[]}`. Because `all(...)` over zero items is vacuously true, `complete=True`.
5. `assess_rounds(archive,R1,R2)` returns two `not-observed-in-comparable-rounds` candidates.

A second variant: WRITER's attest-coverage is revoked by a new policy revision after step 2, and WRITER still completes the round. That contradicts "requires the separate current attest-coverage grant." The impact is limited to steward-review proposals with `effects:[]`, but it defeats a control R3 explicitly claims to have fixed.

**Required change:** for rounds declaring source-snapshot or `visibilityCovered`, require current attest-coverage (at least) for the terminal page and for `round-seal`. Alternatively, record the attester and set `complete=False` whenever the terminal page or seal lacked a current attester. Add tests for both variants.

### M1 (Medium): `assess_rounds` output depends on dict order

`explicitAvailabilityEvidence` picks `unavailable[-1]` while iterating `s['batches'].values()`. For `reg.archive()` that order is insertion order. For the same archive after a canonical round trip (`decode(encode(a))`, sorted keys), it is slot-digest order.

Counterexample: R1 observes `a`. Then batch X records `a` as `source-deleted` and a later batch Y records `a` as `inaccessible`. R2 is empty. Choose batch keys so that Y's slot digest sorts before X's. `assess_rounds(a,…)` reports `inaccessible`, while `assess_rounds(decode(encode(a)),…)` reports `source-deleted`, and both archives validate.

The same filter matches on `scopeId` only, not `purpose`, so availability evidence from another purpose is mixed in.

**Required change:** select evidence by maximum receipt sequence, filter by purpose, and test determinism across a round trip.

### M2 (Medium): cross-scope existence oracles and cross-scope mapping governance

Mapping and round IDs share one global namespace. A map grantee with rights only in scope B who submits `mapping` with the ID of an existing scope-A mapping gets `Invalid('mapping identity')`, while a fresh ID succeeds. `round-open` with a best-effort body behaves the same way (`'round exists'`).

Activation uniqueness and `mapping_outcome` both match on lineage and purpose across scopes. When two scopes share source, resource and scheme (for example, a filter or interpretation rotation), three things follow:
- A scope-B steward can learn that scope A has an active claim for that lineage (`'active mapping already exists'`).
- Scope-B receipts pin and disclose scope-A mapping IDs.
- Scope-B map grantees cannot retract the scope-A claim, because `mapping-state` authorizes against the mapping's own scope. `corrects` also forbids replacing it across scopes.

This is inconsistent with invariant 6's no-probing intent, which R3 fixed only for corrections.

**Required change:** scope object IDs, or return a uniform DENIED on collision with foreign-scope objects. Document or restrict cross-scope pin reuse and its governance path. Add tests.

### M3 (Medium, availability): full replay cost is quadratic

`execute`, `read_receipt` and `archive` replay the full journal under a lock. `execute` uses `BEGIN IMMEDIATE`, which holds the write lock for the whole replay. Each replay schema-validates every event and computes `digest(state)` over the full canonical state for every event. The cost is roughly events × state size per call, which near the stated 2,000-event / 8 MiB budget means gigabytes of encoding and hashing per operation.

Concurrent writers then hit `sqlite3.connect(timeout=10)` and receive `sqlite3.OperationalError`, not the uniform refusal. "Reserve capacity for closure" may be practically unreachable. No test exercises the stated budgets.

**Required change:** add a budget-scale benchmark and either lower the budgets or cache verified prefixes per build.

### M4 (Low–Medium): transport size limit versus canonical budget

`decode` rejects raw input over `MAX_BYTES` before canonicalizing it, but the specification bounds only the canonical archive and says external whitespace is accepted. `fixtures.py` writes `indent=2`, and `json.dumps` defaults to `ensure_ascii=True`, which inflates non-ASCII characters. A valid archive near 8 MiB canonical, exported in the package's own style, is refused by `inspect_import` and `acceptance.py`.

**Required change:** use a separate transport limit or document the restriction, and add a test.

### Low findings

- **L1:** `inspect_import` does not catch `RecursionError`. For example, `b'['*200000+b']'*200000` (about 400 KB) raises instead of returning a LossReport.
- **L2:** The claim "Runtime/dependency versions remain separately pinned" is not supported by the supplied bodies. Only `jsonschema==4.26.0` is pinned. Transitive dependencies (`referencing`, `rpds-py`, `jsonschema-specifications`, `attrs`), Python ("3.12 or newer") and SQLite are recorded but not pinned.
- **L3:** `Register(path,config)` creates the file (`open('xb')`) before the bootstrap transaction. A crash in between leaves an empty file: reopening gives `OperationalError` and re-bootstrapping gives `FileExistsError`.
- **L4:** There is no non-privileged API to discover the head and fence. The head is shared across purposes within an epoch, and receipt IDs embed the global journal sequence, which reveals total register activity to write-only callers.
- **L5:** The clock-rollback check in `execute` runs before authorization, so an unauthorized call with a stale time gets `Invalid` rather than DENIED. The clock is a trusted host input, so impact is minimal.
- **L6:** The ai-team dataset scope reuses the scheme `urn:synthetic:scheme:board-key`. This is cosmetic.

## Documented host duties (not blockers)

These are documented as host responsibilities and I do not count them against the candidate:
- Authentication, source and steward verification, and trusted time.
- Evidence custody.
- Establishing the latest owned store and detecting clones.
- Trusting the native predecessor and the first snapshot.
- The one-bit key-unavailability inference.
- Diagnostic loss at the 128/8 limits.
- The absence of power-loss or lying-storage guarantees.
- Non-public error detail for authorized malformed inputs.
- Hashes proving consistency rather than authenticity.

## Missing tests

1. Intake-only terminal page or seal on an attested round, and attester revocation before seal (H1).
2. `assess_rounds` determinism across a canonical round trip, and cross-purpose availability evidence (M1).
3. Foreign-scope mapping and round ID collisions, and cross-scope activation and pin disclosure and governance (M2).
4. Latency and lock behaviour at the 2,000-event / 8 MiB budget, with concurrent-writer timeouts (M3).
5. `inspect_import` of a near-budget archive in `indent=2` and `ensure_ascii` transport form (M4).
6. Deeply nested import input (L1).
7. Cross-purpose batch-key collision and `read_receipt` purpose isolation.
8. Tampering with a retained conflict record's reason inside an archive, beyond the existing injection test.
9. Recovery from a crash during bootstrap.

## Residual adoption limits (even after fixes)

The candidate remains a single-host synthetic reference. There is no IAM, no live connectors, no distributed exactly-once delivery, no writable import, no automated quarantine resolution and no source authentication. Absence results are proposals only, and native snapshots are restricted projections whose currency depends on the host. Acceptance evidence depends on unsupplied WM-XCT-040 code and author-run reports. Research assurance remains reviewable-draft, and the publication metadata in `acceptance.py` is synthetic.