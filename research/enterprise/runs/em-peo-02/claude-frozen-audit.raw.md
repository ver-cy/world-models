# Frozen Semantic Audit — EM-PEO-02 "Work Relations and Assignments"

## 1. Verdict

**REVISE.**

The decision shape is sound; the object model underneath it does not carry the decision. Roughly half of the stated invariants have no representation in `objects` and cannot hold at instance level, two of them contradict the schema outright, and four fixtures assert outcomes that nothing in the package can produce. Candidate revision 2 is not ready to go to registry allocation as written.

---

## 2. Decision confirmation

**CONFIRMED, with two scope corrections.**

| Element | Ruling |
|---|---|
| PROFILE over `WM-PER-001` | Confirmed. Person anchor stays cross-employer and durable; nothing in the candidate claims worker identity. |
| PROFILE over `WM-ORG-005` | Confirmed as a profile, but note `sourceFacts.WM-ORG-005` states the base is a *reviewable draft* whose relation to assignment is unapproved. The profile is therefore built on an unstable base and must remain held regardless of its own maturity. |
| PROFILE over `WM-ORG-016` | Confirmed. Post/host/scope/authority/allocation ownership is correctly left with the base. |
| Identifier-unassigned `EmployeeProfile` candidate | Confirmed **as a distinct master**. It survives the identity test: employer-scoped continuity across successive Employment spells is not Person (which is cross-employer), not Employment (which is per-spell), and not Assignment (which is per-post). Rehire is the discriminating case and it is correctly handled. |
| `newRuntimeId: false` | Confirmed. Registry allocation is pending; `allocationState: unassigned`, `modelId: null`, `registryId: null` and the fail-closed fixture are mutually consistent. No identifier may be minted. |
| Rejection of `Engagement`, `LifecycleEvent`, `JoinerMoverLeaverCase` as masters | Confirmed for `LifecycleEvent` and `JoinerMoverLeaverCase` (owned by `WM-ACT-040` / `EM-OPS-01`). **Rejected for `Engagement`** as currently reasoned — see D6: the candidate rejects Engagement as a master while its own invariant 10 requires an "engagement context" that no referenced model is stated to own. |

**Correction 1:** the proposed name `Employee Profile` must change (D5).
**Correction 2:** `canonicalPublishable: false` must stay false, and the publication hold must additionally cite the draft status of `WM-ORG-005` explicitly, not only the COMPOSE relation.

---

## 3. Defects, remediation, and fixture expectations

### A. Identity and scope collapse

**D1 — No uniqueness rule for (Person, employing party).**
Nothing forbids two simultaneously active profiles for the same Person at the same employer. Rehire "reuses" the profile only by convention; a second profile can be created instead, fragmenting number history, Employment references and category assertions into two silos. This is the single most likely production collapse in the package.
*Remediation:* add invariant — "At most one EmployeeProfile with status in {proposed, active, inactive} may exist for a given (personRef, employerRef); a closed or superseded profile does not license a duplicate, it licenses reactivation or explicit succession." Add to `EmployeeProfile.required` a uniqueness key declaration `(personRef, employerRef, status∈open)`.
*Fixture `duplicate-profile-same-employer` (negative):* creating a second active EmployeeProfile for a Person who already holds an active profile at the same employer is rejected; the pre-existing profile, its number bindings and its Employment references remain the only resolvable record.

**D2 — `employerRef` has no master and no resolution authority.**
`boundary.references` lists Person, Employment, Assignment, JML, access, process and identifier-scheme masters — but no party/legal-entity master. `employerRef` therefore dangles. Every employer-scoped guarantee in the package (profile scope, number uniqueness, "no cross-employer join key") is keyed on an unresolvable reference, and two records of the same legal employer would silently split or merge scope.
*Remediation:* add an explicit legal-entity/party master reference to `boundary.references` with purpose "employing party identity and legal-entity continuity", and state that `employerRef` must resolve to a legal entity in that master, not to an org unit, brand, payroll code or site.
*Fixture `employer-ref-unresolvable` (negative):* an EmployeeProfile whose `employerRef` resolves to an org unit or payroll code rather than a legal entity is invalid; number-uniqueness evaluation is not attempted.

