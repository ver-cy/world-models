You are the sole frozen independent semantic auditor for EM-TEC-03. Use no tools. Review the reconciled artifacts below for identity, lifecycle, ownership, relation direction, temporal rules, privacy, negative cases, and accidental new IDs. Return: verdict; blocking defects; non-blocking defects; exact remediation; required fixtures; publication disposition. Do not invent registry allocations.


## Claude study
# EM-TEC-03 — Interface, API and Integration

## Verdict
**Reuse/extend, with one gap.** Complete reserved **WM-SFT-003 API / Interface** as the versioned *logical* interface contract; do not mint `InterfaceContract` or `APIVersion` as new types — `APIVersion` is a revision designation of WM-SFT-003, not an entity. **EndpointBinding** stays *inside* WM-SFT-003 as a dependent, effective-dated link to **WM-SFT-018**; it gets no independent identity. **Integration** does **not** belong inside the contract: it needs its own identity, owner and lifecycle, and the dossier holds no reservation for it — the registry must issue one; I will not invent an id. **ExchangeEvent** is rejected as a type: an exchange occurrence is **WM-ACT-015** (undirected) or **WM-REC-003** (addressed, delivery obligation), carrying references to revision, binding and integration. **WM-DAT-004** keeps payload semantics/constraints; **WM-SFT-018** keeps logical connectivity/address/exposure. Boundary decision for the contour: reuse/extend, not new.

## Evidence
- Reservation `vr.wm-sft-003` states the purpose exactly as required — "a versioned machine or human interface contract with independent provider-consumer lifecycle" — and carries `validation_flags: KEEP-STANDALONE: API contract has independent version, owner and consumers`, `review_state: first-pass-reviewed`. `missing_specs` records only the absent spec file, not a rejected boundary.
- `prior_adjudication.EM-TEC-01`: "Complete WM-SFT-003 as the independent API / Interface contract after its missing specification is written." EM-TEC-02: keep logical system, product, runtime and deployment identities separate — the same separation applied here to contract vs binding.
- WM-DAT-004 boundary note (API/interface, OpenAPI/AsyncAPI): "Interface contracts own operations, transport, endpoints and status codes. This model owns payload structure and meaning. The overlap is the message payload schema, which should be defined once here and referenced by the interface model rather than duplicated." Its composition entry to the interface model is `ALIGN`, not merge.
- Binding precedent: WM-DAT-004 `af-binding-descriptor` identity = "contract identifier plus environment identifier from the infrastructure system of record" — a dependent key, not an independent one.
- Consumer-pin precedent: `de-consumer-registration` / `af-consumer-register` — "a consumer registered against a specific contract version, with role and effective period… used to drive impact assessment and notification".
- WM-REC-003 boundary note (event/activity): "An event becomes in-scope only when it is transported as an addressed message." WM-ACT-015 boundary note (CloudEvents): envelope `id/source/type/time` are "a projection of this model's identity, typing and event-time semantics, not additional semantics."
- Declaration vs measurement is already settled twice (WM-DAT-004 policy; its adjudication "Declaration versus measurement boundary… retained from base, reinforced by Grok").

## Identity/mastership
| Thing | Identity | Master (candidate) |
|---|---|---|
| Logical contract | WM-SFT-003 contract id | software catalogue / contract registry |
| Contract revision | contract id **+** version designation | Git / CI-CD |
| Consumer pin | consumer party **+** contract id **+** revision | contract registry |
| Integration | own id (**unreserved**) | service/integration register |
| Endpoint binding | contract id **+** revision **+** WM-SFT-018 endpoint **+** environment **+** period | CMDB / deployment |
| Exchange occurrence | WM-ACT-015 / WM-REC-003 identity rules | observability / message store |
| Data schema | WM-DAT-004 | data steward |
| Transport/address | WM-SFT-018 | service owner |
A version, a URL, a date or a fingerprint is never identity on its own.

## Contract/version/consumer pin
Contract = stable logical surface (owner, purpose, declared specification/dialect, status, compatibility mode, operation and error vocabulary, auth scheme *declared* only). Revision = immutable published designation under a declared scheme; a correction is a new revision, never an edit. Consumer pin = a consumer bound to **exactly one** revision with role and effective period; resolving a contract without a revision must return and state the revision resolved. Pins, not addresses, drive impact assessment, notice and sunset.

