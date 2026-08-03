# K6 Practice Method & Procedure

This meta-model describes codified ways of doing things: methods (the reasoned approach), procedures (the step-by-step instructions), the standards they implement, and the competences they demand. It is separate from process (K3) because a method is knowledge, published, versioned and adopted, whereas a process is an operationalized flow; many processes across many organizations can codify the same method.

## Manifest

```yaml
muif:
  version: "1.0"
metaModel:
  id: "vercy:world:k6"
  csn: world.practiceMethodAndProcedure
  version: 0.2.0
  displayName: "Practice Method & Procedure"
  description: "Codified methods, procedures, the standards they implement and the competences they require."
conformance:
  muc: "2.0: Conformant"
  mmas: A1
namespaces:
  - world.practiceMethodAndProcedure
bundles:
  - csn: world.practiceMethodAndProcedure.codification
    displayName: "Codification"
    layers:
      - world.practiceMethodAndProcedure.codification.methodDefinition
      - world.practiceMethodAndProcedure.codification.procedureText
      - world.practiceMethodAndProcedure.codification.standardReference
  - csn: world.practiceMethodAndProcedure.applicability
    displayName: "Applicability"
    layers:
      - world.practiceMethodAndProcedure.applicability.competenceRequirement
      - world.practiceMethodAndProcedure.applicability.scopeOfUse
  - csn: world.practiceMethodAndProcedure.lifecycle
    displayName: "Lifecycle"
    layers:
      - world.practiceMethodAndProcedure.lifecycle.versioning
      - world.practiceMethodAndProcedure.lifecycle.adoption
imports:
  - source: iso-management-systems
    version: "*"
  - source: iso-9001
    version: "*"
```

## Bundles and layers

| Bundle | Responsibility | Layers |
|---|---|---|
| `codification` | The documented way itself | `methodDefinition`: approach, principles and rationale Â· `procedureText`: ordered step instructions Â· `standardReference`: external norms the method implements |
| `applicability` | Where and by whom it may be used | `competenceRequirement`: capabilities a practitioner needs Â· `scopeOfUse`: domains, conditions and limits of applicability |
| `lifecycle` | Currency and uptake | `versioning`: editions, supersession and errata Â· `adoption`: who adopted which edition and attested conformity |

## Objects

- `method`: a codified approach to a class of work; key attributes: name, purpose, principles, authoring organization, domain
- `procedure`: step-by-step instructions realizing a method; key attributes: name, preconditions, safety notes, expected result
- `procedureStep`: one instruction; key attributes: order, action text, inputs, checks
- `standardReference`: an external norm implemented or cited; key attributes: standard identifier, clause, relation kind
- `competenceRequirement`: a demanded practitioner ability; key attributes: capability reference, minimum level, certification needed
- `edition`: a published version of a method or procedure; key attributes: version, release date, change summary, status
- `adoptionRecord`: an organization's uptake of an edition; key attributes: adopter reference, edition, date, conformity attestation

## Relationships

- `method` -> detailedBy -> `procedure` (one-to-many): the instructions that make the approach executable
- `procedure` -> comprises -> `procedureStep` (one-to-many): the ordered instructions
- `method` -> implements -> `standardReference` (many-to-many): the norms the method gives effect to
- `method` -> requires -> `competenceRequirement` (one-to-many): who is fit to apply it
- `edition` -> supersedes -> `edition` (one-to-one): the version lineage
- `adoptionRecord` -> adoptedBy -> `organization` (many-to-one): the organization that took the method into use

## Events

- `methodPublished`: a method was released for use by its authoring organization
- `editionReleased`: a new version of a method or procedure was issued
- `procedureRevised`: instructions were changed within an edition cycle
- `methodAdopted`: an organization recorded uptake of an edition
- `methodDeprecated`: an edition or a whole method was withdrawn from recommended use

## Contracts

- `methodAccess`: a consumer obtains the right to read and apply a method, free or licensed, per the author's terms
- `adoptionAttestation`: an adopter declares conformity to an edition, verifiable by third parties
- `revisionSubscription`: an adopter receives notice of new editions, errata and deprecations

## Projections

- `practitionerHandbook`: the current edition's procedures for daily use; omits history and adoption data
- `complianceMatrix`: methods mapped to the standard clauses they implement; omits procedure text
- `trainingSyllabus`: competence requirements and steps shaped for instruction; omits versioning detail

## Composition

- REFERENCE `world.functionAndCapability` (K1): competence requirements resolve to capabilities and proficiency levels
- REFERENCE `world.organization` (O1): authoring and adopting organizations
- REFERENCE `world.processAndWorkflow` (K3): processes operationalize methods; the link is held on the process side and navigable from here
- imports: iso-management-systems (REFERENCE): management system requirements that methods commonly implement
- imports: iso-9001 (ALIGN): quality management vocabulary for procedures and conformity

## Stewardship

The authoring organization owns each method and its editions; adopters own their adoption records. Reading and applying a method follows owner-granted contracts under the catalogue's ownership and access models (S1/S2), with audit via S4.
