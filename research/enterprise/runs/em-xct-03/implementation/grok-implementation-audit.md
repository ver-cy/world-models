# Enterprise Assertion Provenance 0.1.0 — frozen implementation audit (EM-XCT-03)

**Verdict: ACCEPT WITH LIMITS**  
**Publication authority: not granted.** This is an implementation review of a bounded original companion. It is not parent/PROV/SLSA/DQV/in-toto/OpenLineage conformance, not a publication decision, and not ratification of the synthetic `publicationStatus: "published"` field inside `acceptance.py`.

Team consensus (Grok, Benjamin, Harper, Lucas): no stated invariant I01–I16 fails under the documented host assumptions (caller authentication, current root/configuration, receipt clock, no concurrency). Several operational edges are real and must be treated as limits, not as “corrections still work.”

---

## Input completeness and truncation

| Marker | Status |
|---|---|
| `END OF PART 01-contract` | present |
| `END OF PART 02-code` | present |
| `END OF PART 03-native` | present |
| Final sentinel `AP-FROZEN-IMPLEMENTATION-20260921` | present |

The three supplied parts are not internally truncated. Prompt size (“73,286 characters”) vs attachment size (73,298 bytes) is a counting mismatch only; no section is missing from the three parts.

**Not in evidence (explicitly omitted; not reviewed):**
- `spec.json` Bundle → Layer → Finding → Question → Artifact → Action tree (only a four-bundle / eight-layer / twenty-route summary)
- `tool-pins.json`, `examples/*.json`, upstream WM-XCT-012 files
- per-type whole-object facets, rights, migration, primary-source/crosswalk material
- file SHA-256 values listed in the prompt (not recomputed)
- tests and native acceptance (reported as executed locally; this audit only statically traces)

Missing semantic context is left unknown. No omitted file is treated as reviewed.

---

## What holds (static trace)

Under a trusted host that authenticates the actor, supplies `now`, and presents the complete current root:

- External claim pins are stored as `(id, revision, digest)` only. `view` always returns `truth: "not-evaluated"` and `permissions: "not-inferred"`. `context-available` is “an active non-unverified account exists,” not a rely verdict (I03, I06, I07, I10).
- `epistemicKind` is an identity anchor. A review Activity plus `ConfidenceAssessment` cannot rewrite `inferred` → `observed`. The ai-team fixture keeps the inferred account and attaches a separate `limited` assessment (I05, I09, I15).
- `view` calls `gate(config, actor, purpose, now)` before any ledger, claim, or `knownAt` diagnostic. `test_read_denied_before_malformed_input` traces as `Denied("Read denied")` on `{SECRET: bad}` / `claim=None` / `knownAt='bad'` (I11).
- Internal refs resolve only in `prior` (already-admitted rows). The new row is not yet in `prior`. Receipts must strictly increase at second resolution. Self-pin fails as an unresolved exact pin (I08).
- New reliance must pin an active current head. Historical rows that already named an older revision remain in the ledger. Withdrawal skips `semantic()` and freezes content to `{revision, previousDigest, recordedAt, writer, state, change, reason}` (I02, I04, I09).
- Replay of identical `(id, revision)` ignoring only a restamped `recordedAt` returns the previous ledger (first receipt kept) after rechecking current grants and `recordedAt == now`. Conflicting payload → `Invalid`. Removed grant → `Denied` (I13).
- `validate_extension` requires equal headers and `candidate.records[:len(previous.records)] == previous.records`. Truncation and rewrite fail (I04, I13).
- Companion identity is `vr.profile.enterprise-assertion-provenance` with binding text “Own companion namespace/specification; no parent subtype.” Parent `vr.wm-xct-012` is semantic-only. Acceptance digest-checks the installed companion against its own binding. Native envelope can remain valid while companion `validate_ledger` rejects a poisoned nested snapshot (I12, I16).
- Scheme pin is `{id: urn:vercy:scheme:qualitative-reliance, revision: 1, digest(encode(SCHEMA['x-confidenceScheme']))}`. Numeric labels are schema-rejected (I10).
- Same-version `import_snapshot` / `migrate` round-trip; any other target version is refused (I14).

Host authentication, latest-root discovery, and concurrency remain outside this reference, as specified.

---

## Severity-ranked defects and limits

### HIGH — operational contract tension (not an I-invariant collapse)

**H1. Current-head rule applies to corrections whose immutable pins still name a now-superseded revision.**

`semantic()` → `resolve()` requires `target['state']=='active' and pin(heads[p['id']])==p` for every non-withdraw row. `EvidenceLink.evidence` and `ConfidenceAssessment.account` are identity anchors, so a correction cannot retarget them. Selector/rationale and label/basis are *not* anchors, so the spec’s “corrections retain versions / explicit revisions” path still runs `semantic()` and is rejected once the cited pin is no longer the head.

