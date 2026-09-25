## Verdict

**PROFILE.** EM-LND-01 is a viewpoint over existing model content, not a new model. It gets no new registry ID. Host it as a view profile on `vr.wm-org-002` (`vr.wm-org-002#profile/landscape-organizational-structure`), referencing WM-ORG-003, WM-ORG-004 and WM-ORG-016.

None of the three candidate types survives an identity/lifecycle test:

- **StructureSnapshot** is already WM-ORG-002's `structure-as-of-view` artifact — serial, keyed by `structureVersionId` plus the world-time/record-time pair, anchored by `contentDigest`, produced by `reconstruct-structure-as-of`. A sibling type would be a second source of truth for the same state.
- **StructureAxis** is already WM-ORG-002's named-hierarchy construct: `hierarchyIdentifier` with purpose, owning role and default flag (`q-hierarchy-inventory`), plus `reportingLineType` and `de-hierarchy-edge` qualified by hierarchy and validity. Axes have identity and an owner *inside WM-ORG-002*; the profile widens the register's subject range, it does not mint the concept.
- **OrganizationLandscape** has no state of its own. Every field it would carry is either a query parameter (`as_of`, `structure_kind`, `boundary`) or derived (`hierarchyPath`, occupancy, vacancy). `candidate_properties_from_v1` is marked `candidate-not-normative` throughout, and the only field with no host anywhere is `scenario` — which is handled below as a held extension, not as a licence to mint.

Not REUSE ONLY, because three things are genuinely unexpressible today: a cross-model axis register (units, teams, posts and assignments each own part of one axis); axis-scoped rather than globally quantified cardinality; and a composed as-of view whose determinism spans four models with four independent reconstruction horizons.

## Boundary

The landscape is a deterministic projection: `f(axis set, world-time, record-time, root, depth, disclosure class) → digest-identified view`. Its inputs are WM-ORG-002 units/hierarchy edges/reporting lines, WM-ORG-003 team nodes and nesting, WM-ORG-004 posts and post-to-post `reports-to`, WM-ORG-016 assignments and `reports_to_ref`. It asserts nothing: no unit, team, post, assignment, person or edge originates here. Writes go to the owning model's write path (`apply-reorganization-act`, `record-structural-change`, `amend-or-reclassify-position`, `amend-assignment`); the profile forks none of them.

Consequences the profile must state: the landscape is not authority. WM-ORG-002 records informal/shadow structure and de facto reporting as an open gap, so the view shows asserted edges only. Vacancy stays derived (WM-ORG-004 `inline_only_rationale`) and is never stored on the view. Segment determination (IFRS 8) and statistical units stay out.

## Axis and snapshot semantics

Four axes, each a separately governed edge set with its own subject type and rules:

| Axis | Subject | Source | Cardinality | Cycles |
|---|---|---|---|---|
| Administrative | unit → unit | WM-ORG-002 `hierarchyEdge` (managerial) | exactly one parent per unit per validity interval | forbidden |
| Functional/professional | unit or post → unit or post | WM-ORG-002 `reportingLine`, type=functional, dotted | many permitted; `overlap-permitted` true | forbidden |
| Project | agent → team, team → team | WM-ORG-003 membership + parent/child | membership many-to-many; team nesting ≤1 parent, or forbidden where the profile is Scrum/secret | forbidden in nesting; inapplicable to membership (bipartite, not a hierarchy) |
| Supervisory | post/agent → post/agent | WM-ORG-004 `de-reports-to`, WM-ORG-016 `reports_to_ref` | one supervisor per assignment per axis per interval; `reporting_line_type_code` precedence resolves conflicts | forbidden |

Acyclicity and single-parent are asserted per axis, never over the union — that is the substance of "cycle forbidden only where hierarchy is required". Any axis whose subject is a *unit* must emit WM-ORG-002's `standardExtensionNote`: `org:reportsTo` binds Agents and Posts, so unit-level reporting publishes as a declared non-conformant extension with a mapping rule.

Snapshot semantics: one `(world_time, record_time)` pair applied uniformly to all four models; assertion-level bitemporality exists in WM-ORG-002 (`validFrom`/`validTo`/`recordedFrom`), WM-ORG-004 (effective windows plus record instants) and WM-ORG-016 (`effective_start`/`effective_end` plus `record_created_at`). Future reorganization needs no new machinery: `apply-reorganization-act` with a future `effectiveTimestamp` plus reconstruction at future world-time and *current* record-time yields the post-reorg view, while the same record-time at today's world-time yields the pre-reorg view. Scenario is a different thing and is not supported (below).

