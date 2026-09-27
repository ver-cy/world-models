# EM-PEO-01 local synthesis

## Disposition

Create a restricted Enterprise profile over WM-PER-001; no new ID. AccountBinding stays outside the person model and remains an identifier-unassigned sibling candidate if no existing contract owns it.

WM-PER-001 masters a person anchor, time-bounded names, qualified identifiers, contact points and identity evidence. HRIS/ATS/LMS records reference the anchor but never become its universal master. Civil facts remain registrar-sourced; contacts, preferred language and usage names may be person-controlled; employment assertions belong to the employment relationship.

## Linking rules

- Display name and email are never identity keys.
- Deterministic linking requires a non-reassigned scheme-qualified identifier in the same authority and applicability domain.
- Other matches create proposed links with confidence, rule-set version, state and authorising role.
- Merge preserves resolvable tombstones and supports reversal.
- Evidence and assurance confirm identity; similarity does not.

Names are versioned assertions. Name change closes one interval and opens another without changing the person anchor. Usage names and pseudonyms are typed aliases with assurance. Local/pairwise pseudonyms may support continuity inside one purpose but cannot seed cross-domain merging.

## Invariants

1. Identity elevation requires evidence or a no-reuse qualified identifier.
2. Every disclosure declares purpose and released attributes.
3. Employer ownership is limited to relationship assertions.
4. Reference identifiers are opaque.
5. Event, registration and observation times remain separate.
6. Contact verification proves channel control, not person identity.
7. Uncertain matches remain proposals.

The namesake scenario keeps two anchors distinct across HRIS, directory and LMS. A legal-name change preserves history. An uncertain LMS link remains a proposal until authorised evidence review.

## Holds

The base is non-canonical. CPV and ISO 24760 version conflicts, the EM-to-WM crosswalk, owner/master-system contradiction, link-state/authoriser fields, account-binding ownership and non-EU validation remain unresolved.
