# EM-WRK-02 provider comparison

Claude and Grok agree on the principal boundary: reuse WM-ACT-005 as Project, retain ProjectCharter as its serial authorization artifact, profile WM-ACT-032 as ProjectChangeRequest, reduce the WM-ACT-005 change register to a projection, preserve project-product and project-tracker many-to-many relations, and allocate no new model or runtime identifier.

They also agree that charter revisions, baseline-package revisions and working-plan revisions are independent series; approved baselines are immutable; forecasts and actuals never mutate an approved baseline; a change approval authorizes but does not itself perform re-baselining; and earlier acceptance bases must survive BL-2. The shared-tracker scenario remains project-scoped and must not alter the other project's charter, package, register or acceptance records.

Grok makes the baseline split more precise. A WM-ACT-005 package must pin immutable WM-ACT-008 revisions or contain a frozen copy. It cannot reference mutable plan heads. Variance and EVM computations must name the baseline-package identifier explicitly. The transition from snapshot through package creation to switching the current pointer needs a declared atomicity contract, and package grain must state whether scope, schedule and cost can be re-baselined independently.

The material disagreement concerns WM-ACT-031. Claude accepts a discriminated union and treats acceptance as criteria, outcome, authority and evidence held by that aggregate. Grok accepts reuse only if the kinds have disjoint relation sets and Acceptance is a separate immutable record pinned to object revision, criteria revision and baseline package; otherwise Acceptance must be split from the union. This disagreement is preserved. The current candidate cannot claim the union is settled.

The reconciled disposition remains reuse/profile with no new identifier. Publication is held until the package adds immutable plan pins, an explicit baseline read path and transition contract, and resolves the WM-ACT-031 acceptance identity/lifecycle question against the full base specifications. The truncated final browser sentence adds no additional finding.
