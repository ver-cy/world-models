# Frozen semantic audit: EM-TEC-04

Audit the reconciled candidate using only the frozen material below. No tools, browsing, identifier invention, code generation or publication claims. Find hidden aggregate boundaries, identity collisions, lifecycle ambiguity, mastership conflicts, temporal-history loss, unsafe CI/asset merging, and missing executable negative cases. Return <=1000 words with headings Verdict; Findings; Required remediations; Adequate decisions; Minimal release gate. Verdict must be ACCEPT, ACCEPT WITH LIMITS, or REVISE.

## Reconciled candidate
```json
{
  "format": "vercy-world-model-candidate/v1",
  "contourId": "EM-TEC-04",
  "modelId": "WM-SFT-010",
  "registryId": "vr.wm-sft-010",
  "name": "Runtime / Compute Environment",
  "version": "0.1.0-candidate.2",
  "entryKind": "runtime-aggregate",
  "status": "research-candidate",
  "canonicalPublishable": false,
  "purpose": "Represent governed runtime environments, infrastructure resources, dependent runtime-occupant records, configuration-control designations and temporal hosting topology without duplicating logical systems, deployment occurrences, asset records or tenant landscape facts.",
  "boundary": {
    "owns": [
      "runtime-environment identity and lifecycle",
      "infrastructure-resource identity and capacity-bearing classification",
      "dependent runtime-occupant records for as-of hosting, never gold-copy subject identity",
      "effective-dated HostingRelation topology",
      "desired-versus-observed state correlation and retained drift",
      "configuration-item designation under a named control authority"
    ],
    "delegates": [
      "logical software-system and business-application identity to WM-SFT-002",
      "deployment occurrence and placement outcome to WM-SFT-009",
      "fact mastership and bounded impact projection semantics to WM-XCT-039",
      "physical-item identity and asset evidence to WM-OBJ-001",
      "financial asset and depreciation semantics to finance masters"
    ],
    "excludes": [
      "a second logical Software System identity",
      "deployment-plan or deployment-event lifecycle",
      "DeployedInstance as an independent gold-copy master",
      "network address as an eternal identifier",
      "copy of financial or physical asset master",
      "current topology represented as timeless truth",
      "deletion or identifier reuse for ephemeral resources"
    ]
  },
  "objects": {
    "RuntimeEnvironment": {
      "identity": [
        "environmentId"
      ],
      "required": [
        "name",
        "environmentKind",
        "controlAuthorityRef",
        "commissionedAt",
        "status"
      ],
      "optional": [
        "region",
        "isolationPolicy",
        "capacityProfile",
        "retiredAt"
      ],
      "lifecycle": [
        "planned",
        "commissioned",
        "active",
        "restricted",
        "retired"
      ]
    },
    "InfrastructureResource": {
      "identity": [
        "resourceId"
      ],
      "required": [
        "resourceKind",
        "providerRef",
        "provisionedAt",
        "status"
      ],
      "optional": [
        "capacity",
        "region",
        "parentResourceRef",
        "releasedAt",
        "successorResourceId"
      ],
      "lifecycle": [
        "planned",
        "provisioned",
        "active",
        "degraded",
        "released"
      ]
    },
    "HostingRelation": {
      "identity": [
        "hostingRelationId"
      ],
      "required": [
        "subjectRef",
        "hostRef",
        "relationKind",
        "validFrom",
        "assertionKind",
        "sourceRef",
        "recordedAt",
        "status"
      ],
      "optional": [
        "validTo",
        "observedAt",
        "confidence",
        "method",
        "withdrawalReason"
      ],
      "lifecycle": [
        "asserted",
        "superseded",
        "withdrawn"
      ]
    },
    "ConfigurationItemDesignation": {
      "identity": [
        "designationId"
      ],
      "required": [
        "subjectRef",
        "controlAuthorityRef",
        "validFrom",
        "scope",
        "status"
      ],
      "optional": [
        "validTo",
        "assetRef",
        "identityEvidenceRefs",
        "withdrawalReason"
      ],
      "lifecycle": [
        "asserted",
        "effective",
        "withdrawn"
      ]
    },
    "StateAssertion": {
      "identity": [
        "stateAssertionId"
      ],
      "required": [
        "subjectRef",
        "stateKind",
        "value",
        "effectiveAt",
        "recordedAt",
        "sourceRef",
        "method"
      ],
      "optional": [
        "observedAt",
        "supersedesAssertionId"
      ]
    },
    "RuntimeOccupantRecord": {
      "identity": [
        "occupantRecordId"
      ],
      "identitySemantics": "Dependent correlation key only; not a gold-copy subject identity and never reused.",
      "required": [
        "logicalSystemRef",
        "deploymentOccurrenceRef",
        "artifactVersionRef",
        "runtimeKey",
        "environmentRef",
        "observedFrom",
        "sourceRef",
        "status"
      ],
      "optional": [
        "observedTo",
        "terminalState",
        "successorRuntimeKey"
      ],
      "lifecycle": [
        "observed-active",
        "observed-stopped",
        "closed"
      ]
    }
  },
  "hostingRelationKinds": [
    "runs-on",
    "member-of",
    "backed-by",
    "served-by"
  ],
  "assertionKinds": [
    "declared",
    "observed",
    "inferred"
  ],
  "relations": [
    {
      "target": "WM-SFT-002",
      "relation": "REFERENCE",
      "required": true,
      "purpose": "Resolve the logical software system or business application without copying identity."
    },
    {
      "target": "WM-SFT-009",
      "relation": "REFERENCE",
      "required": false,
      "purpose": "Resolve the deployment occurrence that created or changed deployed instances."
    },
    {
      "target": "WM-XCT-039",
      "relation": "REFERENCE",
      "required": false,
      "purpose": "Reuse fact-mastership desired-versus-observed and bounded impact projection rules."
    },
    {
      "target": "WM-OBJ-001",
      "relation": "REFERENCE",
      "required": false,
      "purpose": "Resolve an underlying physical item while preserving separate CI and asset lifecycles."
    }
  ],
  "operations": [
    {
      "id": "commission-environment",
      "effect": "Create a governed runtime environment independent of its current members.",
      "authority": "environment owner"
    },
    {
      "id": "provision-resource",
      "effect": "Record a provider-identified capacity-bearing resource.",
      "authority": "resource provider or delegated operator"
    },
    {
      "id": "record-runtime-occupant",
      "effect": "Append a dependent runtime observation bound to one WM-SFT-002 subject, one WM-SFT-009 occurrence and one immutable artifact version.",
      "authority": "authorized orchestrator or observability source; WM-SFT-010 does not mint a competing subject identity"
    },
    {
      "id": "assert-hosting",
      "effect": "Append a temporal topology edge with source and assertion kind.",
      "authority": "authorized topology source"
    },
    {
      "id": "record-state",
      "effect": "Append desired or observed state while retaining drift.",
      "authority": "declared master for the fact path"
    },
    {
      "id": "designate-ci",
      "effect": "Place a referenced subject under configuration control for a validity period.",
      "authority": "configuration-control authority"
    },
    {
      "id": "retire-subject",
      "effect": "Close validity and retain a tombstone and succession evidence.",
      "authority": "subject owner"
    }
  ],
  "invariants": [
    "WM-SFT-002 logical identity is invariant under deployment, hosting, scaling, region and node replacement.",
    "WM-SFT-009 owns the deployment occurrence and desired placement; WM-SFT-010 owns observed environment, resource and hosting facts.",
    "A RuntimeOccupantRecord is dependent on exactly one WM-SFT-002 subject and one WM-SFT-009 occurrence and references exactly one immutable artifact version.",
    "Runtime occupant correlation keys are never treated as independent gold-copy subject identities.",
    "Environment, infrastructure resource, runtime occupant record and CI designation use distinct keys and lifecycles.",
    "Every observation records source, method and observed, effective and recorded times as applicable.",
    "Address or hostname change alone never changes subject identity.",
    "Every HostingRelation has a validity interval, assertion kind and endpoints allowed by hostingEndpointRules.",
    "Cluster membership and occupant hosting are distinct temporal relations.",
    "Current topology is an as-of projection of temporal relations rather than timeless stored truth.",
    "Identifiers are never recycled and retirement retains a policy-governed tombstone.",
    "Environment and cluster identity remain independent of member resources.",
    "Node replacement creates a new resource identifier and closes old membership and hosting intervals.",
    "Desired and observed states remain separate and drift is retained.",
    "A CI designation does not duplicate its designated subject and withdrawal never destroys that subject.",
    "CI-eligible subject types are explicitly limited to the declared list.",
    "A CI designation and a financial or physical asset record never share identity.",
    "Asset-resource linkage requires effective-dated evidence and never merges identities.",
    "Missing or stale observation means unknown rather than absent.",
    "Impact answers are time-qualified and state their completeness boundary.",
    "Region, environment, cluster, node and runtime occupant layers are never flattened into one identity."
  ],
  "holds": [
    "One frozen no-tools semantic audit of the reconciled candidate is pending.",
    "WM-SFT-002 migration and WM-SFT-009/WM-XCT-039 publication holds remain external.",
    "Artifact-version and financial-asset bindings require their domain registries.",
    "The governing tombstone-retention policy must be pinned before a finite historical guarantee is claimed.",
    "Package conversion and live HTTP/runtime/search/package verification are pending."
  ],
  "hostingEndpointRules": {
    "runs-on": {
      "subjectTypes": [
        "RuntimeOccupantRecord"
      ],
      "hostTypes": [
        "InfrastructureResource"
      ]
    },
    "member-of": {
      "subjectTypes": [
        "InfrastructureResource"
      ],
      "hostTypes": [
        "InfrastructureResource:cluster"
      ]
    },
    "backed-by": {
      "subjectTypes": [
        "InfrastructureResource"
      ],
      "hostTypes": [
        "WM-OBJ-001"
      ]
    },
    "served-by": {
      "subjectTypes": [
        "RuntimeOccupantRecord",
        "WM-SFT-002"
      ],
      "hostTypes": [
        "RuntimeEnvironment",
        "InfrastructureResource:cluster"
      ]
    }
  },
  "configurationItemEligibleSubjects": [
    "WM-SFT-002",
    "WM-SFT-009",
    "WM-SFT-010:RuntimeEnvironment",
    "WM-SFT-010:InfrastructureResource"
  ],
  "mastership": {
    "declaredPlacement": "WM-SFT-009",
    "observedHosting": "WM-SFT-010 authorized discovery or observability source",
    "logicalSystemIdentity": "WM-SFT-002",
    "environmentAndResourceIdentity": "WM-SFT-010",
    "projectionAndCompleteness": "WM-XCT-039"
  },
  "identityStack": [
    "region is a classification or external jurisdiction/placement reference, never environment identity",
    "RuntimeEnvironment is the governed regional or isolation context",
    "InfrastructureResource:cluster is a stable logical capacity subject",
    "InfrastructureResource:node is a non-recycled member subject",
    "RuntimeOccupantRecord is a dependent observation bound to WM-SFT-002 and WM-SFT-009"
  ],
  "assetEvidenceContract": {
    "required": [
      "assetRef",
      "resourceRef",
      "evidenceRef",
      "effectiveFrom",
      "sourceRef",
      "confidence"
    ],
    "optional": [
      "effectiveTo",
      "serialOrProviderCorrelation"
    ],
    "rule": "Evidence links identities; it never merges asset, resource or CI designation identity."
  },
  "tombstonePolicy": {
    "rule": "Closed subjects and runtime keys remain as-of queryable for the retention period named by the governing policy; keys are never recycled.",
    "policyOwnership": "external retention policy master",
    "unknownPolicyEffect": "Retention is pending and publication cannot claim unbounded history."
  }
}
```

