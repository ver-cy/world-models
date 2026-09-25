# Verdict

Three-way reuse, one profile, one genuinely new type, two rejections.

- **WM-PER-001 Person — reuse unchanged** as the person anchor. Nothing in EM‑PEO‑02 belongs inside it; it already excludes party roles, employment and account relationships.
- **WM-ORG-005 Employment — reuse under an EM‑PEO‑02 profile.** Its scope already carries relationship identity, multi-party roles, basis, jurisdiction, purpose-qualified status assertions, determinations, continuity and separation. `Engagement` is therefore **not** a new type: a contractor or agency relationship is the same relationship model with a different asserted basis and different party-role fill.
- **WM-ORG-016 Work Assignment — reuse unchanged** for positions, scope, authority, allocation, lifecycle and handover.
- **EmployeeProfile — new type required.** It is the only candidate with identity and lifecycle independent of all three: scoped to one employer, one per worker per employer, created before and surviving after any single Employment, carrying the employee number across termination and rehire. It cannot be an attribute of Employment (it outlives it), of Person (it is employer-scoped), or of Assignment (it is not time-sliced work). It needs its own registry reservation; no identifier is assignable from this dossier.
- **LifecycleEvent — reject as a type.** WM-ORG-005 already owns commencement, suspension, succession, amendment and separation as relationship events; WM-ORG-016 owns `transition_event` with trigger, actor and reversal. A third event model would duplicate both and create a competing state authority.
- **JoinerMoverLeaverCase — reject as owned here.** It is a coordination case over process and access, both of which the contour scope itself declares to be references. It has independent lifecycle but belongs to the process/case contour (EM‑WRK‑02); EM‑PEO‑02 holds only a typed reference and must never derive relationship state from case state.

# Evidence

Uneven, and the unevenness is load-bearing. WM-ORG-005 is a `single-provider-waiver` publication (Codex only; Claude and Grok waived after timeouts) — the weakest adjudication of the three, yet it carries the heaviest semantics here. WM-PER-001 and WM-ORG-016 are dual-provider. All three are `reviewable-draft`, `publishableCanonical: false`.

Two registry/spec mismatches: WM-ORG-016 is registry `status: candidate`, `boundary-review-required`, with an empty `existing_spec_ref`, while a full 255 KB published spec exists; WM-PER-001 is listed in `vercy_candidates` at `evidence_depth: index-and-publication-metadata` although its full spec is parsed and hashed. The crosswalk claim is thinner than the spec parse in both cases.

Both relation rows (WM-ORG-004 COMPOSE WM-ORG-016, WM-ORG-005 COMPOSE WM-ORG-016) are `review_state: candidate`, and WM-ORG-005 holds an explicit publication hold that the composition is draft. The realization link this contour depends on is proposed, not approved. WM-ORG-005 also replaces the legacy O3 card that fused Employment with Membership; the split to WM-ORG-006 is asserted but not exercised here.

# Identity/mastership

Person is mastered by the civil register (WM-PER-001), referenced never copied. Employment relationship identity is independently governed: not the party pair, not a contract number, not a start date, not an employee number. EmployeeProfile identity is the pair (employing party, worker) under an employer's registration scheme, mastered by that employer's HRIS. Assignment identity is its own record with `record_version` and supersession chain, mastered by the organization. Change of employer never touches Person; change of Person attributes (name, legal gender, civil status) never creates a new Employment.

# Relationship kinds/parties

Three party questions must stay separate, and WM-ORG-005's role set already allows it:

- **Employer** — the employing party bound in the Employment relationship; the only party whose identity change implies succession or a new relationship.
- **Work customer (host/client)** — `host_organization_ref` on the Assignment, plus a client role on the relationship. Direction of work does not make a party an employer.
- **Staffing supplier (agency)** — the employing party in an agency relationship, with the host carried as a separate typed role.

Worker categories: *employee* = Employment with employment basis; *contractor* = Employment-model instance with contract-for-services basis plus a commercial contract reference held externally; *agency worker* = Employment with the agency as employer and the host as work customer, realized by an Assignment whose `assigning_organization_ref` and `host_organization_ref` differ. `worker_category` is a derived, purpose-qualified projection of status assertions — never an input that settles status.

# Employee profile and numbering

EmployeeProfile carries `employee_number`, `person_ref`, and zero-to-many `employment_ref` (not one). The v1 field `employment_ref` as single-valued is wrong for rehire and dual contracts with one employer.

