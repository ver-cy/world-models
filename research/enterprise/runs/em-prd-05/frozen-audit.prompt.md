# Frozen no-tools semantic audit — EM-PRD-05

You are the final static semantic auditor. Use only this frozen packet. Do not browse, call tools, invent identifiers, give legal advice or grant publication authority.

Disposition: PROFILE. IPAsset is a non-authoritative view; IPRegistration and RightsClaim profile WM-KNW-003 with WM-REC-001 evidence; UsageGrant profiles WM-ECO-006 plus WM-XCT-029. No new model or runtime identifier is allocated. Standalone UsageGrant identity is held unless instrument-independent grants are proven.

Reconciled boundary:
1. Protected subject, right, application, territorial registration, RightsClaim, creator attribution, assignment, UsageGrant and obligation remain distinct.
2. IPAsset combines exactly one upstream subject with referenced rights and has no durable master key, write authority or assignable/licensable identity.
3. Registration is one territory plus one register. Multiple registrations never merge into a worldwide right.
4. RightsClaim is dated and sourced, never mints a right and never proves title alone.
5. Application is neither registration nor grant; refusal preserves its record and creates no right.
6. UsageGrant is the permission envelope on a contract with WM-XCT-029 duties. Scope states exclusivity slice, field, channel, territory, term, acts, sublicensing and survival.
7. Sublicense requires parent authority and cannot exceed the parent. Assignment transfers an owned right basis and is not a license or registration.
8. Subject creation, application, registration, claim, grant and obligation survival use independent clocks and states.
9. Grant expiry never changes subject or registration. Surviving duties remain on the spent contract and never extend the grant.
10. Brand association and logo use imply no registration, ownership, exclusivity or worldwide right.
11. Sign and invention lack a named subject authority; this is a hold, never a reason to promote IPAsset.

Scenario: one sign has two independently identified territorial registrations. A licence expires before both, while final reporting, audit and confidentiality obligations survive. After expiry the grant is expired, both registrations remain governed by their own states, surviving WM-XCT-029 duties remain active on the spent contract, and the IPAsset view still points to one subject plus two rights. No worldwide exclusivity is inferred from the logo.

Audit questions:
- Is any hidden root or identifier introduced despite `newRuntimeId=false`?
- Are subject, right, application, registration, claim, assignment, grant and obligation mastership and lifecycle unambiguous?
- Does UsageGrant require independent identity now, or can contract/obligation profiling carry addressability safely?
- Can territory, time, ownership, exclusivity, sublicense or survival still leak across boundaries?
- Identify contradictions that make even a held profile unsafe.

Return at most 500 words with exactly: Verdict (`ACCEPT WITH LIMITS`, `REVISE`, or `REJECT`); Critical findings; Required holds; Scenario result; Identifier decision. Treat missing base specifications as holds unless they contradict the profile.

