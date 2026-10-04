# External research focus: WM-ECO-024 Fulfilment / Delivery

Research one governed fulfilment aggregate that links an external order or obligation to promised goods, services, digital content or access and records preparation, dispatch or activation, transfer, receipt, inspection, acceptance, exception and completion evidence. Support physical-goods, service, digital, pickup, installation and multi-stage profiles without making one profile universal.

## Frozen relation and root boundary

The candidate relation ledger says WM-ECO-019 contains WM-ECO-024 fulfilment obligations; WM-ECO-024 references WM-FLW-011 shipments and WM-ECO-008 invoices. Treat all three as candidate edges requiring review, not as cascade authority.

The fulfilment root owns fulfilment-case identity and version; obligation and order-line bindings; promised subjects, quantities, conditions, destinations or service endpoints; allocation and readiness assertions; fulfilment units, splits, batches and dependencies; dispatch, handover, activation, receipt, inspection, acceptance, rejection, exception, retry and completion evidence; discrepancy, damage, shortage, substitution, delay and remedy bindings; provenance and loss-aware projections.

Keep external: purchase order and contract, party, product or service, resource and inventory, warehouse, shipment and transport execution, consignment and package, route and location, digital artifact and entitlement, appointment and work order, invoice and payment, return and refund, support case and record disposition. A fulfilment stores typed references and observations; it does not remaster these lifecycles.

Separate order acceptance from fulfilment commitment, allocation, pick or preparation, dispatch, carrier custody, delivery attempt, handover, receipt, inspection, acceptance, invoice, payment and obligation discharge. Dispatched is not delivered; delivered is not received by the intended party; receipt is not inspection or acceptance; completed is not necessarily conforming, paid or dispute-free.

Separate requested, promised, planned, readiness, dispatch, departure, arrival, attempt, handover, receipt, inspection, acceptance, rejection, completion, observation, ingestion and knowledge times. RFC 3339 timestamps require seconds and explicit offset or Z; schedules and locations need source and timezone context.

## Required outcomes

- Cover physical goods, services, digital delivery, access enablement, pickup, installation, partial, split, staged, recurring and third-party fulfilment profiles.
- Resolve order obligation, fulfilment case, fulfilment unit, shipment, package, consignment, inventory movement, service execution, entitlement, delivery proof, receipt advice, invoice, payment, return and refund boundaries.
- Cover promised and actual item, quantity, unit, lot, serial, condition, substitution, tolerance, destination, channel, endpoint and recipient.
- Cover allocation, backorder, readiness, pick, pack, dispatch or activation, custody, handover, receipt, inspection, acceptance, completion and discharge without owning warehouse, carrier or service-execution masters.
- Cover shortage, excess, damage, loss, delay, failed attempt, rejection, non-conformity, retry, reroute, cancellation, remedy, return and compensation bindings.
- Provide 6 bundles, 12 layers, 24 model-specific findings, at least 72 discriminating questions, artifacts and 10 safe functions.

Use primary official sources and pin editions. Include OASIS UBL fulfilment documents, UN/EDIFACT dispatch and receipt messages, a current traceability or delivery-event standard, sales and consumer delivery obligations, provenance, time, quality and API projections. Agents may not autonomously accept orders, allocate inventory, dispatch goods, activate entitlements, sign receipt, accept conformity, discharge obligations, issue invoices, pay, return, refund, disclose protected delivery data or dispose records without delegated authority.
