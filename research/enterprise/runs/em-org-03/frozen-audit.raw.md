# Frozen audit — EM-ORG-03

## Verdict

**Disposition: sound. Package: not verification-ready.**

The core calls are correct and I would not reopen them: Share Class as the only new master, held identifier-unassigned; Ownership Interest and Control Relation as disjoint typed profiles over WM-ORG-012 with `controls=true` forbidden; Governance Body reusing WM-ORG-018; Resolution as a composition with no minted identity; mandatory procedure evidence; failed quorum preserved-but-not-adopted; signing authority never derived from ownership. `modelId`/`registryId` null, `allocationState: "unassigned"`, `canonicalPublishable: false`, `newRuntimeId: false`, `publishable: false` are mutually consistent and no identifier is guessed.

What fails is enforceability, not judgement. A large fraction of the stated invariants have no field, no object, no base model, or no fixture behind them — including the entire calculation contract, which exists only as prose. Several load-bearing model references appear in one artifact and nowhere else. The package should not advance to canonical reconciliation until D1–D24 are closed.

---

## Material defects

### Share Class identity, lifecycle, versions

**D1. `amended` is a class state.** `ShareClass.lifecycle` and `identityTest.independentLifecycle` both include `amended`, which is a version event, not a state of the issuer-side identity; a class stays active while versions append. `issued` and `active` are also undifferentiated, and no transition rules are declared.
*Remediation:* remove `amended` from both lifecycle lists so amendments are expressed only as appended `ShareClassVersion` records; either distinguish `issued` from `active` or collapse them.

**D2. Authority evidence is single-valued and on the wrong object.** `authorityRef` is required on `ShareClass`, untyped (no target model declared), and absent from `ShareClassVersion` — so the amendment path, which is where rights actually change, carries no authority at all. The invariant demands four things (effective in-scope Mandate, competent decision, authentic record, mandatory procedure evidence) and no field holds them. WM-ORG-007 is cited by that invariant but is missing from `boundary.references`.
*Remediation:* replace `authorityRef` with a required authority bundle on `ShareClassVersion`, gating `approved` → `effective`, holding refs to WM-ORG-007, WM-KNW-010, WM-REC-010 and WM-ACT-025; add WM-ORG-007 to `boundary.references`.

**D3. Designation uniqueness is prose only.** "A class designation is unique only within its issuer" is stated as an invariant but has no constraint and no temporal scope, so a cancelled class's designation cannot be legitimately reused.
*Remediation:* add: `(issuerRef, classDesignation)` unique per issuer across non-overlapping effective intervals; designation is never an identity component.

**D4. Pins are not reproducible.** `contentDigest` is required but no canonicalization or algorithm is named, and the class-version pin is described everywhere as "pinned Share Class version" without the digest — so a re-approved version silently changes what a past calculation resolved to. `ShareClassVersion` also has valid time only (`validFrom`/`validTo`) and no knowledge time, while every calculation must declare knowledge time; a retroactively corrected rights schedule therefore cannot be replayed.
*Remediation:* define the pin as `(shareClassId, version, contentDigest)` with a named canonicalization, and add a recorded/knowledge interval to `ShareClassVersion` with corrections appending a new version rather than editing one.

### Rights and denominator semantics

**D5. The treasury/denominator invariant is unenforceable.** `denominatorPolicyRef`, `authorizedQuantity` and `issuedQuantityRule` are all `optional`, yet "Treasury and suspended holdings follow an explicit denominator and voting rule" is mandatory. There is also no outstanding-quantity concept anywhere, so percentage-of-class denominators have no source.
*Remediation:* make `denominatorPolicyRef` and `issuedQuantityRule` required for any version in `effective` status, and define outstanding = issued − treasury − suspended, per version and instant, as the denominator source.

**D6. `rightsSet` is opaque.** "Economic, capital, voting, conversion, transfer and priority rights remain distinct" has no structural expression, and `votesPerUnit` is named in `boundary.owns` but appears in no object. Fixtures `economic-equals-votes` and `different-vote-ratios` cannot be mechanically evaluated against an unstructured blob.
*Remediation:* decompose `rightsSet` into separately named, independently effective-dated right-type entries, with `votesPerUnit` under voting.

### Calculation, assertion and derivation

**D7. The calculation contract has no object.** `objects` defines only `ShareClass` and `ShareClassVersion`; the profile candidate defines no object at all. Every requirement about derived claims — labelled, reproducible, input-pinned, cycle-convention-bearing — has no schema, so no fixture about it can ever execute.
*Remediation:* define one derived-claim structure in the profile candidate whose required fields are exactly the declared pin set.