## Fixtures
```json
{
  "format": "vercy-world-model-fixtures/v1",
  "modelId": "WM-SFT-010",
  "version": "0.1.0-candidate.2",
  "cases": [
    {
      "id": "two-region-service",
      "kind": "positive",
      "input": "One logical service is placed by two deployment occurrences into EU and US runtime environments.",
      "expect": "One WM-SFT-002 identity, two WM-SFT-009 occurrences and two WM-SFT-010 environments remain distinct."
    },
    {
      "id": "node-replacement-as-of",
      "kind": "positive",
      "input": "Node N1 is retired at T2 and N2 replaces it before T3.",
      "expect": "T1 impact returns N1 and old occupant records; T3 returns N2 and successors with N1 tombstone retained."
    },
    {
      "id": "ip-reassignment",
      "kind": "negative",
      "input": "The same IP address is later assigned to another tenant resource.",
      "expect": "Resources remain distinct because address is an effective-dated observation, not identity."
    },
    {
      "id": "missing-edge",
      "kind": "negative",
      "input": "One topology source is stale or unavailable.",
      "expect": "Impact reports incomplete coverage rather than no impact."
    },
    {
      "id": "ci-and-asset",
      "kind": "positive",
      "input": "One owned chassis is capitalized and also under configuration control.",
      "expect": "Physical item, asset record, resource and CI designation remain distinct and linked by effective evidence."
    },
    {
      "id": "cluster-member-turnover",
      "kind": "positive",
      "input": "All nodes of a logical cluster are replaced.",
      "expect": "Cluster identity remains stable while membership edges close and reopen."
    },
    {
      "id": "desired-observed-drift",
      "kind": "negative",
      "input": "Declared desired version differs from discovered running version.",
      "expect": "Both assertions and drift remain visible; neither silently overwrites the other."
    },
    {
      "id": "occupant-not-master",
      "kind": "negative",
      "input": "A runtime replica key is proposed as a second identity for the logical service.",
      "expect": "The key remains a dependent RuntimeOccupantRecord correlation key bound to WM-SFT-002 and WM-SFT-009."
    },
    {
      "id": "scale-out-one-occurrence",
      "kind": "positive",
      "input": "One deployment occurrence produces four concurrent runtime occupants.",
      "expect": "All four dependent records reference the same occurrence without becoming independent service masters."
    },
    {
      "id": "redeploy-new-occurrence",
      "kind": "positive",
      "input": "A new deployment occurrence replaces occupants while the logical system remains unchanged.",
      "expect": "New dependent occupant records bind to the new occurrence; the WM-SFT-002 identity is unchanged."
    },
    {
      "id": "membership-vs-hosting",
      "kind": "negative",
      "input": "A node member-of edge is supplied where an occupant runs-on edge is required.",
      "expect": "Endpoint rules reject the relation-kind substitution."
    },
    {
      "id": "ci-withdrawal",
      "kind": "positive",
      "input": "Configuration control is withdrawn from an environment.",
      "expect": "The designation closes while the environment subject survives."
    },
    {
      "id": "asset-link-without-evidence",
      "kind": "negative",
      "input": "A resource is equated to an asset using only a matching display name.",
      "expect": "The merge is rejected because effective-dated identity evidence is missing."
    },
    {
      "id": "unknown-retention-policy",
      "kind": "negative",
      "input": "A tombstone has no pinned governing retention policy.",
      "expect": "The record is retained and the history guarantee is marked pending rather than assumed unbounded."
    },
    {
      "id": "region-flattening",
      "kind": "negative",
      "input": "Two regional environments are collapsed because they host the same service.",
      "expect": "The environments remain distinct; service identity and region classification do not replace environment identity."
    }
  ]
}
```