## Integration
A governed producer–consumer relationship: parties, purpose, `flow_direction`, `delivery_semantics`, `freshness_target`, owners, data scope (by reference to WM-DAT-004 — never a copied dataset). It composes contract revisions, consumer pins and endpoint bindings; it survives every revision and every address change. This is why it cannot live inside the contract: one contract has many consumers, and one integration may span several contracts and directions. Its identity is a registry gap, not a modelling choice.

## Endpoint binding
Dependent link: revision × WM-SFT-018 endpoint × environment × effective period, plus protocol and media type. Mastered outside the contract registry (CMDB/deployment), so it changes on its own cadence. No credentials or secrets are held here — referenced indirectly only. Multiple concurrent bindings per revision are normal (environments); a binding never re-versions the contract.

## Message/event/exchange
No new type. An exchange occurrence is: **WM-REC-003 Message** when addressed to identified recipients with delivery obligation, status and disposition evidence; otherwise **WM-ACT-015 Occurrence** (envelope attributes are a projection). EM-TEC-03 contributes only a correlation facet — inline references from the occurrence to `contract revision`, `endpoint binding`, `integration` and validating `schema` — plus `mapping_ref`, which belongs to WM-DAT-004 transform/projection, not here. Observed freshness, latency and delivery counts are measurement and belong to the observation sibling; the contract holds the declared target.

## Compatibility and migration
Inherit WM-DAT-004's evolution layer verbatim: declared mode recorded **on the revision** (backward / forward / full, transitive variants, none); backward ⇒ consumers upgrade first, forward ⇒ producers first; transitive checks the recorded version range. Breaking regardless of any syntactic pass: removing a required element or operation, narrowing a type outside the permitted promotion set, adding an element required on read without a default, changing the meaning of an existing element without renaming. Each candidate revision carries a compatibility check record or a recorded, expiring exception; each publication carries impact assessment against registered pins, a notice period, and on retirement a deprecation notice with sunset instant and successor.

## Invariants
1. An endpoint binding has exactly one environment and one effective period.
2. An address change alone never increments the contract revision.
3. A revision change alone never requires a new binding unless the revision is encoded in the address — then the binding change is a consequence, not a cause.
4. Integration identity is invariant under revision and binding change.
5. A consumer pin names exactly one revision; unpinned resolution must report the revision used.
6. Payload is defined once in WM-DAT-004 and referenced; the integration duplicates no dataset or schema.
7. A published revision is immutable.
8. No revision is published without an owner, a declared compatibility mode and a resolvable schema reference.
9. An exchange occurrence references revision, binding and integration; it never bears contract identity.
10. Syntactic compatibility pass is necessary, never sufficient.

## Scenarios
**Endpoint URL changes, contract unchanged.** New binding revision with effective period; prior binding deprecated with sunset. Contract revision, schema, pins and integration identity all unchanged; no compatibility check; notice scoped to consumers bound in that environment. The negative case — "a new URL is a new business integration" — is refused by invariants 2 and 4.

**Incompatible payload change, URL unchanged.** Major revision of the contract, with compatibility check record, impact assessment against pins, notice period, deprecation of the prior revision with successor reference; each consumer re-pins; schema change is mastered in WM-DAT-004 but the migration is driven by the contract revision. Binding unchanged. Different action set, different owner, different clock — the acceptance scenario holds.

## Minimal completion shape
WM-SFT-003 needs six areas: (1) contract identity and governance; (2) interface surface — operations/resources/channels, parameters, error vocabulary, declared auth, payload `REFERENCE` WM-DAT-004; (3) revision series and compatibility; (4) consumption — pins, obligations, declared service levels including `freshness_target`; (5) binding and exposure — `REFERENCE` WM-SFT-018 with environment and period; (6) exchange correlation — `REFERENCE` WM-ACT-015 / WM-REC-003, observation excluded. Relations: WM-SFT-003 `REFERENCE` WM-DAT-004; WM-SFT-003 `REFERENCE` WM-SFT-018; Integration `COMPOSE` WM-SFT-003 once its id exists.

