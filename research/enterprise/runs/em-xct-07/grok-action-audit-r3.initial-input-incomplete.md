## 1. Method, completeness table, verdict

**Actual method.** Independent static reading of the frozen pasted bundle only. No tools, browsing, execution, hash recomputation, subagents, or prior-round memory. Fragments were counted from their explicit `FRAGMENT i/n` banners; text was not treated as executable. Test JSON and acceptance JSON were treated as unverified assertions. Implementation behavior was not inferred from tests where source was missing.

**Fragment counts actually seen (required names first):**

| File | Claimed | Seen banners | Concatenable full text? |
|---|---|---|---|
| `spec.json` | 17 | **17** (`1/17`–`17/17`) | Yes (compact JSON display) |
| `action_bundle.py` | 9 | **2** (`1/9` and `9/9` only) | **No** |
| `test_action.py` | 6 | **6** (`1/6`–`6/6`) | Yes |
| `install_fixture.py` | 1 | **1** | Yes |
| `acceptance.py` | 2 | **2** (`1/2`–`2/2`) | Yes (split mid-token `afterLab` / `els`) |

**Named symbols required by the brief:**

| Symbol | Status in this paste |
|---|---|
| `Executor.dispatch` | **Missing** (no method body) |
| `Executor.lookup` | **Missing** |
| `Executor.cancel` | **Missing** |
| `Executor.observe` | **Missing** |
| `Executor._tx` | **Missing** |
| `history._validate` | **Missing** |
| `history.current_policy` | **Missing** |
| `native._verify_export` | **Missing** |
| `verify_export` (public name) | Name only, in `action_bundle.py` `9/9` `__main__` wrapper and in tests/acceptance calls |

`action_bundle.py` `1/9` is not complete source. After a short module docstring it contains the literal marker `...(truncated 50777 characters)...` and then jumps to fragment `9/9` (argparse/`verify_export` CLI). Fragments `2/9`–`8/9` are absent. `action.py`, `history.py`, and `native.py` are hash-listed and named as bundle sources, but their bodies are not supplied except via that truncated bundle.

**Verdict: INPUT INCOMPLETE.**

Exact missing parts:
- `action_bundle.py` fragments **2/9 through 8/9**
- the omitted **~50,777 characters** inside `action_bundle.py` `1/9` (ellipses replacement)
- therefore the entire executable bodies of `Executor.dispatch` / `lookup` / `cancel` / `observe` / `_tx`, `history._validate` / `current_policy`, and `native._verify_export` (and the rest of `action.py`/`history.py`/`native.py` as concatenated into the bundle)

Accepting, rejecting, or “revise-before-release” on implementation would require inferring unseen behavior from tests. The brief forbids that.

---

## 2. What can still be said without inventing the missing code

These are **input / display** findings, not implementation accept/reject findings.

**Blocker (input contract, not a code bug).** The R3 packet promised numbered complete fragments with nothing omitted. `action_bundle.py` violates that promise. The implementation under audit is exactly that generated file. Without it, R3 corrections that live in executor/history/native cannot be independently challenged.

**Not treated as code-contract violations (unseen):**
- ordered binary-search policy lookup
- request-ID native projection index
- collision checks across admin/generated IDs
- caller projection stripping of `sequence`/`controlSequence`
- history refusal of rightless replays, unreadable cancel tries, incomplete operation tails
- exact manifest/snapshot byte verification  
Those names appear in `spec.json`, tests, and the R3 cover note. Bodies were not visible.

**Visible supporting materials (usable only as spec/test/installer evidence):**
- `spec.json` 17/17, schema builder + compact schema, tests, fixtures, installer, acceptance, reports, `AGENTS.md`, `migration.md`, `review.json`
- `review.json` still says `publicationDecision: not-yet-made` and holds frozen Claude/Grok audits

Distinguish: missing source is an **audit-input failure**. Explicit fixture deferrals in the spec (no quotas, no external restore detector, no WM-XCT-040 composition acceptance, candidate/`simulationOnly` lock, finite 10,000-row store) are **documented limits**, not proven by this pass.

---

## 3. Adversarial static cases and coverage limits (bounded to visible text)

These are cases the packet *claims* to cover. They cannot be closed against implementation here.

