# EM-LND-03 reconciled local synthesis

## Disposition

Workforce Scope is a versioned rule artifact containing inclusion, counting, access and disclosure semantics. Workforce Landscape is the immutable generated result of one Scope revision over pinned inputs. Neither construct owns a workforce subject or lifecycle, so no runtime/model identifier is allocated.

## Mastership and pins

WM-PER-001 masters person anchors, WM-ORG-005 employment, WM-ORG-016 assignments, WM-ORG-004 positions and WM-ORG-002 unit snapshots. WM-XCT-002 and WM-XCT-003 master the access and disclosure contracts. A released view pins immutable revisions of all used sources, its Scope revision and calculation-engine revision. Missing required pins fail closed; no current-state fallback is permitted.

Scope ids and Landscape fingerprints are non-registrable artifact identifiers for citation and replay. They cannot serve as person, party, employment, assignment, position or organization keys. Published revisions are immutable.

## Measures and source precedence

Unique persons, legal headcount, distinct employed persons, active relationships, assignments, positions, FTE and capacity remain separately named. Every figure declares grain, denominator, time convention, inclusion predicate, source object, null policy, consolidation and deduplication rules.

FTE is always typed. Allocated supply FTE comes from WM-ORG-016; authorized demand FTE comes from WM-ORG-004; an explicitly defined employment FTE may come from WM-ORG-005. Different FTE classes are never coalesced or summed into one unnamed figure. Capacity is separately typed as person-available, assignment-available, position-authorized or unit-planned.

For consolidated employment, legal relationship headcount and anchor-deduplicated distinct employed persons are both published and neither is labelled only `headcount`. Vacancies can add position or authorized-demand FTE without adding a person. Contractors and agency workers can add assignment, allocated FTE or capacity without host legal headcount.

## Time, scenario and privacy

Every output records world time, knowledge time and point-in-time or interval convention. Scenario outputs remain separate from authoritative results. Person anchors are resolved internally and never emitted.

The pinned disclosure policy names cohort thresholds and suppression or aggregation actions for small counts, release deltas, cross-tabs, unusual FTE and unique affiliation patterns. It also governs release-set linkability. Unknown, suppressed and zero remain distinct.

## Acceptance scenario

Person P is employed by A at 0.6 allocated FTE and B at 0.5. The result is one unique person, two active legal relationships, legal headcount 1 for each employer, distinct employed persons 1 for the consolidated perimeter, and allocated supply FTE 1.1. The FTE is not clipped. Any person-available capacity is a different typed measure and cannot rewrite allocated FTE.

## Holds

WM-ORG-005 and WM-ORG-016 remain non-canonical and their composition relation is unapproved. Workforce measurement remains an explicit gap in WM-ORG-016 and extension-grade in WM-ORG-002. A normative FTE/headcount crosswalk, canonical source fixtures and validated disclosure-policy revisions remain required. This checkpoint makes no canonical completeness, installability or publication claim.

## Frozen-audit reconciliation

The single frozen audit found six naming and rule seams. The final candidate explicitly sources the 1.1 scenario from WM-ORG-016 assignment allocations; uses only `employer legal headcount` and `consolidated distinct employed persons`; defines the deduplication anchor as transient, engine-scoped and WM-PER-001-derived; requires cross-employer access to every contributing employer; requires release-level temporal comparability; and states contractor inclusion in unique persons. No second audit was run and no identifier was added.
