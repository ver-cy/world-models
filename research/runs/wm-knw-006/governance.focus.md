Research only lifecycle, evidence, governance and quality structure for
WM-KNW-006 Concept / Term.

- Use the exact registry identity and output `entry_kind` `entity`. Keep the
  stable concept identity separate from mutable terms, definitions and mapping
  assertions.
- Cover proposal/review/approval/publication/deprecation/retirement; version and
  change history; provenance and authoritative sources; evidence and rationale;
  validation/conformance; duplicate detection and merge/split/redirect rules;
  editorial quality and status; ownership/stewardship/decision authority;
  access, embargo, licensing and retention; auditability and event/effective
  timestamps; namespace and identifier stewardship.
- This pass exclusively owns the merged `service_layers`. Make dimension,
  canon/patch compatibility, artifact identity, RFC 3339 timestamps with
  seconds and offset, serial naming, policies, CRUD, roles, access scopes and
  AGENTS.md bootstrap rules concrete for this model.
- Every `service_layers` rule must apply to the final combined WM-KNW-006, not
  merely this governance split. Namespace guidance must explicitly support the
  three stable local-ID zones `ct-core-`, `ct-rel-` and `ct-gov-`. Canonical,
  patch and compatibility rules must cover lexical/designation content,
  language-tagged values, scheme relations/mappings and governance content;
  do not defer any of those surfaces to an "adjacent pass".
- Reconcile `serial_naming_rule` with this complete artifact inventory from the
  other already validated split results:
  - serial, designation-scoped: `ct-core-usage-attestation`;
  - serial, scheme-pair and bound-release-scoped: `ct-rel-art-mapping-set`;
  - serial, export-closure-scoped: `ct-rel-art-interchange-package`;
  - non-serial, bridge-model-scoped: `ct-rel-art-crosswalk-specification`;
  - serial, concept-scoped: `ct-gov-artifact-deprecation-notice`,
    `ct-gov-artifact-change-record`, `ct-gov-artifact-decision-record` and
    `ct-gov-artifact-validation-report`.
  The naming rule must enumerate every serial kind, use the correct scope
  discriminator plus a never-reused sequence, and prohibit dates/timestamps as
  identity. It must not pretend mapping sets or export packages are scoped only
  by a concept. Non-serial artifacts retain their declared external or content
  identity strategy.
- Add an explicit access exception for `ct-core-usage-attestation`: screenshots,
  corpus excerpts and appellations may identify a living person or contain
  third-party/private material, so publication requires a privacy and rights
  review, minimisation/redaction where applicable, and a restricted reference
  when the underlying evidence cannot be disclosed. Do not claim a universal
  legal determination; keep the jurisdiction-specific privacy gap visible.
- Make `integrity_rule` re-derivable for every declared media form. Structured
  artifacts use the versioned canonical semantic form. Digital audio, raster,
  vector, video and screenshot renditions use the exact retained byte stream
  plus declared media type and byte length; any transcoding creates a new
  rendition with its own digest. A physical specimen is never hashed directly:
  only its holding-system record and retained digital rendition are hashed.
  Record the named digest algorithm, canonicalisation or byte-stream mode and
  version. Do not promise a third party can recompute a restricted digest
  without authorized access to the canonical payload.
- Do not repeat detailed lexical core or semantic relation/mapping structures.
  Boundary notes may cite them.
- Target 2-3 bundles, 4-7 layers and 9-13 findings with 3-5 questions each.
- Every local ID, including bundle, layer, finding, question, data element,
  artifact and function IDs, must begin with `ct-gov-`.
- Use at least eight distinct question kinds across the pass. Limit functions
  to governance, validation, lifecycle and audit operations.
- Prefer primary standards/specifications for provenance, vocabulary status,
  versioning, data quality and persistent identifiers. Separate normative
  requirements from local Vercy policy and expose unresolved choices.
