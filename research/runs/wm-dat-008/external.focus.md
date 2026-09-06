# WM-DAT-008 bounded provider focus

Research one governed catalog entry that presents a data product or data offering
for discovery and controlled consumption. It is not the dataset bytes, dataset
version, data contract, schema, access service, distribution, licence, agreement,
subscription, order, delivery, quality assessment, lineage graph or usage event.

The root owns catalog-record identity and version, represented-offering identity
and product semantics, discoverability metadata, purpose, value and intended use,
domain and classifications, owner and accountable roles, dataset and service
bindings, interface and distribution descriptions, contract and quality summaries,
rights and policy references, access request and delivery terms, SLO and support
commitments, lifecycle and deprecation, provenance, feedback, usage indicators,
federation, search projections and correction history. Every authoritative peer
master retains independent identity, lifecycle and operations.

Freeze the ambiguity explicitly: a CatalogRecord describes registration metadata;
a DataProduct or offering describes an accountable reusable governed product.
The Vercy aggregate may bind both but must never collapse them, and it must not
claim that listing, availability, access authorization, delivery, acceptance or
fitness are the same state.

Known registry context:

- registry_id: vr.wm-dat-008
- parent signal: WM-DAT-001 Dataset
- candidate edge: WM-DAT-008 REFERENCE WM-DAT-001
- purpose: discoverable governed offering distinct from dataset bytes
- owner archetype: data product owner or data steward
- the candidate edge grants no approved ownership, mutation or cascade authority

Target 6 bundles, 12 layers, 24 findings, 72 discriminating questions, at least
24 artifacts and 10 functions. Prefer current primary official standards and
first-party specifications. Pin versions and declare every projection loss.

Agents must not autonomously publish restricted metadata, approve access, change
licences or contracts, subscribe consumers, deliver data, mutate datasets,
certify quality, retire services or dispose records without delegated authority.
