# External research focus: WM-LIV-001 Taxon

Research a vendor-neutral model of a taxon concept, not an organism, specimen,
occurrence record, scientific name alone, conservation assessment or generic
classification scheme.

Use primary official sources. At minimum assess TDWG TCS and Darwin Core,
Catalogue of Life ChecklistBank, GBIF species services, NCBI Taxonomy, the
applicable nomenclatural codes and RFC 3339. Preserve disagreements among
classifications and code-specific semantics.

Cover stable concept identity and according-to source, circumscription,
scientific and vernacular name usages, nomenclatural status and type references,
rank and parentage, classification path, uncertain placement, split and lump
history, cross-classification mappings, diagnosis and evidence, stewardship,
version lifecycle, access, retention and interoperability projections.

Distinguish accepted-name status relative to a source from universal truth.
Distinguish a taxon concept from its attached name usages. Do not import the
lifecycle or direct physical properties of organisms, specimens, sequences,
occurrences, habitats or populations into the taxon model.

The model must be agent-native: include the five-facet assessment, safe
functions, explicit uncertainty, source and master-system references, immutable
published versions, seconds-and-offset RFC 3339 event timestamps, validation,
access, retention and an AGENTS.md bootstrap route.

Target a compact but deep structure of about 7 bundles, 16 layers, no more than
32 findings, exactly 3 useful questions per finding and 10 to 12 functions.
Return only the required research JSON contract.
