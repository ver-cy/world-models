# WM-FLW-012 Codex source notes

The synthesis treats Inventory Movement as one governed stock-affecting event
aggregate. GS1 EPCIS 2.0.1 and CBV 2.0 provide the strongest cross-domain event
semantics for object or class-level scope, quantities, business steps,
dispositions, locations, source and destination, event and record time, and
append-only error declarations. EPCIS visibility evidence is not assumed to be
the authoritative inventory ledger.

OASIS UBL 2.4 separates inventory reports, despatch advice and receipt advice.
Its fulfilment rules support full and partial despatch, received, short,
rejected and damaged quantities, line and handling-unit references, and
cancellation. UN/CEFACT code lists distinguish inventory direction, reason,
balance method and quantity kind; Recommendation 20 supplies unit codes. These
exchange semantics remain projections rather than universal warehouse policy.

ISA-95 and IEC 62264 support the enterprise-to-manufacturing-control boundary
and material-information references. RFC 3339, PROV-O, DQV, ODRL, XML Schema
datatypes and ISO 8000 support qualified time, provenance, quality, governed
access, typed values and master-data integrity. Industry, jurisdiction,
accounting, valuation, warehouse execution and safety rules remain explicit
profiles and holds.
