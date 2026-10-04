# EM-DAT-03 audit remediation

The frozen audit returned `REVISE` because the packet did not name the master for a manual correction activity, used aggregate-root language at two levels and left dependent keys implicit. The candidate is revised without adding a model:

- WM-XCT-012, already an explicit external base, masters the provenance Activity record for C1, including activity identity/type, agent association, time, inputs/outputs and supporting evidence references.
- The correction's processing-context fragment is WM-DAT-006 evidence bound to that WM-XCT-012 activity; it is not an independent manifest aggregate.
- WM-DAT-006 is called a mastership boundary, not an aggregate root. Assertion keys and supersession pointers are local dependent-record keys inside that boundary and are never runtime/model identifiers.
- Logic hashes and locators are value attributes. Sharing a digest does not create identity.

The audit's external obligations remain explicit holds: WM-DAT-001/004 must accept snapshots produced by failed attempts and WM-XCT-012 activities; WM-XCT-012 evidence references must resolve the ticket or patch record rather than copying its authority. No second audit is run because the program permits one frozen audit per contour; the remediation is mechanical, reviewable and retained beside the audit.
