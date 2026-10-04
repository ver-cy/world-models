# Verdict

**Profile.** EM-PRD-05 is an **enterprise IP and usage-rights profile** over legacy **WM-KNW-003 Intellectual Property Right**, composed with **WM-MED-001 Creative Work** (protected subject matter), **WM-ECO-006 Commercial Contract** (licence and assignment instruments), **WM-XCT-029 Obligation / Commitment** (licence duties and surviving obligations), **WM-REC-001 Document / Record** (filings, certificates, evidence), **WM-ORG-001 Organization** and **WM-PER-001 Person** (holders, creators, applicants, licensees). No identifiers are allocated. Of the four candidate types, only **UsageGrant** shows a credible case for new owned structure, and even that is provisionally an extension of the contract/obligation pair rather than a standalone model; **IPAsset**, **IPRegistration** and **RightsClaim** are reuse or profile-level structures over the legacy model plus WM-MED-001 and WM-REC-001.

This is a modelling decision, not legal advice, not a claim of canonical completeness, and not installable.

# Evidence

Legacy WM-KNW-003 already separates the right from the work (`validation_flags: "право, не произведение"`), and already carries `ipRight`, `ipApplication`, `registration`, `priorityClaim`, `license`, `assignment`, `opposition`, `renewal`, with events `applicationFiled → applicationPublished → rightGranted | rightRefused`, `oppositionFiled`, `rightAssigned`, `rightLapsed`. It composes REFERENCE to person, organization, creative work, software product, identifier/naming, and COMPOSE to document/record. WM-MED-001 owns the work/expression/manifestation ladder (`FRBR/LRM WEMI внутри, не снаружи`) and explicitly refers rights formalisation out to N12. Both are `described-previous-version`, `migration-boundary-review`, evidence depth `index-and-publication-metadata`; the dossier states published ≠ completed independent expertise. WM-ECO-006, WM-XCT-029, WM-REC-001, WM-ORG-001 and WM-PER-001 are all `publishableCanonical: false`. The v1 predecessor PRD-08 contributes `right_kind`, `territory`, `registration_ref`, `expiry_date`, all `candidate-not-normative`. No relations rows touch WM-KNW-003 or WM-MED-001, so every edge asserted here is a candidate.

# Identity/mastership

- **Work / subject matter** — mastered by WM-MED-001 (creative works) or the relevant subject-matter model (software, invention disclosure, sign/mark as a designation). Identity survives every right over it.
- **Right** — mastered by WM-KNW-003. Identity is (right kind, protected subject matter, territory, legal basis). A right is not the work and not the registration.
- **Application** — mastered by WM-KNW-003 (`ipApplication`). Identity is office plus application number; it survives refusal, so it cannot be identified by the right it sought.
- **Registration** — mastered by WM-KNW-003 (`registration`), identity = register plus registration number plus territory. Its instrument documents are WM-REC-001 records.
- **Rights claim / ownership assertion** — a dated, sourced assertion with a claimant, not a fact of the right. Profile-level structure over WM-KNW-003 holder fields plus WM-REC-001 evidence and provenance.
- **Creator attribution** — references WM-PER-001 / WM-ORG-001 via WM-MED-001 `contribution`; distinct from ownership and from moral-right assertions.
- **Assignment** — WM-KNW-003 `assignment`, instrument in WM-ECO-006, recordal act in WM-REC-001.
- **Licensed use (UsageGrant)** — instrument in WM-ECO-006, permissions and duties in WM-XCT-029; the grant is the addressable permission envelope over a named right set.

Registrar masters register content; holder masters portfolio and exploitation records (legacy stewardship: "right holder; IP registrar keeps register").

# IP asset/right

**IPAsset is a profile view, not new structure.** Two readings collapse into it: the protected subject matter (WM-MED-001 work, software product, invention disclosure, sign) and the commercially managed bundle of rights over it. Neither justifies independent identity: the first is owned upstream, the second is a portfolio projection. The profile therefore defines *protected-subject-matter reference* + *right set*, and forbids storing work attributes on the right.

**Right** stays WM-KNW-003 `ipRight` with `rightType`, `subjectMatterRef`, `territory`, `term`, `status`. Profile adds: basis kind (registration-derived vs arising-by-operation-of-law, e.g. copyright), and an explicit statement that an unregistered right may exist with no `registration`.

# Application and registration

