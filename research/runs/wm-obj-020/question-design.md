# Inventory Stock Position: authored structural design

Proposed six bundles, each containing two layers and one finding per layer.
Every question has its own candidate structured answer group. These are design
contracts, not executable nested schemas. Unknown is not zero. Inventory status
codes and availability formulas are source-qualified, never universal defaults.

## Position identity and custody

### Position key and aggregation grain
- Which issuer, product reference and complete dimension tuple identify this position without merging distinct lots or owners?
- Which dimensions were filtered before aggregation, which were grouped, and which were suppressed from this view?
- Does an absent row mean zero stock, an excluded dimension, no history or an incomplete response?
Candidate fields: position-key {issuer URI; product reference; dimension key/value array; identity revision}; aggregation-contract {filter expression; grouping keys; omitted dimensions; source query digest}; row-presence {state enum; completeness declaration; exclusion reason; evidence reference}.
Sources: SRC-001, SRC-005, SRC-007.

### Owner, custodian and location scope
- Who owns the stock and who holds custody, under which organization and consignment references?
- Which warehouse, bin, transit or external location is represented and which parent totals already include it?
- Which authority may disclose or change this owner's quantity without changing ownership merely because goods moved?
Candidate fields: party-bindings {owner ref; custodian ref; organization ref; consignment agreement ref}; location-scope {location ref; location kind; parent aggregation refs; inclusion rule}; stock-authority {role ref; delegated scope; permitted action; policy ref}.
Sources: SRC-004, SRC-001, SRC-009.

## Measured quantities and restrictions

### Quantity basis and measurement semantics
- What quantity, unit, precision and product-specific conversion basis does each measure carry?
- Is the value counted, measured, estimated or system-derived, and what uncertainty or rounding accompanies it?
- Are negative, zero, unavailable and unknown values permitted for this measure, and what evidence explains an exception?
Candidate fields: quantity-basis {decimal lexical value; unit code; unit system; conversion ref; precision}; measurement-method {kind enum; method ref; uncertainty; rounding rule}; quantity-state {state enum; sign policy; exception ref; source value}.
Sources: SRC-003, SRC-005, SRC-006, SRC-007.

### Stock status, condition and traceability
- Which source-defined status and lot or serial constraints qualify the reported quantity?
- Which quarantines, damage, expiry or other restrictions affect usability, and where is the authoritative evidence?
- Can status buckets overlap, and how is a transition represented without counting the same stock twice?
Candidate fields: stock-dimensions {status code; vocabulary URI; lot refs; serial refs}; usability-restrictions {restriction kind; applicable quantity; effective interval; evidence refs}; bucket-overlap {partition policy; overlap refs; transition ref; deduplication rule}.
Sources: SRC-001, SRC-005, SRC-006.

## Availability and commitments

### Reservations and usable quantity
- What physical and expected-receipt reservations apply, at which dimension hierarchy and for which demand references?
- Which versioned formula and inputs produce availability, including soft reservation offsets without duplicate subtraction?
- Is the result informational or an authoritative booking response, and what expiry and access conditions limit reliance on it?
Candidate fields: reservation-bindings {reservation refs; source bucket; hierarchy grain; demand refs}; availability-derivation {formula ref; input measures; offset mapping; version}; reliance-boundary {authority kind; calculated at; expires at; permitted use}.
Sources: SRC-001, SRC-002, SRC-008.

### Incoming, outgoing and projected position
- Which confirmed or tentative receipts and issues contribute to the selected planning horizon?
- Which forecast assumptions distinguish projected stock from current physical on-hand and available-to-promise?
- How are canceled, delayed or partially fulfilled commitments reflected without rewriting observed quantities?
Candidate fields: planned-flows {order refs; direction; quantity; due instant; commitment status}; forecast-basis {horizon; scenario ref; calculation version; certainty}; commitment-change {change ref; superseded forecast; realized portion; remaining portion}.
Sources: SRC-003, SRC-007, SRC-008.