1. Trailing newline / extra suffix on ID, token, hash, URI (`(?![\\s\\S])` in `build_schema.py` / schema; test `test_trailing_newline_in_ids_tokens_hashes_and_uris_refused`). Schema pattern is visible; executor enforcement is not.
2. Admin `add_resource` / `add_definition` using an existing `requestId` or `eventId` (`test_admin_identity_cannot_poison_existing_request_or_event`). Assertion only.
3. Caller receipt/observation omit `sequence` and `controlSequence` while privileged snapshot retains them (`test_caller_projections_omit_dimension_activity_counters`). Expected shape is visible in the test; `_public_event` is not.
4. Non-canonical manifest/snapshot bytes (float/bool `controlSequence`, trailing space with hash updated) (`test_noncanonical_manifest_or_snapshot_bytes_refused`). `verify_export` body missing.
5. Forged rightless execute/cancel try appended to a coherent snapshot (`test_forged_rightless_replay_and_unreadable_cancel_try_refused`). `validate_snapshot` body missing.
6. Incomplete operation tail (drop delivery/try/receipt or cancel/observe outcome) (`test_incomplete_dispatch_operation_fragments_rejected`, `test_missing_cancel_and_observation_outcomes_rejected`). Spec text requires refusal; validator unseen.
7. Passive lookup after `expiresAt` stays `pending`; retired-key observe is withheld (`test_passive_expired_lookup_and_retired_observe_limits`). Endpoint code unseen.
8. Capacity: 10,000-row resource/event rollback vs policy row 9,999 empty revocation reserve. Tests seed via raw SQL; `_tx` / cap checks unseen.
9. Extra coverage limit: concurrent dispatch/cancel races, `_fault` injection, and bundle-vs-source identity are asserted in JSON reports (`69` / `69`, `passed: true`) — not observed in this audit.
10. Native nested tamper: acceptance claims outer envelope still `valid` while companion `validate_native_records` raises `native-record-projection`. Nested validator unseen.

**Coverage limits of this review:** no runtime, no raw-byte hash check, no 10,000 public admissions, no hardware-fault, no host auth, no latest-history authenticity.

---

## 4. Semantic scope, five-facet coverage, field contracts, navigation, installation

**Semantic scope (from complete `spec.json`).** Two canonical objects (`ActionDefinition`, `ActionRequest`); seven Event profiles (Submission, Delivery, Try, Receipt, Disposition, Observation, KeyRetirement). Descriptive-only vs synthetic ordered-label replacement. Local SQLite transaction only. Host auth, standing, time, disclosure, isolation, rate/admission, and external continuity are assumptions. No command/network effect, distributed exactly-once, legal mandate verifier, erasure, production store, or generic WM-XCT-040 acceptance.

**Five-facet coverage.** `spec.json` `wholeObjectFacets` marks identity-class, direct-properties, recognition-observation, capabilities-behaviour-actions, and context-evidence as `required` for both objects, seven events, and supporting values (`DefinitionRef`, `Intent`, `AuthorityRuleAndScopes`, `CallerEventProjection`, etc.). That is a complete *declared* facet map. Implementation mapping is unverified.

**Field contracts (visible).** `build_schema.py` / `action.schema.json` close additional properties; ID/TOKEN/HASH/URI use end-anchored ASCII patterns; times are integer UTC seconds; labels allow order/duplicates; policy max 128 rules; Event `oneOf` by `kind`. Spec digest is explicit Python `json.dumps` (not JCS). Schema compactness for display is acknowledged; raw hashes were not recomputed.

**Navigation.** Spec statistics match the tree that was readable: 5 bundles, 10 layers, 26 findings, 52 questions, all `kind: host-guidance`. Questions are not automated authority.

**Installation (visible installer/acceptance text only).** `install_fixture.py` copies nine named assets, empty `paths` runtime, `status: candidate` + `simulationOnly: true`, new Dimension only. Acceptance claims three profiles, stored snapshot readback, outer + nested validation, nested tamper rejection, duplicate refuse. Those reports are assertions. Companion code that would perform `validate_native_records` / `export_snapshot` / `verify_export` is in the missing bundle middle.

---

## 5. Release recommendation (no authority claim)

Do not treat this paste as a complete R3 implementation audit. **Re-supply the missing `action_bundle.py` fragments 2/9–8/9 as exact UTF-8 text with no ellipses**, or supply complete `action.py` + `history.py` + `native.py` in the same numbered-fragment discipline, then repeat the static challenge on the named functions.

Until that packet is complete:
- publication decision remains what `review.json` already records (`not-yet-made`);
- test/acceptance JSON must not be used as a substitute for source;
- documented fixture limits (finite rows, host rate limits, no restore detector, candidate lock, synthetic adapter only) stay limits even after source is complete.

No publication authority is granted or withheld beyond: **this input is incomplete; implementation accept/reject is not available from the text actually supplied.**