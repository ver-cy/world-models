# EM-DAT-06 local synthesis

## Disposition

**COMPLETE RESERVED MODEL: WM-REC-002 Report / Statement.** The registry already reserves the correct identity and purpose. The missing specification must own the reusable report definition and the issued report statement while referencing execution, record, publication, edition and disclosure authorities.

## Identity boundaries

Owned by WM-REC-002:

- stable report-definition identity and immutable definition versions;
- parameter contract, asserted reporting grain and measure/query bindings;
- report-issue identity and lifecycle;
- reporting period, cutoff and as-of semantics asserted by the issue;
- pinned input snapshots and execution-evidence references;
- disclosure-policy provenance tuple and suppression manifest;
- correction/restatement lineage.

Referenced authorities:

- WM-ACT-053 owns processing-run execution and resolved inputs/outputs;
- WM-REC-001 owns record versions, artifacts, instantiations, fixity and retention;
- WM-ACT-044 owns publication operations, delivery and propagation of corrections;
- WM-XCT-003 owns permitted output shape and disclosure-policy semantics;
- WM-MED-003 owns bibliographic edition identity.

These identities are never interchangeable. Issuing a report is not executing it, rendering it, publishing it or assigning it an edition.

## Lifecycles

Definition version: `draft -> issued -> superseded -> withdrawn`.

Report issue: `planned -> computed -> issued -> superseded | withdrawn`.

An issued issue is immutable. Correction or changed inputs create a successor issue with an explicit restatement class and reason. The predecessor remains resolvable.

## Core invariants

1. An issue pins one report-definition version.
2. Bound parameters validate against that exact definition version.
3. Input dataset versions, partitions and digests are immutable issue evidence.
4. Reporting period, cutoff, as-of basis and issue time remain distinct.
5. Each execution reference covers the declared period or records a coverage exception.
6. Asserted grain may not exceed the applicable disclosure shape.
7. Every suppressed slice records its policy version and suppression reason without leaking withheld values.
8. A correction creates a successor; no published issue is overwritten.
9. Restatement lineage is acyclic and has one current head for a definition, parameter set and period.
10. Publication does not imply issue validity, and issue validity does not imply publication.
11. Report issue, processing run, record artifact, publication case and edition use disjoint identifiers.
12. Explanation references remain resolvable throughout the record retention period.

## Dashboard disposition

A dashboard definition is a profile of a report definition with external layout and refresh metadata. A live dashboard view is ephemeral and is not a report issue because it lacks a frozen cutoff and evidence tuple. A citable dashboard snapshot mints a report issue. WM-XCT-003 remains the authority for allowed output shape; it is not the dashboard definition itself.

## Acceptance result

Issue A pins definition v1.2, parameters, input snapshots, cutoff, as-of, run R1 and disclosure policy P7. A sensitive slice is recorded as suppressed. After an upstream correction, Issue B is created with new snapshots and run R2, explicitly superseding A. Both remain explainable; neither depends on the current dashboard configuration.

## Holds

All neighboring releases are reviewable drafts, several under single-provider waivers. Metric-definition authority is pending EM-DAT-05. Fiscal-calendar semantics need an explicit time authority. WM-XCT-003 multi-grain validation remains declarative. These holds permit a research candidate but block canonical publication.