## Candidate
```json
{
  "format": "vercy-enterprise-profile-candidate/v1",
  "contourId": "EM-PRD-05",
  "name": "Enterprise Intellectual Property and Usage Rights",
  "decision": "PROFILE",
  "newRuntimeId": false,
  "bases": [
    "WM-KNW-003",
    "WM-MED-001",
    "WM-ECO-006",
    "WM-XCT-029",
    "WM-REC-001",
    "WM-ORG-001",
    "WM-PER-001"
  ],
  "constraints": [
    "IP Asset is a view combining protected subject matter with governed rights and never mints another subject identity.",
    "Protected subject matter, legal right, application, registration, rights claim, attribution, assignment and usage grant remain distinct.",
    "WM-KNW-003 owns right, application and registration lifecycle while subject matter remains with WM-MED-001 or its domain authority.",
    "Filing, certificate and recordal evidence remain WM-REC-001 records and parties retain WM-ORG-001 or WM-PER-001 identity.",
    "A right-holder statement is a dated sourced claim; registered holder, beneficial-owner assertion and creator attribution remain distinct.",
    "An application is identified by office and application number, survives refusal, seeks a right and is never the granted right.",
    "Registration is scoped by register, number and territory, and grant, renewal, lapse, expiry, revocation and invalidation have separate effects and times.",
    "Absence of registration never proves absence of a right when the applicable legal basis permits unregistered rights.",
    "A usage grant references exact right set, exclusivity slice, field, channel, territory, term, limits, permitted acts, prohibitions and sublicensing rule.",
    "A sublicense never exceeds its parent grant and a license never transfers ownership without a separate assignment basis.",
    "Surviving duties remain WM-XCT-029 obligations after grant termination and never inherit registration lifecycle automatically.",
    "Brand association and logo use are evidence of commercial use, not proof of registration, ownership, exclusivity or worldwide scope.",
    "IPAsset is a non-authoritative view of exactly one protected subject plus zero or more referenced rights; it has no durable key, system-of-record role or assignable/licensable identity.",
    "IPRegistration and RightsClaim remain profiles of WM-KNW-003; registration evidence and any registration number remain WM-REC-001-governed records.",
    "RightsClaim is a dated sourced assertion and never mints a right or proves title by itself.",
    "UsageGrant remains a contract-and-obligation profile over WM-ECO-006 and WM-XCT-029; instrument-independent grant identity is held until evidence proves grants without instruments.",
    "A registration covers exactly one territory and one register; multiple registrations over one sign never merge into a worldwide right.",
    "Creator attribution, ownership claim, registrant listing, assignment, licence and brand association are pairwise non-implying.",
    "Application, registration, grant and obligation have independent status and time axes; expiry of one never mutates the others.",
    "Grant scope is incomplete unless exclusivity slice, field, channel, territory, term, acts, sublicensing authority and survival are present or explicitly unbounded.",
    "Surviving obligations stay bound to the spent contract, retain WM-XCT-029 lifecycle and never extend grant status.",
    "Sublicense is another UsageGrant, requires parent authority and cannot exceed the parent on any scope axis.",
    "Sign and invention subject authority remains an explicit coverage gap and never justifies promoting IPAsset to a master."
  ],
  "holds": [
    "WM-KNW-003 and WM-MED-001 lack complete current specifications.",
    "Subject-matter crosswalks, territorial code lists and several non-registration rights remain unresolved.",
    "Standalone Usage Grant identity remains unsupported by current evidence.",
    "Grok Heavy accepted the profile-only disposition, rejected all four new identities and held UsageGrant standalone status unless instrument-independent grants are proven."
  ],
  "version": "0.1.0-candidate.2"
}
```