**D3 — Role taxonomy has no owner; the agency-labor fixture is unsatisfiable.**
Invariant 11 forbids collapsing employer, work customer, staffing supplier, paymaster, platform and host. `sourceFacts.WM-ORG-016` states ownership only of post, **host**, scope, authority, allocation and history. Work customer, staffing supplier, paymaster and platform have no stated owner anywhere in the dossier, and this candidate excludes them. Fixture `agency-labor` expects all four roles to "remain explicit" with no model able to hold three of them.
*Remediation:* either (a) obtain and record a source fact placing work customer / supplier / paymaster / platform role ownership in `WM-ORG-016` or the party master, or (b) downgrade invariant 11 to an *inherited* obligation and mark `agency-labor` as blocked pending that ownership decision. Do not leave it asserted as satisfied here.
*Fixture `role-ownership-unresolved` (negative):* an Assignment recording a staffing supplier through a free-text field, rather than a typed role reference in an owning master, is rejected as unsuitable evidence for the non-collapse invariant.

**D4 — `personRef` immutability and Person merge/split are unhandled.**
Invariant 2 forbids changing the Person anchor only on the specific event of a new employing party. There is no general immutability rule, and no rule for what happens when `WM-PER-001` merges or splits two Person records — at which point two profiles at one employer collapse into a D1 duplicate, or one profile's history splits between two people.
*Remediation:* add invariant — "`personRef` is immutable for the life of the profile. A Person merge in `WM-PER-001` does not merge profiles: it creates an explicit profile-succession link requiring merge evidence; a Person split requires an evidenced reassignment recorded as succession, never an in-place `personRef` edit."
*Fixture `person-merge-downstream` (negative):* a Person merge that rewrites `personRef` in place on an existing profile is rejected; the correct outcome is two profiles linked by evidenced succession with both number histories resolvable.

**D5 — The name asserts the status the model forbids.**
`EmployeeProfile` and `EmployeeNumberBinding` are named "employee" while invariant 6 states profile existence never proves employee status, and the scope explicitly covers freelancers and contested classifications (fixture `freelancer-misclassification`). Consumers read names before invariants; the label is itself the misclassification vector the package exists to prevent.
*Remediation:* rename the candidate to `WorkerProfile` (bindings: `WorkerNumberBinding`) or, if the enterprise term is fixed, record a mandatory registry annotation "the name is an administrative label and carries no employment-status or legal-classification meaning" and bind that annotation to every generated schema description.
*Fixture `name-as-status-evidence` (negative):* a consumer citing the profile type name as evidence of employee status is rejected; only sourced `WorkerCategoryAssertion` plus a competent determination can answer the status question.

**D6 — Engagement context has no representation.**
Invariant 10 requires every Assignment to resolve to "exactly one explicit Employment **or engagement** context". `EmployeeProfileVersion` offers only `employmentRefs`. Non-employee engagements — precisely the freelancer and platform cases — have nowhere to attach, so they will be forced into `employmentRefs`, which both falsifies the Employment record and manufactures the employee inference invariant 6 forbids.
*Remediation:* either add `engagementRefs` alongside `employmentRefs` with a stated owner (`WM-ORG-005` if that master covers engagement, per its title), or record a source fact confirming `WM-ORG-005` represents engagements as a typed variant of Employment and state that `employmentRefs` means "Employment-or-engagement relationship records of `WM-ORG-005`". The current silence is the defect.
*Fixture `engagement-forced-into-employment` (negative):* recording a contractor engagement as an Employment record solely to satisfy a required reference is rejected; the relationship type must be carried explicitly.

### B. History loss and correction