## First Claude study
# EM-TEC-04 — Independent Review

## Verdict
**Extend-by-completion into WM-SFT-010, not new, not WM-SFT-002.** EM-TEC-04 is the subject home for `RuntimeEnvironment`, `InfrastructureResource`, `DeployedInstance` and `HostingRelation`. `ConfigurationItem` is rejected as a fifth class and readmitted as an effective-dated *designation* over a referenced subject. WM-SFT-010 is reserved, wave-1, parented to WM-SFT-002, and has **no specification file**, so this contour supplies its missing content rather than founding a competing model. WM-XCT-039 is `REFERENCE`/compose-only (mastership, projection, bounded impact), never the inventory. WM-SFT-009 stays the deployment *occurrence*. Boundary decision: `extend` (complete the reserved candidate); no new registry ID is proposed or invented.

## Evidence
WM-SFT-009 explicitly out-of-scopes "runtime environment definition, topology, capacity, infrastructure inventory and environment lifecycle (owned by WM-SFT-010)" and keeps `de-instance-refs` / `de-placement-regions` inline as correlation keys only — a declared hole exactly the size of EM-TEC-04. The frozen relation rows already give `WM-SFT-009 → WM-SFT-010` ("Deployment targets a runtime environment"), both `candidate`. Legacy WM-SFT-002 carries only `environment` (environmentType, locationRef, platform) and `deployedSystem` with a single `hostedIn` edge — too coarse, and EM-TEC-02 already resolved installations *out* of WM-SFT-002 into current deployment plus runtime environment. WM-XCT-039 supplies per-fact mastership, desired-versus-observed retention, identity-anchor and bounded-impact semantics, but scope_statement forbids it becoming "a competing CMDB", and its coverage marks validation a `gap`.

