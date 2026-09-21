# Record fields

All fields, exact grammars, maxima, enumerations and nullability are normative in disclosure.schema.json; no units apply except UTC-second timestamps. The following table identifies field groups and semantic ownership.

| Group | Definition / multiplicity | Writer/master / sensitivity |
|---|---|---|
| Envelope | Exactly one format/version/type/Dimension/id/revision/digest | Host-authorized record owner; metadata may be sensitive |
| Proposal capture | One author, one capturedAt, one of each five context pins | Proposal register; source truth owned externally |
| Members | 1–32 ordered members; each one key/source/schema/shape, 1–64 fields | Proposal register declares, source/schema owners attest |
| Fields | One scalar name/kind, 1–8 classification binding pins | Source and classification authorities; no payload values |
| Review | One proposal pin, reviewer, authority, method; 1–16 evidence pins | Review register; restricted attributed judgment |
| Review timing | reviewedAt ≤ validFrom < validTo, whole UTC seconds | Reviewer and trusted capture clock; not source-valid time |
| Verdict | cleared/rejected/inconclusive, one residualRisk string | Reviewer; free text may carry sensitive facts |
| Supersedes | Exactly one null or exact prior-review pin | Correction owner; same proposal identity; no implicit active-set edit |

Every independent identity may have multiple immutable revisions. Each review revision refers to exactly one proposal revision; each proposal may have zero or many reviews, with a bounded complete active set for inspection. Source/member/field relationships are embedded per revision; inverse lookups are derived, never alternate masters. Deletion and cross-register retention are outside this contract. Unknown classification/evidence cannot be represented by an empty required set; request missing context before creating a valid record.
