# EM-KNW-01 local synthesis

## Disposition

- Create an **Enterprise document, knowledge and terminology profile** over WM-REC-001, WM-KNW-006 and WM-KNW-018.
- Do not create a new catalogue or runtime identifier.
- Treat Knowledge Article as a document/record designation and Term Definition as concept-owned descriptive content, not independent aggregate roots.
- Route independently identified assertions and decisions to EM-KNW-02 rather than expanding this contour.

## Aggregate boundaries

WM-REC-001 owns the stable record identity, immutable version chain, instantiations, custody, evidence and disposition. A URL, file or carrier is a location or instantiation, never the record identity. Document Revision remains owned by the record because retention, holds, supersession and last-copy rules span the full aggregate.

WM-KNW-006 owns a concept's persistent identity and intrinsic meaning: delimitation, characteristics, definitions with sources, designations with language/script/context, global deprecation, merge/split and successor continuity. A concept remains valid and citable outside any scheme.

WM-KNW-018 owns scheme identity, namespace, immutable releases and every release-scoped assertion: membership, top concept, in-scheme relations, facets, collections and mappings. It references pinned concept versions; it does not become a second master for intrinsic concept content.

## Ownership rule

If an assertion loses its meaning when the scheme release is removed, the scheme masters it. If it survives removal from every scheme, the concept masters it. Every assertion has one editable master; concept-side membership/relation views are derived and read-only.

Concept retirement and scheme-local withdrawal are different operations. Retirement preserves the globally resolvable concept identifier and successor guidance. Withdrawal removes a concept from a scheme release without deprecating it elsewhere.

## Required profile constraints

1. A document classification binding pins concept IRI and exact scheme release; a label alone cannot classify a record.
2. A new URL or storage system creates a new location/instantiation reference and, only after a fixing event, possibly a new version. It does not create new knowledge identity.
3. Content digest proves byte state, not document or concept identity.
4. Concept equality requires an authorised identity/mapping assertion with basis and context. Lexical equality never establishes same-as.
5. Definitions retain source, provenance, language, subject field, jurisdiction/audience context, status and dispute state. Disputed does not mean deprecated.
6. Scheme-less concepts are allowed; release binding must therefore be optional or point to a concept-register release rather than an unrelated scheme release.
7. Published record versions and scheme releases are append-only and never renumbered.

## Acceptance result

A migrated document keeps its record identifier and complete version sequence. The target system ID becomes an alternate identifier with assertion provenance; format conversion is a derived instantiation with its own digest and event. Existing signatures remain bound to their original bytes.

Two identical words in distinct subject fields remain two concepts. Two competing definitions may remain on one concept only when their intension is the same and each definition retains its authority and context; otherwise they identify distinct concepts. No silent merge or preferred winner is inferred.

## Holds

All three bases are reviewable drafts with `publishableCanonical: false`. WM-KNW-006 and WM-KNW-018 have independent-review waivers; WM-REC-001 retains source/version and cross-profile holds. WM-KNW-006 and WM-KNW-018 currently overlap in ownership text, their registry relationship is unresolved, and definition-level access/dispute semantics need amendment. This checkpoint is research evidence, not an installable release.