**D7 — No record time; amendments and corrections are indistinguishable.**
`effectiveFrom`/`effectiveTo` are valid-time only. Invariant 14 requires corrections to use record versioning **without rewriting real-world history**, and fixture `record-correction` depends on it. With one time axis, a correction can only be expressed as a new valid-time interval — which fabricates a real-world event — or as an in-place edit — which destroys the prior assertion. `supersedesVersion` is ambiguous between the two.
*Remediation:* make `EmployeeProfileVersion` bitemporal: add required `recordedFrom`, optional `recordedTo`, and required `changeType ∈ {initial, amendment, correction}`. A correction shares the predecessor's valid-time interval and opens a new record-time interval; an amendment opens a new valid-time interval. Forbid mutation of any version after `recordedTo` is set.
*Fixture `correction-preserves-valid-time` (positive):* correcting a mis-keyed title produces a new version with an identical `[effectiveFrom, effectiveTo)`, `changeType: correction`, and a closed `recordedTo` on the prior version which remains readable; no lifecycle transition is emitted.

**D8 — `withdrawn` version state has no retention rule.**
`EmployeeProfileVersion.lifecycle` includes `withdrawn` with no statement that withdrawn versions remain stored and resolvable. As written, withdrawal is an erasure affordance that bypasses every "never deletes history" invariant.
*Remediation:* add invariant — "`withdrawn` marks a version non-authoritative; it is never deleted, never removed from version sequence, and remains resolvable with its `contentDigest`, `recordedFrom`/`recordedTo` and withdrawal reason." Add required `withdrawalReasonRef` when status is `withdrawn`.
*Fixture `withdrawn-version-retention` (negative):* a request that withdraws a version and removes it from the profile's version history is rejected; withdrawal must leave the version resolvable with a reason.

**D9 — No overlap rule on profile versions.**
Number bindings get an overlap fixture; versions do not. Two concurrently active versions with overlapping validity can assert contradictory content, including contradictory `employmentRefs` sets.
*Remediation:* add invariant — "Within one `employeeProfileId`, active versions occupy non-overlapping half-open `[effectiveFrom, effectiveTo)` intervals in a single record-time slice." State half-open explicitly to close the boundary-day ambiguity.
*Fixture `overlapping-active-versions` (negative):* a second active version whose validity interval overlaps an existing active version in the same record-time slice is rejected.

**D10 — Number bindings have no void path.**
A number issued in error can only be deleted (history loss) or closed with `validTo` (falsely asserting it was once valid). `EmployeeNumberBinding` has no status, no record time, no void semantics.
*Remediation:* add required `bindingStatus ∈ {active, ended, voided}`, required `recordedFrom`, optional `recordedTo`, and required `voidReasonRef` when voided. A voided binding never occupied its validity interval for uniqueness purposes but remains resolvable for audit and for inbound references.
*Fixture `void-erroneous-number` (positive):* voiding a mis-issued number leaves the binding resolvable with `bindingStatus: voided`, frees the number for issuance in the same interval, and does not imply the worker ever held it.

**D11 — Profile closure does not protect number-binding resolvability.**
Invariant 18 protects number *history* against Employment closure, but nothing states what happens to bindings when the **profile** reaches `closed` or `superseded`.
*Remediation:* add invariant — "Profile closure closes open number bindings by setting `validTo`; it never deletes bindings, and closed-profile bindings remain resolvable for historical lookup and for reuse-policy evaluation."
*Fixture `closed-profile-number-lookup` (positive):* a number issued under a since-closed profile still resolves to that profile and Person for a historical query dated inside its validity interval.

### C. Employment and Assignment integrity