A patent application is a **pending claim to a right, not a right**: it confers a filing date and priority position, is publishable, and terminates in grant, refusal, withdrawal or abandonment. A granted right has enforceable scope fixed by the granted claims or registered classes. Model as separate objects with a directed `seeks` edge, so refusal leaves the application intact and creates no right. Priority is `priorityClaim` (priority date, prior application, convention basis) attached to the application, never to the right. Registration is per-territory: one application family yields N registrations. Lifecycle: `filed → published → (granted | refused | withdrawn)`; then `granted → renewed* → (lapsed | expired | revoked | invalidated)`. Renewal extends a registration; revocation/invalidation is an adjudicated outcome referencing an `opposition` or court act, not a renewal failure.

# Rights claim/ownership

Separate three things the legacy model blurs:

1. **Right-holder of record** — what the register says, sourced from a registration extract.
2. **RightsClaim** — an assertion by a claimant that they hold a right (or a share) over subject matter in a territory, with basis (registration, assignment chain, employment/work-for-hire, statutory vesting, first publication), supporting evidence, assertion date, and status (asserted, corroborated, contested, withdrawn, adjudicated). This is where register and reality can diverge, and it is the object that carries corroboration level.
3. **Creator attribution** — who made it. Never a claim of ownership and never inferred from ownership.

Evidence stays WM-REC-001 records (filing receipts, certificates, recordal confirmations, assignment deeds, publication proofs) with fixity, custody and dated validation outcomes.

# Usage grant/license

**UsageGrant** is the one candidate with a real case for owned structure, because it is the addressable permission envelope that relying parties read, and it has a lifecycle independent of both the right and the contract: it can expire, be suspended, be terminated for breach, or be sublicensed while the right and the agreement persist. Its required dimensions:

- **Exclusivity**: exclusive, sole, non-exclusive — with the field-of-use/territory/channel slice over which exclusivity holds, because exclusivity is never global unless stated.
- **Sublicensing**: permitted / prohibited / permitted-with-consent; if permitted, whether downstream grants may exceed the parent's scope (they may not) and whether they survive parent termination.
- **Field of use**, **channel**, **territory**, **term** (start, end, renewal, evergreen/notice) and **quantity/volume caps** where present.
- **Permitted acts** and **prohibited acts** as directed permissions and prohibitions in WM-XCT-029, each traced to a source clause in WM-ECO-006.
- **Surviving obligations** after term end: royalty reporting and payment for the final period, audit rights, confidentiality, sell-off/run-off rights for existing inventory, attribution, return or destruction of materials, indemnity for pre-termination acts. Survival is WM-ECO-006 `termination-expiry-and-survival` plus WM-XCT-029 limitation/survival.

Recommended disposition: **profile-and-extend** — treat UsageGrant as an extension point on WM-ECO-006 with obligations in WM-XCT-029, and re-test for standalone status only if grants are found to exist without any instrument.

# Territory/time/status

