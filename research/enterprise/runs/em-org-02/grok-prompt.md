# Independent review request: EM-ORG-02 Legal Identity and Registration

Review this Enterprise boundary independently using public company-register, LEI, identifier, branch and succession practice where useful. Separate standards evidence from design inference. Do not invent a Vercy identifier.

Current candidates are non-canonical reviewable drafts:

- WM-ORG-001 Organization currently owns organization identity, status, lifecycle and some registration facts.
- WM-ORG-010 Legal Entity Registration currently treats the authority/register number as legal-person identity.
- WM-ORG-011 Business Establishment / Branch owns operating-presence semantics and lacks independent external review.

Proposed decision: **PROFILE all three, no new ID**. WM-ORG-001 becomes the single organization/legal-subject master. WM-ORG-010 is re-subjected to master registration records, each referencing exactly one subject. WM-ORG-011 is narrowed to operating presence and only references registration evidence.

Subject status, registration-record status, LEI status, tax/VAT registration, national register number and evidence extracts remain distinct. Identifier equality requires scheme + authority/jurisdiction + overlapping validity; cross-scheme equivalence is explicit and evidenced. Importing a record cannot create or merge a subject.

Test a registered branch with no separate legal personality: organization subject with `legalPersonality=false`, head-office attribution, registration record and operating presence. Registration, personality and premises are separate tests. Test succession: merger/split adds predecessor/successor edges and never rewrites historical contract parties.

Negative case: a new extract from another register creates a duplicate company. Acceptance: one subject has three registration records, a non-person branch, and a merger; as-of queries preserve historical identity and independently dated statuses.

Return at most 1000 words with: Verdict per model; subject/record mastership; identifier equality; status distinctions; branch/presence boundary; succession rules; scenario results; migration field moves; required constraints; publication blockers.