Reproducible sequence (synthetic IDs):

1. `admit` Capture `C` rev1 (captured file, digest present).
2. `admit` EvidenceLink `L` rev1 with `evidence = pin(C rev1)`, `relation = cites`.
3. `admit` a correction of `C` to rev2 that only changes `integrity` to `mismatched` (allowed: `integrity` is not a Capture anchor).
4. `admit` a correction of `L` that only changes `selector` or `rationale` and keeps `evidence = pin(C rev1)`.

Result: `Invalid("New link to inactive or superseded revision")`.

Same trap for assessments:

1. Account `A` rev1 → review Activity `R` with `inputs = [pin(A rev1)]` → `ConfidenceAssessment` pinning `A` rev1 and `R`.
2. Correct `A` to rev2 (e.g. notes/limitations; `epistemicKind` cannot change).
3. Correct the assessment label/basis, or try to admit a new assessment of `A` rev1: rejected (not current head).
4. Try to reuse `R` for `A` rev2: rejected (`A` rev2 is not in `R.inputs`; Activity `inputs` are anchors).

Operators must mint a **new** EvidenceLink id, or a **new** review Activity of the live account revision. Withdrawal still works because `semantic()` is skipped. `validate_ledger` of an already-admitted historical chain still passes, because `heads` is rebuilt in receipt order.

This is I02/I08/I09 implemented strictly. It is **not** “in-place metadata correction still works after the target moves.”

**H2. Write path can leak `Invalid` vs `Denied` to an unauthorized caller.**

`admit` order: `config_check` → kind/schema `validate` → writer-grant check. An unauthorized actor submitting a closed-schema violation (`password: secret`, unknown kind, bad pin) gets `Invalid("Schema mismatch")` / `Invalid("Unknown record type")` rather than `Denied("Write denied")`.

`view` does gate first; I11 holds on the read path. Spec/AGENTS require the host to return only a receipt or generic rejection to write-only callers. The library does not wrap that. Combined with H2’s sibling M2 below: `admit` also **returns the full candidate ledger**.

---

### MEDIUM — concrete edges

**M1. Independence signal is only shared `representationDigest` or `originRef` among active accounts.**

`view` sets `independence.status` to `known-shared-origin` iff two or more active accounts for the exact claim pin share a non-null digest or declared origin in their transitive Capture closure; otherwise `unknown`. It never emits “independent.”

The group fixture keeps the default digest `sha256:`+`c`×64 and default `originRef`, and only changes `sourceRef`. Distinct digest+origin stays `unknown`. Matches the spec (“overlap signal, not authenticated historical provenance”) and is easy to over-read as source-copy independence.

**M2. `admit()` returns the full ledger.**

Docstring: host-internal; do not expose ledger/diagnostics to a write-only client. No receipt-only API is implemented. Host obligation, not an invariant break.

**M3. Acquisition modes require all inputs to be matching captured Captures.**

Spec prose: file-acquisition uses “at least one” captured file Capture; live-observation uses captured live-api Captures about `observedTarget`. Code:

```text
require(bool(inputs) and all(x['kind']=='Capture' for x in inputs))
require(all(x['mode']==mode and x['availability']=='captured' for x in inputs))
```

Tighter than “at least one,” not looser. Mixed Capture+ProvenanceRecord inputs are legal only for synthesis/review/proposal. No extra epistemic permission is created.

**M4. Versioned pin DAG is acyclic; unversioned ID graph is untested.**

`ProvenanceRecord.activity` is not an anchor. Sequence: `A` rev1 → later synthesis `S` with `inputs=[pin(A rev1)]` → correct `A` so `activity = pin(S)`. Pin-graph is `A` rev2 → `S` → `A` rev1 (backwards in receipt order). `closure` keys `(id, revision)`, so `view` does not loop. I08 as written holds. Code does not reject “new activity inputs contain an older revision of this same id.” Untested. Not a self-reference of the same `(id, revision)`.

---

### LOW — documented bounds (not defects)

