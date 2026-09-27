**Verdict:** REVISE

**Critical findings**

1. *Unmastered evidenced activity (blocking).* Clause 2 allows an assertion's producer to be "a producing task/attempt **or evidenced activity**," and clause 6 makes C1 exactly such an activity with actor, time, evidence and "its own manifest fragment." But clause 1 gives WM-ACT-053 only "one run plus its ordered attempts and outcomes," and clause 5 pins manifests to run execution. Nothing in the reconciled boundary masters C1 or its manifest fragment. A load-bearing producer reference pointing at an undeclared entity is precisely how a fourth aggregate enters despite `newRuntimeId=false`. This must be resolved textually, not by reviewer inference.

2. *Level conflation in WM-DAT-006.* "Lineage model/root boundary" fuses a model-scope claim with aggregate-root vocabulary — the same vocabulary the reconciliation denies to assertions. The substance is defensible (mastership boundary owning dependent records) and is faithful to both providers: Grok's denial of a third aggregate holds, while Claude's operational needs — addressability, own append-only state, supersession — are preserved without conferring aggregate status. The wording, not the logic, is incoherent; drop root-of-aggregate phrasing for WM-DAT-006.

3. *Identifier surfaces introduced without declaration.* Addressable assertion records plus supersession links imply keys; clause 3's content hash implies a resolvable handle. Both are defensible as dependent keys and value attributes respectively, but the profile asserts `newRuntimeId=false` without saying so.

4. *Non-contradictory but unfunded external obligations.* Clause 7 (partial output of a failed attempt gets external snapshot identity) and clause 6 (Xout@s2 distinct, s1 unrewritten) require WM-DAT-001/004 to admit snapshots whose producer is a failed attempt or a manual activity. Clause 2's evidence/confidence and clause 6's ticket-patch citation depend on WM-XCT-012 shapes not quoted here.

**Required holds**

- H1: Declare the master of manual/evidenced activities and of non-run manifest fragments; either widen WM-ACT-053 explicitly or bind the fragment as WM-DAT-006 evidence. No publication until resolved.
- H2: State that assertion keys and supersession pointers are allocated inside WM-DAT-006's dependent-record scope; state that the logic hash is a value attribute, not an entity key.
- H3: Base-model edit, WM-DAT-001/004 — snapshot provenance must admit failed-attempt partial outputs and manual-correction producers.
- H4: Confirm WM-XCT-012 provides actor/time/ticket/patch and confidence citation shapes; otherwise evidence structure is invented.
- H5: Replace aggregate-root wording for WM-DAT-006 with mastership-boundary wording.

**Scenario result**

Passes on every axis except H1. M1 survives A1→A2 unreplaced; no new run is minted on retry; A1's durable partial output is isolated under its own external identity; Xout@s1 is superseded-by-new-snapshot rather than mutated; R2 reads s2 under M2 without back-writing R1 or C1; Xin remains a boundary node with unresolved ancestry and confidence impact, no synthetic upstream. C1's trace is structurally correct but its producer resolves to nothing declared.

**Identifier decision**

No new runtime or model identifier is warranted, and none is required by the scenario. `newRuntimeId=false` is sustainable **only** after H1 and H2; if C1 resolves by creating an activity entity, the claim fails and the profile returns as a boundary change. No publication authority granted.
