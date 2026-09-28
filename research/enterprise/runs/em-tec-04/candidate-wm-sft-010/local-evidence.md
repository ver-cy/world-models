# EM-TEC-04 local synthesis

## Disposition

Complete reserved WM-SFT-010 as Runtime / Compute Environment. Allocate no new model or runtime identifier.

WM-SFT-010 masters RuntimeEnvironment and InfrastructureResource. `RuntimeOccupantRecord` is a dependent as-of observation bound to exact WM-SFT-002 and WM-SFT-009 references; it is never a gold-copy subject. WM-SFT-009 owns deployment occurrence and desired placement. WM-XCT-039 owns projection and completeness semantics.

Configuration control is an effective-dated designation over explicitly eligible subjects. Asset and resource identities remain separate and join only through `AssetResourceEvidenceLink`. Region, environment, cluster, node and occupant layers are distinct.

## Reconciled semantics

- Temporal `contained-in`, `member-of` and `runs-on` edges distinguish environment composition, cluster membership and occupant hosting.
- Effective-dated StatusAssertion records replace timeless lifecycle status.
- Runtime keys are locally unique within authority and scope for all retained time; tombstones and dated SuccessionRelation records preserve history.
- Declared placement and observed hosting can disagree without overwriting each other.
- Corrections append records and preserve prior assertions.
- CI withdrawal never destroys the subject; physical and financial assets stay externally mastered.

## Verification

Candidate `0.1.0-candidate.3` validates 27 invariants, four external boundaries and 28 fixtures. The exact Grok Heavy response returned accept-with-conditions. One frozen Claude Opus high no-tools audit returned REVISE; twelve findings were remediated once and the audit was not repeated.

## Holds

Canonical specification conversion, retained dependency holds, a pinned tombstone-retention policy, package construction and live HTTP/runtime/search/package verification remain required. This checkpoint does not claim canonical completeness or installability.
