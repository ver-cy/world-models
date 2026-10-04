# EM-LEG-06 — Grok independent review

**Verdict.** Accept with fences. ProcessingActivity needs independent identity and remains identifier-unassigned; EM-LEG-06 mints no identifier. DataSubjectRequest is a WM-ACT-021 profile. Purpose and ProcessingBasis are separate attributable assertions. RetentionRule is policy to duty/assignment under WM-KNW-012 / WM-XCT-029. ROPA is an activity projection, not a master. Consent is one basis; withdrawal is forward-only and basis-scoped. Erasure is per location. Statutory retention and legal hold preserve only the required subset under a restricted purpose. Deletion proof is tombstone plus non-reversible digest with no payload.

**Strongest evidence.** The prescribed test — one activity, mixed bases, operational erase, accounting retain-subset, analytics projection — requires a stable activity subject, split assertions, per-location effects, and ceiling-bound projections.

**Strongest counterexample.** A writable ROPA row beside the activity creates dual masters. Treating the DSR case as the activity, or case-close as erased-everywhere, leaves accounting records unjustified after close. Folding Purpose into Basis mis-applies withdrawal when consent-analytics and legal-obligation-billing coexist.

**Identity / mastership.** Independent identity is not an assigned identifier. The candidate must be referencable for assertions, duties, location outcomes, and derived ceilings. Do not invent a WM- id. Existing fences do not own it (WM-XCT-002 instruments; WM-XCT-003 shape; WM-ACT-021 cases; WM-KNW-012 / WM-XCT-029 rules and duties; WM-DAT-001/004, WM-REC-001 payload/schema/record). Activity mastership is unassigned.

**Processing activity.** One candidate type covers Processing Activity and Processing Register Entry. Activity is standing processing, not a run and not a case. ROPA is the shown projection. Writes go to activity, assertions, and duties, never to the ROPA row.

**Purpose / basis / consent.** Separate assertions on the activity; neither is a root. Consent-basis references a WM-XCT-002 instrument; EM-LEG-06 does not own the instrument. Withdrawal is forward-only and scoped to that consent-basis; concurrent non-consent bases survive. Restricted purpose is a new assertion on the same activity.

**DSR boundary.** DataSubjectRequest profiles WM-ACT-021. Case identity is not activity, instrument, or deletion-proof identity. Case may close while location outcomes remain open. Consent withdrawal is not a DSR; a case may cite it. WM-XCT-003 may shape an access or portability payload; it does not own determination. The case scopes activities by reference and does not write ROPA.

**Retention / erasure.** RetentionRule is not a new master type. Erasure is per location; global erased is a rollup. Statutory retention and legal hold are distinct triggers that may preserve only the required subset under a restricted Purpose at or below the original ceiling. After expiry: erase or re-justify; no silent purpose restoration. Deletion proof stores tombstone and non-reversible digest only.

**Projection / analytics.** Derived datasets inherit the source activity purpose ceiling. WM-XCT-003 may narrow shape and must not add purpose or basis or raise the ceiling. A wider analytics use is a new ProcessingActivity with its own Purpose and ProcessingBasis. Source erasure or hold cascades. A restricted accounting subset may feed an XCT-003 shape only inside the restricted purpose.

**Roles.** Data subject as verified party on the case; case owner (WM-ACT-021); activity steward (unassigned mastership); consent-instrument owner (WM-XCT-002); duty assignee (WM-XCT-029 from WM-KNW-012); shape projector (WM-XCT-003); record/tombstone steward (WM-REC-001). No new role types.

**Scenario.** Erasure DSR (WM-ACT-021 profile) scopes Activity A and derived dataset D. Cited consent withdrawal applies only to the consent-basis; legal-obligation basis on A survives. Operational location: erase payload; write tombstone plus digest with no payload. Accounting location: statutory duty preserves the required invoice subset under a restricted Purpose at or below A's ceiling. D inherits A's ceiling and after operational erase is erased or reduced to the accounting subset; it cannot open a wider analytics purpose. Case may close when determinations are recorded; the accounting subset remains until the duty ends.

**Invariants.**
1. ProcessingActivity is a referencable subject and remains identifier-unassigned.
2. One candidate type for Processing Activity / Register Entry; ROPA is a read-only projection, not a type or master.
3. Purpose and ProcessingBasis are separate assertions on an activity; neither is a root.
4. Consent-basis references a WM-XCT-002 instrument; WM-XCT-002 does not adjudicate non-consent bases.
5. Consent withdrawal is forward-only and scoped to that consent-basis.
6. DataSubjectRequest is a WM-ACT-021 profile; case identity is not activity, instrument, or deletion-proof identity.
7. Case closed does not mean all locations erased and does not retire the activity.
8. RetentionRule is policy to instantiated duty/assignment under WM-KNW-012 / WM-XCT-029.
9. Erasure determination is per location; global erased is a rollup.
10. Statutory retention and legal hold preserve only the required subset under a restricted Purpose at or below the original ceiling.
11. Deletion proof is tombstone plus non-reversible digest and must not contain payload.
12. Derived-dataset purpose ceiling is at or below the source-activity purpose ceiling.
13. Source erasure or hold cascades to derived datasets.
14. An activity with no current Purpose or Basis must not project as an active ROPA row.

**Minimum completion shape.** Identifier-unassigned ProcessingActivity; Purpose and ProcessingBasis as separate assertions; RetentionRule as policy to duty/assignment with distinct statutory versus hold triggers; DSR as WM-ACT-021 profile with case id, verified subject, requested right, activity refs, per-location determinations, basis/duty citations, optional WM-XCT-002 citation, proof pointers; ROPA as read-only projection; deletion proof as tombstone plus digest; derived dataset with source-activity ref and purpose ceiling; location binding present.

**Blockers.** Location owner missing. Tombstone/digest handoff to WM-REC-001 unsigned. Multi-basis compatibility and priority untyped. Legal hold and statutory retention not yet distinct triggers. Derived-dataset cascade owner unset. Production mastership of the activity candidate unassigned. Subject verification across locations outside stated fences. Conflict typing when DSR-erasure and a RetentionRule duty disagree at one location.