## Observation time and reconciliation

### Snapshot currency and source ordering
- At what effective instant and recording instant was the position observed, with which explicit timezone and source watermark?
- Are all pages and dimensions from one consistent snapshot, or is consistency unknown or explicitly eventual?
- Which late, repeated or corrected source records change the interpretation, and what stale-data policy prevents treating old stock as current?
Candidate fields: snapshot-clock {effective timestamp; recorded timestamp; source sequence; snapshot ID}; snapshot-consistency {scope; page tokens; consistency declaration; missing partitions}; freshness-policy {maximum age; last sync; correction refs; duplicate handling; stale state}.
Sources: SRC-006, SRC-007, SRC-010, SRC-009.

### Count evidence and adjustment disposition
- What was independently counted, when and by whom, against which expected position and method?
- Which movements occurred between count and application, and how was the difference reconciled before approval?
- Was an adjustment proposed, approved, applied or reversed, and where is the immutable master receipt?
Candidate fields: count-evidence {count ref; counted quantity; count time; actor; expected snapshot}; discrepancy-analysis {intervening movement refs; reconciled difference; reason; unresolved amount}; adjustment-disposition {state; approval ref; master transaction ref; reversal ref}.
Sources: SRC-005, SRC-009, SRC-010.

## Change lineage and operational boundary

### Movement lineage and balance reconciliation
- Which opening position and authoritative movement records explain the closing position for the chosen dimension grain?
- Which unexplained differences, omitted events or unit conversions prevent a valid reconciliation?
- Are the evidence set and reconstruction rule complete enough to reproduce the view without claiming an event feed itself is a balance?
Candidate fields: balance-lineage {opening snapshot; closing snapshot; movement refs; reconstruction rule}; reconciliation-exceptions {difference; missing refs; conversion exceptions; disposition}; reconstruction-evidence {coverage interval; source completeness; rule version; verification result}.
Sources: SRC-001, SRC-005, SRC-006, SRC-009.

### Operational action and concurrency boundary
- Which authorized master endpoint accepts a reservation, transfer or adjustment instead of treating a local property edit as execution?
- Which expected version, action identifier and receipt distinguish a safely confirmed action from an uncertain or duplicated request?
- What must the agent do when the master rejects a request, the response is lost or another worker changed the position?
Candidate fields: action-routing {action kind; master endpoint ref; policy ref; authority scope}; action-preconditions {expected version; request ID; idempotency capability declaration; receipt ref}; uncertain-outcome {state; rejection code; reconciliation action; retry policy ref}.
Sources: SRC-007, SRC-008, SRC-009.

## Governed stock knowledge and exchange

### Mastership, access and retention
- Which source owns each measure, and which cached or federated copies are subordinate to that authority?
- Which owner, counterparty or location details may each role read, aggregate or export?
- Which records must remain reproducible after correction, deletion or access withdrawal, subject to the applicable retention policy?
Candidate fields: measure-mastership {measure ID; master ref; cache location; synchronization policy}; disclosure-scope {role ref; field scope; aggregation threshold; export restriction}; retention-contract {policy ref; evidence retention; correction chain; redaction receipt}.
Sources: SRC-004, SRC-007, SRC-009.

### Exchange fidelity and semantic validation
- Which source bucket, dimension, unit and timestamp mappings are preserved, transformed or lost in this projection?
- Can the target represent unknown or signed balances when an EPCIS quantity has different constraints, or must export be rejected or explicitly extended?
- Which subject-specific fixtures test consignment, hierarchy reservations, negative balances, concurrent counts and incomplete snapshots before an adapter is trusted?
Candidate fields: mapping-contract {source version; target version; field map; loss register}; representation-limit {unsupported value; target constraint; rejection or extension; evidence}; conformance-evidence {fixture refs; expected results; observed results; unresolved failures}.
Sources: SRC-001, SRC-004, SRC-005, SRC-006, SRC-007.
