# WM-XCT-011 — Identifier Scheme research

Status: **reviewable draft; not yet publishable**.

Both independent provider outputs pass the Vercy research schema and semantic
gate. Claude and Grok agree that the model is a reusable `mixin`, not the model
of a person, organization, document, product or other identified referent.

## Scale

| Result | Sources | Bundles | Layers | Findings | Questions | Artifacts | Functions |
|---|---:|---:|---:|---:|---:|---:|---:|
| Claude | 23 | 6 | 20 | 23 | 112 | 25 | 13 |
| Grok | 16 | 6 | 12 | 24 | 80 | 18 | 9 |
| Synthesis | 33 | 6 | 20 | 29 | 130 | 27 | 14 |

## Synthesized bundles

1. Scheme Constitution and Lexical Form
2. Authority, Delegation and Registration Policy
3. Assignment, State and Continuity
4. Resolution, Dereference and Persistence
5. Interoperability, Carriage and Conflict
6. Assurance, Privacy and Legal Continuity

The synthesis uses the standards-led Claude hierarchy as its structural base and
adds Grok's separately evidenced findings for granularity/qualifiers, split and
merge continuity, scheme-specific resolution parameters, access-controlled
resolution, embedding/encapsulation and the portable computational identifier
tuple. It also adds authority transfer as a separate function.

## Important decisions

- Identifier non-reuse is a versioned per-scheme rule, not a universal invariant.
- Canonicalization and equivalence are scheme-scoped; no universal normalizer is
  valid across URI, URN, XML Namespace, ARK, DOI and other scheme families.
- Possession of an identifier never proves identity, authentication or authority.
- A persistent identifier and a permanently available representation are distinct
  promises; tombstone and metadata behavior must be explicit.
- Split, merge, alias and authority succession are first-class lifecycle cases.

## Publication holds

- Live URL, edition and claim-level support must be verified for all accepted
  sources.
- Deferred families must be researched or explicitly excluded: E.164 and number
  portability, content-addressed IDs, ledger addresses, direct paywalled ISO
  clauses, machine-readable scheme-description languages and registry disputes.

See `adjudication.json` for every explicit acceptance/rejection decision,
`comparison.json` for provider overlap, and `synthesis.validation.json` for the
machine gate.