## Holds
Not canonically complete and not installable. Outstanding: WM-SFT-003 and WM-SFT-018 have no specification files; Integration has no reserved registry id; operation-level compatibility rests only on WM-DAT-004's secondhand OpenAPI citation, so the interface-surface ladder is a gap; WM-DAT-004's own publication holds (ODCS repinning, `dataProduct` status) are inherited by anything referencing it; comparison tracks (ArchiMate, CSDM runtime instance, OpenTelemetry) are unexamined; all `candidate_properties_from_v1` remain candidate-not-normative; fixtures and immutable-ref checks have not been run; the contour's `boundary_decision` stays pending until the two specs exist.


## Grok study
# Grok frozen study — EM-TEC-03

Source conversation: https://grok.com/c/8ccdbc77-f5a5-4d9a-895e-c61c8bfc2e33?rid=abe0c6a7-7b9c-40f2-a759-bd3eacc76ec9

Verdict: ACCEPT WITH CONDITIONS.

Complete reserved WM-SFT-003 as a versioned logical Interface Contract. A published API version is an immutable contract revision. WM-DAT-004 owns payload semantics; WM-SFT-018 owns endpoint/address exposure. Model a stable contract family root with immutable revision children and state this choice explicitly.

Split the former EndpointBinding into two dependent relations: (1) Exposure binds a contract revision or family to an endpoint, environment, and effective interval; (2) ConsumptionRouting binds an Integration to an exposure, environment, role, and effective interval. ContractPin is a dependent, effective-dated relation to one exact revision. `latest` is query behavior only. Dual run uses overlapping, explicitly scoped pin rows.

Integration remains identifier-unassigned. It requires independent continuity, but the candidate grain and natural key remain unresolved. A possible key is producer, consumer, interface family or capability, and purpose discriminator. One provider with many subscribers uses one Integration per subscriber. Consumer replatforming may preserve or replace Integration depending on the final key. Do not invent a successor relation. Exclude test harnesses, intra-component calls, probes, and other ephemeral call paths.

Changing a URL does not change contract or Integration identity. An incompatible payload change at the same URL creates a new contract revision and WM-DAT-004 schema revision; the endpoint may remain. Do not create ExchangeEvent: addressed exchanges use WM-REC-003 Message; other occurrences use WM-ACT-015. A Message interprets against at most one exact revision.

Every published semantic change creates a revision with compatibility assessment, impacted pins, notice, and sunset or successor handling. Retired revisions accept no new pins but remain resolvable for historical messages. Shared gateways may expose many contracts. Blue/green and DR are explicit concurrent scoped relations.

Invariants: published revisions are immutable; address is not contract identity; revision is not Integration identity; Integration continuity survives revision and URL change; every dependent binding has parent, endpoint or exposure, environment, and effective interval; overlap is explicit; bindings cannot change meaning; pins name exact revisions; each message names at most one revision; payload semantics remain in WM-DAT-004; not every call path is an Integration; reserved codes remain reserved.

Open holds: WM-SFT-018 endpoint identity and address-change semantics must be explicit; Integration grain/type/purpose/collision rules remain unallocated; environment is an external master; contract-to-WM-DAT-004 cardinality must be stated; pub/sub and multicast must be covered by fixtures.


## Provider comparison
# Provider comparison — EM-TEC-03

Claude and Grok agree that WM-SFT-003 should be completed rather than replaced, WM-SFT-018 owns endpoint identity, WM-DAT-004 owns payload semantics, Integration has independent continuity but must remain identifier-unassigned, and no ExchangeEvent model should be introduced.

The reconciled design uses a stable InterfaceContract root with immutable ContractRevision children. It separates contract Exposure from Integration-specific ConsumptionRouting, pins every consumer to an exact revision, preserves historical messages after retirement, and keeps address changes independent of semantic revisions. WM-SFT-018 uses stable endpoint identity with effective-dated address and exposure records.

Grok adds conditions that were under-specified locally: explicit family/revision choice; separate exposure and routing relations; pub/sub per subscriber; exclusion of ephemeral call paths; exact one-revision message interpretation; explicit concurrency; contract-to-schema cardinality; and Integration collision rules. Those conditions are frozen for the audit and remediation.


