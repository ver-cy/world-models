# Frozen semantic audit request — EM-LND-01

You are the single independent frozen semantic auditor. Use only this prompt. Do not browse, use tools, execute code, invent identifiers, or authorize publication. Audit the reconciled candidate for identity/lifecycle integrity, source mastership, axis semantics, bitemporal consistency, deterministic snapshot identity, scenario discipline, fixtures and publication holds. Return PASS or REVISE, then findings, required deterministic remediation, identifier discipline, and publication decision. This audit runs exactly once.

## Reconciled profile candidate

```
{
  "format": "vercy-enterprise-profile-candidate/v1",
  "contourId": "EM-LND-01",
  "name": "Organizational Structure Landscape",
  "candidateRevision": 2,
  "decision": "PROFILE",
  "newRuntimeId": false,
  "bases": [
    "WM-ORG-002",
    "WM-ORG-003",
    "WM-ORG-004",
    "WM-ORG-016"
  ],
  "constructs": {
    "OrganizationLandscape": {
      "kind": "projection-specification",
      "identity": [
        "landscapeId",
        "specVersion",
        "organizationPerimeter",
        "axisSet",
        "scenarioClass"
      ],
      "scenarioClass": "authoritative"
    },
    "StructureAxis": {
      "kind": "governed-profile-construct",
      "identity": [
        "axisCode",
        "ruleVersion"
      ],
      "ownsEdges": false
    },
    "StructureSnapshot": {
      "kind": "generated-artifact",
      "identity": "digest(landscapeId,axisId,ruleVersion,worldTime,recordTime,sourceVersions,sourceDigests,generatorVersion)",
      "lifecycle": [
        "created",
        "retained",
        "disclosed",
        "tombstoned"
      ]
    }
  },
  "axes": {
    "administrative": {
      "sources": [
        "WM-ORG-002 containment"
      ],
      "hierarchy": true,
      "cardinality": "one parent per unit per interval",
      "acyclic": true
    },
    "functional": {
      "sources": [
        "WM-ORG-002 typed reporting",
        "WM-ORG-004 post reporting"
      ],
      "multipleEdges": true,
      "hierarchy": "profile parameter",
      "default": "DAG when hierarchy=true"
    },
    "project": {
      "sources": [
        "WM-ORG-003 membership",
        "WM-ORG-003 team nesting"
      ],
      "membershipIsHierarchy": false,
      "nestingSeparate": true
    },
    "supervisory": {
      "sources": [
        "WM-ORG-016 assignment reporting",
        "WM-ORG-004 post reporting"
      ],
      "effectiveSupervisor": "exactly one per assignment and axis after precedence",
      "secondaryEdgesVisible": true
    }
  },
  "constraints": [
    "The profile is read-only and never creates or edits source objects or relations.",
    "Every projected edge declares axis, owning master and world-time interval.",
    "Axis cardinality and cycle rules apply inside one axis only; the union graph is not a hierarchy and is not acyclicity-checked.",
    "Administrative containment has one parent per interval and is acyclic; reparenting remains a source reorganization act.",
    "Functional hierarchy and acyclicity are explicit rule-version parameters; multiple qualified edges are otherwise permitted.",
    "Project membership and team nesting are distinct; membership is many-to-many and never hierarchy.",
    "One effective supervisor is resolved per assignment and supervisory axis after precedence, never globally per person.",
    "One world-time and record-time pair applies to every required source.",
    "Generation pins every constituent source version and digest before evaluation; floating source versions are forbidden.",
    "A required source that cannot reconstruct the requested pair causes a refused snapshot with source and horizon diagnostics.",
    "Optional sources may be omitted only when the axis rule declares them optional and the snapshot records the omission.",
    "Snapshot identity is the digest of landscape, axis rules, time pair, source pins and generator version.",
    "Snapshots are immutable, never overwritten, and never re-imported as source truth.",
    "A later source correction creates a new record-time snapshot and preserves the old digest.",
    "Source-local snapshots remain source artifacts; the landscape snapshot composes them by reference.",
    "Scenario class is authoritative and includes only recorded source facts, including recorded future-effective changes.",
    "Hypothetical or mixed authoritative/scenario requests are refused until a planning extension exists.",
    "Decision time, effective time, world time and record time remain distinct.",
    "Person and organizational-unit facts remain references and are never copied into the profile."
  ],
  "holds": [
    "All four source models remain non-canonical reviewable drafts.",
    "Cross-model reconstruction horizons and retention guarantees are not uniform or verified.",
    "Source pin contracts and crosswalks are not ratified.",
    "Functional-axis hierarchy defaults and reporting-edge vocabularies require canonical agreement.",
    "Scenario branching is unsupported and remains authoritative-only.",
    "No landscape, axis or snapshot runtime identifier may be invented.",
    "W3C ORG, ISO 42010 and ArchiMate are alignments only, not conformance claims.",
    "One frozen semantic audit is pending after provider reconciliation.",
    "Package conversion and live publication are pending."
  ]
}

```

## Fixtures

```
{
  "format": "vercy-enterprise-profile-fixtures/v2",
  "contourId": "EM-LND-01",
  "candidateRevision": 2,
  "cases": [
    {
      "id": "matrix-separate-axes",
      "kind": "positive",
      "asOf": {
        "worldTime": "2026-10-01T09:00:00+00:00",
        "recordTime": "2026-09-28T12:00:00+00:00"
      },
      "records": {
        "assignment": "ASN-1",
        "projectEdge": "EDGE-P1",
        "supervisoryEdge": "EDGE-S1"
      },
      "expected": {
        "outcome": "snapshot-created",
        "code": "AXES_INDEPENDENT"
      }
    },
    {
      "id": "two-assignments",
      "kind": "positive",
      "asOf": {
        "worldTime": "2026-10-01T09:00:00+00:00",
        "recordTime": "2026-09-28T12:00:00+00:00"
      },
      "records": {
        "assignments": [
          "ASN-1",
          "ASN-2"
        ],
        "supervisors": [
          "POST-S1",
          "POST-S2"
        ]
      },
      "expected": {
        "outcome": "snapshot-created",
        "code": "SUPERVISOR_PER_ASSIGNMENT"
      }
    },
    {
      "id": "future-reorg-before",
      "kind": "positive",
      "asOf": {
        "worldTime": "2026-09-30T23:59:59+00:00",
        "recordTime": "2026-09-28T12:00:00+00:00"
      },
      "records": {
        "act": "REORG-1",
        "effectiveAt": "2026-10-01T00:00:00+00:00"
      },
      "expected": {
        "outcome": "snapshot-created",
        "code": "PRE_REORG_STRUCTURE"
      }
    },
    {
      "id": "future-reorg-after",
      "kind": "positive",
      "asOf": {
        "worldTime": "2026-10-01T00:00:00+00:00",
        "recordTime": "2026-09-28T12:00:00+00:00"
      },
      "records": {
        "act": "REORG-1",
        "effectiveAt": "2026-10-01T00:00:00+00:00"
      },
      "expected": {
        "outcome": "snapshot-created",
        "code": "POST_REORG_STRUCTURE"
      }
    },
    {
      "id": "union-cycle",
      "kind": "positive",
      "asOf": {
        "worldTime": "2026-09-28T12:00:00+00:00",
        "recordTime": "2026-09-28T12:00:00+00:00"
      },
      "records": {
        "administrative": "UNIT-A_CONTAINS_UNIT-B",
        "functional": "UNIT-B_REPORTS_UNIT-A"
      },
      "expected": {
        "outcome": "snapshot-created",
        "code": "UNION_CYCLE_ALLOWED"
      }
    },
    {
      "id": "admin-cycle",
      "kind": "negative",
      "asOf": {
        "worldTime": "2026-09-28T12:00:00+00:00",
        "recordTime": "2026-09-28T12:00:00+00:00"
      },
      "records": {
        "axis": "administrative",
        "edges": [
          "A>B",
          "B>A"
        ]
      },
      "expected": {
        "outcome": "refused",
        "code": "ADMIN_CYCLE"
      }
    },
    {
      "id": "short-required-horizon",
      "kind": "negative",
      "asOf": {
        "worldTime": "2020-01-01T00:00:00+00:00",
        "recordTime": "2026-09-28T12:00:00+00:00"
      },
      "records": {
        "source": "WM-ORG-016",
        "horizonStart": "2022-01-01T00:00:00+00:00",
        "required": true
      },
      "expected": {
        "outcome": "refused",
        "code": "SOURCE_HORIZON_UNAVAILABLE"
      }
    },
    {
      "id": "optional-source-omission",
      "kind": "positive",
      "asOf": {
        "worldTime": "2020-01-01T00:00:00+00:00",
        "recordTime": "2026-09-28T12:00:00+00:00"
      },
      "records": {
        "source": "WM-ORG-004",
        "required": false,
        "omissionDeclared": true
      },
      "expected": {
        "outcome": "snapshot-created-partial",
        "code": "DECLARED_OPTIONAL_OMISSION"
      }
    },
    {
      "id": "undeclared-partial",
      "kind": "negative",
      "asOf": {
        "worldTime": "2020-01-01T00:00:00+00:00",
        "recordTime": "2026-09-28T12:00:00+00:00"
      },
      "records": {
        "source": "WM-ORG-004",
        "required": false,
        "omissionDeclared": false
      },
      "expected": {
        "outcome": "refused",
        "code": "UNDECLARED_PARTIAL"
      }
    },
    {
      "id": "mixed-time",
      "kind": "negative",
      "asOf": {
        "worldTime": "2026-09-28T12:00:00+00:00",
        "recordTime": "2026-09-28T12:00:00+00:00"
      },
      "records": {
        "unitWorldTime": "2026-09-28T12:00:00+00:00",
        "assignmentWorldTime": "2026-10-01T00:00:00+00:00"
      },
      "expected": {
        "outcome": "refused",
        "code": "MIXED_TIME_PAIR"
      }
    },
    {
      "id": "floating-source-version",
      "kind": "negative",
      "asOf": {
        "worldTime": "2026-09-28T12:00:00+00:00",
        "recordTime": "2026-09-28T12:00:00+00:00"
      },
      "records": {
        "source": "WM-ORG-002",
        "version": "latest"
      },
      "expected": {
        "outcome": "refused",
        "code": "SOURCE_PIN_REQUIRED"
      }
    },
    {
      "id": "reimport-snapshot",
      "kind": "negative",
      "asOf": {
        "worldTime": "2026-09-28T12:00:00+00:00",
        "recordTime": "2026-09-28T12:00:00+00:00"
      },
      "records": {
        "snapshot": "SNAP-1",
        "operation": "import-as-master"
      },
      "expected": {
        "outcome": "refused",
        "code": "SNAPSHOT_REIMPORT_FORBIDDEN"
      }
    },
    {
      "id": "same-pins-same-digest",
      "kind": "positive",
      "asOf": {
        "worldTime": "2026-09-28T12:00:00+00:00",
        "recordTime": "2026-09-28T12:00:00+00:00"
      },
      "records": {
        "generationA": "GEN-1",
        "generationB": "GEN-2",
        "samePins": true
      },
      "expected": {
        "outcome": "same-digest",
        "code": "DETERMINISTIC_SNAPSHOT"
      }
    },
    {
      "id": "correction-new-record-time",
      "kind": "positive",
      "asOf": {
        "worldTime": "2026-09-01T00:00:00+00:00",
        "recordTime": "2026-09-28T12:00:00+00:00"
      },
      "records": {
        "oldSnapshot": "SNAP-OLD",
        "correctionRecordedAt": "2026-09-20T00:00:00+00:00"
      },
      "expected": {
        "outcome": "new-digest-old-preserved",
        "code": "BITEMPORAL_CORRECTION"
      }
    },
    {
      "id": "project-membership-not-nesting",
      "kind": "negative",
      "asOf": {
        "worldTime": "2026-09-28T12:00:00+00:00",
        "recordTime": "2026-09-28T12:00:00+00:00"
      },
      "records": {
        "member": "PERSON-1",
        "teams": [
          "TEAM-1",
          "TEAM-2"
        ],
        "inferredNesting": true
      },
      "expected": {
        "outcome": "refused",
        "code": "MEMBERSHIP_NOT_HIERARCHY"
      }
    },
    {
      "id": "hypothetical-scenario",
      "kind": "negative",
      "asOf": {
        "worldTime": "2026-12-01T00:00:00+00:00",
        "recordTime": "2026-09-28T12:00:00+00:00"
      },
      "records": {
        "scenarioClass": "hypothetical",
        "sourceAct": null
      },
      "expected": {
        "outcome": "refused",
        "code": "SCENARIO_UNSUPPORTED"
      }
    }
  ]
}

```

## Provider comparison

```
# EM-LND-01 provider comparison

Claude and Grok independently select **PROFILE** over WM-ORG-002, WM-ORG-003, WM-ORG-004 and WM-ORG-016 with no catalogue or runtime identifier. OrganizationLandscape is a governed projection specification, StructureAxis versions projection rules, and StructureSnapshot is an immutable digest-identified generated artifact. None owns organizational facts or edges.

Both providers keep axis validation local to each declared axis and reject any global one-manager rule. Administrative containment, team membership and nesting, position reporting, and assignment supervision remain mastered by their source models. One world-time/record-time pair applies to all required sources; a missing reconstruction horizon refuses the snapshot.

Grok strengthens the contract with an explicit digest tuple, source-version pinning, optional-source omission rules, non-reimport semantics, a functional-axis hierarchy parameter, project membership/nesting separation, union-graph cycle acceptance and authoritative-only scenario treatment. Alignments to W3C ORG, ISO 42010 and ArchiMate remain non-conformance references.

```

## Claude boundary study

```
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

```

## Grok boundary study

```
**Verdict.** PROFILE over WM-ORG-002, WM-ORG-003, WM-ORG-004 and WM-ORG-016. No new catalogue or runtime ID. OrganizationLandscape is a named projection specification. StructureAxis is a governed profile construct. StructureSnapshot is an immutable, digest-identified generated artifact. None of the three is a fifth organization master. Writes stay on the four source models. This is standards alignment, not a new architecture description language.

**Identity / lifecycle test.** Source facts: the card forbids copying Person and Unit; 002 already emits a digest-identified “Structure As-Of View” and says projections must not be re-imported as authoritative; 003 emits team-hierarchy and roster snapshots as audit artifacts; 004 and 016 are bitemporal masters of posts and assignments. ISO/IEC/IEEE 42010 alignment: a viewpoint governs a view; the view is not a second entity of interest. ArchiMate’s Organization viewpoint is a filter over business-structure elements, not a second org register.

- **OrganizationLandscape.** Identity: landscape-id + spec version + organization perimeter + declared axis set + scenario class (`authoritative`). Lifecycle versions the spec (which axes, which node and edge kinds, correspondence rules). Spec change does not rewrite unit, team, post or assignment history. Fail-to-new-aggregate if landscape edges are authored here, if the landscape writes masters, or if it becomes the system of record for a hierarchy.

- **StructureAxis.** Identity: axis code plus rule version (allowed node kinds, allowed edge kinds and owning master, cardinality, whether hierarchy/acyclicity is required, supervisor-precedence). Lifecycle versions the rules. It does not persist edges. Fail-to-new-aggregate if the axis mints an independent edge store.

- **StructureSnapshot.** Identity: digest of `(landscape-id, axis-id, rule version, world-time, record-time, pinned source versions and digests, generator version)`. Same pins produce the same digest. Lifecycle: created, retained, disclosed, tombstoned — never edited. A later master correction yields a new snapshot at a new record-time; the old digest remains the historical view. Fail-to-second-source-of-truth if the snapshot is editable, re-imported as master, or silently overwritten on regeneration.

002’s as-of export and 003’s local snapshots remain source-local. The landscape snapshot composes them by reference.

**Axis rules.** Axes are independent. The union of axes is not itself a hierarchy. Hierarchy rules are applied inside one axis’s declared edge set only. Design inference from the four masters, labelled as such.

1. **Administrative.** 002 containment only. One parent unit per interval. Acyclic. Multi-parent in this axis is refused. Reparenting is a 002 reorganization act, not a landscape edit.

2. **Functional.** 002 typed reporting lines and/or 004 post-to-post reporting of functional or professional kind. Multiple declared edges permitted. Hierarchy (and therefore acyclicity) is a profile parameter; default is a DAG, with cycles refused only if the profile sets hierarchy=true. Dotted-line is an edge qualifier, not a second axis. W3C ORG separates `org:subOrganizationOf` from `org:reportsTo`; unit-to-unit reporting is an extension and must be declared as such.

3. **Project.** 003 agent–team membership plus, separately, 003 team-nesting edges. Membership is a dated assignment fact, not a hierarchy, and does not inherit administrative acyclicity. Members of a child team are not direct members of the parent. A person on two teams is not a cycle.

4. **Supervisory.** 016 assignment reporting and/or 004 post reporting, restricted to the supervisory type. After that axis’s precedence rule, exactly one *effective* supervisor per assignment on this axis. Secondary lines remain visible as non-effective edges. “One effective supervisor” is per assignment and per axis, never a global one-manager law. 016 already allows multiple reporting lines with precedence.

A rendering that “shows three axes” is three projections of the same pinned masters, not one merged graph with a single parent rule.

**Time / snapshot contract.** One `(world-time, record-time)` pair is applied to every required source. The snapshot pins constituent versions and digests and holds references to master objects. Different record-time for the same world-time is a different snapshot (what was believed then versus what is believed now about then).

Refuse generation when any required source cannot reconstruct that pair. Do not drop the short source, interpolate, or emit a best-effort graph. An optional source may be omitted only if the Axis profile marks it optional and the snapshot states the omission. Undeclared partial success is a failure.

002 already asks how far reconstruction is guaranteed after retention-driven deletion. That hold remains visible on this PROFILE; the refuse rule cannot be claimed implemented until source horizons are explicit.

**Scenario treatment.** `authoritative` means only facts already recorded on the masters, including future-dated reorganization acts that already exist with a future effective time. Hypothetical what-if charts are unsupported. Until a planning extension exists, a non-authoritative scenario request is refused, not approximated. Decide-time, effective-time and record-time stay distinct.

**Scenario results.**

1. *Matrix assignment appears to violate a global one-manager rule.* The card negative case is this false collapse. Matrix is two or more edges on different axes. Each axis may still enforce its own cardinality. The landscape must not raise a global one-manager integrity failure. Both edges remain visible; the supervisory axis computes one effective supervisor per assignment. A system that rejects the matrix fails the negative case.

2. *Administrative, project and supervisory views include two assignments and a future reorganization.* Same `(world, record)` pair and pinned source versions. Administrative containment at *t* applies the reorg only if *t* ≥ act.effective. Project shows membership separately from team nesting. Supervisory may give the two assignments different effective supervisors. Person and Unit appear as references. If *t* exceeds a required source’s horizon, refuse rather than invent the post-reorg graph.

3. *A cycle exists across the union of two axes but not within either.* Acyclicity is evaluated per axis. A union-graph cycle (for example admin A contains B, while a functional or project edge from B returns to A) is legal. The snapshot may annotate the correspondence; it must not refuse generation. Refusing because the union is cyclic fails the card invariant that a cycle is forbidden only where a hierarchy is required.

4. *One source has a shorter reconstruction horizon.* Snapshot refused. Return the failing source, the requested pair and the declared horizon. Do not stitch the remaining sources and label the graph complete. An axis that marks that source optional may still generate with an explicit omission flag; default administrative and supervisory axes treat 002 and 016 as required.

**Publication blockers.**
- Snapshot identity as digest-of-pins and the no-reimport rule are not yet written as PROFILE constraints.
- Reconstruction horizons on 002/003/004/016 are not uniform; 002’s horizon question remains open. Test 4 has no fixture.
- Tighten the PROFILE text that union graphs are not acyclicity-checked.
- Floating versus pinned source versions at generation time is unspecified.
- All four masters remain reviewable drafts with source-pin, multi-profile and retention holds.
- Scenario=`authoritative` is a hold: no planning extension, no new ID.
- Alignments to W3C ORG, ISO 42010 and ArchiMate are alignments only, not conformance claims.
- Do not invent a landscape, axis or snapshot runtime identifier.

```

## Frozen dossier