## Fixtures
```json
{
  "format": "vercy-enterprise-profile-fixtures/v1",
  "profileName": "Enterprise Intellectual Property and Usage Rights",
  "cases": [
    {
      "id": "two-territorial-registrations",
      "kind": "positive",
      "input": "One brand references one sign registered separately in territories A and B with different expiry dates.",
      "expect": "The brand, sign and two registrations remain separately identifiable and independently queryable."
    },
    {
      "id": "license-expires-first",
      "kind": "positive",
      "input": "A non-exclusive license covering both territories expires in 2027 while registrations expire in 2029 and 2032.",
      "expect": "The usage grant ends in 2027 without changing either registration lifecycle."
    },
    {
      "id": "surviving-duties",
      "kind": "positive",
      "input": "The grant terminates while final reporting, audit and confidentiality duties survive.",
      "expect": "The grant is terminated and the surviving WM-XCT-029 obligations remain active with their own deadlines."
    },
    {
      "id": "application-refused",
      "kind": "positive",
      "input": "A territorial application is refused after claiming priority.",
      "expect": "The application identity and priority evidence remain resolvable while no granted right is inferred."
    },
    {
      "id": "creator-equals-owner",
      "kind": "negative",
      "input": "A creator attribution is used as conclusive proof that the creator owns the right.",
      "expect": "The ownership conclusion is blocked until a dated sourced ownership claim or assignment basis is provided."
    },
    {
      "id": "worldwide-logo-claim",
      "kind": "negative",
      "input": "Use of one company logo is treated as proof of exclusive trademark rights worldwide.",
      "expect": "The claim is rejected because brand use does not establish territorial registration, ownership or exclusivity."
    },
    {
      "id": "overbroad-sublicense",
      "kind": "negative",
      "input": "A sublicense grants a territory and field of use outside the parent license.",
      "expect": "The sublicense is invalid under the profile because its scope exceeds the parent grant."
    },
    {
      "id": "ipasset-durable-key",
      "kind": "negative",
      "input": "A portfolio assigns a durable master key to the IPAsset view and licenses that key directly.",
      "expect": "Reject the master identity and require references to the protected subject, rights and contract grant."
    },
    {
      "id": "claim-mints-right",
      "kind": "negative",
      "input": "A dated claimant assertion automatically creates a legal right.",
      "expect": "Reject promotion; the claim remains sourced evidence and does not mint a right."
    },
    {
      "id": "registrant-implies-owner",
      "kind": "negative",
      "input": "A register listing is treated as conclusive current beneficial ownership.",
      "expect": "Keep registrant listing and ownership claim distinct and require dated provenance."
    },
    {
      "id": "assignment-mints-registration",
      "kind": "negative",
      "input": "Assignment of one territorial right creates a registration in another territory.",
      "expect": "Reject the inferred registration and preserve independent territorial records."
    },
    {
      "id": "survival-does-not-extend-grant",
      "kind": "positive",
      "input": "Confidentiality and audit obligations survive an expired licence.",
      "expect": "Keep obligations active on the spent contract while the UsageGrant remains expired."
    },
    {
      "id": "application-not-grant",
      "kind": "negative",
      "input": "A pending application is used as permission to exploit the sign.",
      "expect": "Reject the grant inference; application is neither registration nor UsageGrant."
    }
  ],
  "version": "0.1.0-candidate.2"
}
```

## Claude study
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


## Grok study
# Verdict

**ACCEPT WITH CONDITIONS.** None of IPAsset, IPRegistration, RightsClaim, or UsageGrant needs independent identity. IPAsset is a non-authoritative view of one protected subject plus its right set. IPRegistration and RightsClaim profile WM-KNW-003; registration also uses WM-REC-001. UsageGrant profiles and extends WM-ECO-006 and WM-XCT-029. Conditions: keep work/sign/invention, right, application, territorial registration, ownership claim, creator attribution, assignment and license separate; application is not grant; registration is per territory and register; license scope is declared; brand association is not trademark registration; rights claims are dated and sourced; a company logo does not imply worldwide exclusive rights.

## Strongest evidence

The required test is inexpressible if asset, registration, grant and obligation collapse. After the license ends, both territorial registrations remain live, surviving obligations persist on the spent contract, and the view still shows the sign plus two rights without treating the grant as a right.

## Strongest counterexample

Inferring one worldwide exclusive IPAsset, or worldwide exclusive rights, from a company logo or from a single territorial registration.

## Identity / mastership

Explicit decision: no candidate needs independent identity. IPAsset must not receive a durable key and is not a system of record. IPRegistration is a profile of WM-KNW-003 plus WM-REC-001; any registration number lives on the record. RightsClaim is a dated, sourced profile of WM-KNW-003 and does not mint a right. UsageGrant is not a free-floating grant master: the test case is a license with surviving obligations, which is contract plus obligation. Instrument-independent grants are not proven. Mastership stays on party masters, subject matter, WM-KNW-003, WM-REC-001, WM-ECO-006 and WM-XCT-029.

## Subject / right

Work (WM-MED-001), sign and invention are subjects and persist when rights lapse. WM-KNW-003 is the right. IPAsset = one subject ∪ 0..n rights. One subject may carry many rights; one right has one primary subject. Creator attribution attaches to the subject, not to the right or the registration. Sign and invention have no named subject master in the given list; that is a coverage gap, not a reason to promote IPAsset.

## Application / registration

