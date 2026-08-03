# K1 Function & Capability

This meta-model describes what an agent is able to do: the functions an agent can fulfil, the capabilities behind them, the proficiency with which they are held, and the capacity in which they can be exercised. It is its own model because ability is not the same as action: the world needs a stable way to state, evidence and compare what people and organizations could do, independently of any particular act they have performed (that is K2) or any process they take part in (K3).

## Manifest

```yaml
muif:
  version: "1.0"
metaModel:
  id: "vercy:world:k1"
  csn: world.functionAndCapability
  version: 0.2.0
  displayName: "Function & Capability"
  description: "Functions, capabilities, proficiency and capacity of agents."
conformance:
  muc: "2.0: Conformant"
  mmas: A1
namespaces:
  - world.functionAndCapability
bundles:
  - csn: world.functionAndCapability.definition
    displayName: "Definition"
    layers:
      - world.functionAndCapability.definition.functionCatalog
      - world.functionAndCapability.definition.capabilityTaxonomy
      - world.functionAndCapability.definition.proficiencyScale
  - csn: world.functionAndCapability.attribution
    displayName: "Attribution"
    layers:
      - world.functionAndCapability.attribution.agentCapability
      - world.functionAndCapability.attribution.evidence
  - csn: world.functionAndCapability.capacity
    displayName: "Capacity"
    layers:
      - world.functionAndCapability.capacity.throughput
      - world.functionAndCapability.capacity.availability
imports:
  - source: esco
    version: "*"
  - source: onet
    version: "*"
```

## Bundles and layers

| Bundle | Responsibility | Layers |
|---|---|---|
| `definition` | The shared vocabulary of what can be done | `functionCatalog`: named functions agents can fulfil Â· `capabilityTaxonomy`: hierarchy of abilities and skills Â· `proficiencyScale`: graded levels of mastery |
| `attribution` | Attaching capabilities to concrete agents | `agentCapability`: which agent holds which capability at which level Â· `evidence`: assessments, credentials and track records supporting an attribution |
| `capacity` | How much and when a capability can be exercised | `throughput`: quantity per period an agent can deliver Â· `availability`: time windows and conditions under which the capability is exercisable |

## Objects

- `function`: a named purpose an agent can fulfil (for example welding, auditing, translating); key attributes: name, definition, domain, typical outputs
- `capability`: an ability underlying one or more functions; key attributes: name, taxonomy position, description, decay characteristics
- `proficiencyLevel`: a graded step on a mastery scale; key attributes: scale, rank, behavioural descriptor
- `capabilityAttribution`: the statement that a specific agent holds a capability; key attributes: agent reference, capability reference, level, valid period, status
- `evidenceRecord`: support for an attribution; key attributes: evidence kind (assessment, credential, observed act), issuer, date, reference to source record
- `capacityStatement`: a quantitative declaration of how much the agent can do; key attributes: unit, rate, period, constraints
- `capabilityRequirement`: a demand side statement of what a task, role or offering needs; key attributes: required capability, minimum level, criticality

## Relationships

- `capability` -> specializes -> `capability` (many-to-one): the taxonomy of abilities from broad to narrow
- `function` -> realizedBy -> `capability` (many-to-many): the abilities that together make a function performable
- `capabilityAttribution` -> attributesTo -> `agent` (many-to-one): the person or organization the capability statement is about
- `capabilityAttribution` -> atLevel -> `proficiencyLevel` (many-to-one): the mastery grade claimed or assessed
- `evidenceRecord` -> supports -> `capabilityAttribution` (many-to-many): the grounds on which the attribution rests
- `capacityStatement` -> quantifies -> `capabilityAttribution` (many-to-one): how much of the attributed ability is available
- `capabilityRequirement` -> demands -> `capability` (many-to-one): what a task or offering asks for

## Events

- `capabilityAttributed`: an agent was stated to hold a capability, with level and grounds
- `proficiencyAssessed`: an assessment produced or updated a proficiency judgement
- `evidenceRecorded`: a credential, assessment or observed performance was attached as evidence
- `capacityDeclared`: an agent declared or revised the volume and availability of a capability
- `attributionLapsed`: an attribution expired or decayed past its validity conditions
- `attributionRevoked`: an attribution was withdrawn by its issuer or the agent

## Contracts

- `attributionVerification`: a relying party queries whether an agent holds a capability at a level, receiving a yes/no or level answer without underlying evidence detail
- `profileDisclosure`: the agent grants a consumer read access to a defined subset of its capability profile for a period
- `assessmentSubmission`: an assessing organization submits proficiency results into the agent's attribution record under agreed provenance rules

## Projections

- `capabilityProfile`: the public face of an agent's abilities; omits evidence documents and assessor identities
- `matchingView`: capabilities and levels shaped for requirement-to-capability matching; omits personal identifiers beyond an opaque agent reference
- `capacityBoard`: aggregate available capacity by capability and region; omits individual agents

## Composition

- REFERENCE `world.person` (H1): persons are the primary capable agents attributions point at
- REFERENCE `world.organization` (O1): organizations hold collective capabilities and issue assessments
- REFERENCE `world.actAction` (K2): recorded acts serve as observed performance evidence for attributions
- REFERENCE `world.practiceMethodAndProcedure` (K6): competence requirements published in methods resolve to capabilities of this model
- imports: esco (ALIGN): European skills and competences taxonomy aligned with the capability taxonomy layer
- imports: onet (ALIGN): occupational abilities and work activities vocabulary aligned with functions and capabilities

## Stewardship

The capable agent is the owner of statements about its own abilities; assessors contribute evidence but the profile belongs to the agent. Access to attributions, evidence and capacity is granted by the owner through the catalogue's ownership and access models (S1/S2), with audit via S4.
