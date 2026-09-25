# Independent review request: EM-KNW-01 Document, knowledge and terminology

Review this Enterprise metamodel boundary independently. Use public standards and mature DMS, records, terminology and taxonomy practice where useful. Distinguish source facts from design inference. Do not invent a Vercy catalogue/runtime identifier.

Current Vercy candidates:

- WM-REC-001 Document / Record: stable record identity, immutable versions, instantiations, evidence, custody, retention and disposition. File, URL and carrier are not record identity.
- WM-KNW-006 Concept / Term: persistent concept identity, delimitation, definitions, designations, language/context and concept lifecycle.
- WM-KNW-018 Taxonomy / Classification Scheme: scheme identity, immutable releases, concepts, relations, mappings and release governance.
- All three are published research specifications but remain reviewable drafts with publication holds.

Proposed decision: **PROFILE**, no new model ID. Knowledge Article is a document/record designation. Document Revision is owned by the record. Term Definition is concept-owned descriptive content. Independently identified assertions and decisions are deferred to another contour.

Proposed single-master rule:

> If an assertion loses its meaning when a scheme release is removed, the scheme masters it. If it survives removal from every scheme, the concept masters it.

Thus WM-KNW-006 masters intrinsic concept identity, delimitation, definitions, designations and global lifecycle. WM-KNW-018 masters releases and release-scoped membership, top-concept, hierarchy, collection, facet and mapping assertions. Concept-side membership/relation views are derived and read-only. Concept retirement differs from scheme-local withdrawal.

Test:

1. A page receives a new URL or moves between systems. Determine whether record identity, version identity or only instantiation/location changes.
2. Two concepts have the same preferred label in different subject fields.
3. One word has two conflicting definitions from different authorities or contexts.
4. A document is classified: require a binding to concept IRI plus exact scheme release, not a copied label.
5. A concept exists outside any scheme, then later enters and leaves a taxonomy release.

Check these invariants: digest is evidence of byte state, not identity; lexical equality never proves same-as; every definition has source/language/context/status; published versions/releases are append-only; identifiers remain resolvable after deprecation; one assertion has one editable master.

Return at most 1000 words with: Verdict (REUSE ONLY / PROFILE / NEW MODEL); aggregate boundaries; correction to the WM-KNW-006/018 ownership overlap; required constraints; scenario results; gaps and publication blockers. State whether Knowledge Article, Document Revision or Term Definition needs a separate aggregate and why.
