# WM-FLW-011 Codex source notes

The synthesis follows the strongest cross-domain distinction found in primary
sources. UN/CEFACT and WCO describe a shipment as the trade or goods view of
what is shipped and a consignment as the transport-contract view of how goods
are shipped. OASIS UBL 2.4 confirms that the relationship is many-to-many under
split and consolidated transport. The Vercy aggregate therefore requires a
mandatory semantic kind and never treats one term as a universal alias for the
other.

UN/CEFACT BSP-RDM, SCRDM, Integrated Track and Trace and Shipping Instructions
support parties, items, packages, transport services, locations, requirements,
status and document bindings. WCO supports the customs boundary. GS1 EPCIS and
CBV support source-qualified visibility events, IATA ONE Record supports an
air-cargo projection, and DCSA Track and Trace supports a container-shipping
projection. These modal and jurisdictional sources are alignments, not universal
rules.

UN/LOCODE, Recommendations 20 and 21 and ISO/IEC 15459-1 support locations,
units, cargo/package types and transport-unit identities. RFC 3339, PROV-O, DQV
and ODRL support qualified clocks, provenance, quality and governed disclosure.
The model remains format-neutral and keeps external master lifecycles outside
its boundary.
