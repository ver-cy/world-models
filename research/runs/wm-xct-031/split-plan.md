# WM-XCT-031 bounded Claude research plan

WM-XCT-031 is a format-neutral mixin for declaring language, locale,
translation and terminology bindings. It is researched through three bounded,
non-overlapping passes after the monolithic provider run proved operationally
too large.

1. `locale` owns language/locale/script identifiers, canonicalization,
   matching, negotiation, directionality and locale-sensitive conventions.
2. `translation` owns translatable-unit identity, variants, fallback,
   terminology bindings, placeholders, plural/select semantics and quality.
3. `governance` owns authority, lifecycle, provenance, validation, access,
   retention, interoperability and canonical service rules.

Every pass must be independently schema-valid and use its assigned local-ID
prefix. The deterministic merger remaps sources, unions structure, keeps the
complete boundary from `locale`, keeps service layers from `governance` and
validates the merged result. The later no-tools adjudication must verify that
the result remains a host-scoped mixin and does not become a content store,
translation-management system, terminology registry or user-preference model.
