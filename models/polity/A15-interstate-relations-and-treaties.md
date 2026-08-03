# A15 Interstate Relations & Treaties

This meta-model describes the outward-facing relations of a polity: treaties negotiated, signed, ratified and in force, the obligations they create and the reservations that qualify them, memberships in international organizations, and accredited missions between polities. It is its own model because interstate facts belong to two or more sovereign catalogues at once: each polity stewards its own mirrored record of the same treaty or membership and reconciles it with counterparts by federation rather than through any shared owner.

## Manifest

```yaml
muif:
  version: "1.0"
metaModel:
  id: "vercy:world:a15"
  csn: world.interstateRelations
  version: 0.2.0
  displayName: Interstate Relations & Treaties
  description: Treaties, obligations, memberships and missions between sovereign polities.
conformance:
  muc: "2.0: Conformant"
  mmas: A1
namespaces:
  - world.interstateRelations
bundles:
  - csn: world.interstateRelations.treatyLifecycle
    displayName: Treaty lifecycle
    layers:
      - world.interstateRelations.treatyLifecycle.signature
      - world.interstateRelations.treatyLifecycle.ratification
      - world.interstateRelations.treatyLifecycle.entryIntoForce
  - csn: world.interstateRelations.obligations
    displayName: Obligations
    layers:
      - world.interstateRelations.obligations.commitment
      - world.interstateRelations.obligations.compliance
  - csn: world.interstateRelations.membership
    displayName: Membership
    layers:
      - world.interstateRelations.membership.accession
      - world.interstateRelations.membership.representation
imports:
  - source: vclt
    version: "*"
  - source: mufp
    version: "*"
```

## Bundles and layers

| Bundle | Responsibility | Layers |
|---|---|---|
| `treatyLifecycle` | A treaty from text to force | `signature`: negotiation outcomes and signature Â· `ratification`: domestic consent to be bound Â· `entryIntoForce`: force, amendment, denunciation |
| `obligations` | What being bound means | `commitment`: obligations and reservations per party Â· `compliance`: reported performance against obligations |
| `membership` | Standing relations between polities | `accession`: joining organizations and regimes Â· `representation`: missions and accreditation |

## Objects

- `treaty`: an agreement governed by international law; key attributes: title, subjectMatter, adoptedOn, depositaryRef, status
- `party`: one polity's standing under a treaty; key attributes: polityRef, treatyRef, becameBoundOn, status
- `ratification`: the domestic act of consent to be bound; key attributes: instrument, enactmentRef, depositedOn
- `reservation`: a qualification a party attaches to obligations; key attributes: text, targetProvisions, objections
- `obligation`: a distinct commitment arising from a treaty; key attributes: provisionRef, bearer, beneficiary, reportingRule
- `membership`: a polity's membership in an international organization or regime; key attributes: organizationRef, class, since, status
- `mission`: an accredited standing representation to another polity or organization; key attributes: sendingPolityRef, hostRef, headOfMissionRef, status

## Relationships

- `party` -> boundBy -> `treaty` (N:M): a treaty binds several polities; a polity is party to many treaties
- `party` -> isPolity -> `polityRef` (1:1): each party record resolves to a polity in A1
- `ratification` -> binds -> `party` (N:1): consent instruments accumulate on one party record
- `obligation` -> arisesFrom -> `treaty` (N:1): commitments trace to specific provisions
- `reservation` -> qualifies -> `obligation` (N:1): a reservation narrows or excludes particular commitments
- `membership` -> joins -> `organizationRef` (N:1): membership resolves to an organization in O1
- `mission` -> accreditedTo -> `polityRef` (N:1): a mission is hosted by one polity or organization

## Events

- `treatySigned`: a negotiated text was signed by the polity's representative
- `treatyRatified`: domestic consent to be bound was completed and deposited
- `reservationEntered`: a qualification was attached on becoming bound
- `treatyEnteredIntoForce`: the treaty took effect for this party
- `treatyAmended`: the treaty text or annexes were amended in force
- `treatyDenounced`: a party withdrew and the treaty ceased to bind it
- `membershipGranted`: the polity acceded to an organization or regime
- `missionAccredited`: a standing mission was accredited by the host

## Contracts

- `publicTreatyRegistry`: open access to treaty texts, party status and in-force dates
- `federationReconciliation`: the standing agreement by which counterpart catalogues reconcile mirrored records of the same treaty or membership
- `complianceReporting`: scoped exchange of performance reports between parties or with an organization

## Projections

- `treatyBookInForce`: everything currently binding this polity; omits negotiation history and lapsed instruments
- `obligationMatrix`: who owes what to whom under which provision; omits diplomatic correspondence
- `membershipMap`: current memberships and missions; omits compliance detail

## Composition

- REFERENCE `world.organization` (O1): parties, hosts and senders resolve to polities
- REFERENCE `world.organization` (O1): international organizations joined through membership
- REFERENCE `world.lawmaking` (A10): ratification is typically completed by enactment
- REFERENCE `world.publicOffice` (A11): signature and accreditation act under the full powers of an office
- ALIGN `world.interstateRelations` (A15) of each counterpart polity's catalogue: the same treaty is a mirrored sovereign record on both sides, reconciled without merging
- MIX-IN `world.auditTrail` (S4): lifecycle acts and reconciliations are append-only
- imports: vclt (ALIGN): treaty-law lifecycle concepts, signature, ratification, reservation, denunciation
- imports: mufp (REFERENCE): the federation protocol used to reconcile mirrored interstate records between sovereign catalogues

## Stewardship

The foreign-affairs authority stewards the polity's own copy of every interstate record; no shared owner exists across polities. Treaty texts and party status are public; negotiation and compliance layers are opened only by owner grant via S1 and S2.