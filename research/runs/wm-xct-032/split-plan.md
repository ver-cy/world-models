# WM-XCT-032 bounded Claude research plan

WM-XCT-032 is a format-neutral mixin for carrying an exact monetary amount,
currency identity, precision and the minimum valuation/conversion context
needed to interpret it. It is researched through six bounded passes after a
larger amount pass exceeded the provider's reliable execution envelope.

1. `amount-core` owns currency identity and exact decimal representation.
2. `amount-policy` owns precision, scale, quantization, rounding, exceptional
   value states and comparison semantics.
3. `valuation` owns valuation instant/date, amount role, original/reported
   amount linkage, exchange-rate quotation and conversion reproducibility.
4. `governance-controls` owns authority, lifecycle, provenance, access,
   retention, interoperability controls and the canonical service-layer block.
5. `service-state` owns read, bind, correct, review and disposition semantics.
6. `service-calculation` owns validation, quantization, valuation, conversion,
   reconciliation, export and redaction semantics.

Each pass must be independently schema-valid and use its assigned local-ID
prefix. The deterministic merger keeps the complete boundary from
`amount-core`, service layers from `governance-controls`, remaps sources and
validates the union. The later no-tools adjudication must verify that the result remains
a host-scoped mixin rather than a currency registry, price, transaction,
accounting entry, financial instrument, market-data feed or valuation model.
