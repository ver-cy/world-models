# S1 Meta-Object Ownership & Stewardship

This meta-model answers one question for every meta-object in the catalogue: who controls it. It records ownership titles, fractional and joint holdings, appointed stewardship, scoped delegation of control, guardianship for parties who cannot act for themselves, and every transfer of control from one holder to the next. It is its own model because control is the precondition for the rest of this cluster: an access grant (S2), a disclosure shape (S3) or an attestation (S6) is only meaningful when the party issuing it can be shown to hold, or lawfully exercise, control over the underlying object.

## Manifest

```yaml
muif:
  version: "1.0"
metaModel:
  id: "vercy:world:s1"
  csn: world.ownership
  version: 0.2.0
  displayName: "Meta-Object Ownership & Stewardship"
  description: "Records who controls every meta-object: ownership, stewardship, delegation, guardianship and transfers."
conformance:
  muc: "2.0: Conformant"
  mmas: A1
namespaces:
  - world.ownership
bundles:
  - csn: world.ownership.tenure
    displayName: "Tenure"
    layers:
      - world.ownership.tenure.title
      - world.ownership.tenure.shares
      - world.ownership.tenure.guardianship
  - csn: world.ownership.delegation
    displayName: "Delegation"
    layers:
      - world.ownership.delegation.mandates
      - world.ownership.delegation.stewardCharges
  - csn: world.ownership.transfer
    displayName: "Transfer"
    layers:
      - world.ownership.transfer.conveyance
      - world.ownership.transfer.succession
imports:
  - source: iso-19152-ladm
    version: "*"
  - source: mu-core
    version: "*"
```

## Bundles and layers

| Bundle | Responsibility | Layers |
|---|---|---|
| `tenure` | Who holds control of a meta-object right now | `title`: the binding of a holder to an object Â· `shares`: fractional and joint holdings Â· `guardianship`: substitute holders for parties lacking capacity |
| `delegation` | Control exercised by someone other than the holder | `mandates`: scoped powers granted to a delegate Â· `stewardCharges`: steward appointments and their duties |
| `transfer` | How control moves between holders | `conveyance`: voluntary transfers between living parties Â· `succession`: transfers on death, dissolution or lapse |

## Objects

- `registryEntry`: the anchor record that makes an object controllable at all; key attributes: object reference, object kind, registration basis, registered time.
- `ownershipRecord`: the current binding of one or more holders to a registry entry; key attributes: holder references, basis of title, effective from, encumbrances.
- `holdingShare`: one party's fraction of a jointly held object; key attributes: holder, fraction, joint or several, since.
- `steward`: a party charged with operating an object on the holder's behalf without beneficial ownership; key attributes: appointment basis, duty list, term, accountability route.
- `delegationMandate`: a scoped, revocable grant of specific control powers from a holder to a delegate; key attributes: powers, scope, expiry, revocability, sub-delegation flag.
- `guardianshipArrangement`: a substitute-decision arrangement for a holder lacking capacity; key attributes: ward, guardian, legal basis, review date.
- `transferInstrument`: the instrument by which control moves; key attributes: parties, consideration, conditions precedent, execution time.

## Relationships

- `ownershipRecord` -> covers -> `registryEntry` (1..1): every title binds holders to exactly one registered object.
- `holdingShare` -> dividedFrom -> `ownershipRecord` (*..1): shares partition one title among co-holders.
- `delegationMandate` -> issuedUnder -> `ownershipRecord` (*..1): delegated powers can never exceed the title they flow from.
- `delegationMandate` -> vestsIn -> `steward` (*..1): the mandate names the party who may act.
- `guardianshipArrangement` -> exercises -> `ownershipRecord` (1..*): the guardian exercises the ward's holdings within the arrangement's basis.
- `transferInstrument` -> conveys -> `ownershipRecord` (1..*): a transfer rewrites which holders a title binds.
- `transferInstrument` -> authorizedBy -> `guardianshipArrangement` (0..1): transfers for wards require the arrangement's authority.

## Events

- `objectRegistered`: a meta-object received its registry entry and became controllable.
- `ownershipTransferred`: control of an object passed to a new holder under an executed instrument.
- `shareRestructured`: the fractions or parties of a joint holding changed.
- `mandateGranted`: a holder delegated defined powers to a delegate.
- `mandateRevoked`: a previously granted delegation was withdrawn or expired.
- `stewardAppointed`: a steward took charge of an object under stated duties.
- `guardianshipEstablished`: a guardian was empowered to act for a holder lacking capacity.
- `successionOpened`: a holder's death, dissolution or lapse started the transfer of their holdings.

## Contracts

- `titleExtract`: a third party reads the current holder of a named object, without history or shares.
- `mandateVerification`: a counterparty checks that a delegate's claimed powers exist, are in scope and are unrevoked before honoring an act.
- `transferWatch`: a subscriber receives transfer events for named objects, typically a creditor or counterparty with a legitimate interest.

## Projections

- `currentHolderIndex`: object to present holder; omits history, shares, mandates and guardianships.
- `holderPortfolio`: everything one party holds or lawfully exercises; omits all other parties' holdings.
- `chainOfTitle`: the full transfer history of one object; omits the parties' unrelated holdings.

## Composition

- REFERENCE `world.accessContract` (S2): every access grant must resolve its grantor against a live ownership record here.
- REFERENCE `world.accessAudit` (S4): reads of ownership data and all registry changes are logged there.
- REFERENCE `world.person` (H1): holders, wards, guardians and delegates are natural persons defined in the person model.
- REFERENCE `world.organization` (O1): organizations appear as holders and stewards; their identity and lifecycle live in their own model.
- REFERENCE `world.disputeResolution` (A19): disputed titles and contested successions are resolved by the courts model; outcomes flow back as transfer or annulment events.
- imports: iso-19152-ladm (ALIGN): the party, right, restriction and responsibility pattern that tenure and shares follow.
- imports: mu-core (EXTEND): the meta-object identity primitive that every registry entry anchors to.

## Stewardship

A root registrar archetype keeps this model as the constitutional register of control; recording here is what makes a party the grantor of record for everything else. Access to ownership data itself is granted by each object's holder through S1/S2 contracts, and every read is logged in S4.
