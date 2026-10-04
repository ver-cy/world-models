# Frozen no-tools semantic audit — EM-FAC-01

You are the final static semantic auditor. Use only this frozen packet. Do not browse, call tools, invent identifiers, mutate registry reservations or grant publication authority.

Disposition: composed boundary. Complete reserved WM-BLT-002; propose retirement of duplicate WM-PLC-009; profile office use and indoor topology; retain Workplace Allocation as an identifier-unassigned NEW MODEL candidate. Audit semantics only.

Audit questions:
- Is the Place/Site/Facility/Building/Premises path correctly expressed as references and optional containment layers?
- Does WM-BLT-002 preserve physical identity through address, use, occupancy, re-parenting, split and merge events?
- Is WM-PLC-009 retirement safe without erasing indoor topology/navigation semantics?
- Does Workplace Allocation prove independent identity while keeping employment, premises, lease, access, booking, establishment and branch lifecycles external?
- Do home, client-site, mobile and pooled-work cases fail closed on privacy and authority?
- Which holds permit reviewable drafts but block allocation or canonical publication?

Return at most 600 words with exactly: Verdict (ACCEPT WITH LIMITS, REVISE, or REJECT); Critical findings; Required holds; Scenario result; Identifier decisions. Registry mutation and identifier allocation remain holds.

## WM-BLT-002 candidate

