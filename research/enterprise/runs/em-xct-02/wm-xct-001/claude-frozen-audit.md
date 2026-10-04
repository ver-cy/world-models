# Enterprise Fact Authority 0.1.0: frozen semantic audit

**Verdict: BLOCK.** The library semantics mostly hold. However, the "actual native acceptance" evidence contradicts the package's own boundary contract in two places. Both are internal contradictions, not deferred production features.

## Input completeness

The files provided appear complete and not truncated. Several referenced artifacts were **not supplied**, so I did not review them:

- `crosswalk.json`
- `research.md`
- `runtime-model.reference.json`
- `tool-pins.json`
- `requirements.txt`
- `examples/*.json`
- `upstream/*`

Without them I cannot confirm the "direct byte inspection" claim about the parent, the example contents, the pin values, or any digest. `test-results.json` reports 45 tests, which matches the 45 test methods in `test_authority.py`. I cannot confirm that this result, or `acceptance-results.json`, came from these exact bytes.

## Blocking findings

### B1 (High): the native binding asserts more than a discovery association

**Demonstration.** `acceptance.py` composes a release with these values:

- `modelId: vr.wm-xct-001`
- `version: 0.3.0-research.1`
- `role: core`
- `publicationStatus: published`
- `installationMode: native-binding`
- `binding.forSpecificationDigest` set to the WM-XCT-001 spec digest

It also stores the register as `objectType: 'vr.wm-xct-001:authority-register'`. The pins in `acceptance-results.json` record `{"id":"vr.wm-xct-001","mode":"native-binding"}`.

A lock or registry consumer reading these machine fields would conclude that WM-XCT-001 is installed natively and defines an `authority-register` type. The only disclaimer is the free-text `binding.scope` string. Marking the parent `published` with compatibility `accepted` also contradicts the README statement that "parent research and its historical source holds remain open."

**Contradicts:**
- README: "not an `is-a` claim"
- `composition.yaml`: "no subtype assertion"
- The boundary decision: "unchanged parent specification"

**Correction.**
1. Install WM-XCT-001 as `installationMode: 'semantic-only'` with `binding: null`.
2. Ship the companion as its own release with its own modelId and namespace, for example `vr.em-xct-02.enterprise-fact-authority@0.1.0`.
   - Add `references: [{modelId: 'vr.wm-xct-001', relation: 'discovery-association', specSha256: …}]`.
   - Set `binding.forSpecificationDigest` to the profile's own spec digest.
   - Set the object type in the profile namespace.
   - Set a publication status consistent with reviewable-draft.
3. If the composer cannot host a binding without attaching it to a parent release, record that as a tooling hold rather than shipping the binding.
4. Re-run acceptance.

### B2 (High): the native envelope gives register mastership to a steward

**Demonstration.** The stored snapshot fact carries `authority: {'source': 'urn:synthetic:actor:steward', 'rank': 0}`.

**Contradicts:**
- I03 (owner, steward and model maintainer are not implicit writers).
- model-spec: a steward "may receive a route, not acquire powers."
- The boundary decision, which assigns register storage to the deployment operator.

The native `append` path is also the only write path this acceptance exercises. It bypasses `admit` entirely, so in a native deployment register integrity reduces to whoever holds native append rights. That actor is currently labelled as a steward.

**Correction.**
- Set `authority.source` to a deployment register-operator identity and `masterSystem` to the deployment governance register.
- Add an acceptance assertion that the envelope authority is neither an accountable party nor a steward in any stored authority.
- Document that native fact authority governs envelope storage only, never FactAuthority semantics.

## Non-blocking holds

### M1 (Medium): no snapshot-succession check (rollback is undetectable)

`validate_ledger` validates each snapshot on its own terms. Consider the stored startup snapshot with observation 2, or the second authority revision, removed:

- The truncated snapshot is still companion-valid.
- The answer flips from `contested` to `preferred`.

`migration.md` calls replacement by an old file invalid, but nothing detects it. The acceptance only writes `snapshot-r1` with `supersedes: []`.

**Correction.** Add `validate_extension(previous, candidate, config)`:
- Header fields are equal.
- Each collection of `previous` is an exact, encode-equal prefix of `candidate`.
- Every appended receipt is later than the previous head.

The native adapter should call this and `admit` for each appended row. Each snapshot fact should supersede the prior one and carry its `inputDigest`. Add a truncation negative test to acceptance.

### M2 (Medium): replay idempotency conflicts with host-stamped receipts

**Demonstration.**
1. The host admits observation 3 at T1, stamping `recordedAt = T1`.
2. The response is lost and the client retries.
3. The host stamps `recordedAt = T2`.
4. `(id, 1)` exists, the bytes differ only in `recordedAt`, and `admit` raises `Conflicting replay`.

A replay is a no-op only if it carries the original stamp, which the README says clients must not choose. `test_replay_idempotent` covers only the case where the stored row is resubmitted.

**Correction.** Compare replays with `recordedAt` excluded. On a match, return the unchanged ledger plus the stored row as the receipt. Test two cases: a retry with a later `now` is a no-op, and a retry with a changed value is rejected.

### M3 (Medium): same-source disputes can become permanently unresolvable

**Demonstration.**
1. Writer W1 writes O1 (source S, value `A`).
2. The grant is revised to `writers: [W2]`.
3. W2 writes O2 (source S, value `B`). The result is `contested` indefinitely.