Territory is per-right and per-registration, coded (ISO 3166-1/-2 or the register's own territorial designation for regional systems), never a single string on a global asset. Right kind is coded against a named scheme with version. Times to keep distinct: filing, priority, publication, grant, each renewal, expiry (computed from term rules), lapse (non-payment), revocation/invalidation (adjudicated, may be retroactive), assignment effective vs recordal, licence start/end/termination — plus separate event, authority-recording and observation times, RFC 3339 with explicit offset. Status is at least three independent state machines: right status, registration status per territory, and grant status. Collapsing them is the standard defect.

# Brand versus trademark

A **brand / business association** is a commercial and reputational construct: names, logos, styling, positioning, goodwill, applied across products and markets. A **trademark registration** is a territorial legal act over a specific sign in specific classes at a specific office. One brand maps to N signs and N×M registrations, and may have unregistered common-law or use-based protection in some territories and none in others. Model brand as a marketing/product-portfolio concept referencing sign designations and the registrations covering them; model the sign as the protected subject matter; keep registration in WM-KNW-003. Never derive brand ownership from a registration, or registration scope from brand usage.

# Transfer/sublicense/obligation

**Assignment** transfers ownership of the right and needs a chain of title, an effective date and, for registered rights, a recordal act with its own date; an unrecorded assignment may be valid between parties yet ineffective against third parties, so effective and recordal dates must both be stored. **Licence** grants permission and transfers no ownership: it cannot exceed the licensor's own scope, and its termination restores nothing to the licensee. **Sublicence** is a derived grant whose scope is bounded by its parent and whose survival on parent termination must be stated, not assumed. **Security interests and pledges** over rights are noted as out of scope here. All duties — royalty calculation and reporting, quality control and approval, marking and attribution, non-challenge where lawful, audit cooperation — are WM-XCT-029 obligations with obligor, obligee, due basis, fulfilment criterion and evidence.

# Acceptance scenario

One brand, sign S, two territorial registrations, one licence expiring before one registration:

- Brand B → sign S (protected subject matter).
- Application A1 (office O1) → registration R1, territory T1, granted, renewed, expiry 2032.
- Application A2 (office O2, priority claim to A1) → registration R2, territory T2, granted, expiry 2029.
- RightsClaim by organization H over S in T1 and T2, basis = registrations R1 and R2, corroborated.
- UsageGrant G from H to licensee L: non-exclusive, field of use = apparel, channel = e-commerce only, territory = T1 and T2, term ends 2027, sublicensing prohibited, permitted acts = affix sign to goods in field, prohibited acts = modification of the sign and use outside channel.

Result: at 2028 G has expired while R1 and R2 both remain in force; surviving obligations (final royalty report, audit window, six-month sell-off, confidentiality) are live obligations with G terminated. At 2030 R2 has expired while R1 remains in force, so the rights footprint is territorially asymmetric with no licence over either. Nothing about G's expiry touches either registration's status, and R2's expiry does not affect R1. The model passes if all three timelines are independently queryable.

**Negative case rejected.** A company logo does not prove a worldwide exclusive right. A logo is a sign that may be the subject matter of rights; it is evidence of use, not of registration. Registration is territorial and class-bounded; exclusivity is a property of a claim or grant within a defined slice; unregistered protection, where it exists at all, depends on use and reputation in that territory. The model therefore refuses to infer a right from subject matter, refuses to infer exclusivity from ownership, refuses to infer territory from corporate presence, and requires an explicit per-territory registration or a corroborated basis for each asserted right.

# Invariants

1. A right has protected subject matter and a legal basis; neither may be absent.
2. A right is not its subject matter; the work's identity is independent of every right over it.
3. Registration is per-territory; no registration is worldwide, and absence of registration in a territory is data, not a gap.
4. An application is not a right; refusal terminates the application and creates no right.
5. Priority attaches to an application, never to a right or registration.
6. A licence transfers no ownership; only an assignment with a basis does.
7. A sublicence never exceeds its parent's scope.
8. Exclusivity is meaningless without its field-of-use, channel, territory and term slice.
9. Brand association neither creates nor proves a trademark registration.
10. Creator attribution never implies ownership, and ownership never implies authorship.
11. Grant expiry does not change any registration's status, and registration expiry does not retroactively invalidate lawful pre-expiry licensed use.
12. Revocation/invalidation and lapse are distinct terminations with different retroactivity.
13. Every right-holder statement is a dated, sourced claim, not a fact.
14. Surviving obligations outlive the grant and are enumerated, not inferred.

# Minimal model set

Reuse **WM-KNW-003** (rights, applications, registrations, priority, licence, assignment, opposition, renewal), **WM-MED-001** (work/expression/manifestation), **WM-ECO-006** (licence and assignment instruments), **WM-XCT-029** (licence duties, survival), **WM-REC-001** (filings, certificates, recordals, evidence), **WM-ORG-001** and **WM-PER-001** (parties). Profile adds: brand-to-sign-to-registration mapping, RightsClaim as a dated sourced assertion with corroboration, per-territory registration matrix, and the UsageGrant scope envelope (exclusivity slice, sublicensing rule, field/channel/territory/term, permitted and prohibited acts, surviving obligation set). No new standalone model is warranted on this evidence.

# Holds

All six referenced specs are `publishableCanonical: false`; WM-KNW-003 and WM-MED-001 are `described-previous-version` under `migration-boundary-review` with index-level evidence only, so every crosswalk above is a candidate. Unresolved before any publication claim: the full semantic crosswalk between WM-KNW-003 and WM-MED-001 at field level; whether UsageGrant is an extension of WM-ECO-006 or eventually standalone; whether the sign-as-subject-matter belongs in WM-MED-001 or a separate designation model; right-kind, territorial-designation and register code lists with versions; copyright's arising-by-operation-of-law path, which has no registration anchor in most territories; moral rights, collective management, employment/work-for-hire vesting, trade secrets (no registration at all), and security interests over rights — all unaddressed. Jurisdictional rules on assignment recordal effect, sublicence survival, exhaustion and penalty/liquidated-damages enforceability need legal review that this review does not supply. No identifiers were allocated; no fixtures were run; this is not a canonical or installable release.