{
  "format": "vercy-world-model-candidate/v1",
  "contourId": "EM-FAC-01",
  "modelId": "WM-BLT-002",
  "registryId": "vr.wm-blt-002",
  "name": "Premises / Spatial Unit",
  "version": "0.3.0-candidate.2",
  "entryKind": "spatial-aggregate",
  "status": "research-candidate",
  "canonicalPublishable": false,
  "purpose": "Represent persistent bounded interior spatial-unit identity, temporal containment, geometry and area evidence, use designations and split/merge lineage without deriving identity from address, room number, occupier or office use.",
  "boundary": {
    "owns": [
      "persistent premises or spatial-unit identity",
      "effective-dated parent containment and recursive subdivision",
      "spatial-unit kind designator and separately governed status",
      "geometry references and versioned boundary evidence",
      "measured area evidence and design capacity",
      "effective-dated use designations including office",
      "split and merge lineage with predecessor and successor units"
    ],
    "delegates": [
      "building shell identity to WM-BLT-001",
      "facility and site identity to their respective masters",
      "gazetteer place and generalized location references to WM-PLC-010",
      "physical-item identity and movable contents to WM-OBJ-001",
      "address and sub-address identity to address/location masters",
      "lease ownership access booking employment and workplace allocation to external masters",
      "party identity and occupancy authority to person and organization masters"
    ],
    "excludes": [
      "office as a new physical identity",
      "legal branch creation",
      "home address publication",
      "desk reservation or access grant",
      "employment or workplace allocation lifecycle",
      "physical-item composition ownership"
    ],
    "preferredReferencePath": "Gazetteer Place locates Site; Site may contain Facility; Facility may contain Building; Building contains Premises. The path is not mandatory exclusive containment."
  },
  "objects": {
    "SpatialUnit": {
      "identity": [
        "spatialUnitId"
      ],
      "required": [
        "unitKind",
        "parentRef",
        "validFrom",
        "governanceAuthorityRef",
        "status"
      ],
      "optional": [
        "designator",
        "validTo",
        "geometryRef",
        "designCapacity",
        "separatelyGoverned",
        "retirementReason"
      ],
      "lifecycle": [
        "planned",
        "delineated",
        "active",
        "restricted",
        "retired"
      ]
    },
    "ContainmentAssertion": {
      "identity": [
        "containmentId"
      ],
      "required": [
        "childSpatialUnitRef",
        "parentRef",
        "validFrom",
        "authorityRef",
        "status"
      ],
      "optional": [
        "validTo",
        "evidenceRefs",
        "supersedesContainmentId"
      ],
      "lifecycle": [
        "asserted",
        "superseded",
        "withdrawn"
      ]
    },
    "BoundaryEvidence": {
      "identity": [
        "boundaryEvidenceId"
      ],
      "required": [
        "spatialUnitRef",
        "geometryRef",
        "boundaryType",
        "effectiveFrom",
        "sourceRef",
        "method"
      ],
      "optional": [
        "effectiveTo",
        "surveyedAt",
        "supersedesEvidenceId"
      ]
    },
    "AreaMeasurement": {
      "identity": [
        "areaMeasurementId"
      ],
      "required": [
        "spatialUnitRef",
        "areaType",
        "value",
        "unit",
        "measuredAt",
        "methodRef",
        "sourceRef"
      ],
      "optional": [
        "uncertainty",
        "geometryRef",
        "supersedesMeasurementId"
      ]
    },
    "UseDesignation": {
      "identity": [
        "designationId"
      ],
      "required": [
        "spatialUnitRef",
        "useClass",
        "validFrom",
        "authorityRef",
        "status"
      ],
      "optional": [
        "validTo",
        "purpose",
        "conditions",
        "supersedesDesignationId"
      ],
      "lifecycle": [
        "proposed",
        "effective",
        "superseded",
        "withdrawn"
      ]
    },
    "SplitMergeLineage": {
      "identity": [
        "lineageEventId"
      ],
      "required": [
        "eventKind",
        "predecessorUnitRefs",
        "successorUnitRefs",
        "effectiveAt",
        "authorityRef",
        "evidenceRefs"
      ],
      "optional": [
        "reason",
        "decisionRef"
      ]
    }
  },
  "lineageEventKinds": [
    "split",
    "merge"
  ],
  "relations": [
    {
      "target": "WM-BLT-001",
      "relation": "REFERENCE",
      "required": true,
      "purpose": "Resolve the building or structure shell containing the top-level spatial unit."
    },
    {
      "target": "WM-BLT-002",
      "relation": "CONTAINS",
      "required": false,
      "purpose": "Represent recursive spatial subdivision with effective-dated containment assertions."
    },
    {
      "target": "WM-PLC-010",
      "relation": "REFERENCE",
      "required": false,
      "purpose": "Resolve generalized place and address context without using it as spatial-unit identity."
    },
    {
      "target": "WM-OBJ-001",
      "relation": "REFERENCE",
      "required": false,
      "purpose": "Locate physical item instances without owning or composing their identity."
    }
  ],
  "operations": [
    {
      "id": "delineate-unit",
      "effect": "Create a persistent spatial-unit identity with boundary evidence.",
      "authority": "spatial governance authority"
    },
    {
      "id": "reparent-unit",
      "effect": "Issue a successor containment assertion without changing unit identity.",
      "authority": "spatial governance authority"
    },
    {
      "id": "designate-use",
      "effect": "Apply an effective-dated use classification such as office.",
      "authority": "authorized use-designation authority"
    },
    {
      "id": "measure-area",
      "effect": "Append method-qualified area evidence.",
      "authority": "authorized measurer"
    },
    {
      "id": "split-unit",
      "effect": "Retire one unit into multiple successor identities with lineage.",
      "authority": "spatial governance authority"
    },
    {
      "id": "merge-units",
      "effect": "Retire multiple units into one successor identity with lineage.",
      "authority": "spatial governance authority"
    },
    {
      "id": "retire-unit",
      "effect": "End active use while preserving identity geometry and history.",
      "authority": "spatial governance authority"
    }
  ],
  "invariants": [
    "Address, room number, current occupier and use designation never define spatial-unit identity.",
    "Every top-level spatial unit resolves to one building or structure shell for each effective interval.",
    "Recursive spatial containment is acyclic for any as-of time.",
    "Re-parenting changes containment evidence and does not mint a new spatial-unit identity.",
    "Split and merge mint successor identities and preserve predecessor lineage.",
    "Geometry corrections append successor boundary evidence and never rewrite prior evidence.",
    "Area values include method, area type, unit, source and measurement time.",
    "Office is an effective-dated use designation rather than a physical object or legal branch.",
    "A use designation never grants lease occupancy access booking or employment rights.",
    "A home-work context never creates or publishes a residential premises record automatically.",
    "Physical items located in a unit retain independent identity and lifecycle.",
    "Current occupancy or control roles are referenced and never copied as unit identity.",
    "Retired units remain resolvable for historical addresses leases and evidence.",
    "Missing geometry or area evidence means unknown and never zero.",
    "Access to sensitive use or occupancy references cannot exceed the external source authority.",
    "Gazetteer Place locates a managed site by reference and never becomes its containment parent.",
    "A facility may exist without a site and a building may exist without a facility; missing intermediate containers do not change premises identity.",
    "Indoor navigation and topology are profiles over WM-BLT-002 identity and never create a parallel WM-PLC-009 master.",
    "Address replacement never changes site, building or premises identity by itself.",
    "Occupancy, capacity and workplace-allocation data are non-public by default and preserve source-authority restrictions."
  ],
  "holds": [
    "One frozen no-tools semantic audit of the provider-reconciled candidate is pending.",
    "WM-PLC-009 retirement and relation retargeting are proposals; no registry mutation is approved.",
    "Workplace Allocation is identifier-unassigned and requires formal registry allocation.",
    "IFC, IndoorGML, area-measurement and Facility/Building crosswalk conflicts require pinned-source resolution.",
    "Workplace Allocation requires data-protection and employment-law review in at least one non-US jurisdiction.",
    "Package conversion and live HTTP, runtime, search and package verification are pending."
  ],
  "duplicateDisposition": {
    "modelId": "WM-PLC-009",
    "proposal": "retire-superseded-by-WM-BLT-002",
    "profilePreserved": "Indoor Topology",
    "registryMutationApproved": false
  }
}

## WM-BLT-002 fixtures