## WM-SFT-003 candidate
{
  "format": "vercy-world-model-candidate/v1",
  "contourId": "EM-TEC-03",
  "modelId": "WM-SFT-003",
  "registryId": "vr.wm-sft-003",
  "name": "API / Interface Contract",
  "version": "0.1.0-candidate.1",
  "entryKind": "contract-aggregate",
  "status": "research-candidate",
  "canonicalPublishable": false,
  "purpose": "Represent a stable logical interface identity, immutable contract revisions, exact consumer pins, compatibility evidence and effective-dated endpoint bindings without owning payload schema, network endpoint or exchange occurrence identity.",
  "boundary": {
    "owns": [
      "logical interface-contract family identity",
      "immutable published contract revisions and compatibility mode",
      "operations message shapes and semantic references at the interface boundary",
      "consumer-to-revision pins and effective periods",
      "compatibility assessments exceptions and migration notices",
      "effective-dated endpoint bindings between revision endpoint and environment"
    ],
    "delegates": [
      "payload meaning and constraints to WM-DAT-004",
      "network address exposure and endpoint lifecycle to WM-SFT-018",
      "addressed exchange records to WM-REC-003",
      "non-addressed exchange occurrences to WM-ACT-015",
      "governed producer-consumer Integration identity to an identifier-unassigned candidate"
    ],
    "excludes": [
      "payload schema mastership",
      "network endpoint or runtime health state",
      "message or event occurrence lifecycle",
      "automatic integration identity",
      "compatibility claims based on syntax alone",
      "wildcard standards conformance"
    ]
  },
  "objects": {
    "InterfaceContract": {
      "identity": [
        "contractId"
      ],
      "required": [
        "name",
        "purpose",
        "ownerRef",
        "providerRole",
        "consumerScope",
        "status"
      ],
      "optional": [
        "supersedesContractId"
      ],
      "lifecycle": [
        "draft",
        "active",
        "deprecated",
        "retired"
      ]
    },
    "ContractRevision": {
      "identity": [
        "contractId",
        "revision"
      ],
      "required": [
        "publishedAt",
        "compatibilityMode",
        "operationSet",
        "schemaRefs",
        "contentDigest",
        "status"
      ],
      "optional": [
        "supersedesRevision",
        "successorRef",
        "sunsetAt"
      ],
      "lifecycle": [
        "draft",
        "published",
        "deprecated",
        "retired"
      ]
    },
    "ConsumerPin": {
      "identity": [
        "consumerPinId"
      ],
      "required": [
        "consumerRef",
        "contractRevisionRef",
        "effectiveFrom",
        "authorityRef",
        "status"
      ],
      "optional": [
        "effectiveTo",
        "resolutionPolicy",
        "migrationTargetRef"
      ],
      "lifecycle": [
        "proposed",
        "effective",
        "superseded",
        "withdrawn"
      ]
    },
    "EndpointBinding": {
      "identity": [
        "bindingId"
      ],
      "required": [
        "contractRevisionRef",
        "endpointRef",
        "environmentRef",
        "validFrom",
        "authorityRef",
        "status"
      ],
      "optional": [
        "validTo",
        "integrationRef",
        "bindingMetadata",
        "withdrawalReason"
      ],
      "lifecycle": [
        "proposed",
        "effective",
        "superseded",
        "withdrawn"
      ]
    },
    "CompatibilityAssessment": {
      "identity": [
        "assessmentId"
      ],
      "required": [
        "candidateRevisionRef",
        "baselineRange",
        "declaredMode",
        "checks",
        "result",
        "evidenceRefs",
        "assessedAt"
      ],
      "optional": [
        "exceptionRef",
        "impactAnalysisRef",
        "noticeRequirements"
      ]
    }
  },
  "compatibilityRules": [
    "Removing an operation or required element is breaking unless the declared mode explicitly allows it.",
    "Narrowing a type outside an allowed promotion is breaking.",
    "Adding a read-required element without a compatible default is breaking.",
    "Changing established meaning is breaking even when syntax validates.",
    "Every compatibility conclusion states the baseline range and evidence used."
  ],
  "relations": [
    {
      "target": "WM-DAT-004",
      "relation": "REFERENCE",
      "required": true,
      "purpose": "Resolve immutable payload schema and data-contract revisions."
    },
    {
      "target": "WM-SFT-018",
      "relation": "REFERENCE",
      "required": true,
      "purpose": "Resolve endpoint address exposure and network lifecycle through EndpointBinding."
    },
    {
      "target": "WM-REC-003",
      "relation": "REFERENCE",
      "required": false,
      "purpose": "Resolve addressed message exchange records."
    },
    {
      "target": "WM-ACT-015",
      "relation": "REFERENCE",
      "required": false,
      "purpose": "Resolve non-addressed exchange occurrences and correlation evidence."
    }
  ],
  "operations": [
    {
      "id": "publish-revision",
      "effect": "Issue an immutable contract revision with schema pins and compatibility mode.",
      "authority": "interface owner"
    },
    {
      "id": "assess-compatibility",
      "effect": "Record a bounded assessment against an explicit historical revision range.",
      "authority": "authorized reviewer"
    },
    {
      "id": "pin-consumer",
      "effect": "Bind one consumer to exactly one revision for an effective period.",
      "authority": "consumer owner"
    },
    {
      "id": "rebind-endpoint",
      "effect": "Issue a new binding without changing logical contract identity.",
      "authority": "interface owner"
    },
    {
      "id": "deprecate-revision",
      "effect": "Announce successor notice and sunset while preserving the revision.",
      "authority": "interface owner"
    },
    {
      "id": "retire-revision",
      "effect": "End new use after impact and notice requirements are satisfied.",
      "authority": "interface owner"
    }
  ],
  "invariants": [
    "A logical interface contract and each published revision have distinct stable identities.",
    "Published contract revisions are immutable and content-addressed.",
    "Every consumer pin resolves exactly one immutable contract revision.",
    "Unpinned resolution records the exact revision selected at use time.",
    "Every endpoint binding names one endpoint, one environment and one effective period.",
    "Changing an address or endpoint binding alone does not increment contract revision.",
    "Changing contract semantics alone does not require an endpoint change.",
    "Payload schema is defined once in WM-DAT-004 and referenced by immutable revision.",
    "A syntactic compatibility pass is necessary but insufficient.",
    "Every compatibility result declares baseline range, mode, evidence and bounded exceptions.",
    "Breaking changes require impact analysis against consumer pins plus successor or sunset notice.",
    "Exchange occurrences reference contract revision and binding without replacing their identities.",
    "Contract revision or binding changes never silently create a new Integration identity.",
    "Retired revisions and bindings remain resolvable for historical exchange evidence.",
    "Access to exchange metadata cannot exceed access to its payload or endpoint evidence."
  ],
  "holds": [
    "Exact Grok review and provider reconciliation are pending.",
    "One frozen no-tools semantic audit of the reconciled candidate is pending.",
    "WM-SFT-018 remains a reservation-only endpoint boundary.",
    "Integration remains identifier-unassigned pending registry allocation.",
    "WM-DAT-004 retains its own canonical publication holds.",
    "Package conversion and live HTTP/runtime/search/package verification are pending."
  ]
}


