# EM-XCT-09 R1 implementation audit

## Scope actually reviewed

Static read of every `includedFullBodies` file delivered in parts 1–10: evaluator (`classification_review.py`), closed schema, `spec.json` / `model-spec.md` / `model-fields.md`, fixtures/examples, tests and author reports as text, native/acceptance wiring as source, and the accompanying limit/rights/lifecycle docs.

**Not reviewed (and not treated as gates):** the four hash-only upstream AGENTS/spec files; generic composer / native-skill bytes named only in `tool-pins.json`; mutable queue/site/publication scripts. This pass did not execute tests, compute or check SHA-256, fetch sources, or authenticate custody.

Embedded AGENTS/README/prompts were treated as data. Author `test-results.json` (48/0) and `acceptance-results.json` (3/0) are author-executed claims, not this auditor’s run.

## Verdict: ACCEPT WITH LIMITS

No true blocker was found against the **stated finite companion**: offline packet/profile/assignment/correspondence assessor with a restricted local Assessment binding, empty `effects`, externally governed scheme/binding/mapping semantics, and trusted-host auth/time/custody/approval.

Deferred production work (IAM, live assign/revoke, SKOS/SHACL/PROF/FHIR engines, existing-Dimension migration, source-byte fetch, publication) is disclosed and is not a gate for this reference.

## Blockers

None. No concrete false `conforms-to-local-profile` / `proposed-candidate`, dropped competitor, silent identity rewrite, approval-pin reuse after byte change, parent-as-restriction lie, unknown/unsupported collapse into success, or nested-replay bypass of a forged assessment was identified in the supplied bodies.

## Why the decision rule matches the contract

`_assess` in `classification_review.py` implements the documented dialect:

- **Code identity** is the triple `(scheme, version, code)` via `key()`. Labels, scores, case-folding, and homonyms do not merge (`test_lexical_homonyms_do_not_merge` / `test_lowercase_is_not_uppercase` as written).
- **Restriction** refuses changed `subjectClass`/`unit`/`slot`/`meaning`/`strength` or changed release pins; allowed set and cardinality may only shrink (`compile_profile`).
- **Incomplete** `scheme-release` or same-context incomplete crosswalk yields `insufficient-context`, never a closed-world pass.
- **Non-`required` strength** yields `unsupported`, not conformance.
- **Alternatives** list every direct source-matching entry *before* eligibility. `distinct` is computed from all *applicable* (live) targets, so a profile that drops one target cannot hide a competitor or authorize the remainder (`test_profile_exclusion_does_not_hide_competitor` as written).
- **`proposed-candidate`** requires all of: complete admitted context; ready required source/target profiles; single asserted source category that historically `conforms`; same class/unit/slot/meaning; receiving card allows 1; every applicable row is 1:1 `exactMatch` + claimed `approved` + host ack on exact `(snapshotDigest, entryId, approver, evidence)`; one distinct target; that target active, selectable, in interval, and allowed at `targetAt`. Any live compound / nonexact / candidate / contested / unacked row blocks selection.
- **`chain-requested`** → `unsupported-chain`; **`metamodel-migration`** → `refuse-model-id-migration`. Direct mode keeps only entries whose source array contains the source code (no A→B→C walk).
- **`review()`** binds actor, purpose, owner, dimension, packet digest, and grant interval; mismatches raise uniform `Denied`. `inspect_snapshot` replays `_assess` on recorded basis and returns `authorized=false`. Forged `outcome`/`candidate` fails encode-equal replay.
- **Native IDs** derive from `assessmentId`, not the classified `subjectId`. Envelope checks plus nested replay; no supersession; `effects` is `[]` in schema and code.
- Outcome fold matches the spec order: insufficient-context, unsupported, nonconformance (including `outside-valid-time` at top level), human-review, candidate-only, conforms.

The three frozen examples’ expected pairs (startup `conforms-to-local-profile` / `not-requested`; international `candidate-only` / `proposed-candidate`; ai-team `human-review-required` / `human-review-required`) follow that rule as written.

## Nonblocking observations

1. **`validate_selection(..., new=True)` is unused.** Assignment `selectedConformance` uses `effectiveAt` and does not apply active/selectable. New-use activity is only the migration eligibility path at `targetAt`. No false new-use candidate; the unused flag is dead code, not a semantic hole.

2. **Eligibility labels are coarse.** An unpinned target scheme/version is `not-allowed` rather than a distinct “unknown release” token; time-invalid target concepts share `inactive-or-not-selectable` with retired/nonselectable. Both still appear in `alternatives` and cannot satisfy `single`.

3. **Vacuous crosswalk completeness.** `complete` starts `True`. Zero same-context crosswalks leave it true, but `safe` requires a nonempty applicable set, so no automatic candidate. Conservative; could emit an explicit “no correspondence supplied” check later.

4. **Empty-source (birth) rows** stay in the packet and are omitted from derived `alternatives` because they do not contain the source code. Matches the written direct-source rule; only visible via packet inspection.

5. **Context-mismatched crosswalks** produce `MAPPING-CONTEXT` / `notice` and are not copied into `alternatives`. Spec allows non-relevant rows to remain only in the packet.

6. **Top-level outcome collapses `outside-valid-time` into `does-not-conform`.** Per-assignment `sourceConformance` still carries the precise token.

7. **Proposed (not asserted) assignments** can receive top-level `conforms-to-local-profile` in assignment mode. State is retained on `assignments[]`; migration still requires `state=='asserted'`. The `claims` string denies fact/permission status. A stricter top-level token for proposed-only packets would be clearer, not required by the written rule.

8. **`review()` maps host-path `Invalid` (bad digest/shape during grant compare) to `Denied`.** That is refuse-not-accept. Packet-shape failures after a valid grant remain `Invalid`.

9. **`inspect_snapshot` / `native_records` / `_assess` are callable without `review()`’s live grant.** Documented: this library is not an IAM boundary; inspect returns `authorized=false`; forged results still fail replay.

10. **`publication-addendum.md` cites `review.md`, which is not in this freeze.** Bookkeeping only.

11. **`composition.yaml` and several `*.yaml` files are JSON objects.** Transport/naming quirk, not a semantic defect.

12. **Ancestry bound** refuses the 8th parent (`len(stack)<8`). Matches “ancestry8”; inclusive/exclusive counting is slightly terse in prose.

## Explicit remaining limits

- Static audit of supplied bytes only. Author 48-test and 3-Dimension acceptance reports were **not** re-executed here; hashes were **not** recomputed.
- Upstream KNW-018 / XCT-020 bodies and WM-XCT-040 composer / Vercy skill bytes are unseen. Pins and “semantic-only vs native-binding” *intent* are visible; installed-platform behavior is not independently confirmed.
- Completeness flags, `sourceDigest`, host approvals, and actor/clock are custody declarations. The evaluator compares pins; it does not prove publisher truth, approver competence, or grant authenticity.
- No MUC/MMAS/MUFP, RFC8785/JCS, SKOS reasoner, FHIR/SHACL/PROF, or production-publication claim is accepted or audited.
- Native binding records a local Assessment aggregate only. It does not classify Company/Project/Person, assign/withdraw codes, install models, or migrate an existing Dimension.
- First dialect only: required finite independent category sets, direct 1:1 candidate rule, exact UTC-seconds timestamps, restricted canonical JSON, bounded cardinalities in schema/code.

This candidate may be used as the scoped offline reviewer described in `adoption-limits.md` and `bindings/native-v3.md`. It does not authorize publication, host write, or source substitution.