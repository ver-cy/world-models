## Verdict

**PROFILE.** EM-ORG-04 does not prove an independent identity or lifecycle for `OrganizationalUnit` separate from the reserved WM-ORG-002: the reserved model already owns unit identity, kind classification, containment, mandate, establishment, reorganization acts and bitemporality, and EM-ORG-04's four candidate types map onto it without residue at entity grain. A new model candidate is not justified; nor is the reserved model incomplete in the "COMPLETE RESERVED MODEL" sense, since its layers exist and are populated. What is missing is one qualifier dimension (scenario/branch) and a set of enforcement rules that the reserved model states as questions rather than constraints. That is the shape of a narrow Enterprise profile over WM-ORG-002, not a second owner of `unit`. No canonical status, approved relation or installability is claimed here.

## Evidence state

The spec is pinned by digest (`9e3e80da…`, 250,855 bytes) and parsed; the reviewer projection is a selected subset of 28 findings. Publication metadata is self-limiting: `status: published` but `adjudicationStatus: reviewable-draft` and `publishableCanonical: false`, version `0.3.0-research.1`. The registry reservation carries `status: described-previous-version`, `review_state: migration-boundary-review`, and a source date (2026-08-22) earlier than the spec's `generatedAt` (2026-08-23) — a reconciliation item, not a defect finding. The EM-ORG-04 → WM-ORG-002 link is `conceptual-candidate` at `index-and-publication-metadata` depth; both ledger relations are `review_state: candidate`. Seven publication holds are open, including unverified live source versions and paywalled ISO clause text underlying the delegation and segregation findings. Enterprise v1 fields are non-normative. Nothing below should be read as clearing those holds.

## Identity and aggregate boundary

Unit identity passes the separation test in the reserved model: `unitIdentifier` + `unitIdentifierScheme` are mandatory and parent-scoped (ROR explicitly declines to identify subdivisions), names are declared non-identity with aliases and historical names, and `unitStatus` separates "ceased" from "created in error". Identity is therefore independent of name, of mandate and of any placement — the profile only needs to make the identifier-stability question ("does the identifier survive rename, reparent, merger?") a fixed answer rather than an open question.

`UnitType` is not an entity: the reserved model already renders it as `unitKind` against a versioned `classificationScheme`, multi-valued. Do not mint it.

`UnitMandate` is **a temporal assignment, not intrinsic and not an independent aggregate**. Evidence: `mandateValidity` as a period, `assign-unit-mandate` as attach/withdraw over an interval, delegation traced to an instrument, and ISO 37000's requirement that delegation be formalized. It has no identity apart from the (unit, instrument, interval) triple and no lifecycle independent of the unit, so it stays a reified assignment inside WM-ORG-002.

## Placement/axis/scenario contract

`StructuralPlacement` is likewise not a new model: `hierarchyEdge` is already "a parent-child edge qualified by hierarchy identifier and validity period", with `hierarchyIdentifier` required `1..n` and managerial, legal, cost and functional hierarchies kept as separately governed edge sets. Axis coexistence without overwriting is therefore supported today.

Two defects remain. First, `parentUnitRef` (`0..1`) sits on the unit record alongside the edge collection, creating a second, unqualified write path that silently privileges one axis; `hierarchyPath` is derived from it. Second, there is no scenario qualifier anywhere. Asserted-current and historical-as-of are handled by valid-time plus record-time; approved-future is handled by a future `effectiveTimestamp`; **hypothetical scenario is unsupported** — a to-be structure can only be expressed by asserting it, which contaminates `validate-structure-graph`, `reconstruct-structure-as-of` and `derive-org-chart`.

## Mandate and authority

Keep the reserved model's framing: remit statement plus coded purpose, bounded `authorityLimit` objects as first-class data, `headPostRef` to WM-ORG-004 with `headshipState` for acting/vacant, and segregation rules with time-bounded waivers. The profile should add nothing structural here, but must not publish the delegation/segregation material as normatively sourced while the ISO hold stands. Mandate must be placement-independent: a unit's remit is not derived from, and does not change with, its administrative parent.