**D12 — `employmentRefs` is required, which manufactures the Employment inference.**
`boundary.owns` says "references to **zero or more** … Employment records" and invariant 6 says profile existence never proves active Employment. Yet `employmentRefs` sits in `EmployeeProfileVersion.required`. A `proposed` pre-hire profile becomes unrepresentable, and every readable version implies at least one Employment.
*Remediation:* keep the field required but state explicitly "required, may be the empty set", or move it to `optional` with the empty case defined. Add invariant — "A non-empty `employmentRefs` asserts association only; activity, status and classification are read from the Employment records themselves."
*Fixture `pre-hire-profile` (positive):* a `proposed` profile with an empty `employmentRefs` is valid, and a consumer querying employment status for that Person at that employer receives "no Employment", not "unknown" and not "employed".

**D13 — Employment-to-profile association has no validity of its own.**
`employmentRefs` is a bare list re-asserted on each content version, so "which Employments belonged to this profile, and when" is entangled with unrelated content changes, and an Employment cannot be moved between profiles under succession without rewriting version content.
*Remediation:* promote the association to its own object, `ProfileEmploymentLink` — identity `linkId`; required `employeeProfileRef`, `employmentRef`, `validFrom`, `recordedFrom`; optional `validTo`, `successionEvidenceRef` — and add invariant "an Employment is linked to exactly one profile at any point in valid time, except across evidenced employer succession."
*Fixture `employment-linked-once` (negative):* linking one Employment to two profiles with overlapping validity and no succession evidence is rejected.

**D14 — Employer succession leaves the continued Employment homeless.**
Fixture `employer-succession` says the Employment "may continue"; invariant 1 scopes a profile to one employing party and invariant 2 requires a new profile for a new employing party. So a continuing Employment must belong to two employer-scoped profiles across time, and no rule, field or object says how. This is the sharpest structural contradiction in the package (see C1).
*Remediation:* add invariant — "Evidenced legal succession preserves Employment continuity and creates a successor profile at the new employing party. The predecessor profile is set `superseded` with `successorRef`; the Employment link is closed on the predecessor and opened on the successor with `successionEvidenceRef`; number bindings are not carried across unless the successor's numbering scheme explicitly adopts them."
*Fixture `succession-splits-profile-not-employment` (positive):* after evidenced succession, one Employment resolves across two profiles via dated links, the predecessor profile and its number history remain resolvable, and the event is not recorded as separation-plus-rehire.

**D15 — `successorRef` is unidirectional, untyped and unevidenced.**
`EmployeeProfile.optional` holds `successorRef` with no predecessor link, no reason, no evidence reference, and no constraint that the successor share the same `personRef`. As written it can point at another Person's profile, silently merging two people's histories.
*Remediation:* require `successorRef` targets to share `personRef`; add `successionReason ∈ {employer-succession, person-merge, remediated-duplicate}` and required `successionEvidenceRef`; add derived reverse resolution so a successor profile exposes its predecessors.
*Fixture `succession-cross-person` (negative):* a `successorRef` pointing to a profile with a different `personRef` is rejected.

**D16 — Rehire has no legal transition into a closed profile.**
Invariant 17 requires rehire to reuse the profile, but `closed` and `superseded` are terminal with no transition table and no reactivation rule. The rehire fixture cannot be executed against the declared lifecycle.
*Remediation:* publish an explicit transition table. Permit `closed → active` on evidenced rehire with a new version and a new Employment link; forbid `superseded → active` in all cases (a superseded profile is reached only through its successor).
*Fixture `rehire-reactivates-closed-profile` (positive):* rehire moves the profile `closed → active`, clears `closedAt`, adds a new Employment link, and leaves the prior Employment link, its `validTo` and the prior number binding intact.

**D17 — Assignment validation is claimed but not held.**
Fixture `assignment-without-context` expects "the Assignment is invalid **for this profile**", yet `boundary.excludes` disclaims Assignment lifecycle and no object references an Assignment. The package asserts an enforcement it cannot perform. Same pattern for invariants 9, 10 and 13.
*Remediation:* split `invariants` into `localInvariants` (enforceable against objects declared here) and `inheritedObligations` (restated from `WM-ORG-005` / `WM-ORG-016`, non-enforceable here, and held with those bases). Move invariants 8–15 to `inheritedObligations` and restate the fixture as a base-model expectation.
*Fixture `inherited-obligation-not-locally-enforced` (negative):* a claim that this candidate validates Assignment context is rejected; the obligation resolves to `WM-ORG-016` and inherits its publication hold.