## Identity/mastership
- **RuntimeEnvironment** — governed, long-lived logical execution context. Identity from the environment registry/CMDB master; `environment_kind`, `region`, `capacity`, `isolation_policy` are attributes, not keys. Independent of member resources.
- **InfrastructureResource** — capacity-bearing node, VM, volume, cluster or network. Identity from the provider/hardware master (cloud resource id, Redfish-class identity per SRC-005 pattern). Hostname and address are observed attributes.
- **DeployedInstance** — one running incarnation. Identity is `instance_key` minted by the runtime, plus `service_scope`; masters are the orchestrator and observability. Mandatory pinned reference to an artifact version and, where known, the deployment occurrence.
- **ConfigurationItem** — a control assertion ("this referenced subject is under configuration control"), with its own validity interval, declaring authority and CMDB mastership. It designates; it does not exist alongside its subject as a twin.
- **HostingRelation** — reified, effective-dated, source-qualified edge, never a derived join of current state.

Routing follows WM-XCT-039: desired state → Git/CI-CD; observed state → observability/discovery; CI designation and control scope → CMDB; commercial/physical facts → asset and finance masters. Exactly one master per fact path; unknown mastership is `pending` and blocks mutation.

## Environment/resource/instance/CI
Four different lifecycles, deliberately not collapsed. An environment is *commissioned and retired* by governance; a resource is *provisioned and released* by a provider; an instance is *started and terminated* by a scheduler; a CI designation is *asserted and withdrawn* by a control regime. `operational_status` belongs to each separately and must not be propagated upward. A healthy environment can contain failed instances; a retired environment can retain live CI designations pending decommission evidence.