- **L1.** `config_check` can raise `Invalid` / `Denied("Access denied")` on bad config or malformed `now` before the reader allow-list. Trusted-host configuration is assumed.
- **L2.** `import_snapshot` / `validate_ledger` check consistency, not historical authorization. `validate_extension` cannot see a skipped newer root when `previous` is still a prefix. Stated in the spec.
- **L3.** Native V3 envelope validates storage shape only. Companion `validate_ledger` is mandatory for nested snapshots. acceptance.py traces: poison `representationDigest` → native `valid` + companion `Invalid`; truncated snapshot → `validate_extension` `Invalid`.
- **L4.** Only the bundled qualitative-reliance scheme. No numeric conversion, averaging, or cross-scheme mapping.
- **L5.** Serial one-record-per-second clock; host-supplied `now`; no fetch, IAM, PKI, signature verifier, or durable concurrency.
- **L6.** Runtime `modelId` / `objectType` / binding stay on `vr.profile.enterprise-assertion-provenance`. Parent is a semantic reference, not a subtype. Current runtime entry uses its own digest; it does not impersonate WM-XCT-012.
- **L7.** `publicationStatus: "published"` in acceptance.py is synthetic candidate-installation metadata. `researchAssurance` remains `reviewable-draft`. This audit does not convert that into publication authority.
- **L8.** `context-available` includes `proposed`. Explicitly not a ready-to-rely verdict.
- **L9.** URIs are stored opaque; no resolve/normalize/alias merge.
- **L10.** Scheme pin is computed at import from the schema sidecar (`SCHEME = digest(SCHEMA['x-confidenceScheme'])`). Process-local. If a host swapped schema without assessments, every assessment would reject. I10 working as designed.

---

## Tests traced (not executed)

`test-results.json` reports `testsRun: 48`, `failures: 0`, `errors: 0`, `passed: true`. Methods traced against that count:

| Area | Tests traced |
|---|---|
| Fixtures | `test_three_profiles` (startup / group / ai-team) |
| Truth / permissions | `test_no_truth_or_permission_inference` |
| Independence | `test_shared_origin_not_independence`, `test_distinct_roots_remain_unknown` |
| Kind vs review | `test_review_does_not_promote_inference`, `test_citation_has_no_support_default`, `test_file_cannot_be_live`, `test_inference_cannot_be_observation`, `test_live_declaration_positive`, `test_observed_target_mismatch` |
| Gates / rights | `test_wrong_actor_denied`, `test_missing_write_grant`, `test_write_rotation_preserves_attribution`, `test_read_denied_before_malformed_input`, `test_purpose_gate`, `test_expired_config` |
| Replay / receipts | `test_replay_retains_receipt`, `test_replay_rechecks_rights`, `test_conflicting_replay`, `test_receipt_spoof`, `test_non_monotone_receipt` |
| Correction / withdraw | `test_corrective_impact_and_past_knowledge`, `test_withdrawal_preserves_external_claim`, `test_withdraw_dependent_after_input_withdrawn`, `test_terminal_withdrawal`, `test_reject_withdrawal_content_change`, `test_source_pin_is_immutable` |
| Pins / graph / time | `test_no_auto_carryover_to_new_claim`, `test_nested_pin_required`, `test_no_future_or_self_reference`, `test_cross_scope_link`, `test_new_reliance_on_superseded_revision_rejected`, `test_bad_calendar`, `test_activity_clock`, `test_input_cannot_follow_synthesis_event`, `test_future_knowledge` |
| Snapshot / schema | `test_prefix_rewrite_and_truncation`, `test_dimension_header`, `test_schema_closed`, `test_unknown_kind_and_nonrecord`, `test_no_numeric_confidence`, `test_assessment_scheme_and_review`, `test_import_roundtrip_and_lossy_refusal`, `test_rejection_does_not_mutate` |
| Context | `test_unknown_empty_register`, `test_author_observer_asserter_recorder_separate`, `test_unverified_requires_limitations`, `test_unknown_and_unavailable_are_explicit` |

Native summary traced (not executed): three profiles (startup, group, ai-team); fixture admission replayed through the installed companion digest; `validate_extension` rejects truncation; native remains valid on a poisoned nested snapshot while companion `validate_ledger` rejects it.

No traced test exercises H1 (metadata-only correction of a link/assessment *after* its pinned target moved) or M4 (activity retarget onto a later synthesis of an older revision of the same account id).

---

## Evidence and truncation limits

- Static reading of the three supplied parts only. No search, fetch, execution, hash recomputation, or artifact mutation.
- SHA-256 banners in the prompt are unverified claims.
- `spec.json` and the rest of the package tree are outside this review.
- Local “48 passed / 3 native profiles passed” figures are taken as reported, not reproduced.
- Host authentication, current-root freshness, and concurrent writers are outside the pure reference; this audit does not claim they work.
- Synthetic examples only. No claim about actual organizations, sources, or proposition truth.

---

**ACCEPT WITH LIMITS.**  
Do not treat this companion as a published parent profile, as a truth engine, or as a substitute for host admission wrapping. Operators who need selector/label edits after a cited revision moves must open a new link or a new review Activity; they must not assume an in-place correction will admit.
