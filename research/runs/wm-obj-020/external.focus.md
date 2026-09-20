# WM-OBJ-020 frozen scope

Research Inventory Stock Position as an informational, time-qualified quantity
aggregate, not a physical item, warehouse, transaction or accounting valuation.
Identity includes source system, product identity, owner/custodian, location,
stock status and relevant lot/serial/variant dimensions. REFERENCE WM-OBJ-001;
do not inherit physical-item identity into an aggregate stock balance.

Distinguish physical on-hand, reserved, available and projected quantities.
No universal subtraction formula without the master's declared bucket rules;
reservations can refer to expected receipts, and statuses may overlap.
Cover unit and conversion basis, effective versus recorded time, consistent
snapshots, source sequence/watermark, stale/unknown states, counts and approved
adjustments, owner versus custodian, goods in transit, consignment, quarantine,
negative balances, reconciliation and loss-aware exchange.
Movement, reservation, order, valuation, warehouse and item masters remain
referenced. Do not claim this descriptive contract implements atomic inventory
booking, prevents overselling or authorizes stock changes.

Return a concise complete schema-valid result: 6 bundles, 12 focused layers,
12 findings with 3 discriminating questions each, typed candidate fields,
artifacts, bounded functions, composition links and all service layers.
Prefer official public inventory-system docs and standards; record exact source
versions and distinguish documented implementation practice from universality.
This is one complete bounded provider attempt, not a partial response.
