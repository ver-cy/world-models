# R2 Ledger & Account

Append-only accounts of quantity movements: any countable thing (money, goods, credits, allowances) held in accounts whose state changes only by balanced postings that are never deleted, only reversed by contra-entries. It is its own meta-model because the discipline of accounts, postings, balances and reconciliation is identical whatever the quantity, and separating it lets domain models attach meaning to movements without re-inventing bookkeeping.

## Manifest

```yaml
muif:
  version: "1.0"
metaModel:
  id: "vercy:world:r2"
  csn: world.ledgerAndAccount
  version: 0.2.0
  displayName: "Ledger & Account"
  description: "Append-only accounts recording balanced movements of quantities and the balances derived from them."
conformance:
  muc: "2.0: Conformant"
  mmas: A1
namespaces:
  - world.ledgerAndAccount
bundles:
  - csn: world.ledgerAndAccount.chart
    displayName: "Chart"
    layers:
      - world.ledgerAndAccount.chart.accountDefinition
      - world.ledgerAndAccount.chart.partyLinkage
  - csn: world.ledgerAndAccount.movement
    displayName: "Movement"
    layers:
      - world.ledgerAndAccount.movement.postingRules
      - world.ledgerAndAccount.movement.postingLifecycle
  - csn: world.ledgerAndAccount.balance
    displayName: "Balance"
    layers:
      - world.ledgerAndAccount.balance.balanceDerivation
      - world.ledgerAndAccount.balance.statement
  - csn: world.ledgerAndAccount.reconciliation
    displayName: "Reconciliation"
    layers:
      - world.ledgerAndAccount.reconciliation.matching
      - world.ledgerAndAccount.reconciliation.discrepancy
imports:
  - source: iso-20022
    version: "*"
  - source: iso-4217
    version: "*"
```

## Bundles and layers

| Bundle | Responsibility | Layers |
|---|---|---|
| `chart` | What accounts exist and whose they are | `accountDefinition`: account kinds, units of quantity, opening and closing rules · `partyLinkage`: how accounts bind to identified holders and operators |
| `movement` | How quantity moves between accounts | `postingRules`: balance discipline, authorization, value dating · `postingLifecycle`: pending, appended, reversed states and contra-entries |
| `balance` | Positions derived from movements | `balanceDerivation`: how balances are struck from the posting stream · `statement`: periodic account statements for holders |
| `reconciliation` | Agreement between records | `matching`: pairing postings against external records or counter-ledgers · `discrepancy`: raising, investigating and closing mismatches |

## Objects

- `ledger`: one append-only book of accounts for a quantity domain; key attributes: quantityUnit, operator, integrityRegime
- `account`: a holder's position container within a ledger; key attributes: accountNumber, holderRef, kind, status, openedAt
- `posting`: one balanced movement appended to the ledger; key attributes: valueDate, recordedAt, reference, reversalOf
- `postingLine`: a debit or credit leg of a posting against one account; key attributes: direction, amount, accountRef
- `balance`: a derived position of an account at a moment or period end; key attributes: asOf, amount, derivationRule
- `statement`: a periodic account report issued to the holder; key attributes: period, openingBalance, closingBalance
- `reconciliationCase`: an investigation of a mismatch between records; key attributes: scope, status, resolution
- `quantityUnit`: the unit in which the ledger counts; key attributes: unitCode, scheme, precision

## Relationships

- `account` -> heldIn -> `ledger` (many-to-one): every account belongs to one ledger
- `posting` -> composedOf -> `postingLine` (one-to-many): a posting has at least two balancing legs
- `postingLine` -> movesQuantityOn -> `account` (many-to-one): each leg debits or credits exactly one account
- `balance` -> derivedFor -> `account` (many-to-one): balances are computed views over one account's legs
- `statement` -> covers -> `account` (many-to-one): statements report one account per period
- `reconciliationCase` -> disputes -> `posting` (many-to-many): a case can span several postings and a posting can be questioned more than once

## Events

- `accountOpened`: a new account was created for a holder in a ledger
- `postingAppended`: a balanced movement was irrevocably added to the book
- `postingReversed`: a contra-entry cancelled the effect of an earlier posting
- `balanceStruck`: a balance was derived and fixed for an account at a cut-off
- `statementIssued`: a periodic statement was produced and delivered to the holder
- `discrepancyDetected`: matching found records in disagreement and opened a case
- `accountClosed`: an account was closed after settling to zero

## Contracts

- `holderAccessContract`: the account holder's standing right to view postings, balances and statements of their own accounts
- `auditorReadContract`: scoped read access for an examiner over a defined period and account set
- `interLedgerSettlementContract`: terms under which two ledger operators exchange and settle mirrored postings
- `statementDeliveryContract`: how and where statements are delivered to holders

## Projections

- `accountStatementView`: the holder's periodic view of one account; omits operator-internal codes and counterparty account detail
- `trialBalanceView`: the operator's cross-account consistency check; omits holder personal attributes
- `aggregateReportingView`: totals and flows at portfolio grain for oversight; omits person-level accounts and postings

## Composition

- EXTEND `world.registry` (R1): the book of accounts is a register whose entries are accounts with legal effect on ownership of the quantity
- REFERENCE `world.identityRegister` (R4): account holders and operators resolve to anchored identities
- COMPOSE `world.eventRegister` (R3): the posting stream is published as a sequenced, integrity-proofed event log
- REFERENCE (inbound) `world.socialProvisionAndBenefit` (B13): monetary benefit deliveries execute as postings on accounts of this model
- REFERENCE (inbound) `world.personalPropertyAndAssets` (B11): a person's financial holdings resolve to accounts kept here
- MIX-IN `world.audit` (S4): posting authorization and access carry the audit facet
- imports: iso-20022 (ALIGN): account, posting and statement semantics align with the financial message model
- imports: iso-4217 (REFERENCE): currency codes as an externally governed unit scheme for monetary ledgers

## Stewardship

The ledger operator owns the book: it guarantees append-only discipline, balance correctness and statement truthfulness, while each holder owns the view of their own accounts. Access beyond the holder's own record is granted by the operator via the S1/S2 access and consent models and audited via S4.
