# EM-WRK-02 frozen-audit remediation

The independent frozen audit returned `ACCEPT WITH LIMITS`. The profile keeps `newRuntimeId=false` and addresses its portable semantic findings as follows.

1. A baseline package is a project-scoped sub-entity of WM-ACT-005. It is one atomic approved release across its declared scope, schedule and cost dimensions; a partial rebaseline produces a complete successor package that reuses unchanged pins.
2. A package may pin immutable WM-ACT-008 revisions. Any embedded snapshot is explicitly a non-authoritative copy carrying the source revision and digest and cannot replace WM-ACT-008 mastership.
3. The draft package in WM-ACT-005 owns the frozen selection record. The selection contains references and digests, not copied authority.
4. WM-ACT-031 masters criteria revisions with the milestone or deliverable record. Milestone, Deliverable and Acceptance have independent record identities and revision series inside the shared aggregate.
5. Re-baselining does not reopen Acceptance by default. Re-verification requires an explicit impact assertion from the approved change request.
6. Only an approved request classified for re-baselining can create BL-2 or later.
7. Milestone achievement needs an independently recorded achievement status, effective time, authority and evidence; task completion alone cannot establish it.

Standing canonical holds remain visible: the base specifications are reviewable drafts, relation/source/base corrections are outstanding, and publication cannot claim canonical completeness or installability.
