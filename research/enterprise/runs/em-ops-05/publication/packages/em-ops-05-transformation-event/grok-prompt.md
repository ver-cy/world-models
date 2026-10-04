# Exact unsent Grok prompt — EM-OPS-05

Independent enterprise metamodel review. Do not browse, invent identifiers or claim publication readiness.

EM-OPS-05 covers Lot, StockPosition, TransformationEvent, Shipment and LogisticsEvent. Complete drafts cover fulfilment/delivery, physical items, stock positions, goods movements, shipments, inventory movements, supply trace, work orders and purchase/sales orders.

Assess this proposal: create identifier-unassigned Lot and Transformation Event roots; reuse WM-OBJ-020 Stock Position and WM-FLW-011 Shipment; split Logistics Event across existing observation, movement, trace and fulfilment masters; add only a thin Inventory–Genealogy binding profile. Allocate no identifier.

Separate lot, serial item, handling unit, position, work order, shipment plan, actual movement, custody transfer, receipt, inspection and acceptance. Derive balances only from declared snapshots or complete event ledgers with explicit corrections. Every transformation preserves input/output genealogy, quantities/units, yield/scrap, time/place, authority and evidence. Shipped does not mean delivered or accepted.

Test one raw-material lot through transformation into serialized assemblies, partial shipment and targeted recall. Recall proven and potential affected units without recalling the entire SKU.

Return <=900 words with: Verdict; strongest evidence; strongest counterexample; identity/mastership; lot/items/stock; transformation; shipment/movement; fulfilment/acceptance; balance/corrections; recall; time/provenance; governance; scenario; at least 10 invariants; minimum model set; blockers. Decide all five candidates and missing roots.