**D8. The two artifacts mandate different field sets.** The allocation invariant requires right type, class version, denominator, valid time, knowledge time, scenario, rule version and inputs; the profile constraint additionally requires cycle convention and tolerance on *every* calculated claim. A validator built from either artifact rejects claims the other accepts.
*Remediation:* make one list normative and have the other reference it rather than restate it.

**D9. Cycle handling is under-specified.** "Declared cycle convention and tolerance" names no closed vocabulary of permitted conventions, no maximum iterations or divergence handling (tolerance alone does not guarantee termination), and does not require the detected cycle membership to be recorded — so an unresolved case is indistinguishable from a truncated one.
*Remediation:* enumerate conventions as a versioned closed list; require `maxIterations` with non-convergence yielding `unresolved`; require `cycleSet` and iteration count on the claim.

**D10. The calculation-context vocabulary has no owner.** `scenario`, `ruleVersion`, `denominatorPolicy` and `cycleConvention` carry the weight of "one scenario uses one cycle convention" and "results under different conventions are incomparable", but none is bound to a model, registry or identity scheme — equality is being tested on free-text labels.
*Remediation:* declare a single owner for this vocabulary (a named model or an explicit hold with a reserved placeholder namespace) and require identities, not labels.

**D11. Third-party asserted percentages have no home.** The package recognises only asserted holdings and derived percentages. A percentage asserted by a filing or regulatory disclosure is neither, and would be mis-stored as a derivation or as a holding — defeating invariant 4 and the assertion/derivation separation.
*Remediation:* add an asserted-claim category with source, basis, valid and knowledge time, distinct from derivation, with neither able to overwrite the other.

### Ownership Interest versus Control Relation

**D12. Asymmetric profile-instance identity.** `profileRoles.ControlRelation` gets "its own profile-instance identity"; `OwnershipInterest` gets "no new model identity" and nothing else. But the invariants require an ownership instance to bind holder, issuer, pinned version, quantity, time and scenario, and `typed-profile-separation` requires ownership and control instances to be independently addressable.
*Remediation:* state OwnershipInterest's profile-instance identity in the same terms as ControlRelation's, still with no WM identifier.

**D13. Dual mastership has no split rule.** Ownership Interest spans WM-ECO-038 and WM-ORG-012 while "retaining" both masterships, with nothing saying which side owns quantity and the class-version pin — permitting two divergent copies.
*Remediation:* state that quantity and class-version pin are mastered only on the WM-ECO-038 position and that the WM-ORG-012 ownership facet carries no quantity or percentage.

**D14. Holder capacity is unbound.** Registered holder, beneficial owner, economic-interest holder, nominee, custodian and manager are declared "separate capacities" in the local evidence, but no field requires capacity and no rule governs aggregation across capacities — nominee plus beneficial over the same units sums to double.
*Remediation:* require `holderCapacity` on every Ownership Interest and forbid aggregating distinct capacities over the same units absent a declared rule.

**D15. Natural-person holders have no base.** WM-ORG-012 is described as *inter-organizational* qualified relations, yet individuals hold shares. Under the present shape an individual's holding either fabricates an organization or cannot be expressed.
*Remediation:* restrict the WM-ORG-012 ownership facet to organization-to-organization links and state that natural-person holdings are carried by the WM-ECO-038 position alone.

### Governance Body, membership, procedure

**D16. WM-ORG-006 is an unsupported reference; seat has no carrier.** "Appointments profile WM-ORG-006 with party, seat, term, authority and source record" appears only in the local evidence — WM-ORG-006 is absent from `bases`, `profileRoles`, `boundary.references` and the provider comparison, so it is unreconciled. Relatedly, "seat, office, member and person are distinct" and "body and seat persist" have no seat identity anywhere.
*Remediation:* either add WM-ORG-006 to `bases` with an Appointment profile role that carries a seat identity, or delete the sentence and record appointment/seat as an open hold.

**D17. The governing procedure has no base.** Quorum and voting eligibility are assigned to "the governing procedure", but WM-ACT-025 is evidence of a procedure *instance*, not the normative rule. The rule source (charter, bylaws, standing orders) is unmastered, so the constraint cannot be satisfied.
*Remediation:* name the model that masters governing-procedure rules, or add an explicit hold marking the quorum/eligibility constraint unenforceable until it is named.

