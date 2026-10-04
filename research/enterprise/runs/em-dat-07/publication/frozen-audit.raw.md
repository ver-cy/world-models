# EM-DAT-07 frozen independent semantic audit

## Verdict

Conditional accept for the Analytical Study / Finding / Recommendation binding as a non-publishable candidate. WM-ACT-036 mastership and WM-ACT-034 non-mastership are sound. Hold the identifier-unassigned Analysis Method candidate until structural remediation is applied.

## Blocking defects found

1. Claim mood and claim kind were conflated; Recommendation reuse versus specialization was ambiguous and risked accidental identity.
2. Causality gates were prose rather than profile constraints and were not conjoined with method-permitted output kinds.
3. The four-part finding pin was not executable because method, sample and dataset identity are unresolved.
4. Method-owned references to studies and findings inverted method/application separation.
5. Method lifecycle did not distinguish approval from the only pin-eligible effective state or preserve prior pins after deprecation and retirement.
6. Fixtures were specifications but appeared as if executable results.
7. Deviations were not connected to method applicability, validity conditions or output warrant.
8. Defeater semantics and rival-claim retention were absent from the profile.

## Non-blocking defects found

Reports lacked exact study/finding render pins; deontic mood was not explicitly severed from authority; recommendation/decision cardinality and rejection were unspecified; reviewer identity risked accidental scope; successor retention was incomplete; the WM-ACT-034 relation was unnamed; validity conditions and failure modes lacked consumers; source pins and crosswalks remained held.

## Applied remediation

The candidate now separates closed claimMood and claimKind discriminators and creates no Recommendation identity. It encodes the conjunctive causal gate, records unresolved pins as holds, reverses the method reference direction to study-to-method only, makes effective the sole pin-eligible state, preserves issued outputs through deprecation and retirement, labels fixtures specified-not-executed, connects deviations to applicability, models defeaters as pinned retained WM-KNW-007 claims, pins report renders, preserves rejected recommendations and predecessor findings, names WM-ACT-034 as a non-mastership mechanics contribution, and records all missing relation vocabularies as holds.

## Publication disposition

Not publishable. Internal reconciled candidate only. No runtime or model identifier is created, no fixture pass is claimed, and no canonical completeness or installability claim is made.
