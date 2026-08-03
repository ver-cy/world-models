# O4 Organizational Mandate & Charter

This meta-model describes the constitutive rules of an organization: charters and statutes, the mandates and powers they confer, the limits they impose, and the accountability duties they create. It is its own model because constitutive rules outlive officeholders and structures, change by their own formal procedures, and are cited by units, contracts and oversight independently of day-to-day organizational data.

## Manifest

```yaml
muif:
  version: "1.0"
metaModel:
  id: "vercy:world:o4"
  csn: world.charter
  version: 0.2.0
  displayName: "Organizational Mandate & Charter"
  description: "Charters, statutes, mandates, powers, limits and accountability duties that constitute an organization."
conformance:
  muc: "2.0: Conformant"
  mmas: A1
namespaces:
  - world.charter
bundles:
  - csn: world.charter.constitution
    displayName: "Constitution"
    layers:
      - world.charter.constitution.foundingInstrument
      - world.charter.constitution.amendment
  - csn: world.charter.powers
    displayName: "Powers"
    layers:
      - world.charter.powers.mandateGrant
      - world.charter.powers.limits
  - csn: world.charter.accountability
    displayName: "Accountability"
    layers:
      - world.charter.accountability.oversight
      - world.charter.accountability.dischargeRecord
imports:
  - source: legal-templates
    version: "*"
  - source: akoma-ntoso
    version: "*"
```

## Bundles and layers

| Bundle | Responsibility | Layers |
|---|---|---|
| `constitution` | The instrument itself and how it changes | `foundingInstrument`: charter or statute text and its adoption Â· `amendment`: revisions, consolidation and the amendment procedure |
| `powers` | What the instrument permits | `mandateGrant`: mandates and powers conferred on bodies and roles Â· `limits`: restrictions, reserved matters and required approvals |
| `accountability` | To whom the organization answers | `oversight`: bodies to which duties are owed and their scope Â· `dischargeRecord`: reports filed, reviews held, duties met |

## Objects

- `charter`: the constitutive instrument; key attributes: title, adoption date, jurisdiction, consolidation state.
- `charterProvision`: an addressable clause of the instrument; key attributes: citation path, text, in-force period.
- `mandate`: a purposeful assignment of responsibility; key attributes: subject matter, holder reference, validity.
- `power`: a specific authorization to act; key attributes: action class, conditions, financial or scope ceilings.
- `delegation`: a passing of power downward; key attributes: source power, recipient reference, constraints, validity.
- `accountabilityDuty`: an obligation to report or submit to review; key attributes: duty kind, cadence, addressee reference.
- `amendmentAct`: a formal change to the instrument; key attributes: decision reference, affected provisions, effective date.

## Relationships

- `charter` -> constitutes -> `world.organization` (1:1): the organization (O1) this instrument brings into being and governs.
- `mandate` -> conferredBy -> `charter` (n:1): every mandate traces to the instrument.
- `power` -> boundedBy -> `charterProvision` (n:m): the clauses that condition and limit a power.
- `delegation` -> passes -> `power` (n:1): the power being delegated to a unit (O2) or role assignment (O3).
- `accountabilityDuty` -> owedTo -> `world.organization` (n:1): the overseeing body, an organization in O1, including public bodies.
- `amendmentAct` -> revises -> `charter` (n:1): the change history of the instrument.

## Events

- `charterAdopted`: a constitutive instrument was adopted.
- `charterAmended`: provisions were revised by the prescribed procedure.
- `mandateConferred`: a mandate was granted to a body or role.
- `mandateRevoked`: a mandate was withdrawn.
- `powerDelegated`: a power was passed downward with constraints.
- `dutyDischarged`: an accountability duty was met, for example a report was filed.

## Contracts

- `charterPublication`: public or member access to the current consolidated text.
- `dueDiligenceAccess`: counterparty access to powers and limits before entering an agreement.
- `oversightFiling`: periodic submission of discharge records to the overseeing body, standard for public bodies.

## Projections

- `currentConsolidatedCharter`: the text as amended to date; omits drafting history and rejected amendments.
- `powersMatrix`: who may bind the organization, for what, within which limits; omits narrative provisions.
- `oversightLedger`: duties owed, addressees, cadence and discharge status; omits instrument text.

## Composition

- REFERENCE `world.organization` (O1): the constituted organization and any overseeing bodies.
- REFERENCE `world.organizationalUnit` (O2): delegations land on units and their mandates.
- REFERENCE `world.employment` (O3): delegations may attach to role assignments.
- REFERENCE `world.commercialContract` (O5): counterparties verify powers here before executing agreements there.
- REFERENCE `world.publicRegister` (A12): charters of public bodies are published in public registers.
- REFERENCE `world.disputeResolution` (A19): contests over powers and their limits are heard there.
- REFERENCE `world.stewardship` (S1) and `world.accessGrant` (S2): ownership and access grants over charter records.
- MIX-IN `world.auditTrail` (S4): audit facets on adoption, amendment and delegation events.
- imports: legal-templates (COMPOSE): model clause and instrument structures reused in founding instruments.
- imports: akoma-ntoso (ALIGN): machine-readable legal document structure for provisions and citations.

## Stewardship

The organization owns its charter record; for public bodies an oversight body additionally holds a registrar-style copy. Access is granted by the owner under the S1/S2 models of this catalogue.
