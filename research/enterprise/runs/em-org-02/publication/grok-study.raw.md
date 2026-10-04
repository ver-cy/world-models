**Verdict.** PROFILE all three. No new catalogue or runtime ID. WM-ORG-001 is the single organization / legal-subject master. WM-ORG-010 is re-subjected to registration *records*, each referencing exactly one 001 subject. WM-ORG-011 is narrowed to operating presence and only references registration evidence. This is standards alignment, not a GLEIF, ISO 17442 or companies-register conformance claim.

**Subject / record mastership.** Source facts: the card says a registry record has its own identity and a verifiable basis; registration status does not substitute for subject status. 010 today treats the pair (registration authority, assigned identifier) as legal-person identity — that is the defect this PROFILE corrects. 001 already holds legal personality, subject lifecycle and succession. 011 already states there is no universal equivalence of branch, legal entity and premises.

- **001** owns subject identity, `legalPersonality`, subject status with its own validity, name forms, and succession continuity. It does not own the register line. A subject may have `legalPersonality=false` (registered branch) and remain a 001 subject attributed to a head-office subject.

- **010** owns the register/authority, scheme, number, record status, evidence extract, issue/lapse dates, and `subjectRef` cardinality 1. The pair (authority, number) identifies a *record*, not a person. One subject may have many 010 records (national number, LEI, VAT, foreign-branch entry). LEI, tax/VAT, national number and EUID are records under different schemes, not extra subjects.

- **011** owns presence kind, operator / head-office attribution, site / premises reference, local activity and opening/closing. It references a 001 subject and, when present, 010 evidence. It does not mint a subject and does not assert personality.

**Identifier equality.** A number is unique within scheme and jurisdiction (card invariant). Two identifier tokens are the same registration identifier only if `(scheme, authority-or-jurisdiction, number, overlapping validity)` match. A bare number with no scheme is uninterpretable. Cross-scheme links (LEI ↔ company number ↔ VAT) are explicit, evidenced equivalence assertions with source, confidence and validity — never string equality. Importing a record cannot create or merge a subject.

**Status distinctions.** Six independently dated planes. None substitutes for another. Missing on one plane is `unknown`, not copied.

1. **Subject status** (001) — active, in liquidation, dissolved, converted, informal. A lapsed LEI does not dissolve the company.
2. **Registration-record status** (010) — pending, issued/published, lapsed, retired, duplicate, annulled, transferred.
3. **LEI status** — a 010 record under the GLEIF scheme. Issued / Lapsed / Retired is record status. LEI EntityStatus is a *claim about the subject*, stored as evidence pointing at 001. GLEIF itself separates EntityStatus from RegistrationStatus.
4. **Tax / VAT registration status** — a separate 010 record. VAT deregistration ≠ dissolved subject.
5. **National register-number status** — 010 under that authority. A strike-off proposal is a record/procedure flag until 001 is updated from an authoritative event.
6. **Evidence extract** — an observation of a 010 record at a knowledge-time. Extract currency ≠ current record status ≠ subject status.

As-of queries apply one `(valid-time, knowledge-time)` pair to subject, each record and each extract separately.

**Branch / presence boundary.** Registration, personality and premises are separate tests. A registered branch with no separate legal personality:

1. Personality on 001: head-office subject `legalPersonality=true`. If a branch-as-organization row is kept, it has `legalPersonality=false` and `bearingLegalPerson →` head office. Never mint personality from a branch number. GLEIF alignment: an international branch is the same legal person as its head office; it may hold its own LEI as a *record*.
2. Head-office attribution on 011 (or a 012 relationship).
3. 010 branch or LEI-BRANCH record keyed by (authority, number), `subjectRef` to the non-person subject.
4. 011 presence for premises/activity, referencing that 010 evidence.

Passing registration does not pass personality. Passing premises does not pass registration. An unregistered domestic site is 011 only.

**Succession.** 001 owns predecessor/successor edges with transition kind (merger, split, absorption, conversion), effective time, continuity decision and carried/lapsed identifiers. 010 may record register-side events (struck off, converted, successor number in *that* register) pointing at the same 001 edge. Historical contract parties stay the 001 identifiers current at formation. Succession adds edges; it never rewrites those party identifiers (card invariant).

**Scenario results.**

*Negative — new extract creates a duplicate company.* Extract from register B arrives with a different (scheme, authority) pair. Correct path: create or update a 010 record; bind to an existing 001 subject only by evidenced equivalence; otherwise remain `unresolved`. Same scheme+authority+number+overlap as an existing 010 → same record (or record-status DUPLICATE). Minting Company-2 fails the card.

*Acceptance — one subject, three records, non-person branch, merger.* Subject S has 010-R1 (national register ISSUED), 010-R2 (LEI, possibly lapsed independently), 010-R3 (VAT). Branch B: 001 with `legalPersonality=false`, attributed to S; 010 branch record; 011 presence. Merger at \(t_m\) adds S → S′. Contracts dated before \(t_m\) still cite S. As-of \(t < t_m\): S is current; three record statuses independently dated; B visible if valid at \(t\). As-of \(t \ge t_m\): S′ is current; S remains resolvable via the edge; B attribution changes only by an explicit act.

**Migration field moves.**

- 001 → 010: register-authority + number used as subject identity; register-record status living only on the organization; extract-as-identity; alternate scheme numbers stored as if they were the 001 key. 001 keeps subject id, `legalPersonality`, subject status, succession edges, name forms, and a derived index of bound 010 records.
- 010 → 001: drop “authority+number *is* the legal person.” Each record gains mandatory `subjectRef`. Legal form / personality copied from an extract become claims on the record, accepted onto 001 only by an evidenced subject update. 010 entity-status axis becomes a projection, not a second write path.
- 011: drop any field that asserts personality or treats a branch number as a new 001 id. Keep kind, operatorRef, site, activity, evidenceRef → 010.

**Required constraints.** One 010 record → exactly one 001 subject. Import creates records, not subjects. Identifier equality = scheme + authority/jurisdiction + overlapping validity. Cross-scheme equivalence is explicit and evidenced. Six status planes never substitute. 011 references; it does not master subjects. Succession adds edges; contracts keep historical party ids.

**Publication blockers.** All three bases are non-canonical reviewable drafts; 011 has no independent external review. 010’s published identity rule still equates authority+number with the legal person until the PROFILE text lands. Dual-write of subject status versus 010 entity-status is unresolved. No executable fixtures for: extract-does-not-mint-subject; three independently dated records; four-test non-person branch; merger that preserves historical contract parties; as-of queries with mixed record statuses. Source-pin holds on 010 (RA list, ELF, BRIS instrument) remain. Alignments to GLEIF LEI-CDF, ISO 6523 and ISO 17442 are alignments only. Do not invent LegalEntity, Registration or Branch runtime identifiers.
