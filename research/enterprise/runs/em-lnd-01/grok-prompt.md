# Independent review request: EM-LND-01 Organizational Structure Landscape

Review this Enterprise boundary independently. Use public organization-modelling and architecture-view practice where useful. Distinguish source facts from design inference. Do not invent a Vercy identifier.

Sources:

- WM-ORG-002 masters organizational units, concurrent hierarchies, reporting lines, reorganization acts, lineage and bitemporal reconstruction.
- WM-ORG-003 masters teams, membership assignments, nesting and structural changes.
- WM-ORG-004 masters positions and position reporting/placement history.
- WM-ORG-016 masters time-bounded work assignments and assignment-level supervision.
- All four are published reviewable drafts with publication holds.

Proposed decision: **PROFILE**, no new ID. OrganizationLandscape is a deterministic projection. StructureAxis is a governed profile construct. StructureSnapshot is an immutable digest-identified generated artifact, not a second source of truth.

Axes:

- Administrative: unit containment, one parent per interval, acyclic.
- Functional: unit/post reporting, multiple declared edges, profile-specific hierarchy rules.
- Project: agent-team membership plus separate team nesting; membership is not a hierarchy.
- Supervisory: assignment/post/agent reporting, one effective supervisor per assignment and axis after precedence.

Every view applies one world-time/record-time pair to all sources, pins constituent versions and digests, references master objects without copying them, and is refused when a source cannot reconstruct the requested horizon. Scenario is unsupported and must remain `authoritative` until a planning extension exists.

Test:

1. A matrix assignment appears to violate a global one-manager rule.
2. Administrative, project and supervisory views include two assignments and a future reorganization.
3. A cycle exists across the union of two axes but not within either axis.
4. One source has a shorter reconstruction horizon.

Return at most 1000 words with: Verdict; identity/lifecycle test for Landscape, Axis and Snapshot; axis rules; time/snapshot contract; scenario treatment; scenario results; publication blockers.
