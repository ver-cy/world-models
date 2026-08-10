# M5 Medicine & Health Substance

This meta-model describes medicinal products and controlled substances: what a medicine contains and in what form and strength, under which authorizations and schedules it may circulate, how its batches move, and what safety signals surround it. It is its own model because medicines combine market goods semantics with a dense regulatory and vigilance apparatus (authorizations, controlled status, batch verification, signals) that no other goods category carries.

## Manifest

```yaml
muif:
  version: "1.0"
metaModel:
  id: "vercy:world:m5"
  csn: world.medicine
  version: 0.2.0
  displayName: "Medicine & Health Substance"
  description: Medicinal products and controlled substances with composition, form, authorization, batches and safety signals.
conformance:
  muc: "2.0: Conformant"
  mmas: A1
namespaces:
  - world.medicine
bundles:
  - csn: world.medicine.product
    displayName: Product
    layers:
      - world.medicine.product.medicineIdentity
      - world.medicine.product.activeComposition
      - world.medicine.product.formAndStrength
  - csn: world.medicine.authorization
    displayName: Authorization
    layers:
      - world.medicine.authorization.marketingAuthorization
      - world.medicine.authorization.controlledStatus
  - csn: world.medicine.supply
    displayName: Supply
    layers:
      - world.medicine.supply.batchAndSerialization
      - world.medicine.supply.supplyStatus
  - csn: world.medicine.vigilance
    displayName: Vigilance
    layers:
      - world.medicine.vigilance.safetySignal
imports:
  - source: who-atc
    version: "*"
  - source: rxnorm
    version: "*"
  - source: iso-idmp
    version: "*"
```

## Bundles and layers

| Bundle | Responsibility | Layers |
|---|---|---|
| `product` | What the medicine is | `medicineIdentity`: product name, classification codes, holder reference · `activeComposition`: active substances with roles and reference strengths · `formAndStrength`: dose forms, strengths, routes of administration |
| `authorization` | Under what permissions it circulates | `marketingAuthorization`: authorizations per jurisdiction with status and conditions · `controlledStatus`: scheduling of the product or its substances per jurisdiction |
| `supply` | How physical product reaches use | `batchAndSerialization`: batches, expiry, pack serialization ranges · `supplyStatus`: availability and shortage standing per market |
| `vigilance` | What safety knowledge surrounds it | `safetySignal`: signals, their sources, assessment state and outcomes |

## Objects

- `medicine`: a medicinal product class; key attributes: name, classification codes, authorization holder reference.
- `activeSubstanceLink`: the tie from a medicine to an active substance; key attributes: substance reference, role, reference strength.
- `doseFormSpec`: a dose form the medicine is presented as; key attributes: form, route of administration, appearance.
- `strengthSpec`: a strength presentation; key attributes: amount, unit, per-unit basis.
- `marketingAuthorization`: permission to market in a jurisdiction; key attributes: jurisdiction, number, status, conditions, validity.
- `controlledStatus`: scheduling of the product or substance; key attributes: jurisdiction, schedule, restrictions.
- `medicineBatch`: a production batch; key attributes: batch code, expiry date, serialization range, release status.
- `safetySignal`: a detected or reported safety concern; key attributes: source, description, assessment state, outcome.

## Relationships

- `medicine` -> contains -> `activeSubstanceLink` (1..*): every medicine declares at least one active substance.
- `medicine` -> presentedAs -> `doseFormSpec` (1..*): forms the product exists in.
- `medicine` -> dosedAt -> `strengthSpec` (1..*): strengths per form.
- `medicine` -> authorizedUnder -> `marketingAuthorization` (0..*): one authorization per jurisdiction at most is active.
- `medicine` -> scheduledUnder -> `controlledStatus` (0..*): controlled standing varies by jurisdiction.
- `medicineBatch` -> ofMedicine -> `medicine` (many-to-one): batches bound production populations.
- `safetySignal` -> concerns -> `medicine` (many-to-many): one signal can span products sharing a substance.

## Events

- `authorizationGranted`: a marketing authorization was issued in a jurisdiction.
- `authorizationVaried`: the terms or conditions of an authorization changed.
- `authorizationSuspended`: an authorization was suspended or revoked.
- `batchReleased`: a batch passed release and entered the supply chain.
- `batchRecalled`: a batch was recalled with a stated classification and scope.
- `scheduleChanged`: the controlled status of the product changed in a jurisdiction.
- `safetySignalRaised`: a new safety signal entered assessment.
- `shortageDeclared`: availability of the product fell below demand in a market.

## Contracts

- `registerAccess`: read access to identity, form, strength and authorization status, typically broad for public registers.
- `batchVerification`: query contract confirming that a serialized pack belongs to a genuine, released, non-recalled batch.
- `vigilanceExchange`: structured exchange of safety signals and their assessments between the holder and oversight parties.

## Projections

- `publicRegisterView`: name, composition, form, strength and authorization status; omits supply chain and serialization detail.
- `prescriberView`: forms, strengths, controlled status and active signals relevant to prescribing; omits batch logistics.
- `supplyChainView`: batches, expiry, serialization and shortage standing; omits vigilance assessment internals.

## Composition

- EXTEND `world.tradableGood` (M3): a medicine is a good; identifiers, packaging and batch mechanics are inherited, regulatory and vigilance semantics are added.
- REFERENCE `world.materialSubstance` (M1): active substances and excipients resolve to substance classes with their hazard data.
- REFERENCE `world.physicalItem` (M2): a serialized pack under verification is an individual item.
- REFERENCE the health cluster (H): indications, contraindications and adverse effect terms resolve to health-cluster condition semantics rather than local text.
- imports: who-atc (REFERENCE): anatomical-therapeutic-chemical classification codes.
- imports: rxnorm (ALIGN): clinical drug naming alignment.
- imports: iso-idmp (ALIGN): identification-of-medicinal-products concepts for product, form and strength.

## Stewardship

Product records are stewarded by the producer holding the marketing authorization, while authorization, scheduling and vigilance layers are overseen by a public health authority archetype; in both cases access by any other party is granted by the record owner through S1/S2, and all regulatory events are traceable via S4 audit.