### D. Classification

**D18 — Dual classification authority.**
Invariant 8: "Employment owns … classification evidence." `boundary.owns`: "purpose and jurisdiction-qualified worker-category assertions." Both statements cannot be true. Two answerable homes for status produce divergent answers, which is misclassification by construction.
*Remediation:* state the split precisely — `WM-ORG-005` owns classification **determinations** (competent-authority findings and their evidence); this profile owns only **administrative category assertions** for a named purpose, each of which must carry `determinationRef` when it restates a legal finding, and must be marked non-determinative when it does not. Rename the object `AdministrativeWorkerCategoryAssertion` to make the weaker claim visible.
*Fixture `category-without-determination` (negative):* an assertion whose `purpose` is legal or statutory and which lacks `determinationRef` is rejected; the same assertion for purpose `internal-reporting` is accepted and flagged non-determinative.

**D19 — Category assertions cannot be attributed to one of several concurrent Employments.**
`WorkerCategoryAssertion.required` carries `employeeProfileVersionRef` but no `employmentRef`. Under fixture `parallel-contract-same-employer`, one profile holds two concurrent contracts; if one is an employment and the other an engagement, the profile-level category cannot say which is which — and will be read as applying to both.
*Remediation:* add required `employmentRef` (or `engagementRef`) to `WorkerCategoryAssertion`, and add invariant "a category assertion qualifies exactly one relationship, never the profile as a whole."
*Fixture `concurrent-mixed-classification` (positive):* a Person with one employment contract and one contractor engagement at the same employer carries two assertions with distinct relationship refs; a query for either contract returns only its own category.

**D20 — Binding assertions to a *version* fragments category history.**
Every ordinary amendment creates a new `EmployeeProfileVersion`, so long-lived category assertions must be re-pointed or orphaned on unrelated content changes.
*Remediation:* anchor `WorkerCategoryAssertion` to `employeeProfileId` (plus the relationship ref from D19) with its own `validFrom`/`validTo` and record time, not to a version. Delete the duplicated `categoryAssertions` array from `EmployeeProfileVersion` to remove the second, unconstrained source of truth.
*Fixture `amendment-preserves-category` (positive):* an FTE amendment creates a new profile version and leaves the existing category assertion valid, unchanged and singly-sourced.

**D21 — `purpose`, `jurisdictionRef` and dispute outcome are unconstrained.**
`purpose` is free text, so "purpose-qualified" is unenforceable. `disputeRef` is optional with no dispute outcome state, so fixture `freelancer-misclassification`'s requirement that "dispute history remain visible" cannot be met when a dispute exists but was never referenced.
*Remediation:* bind `purpose` to a governed enumeration and `jurisdictionRef` to a scheme under `EM-XCT-01`; add `disputeStatus ∈ {none, raised, under-determination, resolved-upheld, resolved-overturned}` as required, with `disputeRef` required whenever status is not `none`; require that an overturned determination supersede rather than delete the prior assertion.
*Fixture `dispute-visibility` (positive):* an overturned freelancer classification leaves both the original assertion and the overturning determination resolvable, with `disputeStatus: resolved-overturned` on the superseded assertion.

### E. Employee numbers

**D22 — Reuse policy is optional and located on the wrong object.**
Invariant 4 places reuse policy on the **scheme**; `EmployeeNumberBinding.optional` places `reusePolicyRef` on the **binding**. When absent, fixture `number-reuse-overlap` has no policy to fail against, so it fails open.
*Remediation:* resolve reuse policy from `numberSchemeRef` under `EM-XCT-01` as the sole authority; retain a binding-level field only as required provenance `appliedReusePolicyVersion` recording which policy version was evaluated at issuance. A scheme with no declared reuse policy blocks issuance.
*Fixture `scheme-without-reuse-policy` (negative):* issuing a number under a scheme that declares no reuse policy fails closed; it does not default to permit or to deny silently.

