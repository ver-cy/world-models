## Verdict
**Conditional accept.** Reclassify reserved WM-REC-006 from view-candidate to a Requirement aggregate with stable identity and immutable revisions. Contain Acceptance Criterion, Requirement Baseline, and revision-pinned Trace Link records without new catalogue IDs. Reference WM-KNW-013 by exact revision and retire its candidate parent signal. Keep need, feature/design, task, test/result, evidence, waiver and decision in external masters. Task Done never proves satisfaction; failures stay visible.

This is a boundary decision, not a completed model. WM-REC-006 is an unversioned TODO stub: “Candidate governed context model for Requirement; boundary questions remain required.” No spec.yaml exists. EM-PRD-03 research is queued; `boundary_decision` remains pending. Do not treat this review as publication readiness or canonical completeness.

## Identity / mastership
WM-REC-006 / `vr.wm-rec-006` already occupies the Requirement slot (INF.REC.REQ). Completing that reserved identity is reuse, not a new mint. Identity priority, once written: authoritative requirement-system identifier, then governed IRI, then Dimension UUID/ULID. Title, ticket, filename and requirement text are not identity.

Mastership is field-level. The Requirement aggregate owns statement, classification, revision lineage, contained AC set, outbound pinned traces, and the RM baseline collection. Copies in product catalogue, discovery or PLM remain projections. Equal-authority conflict is recorded, not overwritten.

WM-KNW-013 already publishes a non-owning REFERENCE to WM-REC-006 and holds parenthood: a requirement may source a rule, but rules also originate in policies and standards. Retire the parent signal; keep REFERENCE pinned to an exact WM-KNW-013 revision. Same pattern as WM-KNW-014’s withdrawn CHILD to WM-ACT-021.

## Boundaries
**Contained (no new model IDs):** Acceptance Criterion; RM Requirement Baseline as a collection artifact of this model; outbound Trace Link records whose source is a requirement revision. Contained records live in the requirement namespace plus type sub-namespace plus ordinal, as in WM-KNW-014 artifacts. They are not independently addressable in the catalogue namespace.

**External masters (do not absorb):** stakeholder need; feature/design (EM-PRD-01, EM-TEC-01); task/work order (EM-OPS-01, WM-ACT-007); test/result (EM-TEC-08, WM-SFT-015); evidence (WM-XCT-028); waiver/exception; decision; enforcement; reusable Rule (WM-KNW-013). WM-KNW-014 already requires a REFERENCE to a requirement/norm model and states that authoring, versioning and baseline control stay there.

Collision note: WM-ACT-007 already carries work-order acceptance-criteria findings. Those remain work-order local. Requirement AC is the satisfaction clause of a requirement revision, not a work-order field.

## Rule / criterion split
Keep them apart.

- **Rule (WM-KNW-013):** reusable formal or formalizable predicate — operands, units, tolerance, evaluation contract — with its own immutable revisions. One rule may serve many requirements, policies or standards.
- **Acceptance Criterion:** first-class contained record of one requirement revision. It binds one or more pinned Rule revisions, or a local informal condition, to *this* requirement’s pass/fail obligation.

Do not collapse AC into Rule. For a tolerance change: if the threshold lives in a reusable predicate, mint a new WM-KNW-013 revision and re-pin; if it is local only, revise the AC and the requirement revision and leave the Rule pin unchanged. Never mutate a pinned Rule. Syntax validity, rule evaluation, AC satisfaction, verification, conformance, compliance and accountable decision remain distinct claims.

## Revision / baseline
Requirement identity is stable. Each revision is immutable (statement + AC set + Rule pins + outbound traces). Acceptance pins a revision. Supersession does not overwrite.

A Requirement Baseline is a frozen *set* of requirement revisions plus their AC and Rule pins, with purpose and approval. It is not a synonym for one revision. WM-XCT-022 covers per-object history; it does not replace baseline compare.