{
  "format": "vercy-world-model-fixtures/v1",
  "modelId": "WM-BLT-002",
  "version": "0.3.0-candidate.2",
  "cases": [
    {
      "id": "leased-office",
      "kind": "positive",
      "input": "An employer leases office units in a building it does not own.",
      "expect": "Spatial units retain building containment and office designation; lease and ownership remain external."
    },
    {
      "id": "address-change",
      "kind": "positive",
      "input": "The building address changes while boundaries and authority remain stable.",
      "expect": "Site building and spatial-unit identities remain unchanged; only location references change."
    },
    {
      "id": "office-to-lab",
      "kind": "positive",
      "input": "One unit changes use from office to laboratory.",
      "expect": "Issue a successor use designation without changing spatial identity."
    },
    {
      "id": "unit-split",
      "kind": "positive",
      "input": "One floor unit is divided into three separately governed suites.",
      "expect": "Original unit retires and three successor identities preserve split lineage."
    },
    {
      "id": "reparent-no-reidentify",
      "kind": "positive",
      "input": "A room moves between administrative floor groupings without boundary change.",
      "expect": "Containment assertion changes while room identity remains stable."
    },
    {
      "id": "home-work-privacy",
      "kind": "negative",
      "input": "An employee works from home.",
      "expect": "No residential premises or public home address is minted; workplace allocation stores only permitted generalized locus externally."
    },
    {
      "id": "desk-booking",
      "kind": "negative",
      "input": "A pooled desk is reserved for one day.",
      "expect": "Booking does not create a new premises identity use designation or access grant."
    },
    {
      "id": "facility-without-site",
      "kind": "positive",
      "input": "A managed facility is registered without a parent site.",
      "expect": "The facility remains valid; absence of the optional site layer does not alter building or premises identity."
    },
    {
      "id": "building-without-facility",
      "kind": "positive",
      "input": "A standalone building contains premises but is not grouped into a facility.",
      "expect": "Premises resolve to the building shell without inventing a facility."
    },
    {
      "id": "indoor-space-duplicate",
      "kind": "negative",
      "input": "A room is given parallel WM-BLT-002 and WM-PLC-009 identities.",
      "expect": "The second identity is rejected; indoor topology is a profile over WM-BLT-002."
    },
    {
      "id": "gazetteer-not-container",
      "kind": "negative",
      "input": "A Gazetteer Place record is used as the containment parent of a managed site.",
      "expect": "The relation is rejected; the place locates the site by reference."
    }
  ]
}

## Workplace Allocation candidate

