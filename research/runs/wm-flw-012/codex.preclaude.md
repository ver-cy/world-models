# Codex pre-provider hypothesis for WM-FLW-012

## Boundary

Inventory Movement should be an event aggregate for one governed stock-affecting
change. It owns the movement identity, asserted transition, execution and posting
references, event-specific evidence and correction lineage. Inventory position,
product, lot, serial, handling unit, location, order, warehouse task, shipment,
journey, trace, ledger, valuation, document and evidence remain external masters.

## Proposed structure

1. Identity, movement class and posting boundary.
2. Stock subject, quantity and measurement.
3. Source, destination and stock-bucket transition.
4. Trigger, execution and lifecycle clocks.
5. Evidence, exceptions and reconciliation.
6. Governance, access and interoperability.

Each bundle should contain two layers and four findings. Each finding should ask
three model-specific questions and define one data element and one serial
evidence artifact. Ten functions should register, classify, bind the stock
subject, define the state transition, reserve or plan, record execution evidence,
record an external authoritative posting, reverse or correct, reconcile and
project.

## Expected hard points

- Physical movement, observation and inventory-ledger posting may occur at
  different times and must not be collapsed.
- Source and destination positions and stock buckets are references; the event
  does not own their resulting balances.
- Partial, split, merged, failed, reversed and corrected movements require
  append-only lineage and idempotency.
- GS1 EPCIS visibility events and UBL fulfilment messages are evidence or
  projections, not universal inventory-ledger authority.
- Accounting, valuation, production, warehouse, customs and sector profiles
  require separate validation and exact source-version pins.