Application is a request to a register. It is not a grant, not a license and not a registration. Treat it as a filing or pre-grant state of WM-KNW-003 plus WM-REC-001; do not add a type. Registration is per territory and per register. One sign in two territories is two registration profiles of two rights, each with its own record and status. Application to registration is 1:0..n.

## Ownership / claim

Keep four facts distinct: creator attribution on the subject; ownership claim over a right; assignment as a conveyance that changes holder; RightsClaim as a dated, sourced assertion. A claim is not title. Party masters identify creators, claimants, owners, registrants, licensors and licensees. Do not infer owner from registrant listing or from logo use.

## Usage grant

UsageGrant profiles WM-ECO-006 and WM-XCT-029. Scope must declare exclusivity slice, field, channel, territory, term, acts, sublicensing authority and survival (present or explicitly unbounded). Application is not grant. Grant expiry does not expire registrations or the subject. Surviving obligations remain WM-XCT-029 on the spent contract and do not extend grant status.

## Territory / time / status

Time axes are independent: subject creation, application, registration, claim date, grant term, obligation survival. Status is local to each registration and each grant. One territory does not project onto another. Grant term does not project onto registration term. Brand association has no territorial right-scope.

## Brand / trademark

Three layers: sign as subject; brand association as a party-to-sign fact with no register, term, exclusivity or territory; trademark registration as an IPRegistration profile, one territory, one register. Logo presence is association only. Worldwide logo use does not create worldwide or exclusive rights.

## Assignment / sublicense / obligations

Assignment (WM-ECO-006) conveys the ownership-claim holder on a specified right; it is not a license or a registration. Sublicense is a further UsageGrant, only if the parent states authority, and cannot exceed parent scope on any axis. Surviving obligations stay bound to the spent instrument and receive no new identity. Do not use IPAsset as the assignable or licensable object.

## Scenario

Sign S. Party P associated with S as house mark — association only. Reg-T1: S in T1, register X, registered through D1. Reg-T2: S in T2, register Y, registered through D2. License L on contract C expires D0, with D0 < D1 and D0 < D2; scope explicit; survival set {O}. After D0: L expired; both registrations remain registered; {O} persist as WM-XCT-029 on C; IPAsset view of S = S + {Reg-T1, Reg-T2}. Rejected inferences: logo ⇒ worldwide exclusive rights; one registration ⇒ the other territory; grant term ⇒ registration term; association ⇒ ownership claim.

## Invariants

1. No candidate receives a new identity key.
2. IPAsset is not system of record for subject, right, claim or grant.
3. Subject is not the right; one subject may have many rights.
4. Application is not grant and not registration.
5. Each registration is exactly one territory and one register.
6. A RightsClaim is dated and sourced, or it is not a valid instance.
7. Creator attribution ≠ ownership claim ≠ registrant listing ≠ license.
8. License scope is incomplete unless exclusivity slice, field, channel, territory, term, acts, sublicense flag and survival are explicit or explicitly unbounded.
9. Grant expiry does not change registration status or subject identity.
10. Surviving obligations persist as WM-XCT-029 after grant term; they do not extend the grant.
11. Brand association is not trademark registration and implies no exclusive or worldwide right.
12. Two registrations of one sign never merge into one worldwide right.
13. Sublicense requires parent authority and cannot exceed parent scope.
14. Assignment does not mint a registration or grant; license does not mint an ownership claim.
15. Worldwide exclusive rights shall not be inferred from a company logo or from a single-territory registration.

## Minimum model set

Subject: WM-MED-001 for works; sign and invention as distinct subject kinds without new identifiers. Right: WM-KNW-003. Record: WM-REC-001. Contract: WM-ECO-006. Obligation: WM-XCT-029. Party masters. Views/profiles only: IPAsset, IPRegistration, RightsClaim, UsageGrant.

## Blockers

B1: if a later corpus shows grants with no instrument, reopen UsageGrant identity. B2: sign and invention lack a named subject master; flag the gap; do not invent identifiers; do not promote IPAsset to master. B3: exclusivity slice, field, channel and acts are grant-profile attributes, not new types. B4: an operational portfolio number on the view is an external reference, not a new master.