## Hosting and topology
`HostingRelation` carries subject, host, relation kind (runs-on, member-of, backed-by, served-by), `validFrom`/`validTo`, assertion kind (declared / observed / inferred), confidence and `observed_at` with source. Topology is therefore a temporal graph; "what hosts X now" is a projection, not stored truth. Placement facts reported by WM-SFT-009 (`de-placement-regions`) are *per-occurrence outcomes* and must not accrete into environment inventory — that direction of drift is the specific leak to police.

## Ephemeral history
Ephemeral resources are handled by append-only records with closed intervals, never by deletion or identifier reuse. Rules: identifiers are minted once and retired with a tombstone retaining `instance_key`, artifact version reference, environment reference, `region`, interval and terminal status; a successor gets a new identity plus an explicit succession edge; short-lived instances anchor to durable parents (environment plus `service_scope`), so history survives even when every instance has turned over. Aggregate views may summarise generations, but the ledger, not the summary, answers historical impact. Absence of an observation is not absence of a resource.

## Asset boundary
They **reference**; they do not merge. Distinct masters (fixed-asset register versus CMDB/discovery), distinct lifecycles (capitalisation, depreciation, disposal versus commissioning, decommission), distinct granularity (one chassis asset ↔ many CIs; one logical-cluster CI ↔ many assets; leased or cloud resources have no owned asset at all). They *coincide referentially* only when a single owned physical unit is simultaneously capitalised and under configuration control — and even then two records persist, joined by an effective-dated co-designation link carrying identity evidence. Sharing one identifier imports finance disposal semantics into operations and would let a depreciated-but-running node vanish from the impact graph. Financial questions route to EM-FIN-05; EM-TEC-04 holds only the link and its evidence.

## Cluster/node
A logical cluster is a first-class `InfrastructureResource` (or environment, by `environment_kind`) with its own identity, declared `capacity` and `isolation_policy`. Nodes are members through effective-dated `HostingRelation` membership. Cluster identity never depends on the member set, so full node replacement is a membership change, not re-identification. Services depend on the cluster by *declaration* and on nodes by *observation*; both edges are kept, distinguished by assertion kind. A cluster must not be aliased to its control-plane endpoint or VIP.

## Scenario
Service S (WM-SFT-002) has environments `prod-eu` and `prod-us` (`region` differs, `service_scope` shared). A shared cluster C is referenced by both via `HostingRelation` — cross-region reference, not duplication. At T1 node N1 is a member and hosts instances I1..I3; at T2 N1 is retired and N2 joins; at T3 new instances I4..I6 run the same artifact version. Impact as-of T1 returns C, N1, I1..I3; as-of T3 returns C, N2, I4..I6; S's identity, and each environment's identity, are unchanged throughout. An incident at T1 stays attributable to N1 after retirement because the interval and tombstone survive. Where an edge is missing or stale the answer is *incomplete impact*, never *no impact*.

