Research only the translation-resource, fallback, terminology and quality
plane of WM-XCT-031 Localization / Language.

- Use the exact registry identity and output `entry_kind` `mixin`.
- The `model` block must describe the complete combined WM-XCT-031 boundary,
  including language/locale identity, translation/fallback bindings and
  governance. Never mention a split, pass, sibling pass or partial delivery in
  model, coverage or adversarial prose.
- Cover stable translatable-unit/message identity independent of source text;
  source and target language/locale bindings; source revision and target
  variant revision; translation state and approval; plural/select categories;
  variables/placeholders and type constraints; markup/code isolation;
  context, meaning, purpose and audience notes; terminology/glossary concept
  bindings; do-not-translate and protected tokens; ordered fallback chain;
  missing-translation policy; inheritance and override provenance; machine,
  human and mixed origin; confidence/quality assertions; review evidence;
  completeness/coverage measures; pseudo-localization and rendering-test
  evidence; external resource/digest references.
- Keep actual documents, message catalogues, translation memories, termbases,
  binary assets and workflow task histories in their owning systems. This
  mixin binds to them and records the minimum semantic/provenance assertions;
  it does not reproduce their storage format or lifecycle.
- Never equate fallback with translation, machine output with approval, string
  equality with semantic equivalence, or locale coverage with usability.
  Preserve source-language changes, stale translations, ambiguous terminology
  and non-textual accessibility alternatives as explicit cases.
- Target 2-3 bundles, 5-6 layers and 9-11 findings with 3-5 discriminating
  questions each. Use at least seven question kinds and concise descriptions.
- Every local ID, including bundle, layer, finding, question, data element,
  artifact and function IDs, must begin with `loc-trans-`.
- Limit functions to binding translation variants/resources, resolving an
  explicit fallback chain, validating placeholders/markup, applying
  terminology constraints and recording review/quality assertions. Provide
  complete valid service_layers and coverage, but the merger takes canonical
  service layers from `governance`.
- Prefer primary Unicode MessageFormat/CLDR material, W3C ITS, OASIS XLIFF and
  TBX, IETF content-language guidance and official accessibility standards.
  Treat vendor TMS practices as scoped evidence only.
