# F2 Money & Monetary Instrument

This meta-model describes money as an instrument: currencies as units of account, the concrete forms money takes (cash, deposits, electronic money), who holds how much of it, and how it moves between accounts over settlement rails. It covers the payment side of every exchange, while the goods, services or claims being paid for live in their own models. It is its own model because monetary instruments follow denomination, transferability and settlement finality rules that are independent of what the money buys, and because credit claims are deliberately separated into F8.

## Manifest

```yaml
muif:
  version: "1.0"
metaModel:
  id: "vercy:world:f2"
  csn: world.money
  version: 0.2.0
  displayName: Money & Monetary Instrument
  description: Currencies, forms of money, holdings and payments over settlement rails.
conformance:
  muc: "2.0: Conformant"
  mmas: A1
namespaces:
  - world.money
bundles:
  - csn: world.money.denomination
    displayName: Denomination
    layers:
      - world.money.denomination.currencyCatalogue
      - world.money.denomination.exchangeRates
  - csn: world.money.instrument
    displayName: Instrument
    layers:
      - world.money.instrument.instrumentForms
      - world.money.instrument.issuanceAndRedemption
  - csn: world.money.holding
    displayName: Holding
    layers:
      - world.money.holding.accountsAndWallets
      - world.money.holding.balances
  - csn: world.money.payment
    displayName: Payment
    layers:
      - world.money.payment.initiation
      - world.money.payment.clearingAndSettlement
imports:
  - source: iso-4217
    version: "*"
  - source: iso-20022
    version: "*"
```

## Bundles and layers

| Bundle | Responsibility | Layers |
|---|---|---|
| `denomination` | Units of account and their relations | `currencyCatalogue`: currencies, minor units, issuing authorities · `exchangeRates`: quoted rates between currency pairs over time |
| `instrument` | The forms money takes | `instrumentForms`: cash classes, deposit balances, electronic money and their transferability · `issuanceAndRedemption`: how instrument stock enters and leaves circulation |
| `holding` | Who holds what | `accountsAndWallets`: containers in which instruments are held · `balances`: quantified holdings at points in time |
| `payment` | How money moves | `initiation`: payment orders, purposes and parties' account references · `clearingAndSettlement`: rails, finality rules and settlement outcomes |

## Objects

- `currency`: a unit of account; key attributes: alphabeticCode, minorUnit, issuingAuthorityRef.
- `monetaryInstrument`: a concrete form of money; key attributes: form, denominationCurrency, transferability.
- `account`: a container in which instruments are held for a holder; key attributes: accountId, schemeRef, status.
- `holding`: a quantified balance of an instrument in an account; key attributes: amount, asOfTime.
- `payment`: a transfer of value from one account to another; key attributes: amount, currency, purposeCode, status.
- `settlementRail`: infrastructure that clears and settles payments; key attributes: railType, operatingCalendar, finalityRule.
- `exchangeRateQuote`: a rate between two currencies at a moment; key attributes: baseCurrency, quoteCurrency, rate, quotedAt.

## Relationships

- `monetaryInstrument` -> denominatedIn -> `currency` (n:1): the unit of account of an instrument.
- `holding` -> heldIn -> `account` (n:1): where a balance sits.
- `holding` -> of -> `monetaryInstrument` (n:1): which instrument a balance is made of.
- `payment` -> debits -> `account` (n:1): the paying side.
- `payment` -> credits -> `account` (n:1): the receiving side.
- `payment` -> settledVia -> `settlementRail` (n:1): the rail that carried the transfer to finality.
- `exchangeRateQuote` -> quotesPair -> `currency` (n:2): the base and quote currencies of a rate.

## Events

- `instrumentIssued`: new instrument stock entered circulation (notes issued, deposits created, e-money loaded).
- `instrumentRedeemed`: instrument stock left circulation.
- `paymentInitiated`: a payment order was placed against an account.
- `paymentSettled`: a payment reached finality on its rail and balances were updated.
- `paymentReturned`: a payment was rejected or reversed before or after settlement.
- `rateQuoted`: an exchange rate between two currencies was recorded.

## Contracts

- `holderBalanceAccess`: a holder or their delegate reads holdings and statements for the holder's own accounts.
- `paymentStatusInquiry`: a party to a payment queries its lifecycle status.
- `aggregateFlowStatistics`: a consumer receives rail-level volumes and values with no party identification.

## Projections

- `holderStatementView`: one holder's accounts, balances and payment history; omits all other parties' data.
- `railThroughputAggregate`: volumes, values and settlement times per rail and period; omits individual payments and parties.
- `currencyReferenceList`: public catalogue of currencies and reference rates; omits everything transactional.

## Composition

- REFERENCE `world.person` (M1): natural persons as account holders, resolved by identity reference, never inlined.
- REFERENCE `world.organization` (O1): rail operators, issuing authorities and organizational holders.
- REFERENCE `world.creditDebt` (F8): interest, principal and settlement flows of credit instruments appear here as payments; the claims themselves live in F8.
- REFERENCE `world.agreement` (R2): a payment may discharge an obligation arising under a recorded agreement.
- This model's money amount is a value object designed for COMPOSE by sibling models (freight charges in F3, fares in F7, cash flows in F8).
- imports: ISO 4217 (REFERENCE): the externally governed currency code scheme, carried by scheme and version rather than copied.
- imports: ISO 20022 (ALIGN): field equivalences with payment initiation and settlement message semantics.

## Stewardship

Each holding is stewarded by its holder, and each rail's operational records by the settlement rail operator archetype. Access to balances and payment histories is granted only by the respective steward through the catalogue's S1/S2 ownership and access models, with usage auditable via S4.
