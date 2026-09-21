I can see `END OF FROZEN AUDIT INPUT`. The core contract files are present through `composition.yaml`. Referenced but absent from this bundle: `research.md`, `crosswalk.json`, `examples/*.json`, `tool-pins.json`, `runtime-model.reference.json`, `upstream/**`, `requirements.txt`. Those absences are completeness holds, not evidence that the pasted code was cut mid-file.

# Semantic audit — Enterprise Fact Authority 0.1.0

Independent reviewer. Not an approver. No tools. No inferred consensus.

## Scope of review

Reviewed as a bounded reference: trusted host, trusted configuration, trusted actor, trusted receipt clock, trusted full ledger, trusted subject/scope binding. No production IAM, signature, durability, or source-connector claim is in scope. WriteGrant is treated as an original construct, not WM-XCT-002. WM-XCT-001 is treated only as a discovery association / pattern alignment, not ControlRecord conformance.

## Binding and identity

The package’s stated attach point is internally consistent with the text it ships. README, `boundary-decision.md`, and `composition.yaml` all refuse `is-a` ControlRecord. `governs` is fixed to `values`. `definitionAuthorityRef` is an unchecked external pointer. That is the correct narrow reading of `controllable-object-anchor`: a predicate is not owned as a controllable meta-object.

**Does the nested-part binding preserve identity/history?** Yes for the claim they actually make; no for independent assignment streams, which they defer.

- Part URIs are stable and distinct from party, source, and authority.
- `validate_ledger` freezes `(partId → authorityId, kind, party|source)`. A party or source change on the same part id is rejected (`test_graph_negatives` / `part-party`, `part-source`).
- Transfer in `test_transfer_preserves_valid_history` closes the old term on the same authority id, then mints a new authority id and new part ids from the cutoff. `knownAt` / `validAt` still reconstruct the pre-cutoff accountable party.
- Part *version* is only `(partId, authorityId, authorityRevision, authorityDigest)`. Duty, priority, and writer-set changes are whole-authority snapshots. There is no part-level `previousDigest` and no tombstone row when a later revision simply omits a part.

That is a limited document binding, not a hidden subtype. Callers who cite a part id without the containing authority pin cannot distinguish duty/priority editions. That is a disclosed deferral, not an unstated contradiction.

Schema `$id` and acceptance `objectType` (`vr.wm-xct-001:authority-register`) still live under the 001 path. That is association optics, not a conformance claim, but it is the main remaining way a later reader will mis-inherit ControlRecord semantics.

## Contract probes

### Source precedence versus write grants

Held. Separate types, separate clocks.

- Ranking uses `MastershipRule.priority` at **fact-valid** time (`active(rule, validAt)`).
- Submission uses `WriteGrant` at **trusted now** (`authority_for_write(..., now, now)`).
- `test_priority_does_not_grant_write`: rules remain, grants emptied → evaluate still `contested`; new admit denied.
- `test_write_grant_does_not_grant_precedence`: grants remain, rules emptied → admit succeeds; evaluate `unknown` / `no-ranked-observation`.
- Accountable, steward, governor, and writer are distinct; owner/steward cannot admit (`test_owner_not_writer`, `test_steward_not_governor`, `test_confused_deputy`).

No internal collapse of rank into permission.

### Unknown and conflicts

Held for the cases they encode.

- No authority → `unknown` (`test_no_authority`).
- Two active authorities for the same scope/predicate → `authority-contested`; further observation admit denied (`test_overlapping_authorities`).
- Duplicate active rules for one source → `authority-contested` / `overlapping-source-rules` (`test_ambiguous_rules`).
- Equal min-priority, different tagged lexical values → `contested`, `value is None`, both evidence refs, `routeTo` set (`test_equal_conflict`).
- Same lexical + datatype from two sources → `preferred` (`ai-team`).
- Lower priority later import does not win (`test_lower_priority_late_csv`, `test_reverse_import_receipts`).
- `01` versus `1` contests (`test_value_not_coerced`).
- Two records from **one** source with different values contest (`test_same_source_conflict`). Source count is not a vote.