```
{
  "contour": {
    "id": "EM-LND-01",
    "name": "Организационная структура",
    "domain": "LND",
    "kind": "landscape",
    "wave": "W1",
    "scope": "Версионированный граф организационных единиц, позиций, коллективов и назначений по независимым осям.",
    "candidate_types": [
      "OrganizationLandscape",
      "StructureAxis",
      "StructureSnapshot"
    ],
    "specific_questions": [
      "Как различить административную, функциональную и проектную оси?",
      "Где допустим один родитель?",
      "Как увидеть структуру на дату до реорганизации?"
    ],
    "proposed_invariants": [
      "Ось и период обязательны",
      "Цикл запрещается только там, где требуется иерархия",
      "Person и Unit не копируются"
    ],
    "negative_case": "Матричное назначение ломает правило единственного руководителя для всей организации.",
    "acceptance_scenario": "Три оси, два назначения человека и будущая реорганизация дают три согласованных вида одной истории.",
    "comparison_tracks": [
      "Vercy composition и whole-object: отдельный объект ландшафта и делегирование",
      "ArchiMate/ISO 42010: виды, вопросы и правила представления",
      "Сравнить предметные модели участников и практическую сборку разрешённого контекста"
    ],
    "vercy_candidates": [
      {
        "model_id": "WM-ORG-002",
        "mapping_status": "conceptual-candidate",
        "evidence_depth": "index-and-publication-metadata",
        "note": "Связь требует проверки полного семантического crosswalk; published не означает завершённую независимую экспертизу."
      },
      {
        "model_id": "WM-ORG-003",
        "mapping_status": "conceptual-candidate",
        "evidence_depth": "index-and-publication-metadata",
        "note": "Связь требует проверки полного семантического crosswalk; published не означает завершённую независимую экспертизу."
      },
      {
        "model_id": "WM-ORG-004",
        "mapping_status": "conceptual-candidate",
        "evidence_depth": "index-and-publication-metadata",
        "note": "Связь требует проверки полного семантического crosswalk; published не означает завершённую независимую экспертизу."
      },
      {
        "model_id": "WM-ORG-016",
        "mapping_status": "conceptual-candidate",
        "evidence_depth": "boundary-reviewed",
        "note": "Связь требует проверки полного семантического crosswalk; published не означает завершённую независимую экспертизу."
      }
    ],
    "candidate_properties_from_v1": [
      {
        "predecessor": "LND-01",
        "fields": [
          {
            "name": "structure_kind",
            "value_type": "code",
            "status": "candidate-not-normative"
          },
          {
            "name": "as_of",
            "value_type": "datetime",
            "status": "candidate-not-normative"
          },
          {
            "name": "scenario",
            "value_type": "code",
            "status": "candidate-not-normative"
          },
          {
            "name": "boundary",
            "value_type": "text",
            "status": "candidate-not-normative"
          }
        ]
      }
    ],
    "suggested_owner": "Куратор мета-моделей Vercy",
    "candidate_master_systems": "Реестр моделей, sources.yaml, vercy.lock, политики",
    "related_research_contours": [],
    "blocking_decisions": [
      "Установить границу и решение reuse/extend/new по действующим спецификациям.",
      "Подтвердить semantic crosswalk, права и source mastership.",
      "Выбрать immutable refs; провести проверки fixtures до заявления о публикационной готовности."
    ]
  },
  "registry_policy": {
    "reserved_candidates": [
      "WM-ORG-002",
      "WM-ORG-003",
      "WM-ORG-004",
      "WM-ORG-016"
    ],
    "rule": "No new ID without independent identity/lifecycle and registry allocation."
  },
  "models": {
    "unit": {
      "publication": {
        "status": "published",
        "adjudicationStatus": "reviewable-draft",
        "publishableCanonical": false,
        "generatedAt": "2026-08-23T23:43:44Z",
        "synthesisSha256": "a991fb7774ae1b611787fe093e9d9e380499bf42c9fbe69fcb91af147be90812",
        "providerMode": "dual-provider",
        "providers": [
          "Claude",
          "Grok"
        ],
        "waivedProviders": []
      },
      "model": {
        "registry_id": "vr.wm-org-002",
        "model_id": "WM-ORG-002",
        "name": "Organizational Unit",
        "entry_kind": "entity",
        "purpose": "Provide the format-neutral context an agent needs to understand, create, inspect and operate the internal structure of an organization: which units exist, how they nest and report, what each is mandated to do, what establishment and staffing they carry, and how that structure is changed, dated, evidenced and disclosed over time.",
        "scope_statement": "This model covers an organizational unit as a subdivision that, in the words of the W3C Organization Ontology, 'only has full recognition within the context of that Organization'. It governs unit identity, classification, containment and reporting relationships, delegated mandate and decision rights, authorized establishment and measured staffing, structural change acts and their temporal validity, plus the provenance, retention, disclosure and interoperability rules that make the structure record operable. It deliberately stops at the boundaries of legal organizational identity, of the post/position as an object in its own right, of employment relationships, of physical sites, and of statistical or financial reporting units that are derived from - but not identical to - internal structure.",
        "in_scope": [
          "Unit identity, naming, aliases and parent-scoped or ISO/IEC 6523 organization-part identification",
          "Unit kind classification against governed code lists and unit existence status",
          "Containment hierarchies, including multiple concurrent hierarchies (managerial, legal, cost, functional)",
          "Reporting and coordination lines, including non-containment and dotted-line relationships",
          "Delegated mandate, decision rights, authority limits and segregation-of-duties constraints attached to a unit",
          "Authorized establishment (post complement) seated in a unit and its occupancy state at unit granularity",
          "Dated headcount and full-time-equivalent measurement of a unit, with basis and aggregation thresholds",
          "Reorganization acts (create, rename, reparent, merge, split, transfer, disband) and unit lineage",
          "Effective dating, bitemporality and as-of reconstruction of the structure graph",
          "Record authority, approval evidence, retention/disposition and disclosure control for structure data",
          "Crosswalks to W3C ORG, CPOV, FHIR, LDAP, SCIM, schema.org and ISO/IEC 6523 projections"
        ],
        "out_of_scope": [
          "Legal personality, incorporation, registration, LEI and regulatory identity of the whole organization (WM-ORG-001)",
          "The post/position as an object with its own title, grade, job description and occupational classification (WM-ORG-004)",
          "Employment contracts, appointments, persons and their occupancy of posts",
          "Constitutive charter powers of the organization as a legal entity (charter model)",
          "Physical premises, addresses, geometry and site operations (site/location model)",
          "Statistical units such as enterprise, local unit and kind-of-activity unit used for economic observation",
          "Financial segment reporting, general ledger and cost accounting mechanics",
          "Stewardship policy machinery and access-grant issuance (S1/S2 service models)",
          "Business capability, process and value-stream modelling",
          "Identity-provider group membership and directory synchronisation state as a system of record"
        ],
        "boundary_notes": [
          {
            "neighbor": "WM-ORG-001 Organization",
            "distinction": "W3C ORG separates org:FormalOrganization (recognized in a legal jurisdiction, with rights and responsibilities) from org:OrganizationalUnit, which has full recognition only inside its parent. Legal identity, registration and LEI stay in WM-ORG-001. A branch that is separately registered is dual-classified: it is a unit here and a legal entity there, and GLEIF only issues an LEI to the legally registered entity, not to an internal division.",
            "source_refs": [
              "SRC-001",
              "SRC-013"
            ]
          },
          {
            "neighbor": "WM-ORG-004 Position",
            "distinction": "org:Post represents a position that exists independently of who fills it. This model records only the unit-side facts: how many posts are established in the unit, which posts are seated there, and the aggregate occupancy state. Post title, grade, competency profile and occupational classification belong to WM-ORG-004, which this model CONTAINS by reference rather than by copy.",
            "source_refs": [
              "SRC-001"
            ]
          },
          {
            "neighbor": "Site / Location model",
            "distinction": "FHIR states that Location records where a service occurs while Organization records who performed it; Eurostat's 'local unit' is 'an enterprise or part thereof ... situated in a geographically identified place'. A unit may be associated with one or more sites, but premises, addresses and geometry are not unit attributes and are not modelled here.",
            "source_refs": [
              "SRC-002",
              "SRC-010"
            ]
          },
          {
            "neighbor": "Statistical units model",
            "distinction": "Council Regulation (EEC) No 696/93 defines enterprise, kind-of-activity unit and local unit as observation units for economic statistics. These are derived by statistical rules from operational reality, not asserted by the organization, and their boundaries routinely differ from internal units. Treated as an ALIGN target, never as a source of internal unit identity.",
            "source_refs": [
              "SRC-010"
            ]
          },
          {
            "neighbor": "Financial segment reporting",
            "distinction": "IFRS 8 identifies operating segments through a management approach based on how the chief operating decision maker reviews internal reports, and permits aggregation of segments with similar economic characteristics. A reportable segment is therefore a derived view over internal units, not a unit; this model supplies the inputs and the change signal, not the segment determination.",
            "source_refs": [
              "SRC-009"
            ]
          },
          {
            "neighbor": "Directory and identity systems",
            "distinction": "RFC 4519 defines 'ou' as a multi-valued name attribute and RFC 7643 defines SCIM 'department', 'division' and 'organization' as free-text names. These carry no identifier, no validity period and no hierarchy semantics, so directory content is a lossy projection of this model and never its system of record.",
            "source_refs": [
              "SRC-004",
              "SRC-005"
            ]
          },
          {
            "neighbor": "Global organization registries",
            "distinction": "ROR states it 'is not focused on capturing all subdivisions of a given organization such as a university's schools or departments' because departments 'often emerge, close, combine, and change'. No general governed global identifier exists for internal units, so unit identity is parent-scoped by default.",
            "source_refs": [
              "SRC-011",
              "SRC-012"
            ]
          }
        ]
      },
      "selected_findings": [
        {
          "bundle": {
            "id": "unit-identity-and-classification",
            "name": "Unit Identity and Classification",
            "description": "What a unit is, how it is unambiguously referenced, what it is called, what kind of thing it is, and whether it currently exists."
          },
          "layer": {
            "id": "unit-identification",
            "name": "Unit Identification",
            "description": "Identifier assignment, external addressability and naming of a unit."
          },
          "finding": {
            "id": "unit-identifier-scheme",
            "name": "Unit Identifier Scheme and Assignment",
            "description": "A unit's authoritative identifier is normally minted by the parent organization's master system, because no general governed global registry issues identifiers for internal subdivisions. ISO/IEC 6523 provides the only widely deployed external addressing slot, combining an International Code Designator, the parent organization identifier and an optional organization part identifier; schema.org exposes this as iso6523Code in XXXX:YYYYYY:ZZZ form. Identifier stability across rename, reparenting and merge must be decided explicitly.",
            "source_refs": [
              "SRC-001",
              "SRC-007",
              "SRC-008",
              "SRC-012",
              "SRC-013"
            ],
            "questions": [
              {
                "id": "q-authoritative-id",
                "text": "Which system is the authoritative assigner of this unit's identifier, and is that system the parent organization's master record rather than a downstream HR or directory system?",
                "kind": "identity",
                "answer_data": [
                  "assigning system name and reference",
                  "identifier scheme code",
                  "assignment authority role",
                  "assignment timestamp (RFC 3339)"
                ]
              },
              {
                "id": "q-external-addressing",
                "text": "Can this unit be addressed externally as an ISO/IEC 6523 organization part under the parent organization's ICD and organization identifier, and if so which OPI value and source indicator apply?",
                "kind": "interoperability",
                "answer_data": [
                  "ICD value",
                  "organization identifier",
                  "organization part identifier",
                  "OPI source indicator",
                  "composed iso6523Code string"
                ]
              },
              {
                "id": "q-id-stability",
                "text": "Does the identifier survive renaming, reparenting and merger of the unit, and is it guaranteed never to be reassigned to a different unit?",
                "kind": "constraint",
                "answer_data": [
                  "stability policy statement",
                  "reuse-prohibited boolean",
                  "events that force a new identifier"
                ]
              },
              {
                "id": "q-id-fallback",
                "text": "If no master-system identifier exists, which UUID or ULID does the adopting Dimension mint, and where is that minting act recorded?",
                "kind": "provenance",
                "answer_data": [
                  "locally minted identifier",
                  "identifier type (UUID/ULID)",
                  "minting Dimension",
                  "minting record reference"
                ]
              }
            ],
            "data_elements": [
              {
                "id": "de-unit-id",
                "name": "unitIdentifier",
                "description": "The authoritative identifier for the unit within its assigning scheme.",
                "value_kind": "identifier",
                "cardinality": "1",
                "required": true,
                "source_refs": [
                  "SRC-001",
                  "SRC-002"
                ]
              },
              {
                "id": "de-unit-id-scheme",
                "name": "unitIdentifierScheme",
                "description": "Coded reference to the scheme and assigning authority for the identifier.",
                "value_kind": "code",
                "cardinality": "1",
                "required": true,
                "source_refs": [
                  "SRC-007"
                ]
              },
              {
                "id": "de-unit-opi",
                "name": "organizationPartIdentifier",
                "description": "ISO/IEC 6523 organization part identifier for external addressing of the unit, with its source indicator.",
                "value_kind": "identifier",
                "cardinality": "0..1",
                "required": false,
                "source_refs": [
                  "SRC-007",
                  "SRC-008"
                ]
              },
              {
                "id": "de-unit-alt-ids",
                "name": "alternateIdentifiers",
                "description": "Non-authoritative identifiers held in downstream systems (ERP cost centre code, LDAP DN, IdP group id).",
                "value_kind": "collection",
                "cardinality": "0..n",
                "required": false,
                "source_refs": [
                  "SRC-004",
                  "SRC-005"
                ]
              }
            ],
            "artifacts": [
              {
                "id": "unit-register",
                "name": "Unit Identifier Register",
                "description": "The authoritative register of unit identifiers, their scheme, assignment act and retirement state, held by the parent organization.",
                "media_or_form": [
                  "structured register",
                  "tabular export",
                  "graph node set"
                ],
                "serial": false,
                "identity_strategy": "Registered under the parent organization's master-system register identifier; each entry keyed by unitIdentifier, which is never reused.",
                "source_refs": [
                  "SRC-001",
                  "SRC-007",
                  "SRC-012"
                ]
              }
            ],
            "inline_only_rationale": null
          }
        },
        {
          "bundle": {
            "id": "unit-identity-and-classification",
            "name": "Unit Identity and Classification",
            "description": "What a unit is, how it is unambiguously referenced, what it is called, what kind of thing it is, and whether it currently exists."
          },
          "layer": {
            "id": "unit-classification",
            "name": "Unit Classification and Existence",
            "description": "The kind of unit and whether it currently exists as an operating subdivision."
          },
          "finding": {
            "id": "unit-kind-classification",
            "name": "Unit Kind and Classification Scheme",
            "description": "Units are typed against a governed code list (department, division, directorate, branch, committee, board, team, programme office, shared-service centre, cost centre). W3C ORG provides org:classification against a scheme; CPOV constrains purpose to COFOG codes for public organisations and adds a classification property; FHIR uses a CodeableConcept type. The scheme must be named, versioned and resolvable, and the same unit may carry codes from several schemes simultaneously.",
            "source_refs": [
              "SRC-001",
              "SRC-002",
              "SRC-003"
            ],
            "questions": [
              {
                "id": "q-kind-scheme",
                "text": "Against which named and versioned classification scheme is the unit's kind asserted, and is that scheme resolvable to a published code list?",
                "kind": "classification",
                "answer_data": [
                  "scheme identifier or IRI",
                  "scheme version",
                  "code value",
                  "code label"
                ]
              },
              {
                "id": "q-multi-scheme",
                "text": "Does the unit carry codes from more than one scheme (internal kind, public-sector function, industry activity), and which one governs behaviour?",
                "kind": "interoperability",
                "answer_data": [
                  "list of scheme/code pairs",
                  "governing scheme flag",
                  "mapping notes"
                ]
              },
              {
                "id": "q-formal-vs-unit",
                "text": "Is this subdivision also a formal organization recognized in a legal jurisdiction, requiring dual classification and a link to WM-ORG-001?",
                "kind": "definition",
                "answer_data": [
                  "dual-classification boolean",
                  "legal entity identifier if any",
                  "jurisdiction",
                  "basis of legal recognition"
                ]
              },
              {
                "id": "q-kind-change",
                "text": "What evidence is required before a unit's kind may be reclassified, and does reclassification require a reorganization act?",
                "kind": "authority",
                "answer_data": [
                  "reclassification authority role",
                  "required evidence",
                  "linked reorganization act reference"
                ]
              }
            ],
            "data_elements": [
              {
                "id": "de-unit-kind",
                "name": "unitKind",
                "description": "Coded kind of unit against a governed scheme.",
                "value_kind": "code",
                "cardinality": "1..n",
                "required": true,
                "source_refs": [
                  "SRC-001",
                  "SRC-002",
                  "SRC-003"
                ]
              },
              {
                "id": "de-classification-scheme",
                "name": "classificationScheme",
                "description": "Identifier and version of the scheme from which each code is drawn.",
                "value_kind": "reference",
                "cardinality": "1..n",
                "required": true,
                "source_refs": [
                  "SRC-001",
                  "SRC-003"
                ]
              },
              {
                "id": "de-dual-legal-flag",
                "name": "isAlsoFormalOrganization",
                "description": "Whether this subdivision is separately recognized as a legal entity.",
                "value_kind": "boolean",
                "cardinality": "1",
                "required": true,
                "source_refs": [
                  "SRC-001",
                  "SRC-013"
                ]
              }
            ],
            "artifacts": [
              {
                "id": "unit-kind-code-list",
                "name": "Unit Kind Code List",
                "description": "The governed, versioned code list of unit kinds used by the adopting Dimension, with definitions, deprecations and mappings to org:classification and CPOV codes.",
                "media_or_form": [
                  "code list",
                  "SKOS concept scheme",
                  "tabular export"
                ],
                "serial": false,
                "identity_strategy": "Identified by a governed scheme IRI plus semantic version; codes are never reused after deprecation.",
                "source_refs": [
                  "SRC-001",
                  "SRC-003"
                ]
              }
            ],
            "inline_only_rationale": null
          }
        },
        {
          "bundle": {
            "id": "structural-composition",
            "name": "Structural Composition",
            "description": "How units nest into hierarchies and how they report to and coordinate with one another."
          },
          "layer": {
            "id": "containment-hierarchy",
            "name": "Containment Hierarchy",
            "description": "Parent-child membership of units within the organization, including concurrent hierarchies."
          },
          "finding": {
            "id": "parent-child-containment",
            "name": "Parent-Child Containment",
            "description": "Every unit resolves to exactly one parent organization and, except at the top, to one parent unit within a given hierarchy. W3C ORG expresses this with org:unitOf/org:hasUnit and org:subOrganizationOf; FHIR uses partOf; schema.org uses parentOrganization, which supersedes branchOf and is not distinguished from subsidiary ownership. ROR maintains reciprocal parent and child edges on active records. Cycles, orphans and multi-parent assertions within one hierarchy are integrity failures.",
            "source_refs": [
              "SRC-001",
              "SRC-002",
              "SRC-008",
              "SRC-011"
            ],
            "questions": [
              {
                "id": "q-parent-org",
                "text": "Which organization (WM-ORG-001 instance) does this unit ultimately belong to, and is that link mandatory and immutable for the unit's lifetime?",
                "kind": "composition",
                "answer_data": [
                  "parent organization identifier",
                  "link mandatory boolean",
                  "transfer-between-organizations rule"
                ]
              },
              {
                "id": "q-parent-unit",
                "text": "Which unit is the immediate parent within the named hierarchy, and what is the depth and root of that path?",
                "kind": "relationship",
                "answer_data": [
                  "parent unit identifier",
                  "hierarchy name",
                  "root unit identifier",
                  "materialised path or depth"
                ]
              },
              {
                "id": "q-integrity",
                "text": "How are cycles, orphaned units and multiple parents within a single hierarchy detected and prevented at write time?",
                "kind": "validation",
                "answer_data": [
                  "acyclicity check definition",
                  "orphan rule",
                  "single-parent constraint per hierarchy",
                  "rejection behaviour"
                ]
              },
              {
                "id": "q-containment-vs-ownership",
                "text": "Is the parent link a containment of a non-legal subdivision or an ownership relation to a separate legal entity, and how is that difference preserved when exporting to vocabularies that conflate them?",
                "kind": "interoperability",
                "answer_data": [
                  "edge semantics code",
                  "target entity type",
                  "export mapping note",
                  "loss warning"
                ]
              }
            ],
            "data_elements": [
              {
                "id": "de-parent-org-ref",
                "name": "parentOrganizationRef",
                "description": "Reference to the WM-ORG-001 organization instance that owns the structure.",
                "value_kind": "reference",
                "cardinality": "1",
                "required": true,
                "source_refs": [
                  "SRC-001",
                  "SRC-002"
                ]
              },
              {
                "id": "de-parent-unit-ref",
                "name": "parentUnitRef",
                "description": "Reference to the immediate parent unit within a named hierarchy.",
                "value_kind": "reference",
                "cardinality": "0..1",
                "required": false,
                "source_refs": [
                  "SRC-001",
                  "SRC-011"
                ]
              },
              {
                "id": "de-hierarchy-path",
                "name": "hierarchyPath",
                "description": "Ordered path of unit identifiers from the hierarchy root to this unit, derived not asserted.",
                "value_kind": "collection",
                "cardinality": "0..1",
                "required": false,
                "source_refs": [
                  "SRC-001"
                ]
              }
            ],
            "artifacts": [
              {
                "id": "org-chart-projection",
                "name": "Organization Chart Projection",
                "description": "A rendered or serialised view of the containment hierarchy with unit names and kinds, deliberately omitting mandate detail and staffing figures.",
                "media_or_form": [
                  "hierarchical graph",
                  "diagram",
                  "nested list",
                  "tabular edge list"
                ],
                "serial": true,
                "identity_strategy": "Identified by hierarchy name plus as-of instant (RFC 3339) plus source structure version; regenerated projections are new serial instances, never edits.",
                "source_refs": [
                  "SRC-001",
                  "SRC-011"
                ]
              }
            ],
            "inline_only_rationale": null
          }
        },
        {
          "bundle": {
            "id": "structural-composition",
            "name": "Structural Composition",
            "description": "How units nest into hierarchies and how they report to and coordinate with one another."
          },
          "layer": {
            "id": "containment-hierarchy",
            "name": "Containment Hierarchy",
            "description": "Parent-child membership of units within the organization, including concurrent hierarchies."
          },
          "finding": {
            "id": "concurrent-hierarchies",
            "name": "Concurrent Hierarchies and Matrix Structure",
            "description": "One organization commonly maintains several simultaneous hierarchies over the same units: managerial line, legal-entity roll-up, cost/budget roll-up, functional or professional line, and the internal reporting structure that IFRS 8 makes decisive for segment identification. Each hierarchy is a separately named, separately governed edge set; collapsing them into one tree destroys the information that downstream reporting depends on.",
            "source_refs": [
              "SRC-001",
              "SRC-009",
              "SRC-005"
            ],
            "questions": [
              {
                "id": "q-hierarchy-inventory",
                "text": "Which named hierarchies exist over the unit set, who owns each, and which one is the default for display?",
                "kind": "composition",
                "answer_data": [
                  "hierarchy identifier",
                  "hierarchy purpose",
                  "owning role",
                  "default flag"
                ]
              },
              {
                "id": "q-hierarchy-divergence",
                "text": "Where does a unit's position differ between hierarchies, and is that divergence intentional or an integrity defect?",
                "kind": "quality",
                "answer_data": [
                  "divergence report rows",
                  "intentional flag",
                  "justification",
                  "reviewer"
                ]
              },
              {
                "id": "q-codm-hierarchy",
                "text": "Which hierarchy corresponds to the internal reports reviewed by the chief operating decision maker for the purposes of segment identification?",
                "kind": "decision",
                "answer_data": [
                  "hierarchy identifier",
                  "CODM role reference",
                  "attestation date",
                  "scope of internal reports"
                ]
              },
              {
                "id": "q-hierarchy-precedence",
                "text": "When two hierarchies imply conflicting authority over the same unit, which precedence rule resolves the conflict?",
                "kind": "constraint",
                "answer_data": [
                  "precedence ordering",
                  "conflict class",
                  "escalation path"
                ]
              }
            ],
            "data_elements": [
              {
                "id": "de-hierarchy-id",
                "name": "hierarchyIdentifier",
                "description": "Identifier and purpose of a named hierarchy over the unit set.",
                "value_kind": "identifier",
                "cardinality": "1..n",
                "required": true,
                "source_refs": [
                  "SRC-001",
                  "SRC-009"
                ]
              },
              {
                "id": "de-hierarchy-edge",
                "name": "hierarchyEdge",
                "description": "A parent-child edge qualified by hierarchy identifier and validity period.",
                "value_kind": "object",
                "cardinality": "0..n",
                "required": false,
                "source_refs": [
                  "SRC-001",
                  "SRC-011"
                ]
              },
              {
                "id": "de-codm-flag",
                "name": "isCodmReportingHierarchy",
                "description": "Marks the hierarchy that reflects internal management reporting for segment purposes.",
                "value_kind": "boolean",
                "cardinality": "0..1",
                "required": false,
                "source_refs": [
                  "SRC-009"
                ]
              }
            ],
            "artifacts": [],
            "inline_only_rationale": "Concurrent hierarchies are edge sets over the units already registered elsewhere; each materialises through the org chart projection artifact parameterised by hierarchy identifier, so no additional artifact class is warranted."
          }
        },
        {
          "bundle": {
            "id": "structural-composition",
            "name": "Structural Composition",
            "description": "How units nest into hierarchies and how they report to and coordinate with one another."
          },
          "layer": {
            "id": "reporting-and-coordination",
            "name": "Reporting and Coordination",
            "description": "Directed reporting relations and non-containment relationships between units."
          },
          "finding": {
            "id": "reporting-lines",
            "name": "Reporting Lines and Their Standards Basis",
            "description": "Reporting lines are distinct from containment: a unit may sit under one parent but report functionally elsewhere (dotted line). W3C ORG's org:reportsTo is defined between Agents or Posts, not between organizational units, so unit-to-unit reporting is an extension of the standard and must be declared as such rather than claimed as conformant. SCIM offers only a single 'manager' reference at person level, which cannot carry line type or validity.",
            "source_refs": [
              "SRC-001",
              "SRC-005"
            ],
            "questions": [
              {
                "id": "q-line-type",
                "text": "What type is each reporting line - administrative, functional, professional, operational or advisory - and is it solid or dotted?",
                "kind": "relationship",
                "answer_data": [
                  "line type code",
                  "solid/dotted flag",
                  "source unit",
                  "target unit or post"
                ]
              },
              {
                "id": "q-line-subject",
                "text": "Does the reporting line hold between units, between posts, or between the units' heads, and which representation is authoritative?",
                "kind": "definition",
                "answer_data": [
                  "subject type (unit/post/agent)",
                  "authoritative representation flag",
                  "derivation rule for the other representations"
                ]
              },
              {
                "id": "q-line-conformance",
                "text": "Where unit-to-unit reporting is asserted, is the departure from org:reportsTo recorded as an explicit extension with a mapping rule?",
                "kind": "interoperability",
                "answer_data": [
                  "extension declaration",
                  "target standard property",
                  "mapping rule",
                  "non-conformance note"
                ]
              },
              {
                "id": "q-line-validity",
                "text": "Over which period is each reporting line valid, and can two lines of the same type to different targets overlap in time?",
                "kind": "temporal",
                "answer_data": [
                  "validity start and end (RFC 3339)",
                  "overlap-permitted boolean per line type",
                  "conflict detection rule"
                ]
              }
            ],
            "data_elements": [
              {
                "id": "de-reporting-line",
                "name": "reportingLine",
                "description": "Directed reporting relation with type, subject kind, target and validity period.",
                "value_kind": "object",
                "cardinality": "0..n",
                "required": false,
                "source_refs": [
                  "SRC-001"
                ]
              },
              {
                "id": "de-line-type",
                "name": "reportingLineType",
                "description": "Coded type of the reporting relation.",
                "value_kind": "code",
                "cardinality": "1",
                "required": true,
                "source_refs": [
                  "SRC-001"
                ]
              },
              {
                "id": "de-line-extension-note",
                "name": "standardExtensionNote",
                "description": "Declaration that unit-level reporting extends beyond the domain/range of org:reportsTo.",
                "value_kind": "text",
                "cardinality": "0..1",
                "required": false,
                "source_refs": [
                  "SRC-001"
                ]
              }
            ],
            "artifacts": [
              {
                "id": "reporting-line-matrix",
                "name": "Reporting Line Matrix",
                "description": "Edge list of all reporting relations with type, direction, validity and standards-mapping note, usable for matrix-management analysis and for detecting conflicting lines.",
                "media_or_form": [
                  "edge list",
                  "matrix table",
                  "graph export"
                ],
                "serial": true,
                "identity_strategy": "Keyed by organization identifier plus as-of instant (RFC 3339); each generation is a new serial instance referencing the structure version it was derived from.",
                "source_refs": [
                  "SRC-001",
                  "SRC-005"
                ]
              }
            ],
            "inline_only_rationale": null
          }
        },
        {
          "bundle": {
            "id": "structural-composition",
            "name": "Structural Composition",
            "description": "How units nest into hierarchies and how they report to and coordinate with one another."
          },
          "layer": {
            "id": "reporting-and-coordination",
            "name": "Reporting and Coordination",
            "description": "Directed reporting relations and non-containment relationships between units."
          },
          "finding": {
            "id": "cross-unit-affiliations",
            "name": "Cross-Unit and External Affiliations",
            "description": "Units participate in relations that are neither containment nor reporting: shared services, joint committees, secondments of capacity, service-level relations to other units, and affiliations to bodies in other legal entities. FHIR introduces OrganizationAffiliation precisely for 'complex non-hierarchical relationships between separate legal entities without implying ownership'; ROR uses a 'related' type for 'less defined connections, such as resource sharing or participation without direct control'.",
            "source_refs": [
              "SRC-002",
              "SRC-011"
            ],
            "questions": [
              {
                "id": "q-affiliation-kind",
                "text": "What kind of non-hierarchical relation is this - shared service, joint body, service agreement, secondment or partnership - and does it imply any control?",
                "kind": "relationship",
                "answer_data": [
                  "affiliation type code",
                  "implies-control boolean",
                  "counterparty reference"
                ]
              },
              {
                "id": "q-affiliation-boundary",
                "text": "Does the counterparty sit inside the same parent organization or in a different legal entity, and does that change which model owns the relation?",
                "kind": "composition",
                "answer_data": [
                  "internal/external flag",
                  "counterparty organization identifier",
                  "owning model reference"
                ]
              },
              {
                "id": "q-affiliation-terms",
                "text": "Which instrument establishes the affiliation, over what period, and what obligations does it place on the unit?",
                "kind": "authority",
                "answer_data": [
                  "instrument reference",
                  "validity period",
                  "obligation summary",
                  "review date"
                ]
              }
            ],
            "data_elements": [
              {
                "id": "de-affiliation",
                "name": "unitAffiliation",
                "description": "Non-hierarchical relation between a unit and another unit or external body, with type and validity.",
                "value_kind": "object",
                "cardinality": "0..n",
                "required": false,
                "source_refs": [
                  "SRC-002",
                  "SRC-011"
                ]
              },
              {
                "id": "de-affiliation-instrument",
                "name": "affiliationInstrumentRef",
                "description": "Reference to the agreement or decision that establishes the affiliation.",
                "value_kind": "reference",
                "cardinality": "0..1",
                "required": false,
                "source_refs": [
                  "SRC-002"
                ]
              }
            ],
            "artifacts": [],
            "inline_only_rationale": "Affiliations are reference data resolved against counterparty records held by WM-ORG-001 or by contract models; the establishing instrument is an artifact of those models, not of this one."
          }
        },
        {
          "bundle": {
            "id": "change-and-time",
            "name": "Change and Time",
            "description": "How structure changes, what evidences the change, and how any past state can be reconstructed."
          },
          "layer": {
            "id": "structural-change-events",
            "name": "Structural Change Events",
            "description": "The acts that create, alter, combine, move or end units, and the lineage they produce."
          },
          "finding": {
            "id": "reorganization-act",
            "name": "Reorganization Act",
            "description": "A reorganization act is a decision that reshapes structure. It carries at least three distinct times - when it was decided, when it takes effect in the world, and when it was recorded - plus the deciding authority, the affected units and the change kind. W3C ORG's ChangeEvent 'resulted in a major change to an organization such as a merger or complete restructuring'; IFRS 8 then requires prior-period segment information to be restated or the change disclosed, so an act has consequences outside this model.",
            "source_refs": [
              "SRC-001",
              "SRC-009",
              "SRC-006"
            ],
            "questions": [
              {
                "id": "q-act-kind",
                "text": "What kind of act is this - establish, rename, reclassify, reparent, merge, split, transfer between organizations, or disband - and which units does it affect in which role?",
                "kind": "event",
                "answer_data": [
                  "act kind code",
                  "affected unit identifiers",
                  "role per unit (original/resulting/unchanged)",
                  "narrative summary"
                ]
              },
              {
                "id": "q-act-times",
                "text": "What are the decision instant, the effective instant and the record instant of this act, each with an explicit offset?",
                "kind": "temporal",
                "answer_data": [
                  "decision timestamp (RFC 3339)",
                  "effective timestamp (RFC 3339)",
                  "recorded timestamp (RFC 3339)",
                  "timezone rationale"
                ]
              },
              {
                "id": "q-act-authority",
                "text": "Which body took the decision, under which delegated power, and is the decision instrument attached as evidence?",
                "kind": "authority",
                "answer_data": [
                  "deciding body",
                  "power or instrument relied on",
                  "evidence document reference",
                  "approval quorum or signatures"
                ]
              },
              {
                "id": "q-act-consequences",
                "text": "Which downstream obligations does the act trigger - segment restatement, employee information and consultation, directory reprovisioning, contract novation?",
                "kind": "process",
                "answer_data": [
                  "triggered obligation codes",
                  "responsible party per obligation",
                  "deadline",
                  "completion status"
                ]
              },
              {
                "id": "q-retroactive",
                "text": "May an act be recorded with an effective date in the past, and what compensating controls apply to retroactive entries?",
                "kind": "exception",
                "answer_data": [
                  "retroactivity permitted boolean",
                  "maximum backdating window",
                  "approval role",
                  "audit marker"
                ]
              }
            ],
            "data_elements": [
              {
                "id": "de-act-kind",
                "name": "reorganizationActKind",
                "description": "Coded kind of structural change.",
                "value_kind": "code",
                "cardinality": "1",
                "required": true,
                "source_refs": [
                  "SRC-001",
                  "SRC-011"
                ]
              },
              {
                "id": "de-act-decision-time",
                "name": "decisionTimestamp",
                "description": "When the decision was taken, in RFC 3339 form with explicit offset.",
                "value_kind": "timestamp",
                "cardinality": "1",
                "required": true,
                "source_refs": [
                  "SRC-006"
                ]
              },
              {
                "id": "de-act-effective-time",
                "name": "effectiveTimestamp",
                "description": "When the change takes effect in the world.",
                "value_kind": "timestamp",
                "cardinality": "1",
                "required": true,
                "source_refs": [
                  "SRC-006"
                ]
              },
              {
                "id": "de-act-recorded-time",
                "name": "recordedTimestamp",
                "description": "When the change was captured in the record, kept separate from event time.",
                "value_kind": "timestamp",
                "cardinality": "1",
                "required": true,
                "source_refs": [
                  "SRC-006"
                ]
              },
              {
                "id": "de-act-affected",
                "name": "affectedUnits",
                "description": "Units affected by the act with their role as original or resulting participant.",
                "value_kind": "collection",
                "cardinality": "1..n",
                "required": true,
                "source_refs": [
                  "SRC-001"
                ]
              }
            ],
            "artifacts": [
              {
                "id": "reorganization-decision-record",
                "name": "Reorganization Decision Record",
                "description": "The evidenced record of one structural change act: decision instrument, authority, affected units and roles, the three timestamps, and the list of triggered downstream obligations.",
                "media_or_form": [
                  "decision record",
                  "signed instrument",
                  "structured event record"
                ],
                "serial": true,
                "identity_strategy": "Identified by the deciding body's official decision reference where one exists; otherwise a Dimension-assigned ULID. Never keyed by date alone, since several acts may share a date.",
                "source_refs": [
                  "SRC-001",
                  "SRC-009",
                  "SRC-006"
                ]
              }
            ],
            "inline_only_rationale": null
          }
        },
        {
          "bundle": {
            "id": "change-and-time",
            "name": "Change and Time",
            "description": "How structure changes, what evidences the change, and how any past state can be reconstructed."
          },
          "layer": {
            "id": "structural-change-events",
            "name": "Structural Change Events",
            "description": "The acts that create, alter, combine, move or end units, and the lineage they produce."
          },
          "finding": {
            "id": "unit-lineage",
            "name": "Unit Lineage and Succession",
            "description": "Merges and splits create many-to-many lineage that a simple parent pointer cannot express. W3C ORG uses originalOrganization and resultingOrganization on a ChangeEvent; ROR uses predecessor and successor relationships and keeps relationships on inactive or withdrawn records as historical tombstones. Lineage must survive the disappearance of its endpoints so that historical references still resolve.",
            "source_refs": [
              "SRC-001",
              "SRC-011"
            ],
            "questions": [
              {
                "id": "q-lineage-edges",
                "text": "Which units are the predecessors and successors of this unit, and through which act was each lineage edge created?",
                "kind": "provenance",
                "answer_data": [
                  "predecessor identifiers",
                  "successor identifiers",
                  "creating act reference",
                  "edge type"
                ]
              },
              {
                "id": "q-lineage-continuity",
                "text": "Does a merged or renamed unit retain its identifier as a continuation, or is a new identifier minted with a lineage edge to the old one?",
                "kind": "identity",
                "answer_data": [
                  "continuation rule per act kind",
                  "identifier retained boolean",
                  "lineage edge type"
                ]
              },
              {
                "id": "q-tombstone-resolution",
                "text": "When a consumer dereferences the identifier of a disbanded unit, what is returned - a tombstone, a redirect to the successor, or an error?",
                "kind": "interoperability",
                "answer_data": [
                  "resolution behaviour",
                  "tombstone payload fields",
                  "redirect target rule",
                  "status code convention"
                ]
              },
              {
                "id": "q-partial-transfer",
                "text": "When only part of a unit moves in a split, how is the partial transfer of establishment, mandate and staffing apportioned across the lineage edge?",
                "kind": "composition",
                "answer_data": [
                  "apportionment basis",
                  "transferred post identifiers",
                  "transferred mandate elements",
                  "residual retained by source"
                ]
              }
            ],
            "data_elements": [
              {
                "id": "de-predecessor",
                "name": "predecessorUnitRefs",
                "description": "Units from which this unit derives through a change act.",
                "value_kind": "collection",
                "cardinality": "0..n",
                "required": false,
                "source_refs": [
                  "SRC-001",
                  "SRC-011"
                ]
              },
              {
                "id": "de-successor",
                "name": "successorUnitRefs",
                "description": "Units into which this unit continues after a change act.",
                "value_kind": "collection",
                "cardinality": "0..n",
                "required": false,
                "source_refs": [
                  "SRC-001",
                  "SRC-011"
                ]
              },
              {
                "id": "de-lineage-act-ref",
                "name": "lineageActRef",
                "description": "Reference to the reorganization act that created the lineage edge.",
                "value_kind": "reference",
                "cardinality": "0..n",
                "required": false,
                "source_refs": [
                  "SRC-001"
                ]
              }
            ],
            "artifacts": [
              {
                "id": "unit-lineage-graph",
                "name": "Unit Lineage Graph",
                "description": "The directed acyclic graph of predecessor and successor edges across all acts, including tombstoned nodes, used to resolve historical unit references.",
                "media_or_form": [
                  "directed graph",
                  "edge list",
                  "provenance export"
                ],
                "serial": false,
                "identity_strategy": "Identified by organization identifier; nodes keyed by unitIdentifier including retired ones, edges keyed by the act reference that created them.",
                "source_refs": [
                  "SRC-001",
                  "SRC-011"
                ]
              }
            ],
            "inline_only_rationale": null
          }
        },
        {
          "bundle": {
            "id": "change-and-time",
            "name": "Change and Time",
            "description": "How structure changes, what evidences the change, and how any past state can be reconstructed."
          },
          "layer": {
            "id": "temporal-validity",
            "name": "Temporal Validity",
            "description": "Effective dating, bitemporality and reconstruction of the structure at any past instant."
          },
          "finding": {
            "id": "effective-dating-bitemporality",
            "name": "Effective Dating and Bitemporality",
            "description": "Every structural assertion - membership in a hierarchy, a reporting line, a mandate, an establishment line - carries a validity period in world time and a separate transaction period in record time. RFC 3339 requires a stated relationship to UTC and offers '-00:00' where the instant is known but the local offset is not, a distinction that matters for multinational effective dates. ROR's admin block separates created from last_modified, illustrating the record-time axis in practice.",
            "source_refs": [
              "SRC-006",
              "SRC-011"
            ],
            "questions": [
              {
                "id": "q-validity-period",
                "text": "What are the validity start and end of this assertion in world time, and is an open-ended end represented explicitly or by absence?",
                "kind": "temporal",
                "answer_data": [
                  "valid-from (RFC 3339)",
                  "valid-to (RFC 3339) or open marker",
                  "open-end convention",
                  "granularity (instant or date)"
                ]
              },
              {
                "id": "q-transaction-time",
                "text": "When was this assertion first recorded and when was it last modified or superseded in the record, independently of its world-time validity?",
                "kind": "provenance",
                "answer_data": [
                  "recorded-from (RFC 3339)",
                  "recorded-to (RFC 3339)",
                  "modifying actor",
                  "change reason"
                ]
              },
              {
                "id": "q-offset-policy",
                "text": "Which time offset is used for effective dates in a multi-jurisdiction organization, and is a legal local midnight or a UTC instant intended?",
                "kind": "constraint",
                "answer_data": [
                  "offset policy",
                  "legal-local-time flag",
                  "jurisdiction reference",
                  "conversion rule"
                ]
              },
              {
                "id": "q-gap-overlap",
                "text": "Are gaps or overlaps permitted in the validity of successive parent assignments for the same unit and hierarchy?",
                "kind": "validation",
                "answer_data": [
                  "gaps permitted boolean",
                  "overlaps permitted boolean",
                  "detection rule",
                  "remediation action"
                ]
              }
            ],
            "data_elements": [
              {
                "id": "de-valid-from",
                "name": "validFrom",
                "description": "Start of world-time validity for a structural assertion, RFC 3339 with explicit offset.",
                "value_kind": "timestamp",
                "cardinality": "1",
                "required": true,
                "source_refs": [
                  "SRC-006"
                ]
              },
              {
                "id": "de-valid-to",
                "name": "validTo",
                "description": "End of world-time validity, absent or explicitly open where still current.",
                "value_kind": "timestamp",
                "cardinality": "0..1",
                "required": false,
                "source_refs": [
                  "SRC-006"
                ]
              },
              {
                "id": "de-recorded-from",
                "name": "recordedFrom",
                "description": "Start of record-time validity, i.e. when the system first held this assertion.",
                "value_kind": "timestamp",
                "cardinality": "1",
                "required": true,
                "source_refs": [
                  "SRC-006",
                  "SRC-011"
                ]
              },
              {
                "id": "de-time-granularity",
                "name": "temporalGranularity",
                "description": "Whether the assertion is dated to an instant or to a legal calendar day in a stated jurisdiction.",
                "value_kind": "code",
                "cardinality": "0..1",
                "required": false,
                "source_refs": [
                  "SRC-006"
                ]
              }
            ],
            "artifacts": [],
            "inline_only_rationale": "Bitemporal stamps are per-assertion attributes that must travel with every edge and record; isolating them into an artifact would detach them from the assertions they qualify."
          }
        },
        {
          "bundle": {
            "id": "change-and-time",
            "name": "Change and Time",
            "description": "How structure changes, what evidences the change, and how any past state can be reconstructed."
          },
          "layer": {
            "id": "temporal-validity",
            "name": "Temporal Validity",
            "description": "Effective dating, bitemporality and reconstruction of the structure at any past instant."
          },
          "finding": {
            "id": "as-of-reconstruction",
            "name": "As-Of Reconstruction and Versioning",
            "description": "Consumers need the structure as it stood at a past instant, both as it actually was (world time) and as it was believed to be at the time (record time). IFRS 8's requirement to restate prior-period segment information after an internal reorganization, or otherwise disclose the change, makes exact historical reconstruction an external obligation rather than a convenience. Reconstruction outputs must be reproducible and identified.",
            "source_refs": [
              "SRC-009",
              "SRC-006",
              "SRC-011"
            ],
            "questions": [
              {
                "id": "q-asof-query",
                "text": "Given a world-time instant and a record-time instant, can the full unit set, hierarchy and reporting lines be reproduced deterministically?",
                "kind": "process",
                "answer_data": [
                  "query parameters accepted",
                  "determinism guarantee",
                  "excluded elements",
                  "reproduction test result"
                ]
              },
              {
                "id": "q-version-identity",
                "text": "How is a structure version identified so that two consumers can prove they are looking at the same state?",
                "kind": "identity",
                "answer_data": [
                  "structure version identifier",
                  "content digest",
                  "generation timestamp (RFC 3339)",
                  "digest algorithm"
                ]
              },
              {
                "id": "q-restatement-support",
                "text": "Does the model support producing both the pre-reorganization and post-reorganization views of a prior period for comparative reporting?",
                "kind": "requirement",
                "answer_data": [
                  "dual-view supported boolean",
                  "mapping between old and new units",
                  "apportionment method",
                  "limitations"
                ]
              },
              {
                "id": "q-history-truncation",
                "text": "How far back is full reconstruction guaranteed, and what happens to reconstruction after retention-driven deletion?",
                "kind": "retention",
                "answer_data": [
                  "reconstruction horizon",
                  "post-deletion behaviour",
                  "residual summary retained",
                  "disposition authority reference"
                ]
              }
            ],
            "data_elements": [
              {
                "id": "de-structure-version",
                "name": "structureVersionId",
                "description": "Identifier of a reproducible structure state.",
                "value_kind": "identifier",
                "cardinality": "1",
                "required": true,
                "source_refs": [
                  "SRC-011"
                ]
              },
              {
                "id": "de-content-digest",
                "name": "contentDigest",
                "description": "Cryptographic digest over the canonical serialisation of the structure state.",
                "value_kind": "text",
                "cardinality": "0..1",
                "required": false,
                "source_refs": [
                  "SRC-011"
                ]
              },
              {
                "id": "de-asof-params",
                "name": "asOfParameters",
                "description": "The world-time and record-time instants that parameterise a reconstruction.",
                "value_kind": "object",
                "cardinality": "0..1",
                "required": false,
                "source_refs": [
                  "SRC-006"
                ]
              }
            ],
            "artifacts": [
              {
                "id": "structure-as-of-view",
                "name": "Structure As-Of View",
                "description": "A frozen, digest-identified export of the complete unit set, hierarchies, reporting lines and mandates valid at a stated world-time and record-time pair.",
                "media_or_form": [
                  "frozen dataset export",
                  "graph snapshot",
                  "signed archive"
                ],
                "serial": true,
                "identity_strategy": "Identified by structureVersionId plus the as-of pair; content digest is the integrity anchor. Dates alone are never used as the identifier.",
                "source_refs": [
                  "SRC-006",
                  "SRC-009",
                  "SRC-011"
                ]
              }
            ],
            "inline_only_rationale": null
          }
        }
      ],
      "functions": [
        {
          "id": "resolve-unit-identity",
          "name": "Resolve Unit Identity",
          "description": "Resolve any inbound reference - master-system identifier, ISO/IEC 6523 organization part identifier, alias, former name, LDAP distinguished name or IdP group id - to the single current unit record or to a tombstone with a successor pointer.",
          "inputs": [
            "candidate identifier or name string",
            "identifier scheme hint",
            "parent organization identifier",
            "as-of instant (RFC 3339)"
          ],
          "outputs": [
            "resolved unitIdentifier or tombstone",
            "resolution confidence and method",
            "successor unit reference where applicable"
          ],
          "preconditions": [
            "The unit register is loaded for the stated parent organization",
            "The alias and lineage indexes cover the requested as-of instant"
          ],
          "effects": [
            "Emits a resolution audit entry with the input, method and outcome",
            "Never mutates the unit record"
          ],
          "source_refs": [
            "SRC-001",
            "SRC-007",
            "SRC-011",
            "SRC-012"
          ]
        },
        {
          "id": "validate-structure-graph",
          "name": "Validate Structure Graph",
          "description": "Evaluate integrity rules over a structure version: acyclicity within each named hierarchy, single parent per hierarchy per validity interval, no orphans, referential integrity to WM-ORG-001 and WM-ORG-004, temporal gap and overlap rules, and segregation-of-duties constraints.",
          "inputs": [
            "structureVersionId",
            "rule set identifier and version",
            "severity threshold"
          ],
          "outputs": [
            "validation result set with severity per finding",
            "blocking/non-blocking verdict"
          ],
          "preconditions": [
            "The structure version is fully materialised and immutable",
            "The rule set version is published and resolvable"
          ],
          "effects": [
            "Produces a Structure Validation Report artifact",
            "May block a pending write when blocking failures are present"
          ],
          "source_refs": [
            "SRC-001",
            "SRC-002",
            "SRC-014"
          ]
        },
        {
          "id": "reconstruct-structure-as-of",
          "name": "Reconstruct Structure As Of",
          "description": "Return the unit set, hierarchies, reporting lines and mandates valid at a given world-time instant as recorded at a given record-time instant, producing a deterministic, digest-identified view.",
          "inputs": [
            "world-time instant (RFC 3339)",
            "record-time instant (RFC 3339)",
            "hierarchy identifiers to include",
            "disclosure class"
          ],
          "outputs": [
            "Structure As-Of View with structureVersionId and content digest",
            "list of elements excluded by disclosure class"
          ],
          "preconditions": [
            "Bitemporal stamps exist on all included assertions",
            "The requested instants fall inside the reconstruction horizon"
          ],
          "effects": [
            "Materialises a frozen, immutable as-of export",
            "Records the query parameters and digest for reproducibility"
          ],
          "source_refs": [
            "SRC-006",
            "SRC-009",
            "SRC-011"
          ]
        },
        {
          "id": "apply-reorganization-act",
          "name": "Apply Reorganization Act",
          "description": "Apply an evidenced structural change - establish, rename, reclassify, reparent, merge, split, transfer or disband - creating lineage edges, closing and opening validity intervals, and registering downstream obligations.",
          "inputs": [
            "reorganization act record with kind and affected units",
            "decision, effective and record timestamps (RFC 3339)",
            "deciding authority and evidence reference",
            "consultation evidence where required"
          ],
          "outputs": [
            "updated unit records with closed and opened validity intervals",
            "new lineage edges",
            "list of triggered downstream obligations"
          ],
          "preconditions": [
            "The deciding body holds the delegated authority for the act kind",
            "Pre-commit validation passes or an approved override exists",
            "Any jurisdictional consultation precondition is evidenced as complete"
          ],
          "effects": [
            "Mutates the structure graph as of the effective instant",
            "Produces a Reorganization Decision Record artifact",
            "Notifies segment reporting, directory provisioning and contract owners"
          ],
          "source_refs": [
            "SRC-001",
            "SRC-009",
            "SRC-011",
            "SRC-014"
          ]
        },
        {
          "id": "derive-org-chart",
          "name": "Derive Org Chart Projection",
          "description": "Generate a hierarchy view for a named hierarchy at an as-of instant, containing unit names and kinds only, with mandate detail and staffing deliberately excluded.",
          "inputs": [
            "hierarchy identifier",
            "as-of instant (RFC 3339)",
            "root unit identifier",
            "maximum depth"
          ],
          "outputs": [
            "Organization Chart Projection artifact",
            "loss manifest declaring omitted elements"
          ],
          "preconditions": [
            "The named hierarchy exists and has valid edges at the as-of instant",
            "The requesting principal holds read scope for the hierarchy"
          ],
          "effects": [
            "Emits a serial projection instance bound to its source structure version",
            "Marks the output as non-authoritative and non-reimportable"
          ],
          "source_refs": [
            "SRC-001",
            "SRC-011"
          ]
        },
        {
          "id": "evaluate-mandate-conflict",
          "name": "Evaluate Mandate Conflict",
          "description": "Detect overlapping or incompatible remits across units and breaches of authority limits or independence requirements, before or after a proposed structural change.",
          "inputs": [
            "proposed or current structure version",
            "mandate scope assertions",
            "segregation and independence rule set"
          ],
          "outputs": [
            "conflict findings with affected units and rule references",
            "recommended resolution or required waiver"
          ],
          "preconditions": [
            "Mandates are expressed with structured scope, not narrative only",
            "The rule set encodes incompatible mandate pairs"
          ],
          "effects": [
            "Records conflicts as validation findings with severity",
            "Triggers a waiver workflow when an exception is sought"
          ],
          "source_refs": [
            "SRC-014",
            "SRC-001",
            "SRC-003"
          ]
        },
        {
          "id": "compute-headcount-rollup",
          "name": "Compute Headcount Rollup",
          "description": "Aggregate staffing measurements up a named hierarchy under a declared counting basis and period convention, applying suppression where a cell falls below the minimum size.",
          "inputs": [
            "hierarchy identifier",
            "as-of date",
            "counting basis (headcount or FTE)",
            "period convention",
            "minimum cell size"
          ],
          "outputs": [
            "rolled-up figures per unit with basis and period stated",
            "suppression markers distinguishing suppressed values from true zeros"
          ],
          "preconditions": [
            "Underlying snapshots share a compatible basis and population definition",
            "The minimum cell size policy is resolved for the audience"
          ],
          "effects": [
            "Appends to the Headcount Snapshot Series artifact",
            "Logs each suppression with the rule applied"
          ],
          "source_refs": [
            "SRC-015",
            "SRC-006"
          ]
        },
        {
          "id": "reconcile-external-directory",
          "name": "Reconcile External Directory",
          "description": "Compare LDAP or SCIM representations of units against the governed structure, report drift, and push corrections outward without ever accepting the directory as a source of truth.",
          "inputs": [
            "directory export (LDAP entries or SCIM Groups and Enterprise User attributes)",
            "current structure version",
            "name-matching policy"
          ],
          "outputs": [
            "drift report of name, membership and hierarchy differences",
            "outbound correction plan"
          ],
          "preconditions": [
            "A mapping from unit identifiers to directory distinguished names or group ids exists",
            "The directory export carries a generation timestamp"
          ],
          "effects": [
            "Never mutates the governed structure from directory content",
            "Queues outbound provisioning changes and records unresolved name-only matches"
          ],
          "source_refs": [
            "SRC-004",
            "SRC-005"
          ]
        },
        {
          "id": "emit-standards-mapping",
          "name": "Emit Standards Mapping",
          "description": "Serialise the structure into a target vocabulary - W3C ORG, CPOV, FHIR Organization, schema.org, or an ISO/IEC 6523 party identifier - using the versioned crosswalk and attaching a fidelity declaration.",
          "inputs": [
            "structureVersionId",
            "target vocabulary identifier and version",
            "scope filter",
            "disclosure class"
          ],
          "outputs": [
            "target-vocabulary serialisation",
            "fidelity and non-conformance declaration"
          ],
          "preconditions": [
            "A crosswalk entry exists for every included element and target version",
            "No conformance claim is asserted without a referenced test result"
          ],
          "effects": [
            "Produces a serial export bound to the crosswalk version used",
            "Records any element dropped for lack of a target term"
          ],
          "source_refs": [
            "SRC-001",
            "SRC-002",
            "SRC-003",
            "SRC-007",
            "SRC-008"
          ]
        },
        {
          "id": "apply-disposition",
          "name": "Apply Disposition",
          "description": "Execute the approved retention schedule over structure records: destroy, transfer to archive or flag for review, while preserving the tombstones and lineage edges required for historical reference resolution.",
          "inputs": [
            "retention class",
            "disposition schedule reference and version",
            "evaluation date",
            "active legal holds"
          ],
          "outputs": [
            "disposition action log per record",
            "list of records retained under hold or as permanent"
          ],
          "preconditions": [
            "A governed disposition authority covers every record class in scope",
            "No legal hold applies to the record",
            "Tombstone and lineage minimums are defined"
          ],
          "effects": [
            "Irreversibly removes or transfers eligible records",
            "Reduces the reconstruction horizon and records the new horizon",
            "Preserves lineage edges and tombstones for resolvability"
          ],
          "source_refs": [
            "SRC-016",
            "SRC-011"
          ]
        },
        {
          "id": "assign-unit-mandate",
          "name": "Assign mandate",
          "description": "Attach or withdraw a remit, purpose code and delegation source on a unit for a validity interval.",
          "inputs": [
            "unit-master-id",
            "purpose-text",
            "purpose-code",
            "delegation-source-id",
            "mandate-valid-from"
          ],
          "outputs": [
            "unit-mandate-record"
          ],
          "preconditions": [
            "An effective time is supplied and, where the change is material, an authorizing framework is referenced."
          ],
          "effects": [
            "A remit, purpose code and delegation source are attached to or withdrawn from the unit for the stated validity interval."
          ],
          "source_refs": [
            "SRC-017",
            "SRC-003"
          ]
        },
        {
          "id": "seat-post-in-unit",
          "name": "Seat post in unit",
          "description": "Create or attach an established post in a unit independently of any holder. Occupancy is not performed here.",
          "inputs": [
            "unit-master-id",
            "post-label",
            "post-role-id",
            "post-valid-from"
          ],
          "outputs": [
            "establishment-register"
          ],
          "preconditions": [
            "The acting party is the designated establishment function of the parent organization."
          ],
          "effects": [
            "An established post exists in the unit independently of any holder, and no occupancy or employment fact is asserted."
          ],
          "source_refs": [
            "SRC-017",
            "SRC-020"
          ]
        },
        {
          "id": "assert-reporting-line",
          "name": "Assert reporting line",
          "description": "Record a supervisory or dotted-line reporting edge between units or posts with validity.",
          "inputs": [
            "source-id",
            "reports-to-id",
            "reports-to-kind",
            "reporting-valid-from"
          ],
          "outputs": [
            "org-chart-edge"
          ],
          "preconditions": [],
          "effects": [
            "A supervisory or dotted-line reporting edge exists between the source and target for the stated validity interval, without altering containment."
          ],
          "source_refs": [
            "SRC-017"
          ]
        },
        {
          "id": "record-staffing-snapshot",
          "name": "Record staffing snapshot",
          "description": "Store a dated established and filled count for a unit with basis and observation time. Treat as an extension until a primary unit-level metric standard is cited.",
          "inputs": [
            "unit-master-id",
            "as-of-time",
            "established-count",
            "filled-count",
            "count-basis"
          ],
          "outputs": [
            "staffing-snapshot-record"
          ],
          "preconditions": [],
          "effects": [
            "A dated established and filled count is appended for the unit with basis and observation time, without rewriting structure."
          ],
          "source_refs": [
            "SRC-023",
            "SRC-017"
          ]
        }
      ],
      "composition": [
        {
          "target": "WM-ORG-001 Organization",
          "relation": "REFERENCE",
          "purpose": "Every unit resolves to exactly one parent organization, which holds legal identity, registration and external identifiers. W3C ORG grounds the dependency: a unit 'only has full recognition within the context of that Organization'.",
          "required": true,
          "source_refs": [
            "SRC-001",
            "SRC-013"
          ]
        },
        {
          "target": "WM-ORG-004 Position",
          "relation": "CHILD",
          "purpose": "Units contain or govern established posts. This model holds the establishment count, seating and unit-level occupancy; the post as an object that 'exists independently of who fills it' is defined in WM-ORG-004.",
          "required": false,
          "source_refs": [
            "SRC-001"
          ]
        },
        {
          "target": "Employment / role assignment model",
          "relation": "REFERENCE",
          "purpose": "Employment records fill the posts seated in a unit and are the derivation source for unit-level occupancy counts; persons and contracts never enter this model.",
          "required": false,
          "source_refs": [
            "SRC-001",
            "SRC-005"
          ]
        },
        {
          "target": "Charter / constitutive powers model",
          "relation": "REFERENCE",
          "purpose": "Unit mandates trace upward to powers held by the organization; ISO 37000 requires delegation to be formalized and delegators to remain accountable, so the upstream power must be resolvable.",
          "required": false,
          "source_refs": [
            "SRC-014"
          ]
        },
        {
          "target": "Site / Location model",
          "relation": "REFERENCE",
          "purpose": "A unit may be associated with one or more premises, but FHIR keeps Location distinct from Organization and Eurostat's local unit is a geographic statistical construct, so premises are referenced rather than embedded.",
          "required": false,
          "source_refs": [
            "SRC-002",
            "SRC-010"
          ]
        },
        {
          "target": "Stewardship model (S1)",
          "relation": "MIX-IN",
          "purpose": "The parent organization owns the structure record and units have no independent standing; ownership, custodianship and accountability facets come from the stewardship model.",
          "required": true,
          "source_refs": [
            "SRC-014",
            "SRC-013"
          ]
        },
        {
          "target": "Access grant model (S2)",
          "relation": "REFERENCE",
          "purpose": "Disclosure classes defined here are enforced by grants issued in the access model; this model supplies the scoped projections and suppression parameters, not the grant machinery.",
          "required": true,
          "source_refs": [
            "SRC-015",
            "SRC-003"
          ]
        },
        {
          "target": "Audit trail model (S4)",
          "relation": "MIX-IN",
          "purpose": "Reorganization acts, mandate changes, waivers and disposition actions require immutable audit facets with separate event and record timestamps.",
          "required": true,
          "source_refs": [
            "SRC-006",
            "SRC-016"
          ]
        },
        {
          "target": "W3C Organization Ontology (org:)",
          "relation": "ALIGN",
          "purpose": "Primary structural alignment for OrganizationalUnit, hasUnit/unitOf, subOrganizationOf, purpose, classification, Post, Site and ChangeEvent. Unit-to-unit reportsTo is declared an extension, since org:reportsTo binds Agents and Posts.",
          "required": false,
          "source_refs": [
            "SRC-001"
          ]
        },
        {
          "target": "Core Public Organisation Vocabulary (CPOV) v2.1.2",
          "relation": "ALIGN",
          "purpose": "Public-sector profile alignment for hasUnit, code-valued purpose (COFOG), classification and spatial coverage; applicable only where the parent organization is a public body.",
          "required": false,
          "source_refs": [
            "SRC-003"
          ]
        },
        {
          "target": "HL7 FHIR Organization / OrganizationAffiliation (R5)",
          "relation": "ALIGN",
          "purpose": "Healthcare-sector projection where departments are Organization instances chained by partOf and non-hierarchical relations use OrganizationAffiliation; a known structural conflict with the distinct-unit-class model.",
          "required": false,
          "source_refs": [
            "SRC-002"
          ]
        },
        {
          "target": "ISO/IEC 6523 organization part identification (via Peppol ICD registry)",
          "relation": "ALIGN",
          "purpose": "External addressing of a unit as an organization part under the parent's ICD and organization identifier, used for e-business party and delivery-location identification.",
          "required": false,
          "source_refs": [
            "SRC-007",
            "SRC-008"
          ]
        },
        {
          "target": "LDAP (RFC 4519) and SCIM (RFC 7643) directory schemas",
          "relation": "ALIGN",
          "purpose": "Outbound-only projection targets. Both carry unit information as names without identifiers, validity or typed edges, so alignment is declared lossy and re-import is prohibited.",
          "required": false,
          "source_refs": [
            "SRC-004",
            "SRC-005"
          ]
        },
        {
          "target": "Statistical units framework (Council Regulation (EEC) No 696/93)",
          "relation": "ALIGN",
          "purpose": "Mapping of internal units to enterprise, kind-of-activity unit and local unit for statistical reporting, recorded as a derivation with explicit boundary mismatch rather than as equivalence.",
          "required": false,
          "source_refs": [
            "SRC-010"
          ]
        },
        {
          "target": "IFRS 8 operating segment determination",
          "relation": "ALIGN",
          "purpose": "The internal reporting hierarchy is an input to segment identification under the management approach, and reorganization acts trigger the restate-or-disclose obligation; segment determination itself stays outside this model.",
          "required": false,
          "source_refs": [
            "SRC-009"
          ]
        }
      ],
      "researchAdjudication": {
        "providerMode": "dual-provider",
        "activeProviders": [
          "claude",
          "grok"
        ],
        "waivedProviders": [],
        "providerPolicy": {},
        "boundaryDecision": {
          "entry_kind": "entity",
          "status": "accepted",
          "rationale": "Both providers independently classify WM-ORG-002 as an entity, and the base draws the boundary on every side with source-referenced neighbour distinctions: legal personality to WM-ORG-001 (W3C ORG FormalOrganization vs OrganizationalUnit; GLEIF issues LEIs only to legal entities), the post as an object to WM-ORG-004 (org:Post exists independently of its holder), premises to a site model (FHIR Location vs Organization), statistical observation units to a statistics model (Reg. 696/93), and derived segments to financial reporting (IFRS 8 management approach with permitted aggregation). Directory content (RFC 4519 ou, RFC 7643 department) is fixed as a lossy projection and never a system of record. The one live boundary disagreement is the unit-to-site association, which the secondary provider places in scope; the base exclusion is retained for this pass and the association is deferred rather than forced into a layer that does not fit it."
        },
        "decisions": [
          {
            "concept": "Base provider selection",
            "disposition": "accepted claude as base",
            "rationale": "Not chosen for size. The base states in_scope, out_of_scope and seven source-referenced neighbour distinctions that close the boundary on every side, and its adversarial checks show the boundary was tested rather than asserted. The secondary provider leaves the site boundary open and treats multi-hierarchy structure as an omission."
          },
          {
            "concept": "Entry kind",
            "disposition": "accepted as entity",
            "rationale": "Both providers converge on entity independently, and the node behaves as a persistent identified thing with lifecycle, relationships and versioned state rather than as an event, a policy or a service."
          },
          {
            "concept": "W3C ORG OrganizationalCollaboration typing",
            "disposition": "accepted into unit-classification",
            "rationale": "Fills a gap the base itself declares unresolved, is anchored in the base's own tier-1 source, and supplies the test that keeps cross-organization bodies out of the unit set instead of silently absorbing them."
          },
          {
            "concept": "ChangeEvent conformance threshold",
            "disposition": "accepted into structural-change-events",
            "rationale": "Prevents the base from over-claiming ORG semantics by treating every rename or reparent as a ChangeEvent, and adds CPOV hasFormalFramework as the link from the act to its authorizing instrument."
          },
          {
            "concept": "Unit-to-site and contact-point linkage",
            "disposition": "deferred",
            "rationale": "Genuinely evidence-backed in W3C ORG via org:Site, hasSite, hasPrimarySite and hasRegisteredSite, and therefore not rejected on evidence. But the base excludes premises by explicit adversarial decision and no existing base layer hosts a placement finding, so importing it would require inventing structure. Held open as a boundary question."
          },
          {
            "concept": "Grok master-and-global-identifiers finding",
            "disposition": "rejected as duplicative",
            "rationale": "The base already covers master-system assignment, ISO/IEC 6523 organization-part addressing, identifier stability across rename and reparent, and the UUID/ULID fallback. Only the point that an LDAP distinguished name is a naming address rather than a persistent identifier is additive, and it belongs as a crosswalk note on projection fidelity, not a new finding."
          },
          {
            "concept": "Grok lexical-names finding",
            "disposition": "rejected as duplicative",
            "rationale": "The base's naming finding already carries official name, aliases, former names and the rule that names are never identity. The SKOS prefLabel/altLabel/notation binding and CPOV's at-most-one-preferred-label-per-language cardinality are refinements to that finding, to be folded into the crosswalk rather than added as separate structure."
          },
          {
            "concept": "Grok head-of-unit finding",
            "disposition": "rejected as duplicative",
            "rationale": "The base's accountable-role finding already models the head as a post or Membership slot with acting, interim and vacant states and keeps person occupancy out of scope. org:headOf as a specialization of memberOf is a mapping detail for the crosswalk."
          },
          {
            "concept": "Grok unit-purpose finding",
            "disposition": "rejected as duplicative",
            "rationale": "The base's mandate-scope finding covers remit statement, delegating instrument, spatial and functional limits, and the CPOV COFOG recommendation with its public-sector restriction already recorded as a conflict."
          },
          {
            "concept": "Grok posts-in-unit finding",
            "disposition": "rejected as a finding, escalated to a hold",
            "rationale": "Duplicates the base's authorized-post-complement, but carries a caveat the base lacks: neither W3C ORG nor the ISO material consulted defines establishment counts, grades or pay bands, so those are local controls rather than standard properties. That evidentiary limit is recorded as a publication hold instead of new structure."
          },
          {
            "concept": "Grok predecessor-successor finding",
            "disposition": "rejected as duplicative",
            "rationale": "The base's unit-lineage finding covers predecessor and successor edges, identifier continuity, tombstone dereferencing and partial transfer in a split. CPOV prev/next and the dual-running overlap window are deferred as crosswalk and validation detail."
          },
          {
            "concept": "Grok atomic mutation functions",
            "disposition": "rejected as subsumed",
            "rationale": "establish-unit, reparent-unit, merge-or-split-units and disband-unit are decompositions of the base's apply-reorganization-act, which already opens and closes validity intervals, creates lineage edges and registers downstream obligations. Importing them would fork the write path."
          },
          {
            "concept": "Grok disclose-org-chart function",
            "disposition": "rejected as duplicative",
            "rationale": "The base already separates derive-org-chart, which deliberately omits mandate and staffing, from the structure-disclosure package and its scoping rules; a second disclosure entry point would blur that separation."
          },
          {
            "concept": "Unit-to-unit reporting stance",
            "disposition": "accepted base framing",
            "rationale": "Both providers agree org:reportsTo is defined between Agents and Posts. The base's stricter treatment of unit-level edges as a declared non-conformant extension with a mapping rule governs, and the imported assert-reporting-line function must write that declaration."
          },
          {
            "concept": "Measurement coverage status",
            "disposition": "reclassified to extension-grade",
            "rationale": "The base marks measurement covered on ESRS S1-6, which is an undertaking-level disclosure standard, while the secondary provider marks it a gap because no primary source defines a unit-grain metric. The honest position is that unit-level headcount and FTE are operationally necessary but standards-thin."
          },
          {
            "concept": "Concurrent named hierarchies",
            "disposition": "retained from base",
            "rationale": "The base models managerial, legal, cost and functional hierarchies as separately governed edge sets with per-hierarchy single-parent constraints and ties the choice to IFRS 8's management approach; the secondary provider lists typed multi-hierarchy collections as an omission, so the base is strictly stronger here."
          }
        ],
        "publicationHolds": [
          "Source and live-version verification is outstanding for all sixteen base sources and for the two imported W3C ORG and CPOV anchors. Resolve the dated W3C ORG REC URI against the latest-version URI, confirm CPOV 2.1.2, schema.org v30.0 and the Peppol ICD list are still current, and pin FHIR deliberately, since the base cites R5 and the secondary provider cites R4.",
          "ISO-derived structure is guidance-grade, not requirement-grade. ISO 37000:2021, ISO 30414:2018, ISO 15489-1:2016 and ISO/IEC 6523-1:2023 are paywalled and were reviewed only through committee decks, catalogue metadata and deployment profiles, so the delegated-authority, assurance and segregation findings must not be published as normatively sourced until clause text is verified.",
          "ESRS S1-6 clause text was not machine-parsed; headcount, FTE, breakdown and the fifty-employee country threshold are stated at summary level and must be checked against Annex I of Commission Delegated Regulation (EU) 2023/2772 before any compliance-adjacent claim.",
          "Unit-grain staffing measurement has no primary standard. Established-versus-filled counts, budgeted FTE and establishment complement are local controls; publish the measurement layer and record-staffing-snapshot as extension-grade with that limitation visible.",
          "Multi-profile validation is incomplete. The model was tested chiefly against public-sector (CPOV/COFOG), healthcare (FHIR), EU reporting (IFRS 8, ESRS S1), directory (LDAP/SCIM) and e-invoicing (ISO/IEC 6523) profiles. Private-sector matrix organizations, military, academic-collegiate, ecclesiastical and cooperative unit forms are not validated and must not be presented as covered.",
          "Council Regulation (EEC) No 696/93 was not retrieved from EUR-Lex; the statistical-unit boundary currently rests on a Eurostat glossary entry that cites it, and must be confirmed against the regulation text.",
          "Regional scope must be stated on the face of any draft: CPOV, ESRS and the statistical-unit framework are EU instruments, NARA General Records Schedules bind US federal agencies only, financial alignment assumes IFRS rather than ASC 280, and employee consultation duties before a reorganization are jurisdiction-conditioned."
        ],
        "deferredResearch": [
          "Unit-to-site association: decide whether org:hasSite, hasPrimarySite and hasRegisteredSite belong here as a bounded reference or entirely in the site model. The base excludes premises after an explicit adversarial test; the secondary provider places the link in scope on W3C ORG evidence. Resolve before the next boundary pass, and add a placement layer only if the reference is accepted.",
          "CPOV range and lineage detail: CPOV ranges unitOf at Public Organisation and states a unit cannot exist on its own, which is narrower than W3C ORG's units-of-units, and CPOV prev/next cover rename and split sequences that may retain identity. Fold both into the crosswalk with explicit range, cardinality and fidelity notes.",
          "Popolo Organization and Post as an additional crosswalk target, including its single-classification restriction, its rejection of org:holds in favour of Membership, and its distinct former-name property, which few vocabularies provide.",
          "Cost-centre, profit-centre and funds-centre ERP hierarchies: confirm whether these are admitted as named concurrent hierarchies inside this model or remain finance masters referenced from it, since both providers flag them and neither resolves the boundary.",
          "Works councils, union structures and co-determination bodies: both providers record these as an unmodelled gap that nonetheless gates reorganization effectiveness. Determine whether they become a sibling model or remain a jurisdiction-conditioned precondition on the act.",
          "Establishment-count standardization: search for a primary, unit-grain source defining authorized post complement, grade and budgeted FTE. Absent one, keep the establishment findings marked as local control rather than standard property.",
          "LDAP distinguished-name instability under reparenting, and the name-reuse-after-disbandment collision case with x500UniqueIdentifier-style disambiguators, as validation rules on the identity and projection-fidelity findings.",
          "Informal and shadow structure, temporary project organizations and de facto reporting: both providers record these as gaps with no authoritative source. Confirm the gap stands rather than inventing structure to close it."
        ]
      }
    },
    "team": {
      "publication": {
        "status": "published",
        "adjudicationStatus": "reviewable-draft",
        "publishableCanonical": false,
        "generatedAt": "2026-08-24T02:00:48Z",
        "synthesisSha256": "c626866472ec1be766b3ce256f0e3f375118fb1c462fac4921a367f925ca0bc4",
        "providerMode": "dual-provider",
        "providers": [
          "Claude",
          "Grok"
        ],
        "waivedProviders": []
      },
      "model": {
        "registry_id": "vr.wm-org-003",
        "model_id": "WM-ORG-003",
        "name": "Team",
        "entry_kind": "aggregate",
        "purpose": "Provide a format-neutral governed context structure that lets an AI agent identify, constitute, staff, operate, measure, change and retire a team as a bounded working collective, without duplicating the containing organization (WM-ORG-001) or the reusable position catalogue (WM-ORG-004).",
        "scope_statement": "A Team is a named, bounded collective of two or more actors constituted to perform work together under a shared mandate, whose membership is expressed as time-bounded assignment facts. The model is an aggregate: the team node is the root and the membership-assignment records are governed inside it, following the n-ary reification pattern of org:Membership and FHIR CareTeam.participant. Scope covers identity, classification and capability typing, charter and authority, membership and capability composition, lifecycle and structural change, operating interfaces and footprint, measurement binding, and the governance of team records. Storage and interface (JSON, YAML, Markdown, Git, MCP, MongoDB) are projections and carry no semantics here.",
        "in_scope": [
          "Team instance identity, naming, classification and capability tier",
          "Charter, mandate, decision rights, accountable owner and reporting line",
          "Time-bounded membership assignments, in-team roles, external and non-human participants",
          "Capacity, minimum composition constraints, competence coverage and qualification currency",
          "Team status lifecycle and structural change events (formation, merge, split, transfer, dissolution)",
          "Operating interfaces, dependencies, site footprint and time coverage",
          "Binding of team-level metrics and evidence to a stated observation window",
          "Provenance, access scope, privacy, retention and interoperability projections of team records"
        ],
        "out_of_scope": [
          "Legal-entity attributes, registration, LEI and corporate structure of the containing organization (WM-ORG-001)",
          "Reusable position definitions, job architecture, grading and job descriptions (WM-ORG-004)",
          "Person master data, employment contract terms, payroll and benefits (worker/person models and HR Open payroll/compensation domains)",
          "Project, product, work-item and portfolio semantics; a team is not a project",
          "Definition of individual competences and occupations, which are referenced to ESCO/ISCO-08 rather than restated",
          "Metric formulae for human capital disclosure, which are referenced to ISO 30414:2025 rather than restated"
        ],
        "boundary_notes": [
          {
            "neighbor": "WM-ORG-001 Organization (legal or formal organization)",
            "distinction": "FHIR states that Organization is 'a formally recognized entity' while a Group 'represents an undifferentiated collection lacking formal legal recognition'; W3C org distinguishes org:FormalOrganization from org:OrganizationalUnit, which is only meaningful as a part of a formal organization. A team instance therefore never carries legal-entity identity or LEI eligibility; it references exactly one containing organization context.",
            "source_refs": [
              "SRC-001",
              "SRC-003",
              "SRC-015"
            ]
          },
          {
            "neighbor": "WM-ORG-004 Position",
            "distinction": "org:Post is a reusable position that exists independently of who holds it (org:holds / org:heldBy), whereas the in-team role is the n-ary binding of an agent to this team for a period (org:Membership, CareTeam.participant.role). Position definitions stay in WM-ORG-004; the binding stays in this aggregate.",
            "source_refs": [
              "SRC-001",
              "SRC-002"
            ]
          },
          {
            "neighbor": "Identity-provider group / SCIM Group",
            "distinction": "A SCIM Group is an access-control grouping whose membership is authoritative for entitlement, with members mutable only through the Group resource. A team may project to a Group but is not defined by it: teams carry mandate, capability typing and lifecycle that SCIM does not model.",
            "source_refs": [
              "SRC-003",
              "SRC-004"
            ]
          },
          {
            "neighbor": "Undifferentiated cohort or list (FHIR Group, definitional membership)",
            "distinction": "FHIR Group supports 'definitional' membership by characteristic; a team requires 'enumerated' membership with identified participants and roles. Rule-defined cohorts are not teams under this model.",
            "source_refs": [
              "SRC-003"
            ]
          },
          {
            "neighbor": "Care team / clinical team",
            "distinction": "FHIR CareTeam is subject-scoped (bound to a Patient or Group) and carries security category Patient. This model is subject-agnostic; subject-scoped teams are an EXTEND profile, not the base case.",
            "source_refs": [
              "SRC-002"
            ]
          },
          {
            "neighbor": "NIMS typed resource team",
            "distinction": "FEMA types a team definition by minimum capability (Type 1-4) and publishes it as a versioned catalogue entry with its own identifier; that is a team *type* artifact, not a team *instance*. Instance identity must not reuse the typing definition identifier.",
            "source_refs": [
              "SRC-007",
              "SRC-008"
            ]
          },
          {
            "neighbor": "Public-facing department (schema.org)",
            "distinction": "schema.org department is intended for divisions with a distinguishable public presence (separate URL, logo or hours). Most internal teams do not qualify, so department is an optional publication projection only.",
            "source_refs": [
              "SRC-011"
            ]
          }
        ]
      },
      "selected_findings": [
        {
          "bundle": {
            "id": "identity-and-boundary",
            "name": "Identity and boundary",
            "description": "What makes a team instance the same thing over time, and what it is not."
          },
          "layer": {
            "id": "team-identity",
            "name": "Team identity",
            "description": "Identifier assignment, naming and the entity distinctions that keep a team from collapsing into an organization, a group or a position."
          },
          "finding": {
            "id": "team-identifier-assignment",
            "name": "Team instance identifier assignment",
            "description": "A team instance normally has no authoritative external register. SCIM supplies a server-assigned immutable id plus a client-supplied externalId; FHIR CareTeam and Group both carry 0..* business identifiers; GLEIF/ISO 17442 covers legal entities only. Identity therefore resolves in priority order: authoritative master-system identifier (HRIS org-unit key or IdP group id), then a governed IRI in the adopting Dimension's namespace, then a Dimension-minted UUID or ULID. Names and dates are never identifiers.",
            "source_refs": [
              "SRC-002",
              "SRC-003",
              "SRC-004",
              "SRC-015"
            ],
            "questions": [
              {
                "id": "q-master-system",
                "text": "Which system of record is authoritative for this team's identifier, and what is the key?",
                "kind": "identity",
                "answer_data": [
                  "Master system name and instance",
                  "Native key value",
                  "Key immutability and reuse policy"
                ]
              },
              {
                "id": "q-id-fallback",
                "text": "If no master-system key exists, which governed IRI or Dimension-minted UUID/ULID is assigned, and by whom?",
                "kind": "identity",
                "answer_data": [
                  "Assigned identifier value and scheme",
                  "Minting authority",
                  "Assignment timestamp (RFC 3339)"
                ]
              },
              {
                "id": "q-alt-ids",
                "text": "Which alternate business identifiers must be carried, and which are merely correlational?",
                "kind": "interoperability",
                "answer_data": [
                  "Identifier system URI",
                  "Identifier value",
                  "Authoritative or correlational flag"
                ]
              },
              {
                "id": "q-merge-identity",
                "text": "When two records are found to describe the same team, which survives and how is the loser tombstoned?",
                "kind": "exception",
                "answer_data": [
                  "Surviving identifier",
                  "Superseded identifier",
                  "Merge decision record reference"
                ]
              }
            ],
            "data_elements": [
              {
                "id": "team-id",
                "name": "team_id",
                "description": "Canonical identifier for the team instance in the adopting Dimension.",
                "value_kind": "identifier",
                "cardinality": "1",
                "required": true,
                "source_refs": [
                  "SRC-004"
                ]
              },
              {
                "id": "team-external-id",
                "name": "external_identifier",
                "description": "Identifier assigned by an external or upstream system, qualified by its issuing system URI.",
                "value_kind": "identifier",
                "cardinality": "0..n",
                "required": false,
                "source_refs": [
                  "SRC-002",
                  "SRC-004"
                ]
              },
              {
                "id": "team-display-name",
                "name": "display_name",
                "description": "Human-readable label; mutable and explicitly not an identifier.",
                "value_kind": "text",
                "cardinality": "0..1",
                "required": false,
                "source_refs": [
                  "SRC-002",
                  "SRC-004"
                ]
              }
            ],
            "artifacts": [
              {
                "id": "team-registry-entry",
                "name": "Team registry entry",
                "description": "The authoritative record that binds the canonical identifier to the team, its alternate identifiers and the minting decision.",
                "media_or_form": [
                  "structured record",
                  "registry entry"
                ],
                "serial": false,
                "identity_strategy": "Keyed by team_id; alternate identifiers held as system-qualified pairs.",
                "source_refs": [
                  "SRC-004",
                  "SRC-008"
                ]
              }
            ],
            "inline_only_rationale": null
          }
        },
        {
          "bundle": {
            "id": "identity-and-boundary",
            "name": "Identity and boundary",
            "description": "What makes a team instance the same thing over time, and what it is not."
          },
          "layer": {
            "id": "team-identity",
            "name": "Team identity",
            "description": "Identifier assignment, naming and the entity distinctions that keep a team from collapsing into an organization, a group or a position."
          },
          "finding": {
            "id": "team-boundary-and-entity-distinction",
            "name": "Boundary against organization, group and position",
            "description": "FHIR states that Organization is a formally recognized entity while Group is an undifferentiated collection lacking formal legal recognition, and that CareTeam participants are differentiated individuals. W3C org separates FormalOrganization, OrganizationalUnit and OrganizationalCollaboration. HR Open publishes no Team noun at all. Each instance must therefore declare which of these it actually is, or be rejected as a team.",
            "source_refs": [
              "SRC-001",
              "SRC-002",
              "SRC-003",
              "SRC-013"
            ],
            "questions": [
              {
                "id": "q-formal-status",
                "text": "Is this collective an internal unit of one formal organization, a cross-organization collaboration, or a rule-defined cohort?",
                "kind": "classification",
                "answer_data": [
                  "Boundary class (unit, collaboration, cohort)",
                  "Containing organization reference",
                  "Participating organizations for collaborations"
                ]
              },
              {
                "id": "q-enumerated",
                "text": "Is membership enumerated by identified participants or defined by characteristics?",
                "kind": "composition",
                "answer_data": [
                  "Membership basis (enumerated or definitional)",
                  "Characteristic expressions if definitional"
                ]
              },
              {
                "id": "q-legal-recognition",
                "text": "Does the team have any separate legal recognition, and if not, which legal entity bears its obligations?",
                "kind": "authority",
                "answer_data": [
                  "Legal recognition flag",
                  "Bearing legal entity identifier",
                  "Evidence reference"
                ]
              },
              {
                "id": "q-not-a-team",
                "text": "What disqualifies this record from being a team under this model?",
                "kind": "validation",
                "answer_data": [
                  "Disqualifying condition list",
                  "Rejection rationale"
                ]
              }
            ],
            "data_elements": [
              {
                "id": "boundary-class",
                "name": "boundary_class",
                "description": "Declared class: organizational unit, organizational collaboration, or non-team cohort.",
                "value_kind": "code",
                "cardinality": "1",
                "required": true,
                "source_refs": [
                  "SRC-001",
                  "SRC-003"
                ]
              },
              {
                "id": "membership-basis",
                "name": "membership_basis",
                "description": "Whether membership is enumerated or definitional.",
                "value_kind": "code",
                "cardinality": "1",
                "required": true,
                "source_refs": [
                  "SRC-003"
                ]
              },
              {
                "id": "containing-organization",
                "name": "containing_organization_ref",
                "description": "Reference to the organization context that contains or hosts the team.",
                "value_kind": "reference",
                "cardinality": "1",
                "required": true,
                "source_refs": [
                  "SRC-001",
                  "SRC-002"
                ]
              }
            ],
            "artifacts": [],
            "inline_only_rationale": "These are classification assertions on the team record itself; they produce no separate document and are resolved by reference to the containing organization model."
          }
        },
        {
          "bundle": {
            "id": "identity-and-boundary",
            "name": "Identity and boundary",
            "description": "What makes a team instance the same thing over time, and what it is not."
          },
          "layer": {
            "id": "team-identity",
            "name": "Team identity",
            "description": "Identifier assignment, naming and the entity distinctions that keep a team from collapsing into an organization, a group or a position."
          },
          "finding": {
            "id": "containing-and-managing-organization",
            "name": "Containing and managing organization",
            "description": "Most workplace teams are units of one FormalOrganization or Microsoft tenant. FHIR separately records managingOrganization as the organization responsible for the care team. GitHub teams exist only inside an organization.",
            "source_refs": [
              "SRC-001",
              "SRC-019",
              "SRC-020",
              "SRC-021",
              "SRC-025"
            ],
            "questions": [
              {
                "id": "containing-and-managing-organization-q01",
                "text": "Which Organization instance contains this team, and is the team a unit with meaning only inside that organization?",
                "kind": "relationship",
                "answer_data": [
                  "containing_organization_id",
                  "unit_of_flag"
                ]
              },
              {
                "id": "containing-and-managing-organization-q02",
                "text": "Which organization is responsible for managing the team, if that is different from the containing organization?",
                "kind": "ownership",
                "answer_data": [
                  "managing_organization_ids"
                ]
              },
              {
                "id": "containing-and-managing-organization-q03",
                "text": "Which tenant, directory or provisioning domain hosts the team record?",
                "kind": "identity",
                "answer_data": [
                  "tenant_id",
                  "directory_id",
                  "provisioning_domain"
                ]
              },
              {
                "id": "containing-and-managing-organization-q04",
                "text": "Must every member already belong to the containing organization, as GitHub requires, or may outsiders participate?",
                "kind": "constraint",
                "answer_data": [
                  "members_must_be_org_members",
                  "outsider_participation_rule"
                ]
              }
            ],
            "data_elements": [
              {
                "id": "containing-and-managing-organization-data01",
                "name": "Containing organization",
                "description": "Reference to the Organization of which this team is a unit or child.",
                "value_kind": "reference",
                "cardinality": "0..1",
                "required": false,
                "source_refs": [
                  "SRC-001",
                  "SRC-020"
                ]
              },
              {
                "id": "containing-and-managing-organization-data02",
                "name": "Managing organizations",
                "description": "Organizations responsible for the team, as in FHIR managingOrganization.",
                "value_kind": "collection",
                "cardinality": "0..n",
                "required": false,
                "source_refs": [
                  "SRC-019"
                ]
              },
              {
                "id": "containing-and-managing-organization-data03",
                "name": "Tenant identifier",
                "description": "Microsoft Entra tenant or equivalent directory that hosts the team.",
                "value_kind": "identifier",
                "cardinality": "0..1",
                "required": false,
                "source_refs": [
                  "SRC-021"
                ]
              }
            ],
            "artifacts": [
              {
                "id": "containing-and-managing-organization-artifact01",
                "name": "Organization chart extract",
                "description": "Chart or directory extract showing the team as a unit of a containing organization.",
                "media_or_form": [
                  "diagram",
                  "canonical record"
                ],
                "serial": true,
                "identity_strategy": "Containing organization master identifier plus chart version timestamp in RFC 3339",
                "source_refs": [
                  "SRC-001"
                ]
              }
            ],
            "inline_only_rationale": null
          }
        },
        {
          "bundle": {
            "id": "mandate-and-authority",
            "name": "Mandate and authority",
            "description": "Why the team exists, what it may decide, and who is accountable for it."
          },
          "layer": {
            "id": "charter-and-purpose",
            "name": "Charter and purpose",
            "description": "The constituting record: existence, purpose, expected functions, structure and training obligations."
          },
          "finding": {
            "id": "team-charter-and-mandate",
            "name": "Team charter and mandate",
            "description": "OSHA requires an employer to prepare and maintain a written statement establishing the existence of the brigade, its basic organizational structure, the type, amount and frequency of training, the expected number of members and the functions to be performed. W3C org supplies org:purpose, FHIR supplies CareTeam.reason, FEMA supplies overall function, and the Scrum Guide supplies the pattern of a single shared objective. The charter is the authoritative statement of scope and is versioned.",
            "source_refs": [
              "SRC-001",
              "SRC-002",
              "SRC-007",
              "SRC-016",
              "SRC-017"
            ],
            "questions": [
              {
                "id": "q-charter-exists",
                "text": "Is there a written constituting statement, who approved it, and when did it take effect?",
                "kind": "authority",
                "answer_data": [
                  "Charter document reference",
                  "Approver identity and role",
                  "Effective timestamp (RFC 3339)"
                ]
              },
              {
                "id": "q-purpose",
                "text": "What is the team's purpose and the specific functions it is expected to perform?",
                "kind": "definition",
                "answer_data": [
                  "Purpose statement",
                  "Enumerated expected functions",
                  "Explicit non-functions"
                ]
              },
              {
                "id": "q-mandated-by-law",
                "text": "Is any element of the charter mandated by law, regulation or contract rather than chosen?",
                "kind": "requirement",
                "answer_data": [
                  "Obligation source citation",
                  "Mandated element",
                  "Jurisdiction"
                ]
              },
              {
                "id": "q-objective-window",
                "text": "What objective is the team accountable for, over what period, and how is attainment judged?",
                "kind": "measurement",
                "answer_data": [
                  "Objective statement",
                  "Objective period start and end",
                  "Attainment criteria"
                ]
              },
              {
                "id": "q-charter-review",
                "text": "When must the charter be reviewed or revalidated, and what triggers an out-of-cycle review?",
                "kind": "lifecycle",
                "answer_data": [
                  "Review interval",
                  "Trigger conditions",
                  "Last review timestamp"
                ]
              }
            ],
            "data_elements": [
              {
                "id": "purpose-statement",
                "name": "purpose",
                "description": "Declared purpose of the team.",
                "value_kind": "text",
                "cardinality": "1",
                "required": true,
                "source_refs": [
                  "SRC-001",
                  "SRC-017"
                ]
              },
              {
                "id": "expected-functions",
                "name": "expected_functions",
                "description": "Enumerated functions the team is constituted to perform.",
                "value_kind": "collection",
                "cardinality": "1..n",
                "required": true,
                "source_refs": [
                  "SRC-007",
                  "SRC-017"
                ]
              },
              {
                "id": "charter-effective-period",
                "name": "charter_effective_period",
                "description": "Start and optional end of charter validity, expressed as RFC 3339 instants.",
                "value_kind": "object",
                "cardinality": "1",
                "required": true,
                "source_refs": [
                  "SRC-005",
                  "SRC-002"
                ]
              },
              {
                "id": "mandate-obligation-ref",
                "name": "mandate_obligation_ref",
                "description": "Citation of any legal or contractual instrument that compels the team's existence or composition.",
                "value_kind": "reference",
                "cardinality": "0..n",
                "required": false,
                "source_refs": [
                  "SRC-017"
                ]
              }
            ],
            "artifacts": [
              {
                "id": "team-charter",
                "name": "Team charter / organizational statement",
                "description": "The written, approved and maintained statement establishing the team, its structure, expected membership, training obligations and functions.",
                "media_or_form": [
                  "approved written statement",
                  "policy document"
                ],
                "serial": true,
                "identity_strategy": "Charter identifier plus monotonically increasing version, each version carrying its own approval and effective timestamps.",
                "source_refs": [
                  "SRC-017",
                  "SRC-007"
                ]
              }
            ],
            "inline_only_rationale": null
          }
        },
        {
          "bundle": {
            "id": "mandate-and-authority",
            "name": "Mandate and authority",
            "description": "Why the team exists, what it may decide, and who is accountable for it."
          },
          "layer": {
            "id": "authority-and-accountability",
            "name": "Authority and accountability",
            "description": "Decision rights, the accountable owner and the placement of the team in reporting structures."
          },
          "finding": {
            "id": "decision-rights-ownership-and-reporting-line",
            "name": "Decision rights, ownership and reporting line",
            "description": "W3C org gives headOf, reportsTo, unitOf and hasPost; FHIR gives CareTeam.managingOrganization 0..* and Group.managingEntity; FEMA requires delegated authorities to be agreed before deployment; the Scrum Guide assigns distinct accountabilities within a single team. NIST separation of duties and least privilege constrain which decision rights may be concentrated in one holder.",
            "source_refs": [
              "SRC-001",
              "SRC-002",
              "SRC-003",
              "SRC-007",
              "SRC-014",
              "SRC-016"
            ],
            "questions": [
              {
                "id": "q-accountable-owner",
                "text": "Which single party is accountable for the team's outcomes, and through which post is that held?",
                "kind": "ownership",
                "answer_data": [
                  "Accountable party reference",
                  "Post reference in WM-ORG-004",
                  "Accountability period"
                ]
              },
              {
                "id": "q-managing-orgs",
                "text": "Which organizations manage or co-manage the team, and how are conflicts between them resolved?",
                "kind": "authority",
                "answer_data": [
                  "Managing organization references",
                  "Co-management arrangement",
                  "Escalation path"
                ]
              },
              {
                "id": "q-decision-rights",
                "text": "Which decisions may the team make autonomously, which need approval, and up to what threshold?",
                "kind": "authority",
                "answer_data": [
                  "Decision class",
                  "Autonomy level",
                  "Approval threshold and approver"
                ]
              },
              {
                "id": "q-sod",
                "text": "Which combinations of decision rights must not be held by the same person?",
                "kind": "security",
                "answer_data": [
                  "Incompatible right pairs",
                  "Enforcement mechanism",
                  "Documented exception and compensating control"
                ]
              },
              {
                "id": "q-reporting-line",
                "text": "Where does the team sit in the reporting structure, and is that line solid or matrixed?",
                "kind": "relationship",
                "answer_data": [
                  "Parent unit reference",
                  "Line type (solid, dotted, matrixed)",
                  "Secondary reporting references"
                ]
              }
            ],
            "data_elements": [
              {
                "id": "accountable-owner-ref",
                "name": "accountable_owner_ref",
                "description": "Reference to the party accountable for the team.",
                "value_kind": "reference",
                "cardinality": "1",
                "required": true,
                "source_refs": [
                  "SRC-001",
                  "SRC-002"
                ]
              },
              {
                "id": "managing-org-ref",
                "name": "managing_organization_ref",
                "description": "Organizations that manage the team, allowing more than one for co-managed teams.",
                "value_kind": "reference",
                "cardinality": "0..n",
                "required": false,
                "source_refs": [
                  "SRC-002",
                  "SRC-003"
                ]
              },
              {
                "id": "reports-to-ref",
                "name": "reports_to_ref",
                "description": "Parent unit or post the team reports to.",
                "value_kind": "reference",
                "cardinality": "0..n",
                "required": false,
                "source_refs": [
                  "SRC-001"
                ]
              },
              {
                "id": "decision-right",
                "name": "decision_right",
                "description": "A named decision class with autonomy level, threshold and approver.",
                "value_kind": "object",
                "cardinality": "0..n",
                "required": false,
                "source_refs": [
                  "SRC-007",
                  "SRC-014"
                ]
              }
            ],
            "artifacts": [
              {
                "id": "delegation-of-authority-record",
                "name": "Delegation of authority record",
                "description": "Signed record of decision rights delegated to the team or its lead, including thresholds, duration and separation-of-duties exceptions.",
                "media_or_form": [
                  "signed delegation instrument",
                  "structured record"
                ],
                "serial": true,
                "identity_strategy": "Delegation identifier plus version; superseded versions retained with their effective periods.",
                "source_refs": [
                  "SRC-007",
                  "SRC-014"
                ]
              }
            ],
            "inline_only_rationale": null
          }
        },
        {
          "bundle": {
            "id": "composition-and-capability",
            "name": "Composition and capability",
            "description": "Who is on the team, in what role, at what capacity, and whether the collective can actually do the work."
          },
          "layer": {
            "id": "membership-records",
            "name": "Membership records",
            "description": "The time-bounded assignment facts that constitute the team."
          },
          "finding": {
            "id": "membership-assignment-record",
            "name": "Membership assignment record",
            "description": "W3C org expresses membership as an n-ary org:Membership with memberDuring so that duration, remuneration and contract references can be attached; FHIR CareTeam.participant carries role, member, onBehalfOf and coverage; FHIR Group.member carries period and an inactive flag; schema.org OrganizationRole carries roleName with startDate and endDate; SCIM requires membership changes to be applied via the Group resource. Membership is a first-class dated record, never a mutable array of names.",
            "source_refs": [
              "SRC-001",
              "SRC-002",
              "SRC-003",
              "SRC-004",
              "SRC-011"
            ],
            "questions": [
              {
                "id": "q-member-period",
                "text": "For each member, when did participation start and when did or will it end?",
                "kind": "temporal",
                "answer_data": [
                  "Member reference",
                  "Start instant (RFC 3339)",
                  "End instant or open-ended flag"
                ]
              },
              {
                "id": "q-write-authority",
                "text": "Which system is authoritative for writing membership, and how are conflicting writes from HR and IdP reconciled?",
                "kind": "authority",
                "answer_data": [
                  "Authoritative writer",
                  "Reconciliation rule",
                  "Conflict log reference"
                ]
              },
              {
                "id": "q-inactive-vs-removed",
                "text": "Is a departed member marked inactive with a closed period or removed from the record entirely?",
                "kind": "state",
                "answer_data": [
                  "Retention treatment code",
                  "Inactive flag semantics",
                  "Basis for erasure if removed"
                ]
              },
              {
                "id": "q-retroactive",
                "text": "How are backdated or corrected memberships recorded without losing the prior assertion?",
                "kind": "provenance",
                "answer_data": [
                  "Correction record reference",
                  "Original asserted values",
                  "Correction timestamp and author"
                ]
              }
            ],
            "data_elements": [
              {
                "id": "membership-id",
                "name": "membership_id",
                "description": "Identifier of the individual assignment fact.",
                "value_kind": "identifier",
                "cardinality": "1",
                "required": true,
                "source_refs": [
                  "SRC-001"
                ]
              },
              {
                "id": "member-ref",
                "name": "member_ref",
                "description": "Reference to the person, organization or agent participating.",
                "value_kind": "reference",
                "cardinality": "1",
                "required": true,
                "source_refs": [
                  "SRC-002",
                  "SRC-004"
                ]
              },
              {
                "id": "member-during",
                "name": "member_during",
                "description": "Closed or open interval of participation with RFC 3339 endpoints.",
                "value_kind": "object",
                "cardinality": "1",
                "required": true,
                "source_refs": [
                  "SRC-001",
                  "SRC-005"
                ]
              },
              {
                "id": "member-inactive",
                "name": "inactive",
                "description": "Flag marking a retained but no longer effective membership.",
                "value_kind": "boolean",
                "cardinality": "0..1",
                "required": false,
                "source_refs": [
                  "SRC-003"
                ]
              }
            ],
            "artifacts": [
              {
                "id": "membership-assignment-artifact",
                "name": "Membership assignment record",
                "description": "The durable dated record binding an agent to the team in a role for a period, with its own provenance.",
                "media_or_form": [
                  "structured record",
                  "assignment instrument"
                ],
                "serial": true,
                "identity_strategy": "membership_id; supersession chain preserved so no assignment fact is overwritten in place.",
                "source_refs": [
                  "SRC-001",
                  "SRC-002"
                ]
              }
            ],
            "inline_only_rationale": null
          }
        },
        {
          "bundle": {
            "id": "composition-and-capability",
            "name": "Composition and capability",
            "description": "Who is on the team, in what role, at what capacity, and whether the collective can actually do the work."
          },
          "layer": {
            "id": "membership-records",
            "name": "Membership records",
            "description": "The time-bounded assignment facts that constitute the team."
          },
          "finding": {
            "id": "role-and-position-binding",
            "name": "In-team role and position binding",
            "description": "org:Post is a reusable position held by an agent via holds/heldBy; HR Open OrganizationChart models units, positions and incumbents; CareTeam.participant.role types the participation itself. The in-team role is the binding, and is distinct from the position definition owned by WM-ORG-004 and from the occupation code owned by ESCO/ISCO-08.",
            "source_refs": [
              "SRC-001",
              "SRC-002",
              "SRC-010",
              "SRC-012"
            ],
            "questions": [
              {
                "id": "q-role-vs-post",
                "text": "Does this member occupy a defined position, or hold only a team-scoped role with no position behind it?",
                "kind": "composition",
                "answer_data": [
                  "Position reference or null",
                  "Team-scoped role code",
                  "Scheme URI for the role code"
                ]
              },
              {
                "id": "q-occupation-code",
                "text": "Which governed occupation code describes the work performed, and under which classification version?",
                "kind": "classification",
                "answer_data": [
                  "Occupation URI",
                  "Classification and version",
                  "Mapping confidence"
                ]
              },
              {
                "id": "q-multiple-roles",
                "text": "May one member hold several roles in the same team at once, and how is that recorded?",
                "kind": "constraint",
                "answer_data": [
                  "Multiplicity rule",
                  "Concurrent role records",
                  "Conflict rule"
                ]
              },
              {
                "id": "q-lead-role",
                "text": "Which role carries leadership of the team, and is it the same as the accountable owner?",
                "kind": "authority",
                "answer_data": [
                  "Lead role reference",
                  "Divergence from accountable owner",
                  "Rationale"
                ]
              }
            ],
            "data_elements": [
              {
                "id": "in-team-role",
                "name": "in_team_role",
                "description": "Scheme-qualified role played by the member within this team.",
                "value_kind": "code",
                "cardinality": "1..n",
                "required": true,
                "source_refs": [
                  "SRC-001",
                  "SRC-002"
                ]
              },
              {
                "id": "position-ref",
                "name": "position_ref",
                "description": "Reference to a reusable position governed by WM-ORG-004.",
                "value_kind": "reference",
                "cardinality": "0..1",
                "required": false,
                "source_refs": [
                  "SRC-001",
                  "SRC-012"
                ]
              },
              {
                "id": "occupation-uri",
                "name": "occupation_uri",
                "description": "Governed occupation identifier such as an ESCO or ISCO-08 URI.",
                "value_kind": "identifier",
                "cardinality": "0..1",
                "required": false,
                "source_refs": [
                  "SRC-010"
                ]
              }
            ],
            "artifacts": [],
            "inline_only_rationale": "The binding is inline on the membership record; the reusable position definition and the occupation taxonomy are artifacts owned by WM-ORG-004 and by the external classifier respectively."
          }
        },
        {
          "bundle": {
            "id": "composition-and-capability",
            "name": "Composition and capability",
            "description": "Who is on the team, in what role, at what capacity, and whether the collective can actually do the work."
          },
          "layer": {
            "id": "membership-records",
            "name": "Membership records",
            "description": "The time-bounded assignment facts that constitute the team."
          },
          "finding": {
            "id": "nesting-and-inherited-membership",
            "name": "Parent-child and team-of-teams",
            "description": "GitHub allows one parent team and many children; child teams inherit parent permissions; listed members of a parent include child members but those members are not direct parent members. Secret teams cannot nest. Scrum forbids sub-teams and instead splits oversized teams into multiple teams sharing a Product Goal. SCIM Groups may nest Groups. FHIR CareTeam may have another CareTeam as a participant.",
            "source_refs": [
              "SRC-019",
              "SRC-020",
              "SRC-022",
              "SRC-016",
              "SRC-025"
            ],
            "questions": [
              {
                "id": "nesting-and-inherited-membership-q01",
                "text": "What is the parent team, if any, and does this team have exactly one parent as in GitHub or an open unit hierarchy as in ORG?",
                "kind": "relationship",
                "answer_data": [
                  "parent_team_id",
                  "hierarchy_cardinality_rule"
                ]
              },
              {
                "id": "nesting-and-inherited-membership-q02",
                "text": "Which child teams exist, and do their members count as inherited members of this team for listing, mentions or permissions?",
                "kind": "composition",
                "answer_data": [
                  "child_team_ids",
                  "inherited_member_semantics"
                ]
              },
              {
                "id": "nesting-and-inherited-membership-q03",
                "text": "Is nesting forbidden because this is a Scrum Team, a secret team, or another profile that rejects sub-teams?",
                "kind": "constraint",
                "answer_data": [
                  "nesting_forbidden",
                  "forbidding_profile"
                ]
              },
              {
                "id": "nesting-and-inherited-membership-q04",
                "text": "When size or complexity requires change, should the team split into sibling teams sharing a goal rather than adding a child team?",
                "kind": "decision",
                "answer_data": [
                  "split_recommendation",
                  "shared_goal_after_split"
                ]
              }
            ],
            "data_elements": [
              {
                "id": "nesting-and-inherited-membership-data01",
                "name": "Parent team",
                "description": "Reference to a single parent team where the platform uses a tree, such as GitHub parent.",
                "value_kind": "reference",
                "cardinality": "0..1",
                "required": false,
                "source_refs": [
                  "SRC-020",
                  "SRC-025"
                ]
              },
              {
                "id": "nesting-and-inherited-membership-data02",
                "name": "Child teams",
                "description": "Teams nested under this team.",
                "value_kind": "collection",
                "cardinality": "0..n",
                "required": false,
                "source_refs": [
                  "SRC-025"
                ]
              },
              {
                "id": "nesting-and-inherited-membership-data03",
                "name": "Nesting forbidden",
                "description": "True when the chosen profile or privacy class, such as Scrum or GitHub secret, forbids parent or child teams.",
                "value_kind": "boolean",
                "cardinality": "0..1",
                "required": false,
                "source_refs": [
                  "SRC-016",
                  "SRC-025"
                ]
              }
            ],
            "artifacts": [
              {
                "id": "nesting-and-inherited-membership-artifact01",
                "name": "Team hierarchy snapshot",
                "description": "Point-in-time tree of parent and child teams used to audit inherited permissions.",
                "media_or_form": [
                  "diagram",
                  "canonical record"
                ],
                "serial": true,
                "identity_strategy": "Containing organization identifier plus snapshot observation time in RFC 3339",
                "source_refs": [
                  "SRC-025"
                ]
              }
            ],
            "inline_only_rationale": null
          }
        },
        {
          "bundle": {
            "id": "lifecycle-and-change",
            "name": "Lifecycle and structural change",
            "description": "How a team comes into being, changes state, mutates structurally and ends."
          },
          "layer": {
            "id": "state-and-effective-time",
            "name": "State and effective time",
            "description": "The state machine of a team record and the time semantics that make its assertions checkable."
          },
          "finding": {
            "id": "team-status-lifecycle",
            "name": "Team status lifecycle",
            "description": "FHIR CareTeam.status is proposed, active, suspended, inactive or entered-in-error, and Group carries a modifier active flag. The entered-in-error value matters: it separates a team that ended from a team that never should have been recorded, which is an erasure-relevant distinction that a simple active boolean cannot express.",
            "source_refs": [
              "SRC-002",
              "SRC-003"
            ],
            "questions": [
              {
                "id": "q-status-now",
                "text": "What is the team's current status and since when?",
                "kind": "state",
                "answer_data": [
                  "Status code",
                  "Status effective instant",
                  "Prior status"
                ]
              },
              {
                "id": "q-transitions",
                "text": "Which status transitions are permitted, and who may authorise each?",
                "kind": "lifecycle",
                "answer_data": [
                  "Allowed transition pairs",
                  "Authorising role",
                  "Required evidence"
                ]
              },
              {
                "id": "q-error-vs-ended",
                "text": "How is an erroneously created team distinguished from one that ended normally?",
                "kind": "exception",
                "answer_data": [
                  "Error marking rule",
                  "Downstream retraction obligations",
                  "Notification list"
                ]
              },
              {
                "id": "q-suspension",
                "text": "What does suspension mean operationally for memberships, access and obligations?",
                "kind": "process",
                "answer_data": [
                  "Effect on memberships",
                  "Effect on entitlements",
                  "Maximum suspension duration"
                ]
              }
            ],
            "data_elements": [
              {
                "id": "team-status",
                "name": "status",
                "description": "Lifecycle status of the team record.",
                "value_kind": "code",
                "cardinality": "1",
                "required": true,
                "source_refs": [
                  "SRC-002"
                ]
              },
              {
                "id": "status-changed-at",
                "name": "status_changed_at",
                "description": "Instant the current status took effect.",
                "value_kind": "timestamp",
                "cardinality": "1",
                "required": true,
                "source_refs": [
                  "SRC-002",
                  "SRC-005"
                ]
              }
            ],
            "artifacts": [],
            "inline_only_rationale": "Status is inline state on the team record; the durable evidence of each transition is captured by the change-event artifact registered in the structural-change layer."
          }
        },
        {
          "bundle": {
            "id": "lifecycle-and-change",
            "name": "Lifecycle and structural change",
            "description": "How a team comes into being, changes state, mutates structurally and ends."
          },
          "layer": {
            "id": "state-and-effective-time",
            "name": "State and effective time",
            "description": "The state machine of a team record and the time semantics that make its assertions checkable."
          },
          "finding": {
            "id": "effective-dating-and-time-semantics",
            "name": "Effective dating and time semantics",
            "description": "RFC 3339 requires a full date, a full time with seconds and an explicit offset or Z, and reserves -00:00 for an unknown local offset. SCIM meta separates created from lastModified; PROV separates startedAtTime and endedAtTime on activities from generation of records. Event time (when the team changed) must be recorded separately from observation time (when the system learned of it).",
            "source_refs": [
              "SRC-004",
              "SRC-005",
              "SRC-006"
            ],
            "questions": [
              {
                "id": "q-event-vs-observation",
                "text": "For each assertion, when did the fact become true and when was it recorded?",
                "kind": "temporal",
                "answer_data": [
                  "Event instant (RFC 3339)",
                  "Observation or ingestion instant",
                  "Recording system"
                ]
              },
              {
                "id": "q-offset",
                "text": "Is the local UTC offset known for each timestamp, or must -00:00 be used?",
                "kind": "temporal",
                "answer_data": [
                  "Offset value",
                  "Known or unknown flag",
                  "Governing time zone identifier"
                ]
              },
              {
                "id": "q-open-intervals",
                "text": "How are open-ended and future-dated periods represented and queried as-of an instant?",
                "kind": "temporal",
                "answer_data": [
                  "Open-interval convention",
                  "As-of query semantics",
                  "Future-dating policy"
                ]
              },
              {
                "id": "q-precision",
                "text": "What timestamp precision is required, and where is a date alone acceptable?",
                "kind": "constraint",
                "answer_data": [
                  "Required precision",
                  "Fields permitting date-only values",
                  "Rationale"
                ]
              }
            ],
            "data_elements": [
              {
                "id": "event-time",
                "name": "event_time",
                "description": "RFC 3339 instant at which the asserted fact became true.",
                "value_kind": "timestamp",
                "cardinality": "1",
                "required": true,
                "source_refs": [
                  "SRC-005"
                ]
              },
              {
                "id": "observed-at",
                "name": "observed_at",
                "description": "RFC 3339 instant at which the fact was observed or ingested.",
                "value_kind": "timestamp",
                "cardinality": "1",
                "required": true,
                "source_refs": [
                  "SRC-004",
                  "SRC-006"
                ]
              },
              {
                "id": "validity-interval",
                "name": "validity_interval",
                "description": "Interval over which an assertion holds, with explicit open-end handling.",
                "value_kind": "duration",
                "cardinality": "0..1",
                "required": false,
                "source_refs": [
                  "SRC-001",
                  "SRC-005"
                ]
              }
            ],
            "artifacts": [],
            "inline_only_rationale": "Time semantics are cross-cutting constraints on every record in the aggregate; they generate no artifact of their own but govern the timestamps carried by all other artifacts."
          }
        },
        {
          "bundle": {
            "id": "lifecycle-and-change",
            "name": "Lifecycle and structural change",
            "description": "How a team comes into being, changes state, mutates structurally and ends."
          },
          "layer": {
            "id": "structural-change-events",
            "name": "Structural change events",
            "description": "Formation, dissolution, merge, split and transfer expressed as first-class events."
          },
          "finding": {
            "id": "formation-and-dissolution",
            "name": "Formation and dissolution",
            "description": "schema.org supplies foundingDate and dissolutionDate; org:ChangeEvent records organizational change with resultedFrom links; FEMA's ordering specifications frame mobilization and demobilization preconditions. Formation and dissolution are events with their own authority, evidence and downstream obligations, not merely the endpoints of an interval.",
            "source_refs": [
              "SRC-001",
              "SRC-007",
              "SRC-011"
            ],
            "questions": [
              {
                "id": "q-formation-authority",
                "text": "Who authorised the team's formation and on what instrument?",
                "kind": "authority",
                "answer_data": [
                  "Authorising party",
                  "Instrument reference",
                  "Authorisation instant"
                ]
              },
              {
                "id": "q-dissolution-trigger",
                "text": "What condition triggers dissolution, and is it time-based, objective-based or discretionary?",
                "kind": "lifecycle",
                "answer_data": [
                  "Trigger type",
                  "Trigger condition",
                  "Evaluation owner"
                ]
              },
              {
                "id": "q-wind-down",
                "text": "On dissolution, where do open obligations, artifacts and members go?",
                "kind": "process",
                "answer_data": [
                  "Receiving team or unit",
                  "Artifact custody transfer",
                  "Member reassignment records"
                ]
              },
              {
                "id": "q-access-revocation",
                "text": "What entitlements must be revoked on dissolution, and within what window?",
                "kind": "security",
                "answer_data": [
                  "Entitlement inventory",
                  "Revocation deadline",
                  "Revocation evidence"
                ]
              }
            ],
            "data_elements": [
              {
                "id": "formed-at",
                "name": "formed_at",
                "description": "Instant the team came into existence.",
                "value_kind": "timestamp",
                "cardinality": "1",
                "required": true,
                "source_refs": [
                  "SRC-005",
                  "SRC-011"
                ]
              },
              {
                "id": "dissolved-at",
                "name": "dissolved_at",
                "description": "Instant the team ceased to exist.",
                "value_kind": "timestamp",
                "cardinality": "0..1",
                "required": false,
                "source_refs": [
                  "SRC-011"
                ]
              },
              {
                "id": "successor-ref",
                "name": "successor_ref",
                "description": "Team or unit that inherits the dissolved team's obligations.",
                "value_kind": "reference",
                "cardinality": "0..n",
                "required": false,
                "source_refs": [
                  "SRC-001"
                ]
              }
            ],
            "artifacts": [
              {
                "id": "lifecycle-event-record",
                "name": "Team lifecycle event record",
                "description": "Dated record of a formation or dissolution event with authorising instrument, effective instant and downstream obligations.",
                "media_or_form": [
                  "event record",
                  "decision minute"
                ],
                "serial": true,
                "identity_strategy": "Event identifier plus event instant; events are append-only and never edited.",
                "source_refs": [
                  "SRC-001",
                  "SRC-011"
                ]
              }
            ],
            "inline_only_rationale": null
          }
        },
        {
          "bundle": {
            "id": "lifecycle-and-change",
            "name": "Lifecycle and structural change",
            "description": "How a team comes into being, changes state, mutates structurally and ends."
          },
          "layer": {
            "id": "structural-change-events",
            "name": "Structural change events",
            "description": "Formation, dissolution, merge, split and transfer expressed as first-class events."
          },
          "finding": {
            "id": "merge-split-and-transfer-events",
            "name": "Merge, split and transfer events",
            "description": "org:ChangeEvent explicitly links originalOrganization to resultingOrganization so that reorganizations are traceable; PROV wasDerivedFrom carries the same lineage semantics for records; ISO 30414 adds guidance on when multi-unit entities consolidate or report separately, which determines whether merged teams keep separate metric histories.",
            "source_refs": [
              "SRC-001",
              "SRC-006",
              "SRC-009"
            ],
            "questions": [
              {
                "id": "q-change-lineage",
                "text": "Which predecessor teams produced this team, and which successors did it produce?",
                "kind": "provenance",
                "answer_data": [
                  "Original team references",
                  "Resulting team references",
                  "Change event reference"
                ]
              },
              {
                "id": "q-continuity",
                "text": "Does the team retain its identifier through the change, or is a new identity minted?",
                "kind": "identity",
                "answer_data": [
                  "Identity continuity decision",
                  "Rationale",
                  "Superseded identifiers"
                ]
              },
              {
                "id": "q-history-consolidation",
                "text": "Are historical metrics and memberships consolidated, split or left with the predecessor?",
                "kind": "decision",
                "answer_data": [
                  "Consolidation rule applied",
                  "Affected metric series",
                  "Restatement note"
                ]
              },
              {
                "id": "q-transfer",
                "text": "When a team moves to a different parent unit, what changes and what must not?",
                "kind": "relationship",
                "answer_data": [
                  "New parent reference",
                  "Preserved attributes",
                  "Attributes requiring revalidation"
                ]
              }
            ],
            "data_elements": [
              {
                "id": "change-event-type",
                "name": "change_event_type",
                "description": "Formation, merge, split, transfer, rename or dissolution.",
                "value_kind": "code",
                "cardinality": "1",
                "required": true,
                "source_refs": [
                  "SRC-001"
                ]
              },
              {
                "id": "original-team-ref",
                "name": "original_team_ref",
                "description": "Predecessor team references for the change event.",
                "value_kind": "reference",
                "cardinality": "0..n",
                "required": false,
                "source_refs": [
                  "SRC-001",
                  "SRC-006"
                ]
              },
              {
                "id": "resulting-team-ref",
                "name": "resulting_team_ref",
                "description": "Successor team references for the change event.",
                "value_kind": "reference",
                "cardinality": "0..n",
                "required": false,
                "source_refs": [
                  "SRC-001"
                ]
              }
            ],
            "artifacts": [
              {
                "id": "reorganization-record",
                "name": "Reorganization change record",
                "description": "Append-only record linking predecessor and successor teams, the authorising decision and the metric-continuity ruling.",
                "media_or_form": [
                  "event record",
                  "structured lineage record"
                ],
                "serial": true,
                "identity_strategy": "Change event identifier plus effective instant; lineage edges are immutable once published.",
                "source_refs": [
                  "SRC-001",
                  "SRC-006",
                  "SRC-009"
                ]
              }
            ],
            "inline_only_rationale": null
          }
        }
      ],
      "functions": [
        {
          "id": "resolve-team-identity",
          "name": "Resolve team identity",
          "description": "Determine the canonical identifier for a team, applying the identity priority order and minting only when no authoritative or governed identifier exists.",
          "inputs": [
            "Candidate identifiers with issuing system URIs",
            "Containing organization reference",
            "Boundary class declaration"
          ],
          "outputs": [
            "Canonical team_id",
            "Identity resolution record with priority tier applied"
          ],
          "preconditions": [
            "Containing organization is resolvable",
            "Boundary class is declared and is not a non-team cohort"
          ],
          "effects": [
            "Canonical identifier bound and published",
            "Alternate identifiers recorded as system-qualified correlations"
          ],
          "source_refs": [
            "SRC-002",
            "SRC-004",
            "SRC-015"
          ]
        },
        {
          "id": "assert-membership",
          "name": "Assert membership",
          "description": "Create a time-bounded membership assignment binding an agent to the team in one or more roles, optionally on behalf of another organization.",
          "inputs": [
            "Member reference",
            "In-team role codes",
            "Start instant (RFC 3339)",
            "Optional position reference and onBehalfOf organization"
          ],
          "outputs": [
            "Membership assignment record",
            "Updated active-member set as of the start instant"
          ],
          "preconditions": [
            "Team status permits membership changes",
            "Writing system holds membership write authority",
            "Start instant carries an explicit offset or Z"
          ],
          "effects": [
            "Membership fact appended with event and observation times",
            "Composition and qualification validation triggered"
          ],
          "source_refs": [
            "SRC-001",
            "SRC-002",
            "SRC-004",
            "SRC-005"
          ]
        },
        {
          "id": "end-membership",
          "name": "End membership",
          "description": "Close a membership by setting its end instant and inactive flag, preserving the historical assertion rather than deleting it.",
          "inputs": [
            "Membership identifier",
            "End instant",
            "Reason code"
          ],
          "outputs": [
            "Closed membership record",
            "Entitlement revocation task list"
          ],
          "preconditions": [
            "Membership exists and is currently open",
            "End instant is not earlier than the start instant"
          ],
          "effects": [
            "Membership marked inactive with a closed interval",
            "Access revocation obligations raised with a deadline"
          ],
          "source_refs": [
            "SRC-001",
            "SRC-003",
            "SRC-014"
          ]
        },
        {
          "id": "validate-composition",
          "name": "Validate composition and qualification",
          "description": "Evaluate current membership against the declared constraint profile, capability tier and credential currency requirements as of a given instant.",
          "inputs": [
            "Team identifier",
            "Evaluation instant",
            "Constraint profile reference"
          ],
          "outputs": [
            "Compliance verdict",
            "Enumerated shortfalls by role, competence and credential"
          ],
          "preconditions": [
            "A constraint profile is declared",
            "Membership records carry validity intervals"
          ],
          "effects": [
            "Compliance state recorded with the evaluation instant",
            "Non-compliance escalated to the accountable owner"
          ],
          "source_refs": [
            "SRC-007",
            "SRC-016",
            "SRC-017"
          ]
        },
        {
          "id": "transition-team-state",
          "name": "Transition team state",
          "description": "Move the team between proposed, active, suspended, inactive and entered-in-error, enforcing permitted transitions and authorisation.",
          "inputs": [
            "Target status",
            "Effective instant",
            "Authorising party"
          ],
          "outputs": [
            "Updated status with effective instant",
            "Transition event record"
          ],
          "preconditions": [
            "Transition is permitted from the current status",
            "Authorising party holds the delegated right"
          ],
          "effects": [
            "Status changed and downstream obligations raised",
            "Erroneous records marked entered-in-error rather than deleted"
          ],
          "source_refs": [
            "SRC-002",
            "SRC-003"
          ]
        },
        {
          "id": "record-structural-change",
          "name": "Record structural change",
          "description": "Register a formation, merge, split, transfer, rename or dissolution as an append-only change event linking predecessor and successor teams.",
          "inputs": [
            "Change event type",
            "Original and resulting team references",
            "Effective instant",
            "Authorising instrument"
          ],
          "outputs": [
            "Change event record with lineage edges",
            "Identity continuity ruling"
          ],
          "preconditions": [
            "All referenced teams resolve",
            "Effective instant is supplied with an explicit offset"
          ],
          "effects": [
            "Lineage published and immutable",
            "Metric continuity and consolidation decision recorded"
          ],
          "source_refs": [
            "SRC-001",
            "SRC-006",
            "SRC-009"
          ]
        },
        {
          "id": "compute-team-metrics",
          "name": "Compute team metrics",
          "description": "Compute or ingest team-level metric values bound to a versioned definition and an observation window, applying suppression where the population is too small.",
          "inputs": [
            "Metric definition reference and version",
            "Observation window",
            "Population basis"
          ],
          "outputs": [
            "Metric values with computation instant",
            "Suppression and materiality decisions"
          ],
          "preconditions": [
            "Metric definition is versioned and resolvable",
            "Underlying membership and allocation data cover the window"
          ],
          "effects": [
            "Metric report issued and immutable",
            "Re-identification risk assessed before publication"
          ],
          "source_refs": [
            "SRC-009",
            "SRC-018"
          ]
        },
        {
          "id": "evaluate-access-request",
          "name": "Evaluate access request",
          "description": "Decide what portion of the team record a requester may see, applying least privilege, purpose limitation and the record's sensitivity class.",
          "inputs": [
            "Requester identity and role",
            "Requested scope",
            "Declared purpose"
          ],
          "outputs": [
            "Access decision with permitted scope",
            "Audit entry"
          ],
          "preconditions": [
            "Sensitivity class is set",
            "Declared purpose is compatible with the collection purpose"
          ],
          "effects": [
            "Decision enforced and logged",
            "Denials recorded with reason for later review"
          ],
          "source_refs": [
            "SRC-014",
            "SRC-018"
          ]
        },
        {
          "id": "apply-retention-policy",
          "name": "Apply retention and disposal",
          "description": "Apply the retention schedule to each class of team record, honouring legal holds and preferring anonymisation over deletion where history must be preserved.",
          "inputs": [
            "Record class",
            "Retention schedule",
            "Legal hold status"
          ],
          "outputs": [
            "Disposal or anonymisation actions",
            "Disposition certificate"
          ],
          "preconditions": [
            "Retention trigger event has occurred",
            "No active legal hold applies"
          ],
          "effects": [
            "Personal elements disposed or anonymised",
            "Disposition evidence retained beyond the disposed data"
          ],
          "source_refs": [
            "SRC-018"
          ]
        },
        {
          "id": "export-alignment-projection",
          "name": "Export alignment projection",
          "description": "Emit the team as a named external profile such as W3C org, SCIM Group, FHIR CareTeam or schema.org Organization, disclosing every unmapped element.",
          "inputs": [
            "Target profile and version",
            "Scope filter",
            "As-of instant"
          ],
          "outputs": [
            "Projected representation",
            "Loss report listing unmapped elements"
          ],
          "preconditions": [
            "A versioned mapping specification exists for the target profile",
            "Access decision permits the requested scope"
          ],
          "effects": [
            "Projection issued with an explicit as-of instant",
            "Conformance claim limited to the validated profile"
          ],
          "source_refs": [
            "SRC-001",
            "SRC-002",
            "SRC-004",
            "SRC-011"
          ]
        },
        {
          "id": "verify-tier-claim",
          "name": "Verify capability tier claim",
          "description": "Test a claimed capability tier against the referenced typing definition, recording verifier identity, method and result.",
          "inputs": [
            "Claimed tier",
            "Typing definition reference and version",
            "Current roster and equipment inventory"
          ],
          "outputs": [
            "Verification result",
            "Shortfall list with compensating measures"
          ],
          "preconditions": [
            "Typing definition is published and resolvable",
            "Roster snapshot exists for the verification instant"
          ],
          "effects": [
            "Tier claim marked verified or withdrawn",
            "Verification timestamp recorded for currency tracking"
          ],
          "source_refs": [
            "SRC-007",
            "SRC-008"
          ]
        },
        {
          "id": "attach-post-and-assign-holder",
          "name": "Compose via post",
          "description": "Attach a reusable post to the team and optionally assign a holder for an interval, without creating the post definition.",
          "inputs": [
            "team identity",
            "post identity from WM-ORG-004",
            "optional holder and assignment interval"
          ],
          "outputs": [
            "team-post link",
            "optional assignment"
          ],
          "preconditions": [
            "Referenced post exists in the Position model",
            "Assignment interval uses RFC 3339 timestamps if present"
          ],
          "effects": [
            "Team composition includes the post even if vacant",
            "Holder may become an ex-officio member"
          ],
          "source_refs": [
            "SRC-001"
          ]
        },
        {
          "id": "nest-or-reparent-team",
          "name": "Nest or reparent team",
          "description": "Set, change or clear a parent team, or split an oversized team into sibling teams sharing a goal.",
          "inputs": [
            "child team identity",
            "optional new parent team identity",
            "optional split plan"
          ],
          "outputs": [
            "updated hierarchy",
            "optional new sibling team identities"
          ],
          "preconditions": [
            "Secret or Scrum profiles are not asked to nest",
            "New parent is not a descendant of the child",
            "Actors have maintainer or owner rights on both teams when required"
          ],
          "effects": [
            "Child inherits parent entitlements where the platform so defines",
            "Direct versus inherited membership listings change",
            "A Scrum-style split shares Product Goal rather than creating hierarchy"
          ],
          "source_refs": [
            "SRC-016",
            "SRC-025"
          ]
        },
        {
          "id": "grant-team-entitlement",
          "name": "Grant team entitlement",
          "description": "Grant, inherit or revoke a permission held by the team on a resource.",
          "inputs": [
            "team identity",
            "resource identity",
            "permission level"
          ],
          "outputs": [
            "entitlement grant"
          ],
          "preconditions": [
            "Actor may manage access on the resource",
            "Child-team inheritance implications have been reviewed"
          ],
          "effects": [
            "Team members and, where defined, child-team members gain or lose resource access"
          ],
          "source_refs": [
            "SRC-020",
            "SRC-025"
          ]
        },
        {
          "id": "provision-from-external-group",
          "name": "Provision from external group",
          "description": "Create or update a Team from a SCIM Group or identity-provider group, or bind an existing team to that group.",
          "inputs": [
            "SCIM or IdP group identity",
            "target organization",
            "optional team identity"
          ],
          "outputs": [
            "team identity",
            "sync binding"
          ],
          "preconditions": [
            "Group displayName and members are available",
            "Privacy agreements for cross-domain personal data have been considered"
          ],
          "effects": [
            "Team membership is sourced from the external group",
            "Local membership writes may be blocked"
          ],
          "source_refs": [
            "SRC-022",
            "SRC-026"
          ]
        },
        {
          "id": "resolve-effective-members",
          "name": "Resolve effective members",
          "description": "Compute the effective member set, distinguishing direct, inherited, guest, role-only and nested-group members at an observation time.",
          "inputs": [
            "team identity",
            "observation time",
            "inclusion flags for inherited guests and nested groups"
          ],
          "outputs": [
            "effective member list",
            "counts by role or kind"
          ],
          "preconditions": [
            "Caller may read membership of the team"
          ],
          "effects": [
            "No write; returns an observation of membership at the stated time"
          ],
          "source_refs": [
            "SRC-019",
            "SRC-021",
            "SRC-026"
          ]
        }
      ],
      "composition": [
        {
          "target": "WM-ORG-001 (Organization)",
          "relation": "REFERENCE",
          "purpose": "Every team instance resolves to exactly one containing organization context that supplies legal recognition, obligations and the formal-organization frame; the Team model never restates legal-entity attributes.",
          "required": true,
          "source_refs": [
            "SRC-001",
            "SRC-003",
            "SRC-015"
          ]
        },
        {
          "target": "WM-ORG-004 (Position)",
          "relation": "COMPOSE",
          "purpose": "Team composition is expressed through reusable positions and their assignments; org:Post remains defined once and is bound to the team through membership records rather than copied into the team.",
          "required": true,
          "source_refs": [
            "SRC-001",
            "SRC-012"
          ]
        },
        {
          "target": "Membership assignment record (nested record type owned by WM-ORG-003)",
          "relation": "CHILD",
          "purpose": "The n-ary membership fact is governed inside this aggregate because it carries the team-specific role, period and allocation that no sibling model owns.",
          "required": true,
          "source_refs": [
            "SRC-001",
            "SRC-002"
          ]
        },
        {
          "target": "Person / Worker context model (target model id not yet registered in the vr registry)",
          "relation": "REFERENCE",
          "purpose": "Members are referenced, never embedded; personal master data, contract terms and pay remain with the person and employment models to satisfy data minimisation.",
          "required": true,
          "source_refs": [
            "SRC-004",
            "SRC-018"
          ]
        },
        {
          "target": "Provenance mix-in aligned to W3C PROV-O",
          "relation": "MIX-IN",
          "purpose": "Supplies generation, attribution, derivation and qualified-association semantics to every record in the aggregate without duplicating provenance structure per finding.",
          "required": true,
          "source_refs": [
            "SRC-006"
          ]
        },
        {
          "target": "W3C Organization Ontology (org:OrganizationalUnit, org:Membership, org:Post, org:ChangeEvent)",
          "relation": "ALIGN",
          "purpose": "Primary structural alignment for units, n-ary membership with memberDuring, posts, sites and change events; alignment only, no conformance claimed.",
          "required": false,
          "source_refs": [
            "SRC-001"
          ]
        },
        {
          "target": "HL7 FHIR R5 CareTeam and Group",
          "relation": "ALIGN",
          "purpose": "Alignment for team status lifecycle, participant role and coverage, managing organization, and the enumerated-versus-definitional membership distinction.",
          "required": false,
          "source_refs": [
            "SRC-002",
            "SRC-003"
          ]
        },
        {
          "target": "IETF RFC 7643 SCIM Group",
          "relation": "ALIGN",
          "purpose": "Alignment for identity-provider projection: immutable server id, externalId, meta versioning and the rule that membership is written through the Group resource.",
          "required": false,
          "source_refs": [
            "SRC-004"
          ]
        },
        {
          "target": "schema.org Organization and OrganizationRole",
          "relation": "ALIGN",
          "purpose": "Publication projection for externally visible teams, including time-qualified roles and founding or dissolution dates; only where the team has a genuine public presence.",
          "required": false,
          "source_refs": [
            "SRC-011"
          ]
        },
        {
          "target": "ESCO v1.2.1 and ISCO-08 occupation and skill URIs",
          "relation": "ALIGN",
          "purpose": "Governed vocabulary for occupations and competences so that capability coverage is expressed in external identifiers rather than local strings.",
          "required": false,
          "source_refs": [
            "SRC-010"
          ]
        },
        {
          "target": "ISO 30414:2025 human capital reporting",
          "relation": "ALIGN",
          "purpose": "Reference frame for metric definitions, materiality declaration and consolidation of multi-unit reporting; metric formulae are cited, not restated.",
          "required": false,
          "source_refs": [
            "SRC-009"
          ]
        },
        {
          "target": "FEMA NIMS resource typing definitions and National Qualification System",
          "relation": "ALIGN",
          "purpose": "Reference frame for capability tiering, minimum composition, position qualification and task-book evidence for operationally deployable teams.",
          "required": false,
          "source_refs": [
            "SRC-007",
            "SRC-008"
          ]
        },
        {
          "target": "HR Open Standards 4.5R OrganizationChart and Timecard domains",
          "relation": "ALIGN",
          "purpose": "Interchange alignment for units, positions and incumbents and for the worker time data underlying allocation; note that no Team noun exists in the suite.",
          "required": false,
          "source_refs": [
            "SRC-012",
            "SRC-013"
          ]
        },
        {
          "target": "Subject-scoped care team profile (FHIR CareTeam-aligned specialization)",
          "relation": "EXTEND",
          "purpose": "Specialization for teams bound to a specific subject, adding subject reference and the elevated sensitivity handling that entails.",
          "required": false,
          "source_refs": [
            "SRC-002"
          ]
        },
        {
          "target": "Typed emergency response team profile (NIMS-aligned specialization)",
          "relation": "EXTEND",
          "purpose": "Specialization adding mobilization state, ordering specifications, equipment inventory and deployment tracking for typed deployable teams.",
          "required": false,
          "source_refs": [
            "SRC-007"
          ]
        }
      ],
      "researchAdjudication": {
        "providerMode": "dual-provider",
        "activeProviders": [
          "claude",
          "grok"
        ],
        "waivedProviders": [],
        "providerPolicy": {},
        "boundaryDecision": {
          "entry_kind": "aggregate",
          "status": "accepted",
          "rationale": "The base (claude) entry kind stands. Both providers independently model membership as a first-class, time-bounded, separately identified record with its own period, role, state and provenance (claude membership-assignment-record artifact serial:true; grok membership-record artifact serial:true), which is the n-ary reification pattern of org:Membership and FHIR CareTeam.participant. A membership record has no meaning outside its team root and is never referenced independently, which is exactly the aggregate test; grok's own structure satisfies it even though grok labelled the model 'entity'. Grok's 'entity' label is therefore treated as a naming choice, not as contrary evidence, and is rejected without escalating to a critical conflict. Model boundary is fixed before node acceptance: the team node references exactly one containing organization context and never carries legal-entity identity or LEI eligibility (WM-ORG-001), never owns reusable post definitions (WM-ORG-004), and requires enumerated rather than definitional membership, so rule-defined cohorts, access-control-only groups and organization-membered collaborations are rejected as instances."
        },
        "decisions": [
          {
            "concept": "Base provider selection",
            "disposition": "claude adopted as base",
            "rationale": "Claude carries seven source-backed boundary notes against organization, position, SCIM group, definitional cohort, care team, NIMS typed-resource team and public department, plus an explicit disqualification rule for records that are not teams. Its adversarial checks test the sceptical reading that Team is only a view over Organization plus Position and resolve it on evidence. Grok is larger on deployment surface but thinner on boundary derivation; size was not the deciding factor."
          },
          {
            "concept": "Entry kind aggregate versus entity",
            "disposition": "aggregate retained, entity rejected",
            "rationale": "Membership is a separately identified, time-bounded, provenance-bearing record with no meaning outside its team root in both packs, which is the aggregate test under the org:Membership and CareTeam.participant n-ary pattern. Grok's own membership-record artifact satisfies the same test, so its entity label is a naming difference, not contrary evidence."
          },
          {
            "concept": "Names, slugs and display labels",
            "disposition": "accepted from grok into team-identity",
            "rationale": "The base states only that names are never identifiers and provides no positive structure for preferred label, locale, derived slug or rename authority. The addition is evidence-backed across ORG, FHIR, SCIM and vendor directories and closes a real hole without touching the identity priority rule."
          },
          {
            "concept": "Containing and managing organization",
            "disposition": "accepted from grok into team-identity",
            "rationale": "The base leaves the containment edge in prose while modelling only co-management as a question. Separating containing organization from managing organization and adding the hosting tenant makes the single most important team relationship explicit and testable."
          },
          {
            "concept": "Parent-child nesting and inherited membership",
            "disposition": "accepted from grok into membership-records",
            "rationale": "Inherited membership changes what the member set means and the base resolves it nowhere; a single nesting question is not sufficient structure for listings, mentions and entitlement inheritance that behave differently for direct and inherited members."
          },
          {
            "concept": "Membership provisioning, invitation and IdP synchronization",
            "disposition": "accepted from grok into membership-records with a boundary constraint",
            "rationale": "The base asks how HR and IdP write conflicts are reconciled but supplies no mechanism. Accepted on condition that any directory rule must materialise enumerated identified members, preserving the base rule that definitional rule-defined cohorts are not teams."
          },
          {
            "concept": "Team post establishment and ex-officio membership",
            "disposition": "accepted from grok into membership-records",
            "rationale": "Both providers agree post definitions stay in WM-ORG-004, but only grok models org:hasPost attachment, vacant posts and membership arising ex officio from holding a post. Establishment separate from staffing is a genuine gap in the base, and the addition does not breach the sibling-model boundary."
          },
          {
            "concept": "Visibility, discoverability and sensitivity labelling",
            "disposition": "accepted from grok into provenance-access-retention",
            "rationale": "The base covers default record visibility and GDPR principles but not discoverability class, sensitivity-label binding to a directory-preconfigured value, or the leakage case where mentioning a hidden team reveals its name. Competing visibility vocabularies are to be recorded side by side, never merged into one code list."
          },
          {
            "concept": "Team entitlements on external resources",
            "disposition": "accepted from grok into provenance-access-retention",
            "rationale": "The base access layer is entirely inbound; a team holding and inheriting permissions on resources is a distinct concern that neither provider places out of scope. The granted resources themselves remain out of scope, so only the grant relation and member, guest and owner capability sets are taken."
          },
          {
            "concept": "Grok canonical-team-identity",
            "disposition": "rejected as duplicative",
            "rationale": "Identical identity priority order to the base team-identifier-assignment finding, which additionally carries alternate business identifiers and duplicate-record tombstoning. Adding it would create a second identity finding with no new evidence."
          },
          {
            "concept": "Grok defining-purpose",
            "disposition": "rejected as duplicative",
            "rationale": "The base team-charter-and-mandate already binds org:purpose, FHIR reason and the shared-objective pattern to a written constituting statement with approval, effective date and review trigger, and is additionally anchored by a binding legal example. The grok finding is a strict subset."
          },
          {
            "concept": "Grok collaboration-versus-unit-boundary",
            "disposition": "rejected as duplicative",
            "rationale": "The base resolves this in two boundary notes and in the question asking whether the collective is an internal unit, a cross-organization collaboration or a rule-defined cohort. Promoting it to a finding would duplicate settled boundary work."
          },
          {
            "concept": "Grok roles-accountabilities-and-leadership and size-autonomy-and-accountability",
            "disposition": "rejected as duplicative",
            "rationale": "Content is already split across the base role-and-position-binding, decision-rights-ownership-and-reporting-line and minimum-composition-constraints findings, including the lead-role question and the declared constraint profile. Accepting would fragment authority semantics across three layers."
          },
          {
            "concept": "Grok operational-status and archive-error-and-deletion",
            "disposition": "rejected as duplicative; cascade hazard routed to the mapping specification",
            "rationale": "Status values, the entered-in-error versus normal-ending distinction, dissolution and retention are all covered by the base. Archive, unarchive and clone are vendor projection operations, and the hazard that deleting a team also destroys its backing directory group belongs in the projection and mapping specification artifact, not in a new lifecycle finding."
          },
          {
            "concept": "Grok site-contact-and-schedule",
            "disposition": "rejected; shift schedule and virtual-only siting deferred",
            "rationale": "Sites, distribution, jurisdiction effects and coverage gaps are covered by the base site-footprint finding and the team-level contact route is already modelled. Shift rostering rests on a single tier-2 vendor schedule object and the base deliberately declared rostering an omission; virtual-only teams are flagged as a gap by grok itself."
          },
          {
            "concept": "Grok subject-goal-or-sport",
            "disposition": "rejected; retained as an EXTEND profile candidate",
            "rationale": "The base explicitly places subject-scoped teams outside the base case because FHIR CareTeam is subject-bound and carries a patient security category. Accepting a subject binding into the base would contradict a boundary decision made on tier-1 evidence; it is deferred as a profile question instead."
          },
          {
            "concept": "RFC 3339 cited in grok findings without a registered source entry",
            "disposition": "source reference rewired to the base RFC 3339 entry",
            "rationale": "Grok asserts RFC 3339 date-time requirements in membership and post-assignment findings while registering no RFC 3339 source in its own pack. The accepted post-establishment addition must be re-pointed at the base RFC 3339 source so no merged node carries an unregistered citation."
          },
          {
            "concept": "Competing hierarchy, visibility and typing vocabularies",
            "disposition": "recorded as declared conflicts, not merged",
            "rationale": "Method-level prohibition of sub-teams conflicts with nested groups and unit hierarchy; two vendor visibility vocabularies disagree on their own labels; capability-tier typing and functional classification are orthogonal axes. Each is carried as a declared profile constraint with its source, and collapsing any of them into a single field is prohibited."
          }
        ],
        "publicationHolds": [
          "Source and live-version verification is unresolved: all twenty-nine distinct URLs across both packs must be re-fetched and re-pinned before publication, with particular attention to fast-moving or forward-dated version strings including schema.org 30.0 dated 2026-03-19, ESCO v1.2.1 dated 2025-12-10, HR Open 4.5 Final and 4.6 Candidate, the GitHub REST API version 2026-03-10, the Microsoft Graph v1.0 page last updated 2024-10-18, the FEMA RTLT tool version, and the NIST SP 800-53 control release 5.2.0.",
          "Multi-profile domain validation is unresolved: the merged model has not been instantiated against the clinical care-team profile, the workplace-directory profile, the emergency-response typed-resource profile, or the agile-delivery profile. No conformance or alignment language may be published until at least these four profiles have been round-tripped and their loss reports recorded.",
          "Paywalled and landing-page-only evidence must not be published at clause level: ISO 30414:2025 is cited from a committee announcement, ISO 30400:2022 from a catalogue landing page that does not expose a Team term, and ISO 21502 and ArchiMate business collaboration were never obtained. Every claim resting on these must be marked as unverified at clause level or removed.",
          "All seven accepted additions and four of the five accepted functions rest wholly or partly on tier-2 vendor documentation. Each must be re-checked against tier-1 sources for contradiction before publication, and vendor-specific vocabularies for visibility, nesting and archive states must be published as projection detail rather than as base semantics.",
          "Citation provenance for the accepted additions must be repaired: grok asserts RFC 3339 timestamp requirements in membership and post-assignment findings without registering RFC 3339 as a source in its own pack, so every merged node inheriting that claim must be re-pointed at the base RFC 3339 source and re-validated."
        ],
        "deferredResearch": [
          "Virtual and fully distributed teams with no physical site: both providers flag this as a gap and neither found a primary pattern for recording location without inventing a site. Needs an authoritative source before any siting rule is asserted.",
          "Shift rostering, watch and rotation patterns as a modelled construct at team granularity. Present evidence is a single tier-2 vendor schedule object; the base deliberately omitted it. Aviation, maritime and healthcare crew and watch structures should be sourced together.",
          "Team economics: budget, cost centre and chargeback assignment to a team as such. No authoritative source was found in either pack; HR interchange compensation and payroll domains are worker-level and cannot be lifted to team granularity without invention.",
          "Collective representation at team level: works councils, bargaining units and statutory governance bodies. One pack lists labour relations as a reporting topic without team-level structure and the other excludes such bodies outright; the boundary between a team and a statutory body needs primary evidence.",
          "Subject-scoped teams as an EXTEND profile: decide whether a team bound to a patient, product, event or competition is hosted by this model as a profile or by a sibling model, and source the binding trigger for teams constituted before a subject exists.",
          "Unfetched team-of-teams and domain registries: ISO 21502 project-team vocabulary, IPTC Sport Schema club and team-membership types, military order-of-battle structures, named scaled-agile team-of-teams constructs, and O*NET-SOC as the non-EU alternative to the ESCO occupation taxonomy.",
          "Governance of AI-agent and robotic teammates beyond representing them as software agents with a responsible human principal, including qualification, accountability and access semantics for non-human members."
        ]
      }
    },
    "position": {
      "publication": {
        "status": "published",
        "adjudicationStatus": "reviewable-draft",
        "publishableCanonical": false,
        "generatedAt": "2026-08-24T01:09:19Z",
        "synthesisSha256": "276439f4a06ed634dda2e84d4bb34499a521d08dbb31eab9d5dfe8fb041466e0",
        "providerMode": "dual-provider",
        "providers": [
          "Claude",
          "Grok"
        ],
        "waivedProviders": []
      },
      "model": {
        "registry_id": "vr.wm-org-004",
        "model_id": "WM-ORG-004",
        "name": "Position",
        "entry_kind": "entity",
        "purpose": "Model the position as a durable, addressable organizational construct that exists independently of any occupant: the work assigned by competent authority, classified, placed, funded, requirement-bearing and lifecycle-governed, so agents can create, inspect, classify, staff and retire positions without conflating them with people, jobs or contracts.",
        "scope_statement": "In scope is everything that is true of a position while it is vacant. A position is the bundle of duties and responsibilities assigned by competent authority (5 CFR 511.101) and modelled as org:Post, which W3C defines as a position existing independently of the person or persons filling it. The model owns identity, titling, duty content, occupational and grade classification, structural placement and reporting, location and work arrangement, capacity (FTE/headcount) and funding, requirements and essential functions, delegated and prescribed authority, risk/screening designations, working conditions, lifecycle and effective-dated change, governance and evidence, and outbound interoperability. It does not own the person, the occupancy relationship, the employment contract, the recruiting workflow, or the taxonomies it aligns to.",
        "in_scope": [
          "Position identity, keys, official and working titles, and language-tagged alternative labels",
          "Assigned duties, responsibilities and essential functions attributed to the position rather than to an incumbent",
          "Occupational classification, job/class membership, grade or level and job-evaluation outcome",
          "Placement in an organizational unit, cost centre, reporting and supervisory structure",
          "Work location, work arrangement and schedule attributes attached to the seat",
          "Capacity and occupancy control: FTE, headcount, single vs pooled, overlap tolerance, vacancy state",
          "Budget, funding source and the pay range or grade ladder framing the seat",
          "Qualification, competency, credential, screening, clearance and approval requirements",
          "Delegated decision rights and externally prescribed regulatory responsibilities allocated to the seat",
          "Lifecycle states, effective-dated versioning, classification authority, certification, appeal and retention"
        ],
        "out_of_scope": [
          "The natural person, worker or agent identity that may occupy the position",
          "The occupancy relationship itself (appointment, assignment, tenure, occupancy dates) — owned by WM-ORG-016",
          "The organizational unit as an entity, its charter and its own hierarchy — owned by WM-ORG-002",
          "Team formation and team-level goals — owned by WM-ORG-003",
          "Employment contract terms, payroll processing, absence and time records",
          "Recruiting workflow: requisition approval chain, candidate pipeline, interview and selection records",
          "The occupation, skill and competency taxonomies themselves (ISCO-08, ESCO, O*NET-SOC, NICE) — referenced, not owned",
          "Individual performance appraisal, development plans and remuneration paid to an incumbent",
          "Compensation plan and pay-structure master data (grade ladders and steps are referenced by key)"
        ],
        "boundary_notes": [
          {
            "neighbor": "WM-ORG-016 Assignment / occupancy",
            "distinction": "The position persists while vacant; the assignment exists only while an agent occupies it. W3C separates org:Post (independent of holder) from org:Membership, which exists only when an agent occupies a role. Occupancy dates, tenure and incumbent-specific terms belong to the assignment, not the position.",
            "source_refs": [
              "SRC-001"
            ]
          },
          {
            "neighbor": "WM-ORG-002 Organizational unit",
            "distinction": "A unit is a collection of people and functions with its own recognition inside a larger organization; a position is a single seat that is contained in exactly one unit at a time via org:postIn / org:hasPost. Unit charter, mandate and unit hierarchy stay with WM-ORG-002.",
            "source_refs": [
              "SRC-001",
              "SRC-009"
            ]
          },
          {
            "neighbor": "Job / class / occupation classifier",
            "distinction": "A position is an instance; a class is 'all positions which are sufficiently similar as to kind of work, level of difficulty and responsibility, and qualification requirements' (5 CFR 511.101), and an occupation is 'a set of jobs whose main tasks and duties are characterised by a high degree of similarity' (ISCO-08). Classifier definitions, code lists and hierarchies are external registries; the position holds only the coded reference and the evaluation evidence.",
            "source_refs": [
              "SRC-005",
              "SRC-007"
            ]
          },
          {
            "neighbor": "Position opening / job advertisement",
            "distinction": "A vacancy notice is a published recruiting artifact with its own validity window, datePosted, validThrough and application channel; it is a projection referencing zero, one or many positions. HR Open keeps PositionOpening in the recruiting domain and organizational structure with incumbents in OrganizationChart.",
            "source_refs": [
              "SRC-002",
              "SRC-004"
            ]
          },
          {
            "neighbor": "org:Role (abstract role)",
            "distinction": "W3C org:Role denotes the abstract role and requires a Membership instance to link a person, whereas org:Post is a concrete organizational seat. Role vocabularies (NICE work roles, ESCO occupations) are alignments, not the position itself.",
            "source_refs": [
              "SRC-001",
              "SRC-010"
            ]
          },
          {
            "neighbor": "Employment contract and payroll",
            "distinction": "Pay range, grade ladder and budget frame the seat; actual remuneration, contractual clauses and payroll results attach to the occupant's employment relation. EU pay-transparency duties bind the employer's disclosure at recruitment and reporting, not the position record's internal semantics.",
            "source_refs": [
              "SRC-012",
              "SRC-009"
            ]
          }
        ]
      },
      "selected_findings": [
        {
          "bundle": {
            "id": "position-identity-and-definition",
            "name": "Position identity and definition",
            "description": "What uniquely designates this position, what it is called, what work is assigned to it, and how that work is classified and levelled."
          },
          "layer": {
            "id": "identity-and-designation",
            "name": "Identity and designation",
            "description": "Keys, namespaces and names that let an agent address exactly one position across systems and languages."
          },
          "finding": {
            "id": "position-identifier-and-keys",
            "name": "Position identifier and key set",
            "description": "The authoritative identifier for the seat, the secondary business codes that are unique only within a scope, and the external identifiers that make it resolvable outside the master system.",
            "source_refs": [
              "SRC-001",
              "SRC-009",
              "SRC-004",
              "SRC-013"
            ],
            "questions": [
              {
                "id": "q-pid-1",
                "text": "Which system is the master of record for this position and what identifier does it assign?",
                "kind": "identity",
                "answer_data": [
                  "master system reference",
                  "master position identifier",
                  "identifier assignment instant"
                ]
              },
              {
                "id": "q-pid-2",
                "text": "Is the human-facing position code unique globally or only within a business unit or legal entity?",
                "kind": "constraint",
                "answer_data": [
                  "position code",
                  "uniqueness scope reference",
                  "collision policy"
                ]
              },
              {
                "id": "q-pid-3",
                "text": "What resolvable IRI, if any, publishes this position as an org:Post in the organization graph?",
                "kind": "interoperability",
                "answer_data": [
                  "position IRI",
                  "graph publication endpoint",
                  "rdf type assertion"
                ]
              },
              {
                "id": "q-pid-4",
                "text": "When a position is split, merged or renumbered, how are prior identifiers preserved and redirected?",
                "kind": "provenance",
                "answer_data": [
                  "superseded identifier list",
                  "succession relation type",
                  "succession effective date"
                ]
              }
            ],
            "data_elements": [
              {
                "id": "de-position-id",
                "name": "Master position identifier",
                "description": "Identifier assigned by the authoritative HRIS or position-control system; never a title or a date.",
                "value_kind": "identifier",
                "cardinality": "1",
                "required": true,
                "source_refs": [
                  "SRC-009",
                  "SRC-001"
                ]
              },
              {
                "id": "de-position-code",
                "name": "Position code",
                "description": "Human-readable code unique within a declared scope such as business unit; Oracle constrains PositionCode to uniqueness within the business unit.",
                "value_kind": "identifier",
                "cardinality": "0..1",
                "required": false,
                "source_refs": [
                  "SRC-009"
                ]
              },
              {
                "id": "de-position-iri",
                "name": "Published position IRI",
                "description": "Governed global identifier used when the position is exposed as an org:Post in a linked-data organization graph.",
                "value_kind": "identifier",
                "cardinality": "0..1",
                "required": false,
                "source_refs": [
                  "SRC-001"
                ]
              },
              {
                "id": "de-external-ids",
                "name": "External identifier set",
                "description": "Scheme-qualified identifiers used by payroll, recruiting, finance and directory systems, each with the owning system reference.",
                "value_kind": "collection",
                "cardinality": "0..n",
                "required": false,
                "source_refs": [
                  "SRC-002",
                  "SRC-004"
                ]
              },
              {
                "id": "de-identity-assigned-at",
                "name": "Identifier assignment instant",
                "description": "RFC 3339 instant at which the identifier was minted, recorded separately from the business effective date of the position.",
                "value_kind": "timestamp",
                "cardinality": "0..1",
                "required": false,
                "source_refs": [
                  "SRC-013",
                  "SRC-009"
                ]
              }
            ],
            "artifacts": [
              {
                "id": "position-master-record",
                "name": "Position master record",
                "description": "The authoritative, effective-dated record of the seat held by the master system, carrying identifiers, placement, capacity and status.",
                "media_or_form": [
                  "structured record in a system of record",
                  "exported dataset row",
                  "graph node typed as org:Post"
                ],
                "serial": true,
                "identity_strategy": "Master-system position identifier; fall back to governed IRI, then to a Dimension-minted ULID when no upstream key exists.",
                "source_refs": [
                  "SRC-009",
                  "SRC-001"
                ]
              }
            ],
            "inline_only_rationale": null
          }
        },
        {
          "bundle": {
            "id": "structural-placement-and-relations",
            "name": "Structural placement and relations",
            "description": "Where the seat sits in the organization, who it reports to, and where and how the work is performed."
          },
          "layer": {
            "id": "organizational-placement",
            "name": "Organizational placement",
            "description": "Containment in a unit and cost centre, and the reporting relations depicted on an organization chart."
          },
          "finding": {
            "id": "unit-and-cost-center-placement",
            "name": "Unit and cost centre placement",
            "description": "The single organizational unit that holds the position, the legal entity and business unit context, and the cost centre that carries it financially.",
            "source_refs": [
              "SRC-001",
              "SRC-009",
              "SRC-002"
            ],
            "questions": [
              {
                "id": "q-plc-1",
                "text": "Which organizational unit holds this position at a given effective date?",
                "kind": "composition",
                "answer_data": [
                  "unit reference",
                  "effective start date",
                  "effective end date"
                ]
              },
              {
                "id": "q-plc-2",
                "text": "Which legal entity and business unit govern the position for employment and payroll purposes?",
                "kind": "ownership",
                "answer_data": [
                  "legal entity reference",
                  "business unit reference",
                  "jurisdiction code"
                ]
              },
              {
                "id": "q-plc-3",
                "text": "Which cost centre bears the position and does it differ from the holding unit?",
                "kind": "ownership",
                "answer_data": [
                  "cost centre code",
                  "divergence reason",
                  "finance owner reference"
                ]
              },
              {
                "id": "q-plc-4",
                "text": "How is a position moved between units without losing its identity or history?",
                "kind": "lifecycle",
                "answer_data": [
                  "transfer effective date",
                  "prior unit reference",
                  "transfer authorization reference"
                ]
              }
            ],
            "data_elements": [
              {
                "id": "de-unit-ref",
                "name": "Holding organizational unit reference",
                "description": "The unit in which the post exists, corresponding to org:postIn / org:hasPost; mandatory department reference in production systems.",
                "value_kind": "reference",
                "cardinality": "1",
                "required": true,
                "source_refs": [
                  "SRC-001",
                  "SRC-009"
                ]
              },
              {
                "id": "de-business-unit",
                "name": "Business unit reference",
                "description": "Mandatory business-unit scope that also bounds position-code uniqueness.",
                "value_kind": "reference",
                "cardinality": "1",
                "required": true,
                "source_refs": [
                  "SRC-009"
                ]
              },
              {
                "id": "de-cost-center",
                "name": "Cost centre code",
                "description": "Financial owner of the seat, distinct from the organizational holder.",
                "value_kind": "code",
                "cardinality": "0..1",
                "required": false,
                "source_refs": [
                  "SRC-009"
                ]
              },
              {
                "id": "de-placement-window",
                "name": "Placement validity window",
                "description": "Effective start and end dates for the placement of the position in this unit.",
                "value_kind": "date",
                "cardinality": "0..n",
                "required": false,
                "source_refs": [
                  "SRC-009"
                ]
              }
            ],
            "artifacts": [
              {
                "id": "organization-chart-extract",
                "name": "Organization chart extract",
                "description": "Structural view containing units, positions and incumbents as exchanged in HR Open's OrganizationChart object.",
                "media_or_form": [
                  "structured org-chart payload",
                  "rendered chart",
                  "graph export"
                ],
                "serial": true,
                "identity_strategy": "Root unit reference plus as-of effective date and generation instant; regenerated rather than edited in place.",
                "source_refs": [
                  "SRC-002",
                  "SRC-001"
                ]
              }
            ],
            "inline_only_rationale": null
          }
        },
        {
          "bundle": {
            "id": "structural-placement-and-relations",
            "name": "Structural placement and relations",
            "description": "Where the seat sits in the organization, who it reports to, and where and how the work is performed."
          },
          "layer": {
            "id": "organizational-placement",
            "name": "Organizational placement",
            "description": "Containment in a unit and cost centre, and the reporting relations depicted on an organization chart."
          },
          "finding": {
            "id": "reporting-and-supervisory-relations",
            "name": "Reporting and supervisory relations",
            "description": "Post-to-post reporting lines, supervisory span and matrix or dotted-line relations that survive changes of occupant.",
            "source_refs": [
              "SRC-001",
              "SRC-009",
              "SRC-011"
            ],
            "questions": [
              {
                "id": "q-rep-1",
                "text": "To which position does this position report, and is the relation defined post-to-post or person-to-person?",
                "kind": "relationship",
                "answer_data": [
                  "reports-to target reference",
                  "relation subject type",
                  "relation effective window"
                ]
              },
              {
                "id": "q-rep-2",
                "text": "Which positions report to this one, and does that make it a supervisory position?",
                "kind": "composition",
                "answer_data": [
                  "subordinate position references",
                  "supervisory flag",
                  "span of control count"
                ]
              },
              {
                "id": "q-rep-3",
                "text": "Are there secondary, functional or matrix reporting lines and what do they authorize?",
                "kind": "relationship",
                "answer_data": [
                  "secondary relation type",
                  "counterparty position reference",
                  "authorized scope"
                ]
              },
              {
                "id": "q-rep-4",
                "text": "Who acts for this position when it is vacant or its holder is unavailable?",
                "kind": "exception",
                "answer_data": [
                  "delegate position reference",
                  "delegation trigger",
                  "delegation window"
                ]
              }
            ],
            "data_elements": [
              {
                "id": "de-reports-to",
                "name": "Reports-to relation",
                "description": "Reporting relation as depicted on an organization chart, expressible between posts rather than only between agents.",
                "value_kind": "reference",
                "cardinality": "0..n",
                "required": false,
                "source_refs": [
                  "SRC-001"
                ]
              },
              {
                "id": "de-supervisory-flag",
                "name": "Supervisory indicator",
                "description": "Whether the position supervises other positions, which materially affects classification and levelling.",
                "value_kind": "boolean",
                "cardinality": "0..1",
                "required": false,
                "source_refs": [
                  "SRC-007",
                  "SRC-001"
                ]
              },
              {
                "id": "de-delegate-position",
                "name": "Delegate position reference",
                "description": "Position designated to act for this one, mirroring the delegate-position attribute in production position records.",
                "value_kind": "reference",
                "cardinality": "0..1",
                "required": false,
                "source_refs": [
                  "SRC-009"
                ]
              },
              {
                "id": "de-relation-window",
                "name": "Relation validity window",
                "description": "Effective interval for each reporting relation, held separately from occupancy intervals.",
                "value_kind": "date",
                "cardinality": "0..n",
                "required": false,
                "source_refs": [
                  "SRC-001",
                  "SRC-009"
                ]
              }
            ],
            "artifacts": [],
            "inline_only_rationale": "Reporting structure is expressed as typed edges between position nodes and is fully carried by the position master record and the organization chart extract; a separate persisted artifact would duplicate those and risk divergence between the graph and the rendered chart."
          }
        },
        {
          "bundle": {
            "id": "capacity-funding-and-occupancy",
            "name": "Capacity, funding and occupancy control",
            "description": "How much work the seat represents, how many holders it admits, who pays for it, and whether it is currently filled."
          },
          "layer": {
            "id": "capacity-and-occupancy-control",
            "name": "Capacity and occupancy control",
            "description": "Quantified capacity of the seat and the derived vacancy state, including pooled positions with multiple holders."
          },
          "finding": {
            "id": "vacancy-and-occupancy-state",
            "name": "Vacancy and occupancy state",
            "description": "The derived state of the seat with respect to its holders: vacant, partly filled, fully filled or over-established, computed against authorized capacity.",
            "source_refs": [
              "SRC-001",
              "SRC-009"
            ],
            "questions": [
              {
                "id": "q-vac-1",
                "text": "Is the position vacant, and how is vacancy derived rather than asserted?",
                "kind": "state",
                "answer_data": [
                  "open FTE",
                  "open headcount",
                  "derivation as-of instant"
                ]
              },
              {
                "id": "q-vac-2",
                "text": "Which assignments currently consume the capacity of this position?",
                "kind": "relationship",
                "answer_data": [
                  "assignment references",
                  "consumed FTE per assignment",
                  "occupancy window"
                ]
              },
              {
                "id": "q-vac-3",
                "text": "What happens when an incoming holder would exceed authorized capacity?",
                "kind": "exception",
                "answer_data": [
                  "overlap allowed flag",
                  "warning or block outcome",
                  "override authority reference"
                ]
              },
              {
                "id": "q-vac-4",
                "text": "How long has the position been vacant and does that trigger review or lapse?",
                "kind": "temporal",
                "answer_data": [
                  "vacancy start instant",
                  "vacancy duration",
                  "lapse or review trigger"
                ]
              }
            ],
            "data_elements": [
              {
                "id": "de-open-capacity",
                "name": "Open capacity",
                "description": "Remaining unconsumed FTE and headcount at an as-of instant; the basis for incumbent validation.",
                "value_kind": "quantity",
                "cardinality": "0..1",
                "required": false,
                "source_refs": [
                  "SRC-009"
                ]
              },
              {
                "id": "de-occupancy-links",
                "name": "Occupancy links",
                "description": "References to the assignment records that hold the post, corresponding to org:heldBy; the occupancy itself is owned by the assignment model.",
                "value_kind": "reference",
                "cardinality": "0..n",
                "required": false,
                "source_refs": [
                  "SRC-001"
                ]
              },
              {
                "id": "de-vacancy-since",
                "name": "Vacant since instant",
                "description": "RFC 3339 instant from which the seat has had unconsumed capacity, distinct from the ingestion instant of the computation.",
                "value_kind": "timestamp",
                "cardinality": "0..1",
                "required": false,
                "source_refs": [
                  "SRC-013",
                  "SRC-001"
                ]
              },
              {
                "id": "de-overlap-outcome",
                "name": "Overlap validation outcome",
                "description": "Whether exceeding capacity produced a warning or a hard block, and who overrode it.",
                "value_kind": "code",
                "cardinality": "0..1",
                "required": false,
                "source_refs": [
                  "SRC-009"
                ]
              }
            ],
            "artifacts": [],
            "inline_only_rationale": "Vacancy is a derived state, not a stored assertion: it is computed from authorized capacity in the position master record minus capacity consumed by assignment records owned by WM-ORG-016. Persisting it as an independent artifact would create a second, drift-prone source of truth; only the computation's as-of instant and inputs are recorded."
          }
        },
        {
          "bundle": {
            "id": "requirements-authority-and-risk",
            "name": "Requirements, authority and risk",
            "description": "What the seat demands of any holder, what it empowers the holder to do, and what risk and conditions it carries."
          },
          "layer": {
            "id": "authority-and-accountability",
            "name": "Authority and accountability",
            "description": "Decision rights delegated to the seat and externally prescribed responsibilities allocated to it."
          },
          "finding": {
            "id": "delegated-authority-and-decision-rights",
            "name": "Delegated authority and decision rights",
            "description": "The approval limits, signing powers and decision scopes attached to the seat by competent authority, independent of who holds it.",
            "source_refs": [
              "SRC-007",
              "SRC-001",
              "SRC-011"
            ],
            "questions": [
              {
                "id": "q-aut-1",
                "text": "Which decisions may the holder of this position take, and up to what limit?",
                "kind": "authority",
                "answer_data": [
                  "decision scope reference",
                  "monetary or scope limit",
                  "limit currency or unit"
                ]
              },
              {
                "id": "q-aut-2",
                "text": "Which competent authority conferred each delegation and when does it expire?",
                "kind": "provenance",
                "answer_data": [
                  "conferring authority reference",
                  "conferral instant",
                  "expiry or review date"
                ]
              },
              {
                "id": "q-aut-3",
                "text": "Do the delegations lapse, transfer or escalate when the position is vacant?",
                "kind": "exception",
                "answer_data": [
                  "vacancy behaviour code",
                  "escalation target position",
                  "interim authority window"
                ]
              },
              {
                "id": "q-aut-4",
                "text": "Does the position have sufficient seniority and resources to exercise its authority?",
                "kind": "validation",
                "answer_data": [
                  "seniority assessment outcome",
                  "resource sufficiency evidence",
                  "assessment date"
                ]
              }
            ],
            "data_elements": [
              {
                "id": "de-decision-right",
                "name": "Decision right",
                "description": "A named authority conferred on the seat, with scope and any quantitative limit.",
                "value_kind": "object",
                "cardinality": "0..n",
                "required": false,
                "source_refs": [
                  "SRC-007",
                  "SRC-011"
                ]
              },
              {
                "id": "de-conferring-authority",
                "name": "Conferring authority reference",
                "description": "The competent authority that assigned the work and its associated powers to the position.",
                "value_kind": "reference",
                "cardinality": "0..n",
                "required": false,
                "source_refs": [
                  "SRC-007"
                ]
              },
              {
                "id": "de-vacancy-authority-rule",
                "name": "Vacancy authority rule",
                "description": "What happens to each delegation while the seat is unoccupied: lapse, escalate to the reports-to post, or transfer to a delegate.",
                "value_kind": "code",
                "cardinality": "0..n",
                "required": false,
                "source_refs": [
                  "SRC-011",
                  "SRC-009"
                ]
              }
            ],
            "artifacts": [
              {
                "id": "delegation-of-authority-schedule",
                "name": "Delegation of authority schedule",
                "description": "Governed schedule mapping decision rights and limits to positions, with conferral and expiry dates.",
                "media_or_form": [
                  "authority matrix",
                  "structured delegation record set",
                  "approved schedule document"
                ],
                "serial": true,
                "identity_strategy": "Schedule identifier plus version and effective-start date; position-level entries keyed by position identifier.",
                "source_refs": [
                  "SRC-011",
                  "SRC-007"
                ]
              }
            ],
            "inline_only_rationale": null
          }
        },
        {
          "bundle": {
            "id": "lifecycle-governance-and-recordkeeping",
            "name": "Lifecycle, governance and recordkeeping",
            "description": "How positions come into existence, change, are contested, and end, and how the record is kept and disposed of."
          },
          "layer": {
            "id": "lifecycle-and-effective-dating",
            "name": "Lifecycle and effective dating",
            "description": "Status transitions of the seat and the bitemporal discipline that separates business effect from record capture."
          },
          "finding": {
            "id": "position-lifecycle-states",
            "name": "Position lifecycle states",
            "description": "The permitted status values of a seat — proposed, approved, frozen, active, inactive, abolished — and the transitions and authorities that move between them.",
            "source_refs": [
              "SRC-009",
              "SRC-008"
            ],
            "questions": [
              {
                "id": "q-lif-1",
                "text": "What is the current hiring status and activity status of the position, and are they independent?",
                "kind": "state",
                "answer_data": [
                  "hiring status code",
                  "active status code",
                  "status as-of date"
                ]
              },
              {
                "id": "q-lif-2",
                "text": "Which transitions are permitted and who may authorize each one?",
                "kind": "lifecycle",
                "answer_data": [
                  "from and to status",
                  "authorizing role",
                  "transition precondition"
                ]
              },
              {
                "id": "q-lif-3",
                "text": "May a position be frozen or abolished while occupied, and what must happen first?",
                "kind": "constraint",
                "answer_data": [
                  "occupancy precondition",
                  "required prior action",
                  "exception approval reference"
                ]
              },
              {
                "id": "q-lif-4",
                "text": "Can an abolished position be reinstated, or must a new identity be minted?",
                "kind": "decision",
                "answer_data": [
                  "reinstatement policy code",
                  "identity continuity rule",
                  "precedent reference"
                ]
              }
            ],
            "data_elements": [
              {
                "id": "de-hiring-status",
                "name": "Hiring status",
                "description": "Whether the seat is proposed, approved or frozen for staffing purposes.",
                "value_kind": "code",
                "cardinality": "1",
                "required": true,
                "source_refs": [
                  "SRC-009"
                ]
              },
              {
                "id": "de-active-status",
                "name": "Active status",
                "description": "Whether the position record is active or inactive, held separately from hiring status.",
                "value_kind": "code",
                "cardinality": "1",
                "required": true,
                "source_refs": [
                  "SRC-009"
                ]
              },
              {
                "id": "de-transition-authority",
                "name": "Transition authorization",
                "description": "Role and identity that authorized a status transition, with the authorization instant.",
                "value_kind": "reference",
                "cardinality": "0..n",
                "required": false,
                "source_refs": [
                  "SRC-008",
                  "SRC-007"
                ]
              },
              {
                "id": "de-abolition-date",
                "name": "Abolition effective date",
                "description": "Business date on which the seat ceases to exist, distinct from the date the record was closed.",
                "value_kind": "date",
                "cardinality": "0..1",
                "required": false,
                "source_refs": [
                  "SRC-008",
                  "SRC-013"
                ]
              }
            ],
            "artifacts": [
              {
                "id": "position-status-decision",
                "name": "Position status decision record",
                "description": "Record of each establishment, approval, freeze, reinstatement or abolition decision with its authority and effective date.",
                "media_or_form": [
                  "decision record",
                  "establishment action document",
                  "structured status event"
                ],
                "serial": true,
                "identity_strategy": "Position identifier plus monotonically increasing decision sequence and RFC 3339 decision instant.",
                "source_refs": [
                  "SRC-008",
                  "SRC-009"
                ]
              }
            ],
            "inline_only_rationale": null
          }
        },
        {
          "bundle": {
            "id": "lifecycle-governance-and-recordkeeping",
            "name": "Lifecycle, governance and recordkeeping",
            "description": "How positions come into existence, change, are contested, and end, and how the record is kept and disposed of."
          },
          "layer": {
            "id": "lifecycle-and-effective-dating",
            "name": "Lifecycle and effective dating",
            "description": "Status transitions of the seat and the bitemporal discipline that separates business effect from record capture."
          },
          "finding": {
            "id": "effective-dated-change-and-history",
            "name": "Effective-dated change and history",
            "description": "Version history of the seat where every attribute set is bounded by effective dates and queryable as of a date, with record instants kept separate.",
            "source_refs": [
              "SRC-009",
              "SRC-013",
              "SRC-008"
            ],
            "questions": [
              {
                "id": "q-hst-1",
                "text": "What did this position look like as of a given effective date?",
                "kind": "temporal",
                "answer_data": [
                  "as-of date",
                  "attribute snapshot",
                  "version identifier"
                ]
              },
              {
                "id": "q-hst-2",
                "text": "When was each version recorded, as distinct from when it took business effect?",
                "kind": "provenance",
                "answer_data": [
                  "effective start and end dates",
                  "record creation instant",
                  "last update instant"
                ]
              },
              {
                "id": "q-hst-3",
                "text": "Is a change a correction of an erroneous record or a genuine change in the work?",
                "kind": "quality",
                "answer_data": [
                  "change type code",
                  "reason code",
                  "correcting actor identity"
                ]
              },
              {
                "id": "q-hst-4",
                "text": "How are open-ended versions terminated and what end-date sentinel is used?",
                "kind": "constraint",
                "answer_data": [
                  "end-date sentinel value",
                  "termination rule",
                  "sentinel interpretation note"
                ]
              }
            ],
            "data_elements": [
              {
                "id": "de-effective-window",
                "name": "Effective start and end dates",
                "description": "Business validity window of a version; production systems use a far-future sentinel for open-ended versions.",
                "value_kind": "date",
                "cardinality": "1..n",
                "required": true,
                "source_refs": [
                  "SRC-009"
                ]
              },
              {
                "id": "de-record-instants",
                "name": "Record creation and update instants",
                "description": "RFC 3339 instants with explicit offsets recording when the version was captured and last modified.",
                "value_kind": "timestamp",
                "cardinality": "1..n",
                "required": true,
                "source_refs": [
                  "SRC-009",
                  "SRC-013"
                ]
              },
              {
                "id": "de-change-type",
                "name": "Change type",
                "description": "Correction versus substantive change, which determines whether prior versions remain assertable.",
                "value_kind": "code",
                "cardinality": "0..1",
                "required": false,
                "source_refs": [
                  "SRC-008"
                ]
              },
              {
                "id": "de-change-reason",
                "name": "Change reason code",
                "description": "Governed reason for the change, such as reorganization, reclassification, funding change or appeal outcome.",
                "value_kind": "code",
                "cardinality": "0..1",
                "required": false,
                "source_refs": [
                  "SRC-008"
                ]
              }
            ],
            "artifacts": [
              {
                "id": "position-change-history",
                "name": "Position change history",
                "description": "Append-only sequence of effective-dated versions and the record instants at which each was captured.",
                "media_or_form": [
                  "version history table",
                  "event log",
                  "as-of query result set"
                ],
                "serial": true,
                "identity_strategy": "Position identifier plus version sequence; each entry carries both its effective window and its RFC 3339 record instants.",
                "source_refs": [
                  "SRC-009",
                  "SRC-013"
                ]
              }
            ],
            "inline_only_rationale": null
          }
        }
      ],
      "functions": [
        {
          "id": "establish-position",
          "name": "Establish position",
          "description": "Create a new seat by recording the duties assigned by competent authority, mint its identifier and place it in a unit.",
          "inputs": [
            "assigned duty statements",
            "holding unit and business unit references",
            "assigning authority reference",
            "proposed effective date"
          ],
          "outputs": [
            "position master record in proposed status",
            "minted position identifier",
            "establishment authorization artifact"
          ],
          "preconditions": [
            "competent authority has assigned the duties",
            "holding unit exists and is active",
            "identifier namespace is declared by the owner package"
          ],
          "effects": [
            "a new position identity exists and is addressable",
            "hiring status is set to proposed",
            "an establishment decision is appended to the change history"
          ],
          "source_refs": [
            "SRC-007",
            "SRC-009",
            "SRC-001"
          ]
        },
        {
          "id": "classify-position",
          "name": "Classify position",
          "description": "Analyse the assigned duties and place the position in an internal class and one or more external occupational codes.",
          "inputs": [
            "position description",
            "classification plan or job catalogue reference",
            "external scheme versions"
          ],
          "outputs": [
            "job or class assignment",
            "occupation code assertions with scheme and version",
            "classification evaluation record"
          ],
          "preconditions": [
            "a current position description exists",
            "the classifier holds classification authority",
            "scheme versions are pinned"
          ],
          "effects": [
            "position becomes comparable across statistics and systems",
            "classification effective date is recorded separately from the decision instant"
          ],
          "source_refs": [
            "SRC-007",
            "SRC-008",
            "SRC-005",
            "SRC-003"
          ]
        },
        {
          "id": "evaluate-and-level-position",
          "name": "Evaluate and level position",
          "description": "Apply objective, gender-neutral evaluation criteria to assign a grade and allocate the position to a category of workers.",
          "inputs": [
            "duty and responsibility set",
            "working-conditions profile",
            "evaluation scheme reference"
          ],
          "outputs": [
            "grade or level assignment",
            "criterion ratings",
            "category of workers allocation",
            "job evaluation statement"
          ],
          "preconditions": [
            "evaluation scheme is documented as objective and gender-neutral",
            "skills, effort, responsibility and working conditions are all assessable"
          ],
          "effects": [
            "position is levelled and comparable for equal-value analysis",
            "pay range derivation basis becomes available"
          ],
          "source_refs": [
            "SRC-012",
            "SRC-007",
            "SRC-009"
          ]
        },
        {
          "id": "set-capacity-and-funding",
          "name": "Set capacity and funding",
          "description": "Authorize FTE, headcount, position type and overlap tolerance, and bind the seat to a budget and funding source.",
          "inputs": [
            "requested FTE and headcount",
            "position type",
            "budget amount, currency and fiscal period",
            "funding source reference"
          ],
          "outputs": [
            "capacity authorization artifact",
            "funding authorization artifact",
            "updated position master record"
          ],
          "preconditions": [
            "budget authority approval is present",
            "capacity values are internally consistent"
          ],
          "effects": [
            "occupancy validation gains an enforceable ceiling",
            "establishment and budget reporting can include the seat"
          ],
          "source_refs": [
            "SRC-009"
          ]
        },
        {
          "id": "specify-requirements",
          "name": "Specify requirements and essential functions",
          "description": "Record essential and marginal functions, competencies, credentials and experience required of any holder, using versioned catalogue references.",
          "inputs": [
            "duty statements with time shares",
            "competency catalogue references",
            "credential and experience requirements"
          ],
          "outputs": [
            "essential functions analysis",
            "position competency model",
            "requirement strength assignments"
          ],
          "preconditions": [
            "duties are decomposed at task granularity",
            "catalogue versions are pinned",
            "analysis is authored before advertising or interviewing"
          ],
          "effects": [
            "requirements become auditable evidence for selection and accommodation decisions"
          ],
          "source_refs": [
            "SRC-014",
            "SRC-010",
            "SRC-003",
            "SRC-002"
          ]
        },
        {
          "id": "allocate-authority-and-responsibilities",
          "name": "Allocate authority and prescribed responsibilities",
          "description": "Confer decision rights on the seat and allocate any regulator-prescribed responsibilities to it without leaving gaps.",
          "inputs": [
            "decision scopes and limits",
            "prescribed responsibility list",
            "seniority and resource assessment"
          ],
          "outputs": [
            "delegation of authority schedule entries",
            "statement of responsibilities",
            "responsibilities map update"
          ],
          "preconditions": [
            "the position is sufficiently senior for the responsibilities",
            "gap analysis across the firm has been performed"
          ],
          "effects": [
            "accountability is attributable to a designated seat independent of turnover",
            "vacancy behaviour for each delegation is defined"
          ],
          "source_refs": [
            "SRC-011",
            "SRC-007"
          ]
        },
        {
          "id": "designate-risk-and-screening",
          "name": "Designate risk and screening requirements",
          "description": "Determine the clearance, vetting, regulatory approval and access requirements that attach to the seat before recruitment starts.",
          "inputs": [
            "access entitlements implied by the duties",
            "applicable screening regime",
            "regulatory approval regime"
          ],
          "outputs": [
            "position risk and screening designation record",
            "re-screening interval",
            "approval prerequisite flag"
          ],
          "preconditions": [
            "duties and access entitlements are known",
            "the applicable regime is identified for the seat's jurisdiction"
          ],
          "effects": [
            "recruitment and provisioning can enforce prerequisites",
            "lapse handling rules become executable"
          ],
          "source_refs": [
            "SRC-009",
            "SRC-011",
            "SRC-010"
          ]
        },
        {
          "id": "reconcile-occupancy-and-vacancy",
          "name": "Reconcile occupancy and vacancy",
          "description": "Compute consumed and open capacity from assignment records and validate incoming occupancy against the authorization.",
          "inputs": [
            "authorized FTE and headcount",
            "overlap allowed flag",
            "current assignment references and consumed capacity",
            "as-of instant"
          ],
          "outputs": [
            "open FTE and open headcount",
            "vacancy state and vacant-since instant",
            "overlap validation outcome"
          ],
          "preconditions": [
            "assignment records are readable from the occupancy model",
            "capacity authorization is current at the as-of date"
          ],
          "effects": [
            "vacancy is derived rather than asserted",
            "capacity breaches are warned or blocked per the overlap flag"
          ],
          "source_refs": [
            "SRC-009",
            "SRC-001"
          ]
        },
        {
          "id": "amend-or-reclassify-position",
          "name": "Amend or reclassify position",
          "description": "Apply an effective-dated change to duties, placement, capacity or classification, distinguishing correction from substantive change.",
          "inputs": [
            "proposed attribute changes",
            "effective date",
            "change type and reason code",
            "authorizing party"
          ],
          "outputs": [
            "new effective-dated version",
            "updated change history entry",
            "re-issued description or evaluation where triggered"
          ],
          "preconditions": [
            "authorizing party holds the relevant authority",
            "effective date does not silently overwrite prior versions"
          ],
          "effects": [
            "prior versions remain queryable as of their effective windows",
            "dependent artifacts are flagged for review"
          ],
          "source_refs": [
            "SRC-009",
            "SRC-008",
            "SRC-013"
          ]
        },
        {
          "id": "certify-and-appeal",
          "name": "Certify description and process appeals",
          "description": "Certify the accuracy of the position description and administer challenges to its classification, applying decision effective dates.",
          "inputs": [
            "current position description",
            "certifier identity and role",
            "appeal submission where present"
          ],
          "outputs": [
            "certification record",
            "classification appeal decision",
            "corrected classification with its effective date"
          ],
          "preconditions": [
            "the description states the duties actually assigned",
            "the appellant and the matter are within scope of appeal"
          ],
          "effects": [
            "the record becomes evidentiary",
            "corrected classifications take effect on their own governed date"
          ],
          "source_refs": [
            "SRC-007",
            "SRC-008",
            "SRC-014"
          ]
        },
        {
          "id": "publish-position-projection",
          "name": "Publish position projection",
          "description": "Generate an outbound projection of the position for a named recipient profile, applying suppression rules and disclosure duties.",
          "inputs": [
            "position master record",
            "payload profile name",
            "jurisdictional disclosure obligations",
            "suppression rules"
          ],
          "outputs": [
            "position exchange payload",
            "pay range disclosure record where required",
            "publication window values"
          ],
          "preconditions": [
            "position is in an approved status for staffing projections",
            "required pay-range disclosure has been determined for the jurisdiction"
          ],
          "effects": [
            "downstream systems and the public receive a governed subset",
            "disclosure evidence is retained"
          ],
          "source_refs": [
            "SRC-002",
            "SRC-004",
            "SRC-012"
          ]
        },
        {
          "id": "freeze-abolish-or-dispose",
          "name": "Freeze, abolish or dispose position",
          "description": "Move the seat to frozen or abolished status and, at the end of retention, apply the governed disposition action to its records.",
          "inputs": [
            "target status and effective date",
            "occupancy state",
            "retention rule and hold status",
            "disposition action"
          ],
          "outputs": [
            "position status decision record",
            "closed effective windows",
            "disposition record"
          ],
          "preconditions": [
            "occupancy preconditions are satisfied or explicitly overridden",
            "no preservation hold is active before disposition"
          ],
          "effects": [
            "the seat stops consuming establishment and budget",
            "history is preserved until retention expiry, then disposed with an auditable record"
          ],
          "source_refs": [
            "SRC-009",
            "SRC-008",
            "SRC-011"
          ]
        },
        {
          "id": "authorize-fill",
          "name": "Authorize fill or freeze",
          "description": "Permit or withhold recruitment against a vacant Position, producing a fill-authorization that a JobPosting or requisition may reference.",
          "inputs": [
            "Position id",
            "occupancy state",
            "freeze or fill decision",
            "deciding authority"
          ],
          "outputs": [
            "freeze flag or fill-authorization id",
            "decision timestamps"
          ],
          "preconditions": [
            "Position is established and not abolished.",
            "Classification and PD are adequate if the local regime requires them before advertisement."
          ],
          "effects": [
            "A JobPosting may be linked as an advertisement of this vacancy; the posting is not the Position.",
            "Freeze withholds fill without abolishing the slot."
          ],
          "source_refs": [
            "SRC-020",
            "SRC-022",
            "SRC-025"
          ]
        }
      ],
      "composition": [
        {
          "target": "WM-ORG-002 Organizational unit",
          "relation": "CHILD",
          "purpose": "Every position is contained in exactly one organizational unit at a given effective date, matching org:postIn / org:hasPost and the mandatory department reference in production position records.",
          "required": true,
          "source_refs": [
            "SRC-001",
            "SRC-009"
          ]
        },
        {
          "target": "WM-ORG-003 Team",
          "relation": "REFERENCE",
          "purpose": "Teams are composed through positions and their assignments; positions remain reusable across team formations and are referenced, not owned, by the team model.",
          "required": false,
          "source_refs": [
            "SRC-001",
            "SRC-002"
          ]
        },
        {
          "target": "WM-ORG-016 Assignment / occupancy",
          "relation": "COMPOSE",
          "purpose": "A position is occupied through a scoped assignment; occupancy, tenure and incumbent-specific terms live there, mirroring the org:Post versus org:Membership separation, and supply the consumed capacity used to derive vacancy.",
          "required": true,
          "source_refs": [
            "SRC-001",
            "SRC-009"
          ]
        },
        {
          "target": "Job / class / occupation classifier model (sibling; registry entry not yet identified)",
          "relation": "REFERENCE",
          "purpose": "The class grouping similar positions and the occupational category are external classifier concepts; the position holds only coded references, not the class definitions or hierarchies.",
          "required": true,
          "source_refs": [
            "SRC-007",
            "SRC-005"
          ]
        },
        {
          "target": "Person / worker identity model (sibling; registry entry not yet identified)",
          "relation": "REFERENCE",
          "purpose": "Incumbents are referenced only indirectly through assignments so that the position record carries no personal data of its own.",
          "required": false,
          "source_refs": [
            "SRC-001"
          ]
        },
        {
          "target": "ISCO-08 (International Standard Classification of Occupations)",
          "relation": "ALIGN",
          "purpose": "Alignment target for occupational coding and for the job-versus-occupation distinction; mapping strength and version are recorded and conformance is not claimed without assessment evidence.",
          "required": false,
          "source_refs": [
            "SRC-005"
          ]
        },
        {
          "target": "ESCO occupations pillar",
          "relation": "ALIGN",
          "purpose": "Alignment target for multilingual labels, scope notes, regulatory aspects and essential or optional skills at ISCO level 5 and below.",
          "required": false,
          "source_refs": [
            "SRC-003"
          ]
        },
        {
          "target": "O*NET Content Model",
          "relation": "ALIGN",
          "purpose": "Alignment target for duty decomposition into work activities, for requirement typing and for environmental work-context descriptors.",
          "required": false,
          "source_refs": [
            "SRC-006"
          ]
        },
        {
          "target": "W3C Organization Ontology (org:Post)",
          "relation": "ALIGN",
          "purpose": "Ontological alignment for publishing positions as graph nodes with postIn, heldBy and reportsTo edges, and for the vacancy-independent semantics of a post.",
          "required": false,
          "source_refs": [
            "SRC-001"
          ]
        },
        {
          "target": "HR Open Standards 4.5 (OrganizationChart, PositionOpening, PositionCompetencyModel, HRMasterData)",
          "relation": "ALIGN",
          "purpose": "Exchange alignment for organizational structure, recruiting projections, competency models and provisioning payloads.",
          "required": false,
          "source_refs": [
            "SRC-002"
          ]
        },
        {
          "target": "schema.org JobPosting",
          "relation": "ALIGN",
          "purpose": "Publication alignment for the advertisement projection only; the posting is a time-bounded document about the position, not the position itself.",
          "required": false,
          "source_refs": [
            "SRC-004"
          ]
        },
        {
          "target": "NICE Workforce Framework work roles (NIST SP 800-181 Rev.1)",
          "relation": "ALIGN",
          "purpose": "Alignment for composing Task, Knowledge and Skill statements into reusable requirement sets that organizations map onto positions.",
          "required": false,
          "source_refs": [
            "SRC-010"
          ]
        },
        {
          "target": "Effective-dated versioning and provenance mixin",
          "relation": "MIX-IN",
          "purpose": "Supplies the bitemporal pattern separating business effective windows from RFC 3339 record and observation instants, reused by every attribute group in this model.",
          "required": true,
          "source_refs": [
            "SRC-009",
            "SRC-013"
          ]
        },
        {
          "target": "Regulated-firm accountability extension (SM&CR-style designated functions)",
          "relation": "EXTEND",
          "purpose": "Adds prescribed responsibility allocation, statements of responsibilities and responsibilities maps for positions in regulated firms without imposing them on all adopters.",
          "required": false,
          "source_refs": [
            "SRC-011"
          ]
        },
        {
          "target": "Statutory position-classification extension (General Schedule style)",
          "relation": "EXTEND",
          "purpose": "Adds statutory class, grade, official position description certification, classification appeal and effective-date rules for public-sector adopters bound by such a plan.",
          "required": false,
          "source_refs": [
            "SRC-007",
            "SRC-008"
          ]
        }
      ],
      "researchAdjudication": {
        "providerMode": "dual-provider",
        "activeProviders": [
          "claude",
          "grok"
        ],
        "waivedProviders": [],
        "providerPolicy": {},
        "boundaryDecision": {
          "entry_kind": "entity",
          "status": "accepted",
          "rationale": "Both providers independently classify WM-ORG-004 as an entity and both anchor it on the same test: the record must be able to exist while vacant. That test is decidable, is grounded in W3C ORG (org:Post exists independently of the person filling it) and in the regulatory definition of a position as work assigned by competent authority, and it cleanly separates the seat from occupancy (WM-ORG-016), from the unit (WM-ORG-002), from the abstract role, and from the recruitment advertisement. No split or reclassification is warranted; the base boundary is adopted as written, with grok's word-sense and FHIR disambiguations carried forward as boundary annotations rather than as new structure."
        },
        "decisions": [
          {
            "concept": "Base provider selection",
            "disposition": "claude as base",
            "rationale": "Claude offers a single decidable boundary test (everything true of a position while it is vacant), names the owning sibling model for each exclusion, carries roughly 1.4 times the base's own layer count in findings with four questions each, and declares one honest gap. Grok has more bundles and layers but nineteen findings across nineteen layers, so its topology is thinner per node despite the larger frame."
          },
          {
            "concept": "Entry kind",
            "disposition": "entity, accepted",
            "rationale": "Independent agreement between providers plus the vacant-existence test grounded in W3C ORG and the regulatory definition of assigned work; nothing in either pack suggests an event, service or relationship framing would fit better."
          },
          {
            "concept": "Grok eight-bundle topology",
            "disposition": "rejected in favour of base topology",
            "rationale": "Grok's split of location, compensation and establishment into separate top-level bundles fragments concerns the base already integrates, and re-parenting the base's twenty-seven findings into nineteen thin layers would lose the base's explicit inline-only rationales without adding evidence."
          },
          {
            "concept": "Abstract role binding",
            "disposition": "accepted into alignment-and-exchange",
            "rationale": "Materially absent from the base, evidence-backed on ORG, Popolo and schema.org, and consistent with the base's own statement that role vocabularies are alignments rather than the position itself."
          },
          {
            "concept": "Geographic area and constituency",
            "disposition": "accepted into work-location-and-arrangement",
            "rationale": "Distinct from duty station and work arrangement; Popolo ties post existence to area existence and schema.org scopes occupational description by region, and the base's omissions list already concedes elected and appointed offices are underserved."
          },
          {
            "concept": "Interoperability profile declaration",
            "disposition": "accepted into alignment-and-exchange",
            "rationale": "The ORG-versus-Popolo disagreement about direct holds is genuine and source-backed; recording the profile in force per instance is the mechanism that keeps it a declared configuration rather than an unresolved contradiction."
          },
          {
            "concept": "Fill authorization",
            "disposition": "accepted as a narrowed function",
            "rationale": "Closes the only real hole in the base function set and marks the boundary handoff to the excluded recruiting domain; narrowed to fill so it does not duplicate the base freeze and abolish function."
          },
          {
            "concept": "Grok class, series and grade finding",
            "disposition": "rejected as duplicative",
            "rationale": "The base already separates occupational classification from grade and job evaluation across two findings with twelve questions and both a classification evaluation record and a job evaluation statement; grok adds no evidence the base lacks."
          },
          {
            "concept": "Grok occupation code alignment finding",
            "disposition": "rejected as duplicative",
            "rationale": "Covered by the base occupational-classification finding plus the version-pinned crosswalk finding, both of which already require scheme, version and mapping strength; the ISCO armed-forces-major-group nuance is deferred instead."
          },
          {
            "concept": "Grok position remuneration band finding",
            "disposition": "rejected as duplicative",
            "rationale": "The base pay-range-and-transparency finding already fixes the position band against occupant pay and adds disclosure and reporting duties; only the unpaid, nominal-pay and fee-basis case is genuinely new and it is too thin to stand as structure, so it is deferred."
          },
          {
            "concept": "Grok hosting organization finding",
            "disposition": "rejected as duplicative",
            "rationale": "The base unit-and-cost-centre finding covers holding unit, legal entity, business unit and cost centre with movement semantics; the residual ex officio and Post-as-Organization dual-typing questions are deferred rather than injected."
          },
          {
            "concept": "Grok constraints-on-the-position finding",
            "disposition": "rejected as split across existing layers",
            "rationale": "Its three elements land separately in the base screening-and-clearance, retention-and-privacy and pay findings; injecting it whole would create overlapping ownership of sensitivity and privacy rules across two bundles."
          },
          {
            "concept": "Vacancy as derived state",
            "disposition": "retained from base, corroborated",
            "rationale": "Both providers independently refuse to persist occupancy on the seat and both cite ORG and the assignment boundary; the base's no-artifact rationale is kept because a stored vacancy flag would create a second source of truth against WM-ORG-016."
          },
          {
            "concept": "Retention dimension status",
            "disposition": "retained as gap, not upgraded",
            "rationale": "Grok marks retention covered while its own notes concede national schedules were not fetched; the base's gap marking is the accurate one and no fetched primary source in either pack states a retention period for position records."
          },
          {
            "concept": "Source identifier collision",
            "disposition": "re-key all source ids on merge",
            "rationale": "SRC-002 denotes HR Open in the base and Popolo in grok, and several other identifiers collide across providers while pointing at different documents; the synthesizer must re-key rather than union by identifier or every accepted addition will carry the wrong citation."
          },
          {
            "concept": "FHIR and word-sense disambiguation",
            "disposition": "carried as boundary annotation, not structure",
            "rationale": "Grok's align-not-equate treatment of PractitionerRole and its exclusion of financial, geospatial and sports senses of position are correct and useful, but they are boundary prose rather than findings; they are recorded as a publication hold on the boundary notes instead of being injected as nodes."
          }
        ],
        "publicationHolds": [
          "Source verification is incomplete: every base URL and version pin must be re-resolved at publication time. In particular the base cites 5 CFR and 29 CFR from the Cornell LII reproduction because eCFR and opm.gov were unreachable in its run, while grok reached eCFR current as of 2026-08-20 and the OPM classification standards PDF; re-verify and dual-cite or swap to the official host before publishing.",
          "Source identifiers collide across providers with different underlying documents (SRC-002 is HR Open in the base and Popolo in grok, among others). All sources must be re-keyed during merge and every accepted addition re-pointed, and the merged source list re-verified as live, before any draft is published.",
          "ISO 30400:2022 must not be cited as defining position, job, role or FTE: grok's own note concedes the term text was not inspectable behind the paywall, so only the standard's existence, date and scope are supportable. The ISCO-08 citation must likewise resolve to an authoritative ILO or UNSD host rather than the third-party netlify mirror used by grok.",
          "Retention and disposition periods remain a declared gap. No fetched primary source in either pack states a retention period for position records, descriptions or classification decisions; the structure may be published only as a required local determination, never as canonical guidance.",
          "Multi-profile domain validation is outstanding. Evidence concentrates on US federal General Schedule classification, UK FCA prescribed responsibilities, EU pay transparency and a single HCM vendor API. Before publication the model must be exercised against at least a civic or legislative profile (Popolo post with constituency), a healthcare profile (FHIR PractitionerRole unnamed slot) and a non-US private-sector profile, and every regional assumption must be labelled a jurisdiction profile rather than a universal requirement.",
          "Published boundary notes must carry grok's disambiguations verbatim in substance: HL7 FHIR PractitionerRole is aligned, not equated, to a classified position, and the financial, geospatial and sports senses of the word position are excluded, including schema.org's Quarterback example of a named position."
        ],
        "deferredResearch": [
          "Post-as-Organization dual typing and ex officio membership conferred by holding a post (W3C ORG and Popolo), unresolved against the WM-ORG-002 unit and WM-ORG-003 team boundaries and against corporate statutory officer roles versus board membership.",
          "Unpaid, honorary, nominal-pay, fee-basis, piece-work and volunteer positions, and statutory exclusions from classification and pay statutes such as 5 U.S.C. section 5102(c); currently only reachable through grok's rejected remuneration finding.",
          "Military billets versus rank as personal status (including ISCO Major Group 0 alignment), academic faculty lines and endowed chairs, and elected or appointed public office appointment and eligibility rules.",
          "Works council, co-determination and collective consultation duties triggered by position creation, reclassification and abolition; no primary source was verified by either provider.",
          "Occupancy of a position by a non-human agent, unresolved in both packs even though org:holds is defined over agents rather than persons.",
          "National retention schedules (for example NARA GRS) and GDPR storage-limitation periods as concrete durations for position descriptions, classification files and occupant-linked records.",
          "Unfetched standard texts that would strengthen weakly supported areas: HR Open Position and PositionOpening full schemas, the ESCO occupation pillar beyond its ISCO mapping, ISO 30414 human capital metrics, and ISO 30400 term entries.",
          "Dual-incumbency overlap windows for succession, career-ladder or intern positions, job-share fractions and union exclusivity of a slot, all widely practised but without primary support in either run."
        ]
      }
    },
    "assignment": {
      "publication": {
        "status": "published",
        "adjudicationStatus": "reviewable-draft",
        "publishableCanonical": false,
        "generatedAt": "2026-08-24T02:52:14Z",
        "synthesisSha256": "ae1b264d2d9d71872f3f8803680d7e602ad13ef4eb00f5630a2fe08bbf41e201",
        "providerMode": "dual-provider",
        "providers": [
          "Claude",
          "Grok"
        ],
        "waivedProviders": []
      },
      "model": {
        "registry_id": "vr.wm-org-016",
        "model_id": "WM-ORG-016",
        "name": "Work Assignment",
        "entry_kind": "relationship",
        "purpose": "Model the time-bounded, scoped binding of a person or non-human agent to a role, position or body of work within an organization, together with the authority, place, effort, preconditions, lifecycle and evidence that make the binding operable and auditable.",
        "scope_statement": "A Work Assignment is a reified n-ary relationship between an assignee agent, an organization or unit, a role or post, a bounded work scope and a validity period. The model covers how such a binding is identified, classified, authorized, constrained, changed, evidenced and ended. It deliberately holds no definition of the position itself, no contract terms, no person master data and no task-instance execution state; those belong to sibling models and are referenced. The model is format-neutral: JSON, YAML, Markdown, Git, MCP and MongoDB are projections of this semantics, never its source.",
        "in_scope": [
          "Identity, classification and versioning of the individual assignment record",
          "The n-ary participant set: assignee agent, organization/unit, role or post, engagement context",
          "Bounded work scope: objectives, services, caseload, accounts, operational period, exclusions",
          "Granted authority, decision limits, reporting lines, delegation and acting cover",
          "Place of work, mobility, cross-border work and the jurisdictional consequences that follow",
          "Effort allocation and capacity share across concurrent assignments",
          "Effective period, working pattern, availability, duty and rest limits",
          "Assignment lifecycle states, transitions, amendment, handover and offboarding",
          "Eligibility preconditions: competence, credentials, fitness, screening, right to work",
          "Constraints: separation of duty, conflict of interest, cardinality and coverage rules",
          "Authorization evidence, acknowledgement, statutory notification and disclosure",
          "Personal-data classification, access scoping, retention, deletion and legal hold",
          "Alignment to external representations and projection to downstream consumers"
        ],
        "out_of_scope": [
          "Definition, classification, grading and description of the position or post itself (WM-ORG-004)",
          "Employment contract formation and terms, remuneration determination and benefits (WM-ORG-005)",
          "Person, party and agent master identity records",
          "Organization structure, unit hierarchy and legal-entity data",
          "Role, occupation, skill and competence taxonomies as concepts (referenced as classifiers)",
          "Per-task work-item claiming, execution and completion state",
          "Permission and entitlement catalogues, and the access-decision engine itself",
          "Concrete shift instances, time capture, timesheets and attendance actuals",
          "Payroll calculation, cost allocation and inter-company recharge",
          "Performance objectives, appraisal outcomes and succession candidate pools"
        ],
        "boundary_notes": [
          {
            "neighbor": "WM-ORG-004 Position",
            "distinction": "A post exists independently of the person or persons filling it; the assignment is the time-bounded occupancy of that post. Reclassifying a post does not create an assignment, and ending an assignment does not abolish the post.",
            "source_refs": [
              "SRC-001"
            ]
          },
          {
            "neighbor": "WM-ORG-005 Employment relationship",
            "distinction": "The employment relationship is the legal engagement; one engagement can carry several concurrent assignments, and an assignment can rest on a commercial staffing contract or a volunteer arrangement instead of employment. Statutory written particulars attach to the engagement, not to each assignment.",
            "source_refs": [
              "SRC-010",
              "SRC-014"
            ]
          },
          {
            "neighbor": "Role and occupation classifiers (ESCO/ISCO-08, professional specialty codes)",
            "distinction": "A role is an abstract concept in a controlled vocabulary; the assignment is a concrete dated instance that cites it. Classifier codes are alignments held on the assignment, not definitions owned by it.",
            "source_refs": [
              "SRC-001",
              "SRC-006",
              "SRC-002"
            ]
          },
          {
            "neighbor": "Human task / work-item model",
            "distinction": "A task instance has its own short-lived lifecycle with potential owners and an actual owner established by claiming. A work assignment is the standing eligibility and authority from which potential-owner sets are derived; it does not carry task-instance state.",
            "source_refs": [
              "SRC-003"
            ]
          },
          {
            "neighbor": "Access management and entitlement model",
            "distinction": "RBAC user-to-role assignment is a downstream projection of this model. The permission catalogue, role hierarchy and session activation are governed elsewhere; this model supplies the authoritative temporal and organizational basis for provisioning and de-provisioning.",
            "source_refs": [
              "SRC-004"
            ]
          },
          {
            "neighbor": "Schedule, roster and availability model",
            "distinction": "The assignment states the working pattern, availability windows and applicable duty limits; the concrete dated shift or duty instances live in a scheduling model that references the assignment identifier.",
            "source_refs": [
              "SRC-011",
              "SRC-002"
            ]
          },
          {
            "neighbor": "Time capture and timecard model",
            "distinction": "Hours actually worked are observations evidencing performance under an assignment. They are never the assignment itself and must not be used to infer its effective period.",
            "source_refs": [
              "SRC-014"
            ]
          },
          {
            "neighbor": "Incident and operational tasking records",
            "distinction": "Operational tasking documents bind resources to a single operational period and a specific incident objective. They are short-horizon instances of assignment semantics and should reference, not replace, the standing assignment where one exists.",
            "source_refs": [
              "SRC-012"
            ]
          }
        ]
      },
      "selected_findings": [
        {
          "bundle": {
            "id": "assignment-identity-and-definition",
            "name": "Assignment Identity and Definition",
            "description": "What an individual work assignment is as a distinct record: how it is identified, which participants it binds, how it is typed, and what kind of agent may hold it."
          },
          "layer": {
            "id": "assignment-core-relation",
            "name": "Core Assignment Relation",
            "description": "The identity, participant structure and typing of the assignment record itself."
          },
          "finding": {
            "id": "assignment-record-identity",
            "name": "Assignment record identity and versioning",
            "description": "How one assignment instance is identified and kept distinct from the position, the role concept and the person, including identifier priority, correction versus real-world change, and supersession chains.",
            "source_refs": [
              "SRC-001",
              "SRC-002",
              "SRC-008"
            ],
            "questions": [
              {
                "id": "q-identity-master",
                "text": "Which system is the authoritative master for this assignment identifier, and what identifier value and scheme does it issue?",
                "kind": "identity",
                "answer_data": [
                  "Master system name or URI",
                  "Assignment identifier value",
                  "Identifier scheme or namespace"
                ]
              },
              {
                "id": "q-identity-fallback",
                "text": "If no authoritative master identifier exists, which governed IRI or Dimension-assigned UUID/ULID is used instead?",
                "kind": "identity",
                "answer_data": [
                  "Fallback identifier type",
                  "Issuing Dimension",
                  "Minted identifier value"
                ]
              },
              {
                "id": "q-identity-recurrence",
                "text": "How are two assignments of the same agent to the same post in different periods kept distinct without using a date as the identifier?",
                "kind": "identity",
                "answer_data": [
                  "Distinguishing key strategy",
                  "Sequence or occurrence number",
                  "Rule text"
                ]
              },
              {
                "id": "q-identity-correction",
                "text": "How is a corrected version of the assignment record distinguished from a genuine change to the assignment in the world?",
                "kind": "provenance",
                "answer_data": [
                  "Record version identifier",
                  "Change class (correction or real-world change)",
                  "Superseded record reference"
                ]
              }
            ],
            "data_elements": [
              {
                "id": "de-assignment-id",
                "name": "assignment_id",
                "description": "Primary identifier of the assignment instance, resolved by the identity priority rule.",
                "value_kind": "identifier",
                "cardinality": "1",
                "required": true,
                "source_refs": [
                  "SRC-001",
                  "SRC-002"
                ]
              },
              {
                "id": "de-assignment-id-scheme",
                "name": "assignment_id_scheme",
                "description": "Namespace or scheme that governs the primary identifier.",
                "value_kind": "code",
                "cardinality": "0..1",
                "required": false,
                "source_refs": [
                  "SRC-002"
                ]
              },
              {
                "id": "de-record-version",
                "name": "record_version",
                "description": "Version of the record as stored, incremented on correction rather than on real-world change.",
                "value_kind": "identifier",
                "cardinality": "0..1",
                "required": false,
                "source_refs": [
                  "SRC-007"
                ]
              },
              {
                "id": "de-supersedes-ref",
                "name": "supersedes_assignment_ref",
                "description": "Reference to the assignment record this one replaces.",
                "value_kind": "reference",
                "cardinality": "0..1",
                "required": false,
                "source_refs": [
                  "SRC-001"
                ]
              }
            ],
            "artifacts": [],
            "inline_only_rationale": "Identity is a set of inline key values carried on the assignment record itself. The register that holds them is this model's own storage projection, not a separately governed artifact."
          }
        },
        {
          "bundle": {
            "id": "assignment-identity-and-definition",
            "name": "Assignment Identity and Definition",
            "description": "What an individual work assignment is as a distinct record: how it is identified, which participants it binds, how it is typed, and what kind of agent may hold it."
          },
          "layer": {
            "id": "assignment-core-relation",
            "name": "Core Assignment Relation",
            "description": "The identity, participant structure and typing of the assignment record itself."
          },
          "finding": {
            "id": "assignment-participants-and-relation-shape",
            "name": "Participant set and relation shape",
            "description": "The n-ary participants that constitute the assignment: assignee agent, assigning organization or unit, role or post, host organization where different, and the engagement context that gives it a basis.",
            "source_refs": [
              "SRC-001",
              "SRC-002",
              "SRC-014"
            ],
            "questions": [
              {
                "id": "q-participants-triple",
                "text": "Which agent, which organizational unit and which role or post does this assignment bind together?",
                "kind": "composition",
                "answer_data": [
                  "Assignee agent reference",
                  "Organization or unit reference",
                  "Post or role reference"
                ]
              },
              {
                "id": "q-participants-basis",
                "text": "Which employment relationship, staffing contract or volunteer arrangement gives this assignment its basis, and is the assignee engaged by a different organization from the one where the work is performed?",
                "kind": "authority",
                "answer_data": [
                  "Engagement context reference",
                  "Engagement type code",
                  "Host organization reference"
                ]
              },
              {
                "id": "q-participants-shape",
                "text": "Is the assignment expressed against a defined post, an abstract role concept, or a bespoke scope with no post at all?",
                "kind": "classification",
                "answer_data": [
                  "Relation shape code",
                  "Post reference or null",
                  "Role concept references"
                ]
              },
              {
                "id": "q-participants-mutability",
                "text": "Which participant changes may be made in place and which force the creation of a new assignment record?",
                "kind": "constraint",
                "answer_data": [
                  "Immutable participant list",
                  "Mutable participant list",
                  "Rule reference"
                ]
              }
            ],
            "data_elements": [
              {
                "id": "de-assignee-agent-ref",
                "name": "assignee_agent_ref",
                "description": "Reference to the person, unit or non-human agent that holds the assignment.",
                "value_kind": "reference",
                "cardinality": "1",
                "required": true,
                "source_refs": [
                  "SRC-001",
                  "SRC-007"
                ]
              },
              {
                "id": "de-assigning-org-ref",
                "name": "assigning_organization_ref",
                "description": "Organization or unit in which the assignment is held.",
                "value_kind": "reference",
                "cardinality": "1",
                "required": true,
                "source_refs": [
                  "SRC-001"
                ]
              },
              {
                "id": "de-host-org-ref",
                "name": "host_organization_ref",
                "description": "Organization where the work is actually performed when it differs from the engaging organization.",
                "value_kind": "reference",
                "cardinality": "0..1",
                "required": false,
                "source_refs": [
                  "SRC-014"
                ]
              },
              {
                "id": "de-engagement-context-ref",
                "name": "engagement_context_ref",
                "description": "Reference to the employment relationship, staffing contract or other arrangement underpinning the assignment.",
                "value_kind": "reference",
                "cardinality": "0..1",
                "required": false,
                "source_refs": [
                  "SRC-010",
                  "SRC-014"
                ]
              }
            ],
            "artifacts": [
              {
                "id": "assignment-instrument",
                "name": "Assignment instrument",
                "description": "The issued document that constitutes or communicates the assignment: assignment letter, deployment order, secondment agreement or staffing assignment confirmation naming the parties, scope and period.",
                "media_or_form": [
                  "signed document",
                  "structured message",
                  "rendered document in any presentation format"
                ],
                "serial": true,
                "identity_strategy": "Instrument reference issued by the originating system, carried alongside the assignment_id; the instrument identifier is never reused after amendment.",
                "source_refs": [
                  "SRC-014",
                  "SRC-010"
                ]
              }
            ],
            "inline_only_rationale": null
          }
        },
        {
          "bundle": {
            "id": "assignment-scope-and-authority",
            "name": "Assignment Scope and Authority",
            "description": "What the assignment covers and what it empowers: the role linkage, the bounded body of work, the place of work, the authority granted, supervision and delegation, and the share of capacity consumed."
          },
          "layer": {
            "id": "scope-of-work-and-place",
            "name": "Scope of Work and Place",
            "description": "The role linkage, the concrete body of work covered, and where the work is performed."
          },
          "finding": {
            "id": "role-and-position-linkage",
            "name": "Role, post and occupation classification linkage",
            "description": "Which post the assignment fills, which role concepts and external occupation or specialty codes describe it, the title used towards the assignee, and what happens when the underlying post is reclassified.",
            "source_refs": [
              "SRC-001",
              "SRC-002",
              "SRC-006"
            ],
            "questions": [
              {
                "id": "q-role-post",
                "text": "Which post does the assignment fill, and which role concepts describe what the assignee actually does?",
                "kind": "composition",
                "answer_data": [
                  "Post reference",
                  "Role concept references",
                  "Derivation note where role differs from post"
                ]
              },
              {
                "id": "q-role-classifier",
                "text": "Which external occupation, specialty or professional classification codes apply, and at what version of the classification?",
                "kind": "interoperability",
                "answer_data": [
                  "Classification scheme identifier",
                  "Code value and URI",
                  "Scheme version"
                ]
              },
              {
                "id": "q-role-title",
                "text": "What job title is used towards the assignee, and does it differ from the classified title of the post?",
                "kind": "definition",
                "answer_data": [
                  "Working job title",
                  "Classified post title",
                  "Divergence reason"
                ]
              },
              {
                "id": "q-role-reclassification",
                "text": "If the post is reclassified or the classification scheme is reversioned, does the assignment persist unchanged and under what rule?",
                "kind": "lifecycle",
                "answer_data": [
                  "Persistence rule",
                  "Reclassification event reference",
                  "Required re-approval flag"
                ]
              }
            ],
            "data_elements": [
              {
                "id": "de-assigned-job-title",
                "name": "assigned_job_title",
                "description": "Title by which the assignment is known to the assignee and to third parties.",
                "value_kind": "text",
                "cardinality": "1",
                "required": true,
                "source_refs": [
                  "SRC-010"
                ]
              },
              {
                "id": "de-occupation-code",
                "name": "occupation_classification_code",
                "description": "Governed occupation or specialty code with its scheme and version.",
                "value_kind": "code",
                "cardinality": "0..n",
                "required": false,
                "source_refs": [
                  "SRC-006",
                  "SRC-002"
                ]
              },
              {
                "id": "de-post-ref",
                "name": "post_ref",
                "description": "Reference to the post or position occupied through this assignment.",
                "value_kind": "reference",
                "cardinality": "0..1",
                "required": false,
                "source_refs": [
                  "SRC-001"
                ]
              }
            ],
            "artifacts": [],
            "inline_only_rationale": "Role linkage is reference data: codes and pointers into externally governed classifiers and into the Position model. The classification standards themselves are third-party artifacts, not artifacts produced by this model."
          }
        },
        {
          "bundle": {
            "id": "assignment-scope-and-authority",
            "name": "Assignment Scope and Authority",
            "description": "What the assignment covers and what it empowers: the role linkage, the bounded body of work, the place of work, the authority granted, supervision and delegation, and the share of capacity consumed."
          },
          "layer": {
            "id": "authority-supervision-and-capacity",
            "name": "Authority, Supervision and Capacity",
            "description": "What the assignment empowers the assignee to decide, to whom they answer, what may be delegated, and how much capacity the assignment consumes."
          },
          "finding": {
            "id": "granted-authority-and-decision-rights",
            "name": "Granted authority and decision limits",
            "description": "The decisions, approvals and financial limits the assignment authorizes, distinguishing authority inherent in the post from authority granted to this assignee, and the validity of that authority in its own right.",
            "source_refs": [
              "SRC-001",
              "SRC-004",
              "SRC-007"
            ],
            "questions": [
              {
                "id": "q-auth-what",
                "text": "What decisions, approvals and financial limits does this assignment authorize the assignee to exercise?",
                "kind": "authority",
                "answer_data": [
                  "Authority item descriptions",
                  "Financial or quantitative limits",
                  "Scope qualifiers per item"
                ]
              },
              {
                "id": "q-auth-source",
                "text": "Which authorities flow from the post itself and which were granted specifically to this assignee?",
                "kind": "provenance",
                "answer_data": [
                  "Authority source code per item",
                  "Granting instrument reference",
                  "Granting agent reference"
                ]
              },
              {
                "id": "q-auth-validity",
                "text": "Does each granted authority have its own validity period, and does it lapse automatically when the assignment ends or is suspended?",
                "kind": "temporal",
                "answer_data": [
                  "Authority validity start and end",
                  "Automatic lapse rule",
                  "Residual authority after end"
                ]
              },
              {
                "id": "q-auth-competence-of-grantor",
                "text": "Was the granting agent themselves authorized to confer authority at this level and scope?",
                "kind": "validation",
                "answer_data": [
                  "Grantor authority check outcome",
                  "Grantor assignment reference",
                  "Escalation taken where insufficient"
                ]
              }
            ],
            "data_elements": [
              {
                "id": "de-granted-authority-item",
                "name": "granted_authority_item",
                "description": "A single conferred decision right with its qualifiers and limits.",
                "value_kind": "object",
                "cardinality": "0..n",
                "required": false,
                "source_refs": [
                  "SRC-001",
                  "SRC-004"
                ]
              },
              {
                "id": "de-approval-limit",
                "name": "approval_limit",
                "description": "Quantitative ceiling on approvals the assignee may make, with unit and currency where applicable.",
                "value_kind": "quantity",
                "cardinality": "0..n",
                "required": false,
                "source_refs": [
                  "SRC-004"
                ]
              },
              {
                "id": "de-authority-validity-period",
                "name": "authority_validity_period",
                "description": "Start and end of an individual authority grant, independent of the assignment period.",
                "value_kind": "object",
                "cardinality": "0..n",
                "required": false,
                "source_refs": [
                  "SRC-008",
                  "SRC-001"
                ]
              }
            ],
            "artifacts": [
              {
                "id": "delegation-of-authority-instrument",
                "name": "Delegation of authority instrument",
                "description": "The governed instrument conferring named decision rights and limits on an assignee, recording grantor, grantee, scope, limits, validity period and any conditions or compensating controls.",
                "media_or_form": [
                  "signed instrument",
                  "structured record",
                  "register entry"
                ],
                "serial": true,
                "identity_strategy": "Instrument identifier issued by the authority register, referencing the assignment_id; superseded instruments are retained and marked, never overwritten.",
                "source_refs": [
                  "SRC-004",
                  "SRC-007"
                ]
              }
            ],
            "inline_only_rationale": null
          }
        },
        {
          "bundle": {
            "id": "assignment-scope-and-authority",
            "name": "Assignment Scope and Authority",
            "description": "What the assignment covers and what it empowers: the role linkage, the bounded body of work, the place of work, the authority granted, supervision and delegation, and the share of capacity consumed."
          },
          "layer": {
            "id": "authority-supervision-and-capacity",
            "name": "Authority, Supervision and Capacity",
            "description": "What the assignment empowers the assignee to decide, to whom they answer, what may be delegated, and how much capacity the assignment consumes."
          },
          "finding": {
            "id": "supervision-reporting-and-delegation",
            "name": "Supervision, reporting lines and delegation",
            "description": "To whom the assignee reports for this assignment, who may change or end it, whether work or authority may be delegated or forwarded, and how acting cover is recorded when the assignee is unavailable.",
            "source_refs": [
              "SRC-001",
              "SRC-003",
              "SRC-007"
            ],
            "questions": [
              {
                "id": "q-super-reportsto",
                "text": "To whom does the assignee report for this assignment, and is there more than one reporting line?",
                "kind": "relationship",
                "answer_data": [
                  "Reports-to references",
                  "Reporting line type per reference",
                  "Precedence where lines conflict"
                ]
              },
              {
                "id": "q-super-controller",
                "text": "Who may amend, suspend, transfer or terminate this assignment, and is that the same party as the reporting line?",
                "kind": "authority",
                "answer_data": [
                  "Controlling agent references",
                  "Permitted actions per controller",
                  "Basis for the control right"
                ]
              },
              {
                "id": "q-super-delegation",
                "text": "May the assignee delegate or forward the work or the authority, to whom, and does accountability transfer with it?",
                "kind": "authority",
                "answer_data": [
                  "Delegation permitted flag",
                  "Eligible delegate set",
                  "Accountability transfer rule"
                ]
              },
              {
                "id": "q-super-acting",
                "text": "How is temporary acting cover recorded when the assignee is absent, and does the original assignment remain active during it?",
                "kind": "process",
                "answer_data": [
                  "Acting cover assignment reference",
                  "Cover period",
                  "Status of the covered assignment"
                ]
              }
            ],
            "data_elements": [
              {
                "id": "de-reports-to-ref",
                "name": "reports_to_ref",
                "description": "Agent or post to which the assignee reports for this assignment.",
                "value_kind": "reference",
                "cardinality": "0..n",
                "required": false,
                "source_refs": [
                  "SRC-001"
                ]
              },
              {
                "id": "de-reporting-line-type",
                "name": "reporting_line_type_code",
                "description": "Nature of each reporting line, such as line management, functional or operational command.",
                "value_kind": "code",
                "cardinality": "0..n",
                "required": false,
                "source_refs": [
                  "SRC-001",
                  "SRC-012"
                ]
              },
              {
                "id": "de-delegation-permitted",
                "name": "delegation_permitted",
                "description": "Whether work or authority under this assignment may be delegated or forwarded.",
                "value_kind": "boolean",
                "cardinality": "1",
                "required": true,
                "source_refs": [
                  "SRC-003",
                  "SRC-007"
                ]
              },
              {
                "id": "de-delegate-ref",
                "name": "delegate_ref",
                "description": "Agent currently acting on behalf of the assignee under a delegation.",
                "value_kind": "reference",
                "cardinality": "0..n",
                "required": false,
                "source_refs": [
                  "SRC-007",
                  "SRC-003"
                ]
              }
            ],
            "artifacts": [],
            "inline_only_rationale": "Reporting and delegation are relationship attributes evaluated at query time. Where a delegation is formalized it is captured by the delegation of authority instrument in the sibling finding, so no additional artifact is warranted."
          }
        },
        {
          "bundle": {
            "id": "assignment-scope-and-authority",
            "name": "Assignment Scope and Authority",
            "description": "What the assignment covers and what it empowers: the role linkage, the bounded body of work, the place of work, the authority granted, supervision and delegation, and the share of capacity consumed."
          },
          "layer": {
            "id": "authority-supervision-and-capacity",
            "name": "Authority, Supervision and Capacity",
            "description": "What the assignment empowers the assignee to decide, to whom they answer, what may be delegated, and how much capacity the assignment consumes."
          },
          "finding": {
            "id": "effort-allocation-and-capacity",
            "name": "Effort allocation and capacity share",
            "description": "The share of the assignee's capacity the assignment consumes, how total allocation is validated across concurrent assignments, and which measure prevails when contracted, scheduled and allocated effort disagree.",
            "source_refs": [
              "SRC-010",
              "SRC-014",
              "SRC-002"
            ],
            "questions": [
              {
                "id": "q-effort-share",
                "text": "What share of the assignee's capacity does this assignment consume, expressed in which unit and over which reference period?",
                "kind": "measurement",
                "answer_data": [
                  "Allocation value",
                  "Allocation unit",
                  "Reference period"
                ]
              },
              {
                "id": "q-effort-validation",
                "text": "How is total allocation across all of the assignee's concurrent assignments validated, and what is the permitted ceiling?",
                "kind": "validation",
                "answer_data": [
                  "Aggregate allocation",
                  "Ceiling rule",
                  "Validation outcome and exceptions"
                ]
              },
              {
                "id": "q-effort-authority",
                "text": "Which measure is authoritative when contracted hours, scheduled hours and allocated effort disagree?",
                "kind": "quality",
                "answer_data": [
                  "Authoritative measure code",
                  "Precedence rule",
                  "Discrepancy record"
                ]
              },
              {
                "id": "q-effort-partperiod",
                "text": "How is allocation restated for a part-period assignment or one whose allocation changes mid-period?",
                "kind": "temporal",
                "answer_data": [
                  "Effective-dated allocation entries",
                  "Proration rule",
                  "Restated aggregate"
                ]
              }
            ],
            "data_elements": [
              {
                "id": "de-allocation-value",
                "name": "allocation_value",
                "description": "Capacity share consumed by this assignment, such as a full-time-equivalent fraction or hours per reference period.",
                "value_kind": "number",
                "cardinality": "0..1",
                "required": false,
                "source_refs": [
                  "SRC-014"
                ]
              },
              {
                "id": "de-allocation-basis-code",
                "name": "allocation_basis_code",
                "description": "Basis on which allocation is expressed and which measure is authoritative.",
                "value_kind": "code",
                "cardinality": "0..1",
                "required": false,
                "source_refs": [
                  "SRC-010"
                ]
              },
              {
                "id": "de-contracted-hours",
                "name": "contracted_hours_per_period",
                "description": "Hours the assignment is expected to require over a stated reference period.",
                "value_kind": "quantity",
                "cardinality": "0..1",
                "required": false,
                "source_refs": [
                  "SRC-010"
                ]
              }
            ],
            "artifacts": [],
            "inline_only_rationale": "Allocation is a set of effective-dated numeric attributes on the relation. Aggregate capacity reports are derived outputs of the workforce reporting dimension and are not artifacts owned by this model."
          }
        },
        {
          "bundle": {
            "id": "assignment-time-and-schedule",
            "name": "Assignment Time and Schedule",
            "description": "When the assignment is valid, how it relates to preceding, succeeding and concurrent assignments, the working pattern and availability it carries, and the duty and rest limits that constrain it."
          },
          "layer": {
            "id": "effective-period-and-succession",
            "name": "Effective Period and Succession",
            "description": "Validity boundaries of the assignment and its relation to other assignments in time."
          },
          "finding": {
            "id": "effective-period-concurrency-and-succession",
            "name": "Effective period, concurrency and succession",
            "description": "The assignment's start and end instants and their precision, the separation of real-world effective time from record time, the treatment of backdating and correction, and the relation to concurrent, predecessor and successor assignments.",
            "source_refs": [
              "SRC-001",
              "SRC-002",
              "SRC-008"
            ],
            "questions": [
              {
                "id": "q-time-period",
                "text": "What are the assignment's effective start and end instants, at what precision, and is an explicit UTC offset or Z recorded on each?",
                "kind": "temporal",
                "answer_data": [
                  "Effective start timestamp",
                  "Effective end timestamp or null",
                  "Precision and offset note"
                ]
              },
              {
                "id": "q-time-term",
                "text": "Is the assignment open-ended, fixed-term or terminated by a defined event, and what exactly ends it?",
                "kind": "lifecycle",
                "answer_data": [
                  "Term type code",
                  "Terminating event definition",
                  "Expected end where known"
                ]
              },
              {
                "id": "q-time-bitemporal",
                "text": "How is the real-world effective time kept separate from the time the record was created, observed or ingested?",
                "kind": "provenance",
                "answer_data": [
                  "Effective time values",
                  "Record creation timestamp",
                  "Ingestion or observation timestamp"
                ]
              },
              {
                "id": "q-time-concurrency",
                "text": "Which other assignments does this agent hold over an overlapping period, are such overlaps permitted, and which assignment precedes and succeeds this one for the same post?",
                "kind": "relationship",
                "answer_data": [
                  "Concurrent assignment references",
                  "Overlap policy outcome",
                  "Predecessor and successor references"
                ]
              },
              {
                "id": "q-time-transfer-day",
                "text": "How is a same-day transfer between posts represented so that headcount and coverage are not double-counted?",
                "kind": "measurement",
                "answer_data": [
                  "Boundary convention (inclusive or exclusive end)",
                  "Counting rule",
                  "Worked example outcome"
                ]
              }
            ],
            "data_elements": [
              {
                "id": "de-effective-start",
                "name": "effective_start",
                "description": "Instant from which the assignment is valid, with explicit offset or Z.",
                "value_kind": "timestamp",
                "cardinality": "1",
                "required": true,
                "source_refs": [
                  "SRC-008",
                  "SRC-001"
                ]
              },
              {
                "id": "de-effective-end",
                "name": "effective_end",
                "description": "Instant at which the assignment ceases to be valid; absent for open-ended assignments.",
                "value_kind": "timestamp",
                "cardinality": "0..1",
                "required": false,
                "source_refs": [
                  "SRC-008",
                  "SRC-002"
                ]
              },
              {
                "id": "de-term-type-code",
                "name": "term_type_code",
                "description": "Whether the assignment is open-ended, fixed-term or event-terminated.",
                "value_kind": "code",
                "cardinality": "1",
                "required": true,
                "source_refs": [
                  "SRC-010"
                ]
              },
              {
                "id": "de-record-created-at",
                "name": "record_created_at",
                "description": "Instant the assignment record was created or ingested, distinct from its effective time.",
                "value_kind": "timestamp",
                "cardinality": "1",
                "required": true,
                "source_refs": [
                  "SRC-008",
                  "SRC-007"
                ]
              },
              {
                "id": "de-predecessor-ref",
                "name": "predecessor_assignment_ref",
                "description": "Assignment that occupied the same post immediately before this one.",
                "value_kind": "reference",
                "cardinality": "0..1",
                "required": false,
                "source_refs": [
                  "SRC-001"
                ]
              },
              {
                "id": "de-overlap-policy-code",
                "name": "overlap_policy_code",
                "description": "Whether overlapping assignments for the same agent or post are permitted, warned or blocked.",
                "value_kind": "code",
                "cardinality": "0..1",
                "required": false,
                "source_refs": [
                  "SRC-004"
                ]
              }
            ],
            "artifacts": [],
            "inline_only_rationale": "Temporal boundaries and succession links are inline scalar values and references. The evidencing documents for a start or end are the assignment instrument and the change statement held elsewhere in the model."
          }
        },
        {
          "bundle": {
            "id": "assignment-lifecycle-and-change",
            "name": "Assignment Lifecycle and Change",
            "description": "How an assignment moves from proposal to end: its states, the events and approvals that move it, how material changes are made and notified, and what must be handed over and revoked when it ends or transfers."
          },
          "layer": {
            "id": "states-and-transitions",
            "name": "States and Transitions",
            "description": "The permitted state set and the events, actors and preconditions that move an assignment between states."
          },
          "finding": {
            "id": "assignment-state-model-and-transitions",
            "name": "State model, transitions and triggers",
            "description": "The complete permitted state set including terminal states, whether active status is stored or derived, which events and approvals drive each transition, what happens automatically at the effective end, and how an erroneous transition is reversed.",
            "source_refs": [
              "SRC-003",
              "SRC-002",
              "SRC-007"
            ],
            "questions": [
              {
                "id": "q-state-set",
                "text": "What is the complete set of permitted assignment states, which are terminal, and which transitions are forbidden?",
                "kind": "state",
                "answer_data": [
                  "State enumeration",
                  "Terminal state flags",
                  "Forbidden transition list"
                ]
              },
              {
                "id": "q-state-derivation",
                "text": "Is active status stored explicitly, derived from the effective period, or both, and which prevails when they disagree?",
                "kind": "quality",
                "answer_data": [
                  "Status source",
                  "Derivation rule",
                  "Conflict precedence and alert"
                ]
              },
              {
                "id": "q-state-triggers",
                "text": "Which events trigger each transition, which require explicit human approval, and which actor performs them?",
                "kind": "event",
                "answer_data": [
                  "Transition event catalogue",
                  "Approval requirement per transition",
                  "Permitted actor roles"
                ]
              },
              {
                "id": "q-state-automatic-end",
                "text": "What transition occurs automatically at the effective end instant, and what happens if the end data is missing or in the past when discovered?",
                "kind": "exception",
                "answer_data": [
                  "Automatic transition rule",
                  "Missing-end handling",
                  "Late-discovery remediation"
                ]
              },
              {
                "id": "q-state-reversal",
                "text": "How is a transition made in error reversed while preserving the original entry in the audit trail?",
                "kind": "provenance",
                "answer_data": [
                  "Reversal event reference",
                  "Original event retained",
                  "Reason and approver"
                ]
              }
            ],
            "data_elements": [
              {
                "id": "de-assignment-status-code",
                "name": "assignment_status_code",
                "description": "Current lifecycle state of the assignment from the governed state set.",
                "value_kind": "code",
                "cardinality": "1",
                "required": true,
                "source_refs": [
                  "SRC-003",
                  "SRC-002"
                ]
              },
              {
                "id": "de-status-effective-at",
                "name": "status_effective_at",
                "description": "Instant from which the current state applies, with explicit offset or Z.",
                "value_kind": "timestamp",
                "cardinality": "1",
                "required": true,
                "source_refs": [
                  "SRC-008"
                ]
              },
              {
                "id": "de-transition-event",
                "name": "transition_event",
                "description": "Recorded state transition with trigger, actor, reason and timestamps.",
                "value_kind": "object",
                "cardinality": "0..n",
                "required": false,
                "source_refs": [
                  "SRC-003",
                  "SRC-007"
                ]
              },
              {
                "id": "de-reversal-of-event-ref",
                "name": "reversal_of_event_ref",
                "description": "Reference from a corrective transition to the erroneous transition it reverses.",
                "value_kind": "reference",
                "cardinality": "0..1",
                "required": false,
                "source_refs": [
                  "SRC-007"
                ]
              }
            ],
            "artifacts": [
              {
                "id": "assignment-event-log",
                "name": "Assignment event log",
                "description": "Append-only log of every lifecycle transition, authority change, access provisioning action and record read or export relating to an assignment, with actor, role, trigger, event time and record time.",
                "media_or_form": [
                  "append-only log",
                  "structured record stream"
                ],
                "serial": true,
                "identity_strategy": "Monotonic sequence per assignment_id; each entry carries an event identifier, event time and record time in RFC 3339 form and is never mutated in place.",
                "source_refs": [
                  "SRC-003",
                  "SRC-007",
                  "SRC-009"
                ]
              }
            ],
            "inline_only_rationale": null
          }
        },
        {
          "bundle": {
            "id": "assignment-lifecycle-and-change",
            "name": "Assignment Lifecycle and Change",
            "description": "How an assignment moves from proposal to end: its states, the events and approvals that move it, how material changes are made and notified, and what must be handed over and revoked when it ends or transfers."
          },
          "layer": {
            "id": "change-handover-and-exit",
            "name": "Change, Handover and Exit",
            "description": "Material change to a live assignment and the controlled exit from it."
          },
          "finding": {
            "id": "amendment-and-material-change",
            "name": "Amendment and material change",
            "description": "Which changes may be absorbed as amendments, which require a new record, which are material enough to require written notification within a deadline, and what consent or consultation must precede them.",
            "source_refs": [
              "SRC-010",
              "SRC-009"
            ],
            "questions": [
              {
                "id": "q-change-material",
                "text": "Which changes to this assignment are material enough to require a written statement of change to the assignee, and by what deadline?",
                "kind": "requirement",
                "answer_data": [
                  "Material change classification",
                  "Notification deadline",
                  "Statement reference"
                ]
              },
              {
                "id": "q-change-newrecord",
                "text": "Which changes create a new assignment record rather than amend the existing one, and why?",
                "kind": "constraint",
                "answer_data": [
                  "New-record trigger list",
                  "Decision taken",
                  "Link to superseded record"
                ]
              },
              {
                "id": "q-change-dating",
                "text": "How is the effective date of each amendment recorded relative to the date the assignee was notified?",
                "kind": "temporal",
                "answer_data": [
                  "Amendment effective timestamp",
                  "Notification timestamp",
                  "Gap justification where notification is later"
                ]
              },
              {
                "id": "q-change-consent",
                "text": "What consent, consultation or representative involvement is required before the change takes effect, and was it obtained?",
                "kind": "authority",
                "answer_data": [
                  "Consent requirement",
                  "Consent or consultation evidence",
                  "Outcome if refused"
                ]
              }
            ],
            "data_elements": [
              {
                "id": "de-amendment-record",
                "name": "amendment_record",
                "description": "A single recorded change to the assignment with field, prior value, new value, effective time and reason.",
                "value_kind": "object",
                "cardinality": "0..n",
                "required": false,
                "source_refs": [
                  "SRC-010"
                ]
              },
              {
                "id": "de-material-change-flag",
                "name": "material_change_flag",
                "description": "Whether the amendment is material and therefore triggers notification duties.",
                "value_kind": "boolean",
                "cardinality": "0..1",
                "required": false,
                "source_refs": [
                  "SRC-010"
                ]
              },
              {
                "id": "de-notified-at",
                "name": "change_notified_at",
                "description": "Instant the assignee was given written notice of the change.",
                "value_kind": "timestamp",
                "cardinality": "0..1",
                "required": false,
                "source_refs": [
                  "SRC-010",
                  "SRC-008"
                ]
              }
            ],
            "artifacts": [
              {
                "id": "change-to-particulars-statement",
                "name": "Statement of change to particulars",
                "description": "Written statement issued to the assignee recording a change to the particulars of the assignment, its effective date and the date it was given, satisfying statutory notification duties where they apply.",
                "media_or_form": [
                  "issued written statement",
                  "structured record",
                  "rendered document in any presentation format"
                ],
                "serial": true,
                "identity_strategy": "Sequential statement number per engagement, referencing the assignment_id and the amendment_record entries it covers.",
                "source_refs": [
                  "SRC-010"
                ]
              }
            ],
            "inline_only_rationale": null
          }
        }
      ],
      "functions": [
        {
          "id": "propose-assignment",
          "name": "Propose assignment",
          "description": "Create a candidate assignment binding an agent, an organization, a role or post, a scope and a period, without conferring any authority.",
          "inputs": [
            "Assignee agent reference",
            "Organization or unit reference",
            "Post or role reference",
            "Proposed effective period",
            "Work scope statement",
            "Proposed allocation"
          ],
          "outputs": [
            "Assignment record in proposed state",
            "Assignment identifier",
            "Initial validation report"
          ],
          "preconditions": [
            "Referenced agent, organization and post resolve to existing records",
            "Proposer holds an assignment permitting proposal for the target unit"
          ],
          "effects": [
            "A new assignment record exists in a non-authoritative proposed state",
            "A creation event is appended to the assignment event log",
            "No access rights or authorities are provisioned"
          ],
          "source_refs": [
            "SRC-001",
            "SRC-003"
          ]
        },
        {
          "id": "validate-assignment-eligibility",
          "name": "Validate assignment eligibility",
          "description": "Evaluate all prerequisite and constraint rules for a candidate or live assignment and classify each outcome as pass, warning or block.",
          "inputs": [
            "Assignment identifier",
            "Rule set version",
            "Evaluation instant"
          ],
          "outputs": [
            "Per-rule validation outcomes with severity",
            "Blocking issue list",
            "Required exception list"
          ],
          "preconditions": [
            "Prerequisite references and credential statuses are resolvable",
            "Separation, cardinality and coverage rules are published and versioned"
          ],
          "effects": [
            "Validation outcomes are recorded against the assignment with the rule set version",
            "Blocking outcomes prevent activation until resolved or excepted"
          ],
          "source_refs": [
            "SRC-004",
            "SRC-009",
            "SRC-006"
          ]
        },
        {
          "id": "authorize-assignment",
          "name": "Authorize assignment",
          "description": "Record a competent authorization decision for a validated assignment, together with its basis and any conditions.",
          "inputs": [
            "Assignment identifier",
            "Authorizing agent reference",
            "Authorization basis references",
            "Decision and conditions"
          ],
          "outputs": [
            "Approval record",
            "Authorized assignment state",
            "Authorizer competence check outcome"
          ],
          "preconditions": [
            "No unresolved blocking validation outcome",
            "Authorizing agent holds a current assignment conferring authority at the required level and scope"
          ],
          "effects": [
            "An immutable approval record is created with a point-in-time snapshot of the authorizer's role",
            "The assignment moves to an authorized state and becomes eligible for activation"
          ],
          "source_refs": [
            "SRC-007",
            "SRC-004"
          ]
        },
        {
          "id": "activate-assignment",
          "name": "Activate assignment",
          "description": "Bring an authorized assignment into force at its effective start, conferring the recorded authority and triggering downstream provisioning.",
          "inputs": [
            "Assignment identifier",
            "Activation instant",
            "Acknowledgement status where required"
          ],
          "outputs": [
            "Active assignment state",
            "Provisioning instructions for downstream consumers",
            "Activation event entry"
          ],
          "preconditions": [
            "Assignment is authorized and the effective start has been reached or is being set",
            "Any acknowledgement precondition is satisfied",
            "Prerequisite credentials are valid at the activation instant"
          ],
          "effects": [
            "The assignment becomes exercisable and appears in effective-assignment queries",
            "Downstream provisioning is requested and reconciliation is scheduled"
          ],
          "source_refs": [
            "SRC-003",
            "SRC-004",
            "SRC-002"
          ]
        },
        {
          "id": "amend-assignment",
          "name": "Amend assignment",
          "description": "Apply an effective-dated change to a live assignment, classify its materiality and trigger any notification duty.",
          "inputs": [
            "Assignment identifier",
            "Changed fields with new values",
            "Amendment effective instant",
            "Reason"
          ],
          "outputs": [
            "Amendment record",
            "Materiality classification",
            "Notification obligation with deadline"
          ],
          "preconditions": [
            "Change does not fall within the new-record trigger set",
            "Actor holds authority to amend the assignment"
          ],
          "effects": [
            "Prior values are preserved and the amendment is effective-dated",
            "A statement of change is required where the amendment is material",
            "Re-validation is triggered for affected rules"
          ],
          "source_refs": [
            "SRC-010",
            "SRC-004"
          ]
        },
        {
          "id": "suspend-or-resume-assignment",
          "name": "Suspend or resume assignment",
          "description": "Temporarily render an assignment non-exercisable, or restore it, without ending it.",
          "inputs": [
            "Assignment identifier",
            "Suspend or resume action",
            "Reason code",
            "Effective instant"
          ],
          "outputs": [
            "Updated assignment state",
            "Authority suspension or restoration instructions",
            "Event entry"
          ],
          "preconditions": [
            "Assignment is currently active or suspended as appropriate",
            "Actor holds authority to suspend or resume"
          ],
          "effects": [
            "Conferred authorities become non-exercisable on suspension and are restored on resume",
            "The effective period is unchanged and the assignment remains counted as existing"
          ],
          "source_refs": [
            "SRC-003",
            "SRC-004"
          ]
        },
        {
          "id": "delegate-assignment-authority",
          "name": "Delegate assignment authority",
          "description": "Record that another agent acts on behalf of the assignee for named authorities over a bounded period.",
          "inputs": [
            "Assignment identifier",
            "Delegate agent reference",
            "Delegated authority items",
            "Delegation period"
          ],
          "outputs": [
            "Delegation instrument",
            "Updated exercisable-authority view",
            "Accountability statement"
          ],
          "preconditions": [
            "Delegation is permitted for this assignment and for each named authority",
            "Delegate passes separation of duty and eligibility checks"
          ],
          "effects": [
            "The delegate may exercise the named authorities within the period",
            "Accountability remains with the assignee unless the instrument states transfer",
            "The delegation lapses automatically at period end or on suspension of the assignment"
          ],
          "source_refs": [
            "SRC-007",
            "SRC-003",
            "SRC-004"
          ]
        },
        {
          "id": "transfer-or-succeed-assignment",
          "name": "Transfer or succeed assignment",
          "description": "End one assignment and start another for the same post or scope with an explicit succession link and a coverage decision for any interval.",
          "inputs": [
            "Outgoing assignment identifier",
            "Incoming assignee reference",
            "Boundary instant",
            "Coverage arrangement"
          ],
          "outputs": [
            "Ended outgoing assignment",
            "New incoming assignment",
            "Succession link and coverage record"
          ],
          "preconditions": [
            "Boundary convention for inclusive or exclusive end is defined",
            "Incoming assignment passes eligibility validation"
          ],
          "effects": [
            "Predecessor and successor references are recorded on both assignments",
            "Existing authorizations are reviewed and either re-confirmed or removed",
            "Headcount and coverage measures are computed without double counting"
          ],
          "source_refs": [
            "SRC-001",
            "SRC-004"
          ]
        },
        {
          "id": "end-assignment",
          "name": "End assignment and offboard",
          "description": "Close an assignment at its effective end and drive handover, revocation and evidence capture.",
          "inputs": [
            "Assignment identifier",
            "Effective end instant",
            "End reason code"
          ],
          "outputs": [
            "Ended assignment state",
            "Handover and offboarding record",
            "Revocation task set with deadlines"
          ],
          "preconditions": [
            "Actor holds authority to end the assignment or the end is an automatic consequence of the effective end"
          ],
          "effects": [
            "All conferred authorities and delegations lapse",
            "Access revocation or reassignment tasks are raised and tracked to completion",
            "Retention clocks start for the record and its evidence classes"
          ],
          "source_refs": [
            "SRC-004",
            "SRC-003",
            "SRC-009"
          ]
        },
        {
          "id": "resolve-effective-assignments",
          "name": "Resolve effective assignments as of an instant",
          "description": "Return the set of assignments in force for an agent, post or unit at a given instant, using stored state and effective periods with a declared precedence rule.",
          "inputs": [
            "Query subject reference",
            "Evaluation instant in RFC 3339 form",
            "Requested access scope"
          ],
          "outputs": [
            "Effective assignment set with roles, scopes and authorities",
            "Precedence and conflict notes",
            "Redaction applied for the requester's scope"
          ],
          "preconditions": [
            "Effective periods carry explicit offsets",
            "Status derivation precedence is defined"
          ],
          "effects": [
            "A point-in-time answer is produced without mutating any record",
            "The read is recorded in the audit log with actor, scope and instant"
          ],
          "source_refs": [
            "SRC-008",
            "SRC-001",
            "SRC-002"
          ]
        },
        {
          "id": "detect-assignment-conflicts",
          "name": "Detect assignment conflicts",
          "description": "Scan the assignment population for separation of duty breaches, cardinality and coverage violations, capacity over-allocation, overlaps and expired prerequisites.",
          "inputs": [
            "Scope of scan",
            "Rule set version",
            "Evaluation window"
          ],
          "outputs": [
            "Conflict findings with severity and affected assignments",
            "Coverage gap list",
            "Expiring prerequisite list"
          ],
          "preconditions": [
            "Rules are published with a version identifier",
            "Concurrent assignments and allocations are resolvable for each agent"
          ],
          "effects": [
            "Findings are recorded with the rule set version so historic results remain explicable",
            "Findings above threshold raise remediation tasks with owners and due dates"
          ],
          "source_refs": [
            "SRC-004",
            "SRC-001"
          ]
        },
        {
          "id": "project-assignment-to-consumer",
          "name": "Project assignment to a downstream consumer",
          "description": "Emit a consumer-specific representation of the assignment under a published crosswalk and reconcile the consumer's state against this model.",
          "inputs": [
            "Assignment identifier",
            "Target consumer or standard identifier",
            "Crosswalk version"
          ],
          "outputs": [
            "Consumer-shaped representation",
            "Known-loss and conflict caveats",
            "Reconciliation difference report"
          ],
          "preconditions": [
            "A published crosswalk exists for the target at the stated version",
            "Access scope permits disclosure of the projected fields to that consumer"
          ],
          "effects": [
            "The consumer receives a representation with explicit caveats rather than a silently lossy copy",
            "Differences found on reconciliation are recorded rather than auto-overwritten"
          ],
          "source_refs": [
            "SRC-002",
            "SRC-005",
            "SRC-011",
            "SRC-013"
          ]
        },
        {
          "id": "establish-temporary-or-time-limited-assignment",
          "name": "Establish detail or time-limited promotion",
          "description": "Create a time-bounded higher-grade or other temporary occupancy with notice of return terms and 120-day competition accounting.",
          "inputs": [
            "home assignment identifier",
            "temporary post or role",
            "time limit",
            "accrued noncompetitive days",
            "written notice"
          ],
          "outputs": [
            "temporary assignment identifier",
            "return position reference",
            "competition-required flag"
          ],
          "preconditions": [
            "Advance written notice is given, or a nondiscretionary promotion records notice as soon as possible.",
            "Time limit does not exceed five years unless a higher authorization exists."
          ],
          "effects": [
            "A temporary occupancy exists alongside or instead of the home occupancy as locally modelled.",
            "Return to the former or equivalent position remains available as specified in the notice."
          ],
          "source_refs": [
            "SRC-017"
          ]
        }
      ],
      "composition": [
        {
          "target": "WM-ORG-004 Position",
          "relation": "REFERENCE",
          "purpose": "The assignment cites the post it occupies; the post's definition, grading and description remain owned by WM-ORG-004. Direction: WM-ORG-016 points outward to WM-ORG-004, complementing the registered COMPOSE relation in which a position is occupied through a scoped assignment.",
          "required": false,
          "source_refs": [
            "SRC-001"
          ]
        },
        {
          "target": "WM-ORG-005 Employment Relationship",
          "relation": "REFERENCE",
          "purpose": "The assignment cites the engagement that gives it a basis. Marked not required because agency-supplied, contracted and volunteer assignments rest on a commercial or non-employment arrangement instead; what is required is some engagement context, not specifically an employment relationship.",
          "required": false,
          "source_refs": [
            "SRC-014",
            "SRC-010"
          ]
        },
        {
          "target": "Person, party and agent identity model",
          "relation": "REFERENCE",
          "purpose": "Supplies the assignee identity, including non-human agents. This model holds only a reference and never duplicates personal master data.",
          "required": true,
          "source_refs": [
            "SRC-001",
            "SRC-007"
          ]
        },
        {
          "target": "Organization and organizational unit model",
          "relation": "REFERENCE",
          "purpose": "Supplies the organization or unit in which the assignment is held and, where different, the host organization where the work is performed.",
          "required": true,
          "source_refs": [
            "SRC-001",
            "SRC-014"
          ]
        },
        {
          "target": "Role, occupation and competence classifier model",
          "relation": "REFERENCE",
          "purpose": "Supplies role concepts, occupation codes and the competences that become assignment prerequisites; the classifier owns the concepts, the assignment owns the citation.",
          "required": false,
          "source_refs": [
            "SRC-006",
            "SRC-001"
          ]
        },
        {
          "target": "Schedule, roster and availability model",
          "relation": "COMPOSE",
          "purpose": "Concrete dated duty and shift instances are composed from the assignment's pattern, availability and limits, and reference the assignment identifier.",
          "required": false,
          "source_refs": [
            "SRC-011",
            "SRC-002"
          ]
        },
        {
          "target": "Access entitlement and identity management model",
          "relation": "REFERENCE",
          "purpose": "Consumes the assignment as the temporal and organizational basis for user-to-role assignment, activation and de-provisioning; the permission catalogue and decision engine stay outside this model.",
          "required": false,
          "source_refs": [
            "SRC-004"
          ]
        },
        {
          "target": "Place and work location model",
          "relation": "REFERENCE",
          "purpose": "Supplies base and additional work locations from which jurisdictional, safety and working-time regimes are derived.",
          "required": false,
          "source_refs": [
            "SRC-002",
            "SRC-010"
          ]
        },
        {
          "target": "W3C Organization Ontology (org:Membership, org:Post, org:Role)",
          "relation": "ALIGN",
          "purpose": "Primary structural alignment for the reified n-ary agent-organization-role relation with a validity interval. Known divergence: org:memberDuring leaves its range unconstrained, so this model imposes RFC 3339 instants.",
          "required": false,
          "source_refs": [
            "SRC-001",
            "SRC-008"
          ]
        },
        {
          "target": "HL7 FHIR PractitionerRole",
          "relation": "ALIGN",
          "purpose": "Domain alignment showing role code, specialty, organization, location, service scope, period and availability carried on the assignment. Known divergence: FHIR conflates post and membership into one resource and has no separation-of-duty or authority constructs.",
          "required": false,
          "source_refs": [
            "SRC-002"
          ]
        },
        {
          "target": "schema.org Role and OrganizationRole",
          "relation": "ALIGN",
          "purpose": "Publication alignment for lightweight external exposure. Known divergence: no lifecycle status, no authority, and date-only validity, so it is an export target only and never a semantic source.",
          "required": false,
          "source_refs": [
            "SRC-005"
          ]
        },
        {
          "target": "HR Open Standards StaffingAssignment (Contingent Staffing 3.3)",
          "relation": "ALIGN",
          "purpose": "Alignment for the tri-party case in which a resource engaged by one organization is placed with a customer. Known divergence: the consortium's newer JSON API set has no Assignment resource, so no stable modern JSON counterpart exists.",
          "required": false,
          "source_refs": [
            "SRC-014",
            "SRC-013"
          ]
        },
        {
          "target": "W3C PROV-O qualified association and delegation",
          "relation": "MIX-IN",
          "purpose": "Provenance mixin for authorization, acting-on-behalf-of delegation and role-at-time-of-action, applied to approval records and lifecycle events.",
          "required": false,
          "source_refs": [
            "SRC-007"
          ]
        },
        {
          "target": "NIST/INCITS RBAC constraint model",
          "relation": "ALIGN",
          "purpose": "Alignment for static and dynamic separation of duty and cardinality constraints. Known divergence: standard RBAC user assignment carries no temporal bounds, so the temporal semantics are supplied by this model and must not be assumed on the RBAC side.",
          "required": false,
          "source_refs": [
            "SRC-004"
          ]
        },
        {
          "target": "RFC 3339 timestamp profile",
          "relation": "ALIGN",
          "purpose": "Governs every effective, transition, authorization, notification and observation time in the model, including the reserved meaning of an unknown local offset.",
          "required": true,
          "source_refs": [
            "SRC-008"
          ]
        }
      ],
      "researchAdjudication": {
        "providerMode": "dual-provider",
        "activeProviders": [
          "claude",
          "grok"
        ],
        "waivedProviders": [],
        "providerPolicy": {},
        "boundaryDecision": {
          "entry_kind": "relationship",
          "status": "accepted",
          "rationale": "Both providers independently classify WM-ORG-016 as a reified n-ary relationship rather than an entity, and both derive that from the same primary pattern: W3C ORG separates org:Post (which exists independently of any holder) from org:Membership (which exists only while an agent occupies a role), and FHIR PractitionerRole carries a period of authorization rather than a standing post definition. The base boundary is adopted whole: the assignment is the time-bounded occupancy binding agent, organization or unit, role or post, bounded scope and validity period, holding no position definition (WM-ORG-004), no engagement or contract terms (WM-ORG-005), no person or org master data, no task-instance ownership state and no permission catalogue. Grok's two extra exclusions (FHIR CareTeam patient-scoped membership and ISA-95/IEC 62264 personnel-resource binding to a work definition) are consistent with that boundary and sharpen it rather than move it, so they are carried as boundary-note refinements in a later pass, not as a boundary change."
        },
        "decisions": [
          {
            "concept": "Base provider selection",
            "disposition": "Claude adopted as base",
            "rationale": "Not chosen on size. Claude states explicit in-scope and out-of-scope lists plus eight neighbour boundary notes each carrying source refs, and each of the eight is a distinction the model actually needs (post, engagement, classifier, task instance, RBAC, roster, timecard, incident tasking). Its bundle spine also separates scope/authority from time/schedule from lifecycle from controls, which the merged additions can attach to without new scaffolding. Grok's boundary is sound but its decomposition splits parties and location into standalone bundles that the base already covers inside scope-and-authority."
          },
          {
            "concept": "Entry kind",
            "disposition": "Accepted as relationship",
            "rationale": "Independent agreement between providers, both derived from the same primary separation of org:Post from org:Membership and from FHIR PractitionerRole carrying an authorization period. No adjudication needed and no reclassification risk."
          },
          {
            "concept": "Unnamed, pre-allocated and ex officio occupancy",
            "disposition": "Accepted as addition to assignee-agent-kind",
            "rationale": "Materially absent from the base participant set and evidenced directly in FHIR (practitioner 0..1, un-named practitioner at a named organization) and in W3C ORG ex officio membership. Without it, locum slots, job-share halves and ex officio seats cannot be represented at all."
          },
          {
            "concept": "Role-scoped contact, service and endpoint projection",
            "disposition": "Accepted narrowly, spatial questions dropped",
            "rationale": "Only the increment absent from the base is taken: contact points, languages and endpoints belonging to the occupancy rather than the person, plus the FHIR instance-split rule. Base coverage of base location, mobility, jurisdiction, objectives and caseload is retained unchanged, so the overlapping questions are discarded rather than duplicated."
          },
          {
            "concept": "Governed personnel-action typology and status invariance",
            "disposition": "Accepted as addition, jurisdiction-labelled",
            "rationale": "The base has an abstract state machine but no act typology and no rule that a position change leaves tenure and competitive status unchanged. Grok retrieved primary regulatory text for both. Accepted on condition it publishes as a concrete instance of personnel-action semantics under a named appointing regime, never as the universal set."
          },
          {
            "concept": "Temporary, detail and time-limited forms",
            "disposition": "Accepted as addition, jurisdiction-labelled",
            "rationale": "Term ceilings, advance notice of return terms, the right of return to the former or equivalent position, cumulative noncompetitive accounting and conversion to permanent are all absent from the base and all evidenced from retrieved primary text. Grok's own caveat that 'acting' is operational language not present in the cited regulation is carried through so no false label is asserted."
          },
          {
            "concept": "Host organization as separate finding",
            "disposition": "Rejected as duplicative",
            "rationale": "The base participant question already asks whether the assignee is engaged by a different organization from the one where work is performed, and the boundary note on WM-ORG-005 already states that host need not be employer. The only residue is the seconding home-employer-of-record pointer, which is a reference into a sibling model rather than a new node."
          },
          {
            "concept": "Occupied post or role as separate finding",
            "disposition": "Rejected as duplicative",
            "rationale": "The base asks whether the assignment is expressed against a defined post, an abstract role concept or a bespoke scope with no post at all, which is exactly Grok's Membership-versus-Post pattern decision, and the base role-and-position-linkage finding carries the classifier and reclassification questions Grok lacks."
          },
          {
            "concept": "Occupancy and authorization period as separate finding",
            "disposition": "Rejected as duplicative; one residue deferred",
            "rationale": "The base effective-period finding already covers period and precision, RFC 3339 offsets, event versus record time, backdating, concurrency, succession and same-day transfer. The residue worth keeping is the third clock (planned versus actual start and end, distinct from effective versus record time); it is deferred as a question-level refinement to the existing base finding rather than a new node."
          },
          {
            "concept": "Evidence and provenance as separate finding",
            "disposition": "Rejected as duplicative; integrity residue deferred",
            "rationale": "Base coverage of authorization provenance, approval-chain durability, record correction versus real-world change, reversal with audit preservation and the append-only assignment event log already spans PROV-O generation, association, attribution and invalidation. The genuine residue is evidence-artifact integrity hashing and an explicit record-quality claim, which is deferred rather than published as a competing finding."
          },
          {
            "concept": "Interoperability alignments as separate finding",
            "disposition": "Rejected; neighbour notes deferred",
            "rationale": "The base standard-alignment finding is strictly richer, adding versioned crosswalks, unmapped-field disclosure, identifier precedence, downstream reconciliation and visible conflict recording. Grok's distinct contribution is two neighbours the base does not name, FHIR CareTeam and ISA-95/IEC 62264 personnel resources, which belong in a boundary-note pass, not in the finding tree."
          },
          {
            "concept": "Privacy, retention and erasure as separate finding",
            "disposition": "Rejected as structure; evidence retained as corroboration only",
            "rationale": "The base already carries personal-data classification and access scoping plus retention, deletion and legal hold as two findings whose question sets subsume Grok's. Grok's Article 88 and ICO material is corroborating evidence attached to the existing base retention finding, not a new node, and because one of those sources is a non-primary mirror and the other is tier 2, it does not close the base's declared retention gap."
          },
          {
            "concept": "Grok classification, lifecycle-state, assigning-authority and separation-of-duty findings",
            "disposition": "Rejected as duplicative",
            "rationale": "Each maps onto a strictly broader base finding: assignment type and primacy, the state model with stored-versus-derived status, granted authority with grantor competence, and the separation-of-duty, cardinality, coverage and exception finding. The only non-overlapping elements (ex officio, competition thresholds) arrive through the two accepted additions instead."
          },
          {
            "concept": "Non-human agent as assignee",
            "disposition": "Retained with explicit gap label",
            "rationale": "The providers disagree in emphasis rather than in fact: the base structures non-human occupancy with a natural-person reservation and oversight link, while Grok records that no retrieved HR or personnel standard supports a software agent occupying a work assignment. The cited AI Act article obliges deployers to assign oversight to competent natural persons; it does not authorize non-human occupancy. The structure is kept as a constraint-bearing branch and must publish carrying that unsupported-claim label."
          },
          {
            "concept": "Claude-only scope/authority and time/schedule bundles",
            "disposition": "Retained in full",
            "rationale": "Working pattern and predictability, duty and rest limits, eligibility and screening preconditions, handover and offboarding, and acknowledgement and notification duties have no Grok counterpart and are each source-backed in the base. Absence from the second provider is not evidence against them."
          }
        ],
        "publicationHolds": [
          "Source and live-version verification is not discharged. Every accepted source must be refetched and pinned before publication, with particular attention to the two divergent FHIR PractitionerRole citations across providers (hl7.org/fhir/R5/practitionerrole.html described as R5 Maturity 4 Trial Use versus www.hl7.org/fhir/practitionerrole.html described as R5 5.0.0 generated 26 March 2023), and to the moving pins on ESCO v1.2.1, schema.org v30.0, the eCFR currency date and the revised-text-in-force date for the UK written-particulars section.",
          "Multi-profile domain validation is not discharged. The merged structure has been exercised against healthcare (FHIR PractitionerRole), US federal public service (5 CFR 335), contingent staffing (HR-XML 3.3) and incident management (ICS forms), but must additionally be validated against at least one non-US, non-EU appointing regime and one volunteer or platform-work profile before publication, because the accepted personnel-action and temporary-form nodes are otherwise parochial.",
          "Retention remains a declared gap and must publish as a policy hook with a mandatory declared basis, never as a substantive period. Grok's retention evidence rests on a non-primary mirror of the GDPR employment-context article and on tier-2 regulator guidance; neither establishes a general retention period for assignment records, and the base's own attempts to retrieve primary retention instruments returned HTTP 403.",
          "Workforce measurement remains a declared gap. Effort fraction, full-time-equivalent semantics, headcount boundary conventions and coverage metrics are structured but normatively ungrounded in both providers; they must publish as required declarations by the adopting Dimension, not as canonical definitions.",
          "All nodes derived from a single national personnel code or a single national statute (the accepted personnel-action and time-limited-form findings, and the written-particulars duties in the base) must carry an explicit jurisdiction scope label before publication, and the 'acting' terminology must not be attributed to any cited regulation.",
          "The non-human-agent occupancy branch must publish with an explicit note that no retrieved HR or personnel standard supports a software or robotic agent occupying a work assignment, and that the cited AI Act obligation governs assignment of human oversight rather than authorizing non-human occupancy."
        ],
        "deferredResearch": [
          "Retrieve primary retention instruments (statutory limitation periods, tax and social-security record-keeping duties, and the regulator guidance in its original published form) to convert the retention dimension from a declared gap into evidence-backed minimum periods; both providers failed to reach primary text on this dimension.",
          "Retrieve an open or licensed normative definition of full-time-equivalent, effort fraction, headcount boundary and coverage metrics (ISO 30414 and ISO 30400 were paywalled or returned HTTP 403 for both providers) so that workforce measurement can stop publishing as an undefined declaration.",
          "Retrieve the EU transparent and predictable working conditions directive text from EUR-Lex to generalize the written-particulars and unpredictable-pattern duties beyond the single national statute currently relied upon, and to resolve whether particulars attach per engagement or per assignment.",
          "Retrieve HR Open Standards position and assignment JSON schemas and the IEC 62264-1 personnel object model text to firm up the interoperability crosswalk and to convert the ISA-95 boundary from an overview-page claim into a sourced neighbour note.",
          "Retrieve at least two non-US national personnel-action regimes and one collective-agreement-governed regime so the accepted personnel-action typology and time-limited-form constraints can be generalized or explicitly partitioned by jurisdiction.",
          "Machine-parse the incident-management assignment-list forms and retrieve the ILO employment-relationship recommendation full instrument text; both were cited from landing pages or unparsed PDFs and currently support only form identity and stated purpose.",
          "Resolve the two deferred residues from rejected Grok findings: the planned-versus-actual clock as a third temporal axis distinct from effective-versus-record time, and evidence-artifact integrity hashing plus an explicit record-quality claim on the assignment record."
        ]
      }
    }
  }
}

```