Numbering rule: unique within (employing party, numbering scheme, validity window); scheme must declare a reuse policy explicitly, mirroring WM-PER-001's `identifier_reuse_policy`; the number is never a cross-employer join key, never a Person identifier, and never evidence of employment status. Number issue time, profile effective start and relationship effective start are three separate clocks.

# Assignment/versioning

Three-way rule, taken from WM-ORG-016's own distinction:

1. **New Employment** — change of employing legal party without a recorded succession/continuity decision; change of basis (services → employment); re-formation under a different applicable law; rehire after separation; an additional parallel contract with the same employer on a distinct basis.
2. **New Assignment record** — change of post, host organization, assignee, work scope or authority conveyance; use `supersedes_assignment_ref` / `predecessor_assignment_ref`.
3. **Amendment or record version** — effective-dated `amendment_record` for FTE, pattern, location mode, reporting line, title, with `material_change_flag` driving notification; `record_version` only for correcting what was wrongly recorded, never for real-world change.

Employer succession with a continuity decision preserves relationship identity and credited service; it is not a rehire.

# JML/access boundary

Offboarding at the Employment or Assignment layer **emits an obligation**: `access_revocation_task_ref` per entitlement. `offboarding_completed_at` may be set only from confirmed outcomes returned by the access model — never from HR record state. The JML case tracks the obligation; case closure is not evidence either. Access is a reference, per the contour's own scope line.

# Invariants

1. Employee number unique within employer scheme and validity window; no cross-employer meaning.
2. Employing-party change does not alter the Person anchor.
3. Offboarding initiates access verification; it never proves revocation.
4. Existence of an EmployeeProfile, employee number, payroll account or assignment never asserts employment status.
5. Status is purpose- and jurisdiction-qualified; determinations are bitemporal and never erase prior assertions.
6. Every assignment resolves to exactly one engagement context; at most one `is_primary_assignment` per worker per instant.
7. Relationship end requires a separation basis and effective time, not an empty `end_date`.
8. History is append-only under legal hold; terminated relationships remain resolvable.

# Scenarios

**Dual employment** — one Person; two Employments with two employers; two EmployeeProfiles, two independent numbers; allocations validated per employer only, with any total-capacity rule declared as policy, not derived.

**Agency labor** — agency is employing party; host is `host_organization_ref` and client role; one Employment, successive Assignments per placement; host-side supervision recorded as a functional reporting line, not as employer authority.

**Rehire** — same Person, same EmployeeProfile, same or reissued number per scheme policy; **new** Employment with its own identity, credited prior service via antecedent-service and seniority anchor; the prior relationship stays terminated and readable.

**Incomplete offboarding** — Employment separated, Assignments ended, handover partial; JML case open; two entitlements unconfirmed, so `offboarding_completed_at` stays null and the residual-access exception is visible. No record is deleted or overwritten.

**Misclassified freelancer** — asserted basis was contract-for-services; indicators show control and integration; a competent determination lands retroactively. Result: same relationship identity, new determination with its own effective period, prior party assertions immutable, EmployeeProfile created with a backdated effective start. Only a determination substituting the employing party creates a successor binding.

# Profile shape

EM‑PEO‑02 adds: the EmployeeProfile type; a bound `relationship_kind` vocabulary mapped to WM-ORG-005 basis and status assertions; the employer/work-customer/supplier role triple; the numbering rule; the access-verification obligation with confirmed-outcome gating; and a typed JML case reference. v1 fields map as: `relationship_kind`, `jurisdiction`, `start_date`, `end_date` → WM-ORG-005 (split start into agreed/actual/effective; replace `end_date` with interval plus separation event); `employee_number`, `worker_category`, `person_ref`, `employment_ref` → EmployeeProfile (last one multi-valued); `assignment_kind`, `allocation_fte`, `valid_period`, `primary_flag` → WM-ORG-016. The profile re-owns no person attribute, contract term, payroll record or access grant.

# Holds

No canonical or installability claim is made for any model or for this review. The COMPOSE relations remain candidate; the realization link is unapproved. WM-ORG-005's semantics rest on a single-provider waived adjudication. The Employment/Membership split from legacy O3 is untested here. WM-ORG-016's personnel-action and time-limited-form nodes are jurisdiction-parochial and its retention and FTE dimensions are declared gaps. HR Open, ESCO/SFIA and SPACE comparison tracks were not exercised — no crosswalk is asserted. EmployeeProfile has no registry identifier and none was invented.