**D23 — `employerRef` is duplicated on the binding with no equality constraint.**
A binding can name employer A while its `employeeProfileRef` resolves to a profile scoped to employer B — creating exactly the cross-employer join key invariant 5 forbids.
*Remediation:* add invariant `EmployeeNumberBinding.employerRef == EmployeeProfile.employerRef`, or drop the field and derive it. Also express the uniqueness key formally as `(employerRef, numberSchemeRef, number)` non-overlapping over half-open `[validFrom, validTo)`, with `bindingStatus: voided` excluded from the key.
*Fixture `binding-employer-mismatch` (negative):* a number binding whose `employerRef` differs from its profile's `employerRef` is rejected before uniqueness evaluation.

### F. JML, access authority and publication

**D24 — Access-verification obligations are asserted but have no representation.**
Invariants 18–21 say offboarding *creates* access-verification obligations and that closure cannot set revocation success without access-authority evidence. No object here creates, holds or tracks an obligation, and profile closure is unconstrained by any access evidence. Fixtures `incomplete-offboarding` and `case-closure-as-revocation` describe behaviour nothing in the package produces.
*Remediation:* add a closure gate that is local and enforceable — `EmployeeProfile` closure requires `accessVerificationOutcomeRefs` resolving to `EM-RSK-03` verification records covering every account associated with the profile's Employments, with any unverified outcome blocking `closed` and permitting only `inactive`. Move the remaining JML-state invariants to `inheritedObligations` under `WM-ACT-040`.
*Fixture `closure-blocked-by-unverified-access` (negative):* closing a profile with two unverified access outcomes is rejected; the profile may become `inactive`, the obligations stay open and resolvable, and no revocation is recorded.

**D25 — `inactive` is overloaded across two models.**
`EmployeeProfile.lifecycle` has `inactive`, and fixture `incomplete-offboarding` says "**Employment** may be inactive". Two different `inactive` notions with no definitions invites consumers to read profile-inactive as employment-terminated — a status inference the package forbids.
*Remediation:* define each profile state normatively (`proposed`: no relationship yet; `active`: at least one open Employment link; `inactive`: no open Employment link, obligations may be open, reactivation permitted; `closed`: no open links and all access verification evidenced; `superseded`: reached via `successorRef` only), and rename the profile state to `dormant` to break the collision with Employment states owned by `WM-ORG-005`.
*Fixture `profile-inactive-not-terminated` (negative):* reading `status: dormant` as proof that employment ended is rejected; termination is answered only by the Employment record.

**D26 — Governance holds are encoded as model invariants.**
`invariants` 22 and 23 ("COMPOSE remains a draft relation until approved", "The candidate has no model or runtime identifier until registry allocation") are process gates, not instance-level invariants. Left in the invariant list they will be emitted into generated schema validation, where they are meaningless, and they inflate the apparent enforcement surface.
*Remediation:* move both to `holds` (where near-duplicates already sit) and keep `invariants` restricted to statements evaluable against instance data.
*Fixture `governance-hold-not-instance-rule` (negative):* generating instance validation from the invariant list emits no rule derived from a governance hold; the hold is surfaced as a publication block instead.

**D27 — Unsourced neighbor ownership claims.**
`sourceFacts` covers `WM-PER-001`, `WM-ORG-005`, `WM-ORG-016`, registry and runtime only. `WM-ACT-040`, `EM-RSK-03`, `EM-OPS-01` and `EM-XCT-01` carry ownership claims in `boundary.references` with no frozen source fact. `numberSchemeRef` and every number-scope invariant depend on `EM-XCT-01`'s scheme authority; access gating depends on `EM-RSK-03`. Both dependencies are currently asserted, not sourced.
*Remediation:* obtain and record a source fact per referenced neighbor, or demote unsourced references to `referencedNeighbors` marked `unsourced` and hold every invariant that depends on them.
*Fixture `unsourced-dependency-hold` (negative):* a number binding validated against `EM-XCT-01` scheme authority while that authority carries no source fact is reported as held, not as passed.

