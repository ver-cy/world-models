# EM-ORG-02 local synthesis

## Disposition

- Profile WM-ORG-001 as the single master of organization/legal-subject identity, status, continuity and succession.
- Profile and re-subject WM-ORG-010 as the master of registration records, not a second LegalEntity master.
- Profile WM-ORG-011 narrowly as the master of operating presence. It references registration evidence and asserts no legal standing.
- Create no new model ID.

## Mastership

One WM-ORG-001 subject has zero or more WM-ORG-010 registration records. Each registration record has its own identity `(scheme, authority/register, assigned number)`, status, validity, evidence and observation history. Importing a registration record never creates, merges or splits a subject. Linking it to a subject is an explicit, evidenced and reversible resolution decision.

Subject status and registration-record status remain independent. LEI, tax/VAT identifiers, national register numbers and evidence extracts are different facts. Equality requires matching scheme and issuing namespace plus overlapping validity at the query time. Cross-scheme equivalence must be asserted with evidence; equal strings never prove identity.

## Branch and establishment boundary

Legal personality, registration and operating presence are three separate tests. A registered branch may lack legal personality. It is represented by an organization subject with `legalPersonality=false`, a head-office attribution, one or more registration records, and one or more operating-presence records. The head office remains the obligor unless separate authority is evidenced. A branch registration and physical presence are not one-to-one.

WM-ORG-011 owns source-defined establishment/branch/outlet presence, site bindings, local activity and availability. Its registration evidence is a read-only WM-ORG-010 reference.

## Temporal and succession rules

Every assertion separates effective, authority-recorded and observed time. Name change, seat transfer, restoration and many form conversions preserve identity when an explicit continuity decision says so. Merger, division and discontinuous redomiciliation create successor edges. Succession never rewrites historical contract parties, identifiers or evidence. Retired identities remain resolvable.

## Invariants

1. A registration record references exactly one subject; a subject has `0..n` records.
2. Registration ingestion cannot mint or merge a subject.
3. Identifier uniqueness is scoped by scheme, authority/jurisdiction and validity.
4. Registration status never substitutes for subject status.
5. Registration never implies legal personality.
6. LEI, tax/VAT and register numbers are separate qualified identifiers.
7. Evidence extracts are dated observations, not identity or current status.
8. Operating presence asserts no legal standing.
9. Succession adds edges and preserves historical parties.
10. As-of answers use assertion history rather than current state.

## Scenario result

A second register extract creates a new registration record in an unlinked state, not a duplicate company. An explicit resolution may link or reject it. One subject can carry home-register, LEI and VAT records with independent statuses. A non-person branch links to its head office, registration and presence. After a merger, current queries resolve the successor while historical contracts still name the predecessor.

## Holds

All three bases are non-canonical drafts. WM-ORG-010 must be re-subjected and its required CHILD relation replaced by an upward subject reference. WM-ORG-001/010 field and status crosswalks, branch triple-placement fixtures, identifier non-match fixtures and independent review of WM-ORG-011 are missing. Source pins and jurisdiction profiles remain incomplete. This checkpoint is not an installable release.
