Research only governance, lifecycle and service rules for WM-XCT-031
Localization / Language.

- Use the exact registry identity and output `entry_kind` `mixin`.
- The `model` block must describe the complete combined WM-XCT-031 boundary,
  including language/locale identity, translation/fallback bindings and
  governance. Never mention a split, pass, sibling pass or partial delivery in
  model, coverage or adversarial prose.
- Cover responsible owner, language/locale experts, translators, reviewers and
  release authority; authority to declare defaults and fallback; lifecycle,
  version, effective interval, supersession and deprecation; provenance of
  tags, translations, terminology and inferred values; source revision pins;
  registry/profile version pins; validation and reconciliation; conflicts
  among tags, locale profiles and content claims; audit/evidence references;
  access to sensitive or embargoed localized content; field/resource-level
  disclosure; integrity, retention, legal hold, tombstones and correction by
  supersession; regional or organizational profiles; interoperability
  mappings; accessibility and cultural-review limitations.
- Cover canonical read, create, bind/unbind, update, resolve, validate, review,
  approve, export, redact and delete/tombstone operations for the host-scoped
  mixin, including authorization, idempotency, optimistic concurrency,
  referential integrity, immutable evidence and explicit failure semantics.
- Do not create an independent lifecycle for a language, country, person,
  content item or translation project. Lifecycle verbs govern the binding on
  its host object unless a separately identified resource is explicitly
  referenced.
- Target 2 bundles, 4-5 layers and 8-10 findings with 3-5 discriminating
  questions each. Use at least seven question kinds and concise descriptions.
- Every local ID, including bundle, layer, finding, question, data element,
  artifact and function IDs, must begin with `loc-gov-`.
- Functions own authorization, versioning/supersession, validation,
  reconciliation, approval, export/redaction and disposition. This result
  supplies the canonical complete `service_layers` block for the merged
  result.
- Prefer primary IETF, IANA, Unicode/CLDR, W3C, OASIS, ISO catalogue/public
  material, accessibility, provenance, privacy and records-management
  standards. Preserve unresolved jurisdictional and cultural differences as
  gaps or holds.
