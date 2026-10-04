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