## Required profile

1. Cross-model axis register: axis id, subject type, source model and element, owning role, cardinality rule, cycle rule, overlap policy, default-display flag, CODM flag where applicable.
2. Composed view parameters: axis set, world-time, record-time, root, max depth, disclosure class, `scenario` fixed to `authoritative` until the extension lands.
3. Composed view identity: constituent `structureVersionId`s and per-model content digests plus one digest over the canonical composed serialisation. Dates are never identifiers.
4. Reference-only rule: Person and Unit appear as `{model_id, identifier, scheme}` plus display label; no personal master data, no copied unit attributes; loss manifest declares omissions.
5. Loss/fidelity manifest and non-reimportable marking, per `derive-org-chart`.
6. Validation binding to `validate-structure-graph` with the axis-scoped rule set version recorded on every view.
7. Disclosure: suppression parameters supplied here, grants issued by S2; audit facets by S4.

## Invariants

1. Every edge carries an axis id and a world-time interval; unqualified edges are rejected at write time.
2. Cardinality and acyclicity are evaluated per axis per interval; a violation on one axis never invalidates another.
3. Person and Unit are referenced, never copied; a view containing person attributes beyond the declared label set fails.
4. Views are immutable, digest-identified and reproducible; regeneration produces a new serial instance.
5. A view is refused, not degraded, when either instant falls outside the narrowest reconstruction horizon among the four models.
6. Scenario-marked facts never appear in an `authoritative` view, and vice versa.
7. Acting cover substitutes within a supervisory interval; it does not add a second edge on that axis.

## Scenario walkthrough

**Negative — matrix assignment.** Person P holds WM-ORG-016 assignment A1 (post in unit U, supervisor S1) and A2 (project team T, supervisor S2). Under the contour's globally quantified single-manager rule, A2 is rejected. Under the profile, S1 is a supervisory-axis edge and S2 a project-axis edge: no violation, because cardinality is axis-scoped and `overlap_policy_code` is evaluated within an axis. The rule fires only if S1 and S2 are both asserted on the *supervisory* axis over overlapping intervals; then WM-ORG-016's precedence rule resolves or `validate-structure-graph` blocks. The contour invariant is mis-quantified and must be rewritten per axis.

**Acceptance — three axes plus future reorganization.** Administrative, project and supervisory axes over P's A1 and A2, with a reorganization act effective 2027-01-01 reparenting U. Three views at record-time now: 2026-09-26 (pre-reorg), 2027-01-02 (post-reorg), and 2027-01-02 at record-time 2026-12-01 (what was believed then). All three reproduce deterministically, each digest-identified, each showing P once per axis with no duplicated Person record — one history, three consistent views.

## Gaps and publication holds

- **Scenario is unsupported.** No model carries a branch dimension; `scenario` is non-normative. Needs a scoped EXTEND on WM-ORG-002 assertions and WM-ORG-016, or an explicit decision that alternatives live in a planning model. Publication hold until decided.
- All four models are `publishableCanonical: false` / `reviewable-draft`; the profile inherits that ceiling and must pin all four `synthesisSha256` values as immutable refs.
- Crosswalk evidence for WM-ORG-002/003/004 is `index-and-publication-metadata` only; only WM-ORG-016 is boundary-reviewed. Semantic crosswalk unconfirmed.
- Axis register cannot close while WM-ORG-002 defers ERP cost/profit/funds-centre hierarchies and the unit↔site association.
- WM-ORG-003 `team-hierarchy-snapshot` is keyed by observation time alone (single-clock artifact identity) though `observed_at`/`event_time` exist at assertion level — reconstruct from assertions, not from that artifact.
- Conflicting nesting vocabularies (Scrum prohibition, one-parent, nested groups) publish side by side as declared profile constraints; do not merge.
- Inherited WM-ORG-002 holds: ISO clause text unverified, unit-grain staffing extension-grade, private-sector matrix forms unvalidated, EU/US regional scope must be stated.
- Registry: no ID allocated and none required; the contour's blocking decisions on source mastership, immutable refs and fixture checks remain open.
