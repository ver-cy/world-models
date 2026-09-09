# WM-OBJ-017 frozen subject and evidence checkpoint

The root is a reusable product configuration or variant definition, linked to
WM-OBJ-002 Product Type / Catalog Item and classifying WM-OBJ-001 instances.
The root must declare whether it is a partial configuration, a resolved
configuration or a released variant. The configurable family and its complete
option/rule space are versioned references. An individual selection session,
order, offer, inventory position and serial-numbered item remain external.

Required bundles to investigate:

1. Variant identity, family and classification: source-system ID, revision,
   variant kind, family version, SKU/GTIN/CPV scope and instance classification.
2. Feature selections: feature definitions, allowed values, units, explicit and
   inherited selections, defaults, mandatory cardinalities and provenance.
3. Configuration rules and evaluation: requires/excludes, tables, formulas,
   compatibility, partial completion, contradictions and explanation evidence.
4. Resolved physical and functional definition: dimensions, material, colour,
   ratings, interfaces, observable distinguishing features, capability and use
   limits, with nominal values distinguished from measurements of instances.
5. Design, composition and release: design/BOM references, effectivity, market
   applicability, baseline approval, revisions, substitutions and retirement.
6. Governance and interchange: ownership, access, change evidence, retention,
   mappings, conformance and semantic loss.

Source checks performed on 2026-09-07:

- https://schema.org/ProductGroup : official page fetched. ProductGroup groups
  products differing in declared dimensions; inspect ProductModel separately.
- https://ref.gs1.org/guidelines/cpv/1.1.0/ : official 30-page PDF fetched;
  release 1.1 ratified November 2024. CPV is a qualifier under a GTIN, not a
  universal identity for every engineering or commercial variant.
- https://www.iso.org/standard/70400.html : official search confirms ISO
  10007:2017; direct browser fetch failed. Full normative text not inspected.
- https://learn.microsoft.com/en-us/dynamics365/supply-chain/pim/set-up-maintain-product-configuration-model
  and https://learn.microsoft.com/en-us/dynamics365/supply-chain/pim/product-information
  : official indexed documentation supports distinct product masters, feature
  choices, constraint models and BOM selection. Treat as implementation
  evidence rather than universal normative semantics.
- https://industrialdigitaltwin.org/en/content-hub/aasspecifications : official
  discovery source found; release and metamodel details still need inspection.

Pending: complete primary-source inspection, provider results, model-specific
questions and properties, independent no-tools audit, synthesis, validation,
publication, deployment and commit. No completeness or publication claim.