{
  "format": "vercy-model-allocation-candidate/v1",
  "contourId": "EM-FAC-01",
  "proposedName": "Workplace Allocation",
  "modelId": null,
  "registryId": null,
  "allocationState": "unassigned",
  "decision": "NEW MODEL",
  "canonicalPublishable": false,
  "identityTest": {
    "stableIdentity": "A governed relationship between exactly one engagement context and one physical, generalized, client-site, home-jurisdiction or mobile work locus remains identifiable across address, endpoint description, recurrence and booking changes.",
    "versionIdentity": "Changes to locus, workplace kind, validity, recurrence, exclusivity, purpose or primary status create effective-dated allocation versions while preserving prior allocation history.",
    "independentLifecycle": [
      "proposed",
      "approved",
      "active",
      "suspended",
      "ended",
      "superseded",
      "revoked"
    ],
    "mastership": "workplace planning and allocation authority"
  },
  "boundary": {
    "owns": [
      "persistent workplace-allocation identity",
      "employment or engagement context reference",
      "locus choice and workplace kind",
      "effective validity and recurrence",
      "exclusive, shared or pooled allocation semantics",
      "purpose, approving authority and primary-location assertion",
      "disclosure class and allocation status",
      "supersession and termination history"
    ],
    "references": [
      {
        "target": "WM-ORG-005",
        "purpose": "Employment or engagement context"
      },
      {
        "target": "WM-ORG-016",
        "purpose": "Position or work assignment context"
      },
      {
        "target": "WM-BLT-002",
        "purpose": "Premises or spatial-unit locus"
      },
      {
        "target": "WM-BLT-008",
        "purpose": "Site or campus locus"
      },
      {
        "target": "WM-PLC-010",
        "purpose": "Generalized place or jurisdiction locus"
      }
    ],
    "excludes": [
      "person, employment, assignment, place, site or premises identity",
      "home address or residential premises record",
      "lease, licence or ownership terms",
      "physical or logical access authorization",
      "desk, room or visit booking",
      "legal branch or establishment identity"
    ]
  },
  "objects": {
    "WorkplaceAllocation": {
      "identity": [
        "workplaceAllocationId"
      ],
      "required": [
        "engagementContextRef",
        "locus",
        "workplaceKind",
        "approvingAuthorityRef",
        "status"
      ],
      "optional": [
        "successorRef",
        "endedAt"
      ],
      "lifecycle": [
        "proposed",
        "approved",
        "active",
        "suspended",
        "ended",
        "revoked"
      ]
    },
    "AllocationVersion": {
      "identity": [
        "workplaceAllocationId",
        "version"
      ],
      "required": [
        "locus",
        "workplaceKind",
        "validFrom",
        "contentDigest",
        "status"
      ],
      "optional": [
        "validTo",
        "recurrence",
        "exclusivity",
        "purpose",
        "primaryLocation",
        "disclosureClass",
        "supersedesVersion"
      ],
      "lifecycle": [
        "draft",
        "approved",
        "active",
        "superseded",
        "withdrawn"
      ]
    },
    "LocusChoice": {
      "identity": [
        "locusChoiceId"
      ],
      "required": [
        "locusKind"
      ],
      "optional": [
        "premisesRef",
        "siteRef",
        "generalizedPlaceRef",
        "externalSiteRef",
        "mobileRegionRef"
      ],
      "oneOf": [
        "premisesRef",
        "siteRef",
        "generalizedPlaceRef",
        "externalSiteRef",
        "mobileRegionRef"
      ]
    }
  },
  "invariants": [
    "Every allocation resolves to exactly one explicit employment or engagement context.",
    "A locus choice identifies one permitted locus form and never silently converts between place, site and premises identities.",
    "Remote-home allocation stores only the approved generalized place or jurisdiction detail required for its purpose.",
    "Home work never creates a company office, public residential premises or ownership assertion.",
    "Workplace allocation never grants physical or logical access.",
    "A lease, licence or client-site agreement remains an external agreement record.",
    "A pooled allocation is not a desk reservation and an individual booking does not create an allocation.",
    "Office is an effective-dated use designation and never a new physical identity.",
    "A location designation never creates a legal branch or establishment.",
    "At most one primary allocation is effective per engagement context and period unless a named profile permits multiple primaries.",
    "Changing endpoint descriptions or addresses never silently mints a new site or premises identity.",
    "Ended and superseded allocations remain resolvable for historical workforce and facilities analysis.",
    "The allocation subject is an employment or engagement context and never a copied person master.",
    "A home-work locus is capped at approved jurisdiction granularity and never contains a residential address string.",
    "Replacing or splitting an endpoint creates an explicit successor allocation version when locus meaning changes.",
    "A client-site or third-party locus never implies employer ownership, lease, establishment or branch identity.",
    "Occupancy, capacity and allocation details are non-public by default and preserve source disclosure rules."
  ],
  "holds": [
    "Registry namespace and identifier allocation are pending and no identifier may be guessed.",
    "Data-protection and employment-law review is required for remote, client-site, mobile and desk-level records.",
    "WM-BLT-002 migration and WM-PLC-009 retirement remain unapproved proposals.",
    "One frozen semantic audit of the reconciled boundary is pending.",
    "Package conversion and live verification are pending."
  ],
  "version": "0.1.0-candidate.2"
}

## Workplace Allocation fixtures

{
  "format": "vercy-model-allocation-fixtures/v1",
  "proposedName": "Workplace Allocation",
  "cases": [
    {
      "id": "leased-hybrid-office",
      "kind": "positive",
      "input": "A hybrid team uses leased premises with pooled desks.",
      "expect": "Allocations reference the engagement and premises; lease and desk bookings remain external."
    },
    {
      "id": "client-site",
      "kind": "positive",
      "input": "A contractor works at a client site for a bounded period.",
      "expect": "The allocation records the client-site locus and validity without asserting employer ownership or creating a branch."
    },
    {
      "id": "remote-home",
      "kind": "positive",
      "input": "An employee is approved for home work in a stated jurisdiction.",
      "expect": "Only the permitted generalized location is stored; no residential premises or public address is created."
    },
    {
      "id": "mobile-work",
      "kind": "positive",
      "input": "A field role operates across a defined region without a fixed premises.",
      "expect": "A mobile or generalized-region locus is valid and does not require a building."
    },
    {
      "id": "allocation-grants-access",
      "kind": "negative",
      "input": "A system grants door and application access solely from workplace allocation.",
      "expect": "The inference is rejected; explicit access grants remain required."
    },
    {
      "id": "double-primary",
      "kind": "negative",
      "input": "Two overlapping allocations are both marked primary without an enabling profile.",
      "expect": "The allocation set is rejected."
    },
    {
      "id": "home-address-string",
      "kind": "negative",
      "input": "A remote allocation stores a worker's street address.",
      "expect": "Validation rejects the address and permits only the approved generalized jurisdiction."
    },
    {
      "id": "client-site-branch",
      "kind": "negative",
      "input": "A client-site allocation is treated as an employer legal branch.",
      "expect": "The inference is rejected because allocation never creates establishment identity."
    },
    {
      "id": "endpoint-split",
      "kind": "positive",
      "input": "An allocated premises is split into successor units.",
      "expect": "The old allocation remains historical and a successor allocation version explicitly chooses the new locus."
    }
  ],
  "version": "0.1.0-candidate.2"
}

## Profile candidate

