# Selected primary-source evidence for WM-ORG-019

Inspected 2026-09-09 UTC. Selected clauses only, not exhaustive standards
conformance. Subject design in question-design.md is an authored synthesis.
No external provider result has been admitted at this preparation checkpoint.

## SRC-001 W3C ODRL Information Model 2.2

https://www.w3.org/TR/2018/REC-odrl-model-20180215/

Recommendation 15 February 2018, pinned dated URL. Selected sections 2.1,
2.7, 2.8, 2.10: policy/rule distinctions, atomic rule expansion, descriptive
metadata and explicit conflict strategy. ODRL's default invalid strategy is a
profile-specific rule, not a universal precedence rule for organizations.
Offers do not themselves grant rules. Mapping only selected machine-readable
clauses is plausible; full natural-language policy translation is unproven.
License and implementation conformance remain separate holds.

## SRC-002 NIST SP 800-53 revision 5

https://nvlpubs.nist.gov/nistpubs/SpecialPublications/NIST.SP.800-53r5.pdf

Revision 5, selected AC-1 at printed page 18 (PDF page 44 zero-based); source
contains December 2020 update table. AC-1 distinguishes policy from implementing
procedures and requires assigned ownership, dissemination and organization-set
review frequency/events. It contextualizes scope and higher requirements;
copying controls alone is not policy. Security/privacy context, not every
organization's binding rulebook. Further release currency and reuse review
remain open; do not claim this URL exhausts later control updates.

## SRC-003 OASIS XACML 3.0

https://docs.oasis-open.org/xacml/3.0/xacml-3.0-core-spec-os-en.html

Selected section 7.10, rule truth table and Appendix C combining algorithms:
indeterminate and not-applicable cannot be silently collapsed to permit.
Different combination strategies exist. This supports preserving evaluation
uncertainty and named algorithm profiles, not implementing a policy decision
point here. Exact release/errata and license pins still need verification.

## SRC-004 ISO/TC 176/SC2/N1286 public guidance

https://www.iso.org/files/live/sites/isoorg/files/archive/pdf/en/documented_information.pdf

Guidance on documented information for ISO 9001:2015, selected sections 2-4.
It separates maintained operational information from retained result evidence,
allows different media, and includes policy among controlled information.
This is public guidance, not the full ISO 9001 text or a certification claim.
Document issue date not established from inspected pages. Reproduction rights
are not inferred from public readability; do not vendor the standard text.

## SRC-005 University of Edinburgh policy example

https://research-office.ed.ac.uk/sites/default/files/2023-12/University%20of%20Edinburgh%20Export%20Control%20and%20Sanctions%20Policy.pdf

Version 1.0, effective 11 September 2019; section 6 records University Executive
approval on 30 July 2019, issue September 2019 and review September 2021.
Sections 1-4 and 6 demonstrate purpose, scope, related procedure and distinct
approval/issue/review metadata. Used only as a historical document-structure
example. No current export-law advice or assumption this old review date implies
expiry. Current policy status and reuse license unknown; legal content not copied.

## SRC-006 W3C PROV-O

https://www.w3.org/TR/prov-o/

Selected wasRevisionOf / qualifiedRevision definitions: version derivation can
carry provenance. A derivation or attribution link does not establish approval,
legal standing or authenticity. Dated release and license pin remain open.

## Old preparation and boundary decisions

Read the retired stream-03 codex-pre-research.md as untrusted preparation;
no provider output present there. Other five exact model run paths absent.
Its generic six-bundle skeleton and aggregate hypothesis are not adopted as
evidence. New design is policy-specific. Canonical registry has parent_ids
WM-ORG-007, but the relation ledger yields no rows for WM-ORG-019; parent meaning
must be checked before asserting EXTEND. Governance authority can reference
WM-ORG-018, with a composition mapping hold until explicitly adjudicated.

Registry lookup identifies WM-ORG-007 as Mandate / Charter, constitutive rules
of an organization. Prefer an authority REFERENCE rather than assuming policy
is a subtype of charter merely because the registry uses parent_ids.

Direct HEAD checks succeeded for SRC-001/002/003/005/006. SRC-004 HEAD was
unavailable although its PDF text was readable via web. No failure hidden.

Proposed evidence mapping for serialization: bundle 1 SRC-005/006 (approval
and versioned provenance); bundle 2 SRC-002/005 (purpose and scope), with
SRC-003 for evaluation uncertainty; bundle 3 SRC-001/003 (profiled normative
structure and conflicts); bundle 4 SRC-002/004/005 (implementation evidence,
with exception fields explicitly an authored extension); bundle 5 SRC-002/005/006
(dissemination and revision); bundle 6 SRC-004/006 for controlled provenance and
SRC-001/003 for limited machine projections. Each fine-grained node must retain
its own source refs and distinguish evidence from inferred design proposals.

Exceptions, acknowledgement distinctions, retention safeguards and agent
execution boundaries are authored design proposals requiring profile fixtures,
not direct claims that these six sources universally mandate each field.
