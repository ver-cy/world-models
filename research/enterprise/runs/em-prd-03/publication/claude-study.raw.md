## Verdict

**Extend and complete WM-REC-006; keep WM-KNW-013 separate and referenced, not inherited.**

EM-PRD-03 must not be given a new root. WM-REC-006 cannot remain a `view-candidate`: it must be completed as an **aggregate root entity** — requirement identity + immutable revisions, with acceptance criteria as contained non-standalone parts. WM-KNW-013 stays the reusable formal-rule entity; a requirement's criterion **references a pinned rule revision** and never inlines or owns it. The registry signal `parent_ids: WM-REC-006` on WM-KNW-013 is wrong in direction and must be dropped in favour of the REFERENCE already recorded in adjudication. Baseline, trace link, stakeholder need, task and test case/result require separately reserved identifiers that this review cannot allocate.

## Evidence

- `specs.WM-REC-006.available: false` — no specification exists; `entry_kind: view-candidate`, `review_state: first-pass-reviewed`, `validation_flags: "не всегда standalone | resolved-kind=view-candidate"`.
- WM-REC-006 is already the **target** of two candidate REFERENCE relations (WM-ACT-032 change request; WM-OBJ-018 design realizes). A projection cannot be the stable referent of mastered trace assertions, nor own immutable revision identity. This alone forces reclassification.
- WM-KNW-013 is `entry_kind: entity`, `publishableCanonical: false`, `adjudicationStatus: reviewable-draft`, `providerMode: single-provider-waiver` (Codex only; Claude and Grok waived). Its own adjudication holds the WM-REC-006 parent signal as `held-as-reference`, pending joint boundary review.
- WM-KNW-013 already owns identity/revision/predecessor/successor, modality, applicability, predicate/operands/units/tolerance, conflict and precedence, evaluation outcomes, and an explicit "test passed ≠ compliance" boundary note. Duplicating any of this inside a requirement model would create overlap the registry does not record (`factor_overlap` 0.08–0.09).
- Gaps: no reserved identifier appears for `RequirementBaseline`, `AcceptanceCriterion`, `TraceLink`, stakeholder need, implementation task, or test result; `candidate_properties_from_v1` (PRD-04) are `candidate-not-normative`; WM-REC-006 sits in `priority_wave: 2` while EM-PRD-03 is W1 — a sequencing conflict.

## Identity and mastership

- **Requirement identity**: stable `requirement_id` in the requirement master (`Каталог продуктов`/PLM per `candidate_master_systems`); accountable owner = product lead (`suggested_owner`).
- **Revision identity**: `(requirement_id, revision_id)` where `revision_id` is a content digest over the canonically serialized normative payload — normalized text, kind, modality, criterion set, pinned rule references. Immutable.
- **Rule mastership stays with WM-KNW-013**; issuer/authority for the rule is external to the requirement owner.
- **Need mastership** is discovery; **design/feature** mastership is the engineering-design side reached via WM-OBJ-018; **task, test and evidence** mastership is external (the related contours EM-OPS-01 / EM-TEC-01 / EM-TEC-08 are the plausible homes; this must be confirmed, not assumed).

## Need/requirement/feature/task boundary

Discriminate by *who asserts*, *what changes it*, *what it may prove*:

| Artifact | Asserter | Changes when | May prove satisfaction? |
|---|---|---|---|
| Stakeholder need | stakeholder, own wording | stakeholder restates | no |
| Requirement revision | requirement authority | new revision only | it is the *subject* of proof |
| Acceptance criterion | requirement authority, part of revision | with its revision | defines decidability |
| Feature / design decision | design authority | design change | claims, does not prove |
| Implementation task | delivery authority | workflow state | **never** |
| Test case | verification authority | re-pin/new case | defines the attempt |
| Test result | execution, append-only | never (superseded only) | yes, with evidence |
| Observed evidence | observer + input snapshot | never | required support |

The need's original wording is preserved verbatim under derivation; a requirement is not an edited need.

## Rule and acceptance-criterion boundary

A **rule** (WM-KNW-013) is subject-general, authority-owned, reusable across many requirements. An **acceptance criterion** is requirement-scoped: it binds that rule revision's operands, units, tolerance and subject to *this* requirement's target, and adds `verification_method`. Criterion = `{rule_ref: (rule_id, rule_revision), binding, expected_outcome}`. If a predicate is genuinely one-off it stays inside the requirement revision and must not be promoted to a rule. Rule retirement never mutates the criterion: the pin holds and a `stale-pin` flag is raised.

