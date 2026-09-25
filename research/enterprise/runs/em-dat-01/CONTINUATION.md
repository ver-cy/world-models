# EM-DAT-01 continuation

## State

Research contour: **Dataset, schema and contract**. Existing authorities are WM-DAT-001 Dataset and WM-DAT-004 Data Schema / Data Contract.

Local boundary review and Claude's frozen-dossier review both reject a new aggregate. Claude selected **PROFILE, no new runtime identity** because the base models contain the needed assertions but leave several cross-model obligations optional.

The exact public Grok prompt is preserved in `grok-prompt.md`. Browser submission is pending the required action-time confirmation. No Grok result exists yet, so no final publication decision has been made.

## Candidate profile

The profile would only tighten existing semantics: two-level dataset identity, distribution fixity, version-pinned conformance, distribution coherence, explicit compatibility mode and outcome, one breaking-change authority, declared consumer scope, provenance on version issue, and governed term/value-domain bindings for critical data elements.

## Holds

- WM-DAT-001 and WM-DAT-004 are published reviewable drafts with `publishableCanonical: false`.
- DataCite source versions are inconsistent.
- ODCS evidence is not fully pinned and carries a `dataProduct` deprecation issue.
- ISO/IEC 11179 evidence does not support clause-level conformance.
- DCAT-AP/DCAT-US multi-profile SHACL validation is incomplete.

These holds block a canonical normative release. They do not prevent preserving a reviewable profile draft.

## Next safe step

After authorized Grok submission, preserve the raw response and reconcile the two independent reviews. If Grok confirms portable cross-model constraints, create a minimal English Enterprise profile binding pinned to the exact WM-DAT-001 and WM-DAT-004 versions/digests, perform one frozen audit, and publish only after the base blockers are cleared. If Grok classifies the constraints as deployment policy, publish an Enterprise reuse/adoption mapping without a new runtime id.
