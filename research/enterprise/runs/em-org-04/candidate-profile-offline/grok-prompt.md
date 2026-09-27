# Independent review request: EM-ORG-04 Organizational Unit and Mandate

Review this Enterprise boundary independently using public organization-ontology, matrix-organization, delegation and temporal graph practice where useful. Separate standards evidence from design inference. Do not invent a Vercy identifier.

WM-ORG-002 is an existing non-canonical reviewable draft covering unit identity, concurrent hierarchies, mandate, reorganization and bitemporal history.

Proposed decision: **PROFILE**, no new ID. OrganizationalUnit retains stable identity independent of name, mandate and placement. UnitType is classification; UnitMandate is a temporal assignment; StructuralPlacement is a reified edge keyed by child, parent, axis, scenario and interval.

Administrative, functional, legal, cost and reporting axes coexist. The unqualified unit-level parent field must not be a second write path. Asserted current, historical, approved future and hypothetical scenario are distinct. Hypothetical structures require an explicit branch and remain excluded from authoritative reads.

Rules to challenge: single parent only within tree-like axis/scenario/time; acyclicity per axis/scenario/interval; rename/reparent preserve ID; merge/split/disband require lineage and act; management parent never determines employer/legal entity; collaboration/team cannot receive administrative placement; mandate is placement-independent.

Negative case: a cross-department product team is forced under one administrative parent. Acceptance: an as-is/to-be reorganization preserves old assignments and validates no cycle in the selected axis without contaminating current state.

Return at most 1000 words with: Verdict; identity test; mandate boundary; placement key/cardinality; scenario model; team/unit distinction; temporal and lineage rules; scenario results; required profile constraints; publication blockers.
