# WM-ORG-012 source inspection, 2026-09-09

Selected primary-source sections inspected, not complete normative verification.
No source prescribes this Vercy bundle design. Exact release pins, licenses,
round-trip fixtures and jurisdiction-specific legal interpretation remain holds.

## SRC-001 W3C Organization Ontology
https://www.w3.org/TR/vocab-org/

Recommendation status and sections 2.1, 2.2, 2.4, 5.2 inspected. ORG supplies
generic organization links and specialized hierarchy terms. The explicit
transitive hierarchy term must not be confused with arbitrary linkedTo edges.
Supply/funding specializations need their own semantics. ORG acknowledges that
its core does not fully model accountability/control. Version-date pin pending.
Supports kind, direction, hierarchy and proposed relationship profile design.

## SRC-002 GLEIF RR-CDF 2.1 documentation
https://www.gleif.org/content/4_lei-data/1_access-and-use-lei-data/4_level-2-data-relationship-record-rr-cdf-2-1-format/rr-cdf_version_2.1-documentation.html

Intro, release notes and abstract content inspected. Version 2.1 adds government
accounting-standard qualifier; 2.0 includes fund relation types. Records carry
related entities, relation and registration information. Rendered page does not
expose all XSD field tables: exact validation enumerations and cardinalities
must be inspected in the downloadable schema before claiming conformance.

## SRC-003 GLEIF Level 2 explanation
https://www.gleif.org/en/lei-data/access-and-use-lei-data/level-2-data-who-owns-whom

Official indexed definition and page inspected for accounting-consolidating
direct and ultimate parents. This is not a universal beneficial-ownership graph.
Source release date not pinned. Reporting exceptions must not be interpreted as
proof that an organization has no parent. Detailed exception rules still pending.

## SRC-004 Open Ownership BODS 0.4
https://standard.openownership.org/en/latest/standard/reference.html

Version 0.4 header, relationship records, components, record status, sources and
selected entity fields inspected. Relationships describe interests with distinct
subject/interested-party roles; components preserve an indirect chain. Record
closure is publisher lifecycle, not automatically termination of the underlying
interest. Unknown identities and withheld information need explanations. BODS
also covers natural persons, outside this model's organization endpoints.
The latest alias must be version-pinned before executable interchange.

## SRC-005 Open Contracting Data Standard 1.1.5
https://standard.open-contracting.org/latest/en/schema/reference/

Displayed version 1.1.5; release parties, organization references and roles
inspected. Buyer and procuring entity can differ. Role is qualified by the
contracting process, not a permanent intrinsic organizational identity.
Supports reference-only procurement links, not an entire supplier lifecycle.
Extension schemas, legal standing and all award rules were not reviewed.

## SRC-006 W3C PROV-O
https://www.w3.org/TR/prov-o/

Qualified Association definition and examples inspected. This links activity
and agent with responsibility/role/plan, not an arbitrary organization-to-
organization partnership. Use for provenance of relationship assertion work,
not an equivalent relation predicate. Full constraints and date pin pending.

## SRC-007 IETF RFC 3339
https://www.rfc-editor.org/rfc/rfc3339

Redirects to /info/rfc3339/ containing RFC text. July 2002, selected timestamp
examples inspected, including seconds, fractional seconds and UTC marker.
Use for precise observation/recording instants; do not fabricate clock precision
for date-only legal effect. Grammar/leap-second edge review remains pending.

## Legacy input and design holds

Retired stream-04 local-preflight.md read as untrusted preparation only. It has
generic candidate axes, no independent results and no frozen relationship rows.
Its obsolete Grok waiver/Claude-only wording is superseded by current policy.
Registry proposes WM-ORG-001 adjacency and siblings WM-ORG-014/015, not approved
typed composition. question-design.md is freshly authored subject structure.
External results, if any, must be validated before admission. No independent
provider agreement may be claimed from this source inspection.
