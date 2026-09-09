# WM-OBJ-020 source inspection and limitations

Inspected 2026-09-09 through web search/open/find. Only selected passages are
admitted, not whole-document or implementation conformance. Vendor behavior is
counterexample evidence, not a universal inventory standard. No adapters or
transactional stock system were executed. The candidate field groups in
question-design.md are proposed Vercy contracts, including explicit unknowns.

## SRC-001 Microsoft: Inventory on-hand list
https://learn.microsoft.com/en-us/dynamics365/supply-chain/inventory/inventory-on-hand-list
Public documentation inspected 2026-09-09; exact page revision to pin later.
Indexed article text inspected: dimension filtering and grouping, quantity
columns, reservation hierarchy, retained empty rows. Aggregate totals depend
on grain. Reservation rows need not be at physical-stock grain. Supports
identity and aggregation contracts; no universal summation across all rows.

## SRC-002 Microsoft: Reserve inventory quantities
https://learn.microsoft.com/en-us/dynamics365/supply-chain/inventory/reserve-inventory-quantities
Public documentation inspected 2026-09-09; exact page revision to pin later.
Indexed text inspected: reservations may concern physical or ordered stock.
Reservation is not proof of physical availability. This source does not define
Vercy's approval policy or implement its reservation adapter.

## SRC-003 Odoo: Stock report
https://www.odoo.com/documentation/18.0/applications/inventory_and_mrp/inventory/warehouses_storage/reporting/stock.html
Odoo 18.0. Indexed passage inspected from official-domain search result; direct
open timed out. On-hand, free-to-use, incoming, outgoing and forecast are
different measures. Selected text only; do not claim a full direct read.

## SRC-004 Odoo: Consignment
https://www.odoo.com/documentation/18.0/applications/inventory_and_mrp/inventory/shipping_receiving/daily_operations/owned_stock.html
Odoo 18.0. Indexed article text inspected: storage and ownership can differ;
owner appears in stock reports, while consignee valuation excludes these
goods. This is implementation evidence, not legal title or accounting advice.

## SRC-005 Odoo: Inventory adjustments
https://www.odoo.com/documentation/18.0/applications/inventory_and_mrp/inventory/warehouses_storage/inventory_management/count_products.html
Odoo 18.0. Indexed article text inspected, including counted versus recorded
quantity, unapplied count, intervening moves and reversal history. Negative
recorded balances can appear. Count time and application are distinct; an
observed discrepancy is not itself an authorized adjustment.

## SRC-006 GS1: EPCIS
https://ref.gs1.org/standards/epcis/2.0.1/
The URL resolves to a 229-page PDF whose visible header says Release 2.0,
Ratified June 2022. Preserve this label versus URL-version distinction.
Selected parsed sections 7.3.3.1 and 7.4.1 inspected: class-level quantities
and unit constraints; eventTime versus repository recordTime. An EPCIS event
feed is not automatically a complete stock balance. Signed or zero stock
balances cannot be blindly mapped to positive QuantityElement values. Omitted
quantity is unknown/unspecified. Exact adapter/profile validation remains open.

## SRC-007 Microsoft: Inventory Visibility public APIs
https://learn.microsoft.com/en-us/dynamics365/supply-chain/inventory/inventory-visibility-api
Page updated 2026-03-10. Opened and selected query contract/examples inspected:
source-qualified measures, groupByValues, dimensions and returnNegative.
Find returned no idempotency statement. Expected-version and retry contracts
are proposed Vercy safeguards, not claims that these APIs guarantee them.

## SRC-008 Microsoft: Inventory Visibility reservations
https://learn.microsoft.com/en-us/dynamics365/supply-chain/inventory/inventory-visibility-reservations
Public documentation inspected 2026-09-09; exact page revision to pin later.
Indexed selected mapping/formula passage inspected: physical measures and
calculated availability are configured; soft reservations need offsets.
Avoid hard-coded global availability arithmetic and duplicate subtraction.

## SRC-009 W3C: PROV-DM
https://www.w3.org/TR/prov-dm/
Recommendation 2013-04-30. Public page opened; attribution and derivation are
alignment candidates. No inventory-specific access grant or correctness proof
follows from provenance metadata. Full mapping and application tests remain.

## SRC-010 IETF: RFC 3339
https://www.rfc-editor.org/rfc/rfc3339
RFC 3339, July 2002. Public page opened. Use explicit timestamp offset and
seconds; identifiers, ordering, interval semantics and snapshot consistency
require separate contracts. A timestamp alone cannot prevent duplicate actions.

## Mandatory holds for any publication

- Independent external review absent unless a provider actually validates.
- Exact mutable Microsoft revision pins and direct source checks remain open.
- Odoo stock-report direct fetch unavailable; selected indexed text only.
- No executed inventory engine, nested instance schema, concurrency test or
  adapter conformance; all functions proposed and authority-bounded.
- Warehouse/industry unit, negative-stock, quarantine and consignment profiles
  require specialist validation. Do not infer physical characteristics of an
  informational stock aggregate; reference product/item master descriptions.
- Freeze source-result digest before a separate no-tools self-audit; do not
  conflate a source-grounded design with complete coverage or canonical status.
