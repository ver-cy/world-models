# EM-TEC-04 audit remediation

The single frozen Claude audit returned `REVISE`. All twelve findings were remediated deterministically; the audit was not repeated.

- Added an effective-dated `contained-in` resource-to-environment relation and an occupant/resource environment-consistency invariant.
- Replaced timeless subject status with effective-dated `StatusAssertion` history.
- Removed lifecycle timestamp contradictions: planned records can exist before commissioning, while terminal states require close timestamps.
- Made WM-SFT-009 and WM-XCT-039 required because the candidate depends on their occurrence and projection contracts.
- Removed undated `parentResourceRef`; membership and containment use temporal relations only.
- Enumerated resource kinds and resolved cluster/node subtype endpoints.
- Replaced scalar successor fields with dated, sourced and evidenced `SuccessionRelation`; runtime-key uniqueness is locally scoped and enforced.
- Added first-class `AssetResourceEvidenceLink`; removed direct asset linkage from CI designation.
- Moved configuration authority entirely to the effective-dated designation plane.
- Added missing source, method and recorded-time fields plus append-only `CorrectionRecord` semantics.
- Enumerated desired/observed/inferred state, added functional-relation non-overlap and named observed-hosting authority.
- Expanded fixtures to 28 structured cases, including key recycling, conflicting hosting, containment mismatch, ineligible CI, asset cardinality, correction and terminal-close negatives.

Reserved WM-SFT-010 remains the only model completion and `newRuntimeId=false`. Publication remains held by missing canonical specification conversion and external dependency readiness.
