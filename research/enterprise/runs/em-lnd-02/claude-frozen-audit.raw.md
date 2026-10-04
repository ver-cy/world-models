**Verdict:** ACCEPT WITH LIMITS

**Critical findings**

1. *No hidden aggregate, but two derived keys exist.* The Group Scope View digest and the Group Landscape revision are both identifiers in effect. The digest is content-addressed, master-less and non-reimportable (clause 2), and the landscape revision is configuration versioning for a governed profile (clause 1) — neither is a business-object key. They are admissible only if nothing else may reference them as foreign keys.
2. *WM-XCT-040 is cited but unused.* Composition appears in the reference set and in clause 6 ("survive composition"), yet no clause assigns WM-XCT-040 mastership of six-graph composition, typed-unknown propagation, or claim merge. Mastership of profile, subject (WM-ORG-001), relationship (WM-ORG-012), grant (WM-XCT-002) and shape (WM-XCT-003) is otherwise unambiguous; composition is the one gap.
3. *Digest input set is incomplete.* Pins cover landscape revision, world/knowledge time, scenario, graph rules, source revisions, grant set, shape and projection — but not the composition rule/engine revision. Clause 2 is worded defensively ("identical pins **and projection**"), so it does not actually claim pin-determinism. Two composition versions over identical pins yield divergent projections with no attributable pin.
4. *Digest recomputability under grant revocation is unspecified.* Grant set and shape are digest inputs while remaining external (clause 5). If a referenced grant is revoked or mutated, a prior view's digest becomes unverifiable, or verification itself requires privileged reads. This does not contradict immutability, but it is unresolved.
5. *Clause 5 and the scenario disagree on scope of grant.* Clause 5 requires grant and shape for *each cross-organization fact* in a view; the scenario restricts that requirement to "cross-company figures," implying membership edges are ungated. Membership edges are WM-ORG-012 facts and are cross-organizational.

No contradiction rises to unsafe-even-when-held. Clause 4 (parallel, non-substitutable graphs; security trust unowned; access not a graph) is internally consistent and correctly blocks membership-to-authority inference.

**Required holds**

- H1: Declare digest and landscape revision non-registrable; prohibit foreign-key reference from any business object.
- H2: Name WM-XCT-040 as master of graph composition, claim survival and typed-unknown propagation, or remove it from the reference set.
- H3: Add composition rule/engine revision to the digest input set; restate clause 2 as pin-determinism once complete.
- H4: Require grant-set and shape pins to be immutable revision references, resolvable for verification independent of current authorization state.
- H5: Reconcile clause 5 with the scenario — state explicitly whether membership edges are grant-gated.
- H6: Publication blocked until H1–H5 clear; held reviewable status is appropriate now.

**Scenario result**

Consistent. Control {S1,S2,S3} ≠ consolidation {S1,S2} correctly exercises non-substitutability; S3 is not leaked by projection. Franchisee-operated F1 in management without ownership is admissible. F3's concurrent unverified and disputed claims both persist, satisfying clause 6; excluding F3 is legitimate only with the exclusion visible in pins, and produces a new digest leaving prior views intact. The H/S1/S2 view at T/K/Base is well-formed, subject to H5.

**Identifier decision**

`newRuntimeId=false` upheld. No new runtime or model identifier is proposed or implied. Group Landscape and Group Scope View remain profile constructs over WM-ORG-001 and WM-ORG-012.