**D28 — Fixture wording overclaims execution.**
`fixturesExecuted: false` and the runtime hold are correct and consistent, but individual fixtures use enforcement voice — "Validation fails", "Generation fails closed", "The write is rejected" — which reads as observed behaviour in any downstream extract.
*Remediation:* restate all 18 cases in expectation voice ("a conforming validator must reject …") and carry `fixturesExecuted: false` into each case record, not only the envelope.
*Fixture `execution-claim-check` (negative):* any report presenting these cases as passing tests is rejected while `fixturesExecuted` is false.

---

## 4. Contradictions

| # | Contradiction | Defect |
|---|---|---|
| C1 | Invariants 1–2 (profile scoped to one employing party; new employing party ⇒ new profile) vs fixture `employer-succession` (Employment continues across a change of employing party). No rule reconciles a continuing Employment spanning two profiles. | D14 |
| C2 | Invariant 8 ("Employment owns … classification evidence") vs `boundary.owns` ("worker-category assertions") and the `WorkerCategoryAssertion` object carrying `sourceRef`, `determinationRef`, `disputeRef`. | D18 |
| C3 | `boundary.owns` "references to **zero or more** Employment records" and invariant 6 vs `EmployeeProfileVersion.required: employmentRefs`. | D12 |
| C4 | Fixture `assignment-without-context` ("invalid **for this profile**") vs `boundary.excludes` disclaiming Assignment lifecycle and the absence of any Assignment reference in `objects`. | D17 |
| C5 | Invariant 17 (rehire reuses the profile) vs terminal `closed`/`superseded` lifecycle states with no reactivation transition. | D16 |
| C6 | Object names `EmployeeProfile` / `EmployeeNumberBinding` vs invariant 6 (existence proves no employee status) and a scope covering freelancers and engagements. | D5 |
| C7 | Invariant 4 (the **scheme** declares reuse policy) vs `reusePolicyRef` being an **optional binding-level** field. | D22 |
| C8 | Invariant 10 requires an "Employment **or engagement** context" vs `rejectedNewMasters: ["Engagement", …]` with no engagement representation in any referenced master's source fact. | D6 |
| C9 | Invariant 11 (six roles not collapsed) vs `sourceFacts.WM-ORG-016`, which grants ownership of host only, and the absence of any party master. | D3 |
| C10 | Profile state `inactive` vs fixture `incomplete-offboarding`'s Employment state `inactive` — the same word for two states owned by different models. | D25 |
| C11 | `holds` "this package has no runtime semantics" vs `identityTest.independentLifecycle`, four object lifecycles, and fixtures phrased as executed enforcement. | D28 |

Note one item that is **not** a contradiction, having been checked: `decision.newRuntimeId: false` against `allocationCandidate.decision: "NEW MODEL CANDIDATE"`. These are consistent under the reading "a new master is proposed; no identifier is allocated yet", which `allocationState: unassigned` and the `candidate-id-invention` fixture confirm. The wording is nonetheless easy to misread and should carry a one-line gloss.

---

## 5. Remediation checklist