**Challenge — does baseline already need its own model?** Not now, and not by allocating a new WM-ID. No published independent Baseline model was found. Containment is coherent if baseline is a *collection artifact of the Requirement model* (population-level), not a child of a single requirement instance. Treating baseline as a per-requirement child fails the card scenario (compare two baselines after a tolerance change). A product/CM baseline that also pins design, test and evidence is configuration management, not this aggregate; smuggling it in would break external mastership. Flag as a later CM/XCT question. Do not invent an identifier.

## Trace / conflict
A revision-pinned Trace Link can live as a contained record: one owned endpoint (requirement revision) plus an external endpoint. Link presence does not prove satisfaction. Unpinned traces are not baseline-eligible.

Conflicts that must remain explicit: suspect link after either end revises; Done tasks versus a failed test; waiver versus open failure; two baselines naming the same requirement identity at different revisions; competing satisfy/verify claims. A conflict does not erase the alternative.

**Challenge — does trace already need its own model?** Not for this increment. No published independent Trace Link model was found. WM-XCT-036 is alias/same-as, not RM trace. Inbound traces from test, issue and design already exist as those models’ REFERENCE edges. A shared bidirectional fabric queried with no requirement endpoint would be an XCT question later. Do not allocate a Trace model ID here.

## Invariants
1. Requirement identity is stable; revisions are immutable; change yields a new revision.
2. Acceptance pins a requirement revision.
3. AC ≠ Rule ≠ Test ≠ Task. AC is contained and bound to a requirement revision.
4. Reusable Rule is cited by exact WM-KNW-013 revision.
5. Task Done does not prove AC satisfaction or requirement satisfaction.
6. Failed test/result remains visible on the pinned trace; baselines do not hide it.
7. Need, feature/design, task, test/result, evidence, waiver and decision remain external; only typed revision-pinned refs live here.
8. Baseline compare is identity-preserving: B1 is not rewritten when B2 is taken.
9. Contained AC/baseline/trace identifiers are requirement-scoped, not catalogue IDs.
10. This model declares expected behaviour; evaluation and enforcement live elsewhere.

## Scenario
Use fixture-local labels only.

R@rev1 carries AC1 (tolerance X) and traces to tasks T1, T2, T3 (all Done) and test F (failed). Satisfaction stays unsatisfied or inconclusive. Three Done tasks do not prove R. B1 freezes R@rev1 + AC1 + pinned traces, including F-failed.

Tolerance change produces R@rev2 + AC2 (tolerance Y), and a new Rule pin if the threshold lives in WM-KNW-013. B2 freezes R@rev2 + AC2. B1 remains readable and unchanged. Diff(B1, B2): same requirement identity, new revision, AC/tolerance/rule-pin delta; the prior failed result stays visible against B1 and must be re-evaluated for B2. Any waiver is an external record, not a silent pass. The negative case — ticket Done auto-confirms linked requirements — is rejected by invariants 5 and 6.

## Blockers
- WM-REC-006 has no written specification; this review audits a proposal against neighbours, not a completed card.
- Relation-ledger write is required to retire the WM-KNW-013 parent signal; prose is not enough.
- Collection-versus-child tension on Baseline must be stated in the boundary note or implementers will store baselines as per-requirement children.
- Rule-versus-AC ownership of tolerance must be explicit before the scenario is executable.
- Need versus Requirement remains an open card question; WM-KNW-013 still slurs “need or governed requirement record.”
- WM-ACT-007 AC collision needs a published boundary note.
- External task, test, evidence, waiver and decision masters are named, not shown complete; the satisfaction graph is distributed across EM-OPS-01, EM-TEC-08, EM-PRD-01 and EM-TEC-01.
- WM-KNW-013 is a reviewable draft (`publishableCanonical: false`); exact-revision cite is a required relation, not a confirmed pin.
- Fixtures, field-level mastership map and at least the card’s three invariants plus identity/time/disclosure constraints are still owed before any publication-candidate claim.

No identifiers were invented. No completeness is claimed.
