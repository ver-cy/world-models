# WM-DAT-008 Data Product candidate

This candidate completes the reserved WM-DAT-008 identity without allocating a new model or runtime ID. Data Product is the aggregate root. Product Catalog Record is a separately identified facet whose described resource is restricted to a product or product version, so dataset records remain WM-DAT-001-owned.

The package is declarative. It references dataset, contract, assessment, observation, interface and run masters; it does not duplicate them. Market Offering and Consumer Agreement remain external authorities.

Run `python validate_candidate.py`. Grok reconciliation and one frozen semantic audit remain required before publication.