**Negative case rejected.** IP as sole eternal server identity fails on reassignment, DHCP, dual-stack, multi-homing, shared VIPs, overlay reuse and cross-tenant address recycling — the last producing a false merge across tenants. Address is an effective-dated observed endpoint binding, consistent with EM-TEC-03.

## Invariants
1. Every `DeployedInstance` references exactly one pinned artifact version.
2. Every observation carries `observed_at`, source and method; effective, observed and recording time stay separate.
3. Address or endpoint change never changes identity; identity change requires a new record plus a succession edge.
4. Every `HostingRelation` carries validity interval and assertion kind.
5. Identifiers are never recycled; retirement produces a tombstone, not a delete.
6. Environment and cluster identity are independent of member resources.
7. A CI designation and an asset record never share an identifier.
8. Desired and observed state are stored separately; discrepancies are retained.
9. Impact answers are as-of-time and carry a completeness boundary.
10. One environment per region-scoped context; environment identity is not service identity.

## Minimal completion shape
For the WM-SFT-010 specification: (1) identity and classification of environment, resource and instance; (2) inventory, `capacity` and `isolation_policy`; (3) effective-dated hosting and membership topology; (4) desired-versus-observed state with retained drift; (5) designation and asset-linkage layer (CI plus co-designation evidence); (6) history, retirement and tombstones; (7) mastership, projection and access, composed from WM-XCT-039; (8) alignment records (no conformance claims). Registry actions: deprecate the legacy WM-SFT-002 `environment` and `deployedSystem` objects with a migration mapping; promote the two candidate WM-SFT-009 relation rows; add the missing WM-SFT-010 ↔ WM-XCT-039 ledger row — it does not exist in the frozen relations and must not be assumed.

## Holds
WM-SFT-010 has no specification file, so every mapping here is a conceptual candidate on index and publication metadata only; the semantic crosswalk is unverified. WM-XCT-039 is a single-provider Codex-only reviewable draft with external review waived and executable validation deferred; WM-SFT-009 is a Claude-only reviewable draft with live source re-pin, ledger and coverage-downgrade holds; WM-SFT-002 is a described-previous-version record under migration boundary review. No fixtures were run. This review claims neither canonical completeness nor installability.


## Grok independent review
# EM-TEC-04 — Independent Grok Review

## Verdict

**Accept-with-conditions.** Completing reserved WM-SFT-010 as Runtime / Compute Environment is the right place-and-capacity boundary if WM-SFT-002 stays the logical system/application and WM-SFT-009 stays the deployment occurrence. WM-XCT-039 may be reused only for mastership assignment and impact projection. Two conditions are mandatory: DeployedInstance is not accepted as a first-class 010 gold-copy master; ConfigurationItem is not an independent subject identity. This is an independent boundary review of given codes. It is not a catalog and does not claim completeness. Reservation text for WM-SFT-010 was not available, so “complete reserved” is unverified.

## Identity / mastership

One durable subject has one master. 002 owns logical identity and is invariant under deploy, region, scale, and node replacement. 009 owns the placement act and its intended binding. 010 owns RuntimeEnvironment and InfrastructureResource identity. HostingRelation is a temporal fact, not a third system of record. 039 records which source is authoritative for which attribute slice and projects impact from those masters plus observed hosting; it must not mint or redefine 002/009/010 identity. Observed hosting and declared placement may disagree. Coincidence of name, address, or CI label is not identity merge.

## Environment / resource / instance / CI

RuntimeEnvironment is durable place or compute context, including a regional runtime. InfrastructureResource is allocatable operational capacity (node, pool, host slice), not a financial asset. DeployedInstance as proposed does not belong in 010 as a competing master. “Deployed” names a 009 result; “instance” is ambiguous among replica, environment-binding, and occurrence-result. Live replicas outnumber and outlive one occurrence (scale-out, restart, reschedule) without becoming a new 002 subject or, necessarily, a new 009 act. A thin dependent occupant record may sit with 010 for as-of hosting if and only if it is not a gold-copy master and is bound to a 009 occurrence and a 002 subject; minting authority should not default to 010. ConfigurationItem is an effective-dated control designation (owner, criticality, change window, audit scope) over a referenced 002, 009, or 010 subject. A designation-record surrogate key is allowed. That key is not a fourth identity for the designated thing. Withdrawing the designation must not destroy the subject.