{
  "format": "vercy-enterprise-profile-candidate/v1",
  "contourId": "EM-FAC-01",
  "name": "Office Use and Indoor Topology",
  "decision": "PROFILE",
  "newRuntimeId": false,
  "bases": ["WM-BLT-002"],
  "duplicateRetirementProposal": "WM-PLC-009",
  "constraints": [
    "Office is an effective-dated use designation of a premises or bounded premises set.",
    "Indoor navigation and topology are WM-BLT-002 profiles rather than competing spatial identity.",
    "Address, occupier, room number and use designation never define premises identity.",
    "Re-parenting preserves spatial-unit identity; split or merge creates explicit lineage.",
    "Lease, ownership, legal branch, access, booking and person identity remain external."
  ]
}

## Local evidence

# EM-FAC-01 local synthesis

## Disposition

EM-FAC-01 is a composed landscape with two missing pieces:

1. **complete reserved WM-BLT-002 Premises / Spatial Unit** as the single interior-space authority;
2. research a separate **Workplace Allocation relationship** whose identifier remains unassigned.

Reuse WM-PLC-010 Gazetteer Place, WM-BLT-008 Site / Campus, WM-BLT-006 Facility and WM-BLT-001 Building / Structure. Treat `office` as an effective-dated use/designation profile, not a new physical object or legal branch.

## Duplicate resolution

WM-PLC-009 Indoor Space overlaps the same bounded interior extent as WM-BLT-002. WM-BLT-002 has stronger inbound evidence: WM-BLT-001 contains it, WM-OBJ-001 names it as premises identity/geometry master, and WM-BLT-006 explicitly delegates room and space semantics to a space model.

Proposed registry action: retire WM-PLC-009 as a standalone candidate and preserve indoor navigation/topology as a profile of WM-BLT-002. This remains a proposal pending independent review and relation-ledger audit.

## Physical containment spine

`Gazetteer Place <- Site/Campus -> Facility -> Building/Structure -> Premises/Spatial Unit`, with recursive premises containment where appropriate. Address, legal branch, lease, ownership, employment, access grant, booking and person identity remain external.

## WM-BLT-002 minimum boundary

The model owns persistent spatial-unit identity, parent containment with validity, kind, designator, geometry reference, measured area evidence, design capacity, separately-governed status, control/occupancy role references, effective-dated use designations and split/merge lineage.

Address, room number, current occupier and use designation never define identity. Re-parenting does not mint identity. Split and merge do.

## Workplace Allocation candidate

An allocation relates an employment or engagement context to a physical or external locus for a validity window. It needs its own identity because one engagement may have concurrent allocations, remote/mobile/client-site loci may have no premises record, and allocation survives changes to either endpoint.

Portable fields: subject-context reference, locus choice, workplace kind, exclusivity/pooled status, validity and recurrence, approving authority, purpose, primary-location flag, disclosure class and status.

The identifier is deliberately unassigned. Claude proposed `WM-WPL-001`, but no WPL namespace exists in the registry; allocation must follow the registry process.

## Privacy and authority invariants

- A home address never becomes a company office, premises record or public fact merely because work occurs there.
- Remote-home allocation stores at most an appropriate jurisdiction/generalized place reference.
- Workplace allocation never grants physical or logical access automatically.
- A legal branch references a location; location designation never creates a branch.
- Lease and licence terms remain agreement records.
- Desk reservations remain booking records; pooled entitlement is an allocation.
- At most one primary work location is effective per subject context and period unless a declared profile allows multiple primaries.

## Holds

WM-BLT-002 now has a reviewable completion candidate with persistent identity, temporal containment, boundary and area evidence, use designations, split/merge lineage, four external relation contracts and seven fixtures. The previous description still requires migration packaging. IFC host/version differences, Facility/Building crosswalk, indoor topology sources, area standards, privacy review, WM-PLC-009 retirement and Workplace Allocation allocation remain unresolved. Exact Grok comparison, one frozen semantic audit, package conversion and live verification are still required.

## Initial Claude study

## DECISION

**Combination: REUSE (4) + COMPLETE RESERVED MODEL (1) + PROFILE (1) + NEW MODEL (1). LANDSCAPE rejected.**

- **REUSE unchanged:** WM-PLC-010 Gazetteer Place (named place, geographic identifier, sensitivity/generalization mixin), WM-BLT-008 Site / Campus, WM-BLT-006 Facility, WM-BLT-001 Building / Structure. All four already carry identity, bitemporal lifecycle, address-by-reference and party-by-reference. Nothing in EM-FAC-01 requires a new physical container.
- **COMPLETE RESERVED MODEL WM-BLT-002 Premises / Spatial Unit** as the single interior-space master. Three published models already point at a space master that does not exist (WM-BLT-006 out-of-scope "Space model", WM-BLT-001 `COMPOSE` to WM-BLT-002, WM-OBJ-001 naming WM-BLT-002 master for premises identity/geometry/address semantics). This is a dangling reference, not a new idea.
- **PROFILE, not model: Use / Occupancy Designation.** "Office" is a dated designation assertion profile applied to WM-BLT-002 and WM-BLT-006. It has no identity of its own and no lifecycle beyond its validity window.
- **NEW MODEL WM-WPL-001 Workplace Allocation** (relationship/event model, `entry_kind: relationship`). Proof of independent identity below.
- **WM-PLC-009 Indoor Space: retired by merge, not kept as a synonym.**