Missing authority is not a grant. Missing steward is an empty route, not an approval (`test_future_steward`, `ai-team`).

### Whole-term correction and transfer

Held within the one-receipt-per-second, two-admit transfer model.

- A revision must cite the predecessor digest and replaces the whole claimed interval.
- `test_correction_history` / `test_retraction_history`: current knowledge changes; `knownAt` before the new receipt keeps the old status; prior rows remain.
- Transfer keeps the old start and old party on the closed term; successor is a new id from the cutoff. Query at `NOW` still names the old accountable; query at `cutoff` names the successor.
- Exclusive end: `validAt=END` is `unknown` (`test_exclusive_interval_end`).
- Multi-record durable atomic transfer is deferred in the text and unimplemented in code. A crash between the two admits is fail-closed. That is a production deferral, not a spec/code fight.

### Past knowledge and receipts

Held.

- Evaluate order is `recordedAt <= knownAt`, then latest id, then interval and state.
- `knownAt > now` rejected (`test_future_knowledge`).
- New receipt must equal trusted `now` and strictly follow every prior receipt (`test_backdate_receipt`, `test_future_receipt`, `test_head_order`).
- Exact `(id,revision)` replay is idempotent after current authorization; mutated replay rejects (`test_replay_idempotent`, `test_conflicting_replay`).
- Retroactive rule change received later does not alter an earlier knowledge cut (`test_retroactive_rule`).

`recordedAt` is explicitly receipt, not source-event time and not authenticated publication. There is no fifth policy-publication clock. That is a deliberate collapse, not an accidental one.

### Denied-read leakage

Held for the stated all-or-deny rule.

- Reader/purpose check runs after config currency and **before** `validate_ledger`.
- Unauthorized actor or purpose raises `Denied('Read denied')` only (`test_denied_no_data`, `test_purpose_denied`).
- The malformed-ledger deny test never inspects ledger contents.
- Authorized evaluate returns the full matching slice, including losers and unranked ids. No implementation hides one observation from a permitted reader.

This is coarser than a 002 projection. It does not violate *this* package’s disclosure rule.

### Pins and native acceptance

Held.

- Every evaluate result carries `profileVersion`, `authorityPins` (`id`, `revision`, `sha256`), `inputDigest` of the known register slice, and `configDigest`.
- `acceptance-results.json` shows native V3 `valid: true` on a nested snapshot with `priority: -1`, while the companion raises `Invalid`. That is the documented native/companion split, not a passing claim that V3 proves semantics.

Frozen `test-results.json` reports 45 tests, 0 failures. That matches the 45 `test_*` methods in the pasted runner. I did not re-execute.

---

## Defects versus deferrals

Only internal contradictions with the *stated bounded contract* can BLOCK. Production absences listed in README/model-spec are limits.

### 1. Evaluate drops observations when authority is absent

**Severity:** Medium (limit / spec tightness, not BLOCK)  
**Contract tension:** model-spec step 6 and Q15 say retain matching observations / expose unranked ids. Code returns immediately on `len(match)==0` with `observationIds=[]` and `evidence=[]`, even if asserted rows exist for that subject/predicate.  
**Concrete input:** Ledger with no active authority (empty authorities, or sole authority `state=retracted`) plus two asserted observations for `urn:synthetic:subject` / `urn:synthetic:predicate`. `evaluate(..., validAt=NOW, knownAt=NOW)` → `status=unknown`, empty observation lists.  
**Correction:** Collect the matching observation slice before the authority early-return. Keep `status=unknown` / `reason=missing-authority`. Do not rank or set `value`.  
Why not BLOCK: zero authorities is defined as unknown and “never a grant.” Hiding ids from the *evaluation artifact* is consistent with not selecting a value. Raw ledger access remains the full-register channel.

### 2. `validate_ledger` / `import_snapshot` accept overlapping write grants

