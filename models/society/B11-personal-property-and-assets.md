# B11 Personal Property & Assets

The person-side view of owned things: what a person holds, how each holding was acquired and disposed of, and what encumbrances burden it. Authoritative title always lives in the relevant domain register; this model is the person's own consolidated inventory that references those registers rather than copying them. It is its own meta-model because the holder's perspective, one person across many asset kinds and registers, is a different slice of the world from any single register's perspective.

## Manifest

```yaml
muif:
  version: "1.0"
metaModel:
  id: "vercy:world:b11"
  csn: world.personalPropertyAndAssets
  version: 0.2.0
  displayName: "Personal Property & Assets"
  description: "The person's consolidated, register-referencing view of holdings, acquisitions, disposals and encumbrances."
conformance:
  muc: "2.0: Conformant"
  mmas: A1
namespaces:
  - world.personalPropertyAndAssets
bundles:
  - csn: world.personalPropertyAndAssets.holding
    displayName: "Holding"
    layers:
      - world.personalPropertyAndAssets.holding.holdingInventory
      - world.personalPropertyAndAssets.holding.titleEvidence
  - csn: world.personalPropertyAndAssets.flow
    displayName: "Flow"
    layers:
      - world.personalPropertyAndAssets.flow.acquisition
      - world.personalPropertyAndAssets.flow.disposal
  - csn: world.personalPropertyAndAssets.burden
    displayName: "Burden"
    layers:
      - world.personalPropertyAndAssets.burden.encumbrance
      - world.personalPropertyAndAssets.burden.obligationLinkage
imports:
  - source: iso-19152-ladm
    version: "*"
```

## Bundles and layers

| Bundle | Responsibility | Layers |
|---|---|---|
| `holding` | What the person currently and historically holds | `holdingInventory`: the consolidated list of holdings across asset kinds and registers · `titleEvidence`: references to register entries and documents that evidence each holding |
| `flow` | How holdings begin and end | `acquisition`: purchase, gift, inheritance and other modes of acquiring · `disposal`: sale, gift, loss and other modes of parting with a holding |
| `burden` | What limits the person's holdings | `encumbrance`: mortgages, pledges, liens and restrictions burdening a holding · `obligationLinkage`: the obligations and counterparties behind each encumbrance |

## Objects

- `holding`: one thing the person holds, as seen from the person's side; key attributes: assetKind, assetRef, share, heldFrom, heldUntil
- `assetRef`: the resolvable reference to the thing itself in its authoritative model or register; key attributes: targetCsn, targetId, registerEntryRef
- `acquisition`: how a holding began; key attributes: mode, counterpartyRef, occurredAt, considerationNote
- `disposal`: how a holding ended; key attributes: mode, counterpartyRef, occurredAt
- `encumbrance`: a burden limiting the holding; key attributes: kind, beneficiaryRef, registeredRef, createdAt, releasedAt
- `titleEvidence`: a document or register extract supporting the holding; key attributes: kind, sourceRef, capturedAt, snapshotFlag
- `portfolio`: a person-defined grouping of holdings; key attributes: name, purpose, memberHoldings
- `valuationNote`: an informal person-side value estimate; key attributes: amount, basis, notedAt

## Relationships

- `holding` -> heldBy -> `world.person` person (many-to-one): every holding names its holder
- `holding` -> refersToAsset -> `assetRef` (one-to-one): the thing itself is referenced, never copied
- `acquisition` -> creates -> `holding` (one-to-one): each holding begins with exactly one acquisition
- `disposal` -> ends -> `holding` (one-to-one): a holding ends at most once
- `encumbrance` -> burdens -> `holding` (many-to-one): a holding can carry several burdens
- `titleEvidence` -> supports -> `holding` (many-to-one): evidence accumulates on a holding over time
- `portfolio` -> groups -> `holding` (one-to-many): groupings are the person's own arrangement

## Events

- `assetAcquired`: a holding entered the person's inventory
- `assetDisposed`: a holding left the inventory
- `encumbranceCreated`: a burden attached to a holding
- `encumbranceReleased`: a burden was discharged
- `titleEvidenceAttached`: a register extract or document was captured as a marked snapshot supporting a holding
- `valuationRecorded`: the person noted an estimate of a holding's worth

## Contracts

- `inventoryAccessContract`: a scoped grant by the person letting an advisor or institution view defined holdings
- `creditorVerificationContract`: confirmation to a named creditor of one specific encumbrance and its rank, nothing more
- `successionDisclosureContract`: release of the full inventory to an authorized executor upon a registered death event

## Projections

- `netHoldingsView`: current holdings and burdens as a list; omits evidence documents and acquisition history
- `creditorView`: the one encumbered holding relevant to a creditor; omits the rest of the inventory
- `estateView`: the complete inventory with evidence, released for succession; omits nothing within its trigger's scope

## Composition

- REFERENCE `world.person` (H1): the holder is the person entity governed in its own model
- REFERENCE `world.registry` (R1): title evidence points at register entries under the generic pattern, with snapshots explicitly marked
- REFERENCE `world.landParcel` (P2): land holdings resolve to cadastre parcels and their registered rights
- REFERENCE `world.ledgerAndAccount` (R2): financial holdings resolve to accounts kept in ledgers
- REFERENCE `world.lifeEventsAndCivilStatus` (B12): succession disclosure is triggered by a registered death event
- MIX-IN `world.audit` (S4): every grant and disclosure of inventory data carries the audit facet
- imports: iso-19152-ladm (ALIGN): rights, restrictions and responsibilities vocabulary for holdings and encumbrances

## Stewardship

The person owns this inventory as their private view of the world's registers; registrars remain the owners of the authoritative entries it references. Any access by advisors, creditors or executors is granted by the person through the S1/S2 access and consent models and audited via S4.