## WM-SFT-003 fixtures
{
  "format": "vercy-world-model-fixtures/v1",
  "modelId": "WM-SFT-003",
  "version": "0.1.0-candidate.1",
  "cases": [
    {
      "id": "url-change-only",
      "kind": "positive",
      "input": "The API URL changes while operations payload meaning and compatibility mode remain unchanged.",
      "expect": "Create a successor EndpointBinding; keep contract revision consumer pins and Integration identity."
    },
    {
      "id": "semantic-change-same-url",
      "kind": "positive",
      "input": "Payload meaning changes incompatibly at the same URL.",
      "expect": "Publish a new contract and WM-DAT-004 schema revision with impact and migration evidence; endpoint binding may remain."
    },
    {
      "id": "removed-operation",
      "kind": "negative",
      "input": "A published revision removes an operation used by pinned consumers.",
      "expect": "Compatibility assessment is breaking and retirement requires impact and notice handling."
    },
    {
      "id": "required-field-without-default",
      "kind": "negative",
      "input": "A read-required payload field is added with no compatible default.",
      "expect": "Assessment is breaking despite syntactic validity."
    },
    {
      "id": "consumer-unpinned",
      "kind": "negative",
      "input": "A consumer resolves latest with no stored selected revision.",
      "expect": "Exchange is not reproducible; selected revision must be recorded."
    },
    {
      "id": "historical-exchange",
      "kind": "positive",
      "input": "A retired revision and endpoint binding are referenced by an old message.",
      "expect": "Both remain resolvable and immutable for historical evidence."
    },
    {
      "id": "restricted-payload",
      "kind": "negative",
      "input": "Interface metadata is broadly visible but the payload schema is restricted.",
      "expect": "Projection preserves the stricter payload evidence ceiling."
    }
  ]
}