Neither W2 nor the governor can retract O1: `writer` is a lineage anchor, and retraction requires `writer == actor` plus a current grant. The only exits are unsatisfactory:
- Remove S's rule, which turns the answer into `unknown`.
- Re-grant a departed actor.
- Invent an alias source.

Q08 and Q11 promise human review, but the review cannot be recorded.

**Correction (either):**
- Make the anchor source + subject only, keep `writer` per revision, and require each revision's writer to be in the current grant for that source.
- Or state this explicitly as a 0.1.0 limit.

### M4 (Medium): `admit` is a read side channel for non-readers

`admit` returns the full ledger. Its error messages also reveal state:
- `Conflicting replay` means some `(id, revision)` exists.
- `Unknown or contested write authority` and `Overlapping write grants` reveal authority and grant state.

**Demonstration.** A writer who is not in `readers` submits a record with a guessed ID, its own writer and source, and receipt `now`. A `Conflicting replay` error means another source's observation with that ID exists.

This contradicts the principle that governors and writers do not automatically gain read rights.

**Correction.**
- Document that the host must never return the ledger or raw messages to the caller.
- Collapse post-authorization failures into a single message such as `Admission rejected` for non-readers.
- Return a receipt, not the ledger, from the host-facing API.

### M5 (Medium): corrections and transfers are indistinguishable, and start truncation is not enforced

**Demonstration.** A revision of authority rev1 that sets `validFrom = 2026-10-01` and a new `accountable` is accepted. At `knownAt = now`, a query for `validAt = 2026-06-01` returns `unknown`. Past valid-time coverage is erased, even though the transfer rule says "preserve start." Nothing in the data says whether this was a correction or a mistaken transfer.

**Correction.** Add a required `change` field with values `genesis | correction | closure | retraction`. For `closure`, enforce that everything equals the predecessor except a reduced `validUntil`, with part ends clipped to it.

## Low-severity findings

| # | Finding | Correction |
|---|---|---|
| L1 | Outcomes pin only the authority. There are no rule or stewardship part pins and no observation `(id, revision, sha256)`, although the contract requires part references to carry ID + revision + digest. | Add `rulePins`, `routePins` and `observationPins`. |
| L2 | The requirement that a part ID be "distinct from authority/party" is not enforced. A stewardship with `id == party` is accepted. | Check the part ID against party, source, writers, accountable and issuedBy. |
| L3 | `authority-contested` and `overlapping-source-rules` outcomes return empty `observationIds` and `evidence` even when observations exist. | Include them, or add `observationsEvaluated: false`. |
| L4 | A governor can add themselves to `writers` in one revision. There is no separation-of-duties check. | Document this, or enforce `issuedBy ∉ writers`. |
| L5 | `composition.yaml` marks 002 as `pattern-alignment` although WriteGrant is explicitly not 002. The 001 relation should be `discovery-association`. | Correct both relation values. |
| L6 | Acceptance breaks after 2026-12-31: it uses the wall clock (`c.now()`) against fixed plan and policy windows. | Inject a fixed clock. |
| L7 | Minor inconsistencies: digest formats differ (bare hex vs `sha256:` prefix), and `inputDigest` omits the ledger header. | Unify the digest format and include the header. |
| L8 | Unauthorized callers can see config-validity or schema messages, because `root_check` runs before the read denial. | Deny first, or return a generic message. |

## Probe results (library behaviour holds)

- **Precedence vs grants:** independent. `evaluate` never reads `writeGrants`, and write checks never read rules.
- **Unknown and conflict outcomes:**
  - No authority gives `unknown`.
  - Overlapping authorities or duplicate rules give `authority-contested`.
  - Duplicate grants deny writes.
  - Equal-priority or same-source disagreement gives `contested` with a null value.
  - There is no majority vote and no approval without a steward.
- **Past knowledge:** the order is receipt cut, then latest revision, then interval, then state. Corrections do not leak into earlier `knownAt` queries.
- **Receipts:** strictly increasing, equal to `now`, and unique per second.
- **Denied reads in `evaluate`:** only `Read denied` is returned, and the ledger is not touched.
- **No value coercion.**
- **Tool pins:** they bind bytes only, and the README states the import-sandbox limit. I could not check the pin values because `tool-pins.json` is missing.

**Identity and history:** for a single register, the narrow binding does preserve them. Each part's `(authority, kind, party/source)` is immutable across all revisions and cannot collide with record IDs. Every part version can be recovered through the containing authority revision under `knownAt`. Transfer by new part IDs keeps prior rows. The remaining gaps are auditability issues (L1, M5), not contradictions:
- Part-level change intent is not recorded.
- A removed part ID can reappear.
- There is no cross-register uniqueness; this is stated as deferred.

## Remaining holds

1. **B1:** re-bind as a separate profile release. WM-XCT-001 becomes semantic-only, and the object type moves to the profile namespace.
2. **B2:** remove steward mastership from the native envelope.
3. M1: add a snapshot-succession check.
4. M2: fix replay semantics.
5. M3: fix same-source resolvability, or declare it as a limit.
6. M4: close the admission read channel, or document the host obligation.
7. M5: add a change kind and enforce closure.
8. Unreviewed artifacts: crosswalk, runtime model, pins, examples and upstream.

Clearing B1 and B2, with M1–M5 either fixed or explicitly documented as limits, would support **ACCEPT WITH LIMITS**.