Smallest coherent composition (containment spine): Gazetteer Place ←reference— Site/Campus —contains→ Facility —contains→ Building/Structure —composes→ Premises/Spatial Unit (recursive) ←locus— Workplace Allocation.

## BOUNDARY AND OVERLAP RESOLUTION

**WM-BLT-002 vs WM-PLC-009.** Both describe a bounded interior extent. Two identities for one room is the defect, so one entry must lose standalone status. WM-BLT-002 wins on evidence, not seniority: it has a spec (`U2-premises-and-spatial-unit.md`), an inbound `CONTAINS` from WM-BLT-001, a declared `contains_ids` to WM-OBJ-001, and a named mastership claim from WM-OBJ-001. WM-PLC-009 has no spec, no composition role, no relations file and a purpose that only records that its boundary is unresolved.

Action: set WM-PLC-009 `status: retired-superseded`, `possible_duplicate_of / superseded_by: WM-BLT-002`, `entry_kind: profile-of`. Keep `NAV.PHY.PLC.IND` as a redirect alias onto an **Indoor Topology profile of WM-BLT-002** (navigable cell, connectivity graph, indoor positioning reference). That content is a projection over the same spatial unit, so it is a profile, never a second class. Do not mint an "Indoor Space" class name as an alternate name for Premises: aliasing at class level is how synonym drift restarts.

**Other boundaries held.** Premises identity ≠ address (WM-PLC-010 / address sibling). Premises ≠ legal branch: a branch is an Organization-model construct that *references* a premises as registered or operating locus; no designation on a premises may create, imply or publish a branch, and no branch registration may mint a premises. Lease and licence terms stay in the agreement sibling (referenced by identifier only). Employment stays WM-ORG-005, which already declares it does not own workspace identity. Person, credential and access-card issuance stay in Identity/Access. Desk *reservations* stay in the Booking sibling. Facility keeps only aggregate space counts and area totals, as it already states.

**Does allocation need its own identity?** Yes, on three independent grounds. (1) The locus may not be a registry object at all — home, mobile and client-site workplaces have no premises row, so the allocation cannot be an assertion hanging off WM-BLT-002. (2) One employment period carries several concurrent allocations with different dates, exclusivity and approvers; folding them into WM-ORG-005 either flattens them or re-invents a relationship table inside Employment. (3) It must survive replacement of both endpoints (premises re-parented or split, employment record superseded) and be independently supersedable and auditable. That is an identity, not a field.

## MINIMAL CONTRACTS

**WM-BLT-002 Premises / Spatial Unit**

*Identity:* opaque persistent identifier, master-system qualified. Created when a spatial extent is separately usable or separately governed. Unit designator, storey label, address and occupier are attributes, never identifiers. Exactly one active parent containment at a time (Building, Facility or Premises), dated; re-parenting does not mint a new identifier.

*Lifecycle:* planned → shell/constructed → fit-out → available → in use → vacant → out of service / refurbishment → decommissioned / demolished; plus split and merge transitions requiring predecessor–successor lineage and reason. Bitemporal (record validity distinct from real-world validity), inherited from the existing versioning mixin.

*Core fields:* id; parent ref + period; spatial-unit kind (room, suite, floor, open area, apartment, parking bay, unallocated circulation); designator + issuing authority; geometry ref with CRS and LoD (geometry mixin); measured area with declared measurement standard, method and date; design occupant capacity; separately-governed flag; control and occupancy role refs (controller, occupant, service provider) with validity and agreement ref; use/occupancy designation assertions (dated, with asserting authority, code-occupancy kept distinct from operational designation); sensitivity class.

*Invariants:* (i) address is never sole or mandatory identifier; (ii) contained extents may not exceed the parent extent, and containment periods may not overlap across parents; (iii) designation, occupancy and control are dated assertions and never change identity; (iv) no person, credential, lease-term, employment or booking data — references only; (v) split/merge requires lineage; (vi) a premises record may not be created from a worker's residential address.

**WM-WPL-001 Workplace Allocation**

*Identity:* opaque id over (subject context, locus, workplace kind, validity window, authority). *Lifecycle:* proposed → active → suspended → ended / superseded / revoked; one authority per transition; effective-dated with supersession lineage.

*Core fields:* subject ref (employment or engagement context, not person master); locus — exactly one of premises ref, facility/site ref, or external-locus descriptor {kind: client-site | third-party | home | mobile, jurisdiction ref via WM-PLC-010, controlling org ref}; workplace kind (assigned desk, shared-desk entitlement, hotelling, office-based, remote-home, mobile, client-site); exclusivity (exclusive | shared | pooled); validity window and recurrence; approving authority; purpose; primary-work-location flag; disclosure class; status.