**D18. The corporate-action / transaction boundary is never named.** Both `resolution-mutates-holding` ("execution requires the appropriate corporate-action or transaction boundary") and class conversion, replacement and cancellation depend on a boundary model that no artifact names or holds.
*Remediation:* add an explicit hold naming it as unassigned and mark the dependent fixture expectation unevaluable until then.

**D19. Membership intervals lack overlap and containment rules.** "Interval-valued" is asserted, but nothing forbids two open memberships on the same `(body, seat)` at one instant, nothing requires an appointment interval to sit inside body existence and cited authority validity, and term end is not distinguished from actual cessation (resignation, removal).
*Remediation:* add: at most one open membership per `(body, seat)` per instant; appointment interval contained in body existence and in the cited authority's validity; `termEnd` separate from `cessation` with reason.

**D20. Continuity versus succession is undefined.** "The body persists across changes in members, seats and meetings" does not say when a body *stops* persisting — charter replacement, merger of committees, dissolution-and-replacement all read as continuity today.
*Remediation:* add a rule that charter or mandate replacement preserves body identity, while dissolution-and-replacement opens a new body with an explicit succession link.

### Resolution, Mandate, signing authority

**D21. The Resolution composition has no anchor and no status bearer.** "No new Resolution identity is minted" leaves nothing for a Mandate, contract or later resolution to cite as *the* resolution. The local evidence assigns a "defective/contested status" and the acceptance result relies on it, but no status vocabulary is defined and, with no composition identity, it has nowhere to live. Ratification is entirely absent — the normal remedy for a defective resolution.
*Remediation:* designate the WM-REC-010 authentic expression as the citable anchor carrying the composition refs and a status vocabulary (validly adopted / not validly adopted / contested / superseded), and state that ratification is a *new* valid Resolution referencing the defective one, which never transitions to valid.

**D22. Signing authority has no evaluation instant and one unbound term.** "A live in-scope Mandate plus the relevant appointment or role" does not say at which instant, in which of valid and knowledge time, liveness is assessed; retroactive revocation is unhandled; and "role" has no base model or profile role anywhere in the package.
*Remediation:* require authority to be evaluated at the act instant in both valid and knowledge time, with retroactive revocation superseding rather than erasing the earlier authority claim; bind "role" to a base or delete it.

**D23. Conditional Mandate reuse has no gate and no fallback.** WM-ORG-007 reuse is conditional in all four artifacts, but no artifact states the verification test's pass criteria or what happens on failure.
*Remediation:* state the test as the nine required separately-recorded elements plus the eligibility/quorum exclusion, and declare the failure branch: reuse blocked and Mandate raised as its own candidate under hold.

### Fixture coverage and traceability

**D24. The fixture set is not executable and not traceable.** No `contourId`; no reference to the profile candidate, whose constraints supply most of what is being tested; invariants and constraints carry no ids and fixtures carry no `covers`, so coverage cannot be measured. Positive cases state no concrete inputs or expected values — `different-vote-ratios` expects only that shares "are calculated separately", which no wrong computation would fail, and it duplicates the `economic-equals-votes` negative. `class-amendment` and `class-version-pin` are near-duplicates. Finally, the local-evidence hold says "executable quorum, appointment and indirect-calculation fixtures are missing" while prose cases for quorum and membership exist — a reader cannot reconcile the two.
*Remediation:* number the invariants and constraints; add `contourId` and a profile-candidate reference to the fixture file and a `covers` field per case; give positive cases concrete inputs and expected values; restate the hold as "prose-only, non-executable".

---

## Additional fixtures required

Exactly these, in the existing `vercy-enterprise-allocation-fixtures/v1` case shape:

| id | kind | input | expect |
|---|---|---|---|
| `identifier-unassigned-guard` | negative | A consumer assigns or infers a WM identifier for Share Class, or publishes canonically, while `allocationState` is `unassigned`. | Both are rejected; the candidate stays identifier-unassigned and non-publishable. |
| `class-lifecycle-amended-state` | negative | A class transitions to an `amended` status instead of appending a version. | The transition is rejected; the class stays active and a new `ShareClassVersion` appends. |
| `amendment-without-authority-evidence` | negative | A version reaches `effective` without Mandate, decision, authentic record and procedure-evidence pins. | The transition is rejected; all four pins are required at `approved` → `effective`. |
| `class-designation-reuse` | positive | The same issuer reassigns a cancelled class's designation to a new class. | Two distinct `shareClassId`s; uniqueness holds on `(issuer, designation, non-overlapping interval)`. |
| `version-digest-pin-mismatch` | negative | A pinned class version's `contentDigest` no longer matches the stored version record. | Every calculation resolving that pin is non-reproducible and non-authoritative. |
| `retroactive-rights-correction` | positive | A rights schedule is corrected retroactively after calculations were published. | A new version appends with its own knowledge time; the earlier calculation replays unchanged at its original knowledge time. |
| `effective-version-without-denominator-policy` | negative | A version becomes `effective` with no denominator policy or issued-quantity rule. | Rejected; the treasury and suspended-holding rule is otherwise unenforceable. |
| `outstanding-quantity-denominator` | positive | Issued, treasury and suspended quantities are known per version and instant. | Outstanding = issued − treasury − suspended is the declared denominator; treasury casts no vote. |
| `derived-claim-schema-completeness` | positive | A derived indirect voting percentage is recorded. | It persists as a derived-claim record carrying the full normative pin set, never as a holding or relationship. |
| `calculation-field-omission-matrix` | negative | One case per required field omitted: right type, class version, content digest, denominator, valid time, knowledge time, scenario, rule version, input pins, cycle convention, tolerance. | Each omission independently makes the claim non-authoritative. |
| `cycle-non-convergent` | negative | An iterative convention fails to reach tolerance within maximum iterations. | Result is `unresolved`; cycle set, convention id, tolerance and iteration count are recorded; no truncated figure is published. |
| `cycle-membership-recorded` | positive | An indirect walk traverses a reciprocal-holding cycle and converges. | The claim records cycle set, convention id, tolerance and iteration count. |
| `scenario-identity` | negative | Two calculations bear the same scenario label but different input pins, with no scenario identity. | Comparison and aggregation are rejected; scenario equality requires identity, not a label. |
| `asserted-vs-derived-percentage` | positive | A filing asserts 30 percent while the pinned walk derives 28.7 percent. | Both persist in distinct categories; neither overwrites the other; the discrepancy stays visible. |
| `natural-person-holder` | positive | An individual holds units of a class. | The holding is carried by the WM-ECO-038 position alone; no inter-organizational WM-ORG-012 link is fabricated. |
| `holder-capacity-double-count` | negative | A nominee's registered holding and the beneficial owner's interest over the same units are summed. | Rejected; each Ownership Interest declares its capacity and cross-capacity aggregation needs a declared rule. |
| `ownership-facet-quantity-duplication` | negative | A WM-ORG-012 ownership facet stores quantity or percentage duplicating the WM-ECO-038 position. | Rejected; quantity and class-version pin are mastered only on the position. |
| `seat-overlap` | negative | Two open memberships exist on the same `(body, seat)` at one instant. | Rejected; at most one open membership per seat per instant. |
| `appointment-outside-authority-interval` | negative | An appointment interval extends beyond body existence or beyond the cited authority's validity. | Rejected; containment in both is required. |
| `resignation-before-term-end` | positive | A member resigns mid-term. | Cessation is recorded with reason, distinct from term end; prior attendance and votes are untouched. |
| `body-continuation-vs-succession` | positive | Case A replaces the charter; case B dissolves the body and constitutes a replacement. | A preserves body identity; B opens a new body with an explicit succession link. |
| `recusal-per-matter` | positive | One meeting decides two items with different recusals. | Eligibility, quorum base, exclusions and determination are recorded per item, not per meeting. |
| `written-consent-threshold` | positive | A decision is taken by written consent with no meeting. | The consent threshold and each consent's own authority are recorded; no attendance or quorum values are asserted. |
| `resolution-composition-anchor` | positive | A Mandate and a contract each cite one resolution. | Both resolve to the same composition anchor, which carries refs to all three masters and the adoption status. |
| `defective-resolution-ratified` | positive | A later valid resolution ratifies an earlier no-quorum resolution. | A new valid Resolution records the ratification; the defective record keeps its failed attestation and never becomes valid. |
| `mandate-element-completeness` | positive | A WM-ORG-007 instance records grantor, grantee, scope, instrument, effective interval, revocation, powers, reserved matters and limits, and no eligibility or quorum. | Conditional reuse passes; omission of any element blocks reuse and routes Mandate to its own candidate. |
| `retroactive-mandate-revocation` | positive | A Mandate is revoked with retroactive effect after a signature was given under it. | Authority is re-evaluated at the act instant in valid and knowledge time; the earlier claim is superseded, not erased. |
| `conversion-execution-boundary` | negative | Class conversion rights are used to move positions from class A to class B inside Share Class or Resolution. | Rejected; execution requires the corporate-action boundary — this case stays held and unevaluable until that model is named (D18). |
