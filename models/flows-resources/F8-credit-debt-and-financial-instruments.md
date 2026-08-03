# F8 Credit Debt & Financial Instruments

This meta-model describes claims and obligations expressed as instruments: loans, bonds, equity and similar contracts, their issuance into existence, the holdings and obligations they create between parties, the schedules that service them, the collateral that secures them, and the corporate actions that modify them. It is the credit side of finance, deliberately separated from money (F2): money is the instrument that settles, while this model carries the claims being settled. It is its own model because instruments have lifecycles (issuance, servicing, transfer, default, maturity) and inherently bilateral position semantics.

## Manifest

```yaml
muif:
  version: "1.0"
metaModel:
  id: "vercy:world:f8"
  csn: world.creditDebt
  version: 0.2.0
  displayName: Credit Debt & Financial Instruments
  description: Loans, bonds, equity and other instruments with their issuance, holdings, obligations and collateral.
conformance:
  muc: "2.0: Conformant"
  mmas: A1
namespaces:
  - world.creditDebt
bundles:
  - csn: world.creditDebt.instrument
    displayName: Instrument
    layers:
      - world.creditDebt.instrument.instrumentTypes
      - world.creditDebt.instrument.identification
  - csn: world.creditDebt.lifecycle
    displayName: Lifecycle
    layers:
      - world.creditDebt.lifecycle.issuance
      - world.creditDebt.lifecycle.servicingAndActions
  - csn: world.creditDebt.position
    displayName: Position
    layers:
      - world.creditDebt.position.holdings
      - world.creditDebt.position.obligations
  - csn: world.creditDebt.collateral
    displayName: Collateral
    layers:
      - world.creditDebt.collateral.pledges
      - world.creditDebt.collateral.valuation
imports:
  - source: iso-20022
    version: "*"
  - source: omg-figi
    version: "*"
  - source: iso-17442-lei
    version: "*"
  - source: iso-6166-isin
    version: "*"
```

## Bundles and layers

| Bundle | Responsibility | Layers |
|---|---|---|
| `instrument` | What the claim is | `instrumentTypes`: loans, bonds, equity, guarantees and their defining terms Â· `identification`: external identifier schemes for instruments and parties |
| `lifecycle` | How instruments live | `issuance`: creation of instruments and their initial allocation Â· `servicingAndActions`: interest, repayment, corporate actions and maturity |
| `position` | Who holds and who owes | `holdings`: the asset side of positions per holder Â· `obligations`: the liability side per obligor with amounts and due dates |
| `collateral` | What secures the claims | `pledges`: assets pledged against obligations Â· `valuation`: marks and margins applied to pledged assets |

## Objects

- `financialInstrument`: a claim contract in a defined form; key attributes: instrumentType, identifier (ISIN/FIGI), currency, terms.
- `issuance`: the act and record of bringing an instrument into existence; key attributes: issuerRef, issueDate, issueSize, agreementRef.
- `holding`: a party's asset position in an instrument; key attributes: holderRef, quantity, acquiredAt.
- `obligation`: a party's liability under an instrument; key attributes: obligorRef, outstandingAmount, dueSchedule, status.
- `repaymentSchedule`: the planned stream of servicing flows for an obligation; key attributes: frequency, installmentAmount, finalMaturity.
- `collateralPledge`: an asset pledged to secure an obligation; key attributes: assetRef, pledgeType, pledgedValue.
- `corporateAction`: a lifecycle modification of an instrument; key attributes: actionType, effectiveDate, terms.

## Relationships

- `issuance` -> creates -> `financialInstrument` (1:n): the instruments brought into existence by an issue.
- `holding` -> positionsIn -> `financialInstrument` (n:1): the asset side of a position.
- `obligation` -> arisesUnder -> `financialInstrument` (n:1): the liability side of a position.
- `repaymentSchedule` -> plans -> `obligation` (1:1): the servicing plan of a liability.
- `collateralPledge` -> secures -> `obligation` (n:m): pledges backing one or more obligations.
- `corporateAction` -> modifies -> `financialInstrument` (n:1): splits, calls, conversions and similar changes.

## Events

- `instrumentIssued`: an instrument came into existence and initial holdings were allocated.
- `interestPaid`: a servicing flow was paid on schedule or otherwise.
- `principalRepaid`: outstanding principal was reduced.
- `holdingTransferred`: an asset position moved between holders.
- `collateralPledged`: an asset was pledged against an obligation.
- `collateralReleased`: a pledge was discharged.
- `defaultRecorded`: an obligor failed to meet a due obligation.
- `instrumentMatured`: an instrument reached the end of its life and positions closed.

## Contracts

- `bilateralPositionAccess`: issuer and holder each read their own side of a position; neither sees the other's full book.
- `collateralStatusVerification`: a party with a legitimate interest verifies whether an asset is already pledged.
- `aggregateExposureStatistics`: sector and territory level exposure aggregates with all parties anonymized.

## Projections

- `holderPortfolioView`: one holder's instruments, holdings and expected flows; omits other holders and issuer internals.
- `issuerLiabilityView`: one issuer's outstanding instruments, obligations and schedules; omits holder identities beyond what the register requires.
- `systemicAggregateView`: anonymized totals of debt stock, maturity walls and collateral coverage for analysis; omits all position identity.

## Composition

- REFERENCE `world.agreement` (R2): every instrument is anchored to the recorded agreement that creates its obligations.
- REFERENCE `world.money` (F2): interest, principal and settlement flows are payments in the money model; amounts COMPOSE the F2 money value object.
- REFERENCE `world.landParcel` (P2): mortgage pledges attach to identified parcels and their registered rights.
- REFERENCE `world.person` (M1): natural persons as holders and obligors, resolved by reference.
- REFERENCE `world.organization` (O1): issuers, obligors and intermediaries as organizations.
- imports: ISO 20022 (ALIGN): securities and servicing message semantics.
- imports: OMG FIGI (REFERENCE): externally governed instrument identifiers.
- imports: ISO 17442 LEI (REFERENCE): externally governed party identifiers.
- imports: ISO 6166 ISIN (REFERENCE): externally governed security identification.

## Stewardship

Stewardship is bilateral: the issuer stewards the instrument and obligation records, the holder stewards its holdings, and each sees the shared position only through the bilateral contract. Access follows the catalogue's S1/S2 ownership and access models, anchored to the underlying R2 agreement, with position access audited via S4.