*Invariants:* no address string, no PII, no lease or agreement terms, no access rights, no reservation instances; must not create or imply a premises, facility or branch; at most one primary work location per subject per period; remote-home locus precision capped at jurisdiction granularity; access grants are never derived automatically from an allocation.

## ACCEPTANCE WALKTHROUGH

1. **Containment:** Gazetteer Place names the locality; Site holds managed extent and tenure refs; Facility is the operating unit; Building holds fabric; Premises holds the room. Each retains its own identifier and lifecycle.
2. **Office as role:** a Premises carries a dated `office` use designation; the branch, if any, is an Organization record referencing it. Removing the designation does not touch either identity.
3. **Address change:** Site and Premises identifiers are unchanged; the role-tagged address reference is superseded with its own validity, per existing Site lifecycle rules.
4. **Leased office / client site:** occupancy and control roles are dated refs with an agreement identifier; ownership is absent. A client site needs no premises record — it is an external-locus descriptor on the allocation.
5. **Remote worker:** allocation kind `remote-home`, locus = jurisdiction ref only. No premises, no facility, no designation, no published address.
6. **Hot desk / hotelling:** allocation with exclusivity `shared` or `pooled`, bounded window and recurrence; the daily desk reservation resolves in the Booking sibling against that entitlement.
7. **Seven-way separation:** identity (WM-BLT-002) / designation (profile) / allocation (WM-WPL-001) / lease (agreement sibling) / employment (WM-ORG-005) / access (Identity–Access) / booking (Booking sibling), each with its own authority and dates.
8. **Allocation identity:** established above; it is a model, not a profile.

WM-ACT-040's external Workspace and Facility masters now resolve to WM-WPL-001 and WM-BLT-006.

## PRIVACY AND AUTHORITY RULES

Residential addresses remain in the Party/Person master under its own access controls; allocation stores only the fact of remote work and a jurisdiction. Home loci are never publishable, never designated, never aggregated into public premises or facility inventories. Apply the WM-PLC-010 graded sensitivity mixin to premises and allocation: default non-public for occupancy, capacity and allocation; generalize rather than randomize; record what was withheld, on what basis, who may except it, and the review date. Authority: premises identity and geometry — facility/premises owner or custodian; code occupancy — authority having jurisdiction only; operational designation — facility management; allocation — employing organization's named approver; jurisdiction and place naming — external gazetteer authority. No single role may assert across two of these.

## HOLDS AND PUBLICATION RECOMMENDATION

Publish WM-BLT-002 and WM-WPL-001 as **reviewable-draft, publishableCanonical false**. The composition cannot exceed its weakest member: all four reused models are reviewable drafts with open source-pinning holds, and WM-BLT-001 is a single-provider waiver.

Inherited blockers: the unresolved IFC documentation host/build pin (WM-BLT-006 and WM-BLT-008 disagree), the Facility-contains-Building versus IfcBuilding-subtype-of-IfcFacility conflict, unread ISO clause text, and incomplete non-US/multi-profile validation.

New holds: (1) re-read and diff `U2-premises-and-spatial-unit.md` before completion — WM-BLT-002 is `described-previous-version`, so this is a migration, not a green field; (2) pin one IFC citation for IfcSpace/IfcSpatialZone and one for COBie Space/Zone; (3) IndoorGML and indoor-positioning grounding is unverified — publish the Indoor Topology profile as provisional; (4) area measurement standards (ISO 9836, IPMS) cited for existence only, so no field-level area naming; (5) WM-WPL-001 needs an employment-law and data-protection cross-check in at least one non-US jurisdiction, including works-council consultation on desk-level allocation records, before any operational use; (6) registry hygiene: record the WM-PLC-009 supersession, update `VERCY-MODEL-RELATIONS.csv`, and re-target every "Space model" reference in WM-BLT-006 and WM-BLT-001 to WM-BLT-002; the current `factor_overlap` of 0.08 on both reserved entries is contradicted by this review and should be corrected.

## Grok study

DECISION

Accept the proposed composition with four corrections.

The physical spine is a preferred reference path, not mandatory exclusive containment. Gazetteer Place locates; it does not parent a managed site.

Retire WM-PLC-009 as a standalone synonym. Surviving identity is WM-BLT-002 Premises / Spatial Unit. Indoor navigation and topology survive only as a WM-BLT-002 profile.

Office is an effective-dated use/designation profile, not a physical identity and not a legal branch.

Workplace Allocation is a NEW MODEL (relationship). It is not REUSE of employment, work assignment, position or premises occupancy, and not a PROFILE of those models. No numeric catalogue identifier is assigned.

PHYSICAL MODEL BOUNDARY

Gazetteer Place (WM-PLC-010) is a named real-world location whose opaque identifier survives rename, reclassification and re-delimitation. A date, name or coordinate pair is never the identifier. The model is gazetteer-centric and does not govern indoor units unless they are separately registered as named places. Cross-theme linking to built works is deferred.