## WM-SFT-018 candidate
{
  "format": "vercy-world-model-candidate/v1",
  "contourId": "EM-TEC-03",
  "modelId": "WM-SFT-018",
  "registryId": "vr.wm-sft-018",
  "name": "Network / Endpoint",
  "version": "0.1.0-candidate.1",
  "entryKind": "network-endpoint-aggregate",
  "status": "research-candidate",
  "canonicalPublishable": false,
  "purpose": "Represent stable logical network endpoint identity, effective-dated address bindings, connectivity and exposure assertions without owning software-system, runtime-resource, interface-contract or traffic-observation identity.",
  "boundary": {
    "owns": [
      "logical network-endpoint identity and lifecycle",
      "effective-dated address and name bindings",
      "effective-dated connectivity relations",
      "declared network exposure and reachability assertions",
      "network-zone or segment membership assertions",
      "successor and tombstone history for retired endpoints"
    ],
    "delegates": [
      "logical software-system identity to WM-SFT-002",
      "runtime environment and infrastructure-resource identity to WM-SFT-010",
      "logical API/interface contract and endpoint binding to WM-SFT-003",
      "observed telemetry and operational signals to WM-SFT-017"
    ],
    "excludes": [
      "credentials secrets or private key material",
      "software-system or deployed-instance mastership",
      "API schema and compatibility semantics",
      "packet flow or telemetry occurrence lifecycle",
      "IP address hostname or URL as eternal identity",
      "unbounded claims of actual reachability"
    ]
  },
  "objects": {
    "NetworkEndpoint": {
      "identity": [
        "endpointId"
      ],
      "required": [
        "name",
        "endpointKind",
        "ownerRef",
        "status"
      ],
      "optional": [
        "logicalServiceRef",
        "successorEndpointId",
        "retiredAt"
      ],
      "lifecycle": [
        "planned",
        "active",
        "restricted",
        "retired"
      ]
    },
    "AddressBinding": {
      "identity": [
        "addressBindingId"
      ],
      "required": [
        "endpointRef",
        "addressKind",
        "addressValue",
        "validFrom",
        "authorityRef",
        "status"
      ],
      "optional": [
        "validTo",
        "environmentRef",
        "resolutionEvidenceRef"
      ],
      "lifecycle": [
        "proposed",
        "effective",
        "superseded",
        "withdrawn"
      ]
    },
    "ConnectivityRelation": {
      "identity": [
        "connectivityRelationId"
      ],
      "required": [
        "sourceEndpointRef",
        "targetEndpointRef",
        "protocol",
        "validFrom",
        "authorityRef",
        "status"
      ],
      "optional": [
        "validTo",
        "portOrChannel",
        "direction",
        "evidenceRefs"
      ],
      "lifecycle": [
        "declared",
        "effective",
        "superseded",
        "withdrawn"
      ]
    },
    "ExposureAssertion": {
      "identity": [
        "exposureAssertionId"
      ],
      "required": [
        "endpointRef",
        "audienceScope",
        "accessMode",
        "effectiveFrom",
        "authorityRef",
        "status"
      ],
      "optional": [
        "effectiveTo",
        "policyRef",
        "evidenceRefs",
        "confidence"
      ],
      "lifecycle": [
        "declared",
        "effective",
        "superseded",
        "withdrawn"
      ]
    },
    "ZoneMembership": {
      "identity": [
        "zoneMembershipId"
      ],
      "required": [
        "endpointRef",
        "zoneRef",
        "validFrom",
        "authorityRef",
        "status"
      ],
      "optional": [
        "validTo",
        "evidenceRefs"
      ],
      "lifecycle": [
        "asserted",
        "effective",
        "superseded",
        "withdrawn"
      ]
    }
  },
  "relations": [
    {
      "target": "WM-SFT-002",
      "relation": "REFERENCE",
      "required": false,
      "purpose": "Resolve the logical software system or service exposed by the endpoint."
    },
    {
      "target": "WM-SFT-010",
      "relation": "REFERENCE",
      "required": false,
      "purpose": "Resolve the runtime environment or infrastructure resource hosting the endpoint."
    },
    {
      "target": "WM-SFT-003",
      "relation": "REFERENCE",
      "required": false,
      "purpose": "Resolve interface contracts and their effective endpoint bindings."
    },
    {
      "target": "WM-SFT-017",
      "relation": "REFERENCE",
      "required": false,
      "purpose": "Resolve observed traffic health and reachability evidence without copying telemetry."
    }
  ],
  "operations": [
    {
      "id": "register-endpoint",
      "effect": "Mint a stable endpoint identity independent of current address or host.",
      "authority": "network or service owner"
    },
    {
      "id": "bind-address",
      "effect": "Append an effective-dated name address or URL binding.",
      "authority": "authoritative address registrar"
    },
    {
      "id": "assert-connectivity",
      "effect": "Append a bounded directional connectivity relation.",
      "authority": "network control authority"
    },
    {
      "id": "assert-exposure",
      "effect": "Declare intended audience and access mode with policy evidence.",
      "authority": "service and security owner"
    },
    {
      "id": "retire-endpoint",
      "effect": "Close current assertions and retain tombstone and successor references.",
      "authority": "endpoint owner"
    }
  ],
  "invariants": [
    "Endpoint identity is independent of IP address hostname URL port and runtime resource identity.",
    "An address binding has one bounded validity interval and one authoritative source.",
    "Reassigning an address never reuses or merges endpoint identity.",
    "Concurrent address bindings are permitted only when their scopes or environments are explicit.",
    "Connectivity relations are directional unless explicitly declared bidirectional.",
    "Every connectivity relation identifies source target protocol authority and validity period.",
    "Declared connectivity does not prove observed traffic or current reachability.",
    "Exposure assertions state audience access mode authority and effective period.",
    "Secrets credentials and private keys are referenced indirectly and never stored in this aggregate.",
    "Runtime resource replacement does not change endpoint identity when the logical exposure remains continuous.",
    "Interface contract revision changes do not change endpoint identity.",
    "Endpoint address changes do not change interface contract revision.",
    "Retired endpoints retain tombstones and successor evidence.",
    "Historical resolution uses the binding valid at the requested time.",
    "Access to endpoint and exposure metadata cannot exceed the governing policy and evidence rights."
  ],
  "holds": [
    "Exact Grok review and provider reconciliation are pending.",
    "One frozen no-tools semantic audit of the reconciled candidate is pending.",
    "WM-SFT-017 retains its own specification and publication holds.",
    "Integration remains identifier-unassigned in EM-TEC-03.",
    "Package conversion and live HTTP/runtime/search/package verification are pending."
  ]
}


