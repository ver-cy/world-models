# Independent review request: EM-DAT-01 Dataset, schema and contract

Act as an independent enterprise information-architecture reviewer. This is a public metamodel review; do not request or infer private company data.

Review these two existing Vercy models and the proposed Enterprise contour:

- WM-DAT-001 Dataset: https://ver.cy/models/wm-dat-001-dataset/
- WM-DAT-004 Data Schema / Data Contract: https://ver.cy/models/wm-dat-004-data-schema-data-contract/
- EM-DAT-01 assignment: https://ver.cy/enterprise/models/em-dat-01/

The target contour is **EM-DAT-01 Dataset, schema and contract**. Its scope is dataset identity and versions, distributions, schema, quality and permitted-use contract. A catalogue entry references a dataset; it is not the dataset.

Required invariants:

1. Dataset identity, dataset-version identity and distribution bytes are distinct.
2. Dataset version and schema/contract version advance independently.
3. A catalogue record describes a dataset rather than replacing it.
4. Structural schema is distinct from governed field meaning and value domains.
5. A contract identifies producer/owner, consumer scope and change obligations.
6. Compatibility is explicit and drives the dataset breaking-change indication.
7. A new dataset version preserves predecessor and provenance assertions.

Acceptance scenario: one dataset has two delivery formats and later changes schema while preserving provenance and explicit compatibility.

Local and Claude review found that WM-DAT-001 already owns dataset, version, distribution, catalogue-record distinction, fixity, provenance summary, rights and quality evidence; WM-DAT-004 already owns schema/contract versions, property structure, term/value-domain binding, compatibility modes, producer/consumer obligations and publication. Claude selected **PROFILE**, not a new aggregate, because these cross-model rules are optional in the base contracts:

- stable dataset id plus version-scoped id for each release;
- checksum for every distribution;
- version-pinned contract reference and conformance status;
- one contract version across all distributions of a dataset version;
- required compatibility mode and published compatibility outcome;
- dataset breaking flag derived from that outcome;
- declared consumer scope and change-notice path;
- predecessor plus provenance assertions on version issue;
- authoritative term/value-domain bindings for designated critical data elements.

Known release limits: both bases currently report `publishableCanonical: false` and `adjudicationStatus: reviewable-draft`; DataCite source-version consistency, ODCS source pinning/deprecation, clause-level ISO/IEC 11179 evidence and multi-profile SHACL validation remain unresolved.

Choose exactly one disposition:

- **REUSE ONLY**: the Enterprise result should be only a discoverability/adoption mapping;
- **PROFILE**: a thin version-pinned Enterprise conformance layer is justified;
- **NEW MODEL**: prove a missing aggregate with its own stable identity and lifecycle.

Check the result against DCAT 3, DQV, PROV-O, DataCite, ODCS, JSON Schema and ISO/IEC 11179 using primary sources where accessible. Be sceptical of a new runtime identity. Distinguish portable metamodel semantics from organization-specific policy.

Return no more than 900 English words with these headings:

DECISION
BOUNDARY CHECK
ACCEPTANCE SCENARIO
PORTABLE CONSTRAINTS
HOLDS
PUBLICATION RECOMMENDATION

Under DECISION state exactly REUSE ONLY, PROFILE or NEW MODEL. Under PORTABLE CONSTRAINTS retain only constraints that belong in a reusable Enterprise profile; mark the rest as deployment policy. Under HOLDS say which issues actually prevent publication and whether a non-canonical draft is still appropriate.