Site / Campus (WM-BLT-008) is bounded land under coordinated management. It may contain facilities, infrastructure and open space; it may include discontiguous parts and third-party enclaves; its operational boundary may diverge from the legal parcel.

Facility (WM-BLT-006) is a managed aggregation of buildings, structures, systems and grounds. It is not a space and not a single asset. Site containment is conditional: IFC permits a facility with no site. Identity persists through site split or amalgamation.

Building / Structure (WM-BLT-001) is a persistent engineered artifact. Site, parcel and address are external georeferences, not identity. Premises, space and zone are referenced through spatial decomposition; the building does not absorb their mastership.

Premises / Spatial Unit (WM-BLT-002, published only as 0.2.0-legacy) is the interior identity and geometry master: independently delineated units, successive boundaries, common parts, use class and occupancy spells. A premise sits inside a building shell but is transacted and occupied independently of that shell.

Preferred path: Place locates Site; Site may contain Facility; Facility may contain Building; Building contains Premises. Allowed exceptions already present in the published models: facility without site; building without facility; premises in a building the employer does not own; workplace loci that never enter the building layer (client site, home-jurisdiction, mobile).

WM-PLC-009 Indoor Space must not be completed as a gazetteer sibling. Indoor space is a bounded built-environment unit with geometry, common parts, merge and split events. Published models already point at WM-BLT-002; WM-XCT-010 resolves floor, unit, room and seat locators to the premises model. A parallel PLC identity would split the master. No public published page for WM-PLC-009 was found.

WORKPLACE ALLOCATION BOUNDARY

Office is a use designation. A premises or site may carry an effective-dated office use class without changing identity. The same unit can be office this year and shop next year. “Registered office” remains a legal-address role on the organization (WM-ORG-001). Business establishment / branch (WM-ORG-011) is an operating-presence record with no universal equivalence to premises, site or legal entity. “Office of the CTO” is an organizational function and is out of this composition.

Workplace Allocation cannot be owned by employment or by space.

WM-ORG-005 records workplace, remote, mobile and cross-border context by reference; it does not identify concurrent allocations.
WM-ORG-016 binds an agent to a role or body of work and references a base location; one assignment commonly needs several concurrent loci.
WM-ORG-004 records a position’s default work-location arrangement, not a person-period allocation.
Legacy occupancySpell records who occupies a unit. It is premises-centric, names occupants, is silent for mobile and jurisdiction-only loci, and is unsafe for homes.

Workplace Allocation is therefore a NEW MODEL: an independently identified, effective-dated relationship between an employment or engagement context and a polymorphic locus — premises, site, client-site, home-jurisdiction or mobile. Cardinality is many concurrent allocations per engagement. Booking, hoteling and badge grants remain external. No numeric identifier is minted until registry review.

Lease, access, booking, employment and legal-branch boundaries are correctly external, as EM-FAC-01 already states. Location is not a legal branch.

ACCEPTANCE SCENARIO

A hybrid team is representable without employer building ownership and without publishing homes.

Leased office: third-party Site and/or Premises, office use designation, external lease. No employer Building master.
Pooled desks: Premises or spatial units plus dated Workplace Allocations; desk booking stays external.
Client site: referenced third-party Site, Facility or Premises; no ownership transfer.
Remote/mobile: Workplace Allocation mode with host jurisdiction and optional coarse gazetteer Place; no Building required.

Address change does not mint a new Site or Premises. Address is a WM-XCT-010 binding. Rebind the address with a validity interval; keep the prior binding; site and premises identifiers persist.

PRIVACY AND AUTHORITY

The negative case is binding: a remote employee’s home address must not be published as a company office.

Do not mint a residential WM-BLT-002 premises from home-work. Do not project street-level or unit-level residential facts into any facilities or office directory. Home-work is an allocation mode plus jurisdiction, optionally a coarse Place (city or region). Street address, if held at all, stays on the party contact profile under purpose limitation and a disclosure policy. Occupancy spells must not be used for homes. Person civil-identity fields are not required merely to collaborate. Private instance records must not be sent to the public catalogue.

HOLDS AND PUBLICATION RECOMMENDATION

Recommend the corrected composition for further research. Do not declare it canonical.

Complete WM-BLT-002 from 0.2.0-legacy to a research draft before treating it as an installable master. Unresolved requires include parcel, organization and person; it is not installable today.

Retire WM-PLC-009 by registry decision; do not publish a stub.

Do not assign a numeric identifier to Workplace Allocation in this review.

WM-PLC-010, WM-BLT-008, WM-BLT-006 and WM-BLT-001 remain reviewable-drafts with open source and coverage holds. Facility CONTAINS Building versus IFC IfcBuilding-as-subtype remains an open crosswalk.

Home-work non-publication is a hard hold on any derived office directory. Semantic fit of the published BLT models to EM-FAC-01 still requires a full crosswalk; publication of a sibling does not complete this card.