## Temporal/reorganization rules

`apply-reorganization-act` carries decision, effective and record instants with `affectedUnits`, closes and opens validity intervals and writes lineage; `predecessorUnitRefs`/`successorUnitRefs` plus `lineageActRef` express many-to-many merge and split; tombstones are retained through `apply-disposition`. Rename and reparent therefore preserve identity by construction, and merge/split/disband produce explicit lineage. The gaps are narrow: the open question on gaps/overlaps between successive parent assignments must be closed as a rule, and the ChangeEvent conformance threshold (accepted in adjudication) must prevent every rename being over-claimed as `org:ChangeEvent`.

## Invariants

Proposed as profile-level, testable constraints (labels illustrative, not assigned identifiers):

1. A placement is valid only as an axis-, scenario- and interval-qualified edge; no parent may be asserted on the unit record itself.
2. Per (axis, scenario, instant): at most one parent, and the edge set is acyclic. Acyclicity is evaluated per scenario branch, never across merged branches.
3. Rename and reparent preserve `unitIdentifier`; merge, split and disband require a lineage edge and an act reference.
4. Placement on any management axis never determines employer or legal entity; the employer derives only from `parentOrganizationRef` / `isAlsoFormalOrganization` and the out-of-scope employment model.
5. A body typed as collaboration may not hold an administrative-axis parent placement.
6. Scenario-qualified placements are excluded from asserted-current reads unless the scenario is the asserted branch.

## Scenario walkthrough

**Negative case.** A cross-department product team is given one administrative parent. The reserved model can represent it correctly — `Body mode: collaboration`, plus `unitAffiliation` edges to contributing units — but nothing prevents the wrong representation: `parentUnitRef` accepts a single value, and `derive-org-chart` needs a tree in the default hierarchy, which pressures an operator to invent a parent. Result: the team is mistaken for a unit, its members' home-unit posts are double-counted by `compute-headcount-rollup`, and the misplacement propagates into the IFRS 8 reporting hierarchy. Invariants 1 and 5 close this; without them the case fails.

**Acceptance case.** As-is/to-be reorganization on the administrative axis. If "to-be" is an *approved* future act, the reserved model passes: the act opens new intervals without deleting old assignments, `reconstruct-structure-as-of` replays the as-is state, and `validate-structure-graph` proves acyclicity on the selected axis. If "to-be" is a *hypothetical* option under evaluation, it fails: there is no branch on which to run validation, and asserting it corrupts the current view. The acceptance scenario is therefore met only under the approved-future reading.

## Profile shape

A narrow Enterprise profile over WM-ORG-002 — no new model, no second owner of `unit`, identifier unassigned and not requested. Content: (a) reify placement and forbid the unit-level parent attribute; (b) add the scenario/branch qualifier to placements, mandates, reporting lines and to the parameters of `validate-structure-graph`, `reconstruct-structure-as-of` and `derive-org-chart`; (c) convert the open questions on identifier stability, single-parent-per-axis, gap/overlap and employer independence into the invariants above; (d) tighten collaboration typing from a code value to an enforced exclusion. EM-ORG-04's questions 1–3 resolve as: identity is what makes a unit standalone; axes separate the three belongings; and the two-owner risk disappears because the profile constrains rather than redefines.

## Gaps and publication holds

Unsupported scenario semantics: hypothetical/branch structures, scenario comparison and per-branch validation — the single material capability gap. Also unresolved and blocking any readiness claim: the unit-to-site placement question (deferred in adjudication, and it would host any future site-axis placement); cost/profit/funds-centre hierarchies unresolved as in-model axes versus finance masters; unit-grain staffing measurement with no primary standard (extension-grade); ISO clause text, EUR-Lex 696/93, ESRS S1-6 Annex I and all source live-version checks outstanding; FHIR R4/R5 unpinned; private-sector matrix, military, academic, ecclesiastical and cooperative forms unvalidated — directly relevant to the matrix case above. The crosswalk depth required by EM-ORG-04's blocking decisions is not yet evidenced, so the profile recommendation is a boundary finding only.
