Verdict: Conditionally accept. The proposal correctly keeps title, custody, operational responsibility, location and access apart; treats WM-ECO-011 as an aligned holding view only; treats WM-OBJ-022 as a projection; treats WM-ACT-007 as authorization that never proves execution; forbids silent calibration transfer on component replacement; and rejects class-level propagation. It is not accepted as stated on Custody: Custody profiles nothing in WM-OBJ-001. Three new candidates remain identifier-unassigned and cannot be mastered by the legacy objects named below.

Strongest evidence: WM-OBJ-001 is the only physical master in the given set, so an Asset Instance can be grounded there without a second physical master. WM-ECO-011 is named as an Economic Asset view, so it can align a holding interest and nothing operational. WM-ACT-007 is a Work Order, so it can authorize scope and resources only. WM-ACT-034 Assessment and WM-MAT-008 Observation can attach evidence, but neither is an execution master. WM-OBJ-022 and WM-OBJ-023 are reserved, so lifecycle must stay derived and a measuring configuration is not yet a master.

Strongest counterexample: A leased instrument of one model has its measuring subsystem replaced under a closed WM-ACT-007, and the prior certificate is still inside its stated dates. If calibration is stored on the Asset Instance shell, on the model, or copied because the order closed, the new subsystem inherits a result that never measured it, and every other instrument of that model is treated as covered. Title never left the lessor and custody never left the lessee, so economic and possession history cannot repair the false fitness claim.

Identity/mastership: Asset Instance does not receive a parallel physical identity. It profiles the WM-OBJ-001 assembly whose continuity identity survives component replacement; a component serial is never the asset identity. Custody requires an independent temporal relationship identity (holder, interval, basis), not a profile of the item. Maintenance Plan, Maintenance Event and Calibration Event each require independent identity; none may reuse WM-ACT-007, WM-ACT-034 or WM-MAT-008 as master. WM-OBJ-022 requires no independent identity. WM-OBJ-023 requires an independent configuration identity, as a specialization, because calibration binds a configuration rather than a model or an economic view.

Title/custody/responsibility: Title is the holding interest aligned only through WM-ECO-011. Custody is physical control over an interval. Operational responsibility is accountability for safe use and upkeep. Location and access are further assignments. All five may differ at the same time, and a change to one does not rewrite the others.

Component continuity: Replacement follows a versioned identity-continuity rule. The parent Asset Instance identity stays; the retired component version is frozen with its history; the replacement starts a new component version. Calibration, certificate and fitness do not move with the parent.

Maintenance plan/order/event: A Maintenance Plan is recurring intent and needs its own identity. WM-ACT-007 authorizes a bounded scope and never proves that work occurred. A Maintenance Event is the execution fact and may cite the order. An order may have zero events. Assessment and Observation may evidence an event; they do not replace it.

Calibration event/certificate: A Calibration Event binds exactly one instrument configuration to a pinned method, references, traceability chain, range, results, uncertainty, decision rule, certificate and validity conditions. The certificate is an immutable artifact of that event, not a substitute for it. WM-OBJ-023 is the configuration the event binds, not a class.

Validity/fitness: Validity is a condition of one Calibration Event on one configuration. Fitness is derived for a stated purpose from the current configuration and its validity conditions. Expiry, configuration change or purpose change drops the current fitness assertion and leaves history intact.

Scenario: A pressure instrument is leased. The lessor retains title in the WM-ECO-011 holding view. The lessee holds custody and operational responsibility; location is a third site; access is a fourth assignment. Sensor module S1 carries Calibration Event E1 and certificate C1, valid to T1. At T2 before T1, S1 is replaced by S2 under a WM-ACT-007 order. Asset Instance identity continues. S1 and E1/C1 stay bound to the retired version. S2 has no calibration. Closing the order does not create E2. At T3 after T1, even an unrestored S1 would be outside validity. Fitness for the stated purpose is not established until a new Calibration Event binds S2. No other serial of the model is affected. Title, custody, responsibility, component and suitability histories remain separately queryable.

Invariants:

1. An Asset Instance profiles exactly one WM-OBJ-001 assembly continuity identity.
2. A component serial is never adopted as the Asset Instance identity.
3. Title holder, custodian and operational responsible party may be three parties at once.
4. A custody interval does not imply title, responsibility, location or access.
5. A location or access change does not imply a custody change.
6. WM-ECO-011 never masters custody, responsibility or fitness.
7. WM-ACT-007 authorizes work and never constitutes a Maintenance Event or Calibration Event.
8. A Maintenance Event may cite at most one authorizing order; an order may cite zero events.
9. Assessment and Observation may evidence an event and never replace event identity.
10. Component replacement preserves parent identity, freezes the retired version, and never transfers calibration.
11. A Calibration Event references exactly one instrument configuration.
12. A successful calibration never covers another serial of the same model.
13. A certificate is the immutable artifact of exactly one Calibration Event.
14. Fitness is derived and purpose-scoped; expiry or configuration change invalidates the current assertion without deleting history.
15. WM-OBJ-022 is derived only and never masters identity or validity.

Minimum model set: WM-OBJ-001 Asset Instance profile; custody relationship; title alignment via WM-ECO-011; responsibility role; location and access as separate assignments; component version under identity continuity; Maintenance Plan; Maintenance Event; Calibration Event with certificate artifact; WM-OBJ-023 configuration; derived fitness assertion; WM-OBJ-022 as projection only.

Blockers: Maintenance Plan, Maintenance Event and Calibration Event are still identifier-unassigned. Custody must not be profiled onto WM-OBJ-001. No rule yet states that WM-ACT-034 and WM-MAT-008 evidence an event without becoming it. WM-OBJ-023 remains reserved and is not yet the configuration master. Until those are fixed, class propagation and silent transfer stay possible in implementation even if rejected in this proposal.
