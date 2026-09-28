# EM-PRD-03 audit remediation

The single frozen Claude audit returned `REVISE`. All six semantic issues were remediated deterministically; the audit was not repeated.

- The latent authoritative Requirement Baseline was removed from WM-REC-006. It is now an identifier-unassigned independent-boundary candidate pending registry reservation review.
- WM-REC-006 retains only `RequirementRevisionSetView`, a derived non-authoritative identity/digest comparison with no approval, effectivity, successor lifecycle or master persistence. Diffs are always recomputed.
- Inter-Requirement Conflict was removed as a local object. Conflict identity and lifecycle belong to an external issue, case or decision master.
- Rule-pinned criteria cannot carry local predicate, unit or tolerance overrides. Conversion to a one-off informal condition removes the Rule pin, records provenance and appends a Requirement revision.
- Every Requirement-to-Requirement Trace Link has one source-revision owner. The target exposes a derived inbound projection; mirrored records are forbidden.
- Revision-set views pin identities and content digests only, never satisfaction or decision verdicts.
- Redacted views are labelled `partial-redacted`, cannot imply completeness, and reveal neither withheld identities nor counts.

Fixtures cover every correction. Reserved WM-REC-006 remains the only model completion, `newRuntimeId=false`; publication remains held and the authoritative Baseline receives no identifier here.
