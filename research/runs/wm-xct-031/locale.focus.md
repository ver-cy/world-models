Research only the language, locale, script and negotiation plane of WM-XCT-031
Localization / Language.

- Use the exact registry identity and output `entry_kind` `mixin`. Treat the
  subject as an embeddable, format-neutral declaration of linguistic and
  locale context, not as the localized content, person profile, geographic
  region, jurisdiction or translation workflow.
- The `model` block must describe the complete combined WM-XCT-031 boundary,
  including language/locale identity, translation/fallback bindings and
  governance. Never mention a split, pass, sibling pass or partial delivery in
  model, coverage or adversarial prose.
- Cover BCP 47 language-tag identity and canonical form; language, script,
  region, variant, extension and private-use subtags; grandfathered/deprecated
  identifiers and replacement; macrolanguage and extlang caveats; locale
  identity distinct from language identity; Unicode locale extensions;
  script direction and writing-mode hints; matching/filtering/lookup;
  requested, available and resolved locale; ordered preferences; explicit
  fallback outcome and reason; default locale; content-language versus user
  interface locale; number/date/time/unit/collation conventions as referenced
  profiles rather than duplicated data.
- Preserve the distinction between declared language, inferred language,
  locale, script, region, audience preference and resource availability. Do
  not infer nationality, jurisdiction, ethnicity or physical location from a
  language or locale tag.
- Target 2 bundles, 4-5 layers and 8-10 findings with 3-5 discriminating
  questions each. Use at least seven question kinds and concise descriptions.
- Every local ID, including bundle, layer, finding, question, data element,
  artifact and function IDs, must begin with `loc-locale-`.
- Limit functions to parsing/canonicalizing tags, validating registry
  references, matching/filtering/lookup and resolving declared preferences.
  Provide complete valid service_layers and coverage, but the merger takes
  canonical service layers from `governance`.
- Prefer primary IETF BCP 47/RFC 5646/RFC 4647, IANA Language Subtag Registry,
  W3C Internationalization and Unicode/CLDR specifications. Distinguish
  normative standards from implementation guidance and never claim unseen
  paywalled clauses.
