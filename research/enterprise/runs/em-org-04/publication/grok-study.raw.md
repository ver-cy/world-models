**Verdict.** PROFILE over WM-ORG-002. No new catalogue or runtime ID. OrganizationalUnit, UnitType, UnitMandate and StructuralPlacement are named 002 constructs, not a second unit master. The org chart remains the EM-LND-01 projection. Team collectives remain WM-ORG-003 / EM-ORG-05. OUMM-style fields are reconciled by constraining 002, not by minting a parallel owner. This is standards alignment, not a W3C ORG or ISO 37000 conformance claim.

**Identity test.** Source facts: 002 already treats names as unstable and non-unique; the identifier is minted by the containing WM-ORG-001 organization and survives rename, reparenting and merger unless a continuity decision mints a new id with a lineage edge. Card invariant: renaming preserves the ID. Every unit resolves to exactly one parent *organization* for its lifetime.

The unit key is that 002 identifier. Rename updates name forms and keeps historical names. Reparent closes one StructuralPlacement interval and opens another. Reclassification changes UnitType only. Fail-to-new-ID if current name, current mandate text or current parent is treated as the key.

Merge, split, disband and transfer between 001 organizations require a reorganization *act* plus lineage edges. Continuity is an explicit decision (retain id XOR new id + predecessor/successor). Partial transfers apportion mandate and establishment across the lineage. The 001 owner link is not an axis parent.

**Mandate boundary.** UnitMandate is a temporal assignment on the unit, not the unit’s identity and not a placement edge. It owns remit and coverage (subject, geography, customer, process), delegating instrument and body, bounds (spend, signing, hiring), validity interval and sub-delegation conditions. 002 already traces mandate to a formal instrument (ISO 37000 alignment).

Mandate is placement-independent: a unit can keep the same remit across a reparent; a reparent does not rewrite remit. Changing remit is a mandate-version event. Fail if remit is stored only as the parent’s purpose, or if moving a unit silently edits mandate.

UnitType is classification against a governed scheme (department, division, cost centre, …). Repeatable and dated. Not identity. Listing “team” as a 002 type code must not collapse a 003 collective into a unit.

**Placement key / cardinality.** StructuralPlacement is a reified 002 edge. Key:

`(childUnit, parentUnit, axis, scenario, validInterval)`

Record-time and act-ref are provenance, not identity.

Tree-like axes (administrative containment, legal-entity roll-up, cost roll-up when declared as a tree): at most one parent per `(child, axis, scenario)` at any overlapping valid-time instant. Overlap of two open intervals on that key is refused. Graph-like axes (functional / professional, some reporting): multiple declared parents only if the axis profile allows them; still acyclic per `(axis, scenario, interval)`. Child ≠ parent. Self-loops refused.

The **unqualified unit-level parent field is the second write path this PROFILE forbids.** If 002 still exposes `parentUnit` without axis + scenario + interval, that field becomes a derived projection of one designated default (typically administrative + authoritative current) or is removed. Writes go only through StructuralPlacement. Dual-write of “the parent” and an axis edge is a publication blocker.

**Scenario model.** Four assertion kinds, not interchangeable.

1. **Asserted current** — authoritative as-of now; default read.
2. **Historical** — closed valid-intervals; immutable except record-time correction.
3. **Approved future** — valid-from in the future, backed by an approved reorganization act; visible in planning reads, not in current structure unless as-of ≥ effective instant.
4. **Hypothetical** — requires an explicit scenario-branch identifier. Excluded from authoritative reads. Must not leak into current or approved-future graphs.

EM-LND-01 left scenario unsupported on the landscape. This PROFILE is the unit-placement extension: hypotheticals are first-class 002 facts only when `scenario ≠ authoritative`. Landscape snapshots pin scenario + as-of; they do not own placements. An authoritative read that cannot reconstruct the requested horizon is refused.

**Team / unit distinction.** A 003 collaboration or cross-department product team cannot receive an administrative StructuralPlacement. Administrative placement is unit-to-unit containment on the administrative axis. Team members remain in their home units; the team is linked by 003 membership and optionally a functional or project edge. If the product body is *also* a standing 002 unit, dual-typing must be explicit — then it is a unit, not a 003 collaboration. W3C ORG alignment: `org:OrganizationalUnit` ≠ `org:OrganizationalCollaboration`.

Management parent never determines employer or legal entity (card invariant). Employer is a WM-ORG-005 fact bound to a 001 legal subject. Administrative, functional, legal, cost and reporting parents are independent graphs. None is inferred from another.

**Temporal and lineage rules.** Every placement and mandate carries world-time validity and record time. Axes coexist and are not unioned before evaluation. A cycle across the union of two axes is allowed; a cycle inside one `(axis, scenario, interval)` is refused. Reorganization acts carry decision, effective and record instants. Old intervals are closed, not rewritten.

**Scenario results.**

*Negative — product team forced under one administrative parent.* Team T has members from units A and B. Writing T as administrative child of A falsifies A/B containment and invents a single tree parent. Correct: T is a 003 team; members keep placements in A and B; optional project-axis coordination; no administrative parent for T.

*Acceptance — as-is / to-be reorganization.* As-is = authoritative placements valid at \(t_0\). To-be = approved-future (or named branch) placements valid at \(t_1\), produced by a reorganization act with lineage. Cycle check runs inside the selected `(administrative, scenario, interval)` only, not across as-is ∪ to-be. Authoritative current read at \(t < t_1\) returns as-is. Old mandates, staffing and 003 membership persist via closed intervals. Contaminating current state with to-be edges fails the card.

**Required profile constraints.** Unit ID survives rename and reparent. Merge / split / disband require act + lineage. UnitType ≠ identity. Mandate ⊥ placement. Placement key includes axis + scenario + interval. No unqualified parent write path. Single parent only within tree-like axis/scenario/time. Acyclicity per axis/scenario/interval. Hypothetical needs an explicit branch and is excluded from authoritative reads. 003 teams cannot take administrative placement. Management parent ≠ employer / legal entity. EM-LND-01 remains the projection; 002 remains the unit master.

**Publication blockers.** 002 is a non-canonical reviewable draft; source and live-version pins remain open. 002 still describes “one parent unit within a given hierarchy” without a first-class StructuralPlacement key or a named scenario field — PROFILE text must land before dual-write of an unqualified `parentUnit` can be closed. “Team” remains a 002 type-code leak against 003. No executable fixtures for: rename/reparent identity stability; mandate unchanged across reparent; refused admin placement of a 003 team; as-is/to-be cycle check that does not contaminate current state; acyclicity per axis with a legal cycle across the union. Alignments to W3C ORG and ISO 37000 are alignments only. Do not invent OrganizationalUnit, UnitMandate, UnitType or StructuralPlacement runtime identifiers.