## WM-SFT-018 fixtures
{
  "format": "vercy-world-model-fixtures/v1",
  "modelId": "WM-SFT-018",
  "version": "0.1.0-candidate.1",
  "cases": [
    {
      "id": "address-reassignment",
      "kind": "negative",
      "input": "IP A moves from endpoint E1 to E2 at T2.",
      "expect": "E1 and E2 remain distinct; two non-overlapping bindings preserve history."
    },
    {
      "id": "blue-green",
      "kind": "positive",
      "input": "One logical endpoint exposes blue and green runtime resources during migration.",
      "expect": "Endpoint identity remains stable while scoped bindings overlap explicitly."
    },
    {
      "id": "contract-revision",
      "kind": "positive",
      "input": "API contract advances from R1 to R2 at the same URL.",
      "expect": "Contract pin changes; endpoint and address binding remain stable."
    },
    {
      "id": "url-change",
      "kind": "positive",
      "input": "An API URL changes without semantic contract change.",
      "expect": "A new address binding supersedes the old one; contract revision is unchanged."
    },
    {
      "id": "declared-not-observed",
      "kind": "negative",
      "input": "A declared route has no current telemetry.",
      "expect": "Connectivity remains declared with observation status unknown, not asserted reachable."
    },
    {
      "id": "secret-leak",
      "kind": "negative",
      "input": "A credential value is offered as endpoint metadata.",
      "expect": "Reject secret material and retain only an indirect governed reference."
    },
    {
      "id": "retired-resolution",
      "kind": "positive",
      "input": "Resolve an endpoint address before and after retirement.",
      "expect": "Historical lookup returns the then-valid binding; current lookup returns retired state and successor."
    }
  ]
}