**Severity:** Low  
**Concrete input:** Snapshot whose single active authority contains two `writeGrants` for `urn:synthetic:source:a` with overlapping intervals. `import_snapshot` / `validate_ledger` succeed. `admit` of a new observation later raises `Overlapping write grants`.  
**Correction:** Apply the same uniqueness check in `validate_ledger` that `authority_for_write` applies at `now`, or document that grant overlap is query/admit-only.  
Why not BLOCK: import is declared “not an admission or security boundary.”

### 3. Observation interval is not contained in any authority interval

**Severity:** Low  
**Concrete input:** Authority `[2026-01-01, 2027-01-01)` and an admitted observation `[2020-01-01, 2030-01-01)`. Queries at 2020 are `unknown`; the row is retained but dead for selection.  
**Correction:** On admit, require observation `[validFrom, validUntil)` ⊆ the unique current authority term, or reject as host-invalid.  
Why not BLOCK: host is trusted for subject/scope/cardinality; past effective dates are allowed.

### 4. `Denied` is a subclass of `Invalid`

**Severity:** Low  
**Concrete operation:** `except Invalid` around `evaluate` treats `Read denied` as a schema failure.  
**Correction:** Make `Denied` a sibling of `Invalid`, or give it a distinct catch path in the agent-guide.

### 5. Association optics under WM-XCT-001

**Severity:** Low (documentation risk)  
**Concrete artifact:** schema `$id` `.../wm-xct-001-ownership-stewardship/profiles/enterprise-fact-authority/0.1.0/...` and composed `objectType` `vr.wm-xct-001:authority-register`.  
**Correction:** Sibling URI and object type that do not look like a 001 profile class. Keep the crosswalk as pattern-alignment only.

None of these make equal-rank contest, last-write independence, unknown-is-not-a-grant, transfer history, or native/companion distinction false.

## Explicitly deferred (not defects)

No signatures, durable concurrency, source connectors, subject-membership proof, policy federation, recursive delegation, definition-authority resolution, adjudication, confidence, staleness, multi-valued predicates, units, legal validity, production PEP, existing-Dimension migration, independent assignment revision streams, cross-authority reusable assignments, authenticated policy publication distinct from receipt, fine-grained 002 disclosure, erasure/legal hold.

`preferred` is a selected lexical tag. The contract already says it can be false.

## Holds that remain open

1. Unread ISO / legal-validity holds inherited from WM-XCT-001.  
2. `research.md` and `crosswalk.json` not in this frozen bundle; source-linking cannot be checked.  
3. Example JSON files not pasted; fixtures were audited via `test_authority.py` constructors and `acceptance-results.json`, not the on-disk examples.  
4. Predicate identity (SKOS vs opaque URI) unresolved; package correctly uses opaque URIs.  
5. Overlapping unequal-rank *partial* scope composition is out of 0.1.0 (exact scope match only).  
6. Fifth clock (authenticated policy publication ≠ receipt ≠ valid time) is not implemented.  
7. Part citation without authority digest is ambiguous after a duty/priority edit.  
8. Retention versus erasure of party URIs is deployment-unresolved.  
9. Tool pins hash local bytes only; they do not authenticate Python imports.  
10. This review did not re-run the test or acceptance processes.

---

## Verdict

**ACCEPT WITH LIMITS**

The frozen 0.1.0 reference does not violate its own bounded contract on the probes required: source precedence is not a write grant; equal-rank disagreement is contested and retains both evidence references; import order is not a rank; unknown or overlapping authority does not select a value; whole-term correction and split-term transfer keep prior `knownAt` answers; receipts are monotone and replay-safe; denied reads return no register payload; same-source disagreement contests; pins are emitted; native V3 acceptance is not treated as semantic proof.

The nested assignment/rule/grant binding preserves identity and historical *answers* when parts are cited with authority revision and digest. It does not give those parts an independent lifecycle. That is the disclosed 0.1.0 limit, not a silent subtype of WM-XCT-001.

Do not promote this to an authenticated service, a ControlRecord profile, or a WM-XCT-002 implementation. Remaining work is the holds above, not a rewrite of the three-type split.
