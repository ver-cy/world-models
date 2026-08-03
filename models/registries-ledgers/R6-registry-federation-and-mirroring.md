# R6 Registry Federation & Mirroring

The reference-not-copy fabric between registers: which register is authoritative for what, how entries in one register point into another, and under what freshness and drift rules derived mirrors may exist at all. It is its own meta-model because inter-register topology, authority precedence and mirror hygiene are concerns of the federation as a whole, owned jointly by registrars, and belong to no single register.

## Manifest

```yaml
muif:
  version: "1.0"
metaModel:
  id: "vercy:world:r6"
  csn: world.registryFederationAndMirroring
  version: 0.2.0
  displayName: "Registry Federation & Mirroring"
  description: "Authority, cross-reference and mirroring rules that connect independent registers without copying their content."
conformance:
  muc: "2.0: Conformant"
  mmas: A1
namespaces:
  - world.registryFederationAndMirroring
bundles:
  - csn: world.registryFederationAndMirroring.authority
    displayName: "Authority"
    layers:
      - world.registryFederationAndMirroring.authority.authorityScope
      - world.registryFederationAndMirroring.authority.precedence
  - csn: world.registryFederationAndMirroring.linkage
    displayName: "Linkage"
    layers:
      - world.registryFederationAndMirroring.linkage.referenceRules
      - world.registryFederationAndMirroring.linkage.resolutionRouting
  - csn: world.registryFederationAndMirroring.mirroring
    displayName: "Mirroring"
    layers:
      - world.registryFederationAndMirroring.mirroring.mirrorProvisioning
      - world.registryFederationAndMirroring.mirroring.freshnessAndDrift
imports:
  - source: mu-arch-018
    version: "*"
  - source: mufp
    version: "*"
```

## Bundles and layers

| Bundle | Responsibility | Layers |
|---|---|---|
| `authority` | Who is authoritative for which facts | `authorityScope`: declared subject domains per register, no overlaps unresolved Â· `precedence`: which register wins when declarations collide, and how conflicts are settled |
| `linkage` | Pointing instead of copying | `referenceRules`: what a cross-register reference must carry to stay resolvable Â· `resolutionRouting`: where a consumer resolves a given reference, including fallbacks |
| `mirroring` | Derived copies under discipline | `mirrorProvisioning`: when a mirror may exist, its scope and its marking as non-authoritative Â· `freshnessAndDrift`: staleness budgets, drift detection and reconciliation duties |

## Objects

- `federationLink`: an established relationship between two registers; key attributes: memberRegisters, agreementRef, status
- `authorityDeclaration`: a register's declared authority over a subject domain; key attributes: registerRef, domainScope, declaredAt
- `crossReference`: a resolvable pointer from an entry in one register to an entry in another; key attributes: sourceEntryRef, targetRegisterRef, targetEntryRef, referenceKind
- `resolutionRoute`: the path by which a class of references is resolved; key attributes: targetRegisterRef, endpoint, fallbackRoute
- `mirror`: a marked, non-authoritative derived copy of register content; key attributes: sourceRegisterRef, scope, provisionedAt, freshnessPolicyRef
- `freshnessPolicy`: the staleness budget a mirror must respect; key attributes: maxLag, refreshCadence, expiryBehavior
- `driftReport`: a recorded comparison of a mirror against its source; key attributes: comparedAt, divergences, resolutionState

## Relationships

- `federationLink` -> connects -> `world.registry` registers (many-to-many): the federation is a graph of pattern-R1 registers
- `authorityDeclaration` -> assignsAuthorityTo -> register (many-to-one): each declaration names exactly one authoritative register for its scope
- `crossReference` -> resolvesVia -> `resolutionRoute` (many-to-one): references of a class share a declared route
- `mirror` -> mirrors -> register (many-to-one): every mirror names its single authoritative source
- `mirror` -> governedBy -> `freshnessPolicy` (many-to-one): no mirror exists without a staleness budget
- `driftReport` -> compares -> `mirror` (many-to-one): drift checks accumulate over a mirror's life

## Events

- `federationEstablished`: two registrars concluded an agreement and linked their registers
- `authorityDeclared`: a register's authoritative scope was declared or adjusted within the federation
- `mirrorProvisioned`: a derived copy was created under a freshness policy and marked non-authoritative
- `mirrorRefreshed`: a mirror was brought up to date from its source
- `driftDetected`: comparison found a mirror diverging from its source beyond tolerance
- `driftReconciled`: a detected divergence was resolved in favor of the authoritative source
- `federationSuspended`: a link was taken out of service and its routes disabled

## Contracts

- `federationAgreement`: the registrars' mutual terms for linking registers, declaring authority and honoring references
- `mirrorProvisionContract`: the conditions under which a consumer may hold a mirror, including scope, marking and refresh duties
- `freshnessServiceLevelContract`: the staleness budget and refresh guarantees for a mirror class
- `resolutionServiceContract`: terms of the reference resolution service offered to federation consumers

## Projections

- `federationMapView`: the topology of registers, links and authority scopes; omits all entry-level content
- `mirrorHealthView`: lag, last refresh and open drift per mirror; omits mirrored content itself
- `consumerResolutionView`: where to resolve which reference class; omits agreement terms and internal routes

## Composition

- REFERENCE `world.registry` (R1): every federated endpoint is a register of the pattern, and authority scopes are expressed over its entry domains
- COMPOSE `world.eventRegister` (R3): mirrors refresh by replaying source event logs, and drift checks compare against sealed checkpoints
- REFERENCE `world.identityRegister` (R4): registrar parties to agreements resolve to anchored identities
- REFERENCE `world.mandate` (A12): a registrar's capacity to enter federation agreements derives from its mandate
- MIX-IN `world.audit` (S4): provisioning, refresh and reconciliation acts carry the audit facet
- imports: mu-arch-018 (ALIGN): the reference-not-copy doctrine this model operationalizes
- imports: mufp (ALIGN): federation exchange semantics for resolution and synchronization

## Stewardship

Ownership is joint: the registrars party to each federation link own the link, its declarations and its routes, while each mirrored fact remains owned by its authoritative source register. Access to routes, mirrors and drift data is granted via the S1/S2 access and consent models and audited via S4.
