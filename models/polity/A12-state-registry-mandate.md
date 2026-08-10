# A12 State Registry Mandate

This meta-model describes which registers a polity must keep, on what legal basis, who is assigned as registrar for each, and which trust rules (public faith, correction, retention, access regime) govern them. It is its own model because it is the constitutional table of contents of the register landscape: every register-shaped model in the catalogue points here to prove that it exists by mandate rather than by habit, and registrar accountability is only checkable against an explicit mandate record.

## Manifest

```yaml
muif:
  version: "1.0"
metaModel:
  id: "vercy:world:a12"
  csn: world.registryMandate
  version: 0.2.0
  displayName: State Registry Mandate
  description: The mandated registers of a polity, their registrars and the trust rules that govern them.
conformance:
  muc: "2.0: Conformant"
  mmas: A1
namespaces:
  - world.registryMandate
bundles:
  - csn: world.registryMandate.mandateSource
    displayName: Mandate source
    layers:
      - world.registryMandate.mandateSource.constitutionalBasis
      - world.registryMandate.mandateSource.statutoryMandate
  - csn: world.registryMandate.registerCatalogue
    displayName: Register catalogue
    layers:
      - world.registryMandate.registerCatalogue.registerDefinition
      - world.registryMandate.registerCatalogue.dataScope
  - csn: world.registryMandate.operation
    displayName: Operation
    layers:
      - world.registryMandate.operation.registrarAssignment
      - world.registryMandate.operation.publicFaith
      - world.registryMandate.operation.correction
imports:
  - source: eli
    version: "*"
  - source: akoma-ntoso
    version: "*"
```

## Bundles and layers

| Bundle | Responsibility | Layers |
|---|---|---|
| `mandateSource` | The legal basis of each obligation to keep a register | `constitutionalBasis`: mandates rooted directly in the constitution · `statutoryMandate`: mandates created by enacted statute |
| `registerCatalogue` | The registers themselves as defined obligations | `registerDefinition`: identity, subject matter, uniqueness rules · `dataScope`: what each register must and must not record |
| `operation` | How a mandated register must be run | `registrarAssignment`: who operates each register · `publicFaith`: reliance and presumption rules for entries · `correction`: rectification and appeal procedure |

## Objects

- `registryMandate`: an obligation of the polity to keep a register; key attributes: legalBasisRef, subjectMatter, since, status
- `registerDefinition`: the defined register an obligation calls for; key attributes: name, keyedBy, uniquenessRule, mandateRef
- `registrarAssignment`: the designation of an operator for a register; key attributes: registerRef, registrarRef, since, terms
- `publicFaithRule`: the reliance rule for entries of a register; key attributes: presumption, goodFaithProtection, exceptions
- `retentionRule`: how long and in what form entries must be kept; key attributes: period, archivalForm, disposalRule
- `correctionProcedure`: how erroneous entries are rectified; key attributes: initiators, evidenceRequired, appealPath
- `accessRegime`: the default openness of a register; key attributes: publicByDefault, gradedClasses, selfAccessRule

## Relationships

- `registryMandate` -> establishedBy -> `enactmentRef` (N:1): every mandate traces to a constitutional provision or enactment in A10
- `registerDefinition` -> mandatedBy -> `registryMandate` (N:1): a register exists only under an explicit mandate
- `registrarAssignment` -> assigns -> `registerDefinition` (N:1): each assignment designates the operator of one register
- `registrarAssignment` -> namesRegistrar -> `officeRef` (N:1): the registrar is an office of A11 or a body of O1
- `publicFaithRule` -> governs -> `registerDefinition` (N:1): reliance rules attach per register
- `correctionProcedure` -> appliesTo -> `registerDefinition` (N:1): rectification paths attach per register
- `accessRegime` -> constrains -> `registerDefinition` (N:1): the openness default attaches per register

## Events

- `mandateEnacted`: a new obligation to keep a register entered into force
- `registerEstablished`: a mandated register was defined and opened
- `registrarAssigned`: an operator was designated for a register
- `registrarChanged`: operation of a register passed to a different registrar
- `publicFaithRuleChanged`: the reliance rules of a register were amended
- `accessRegimeChanged`: the openness default of a register was amended
- `registerDecommissioned`: a register was closed and its retention rule took over

## Contracts

- `mandateCatalogueAccess`: open access to the full list of mandated registers, registrars and trust rules
- `registrarConformanceAttestation`: a registrar's periodic attestation that a register is operated per its mandate
- `interRegisterExchangeAgreement`: agreed data flows between two mandated registers, scoped by their access regimes

## Projections

- `registerDirectory`: the public map of registers and their registrars; omits operational and conformance detail
- `registrarObligations`: everything one registrar owes across its assignments; omits other registrars
- `publicFaithMap`: which registers and entry classes enjoy reliance presumptions; omits procedure detail

## Composition

- REFERENCE `world.lawmaking` (A10): mandates are created, amended and repealed by enactment
- REFERENCE `world.publicOffice` (A11): registrar assignments name offices as accountable operators
- REFERENCE `world.organization` (O1): registrars may be bodies rather than single offices
- REFERENCE `world.grantedRight` (R5): a mandated register whose definition, registrar and public-faith rule live here; the same pattern anchors the other register models of the catalogue
- MIX-IN `world.auditTrail` (S4): every mandate and assignment change is append-only and traceable
- imports: eli (REFERENCE): durable identifiers for the founding legal acts of each mandate
- imports: akoma-ntoso (ALIGN): document structure of mandate and amendment texts

## Stewardship

The constitution-maker and the legislature own the mandate layer; each registrarAssignment then names the operating steward per register. The catalogue of mandates is public; any restricted operational detail is opened only by owner grant through S1 and S2.