## Revision/baseline semantics

- Revisions are append-only; supersession is a successor pointer, never overwrite.
- A **baseline** is a sealed, named set of exact `(requirement_id, revision_id)` pairs plus a digest over their canonical serialization, with authority and effective time. Membership is immutable after sealing; any addition, removal or revision change yields a **new baseline**.
- What a new baseline changes: membership, digest, effectivity, and which revisions are under acceptance. What it never changes: prior baselines, prior revisions, prior results, prior links.
- **Verification does not transfer across revisions.** Carry-forward exists only for entries whose `revision_id` is byte-identical, and is recorded as an explicit re-affirmation.

## Trace/conflict semantics

Trace links are first-class records with own id, asserter, time, link kind, and **both endpoints pinned to revisions** (unpinned link = invalid). Kinds carry different evidential weight: `derives_from` (need→requirement) none; `satisfied_by` (design/feature) a claim; `implemented_by` (task) **zero**; `verified_by` (test result) proof-bearing only together with `evidenced_by`.

Conflict is its own record citing two or more requirement revisions from different stakeholders. All alternatives persist and remain retrievable; resolution is an appended precedence decision with authority, rationale, scope and time, marking the losing alternative `not-selected-in-baseline-X` — never deleted, never rewritten. Only the accountable authority may change status; an engine or automation may not.

## Invariants

1. Every acceptance record cites exactly one `revision_id`, never a bare `requirement_id`.
2. A satisfaction claim requires ≥1 test result with outcome `satisfied` pinned to *that* revision, plus ≥1 evidence reference.
3. Task state — including Done — is not an admissible input to any requirement status derivation; no such path may exist.
4. Test results are append-only; a failed result stays visible in lineage after any later pass.
5. Outcome vocabulary includes `indeterminate`, `not-applicable`, `waived`; absence of a result is never a pass.
6. Sealed baseline membership is immutable; recomputed digest must match.
7. Every trace link pins both endpoint revisions.
8. Rule text is never copied without a pinned WM-KNW-013 revision reference.
9. Conflict alternatives are never removed or edited.
10. A waiver is a separate bounded record with authority, scope and expiry; it rewrites nothing.

## Scenario

**One requirement, three tasks, failed test.** `R-1@r1` in baseline `B1`, criterion `AC-1` pinned to rule revision `K@v3`. `T1,T2,T3` each `implemented_by`→`r1`; all Done. `TC-1` `verified_by`→`AC-1@r1` yields `RES-1 = violated` with evidence `E-1`.

Result: `R-1@r1` verification status = **not verified**; `B1` acceptance = blocked. Three-of-three Done changes nothing — the negative case (`Done ⇒ confirmed`) is unreachable by construction of invariant 3. After a fix, `RES-2 = satisfied` with `E-2` sets verified@`r1`, and `RES-1` remains visible in the lineage.

**Two baselines.** Tolerance change creates `r2`; `B2 = B1 − {R-1@r1} + {R-1@r2}`. Diff yields `revision-changed` for `R-1`, `unchanged` elsewhere. Consequences: `r1` verification is **not carried** to `r2`; `TC-1` is stale-pinned and must be re-pinned and re-run; `B1` remains valid and sealed. Verdict: `B1` and `B2` are not interchangeable for acceptance — only byte-identical revisions carry forward.

## Minimal completion shape

Reclassify WM-REC-006 to entity/aggregate with a full specification covering: identity, immutable revision, contained acceptance criteria, need-derivation, pinned rule references, conflict records, and status computed only from results plus evidence. Drop the WM-KNW-013 `parent_ids` signal; keep REFERENCE. Obtain registry-allocated reservations for baseline, trace link, need, task, test case/result. Resolve the wave-2 / W1 sequencing conflict. Re-adjudicate WM-KNW-013 under multi-provider review. Build fixtures for the scenario above before any readiness claim.

## Holds

No canonical completeness is claimed and nothing here is installable. Open: absence of a WM-REC-006 specification; WM-KNW-013's single-provider waiver and ten standing publication holds; unallocated identifiers for four required concepts; unverified semantic crosswalk to TM Forum SID, IDTA AAS and PLM practice; non-normative v1 field set; mastership assignments for task, test and evidence unconfirmed.
