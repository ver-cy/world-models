# N8 Identifier & Naming System

This meta-model describes identifier schemes and namespaces as things in the world: who establishes a scheme, what syntax and checksums constrain it, how identifiers are assigned to referents, and how they are resolved and crosswalked between schemes. It is its own model because nearly every other model in the catalogue carries identifiers, and the drift, collision and resolution problems of naming can only be handled once, at the scheme level, rather than inside each consuming model.

## Manifest

```yaml
muif:
  version: "1.0"
metaModel:
  id: "vercy:world:n8"
  csn: world.identifierNaming
  version: 0.2.0
  displayName: "Identifier & Naming System"
  description: "Identifier schemes, registration authorities, assignments, resolution and crosswalks."
conformance:
  muc: "2.0: Conformant"
  mmas: A1
namespaces:
  - world.identifierNaming
bundles:
  - csn: world.identifierNaming.scheme
    displayName: "Scheme"
    layers:
      - world.identifierNaming.scheme.schemeDefinition
      - world.identifierNaming.scheme.authorityAndDelegation
  - csn: world.identifierNaming.assignment
    displayName: "Assignment"
    layers:
      - world.identifierNaming.assignment.allocation
      - world.identifierNaming.assignment.identifierLifecycle
  - csn: world.identifierNaming.resolution
    displayName: "Resolution"
    layers:
      - world.identifierNaming.resolution.resolutionService
      - world.identifierNaming.resolution.crosswalkAndMapping
imports:
  - source: iso-identifier-suites
    version: "*"
  - source: rfc-8141-urn
    version: "*"
```

## Bundles and layers

| Bundle | Responsibility | Layers |
|---|---|---|
| `scheme` | What a naming system is and who runs it | `schemeDefinition`: schemes, syntax, checksums, scope · `authorityAndDelegation`: registrars, mandates, sub-delegation |
| `assignment` | Binding names to things | `allocation`: assignment of identifiers to referents · `identifierLifecycle`: reservation, retirement, reassignment |
| `resolution` | Getting from name to referent | `resolutionService`: resolvers, endpoints, coverage · `crosswalkAndMapping`: equivalences between schemes |

## Objects

- `identifierScheme`: a naming system with rules and scope; key attributes: schemeId, name, syntaxPattern, checksumAlgorithm, scope.
- `registrationAuthority`: the party mandated to run a scheme or sub-namespace; key attributes: authorityRef, mandate, since.
- `syntaxRule`: a constraint on valid identifiers; key attributes: ruleKind, expression.
- `identifier`: a name within a scheme; key attributes: value, schemeRef, status.
- `identifierAssignment`: the binding of an identifier to a referent; key attributes: referentRef, assignedAt, assignedBy, evidenceRef.
- `resolutionService`: a service that dereferences identifiers; key attributes: endpointRef, protocol, coverage, serviceLevel.
- `schemeCrosswalk`: a declared equivalence between schemes; key attributes: fromSchemeRef, toSchemeRef, mappingQuality.

## Relationships

- `identifierScheme` -> governedBy -> `registrationAuthority` (N:1): the mandate behind the scheme.
- `identifierScheme` -> constrainedBy -> `syntaxRule` (1:N): what counts as a well-formed identifier.
- `identifierAssignment` -> assigns -> `identifier` (1:1): the binding act for one name.
- `identifier` -> resolvedBy -> `resolutionService` (N:N): where the name can be dereferenced.
- `schemeCrosswalk` -> maps -> `identifierScheme` (N:N): equivalences across naming systems.
- `registrationAuthority` -> delegates -> `registrationAuthority` (1:N): sub-namespace delegation chains.

## Events

- `schemeEstablished`: a new identifier scheme was created under a mandate.
- `authorityDelegated`: a sub-namespace was delegated to another registrar.
- `identifierAssigned`: an identifier was bound to a referent.
- `identifierRetired`: an identifier was withdrawn from active use.
- `identifierReassigned`: a retired identifier was bound to a new referent where the scheme permits.
- `resolverEndpointChanged`: a resolution service moved or changed protocol.

## Contracts

- `registrationContract`: terms under which a registrant obtains and keeps an assignment.
- `resolutionServiceContract`: service terms for dereferencing identifiers at volume.
- `bulkCrosswalkContract`: licensed access to full crosswalk tables between schemes.

## Projections

- `schemeRegistryView`: schemes, authorities and syntax rules; omits individual assignments.
- `resolverLookupView`: single-identifier dereference results; omits scheme administration detail.
- `crosswalkExport`: pairwise equivalence tables; omits assignment provenance.

## Composition

- REFERENCE `world.organization` (O1): registration authorities and resolver operators are organizations.
- REFERENCE `world.modelOntology` (N6): the formal syntax of a scheme may itself be registered as a model.
- REFERENCED BY `world.documentRecord` (N1), `world.dataset` (N3), `world.intellectualProperty` (N12) and other catalogue models: identifier and code Properties across the catalogue carry scheme plus version from this register, which is what makes drift detectable.
- imports: iso-identifier-suites (ALIGN): the ISO family of identifier standards registered as schemes here.
- imports: rfc-8141-urn (ALIGN): URN namespace syntax and resolution behaviour.

## Stewardship

The neutral owner archetype is the scheme registrar, who owns scheme definitions and assignment records; registrants own the facts about their own referents. Access is always granted by the respective owner through the catalogue's S1/S2 ownership and access models, with bulk exports audited via S4.
