# EM-LND-03 provider comparison

Claude and Grok independently agree that Workforce Scope and Workforce Landscape are profile/projection artifacts over existing person, employment, assignment, position and organization masters. Neither provider finds independent subject identity, lifecycle or mastership; `newRuntimeId` remains false. Artifact identifiers support citation and deterministic replay only.

Both reviews keep unique persons, legal headcount, distinct employed persons, active relationships, assignments, positions, FTE and capacity as separate measures. They agree that one person employed by A at 0.6 allocated FTE and B at 0.5 remains one person, two legal relationships, one employer headcount in each perimeter, and 1.1 allocated FTE. The value is not clipped across employers. Contractors and agency workers may contribute assignments, FTE or capacity without increasing host legal headcount.

Grok sharpened seven operational gaps. The reconciled profile therefore requires immutable source, access, disclosure and calculation-engine pins and fails closed on missing pins. Every measure binds grain, denominator, time convention, inclusion predicate, source and null policy. FTE classes use explicit source precedence: assignment allocation from WM-ORG-016, authorized demand from WM-ORG-004, and any employment FTE from WM-ORG-005; classes are never coalesced into an unnamed total. Capacity is typed as person-available, assignment-available, position-authorized or unit-planned. Cross-employer roll-ups publish legal relationship headcount and anchor-deduplicated distinct employed persons separately.

The Landscape-versus-Scope distinction is now explicit. Workforce Scope is the versioned inclusion, counting, access and disclosure rule set. Workforce Landscape is the immutable result projected from one Scope revision and its pinned inputs. A change to predicates, pins, disclosure shape or engine revision creates a new version and fingerprint.

Both reviews identify disclosure risk after direct identifiers are removed. The release contract pins operational rules for small counts, deltas, cross-tabs, unusual FTE, unique affiliation patterns and release-set linkability. Person anchors are resolved inside population calculation and never emitted.

The disposition remains a held profile with no new identifier. Canonical publication still depends on the readiness and composition of WM-ORG-005/016, a normative measurement crosswalk, canonical source fixtures and validated disclosure policy.

## Frozen-audit reconciliation

The single frozen audit found six naming and rule seams. The final candidate explicitly sources the 1.1 scenario from WM-ORG-016 assignment allocations; uses only `employer legal headcount` and `consolidated distinct employed persons`; defines the deduplication anchor as transient, engine-scoped and WM-PER-001-derived; requires cross-employer access to every contributing employer; requires release-level temporal comparability; and states contractor inclusion in unique persons. No second audit was run and no identifier was added.