## Hosting / topology

HostingRelation is the only temporal bind of occupant to environment or resource. Topology is derived from as-of hosting plus membership, not a separate master. Membership (node in cluster) and hosting (occupant on resource) are different intervals; the proposal names the latter and leaves the former implicit. Desired placement lives on 009; observed hosting lives on 010 relations. Neither silently overwrites the other. Multi-region is two environments, not one environment with a region attribute pretending to be topology. Allowed HostingRelation endpoints and subject classes are not given.

## Ephemeral history

Keys are never recycled. End of life is a tombstone, not a delete-and-reuse. As-of queries reconstruct occupancy from open and closed intervals plus tombstones. Addresses, hostnames, and IPs are time-stamped observations attached to a subject or relation; they are never identity. Recycled node names or addresses must not resurrect a closed subject. Retention bounds for tombstones are required policy and are not specified here.

## Asset boundary

Physical and financial assets remain in separate masters. 010 InfrastructureResource is a runtime view of capacity. Join asset to resource only by evidence (correlation, serial, provider resource identifier, effective dating, confidence). Do not collapse the asset register into the runtime model. Cloud capacity may have no asset; an asset may have no current runtime resource. Asset identity, resource identity, and CI designation remain distinct.

## Cluster / node

A logical cluster keeps identity while node membership changes. Membership rewrite is not identity rewrite. Node replacement closes the old membership and hosting intervals, issues a new non-recycled node key, tombstones or closes the old node record, and opens new intervals. Cluster identity is unchanged. The 002 service is unchanged.

## Scenario

One 002 service. Two 010 RuntimeEnvironments in two regions. One 009 occurrence per region placing the same logical service. One cluster identity per region. Occupants referenced from those occurrences are hosted on nodes in each environment. At T1, 039 as-of impact for the 002 subject includes the old node in the first region. That node is replaced: old key is not recycled; HostingRelation and membership close; new node key is issued; new relations open; cluster identity unchanged. At T2, impact for the same 002 subject no longer includes the old node and includes the new node. CI designations ride the 002 subject, and optionally the environment, not the replaced node. Addresses observed on the old and new nodes remain observations.

## Invariants

1. 002 identity is invariant under deploy, host, scale, region, and node replace.
2. 009 records an occurrence, not place/capacity and not automatically the replica.
3. 010 masters are place and capacity; keys are never recycled; tombstones stay as-of queryable.
4. HostingRelation is the sole temporal occupant-capacity bind; topology is derived.
5. Desired 009 placement and observed 010 hosting may diverge.
6. CI designates; designation-record key is not subject identity.
7. Asset identity is not InfrastructureResource identity; join by evidence only.
8. Address, hostname, and IP are observations, not identities.
9. Cluster identity survives node membership change.
10. 039 projects mastership and impact; it does not own 010 facts.
11. Region is not flattened into a single environment identity.

## Blockers

1. DeployedInstance semantics (replica vs environment-binding vs 009 result) and minting authority are unspecified; placement cannot close until named.
2. Cardinality from one 009 occurrence to N occupants and M resources is unspecified; this decides whether a separate occupant record is necessary.
3. Possible name collision if 009 already has an instance concept is unknown and is not invented here.
4. HostingRelation allowed endpoint types and subject classes are not given.
5. Cluster-membership versus hosting is not distinguished as temporal facts.
6. CI-eligible subject types for this boundary are not enumerated.
7. Asset-resource evidence contract is unspecified.
8. Reservation text for WM-SFT-010 is unavailable.
9. Region / environment / cluster / node identity stack is not stratified.
10. Tombstone retention policy is unspecified; as-of history is otherwise unbounded.
11. Instance key authority (orchestrator identifier versus registry) is unassigned, with recycle risk.
12. Mastership of observed versus declared hosting is unspecified, so 039 cannot project an authoritative slice.

## Challenges

DeployedInstance does not belong in WM-SFT-010 as a first-class owned master. ConfigurationItem does not need independent subject identity.
