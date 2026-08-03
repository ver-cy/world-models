# N9 Language & Terminology

This meta-model describes languages, scripts and their varieties, the concepts and terms of specialist domains, glossaries that collect them, translations that connect them, and the locale conventions that combine language with territory. It is its own model because linguistic reference data is consumed by every model that displays a label or stores multilingual text, and because terminology (concept-based, authority-managed) follows different rules from free text and must be modelled once for the whole catalogue.

## Manifest

```yaml
muif:
  version: "1.0"
metaModel:
  id: "vercy:world:n9"
  csn: world.languageTerminology
  version: 0.2.0
  displayName: "Language & Terminology"
  description: "Languages, scripts, varieties, concepts, terms, glossaries, translations and locales."
conformance:
  muc: "2.0: Conformant"
  mmas: A1
namespaces:
  - world.languageTerminology
bundles:
  - csn: world.languageTerminology.language
    displayName: "Language"
    layers:
      - world.languageTerminology.language.languageAndScript
      - world.languageTerminology.language.varietyAndUsage
  - csn: world.languageTerminology.terminology
    displayName: "Terminology"
    layers:
      - world.languageTerminology.terminology.conceptAndTerm
      - world.languageTerminology.terminology.glossaryAndDomain
  - csn: world.languageTerminology.translation
    displayName: "Translation"
    layers:
      - world.languageTerminology.translation.equivalenceAndTranslation
      - world.languageTerminology.translation.localeConvention
imports:
  - source: iso-639-15924
    version: "*"
  - source: tbx
    version: "*"
  - source: bcp-47
    version: "*"
```

## Bundles and layers

| Bundle | Responsibility | Layers |
|---|---|---|
| `language` | The languages of the world | `languageAndScript`: languages, scripts, orthographies Â· `varietyAndUsage`: dialects, regional variants, registers |
| `terminology` | Domain meaning fixed in words | `conceptAndTerm`: concepts, definitions, terms, usage status Â· `glossaryAndDomain`: glossaries, term collections, domains |
| `translation` | Crossing language boundaries | `equivalenceAndTranslation`: translations and equivalence degrees Â· `localeConvention`: locale tags and formatting conventions |

## Objects

- `language`: a natural or constructed language; key attributes: languageCodeRef, autonym, status.
- `script`: a writing system; key attributes: scriptCodeRef, direction, exemplarCharacters.
- `languageVariety`: a dialect, regional variant or register; key attributes: varietyType, region, parentLanguageRef.
- `concept`: a unit of domain meaning; key attributes: conceptId, definition, domain.
- `term`: a word or phrase denoting a concept in one language; key attributes: lemma, languageRef, partOfSpeech, usageStatus.
- `glossary`: a managed collection of terms for a domain; key attributes: glossaryId, domain, ownerRef, termCount.
- `translation`: a rendering of a term into another language; key attributes: sourceTermRef, targetTermRef, equivalenceDegree, approvedBy.
- `locale`: a language plus territory convention set; key attributes: localeTag, languageRef, territoryRef, conventions.

## Relationships

- `language` -> writtenIn -> `script` (N:N): languages and their writing systems.
- `languageVariety` -> variantOf -> `language` (N:1): the variety's parent language.
- `term` -> denotes -> `concept` (N:N): terms name concepts; synonyms and homonyms follow.
- `term` -> collectedIn -> `glossary` (N:N): membership of managed term collections.
- `translation` -> renders -> `term` (N:1): the source term the translation carries across.
- `concept` -> broaderThan -> `concept` (N:N): hierarchy within a domain's concept system.
- `locale` -> basedOn -> `language` (N:1): the language component of the locale tag.

## Events

- `termAdded`: a term entered a glossary with a usage status.
- `definitionRevised`: a concept's definition was changed by its authority.
- `translationApproved`: a translation reached approved equivalence status.
- `glossaryPublished`: a glossary edition was released for use.
- `varietyRecognized`: a dialect or variant was formally recognized in the register.
- `localeConventionUpdated`: formatting conventions of a locale changed.

## Contracts

- `terminologyLicenseContract`: reuse terms for glossaries and term collections.
- `translationServiceContract`: engagement terms for producing and approving translations.
- `glossaryContributionContract`: terms under which contributors add terms to a managed glossary.

## Projections

- `termLookupView`: term, concept, definition and approved translations; omits contribution history.
- `bilingualGlossaryExport`: paired source and target terms for one domain and language pair; omits other languages.
- `codeListView`: language, script and locale codes with names; omits terminology content.

## Composition

- REFERENCE `world.identifierNaming` (N8): language, script and locale codes are registered identifier schemes.
- REFERENCE `world.creativeWork` (N5): expression languages and translated works reference languages here.
- REFERENCE `world.place` (P1): territories inside locale tags.
- MIX-IN (offered): a multilingualLabel facet that sibling models apply to display names and definitions under this model's namespace.
- imports: iso-639-15924 (REFERENCE): language and script code sets carried as scheme references.
- imports: tbx (ALIGN): termbase structure of concept, term and usage.
- imports: bcp-47 (ALIGN): locale tag composition rules.

## Stewardship

The neutral owner archetype is a knowledge steward at class level for reference data (languages, scripts, locales), while glossary and translation records belong to their authors and commissioning organizations. Access is always granted by the respective owner through the catalogue's S1/S2 ownership and access models, with exports audited via S4.
