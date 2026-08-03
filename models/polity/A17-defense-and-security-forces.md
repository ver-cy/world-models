# A17 Defense & Security Forces

This meta-model is a breadth placeholder describing a polity's forces: their units and command lines, references to the assets they hold, the legal mandates under which they exist and may deploy, and coarse readiness states. It is deliberately shallow: operational depth, plans and engagements live in the dedicated operations model (G3). It is its own model because even a placeholder must anchor the catalogue's references to forces and their mandates, and because it carries the most restrictive default access in the catalogue.

## Manifest

```yaml
muif:
  version: "1.0"
metaModel:
  id: "vercy:world:a17"
  csn: world.defenseForces
  version: 0.2.0
  displayName: Defense & Security Forces
  description: Forces, units, mandates, asset references and coarse readiness, as a breadth placeholder.
conformance:
  muc: "2.0: Conformant"
  mmas: A1
namespaces:
  - world.defenseForces
bundles:
  - csn: world.defenseForces.forceStructure
    displayName: Force structure
    layers:
      - world.defenseForces.forceStructure.unit
      - world.defenseForces.forceStructure.command
  - csn: world.defenseForces.assetsAndReadiness
    displayName: Assets and readiness
    layers:
      - world.defenseForces.assetsAndReadiness.assetReference
      - world.defenseForces.assetsAndReadiness.readiness
  - csn: world.defenseForces.mandate
    displayName: Mandate
    layers:
      - world.defenseForces.mandate.legalMandate
      - world.defenseForces.mandate.deploymentAuthorization
imports:
  - source: nato-standards
    version: "*"
```

## Bundles and layers

| Bundle | Responsibility | Layers |
|---|---|---|
| `forceStructure` | Forces and units as organizations | `unit`: forces, units and their ordering Â· `command`: command and subordination lines |
| `assetsAndReadiness` | What forces hold and how ready they are | `assetReference`: identifiers of held assets, never their operational detail Â· `readiness`: coarse readiness states per unit |
| `mandate` | Why forces exist and may act | `legalMandate`: founding and empowering acts Â· `deploymentAuthorization`: decisions permitting deployment |

## Objects

- `force`: a constituted armed or security force; key attributes: name, serviceBranchType, mandateRef, status
- `forceUnit`: an organizational unit within a force; key attributes: designation, echelon, parentRef, location Class
- `assetReference`: an identifier of an asset held by a unit, resolved elsewhere; key attributes: assetIdentifier, assetClass, custodyUnitRef, snapshotDate
- `forceMandate`: the legal basis of a force's existence and powers; key attributes: legalBasisRef, scope, constraints, review Rule
- `readinessState`: a coarse, dated readiness assessment of a unit; key attributes: unitRef, readinessCategory, assessedOn, validity
- `deploymentAuthorization`: a decision permitting deployment within or beyond the polity; key attributes: authorityRef, scope, duration, reportingDuty

## Relationships

- `forceUnit` -> partOf -> `force` (N:1): units nest within one constituted force
- `forceUnit` -> subordinateTo -> `forceUnit` (N:1): the command line is a hierarchy over units
- `force` -> constitutedBy -> `forceMandate` (N:1): a force exists only under a legal mandate
- `assetReference` -> assignedTo -> `forceUnit` (N:1): asset identifiers attach to the unit holding custody
- `readinessState` -> describes -> `forceUnit` (N:1): coarse readiness is assessed per unit
- `deploymentAuthorization` -> permits -> `force` (N:1): deployment decisions name the force they cover

## Events

- `forceEstablished`: a force was constituted under a legal mandate
- `unitFormed`: a unit was formed and placed in the command structure
- `unitDisbanded`: a unit was dissolved and its references closed
- `mandateGranted`: a founding or empowering act took effect for a force
- `readinessAssessed`: a dated coarse readiness state was recorded for a unit
- `deploymentAuthorized`: a competent authority permitted a deployment
- `deploymentConcluded`: an authorized deployment ended and reporting closed

## Contracts

- `oversightDisclosure`: graded access for mandated oversight bodies, scoped by clearance class
- `alliedExchange`: treaty-based exchange of structure and readiness data with allied polities per A15
- `publicTransparencySummary`: periodic aggregate disclosure of force posture and spending class

## Projections

- `publicDefenseSummary`: high-level posture and mandate summary; omits units, assets and readiness
- `oversightView`: structure, mandates and authorizations for mandated committees; omits operational detail held in G3
- `orderOfBattle`: the restricted full structure with asset references and readiness; omits nothing within this model's breadth

## Composition

- REFERENCE `world.defenseOperations` (G3): all operational depth, plans and engagements live there; this model only anchors identity, structure and mandate
- REFERENCE `world.lawmaking` (A10): mandates and deployment authorizations trace to enactments
- REFERENCE `world.publicOffice` (A11): the command apex and civilian control sit in branch bodies
- REFERENCE `world.interstateRelations` (A15): alliance obligations shape structure and govern allied exchange
- MIX-IN `world.auditTrail` (S4): every structural and mandate change is append-only
- imports: nato-standards (ALIGN): interoperability terminology for units, echelons and readiness categories, referenced not adopted

## Stewardship

The defense authority stewards this model under the tightest default access in the catalogue: nothing is visible beyond the public transparency summary except by explicit owner grant. All grants, including oversight and allied exchange, flow through S1 ownership and S2 access, with S4 audit on every disclosure.