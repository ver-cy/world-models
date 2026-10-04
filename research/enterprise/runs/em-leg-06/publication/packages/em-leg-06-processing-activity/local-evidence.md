# EM-LEG-06 reconciled local evidence

## Decision

Create one identifier-unassigned Processing Activity / Processing Register Entry candidate and profile WM-ACT-021 for Data Subject Request. Purpose and Processing Basis remain separate attributable assertions. Retention policy and instantiated duty remain mastered by WM-KNW-012 and WM-XCT-029. ROPA is a read-only projection. No model or runtime identifier is allocated.

## Reconciled semantics

ProcessingActivity has stable identity and immutable, non-overlapping revisions. Purpose, basis, party role and dataset-system location bindings are revisioned. A purpose requires an accepted basis over the same interval before activation. Consent basis cites a WM-XCT-002 instrument; withdrawal closes only assertions citing that instrument and never deletes history.

Every erasure target is a dataset-system tuple with an explicit owner and optional record set. The WM-ACT-021 profile records one outcome per tuple. Case closure does not imply universal erasure or activity retirement. Jurisdiction profiles supply deadlines, pauses and extensions; the base profile defaults to no pause.

Statutory retention floor and legal hold are distinct authority-backed constraints. If their disposition effects conflict and no precedence owner resolves them, execution is refused. Suppress-and-retain moves the required subset under a separately governed restricted-purpose ProcessingActivity with its own accepted basis and expiry.

Derived data receives the intersection of input purpose ceilings and may only preserve or narrow it. A broader analytics purpose requires a new ProcessingActivity. WM-XCT-003 can narrow shape but cannot add purpose or basis.

Durable tombstones are mastered by WM-DAT-001 or WM-REC-001 and referenced by the case. Their retention is independent of case retention. The digest covers disposition metadata, not erased payload; subject-derived digest input requires a secret key held outside the proof.

## Holds

Registry allocation is pending. Cross-model legal-hold precedence, purpose-taxonomy and ROPA-edition mastership, cohort-control and derivation-lineage mastership, processing-operation vocabulary, technical-measure ownership and jurisdiction profiles remain unresolved. WM-XCT-002, WM-XCT-003 and WM-ACT-021 remain non-canonical drafts. WM-PER-001 subject-rights overlap must be reduced to a person-to-case reference. These holds prevent publication and executable erasure claims.