1. Add a uniqueness invariant over `(personRef, employerRef)` for all open profile states, with fixture `duplicate-profile-same-employer`. **(D1)**
2. Add a legal-entity/party master to `boundary.references` and constrain `employerRef` to resolve there, with fixture `employer-ref-unresolvable`. **(D2)**
3. Source or demote ownership of work customer, staffing supplier, paymaster and platform roles; block `agency-labor` until owned, with fixture `role-ownership-unresolved`. **(D3)**
4. Declare `personRef` immutable and specify Person merge/split handling as evidenced succession, with fixture `person-merge-downstream`. **(D4)**
5. Rename the candidate to a status-neutral term, or bind a mandatory non-inference annotation to the name, with fixture `name-as-status-evidence`. **(D5)**
6. Represent engagement context explicitly, or record a source fact that `WM-ORG-005` covers engagements as typed relationships, with fixture `engagement-forced-into-employment`. **(D6)**
7. Make `EmployeeProfileVersion` bitemporal and add required `changeType`, with fixture `correction-preserves-valid-time`. **(D7)**
8. Add a retention and reason rule for `withdrawn` versions, with fixture `withdrawn-version-retention`. **(D8)**
9. Add a half-open non-overlap invariant for active profile versions, with fixture `overlapping-active-versions`. **(D9)**
10. Add `bindingStatus`, record time and void semantics to `EmployeeNumberBinding`, with fixture `void-erroneous-number`. **(D10)**
11. State that profile closure closes but never deletes number bindings, with fixture `closed-profile-number-lookup`. **(D11)**
12. Permit an empty `employmentRefs` explicitly and state that association implies no status, with fixture `pre-hire-profile`. **(D12)**
13. Promote profile↔Employment association to a dated `ProfileEmploymentLink` object, with fixture `employment-linked-once`. **(D13)**
14. Write the employer-succession rule that splits the profile while continuing the Employment, with fixture `succession-splits-profile-not-employment`. **(D14)**
15. Constrain `successorRef` to the same Person and require succession reason and evidence, with fixture `succession-cross-person`. **(D15)**
16. Publish a profile state-transition table permitting `closed → active` on evidenced rehire and forbidding `superseded → active`, with fixture `rehire-reactivates-closed-profile`. **(D16)**
17. Split `invariants` into `localInvariants` and `inheritedObligations`; move invariants 8–15 to the latter, with fixture `inherited-obligation-not-locally-enforced`. **(D17)**
18. Resolve the dual classification authority; restrict this model to administrative, purpose-scoped assertions requiring `determinationRef` for legal purposes, with fixture `category-without-determination`. **(D18)**
19. Add a required relationship reference to every category assertion, with fixture `concurrent-mixed-classification`. **(D19)**
20. Re-anchor category assertions to the profile with their own validity and delete the duplicate `categoryAssertions` array, with fixture `amendment-preserves-category`. **(D20)**
21. Govern `purpose` and `jurisdictionRef` by enumeration and scheme, and add a required `disputeStatus`, with fixture `dispute-visibility`. **(D21)**
22. Move reuse-policy authority to the numbering scheme and fail closed when a scheme declares none, with fixture `scheme-without-reuse-policy`. **(D22)**
23. Constrain binding `employerRef` to equal the profile's, and express the number uniqueness key formally over half-open validity, with fixture `binding-employer-mismatch`. **(D23)**
24. Add an enforceable access-verification gate on profile closure and move residual JML invariants to inherited obligations, with fixture `closure-blocked-by-unverified-access`. **(D24)**
25. Define every profile state normatively and rename `inactive` to `dormant` to break the collision with Employment states, with fixture `profile-inactive-not-terminated`. **(D25)**
26. Move governance holds out of `invariants` into `holds`, with fixture `governance-hold-not-instance-rule`. **(D26)**
27. Add a source fact for `WM-ACT-040`, `EM-RSK-03`, `EM-OPS-01` and `EM-XCT-01`, or demote them to unsourced and hold every dependent invariant, with fixture `unsourced-dependency-hold`. **(D27)**
28. Restate all fixture expectations in expectation voice and carry `fixturesExecuted: false` per case, with fixture `execution-claim-check`. **(D28)**
29. Add the `newRuntimeId` gloss distinguishing "no identifier allocated yet" from "no identifier will be allocated". **(C-note)**
30. Extend the publication hold to cite the draft status of `WM-ORG-005` explicitly, independently of the COMPOSE relation hold; keep `canonicalPublishable: false` and `allocationState: unassigned` until items 1–29 close.
