TEXT TRANSPORT PART 2/6. Acknowledge this part only. Do not audit yet; wait for all parts.
PART CONTENT
le>
# Native V3 binding

The original companion uses `vr.profile.enterprise-disclosure-review`; it does not inherit an access or classification model. Each ContextPackageProposal owns a native object of type `vr.profile.enterprise-disclosure-review:proposal`; each JointDisclosureReview owns a separate `:review` object. Native object ID equals the qualified record identity. Members/fields remain embedded in each proposal revision.

Paths `disclosure.proposal.revision` and `disclosure.review.revision` carry one complete immutable record per fact. Use `native_fact_id()` for a storage ID derived from Dimension/id/revision. A different digest for the same identity/revision conflicts at immutable import; do not create a second storage key to conceal it. Native envelopes have unit null, asserted status, empty supersedes, no validTo, accessClass restricted and validity starting at the actual native storage receipt. Storage authority rank 0 identifies the trusted registrar, never the reviewer or permission to disclose.

All revisions coexist. Review supersession is the record's own exact `body.supersedes` link; the complete current active set comes from an independent host snapshot. Generic native fact resolution may therefore show peers/contested results: it is not the active-review selector. Fetch the complete authorized register, not only a generic “latest” resolved fact. Current read permission applies to every historical record.

Required sequence: authenticate and authorize through the host; validate the native object/fact envelopes with the pinned V3 runtime; call `validate_native(fact, object, dimension=..., capability=..., now=..., master=..., writer=...)`; call `import_records()` with the complete bounded register to enforce internal links, identity-type and immutable history; call `inspect()` with a separately resolved current snapshot. No API is a substitute for the others. V3 does not automatically invoke these companion functions.

The native companion enforces object identity/type, Dimension, exact path, deterministic revision key, local record schema/digest, restricted class, storage master/writer/digest receipt, and ordered native object/record/evaluation times. It relies on separate native envelope validation for the complete outer schema and native object revision graph. It does not authenticate the input dictionaries, check a database transaction or enforce a recipient channel. Host clock skew and recovery affect every now/asOf-taking operation; do not silently rewrite receipt times.

`acceptance.py` pins the toolchain, creates three temporary synthetic new Dimensions, installs exact specification/code/schema bytes, stores two independent objects and three immutable revision facts, imports and replays the installed companion, constructs distinct time-indexed synthetic snapshots for an earlier assessment (10:01:30 UTC) and later correction (12:00:00 UTC). It exercises 22 negative native cases per profile and demonstrates that an invalid nested verdict can pass the outer native schema while the companion rejects it. Both snapshots are constructed fixtures, separate from the installation receipt; they are not preserved real history or present serving authority.

No production source resolver, current-grant evaluator, persistent store/CAS, removal/retention operation, automatic dispatch or existing-Dimension adapter is supplied. Parent semantic comparisons are optional reading only and require no runtime installation.

Native object envelopes must remain `active` for this binding to validate their history. Review retirement/withdrawal is represented in the host snapshot, not by retiring its native storage object. At-rest append-only storage and CAS are host duties: outer V3 validation does not detect an in-place replacement, and the pure companion merge compares only the supplied register. Protect earlier digest/snapshot anchors independently.

</file>
END FILE bindings/native-v3.md

## FILE boundary-decision.md
ORIGINAL SHA256 65f8ca55641832da69e233872e248eee2246a9ce146a6efdc192ee3eeffc67a7
<file>
# Boundary decision and alternatives

An original companion is narrower than the whole EM-XCT-05 contour. It exports exactly two independent record types: ContextPackageProposal and JointDisclosureReview. A proposal has its own durable identity and immutable revisions; a review has a separate owner, identity, correction chain and finite validity. Members, fields and pins are embedded values, not separately mastered objects. The result of inspect() is an ephemeral diagnostic, not a grant or a third persistent business type.

One member refers to one source object. A package may combine different objects and multiple projections of the same object. A source aggregate must have its own domain identity, calculation and disclosure owner before appearing as a source pin. The review assesses the package; it does not calculate that aggregate.

The independent studies proposed richer manifests, policy and retention objects. Those are deliberately not duplicated here. Classification scheme/term semantics remain behind exact binding references. Source schema and projection shape are opaque pins. IAM, source resolution, retention floors, disposal deadlines and holds are separate owned contracts; no executable delegation is invented to WM-XCT-035 or WM-XCT-038. Current custody context is bound, but no disposition state is calculated.

Alternative: one combined permission/retention Boolean would lose attribution, conflicting verdicts and separate time axes. Alternative: copying every source object would create another master and increase disclosure. Alternative: treating every embedded field as a standalone object imposes needless lifecycle without an independent owner. Exact bounded immutable metadata plus an attributed review is the minimum chosen design, not a universal enterprise privacy ontology.

The instance graph (proposal/review/source links), specification graph (semantic comparison only) and delivery graph (code/schema/docs/tests) remain distinct. Supersession must be acyclic; source business links may be cyclic outside this boundary. No mandatory runtime domain imports exist.

</file>
END FILE boundary-decision.md

## FILE composition.yaml
ORIGINAL SHA256 7a509c5dfb46cdea05fbfd51d52629b49a5ada99d9d928954a06ce7cea30f74d
<file>
{"runtimeImports":[],"semanticReferences":[{"id":"WM-XCT-002","version":"0.3.0-research.1","specDigest":"sha256:9085d977567f3e1fc0b9bb27c6a7c517139f5972a1b95bf4a2bedccdb10bf2db","relation":"boundary-reference-no-findings-selected"},{"id":"WM-XCT-003","version":"0.3.0-research.1","specDigest":"sha256:058191fe49bd1a52d52669211893d91971511f33a2aad1f15407e409d2553edb","relation":"selected-semantic-overlap-not-subtype"},{"id":"WM-XCT-020","version":"0.3.0-research.1","specDigest":"sha256:47aa90ca48b7e367f61c30e454fd7859ba2dc7e2b998bbd4541acb6eda81b9bd","relation":"selected-semantic-overlap-not-subtype"},{"id":"WM-DAT-004","version":"0.3.0-research.1","specDigest":"sha256:0c6fc7db12c33efe0d9283b5830b4c679935dd5b640417e7e315a564b4971c94","relation":"selected-semantic-overlap-not-subtype"},{"id":"WM-KNW-012","version":"0.3.0-research.1","specDigest":"sha256:b7a880e4e07b26f8962e8d3b5b23b33c1062abcb83303ff8f0e8b5a3134e61b8","relation":"selected-semantic-overlap-not-subtype"}],"delivery":"Original reference, closed schema, synthetic fixtures, contract and native binding; external pins are not executable imports."}
</file>
END FILE composition.yaml

## FILE crosswalk.json
ORIGINAL SHA256 07964eec4ae8e74253b86c0d97f0ff5c1c2d92f1e206efca88cdeb3d92d1adf4
<file>
{"checkedAt":"2026-09-21T20:48:36.824433+00:00","mode":"Codex comparison and disposition; not provider output","rows":[{"candidate":"DisclosurePolicy / permission","currentId":"vr.wm-xct-002","catalogueId":"WM-XCT-002","version":"0.3.0-research.1","status":"published","installable":true,"researchAssurance":"reviewable-draft","specUrl":"https://ver.cy/models/wm-xct-002-access-contract-consent/spec.yaml","specDigest":"sha256:9085d977567f3e1fc0b9bb27c6a7c517139f5972a1b95bf4a2bedccdb10bf2db","relation":"boundary-reference-no-findings-selected","decision":"Reference permission evidence only; current grant evaluation belongs to the host.","runtimeImport":false,"typeConformanceVerified":false,"losses":"No adapter claims to preserve all parent fields or rules. Opaque pins require an independent host resolver. All original holds remain.","fullSpecificationBytesCompared":true,"semanticReading":"Complete spec parsed and finding inventory inspected; boundary-only reference, no finding selected. Full parent citation ratification and runtime implementation validation are not claimed.","findingInventory":["grantor-authority-basis","grantee-designation","party-functional-roles","scope-clause-selection","data-category-sensitivity","purpose-specification","permitted-action-read-semantics","constraints-validity-window","obligations-and-duties","consent-validity-elements","consent-capture-context","consent-record-and-proof","receipt-and-portability","contract-state-model","temporal-semantics","amendment-versioning-reconsent","revocation-and-withdrawal","propagation-and-erasure","entitlement-cutoff","coverage-decision-exchange","fail-closed-handling","multi-grant-conflict","record-provenance-integrity","instrument-identity","retention-of-records","access-to-contract-record","standards-alignment-map","jurisdictional-parameters","instrument-flavour-classification"],"selectedFindingIds":[],"publicationHolds":["Source liveness and version pinning is unverified for all nineteen accepted sources. Two specific reconciliations are mandatory before publication: pin FHIR Consent to the version-qualified R5 URL rather than the unversioned current URL that will drift, and reconcile the two DPVCG 27560-guide citations that disagree on both host and date (w3c-cg.github.io retrieved 2026-08-23 versus w3id.org Final Community Group Report 15 February 2026).","Domain-profile validation is incomplete. The model has been exercised only against EU/GDPR, the US health sector under 45 CFR 164.508, and a healthcare FHIR profile. At least one non-health, non-EU jurisdiction profile must be run end to end before publication to test whether the instrument-form and flavour parameters actually generalise.","Normative text for ISO/IEC TS 27560:2023 and ISO/IEC 29184:2020 is paywalled; field inventories rest on catalogue pages plus the DPVCG mapping rather than annex text. TS 27560 is a Technical Specification, not an International Standard, and a revision (CD 27560.2) may change mandatory fields. Any field-level claim must be labelled as mapping-derived.","The security dimension is self-declared a gap by the base (key management, token binding, replay resistance, cryptographic proof suites). Now that entitlement cutoff is imported, publication must name the sibling security model that owns these and state plainly that this model does not close them.","Collective, community and Indigenous group permission is unsupported by any source in either pack and must be published as an explicitly unmodelled gap, never approximated through the delegate capacity."]},{"candidate":"DisclosurePolicy / shape","currentId":"vr.wm-xct-003","catalogueId":"WM-XCT-003","version":"0.3.0-research.1","status":"published","installable":true,"researchAssurance":"reviewable-draft","specUrl":"https://ver.cy/models/wm-xct-003-projection-disclosure-policy/spec.yaml","specDigest":"sha256:058191fe49bd1a52d52669211893d91971511f33a2aad1f15407e409d2553edb","relation":"overlap","decision":"Reference the exact shape record; no subtype or runtime transformation claim.","runtimeImport":false,"typeConformanceVerified":false,"losses":"No adapter claims to preserve all parent fields or rules. Opaque pins require an independent host resolver. All original holds remain.","fullSpecificationBytesCompared":true,"semanticReading":"Complete spec parsed and whole finding inventory inspected; boundary, exclusions, holds and selected exact findings/fields read. Full parent citation ratification and runtime implementation validation are not claimed.","findingInventory":["selection-scope-and-defaults","path-expression-and-addressing","graph-extent-and-nested-shape","treatment-technique-and-parameters","reversibility-and-recoding","population-and-record-scope","aggregation-grain-declaration","leaving-shape-grain-class","shape-narrowing-and-combination","compiled-template-and-fingerprint","source-schema-binding-and-drift","encoding-and-media-profile","residual-disclosure-and-side-channels","binding-target-and-audience","applicability-conditions","class-to-treatment-matrix","regime-mandated-shapes","element-identifiability-roles","assurance-method-and-evidence","release-set-linkability","policy-expression-crosswalk","selective-disclosure-protocol-fit","self-applied-policy-projection","disclosure-change-classification","served-output-reproducibility","shape-invalidation-signals"],"selectedFindingIds":["selection-scope-and-defaults","graph-extent-and-nested-shape","source-schema-binding-and-drift","residual-disclosure-and-side-channels","binding-target-and-audience","class-to-treatment-matrix","release-set-linkability","shape-invalidation-signals"],"publicationHolds":["Source verification hold: re-check live URLs, version pins and current status for all 14 base sources and the Grok sources backing the accepted additions before publication. ISO/IEC 20889 and 27559 are paywalled and were not read in full, the JSON Schema 2020-12 core document is an expired Internet-Draft, DPV 2.1 is Community Group output, and the XACML Multiple Decision Profile is a committee draft; each must be re-tiered or replaced if it has moved.","Multi-profile validation hold: the merged structure has not been exercised against one instance per accepted grain class (record-level subset, named summary, aggregate-only) nor against a non-JSON medium such as a tabular extract, an RDF graph or free text. Until that is done, the selection and graph-extent findings are asserted to generalise, not shown to.","Jurisdictional profile hold: only US federal and EEA sources were gathered. Regime-mandated-shapes, the identifiability roles and the assurance-method claims must be published as US/EEA-evidenced only, with no implied applicability to APPI, LGPD, DPDP, PIPL or UK DPA regimes.","Ownership gap hold: record-level expert-determination evidence has no named owning model. WM-XCT-005 is scoped to cohort floors and aggregation assurance, so a non-aggregate shape's assurance evidence currently has no home; publish only with this stated as unresolved or after an owner is assigned.","Cross-model retention hold: legal-hold precedence across WM-XCT-004 audit-entry disposition, WM-DAT-004 and Dimension source-data erasure, and WM-KNW-012 destruction of the policy record is unrecorded, so a hold in one owner may strand a tombstone in another. Publish only with the missing precedence explicit."]},{"candidate":"ClassificationAssignment","currentId":"vr.wm-xct-020","catalogueId":"WM-XCT-020","version":"0.3.0-research.1","status":"published","installable":true,"researchAssurance":"reviewable-draft","specUrl":"https://ver.cy/models/wm-xct-020-classification-binding/spec.yaml","specDigest":"sha256:47aa90ca48b7e367f61c30e454fd7859ba2dc7e2b998bbd4541acb6eda81b9bd","relation":"overlap","decision":"Reference exact binding records; no scheme authoring, classification judgment or access grant.","runtimeImport":false,"typeConformanceVerified":false,"losses":"No adapter claims to preserve all parent fields or rules. Opaque pins require an independent host resolver. All original holds remain.","fullSpecificationBytesCompared":true,"semanticReading":"Complete spec parsed and whole finding inventory inspected; boundary, exclusions, holds and selected exact findings/fields read. Full parent citation ratification and runtime implementation validation are not claimed.","findingInventory":["binding-as-reified-assertion","classification-vs-typing-boundary","subject-and-scope-of-application","binding-identifier-and-keys","scheme-and-term-reference-identity","lexical-form-and-language","binding-slot-declaration","permitted-value-space","value-set-slot-binding-reference","binding-strength","multiplicity-and-completeness","asserted-term-and-role","origin-of-binding-assertion","classification-facet-axis","residual-and-unclassifiable-handling","uncoded-text-fallback","assignment-actor-and-method","evidence-and-justification","assignment-authority-and-legal-effect","scheme-custodianship-and-jurisdiction","confidence-and-uncertainty","coding-quality-measurement","temporal-frames-of-a-binding","scheme-version-drift-and-migration","binding-lifecycle-states","supersession-correction-and-dispute","binding-validation-rules","conflict-and-consistency-detection","mapping-derived-bindings","exchange-projection-and-round-trip","parallel-codings-and-translation-set","sensitive-binding-access-and-erasure"],"selectedFindingIds":["binding-as-reified-assertion","scheme-and-term-reference-identity","multiplicity-and-completeness","assignment-authority-and-legal-effect","temporal-frames-of-a-binding","supersession-correction-and-dispute","sensitive-binding-access-and-erasure"],"publicationHolds":["Source verification hold: every accepted source URL must be re-fetched live and version-pinned before publication, including canonicalising the two FHIR R5 URL variants (hl7.org/fhir/terminologies.html versus hl7.org/FHIR/terminologies.html; datatypes.html versus R5/datatypes.html) and adopting the dated DCMI 2020-01-20 URL over the undated latest URL.","Paywalled ISO normative text hold: ISO/IEC TR 11179-2:2019, ISO/IEC 11179-1:2023 and its Part 3 classification package, and ISO 25964-1/-2 were cited from catalogue abstracts, Part 1 terms or NISO-hosted material. Clause-level obligations are unverified and no conformance-sounding claim may be published against them.","Unparsed primary-source hold: the UNSD Best Practice Guidelines PDF and the SDMX Section 2 Information Model PDF could not be machine-parsed in the base run; exhaustiveness, mutual-exclusivity and SDMX hierarchy claims must be re-verified against parsed text before publication.","Multi-profile validation hold: the pattern is validated against health terminology, EU customs rulings, EU statistics and cataloguing profiles only. At least one non-EU legal ruling regime and one commercial product-taxonomy or multi-label machine-learning profile must be run before any general-applicability claim.","Sibling dependency hold: the Classification Scheme, Value Set and Mapping/Correspondence models are unregistered, so REFERENCE composition links point at non-existent registry entries. The entry may publish as a research draft but not as production-ready.","Evidence-gap disclosure hold: confidence semantics, calibration and acceptance thresholds must be published as an explicit declared gap with a non-comparability warning, never as canonical structure.","XKOS citation hold: one provider reported a 404 on a W3C-hosted XKOS URL while the base cites the DDI Alliance URL; the surviving citation must be confirmed live and its revision date pinned."]},{"candidate":"ProjectionContract / source schema","currentId":"vr.wm-dat-004","catalogueId":"WM-DAT-004","version":"0.3.0-research.1","status":"published","installable":true,"researchAssurance":"reviewable-draft","specUrl":"https://ver.cy/models/wm-dat-004-data-schema-data-contract/spec.yaml","specDigest":"sha256:0c6fc7db12c33efe0d9283b5830b4c679935dd5b640417e7e315a564b4971c94","relation":"overlap","decision":"Reference exact source schema; no copied generic schema model or instance compiler.","runtimeImport":false,"typeConformanceVerified":false,"losses":"No adapter claims to preserve all parent fields or rules. Opaque pins require an independent host resolver. All original holds remain.","fullSpecificationBytesCompared":true,"semanticReading":"Complete spec parsed and whole finding inventory inspected; boundary, exclusions, holds and selected exact findings/fields read. Full parent citation ratification and runtime implementation validation are not claimed.","findingInventory":["f-contract-identifier","f-governed-subject","f-dialect-and-vocabulary","f-version-designation","f-contract-status","f-ownership-stewardship","f-object-property-structure","f-keys-and-relationships","f-composition-references-and-shape-targets","f-logical-physical-types","f-encoding-temporal-conventions","f-term-value-domain-binding","f-structural-value-constraints","f-cross-field-constraints","f-quality-rule-declaration","f-validation-outcome-report","f-compatibility-mode","f-schema-resolution-defaults","f-canonical-form-and-fingerprint","f-change-approval-process","f-deprecation-and-sunset","f-producer-consumer-parties","f-obligations-acceptance","f-declared-access-roles","f-service-levels-support","f-classification-privacy-terms","f-server-serialization-binding","f-contract-provenance","f-registry-publication","f-standard-alignment-mapping","f-profile-jurisdictional-conformance"],"selectedFindingIds":["f-dialect-and-vocabulary","f-object-property-structure","f-composition-references-and-shape-targets","f-canonical-form-and-fingerprint","f-classification-privacy-terms"],"publicationHolds":["Live-URL and version-pin verification for the full merged source register is outstanding. Claude's three ODCS citations use 'latest' URLs annotated v3.1.0 while Grok cites the immutable v3.1.0 path; all ODCS references must be repinned to the versioned URL and refetched before publication, and the newly introduced OpenAPI 3.1.1 and ISO/IEC 11179-31:2023 entries must be fetch-verified and tier-assigned.","Direct contradiction about ODCS v3.1.0 field status: Claude's f-governed-subject describes the governed subject as expressed through domain, dataProduct and tenant, while Grok states v3.1.0 deprecated the dataProduct field. This does not block a research draft, but f-governed-subject must not be published naming dataProduct as a live binding mechanism until the v3.1.0 text is reread.","ISO/IEC 11179-3:2023 and 11179-31:2023 were verified only at catalogue-record level because the full texts are paywalled. Every 11179-derived construct (administered item, data element concept, conceptual domain, value domain, registration authority, registration status) must be published as an alignment hypothesis with no clause-level conformance claim.","Domain-profile validation is incomplete. The model has been exercised against a generic enterprise profile and the European public-sector profile (DCAT-AP 3.0.0) only. It must be run against at least one regulated sector profile - clinical, financial reporting or geospatial - before any multi-profile coverage claim, since such regimes may mandate elements this model treats as optional.","The spatial and data-residency dimension is a declared gap in both providers. Publication must state the gap explicitly and must not present server and environment binding as satisfying residency coverage.","The accepted f-declared-access-roles finding must be reviewed at publication to confirm it reads as declaration only. If it drifts into entitlement grants, authentication or key management it breaches the base out-of-scope statement and must be cut back rather than published."]},{"candidate":"DisclosurePolicy / governed policy","currentId":"vr.wm-knw-012","catalogueId":"WM-KNW-012","version":"0.3.0-research.1","status":"published","installable":true,"researchAssurance":"reviewable-draft","specUrl":"https://ver.cy/models/wm-knw-012-policy-rule/spec.yaml","specDigest":"sha256:b7a880e4e07b26f8962e8d3b5b23b33c1062abcb83303ff8f0e8b5a3134e61b8","relation":"overlap","decision":"Reference governed policy/authority context; no execution or combining language.","runtimeImport":false,"typeConformanceVerified":false,"losses":"No adapter claims to preserve all parent fields or rules. Opaque pins require an independent host resolver. All original holds remain.","fullSpecificationBytesCompared":true,"semanticReading":"Complete spec parsed and whole finding inventory inspected; boundary, exclusions, holds and selected exact findings/fields read. Full parent citation ratification and runtime implementation validation are not claimed.","findingInventory":["statement-identifier-and-naming","version-identity-and-point-in-time","deontic-modality-force-and-defeasibility","instrument-genre-and-binding-form","issuing-authority-and-mandate","ownership-stewardship-and-roles","jurisdiction-and-territorial-scope","subject-target-action-and-context-scope","rule-slot-inventory-and-atomicity","policy-set-containment-and-inheritance","constraint-expression-binding","parameterization-and-tailoring-values","defined-terms-and-vocabulary-binding","combining-and-hit-policy-declaration","override-and-superiority-relations","derogation-and-waiver-declaration","declared-conflicts-and-alternatives","policy-lifecycle-state-model","amendment-supersession-and-repeal","validity-intervals-and-record-time","authoring-derivation-and-source-mapping","statement-quality-and-review-status","conformance-and-standard-alignment","record-classification-access-and-retention"],"selectedFindingIds":["version-identity-and-point-in-time","issuing-authority-and-mandate","constraint-expression-binding","combining-and-hit-policy-declaration","validity-intervals-and-record-time","record-classification-access-and-retention"],"publicationHolds":["Live source and version verification hold: before publication, confirm every accepted source URL resolves and pin a version for the three access-dated entries that currently carry no version token — SRC-010 (OSCAL catalog concepts), SRC-011 (ELI framework pages) and SRC-012 (ODRL Formal Semantics editor's draft, non-normative). Any source that cannot be resolved and pinned must be downgraded and the nodes resting on it re-checked for remaining primary support.","Single-provider hold: every publication artifact must carry a visible notice that this result was produced by Claude alone and received no independent second-provider review, naming the repository owner's waiver of Grok effective 2026-08-29T09:06:27Z and its stated reason (repeated structured-output failures). The artifact stays a reviewable draft, not a validated model, for as long as that waiver stands.","Timestamp-rule verification hold: SRC-009 is registered as RFC 3339 'updated by RFC 9557', but RFC 9557 is not itself a registered source while the canonicalization and artifact timestamp rules depend on the exact unknown-local-offset clause. Either register the updating RFC and confirm the -00:00 convention survives it, or restate the rule against the pinned RFC 3339 text before freezing the hashing rule.","Boundary-review hold: the frozen registry carries status 'candidate' and review_state 'boundary-review-required', and this audit reclassifies the subject-model entry kind from entity to aggregate on the strength of the service-layer invariants. Publication must surface both the outstanding boundary review and the reclassification, so no downstream consumer treats the entry kind as settled.","Paywalled-source hold: SRC-013 (ISO 37301:2021) grounds lifecycle currency, ownership and compliance-boundary claims but is behind a paywall. Confirm that the cited structure is supported by publicly verifiable scope material or by a licensed reading on record; if neither, downgrade the affected notes to partial support rather than leaving an uncheckable tier-1 citation in a public draft.","Independent second-provider review was explicitly waived by the repository owner; this Claude-only result remains a reviewable draft."]},{"candidate":"RetentionConstraint","currentId":"vr.wm-xct-035","catalogueId":"WM-XCT-035","version":null,"status":"todo","installable":false,"specDigest":null,"relation":"research-target","decision":"Documented deferral; custodyContext is an opaque host-owned evidence pin, not an executable 035 dependency.","runtimeImport":false,"losses":"No retention schedule/hold evaluator, disposition execution or destruction evidence implemented."}],"composition":{"runtimeImports":[],"semanticReferences":[{"id":"WM-XCT-002","version":"0.3.0-research.1","specDigest":"sha256:9085d977567f3e1fc0b9bb27c6a7c517139f5972a1b95bf4a2bedccdb10bf2db","relation":"boundary-reference-no-findings-selected"},{"id":"WM-XCT-003","version":"0.3.0-research.1","specDigest":"sha256:058191fe49bd1a52d52669211893d91971511f33a2aad1f15407e409d2553edb","relation":"selected-semantic-overlap-not-subtype"},{"id":"WM-XCT-020","version":"0.3.0-research.1","specDigest":"sha256:47aa90ca48b7e367f61c30e454fd7859ba2dc7e2b998bbd4541acb6eda81b9bd","relation":"selected-semantic-overlap-not-subtype"},{"id":"WM-DAT-004","version":"0.3.0-research.1","specDigest":"sha256:0c6fc7db12c33efe0d9283b5830b4c679935dd5b640417e7e315a564b4971c94","relation":"selected-semantic-overlap-not-subtype"},{"id":"WM-KNW-012","version":"0.3.0-research.1","specDigest":"sha256:b7a880e4e07b26f8962e8d3b5b23b33c1062abcb83303ff8f0e8b5a3134e61b8","relation":"selected-semantic-overlap-not-subtype"}],"packageContents":"Original metadata-only reference; parent comparison is semantic evidence, not imported types.","deferredTargets":["WM-XCT-035"]},"otherNeighbors":"005 is a legacy non-installable entry; 038 is an unversioned todo. No executable delegation. See adjacent-model-checks.json."}
</file>
END FILE crosswalk.json

## FILE disclosure.py
ORIGINAL SHA256 c2371aac6c1adfbdd694e7280b2140cae6cd6649aabe3c738e6bd3f925979b17
<file>
"""Metadata-only reviewable reference. All callers/snapshots require a trusted host.

No network, payload access, grant evaluation, inference proof or deletion occurs.
Bounded reviewable reference; see review.md for the exact external audit scope.
"""
from pathlib import Path
import copy, datetime, hashlib, json, re
from jsonschema import Draft202012Validator

VERSION='0.1.0'
SCHEMA=json.loads(Path(__file__).with_name('disclosure.schema.json').read_text(encoding='utf-8'))
if not all(SCHEMA['$defs'][t]['properties']['version']['const']==VERSION for t in ('proposal','review','snapshot')):
    raise RuntimeError('schema/version mismatch')
VALIDATOR=Draft202012Validator(SCHEMA)
MAX_BYTES=262144
class Invalid(ValueError):pass
class Unauthorized(ValueError):pass

def canonical(value):
    """Restricted JSON: sorted keys, UTF-8, compact, no floats or normalization.

    List order is significant. Strings preserve code points. This is NOT JCS.
    Bounds are prototype limits, not a hardened hostile-input parser guarantee.
    """
    def visit(x,depth=0):
        if depth>20:raise Invalid('depth')
        if type(x) is str:
            if len(x)>4096 or any(0xD800<=ord(c)<=0xDFFF for c in x):raise Invalid('string')
        elif x is None or type(x) is bool:pass
        elif type(x) is int:
            if not -(2**53-1)<=x<=2**53-1:raise Invalid('integer')
        elif type(x) is list:
            if len(x)>128:raise Invalid('list')
            for a in x:visit(a,depth+1)
        elif type(x) is dict:
            if len(x)>128:raise Invalid('object')
            for k,v in x.items():
                if type(k) is not str:raise Invalid('key')
                visit(k,depth+1);visit(v,depth+1)
        else:raise Invalid('unsupported JSON value')
    visit(value)
    raw=json.dumps(value,ensure_ascii=False,sort_keys=True,separators=(',',':'),allow_nan=False).encode('utf-8')
    if len(raw)>MAX_BYTES:raise Invalid('size')
    return raw

def load(raw):
    if not isinstance(raw,bytes) or len(raw)>MAX_BYTES:raise Invalid('input bytes')
    def pairs(items):
        d={}
        for k,v in items:
            if k in d:raise Invalid('duplicate JSON key')
            d[k]=v
        return d
    def forbidden(_):raise Invalid('non-integer number')
    def integer(s):
        if len(s)>17:raise Invalid('integer')
        return int(s)
    try:
        result=json.loads(raw.decode('utf-8'),object_pairs_hook=pairs,parse_float=forbidden,parse_constant=forbidden,parse_int=integer)
        canonical(result)
    except (UnicodeError,RecursionError,json.JSONDecodeError) as e:raise Invalid('JSON') from e
    return result

def native_fact_id(record):
    """Deterministic storage key for one immutable record revision."""
    validate(record)
    return 'urn:vercy:disclosure-revision:'+hashlib.sha256(canonical({'dimension':record['dimension'],'id':record['id'],'revision':record['revision']})).hexdigest()

def validate_native(fact,obj,*,dimension,capability,now,master,writer):
    """Companion semantic check AFTER separate V3 envelope validation.

    Host supplies authentic expected Dimension/master/writer and object registry.
    This is storage binding only, not active selection or disclosure permission.
    """
    authorize(capability,dimension)
    canonical(fact);canonical(obj)
    if not isinstance(fact,dict) or not isinstance(obj,dict):raise Invalid('native objects')
    for name in (master,writer):
        if type(name) is not str or not re.fullmatch(r'[A-Za-z][A-Za-z0-9+.-]*:[!-~]+',name):raise Invalid('native trusted identity')
    record=fact.get('value');validate(record)
    if record['dimension']!=dimension:raise Invalid('native Dimension')
    typ=record['type'];mid='vr.profile.enterprise-disclosure-review'
    if obj.get('recordType')!='object' or obj.get('schemaVersion')!='1.0.0' or obj.get('objectId')!=record['id'] or obj.get('objectType')!=mid+':'+typ or obj.get('state')!='active':raise Invalid('native object binding')
    if fact.get('recordType')!='fact' or fact.get('schemaVersion')!='1.0.0' or fact.get('subjectId')!=record['id'] or fact.get('path')!='disclosure.'+typ+'.revision':raise Invalid('native fact binding')
    if fact.get('factId')!=native_fact_id(record):raise Invalid('native revision identity')
    if fact.get('status')!='asserted' or 'unit' not in fact or fact['unit'] is not None or 'validTo' not in fact or fact['validTo'] is not None or fact.get('supersedes')!=[]:raise Invalid('native immutable storage semantics')
    if fact.get('accessClass')!='restricted' or obj.get('accessClass')!='restricted':raise Invalid('native access class')
    if fact.get('masterSystem')!=master or fact.get('authority')!={'source':writer,'rank':0} or type(fact['authority']['rank']) is not int:raise Invalid('native storage authority')
    if not isinstance(fact.get('provenance'),dict) or fact['provenance'].get('source')!=master or fact['provenance'].get('recordDigest')!=record['digest']:raise Invalid('native storage provenance')
    recorded=instant(fact.get('recordedAt'));object_at=instant(obj.get('recordedAt'));evaluation=instant(now)
    declared=instant(record['body']['capturedAt' if typ=='proposal' else 'reviewedAt'])
    if fact.get('validFrom')!=fact.get('recordedAt') or not object_at<=recorded<=evaluation or not declared<=recorded:raise Invalid('native storage time')
    return record

def hash_body(record):
    return 'sha256:'+hashlib.sha256(canonical({k:v for k,v in record.items() if k!='digest'})).hexdigest()

def instant(s):
    if not isinstance(s,str):raise Invalid('timestamp')
    try:
        m=re.fullmatch(r'([0-9]{4})-([0-9]{2})-([0-9]{2})T([0-9]{2}):([0-9]{2}):([0-9]{2})Z',s)
        if not m:raise ValueError()
        return datetime.datetime(*map(int,m.groups()),tzinfo=datetime.timezone.utc)
    except ValueError as e:raise Invalid('timestamp') from e

def pin(record):return {k:record[k] for k in ('id','revision','digest')}

def seal(record):
    if type(record) is not dict:raise Invalid('record object')
    canonical(record)
    result=copy.deepcopy(record);result['digest']=hash_body(result);validate(result);return result

def exact_identifiers(value,coherence=False):
    coherent={}
    def exact_strings(x):
        if isinstance(x,dict):
            if coherence and set(x)=={'id','revision','digest'}:
                previous=coherent.setdefault(x['id'],(x['revision'],x['digest']))
                if previous!=(x['revision'],x['digest']):raise Invalid('incoherent reference pin')
            for k,v in x.items():
                pattern=None
                if k in ('id','dimension','author','reviewer'):pattern=r'[A-Za-z][A-Za-z0-9+.-]*:[!-~]+'
                elif k in ('revision','key'):pattern=r'[A-Za-z0-9][A-Za-z0-9._-]*'
                elif k=='name':pattern=r'[A-Za-z_][A-Za-z0-9_]{0,63}'
                elif k=='digest':pattern=r'sha256:[0-9a-f]{64}'
                if pattern and (not isinstance(v,str) or not re.fullmatch(pattern,v)):raise Invalid('exact identifier syntax')
                exact_strings(v)
        elif isinstance(x,list):
            for v in x:exact_strings(v)
    exact_strings(value)

def validate(record):
    canonical(record)
    errors=list(VALIDATOR.iter_errors(record))
    if errors:raise Invalid('record shape')
    if record['digest']!=hash_body(record):raise Invalid('digest')
    exact_identifiers(record,coherence=True)
    b=record['body']
    if record['type']=='proposal':
        instant(b['capturedAt']);members=b['members']
        if len({m['key'] for m in members})!=len(members):raise Invalid('duplicate member key')
        for m in members:
            if len({f['name'] for f in m['fields']})!=len(m['fields']):raise Invalid('duplicate field')
    else:
        a,start,end=map(instant,[b['reviewedAt'],b['validFrom'],b['validTo']])
        if not a<=start<end:raise Invalid('review time interval')
        if b['supersedes'] and (b['supersedes']['id'],b['supersedes']['revision'])==(record['id'],record['revision']):raise Invalid('self supersession')
    return record

def authorize(capability,dimension):
    # These are trusted host assertions, never caller-submitted credentials.
    if not isinstance(dimension,str) or not re.fullmatch(r'[A-Za-z][A-Za-z0-9+.-]*:[!-~]+',dimension) or not isinstance(capability,dict) or capability.get('dimension')!=dimension or capability.get('inspect') is not True:
        raise Unauthorized('unavailable')

def validate_snapshot(snapshot,now):
    canonical(snapshot)
    v=Draft202012Validator({'$ref':'#/$defs/snapshot','$defs':SCHEMA['$defs']})
    if list(v.iter_errors(snapshot)):raise Invalid('snapshot shape')
    exact_identifiers(snapshot)
    for k in ('proposalAuthors','reviewers'):
        if any(not re.fullmatch(r'[A-Za-z][A-Za-z0-9+.-]*:[!-~]+',x) for x in snapshot[k]):raise Invalid('actor catalog syntax')
    if instant(snapshot['asOf'])!=instant(now):raise Invalid('snapshot time mismatch')
    active=snapshot['activeReviews'];withdrawn=snapshot['withdrawnReviews']
    if len({p['id'] for p in active})!=len(active):raise Invalid('multiple active revisions')
    a={(p['id'],p['revision']) for p in active};w={(p['id'],p['revision']) for p in withdrawn}
    if len(w)!=len(withdrawn):raise Invalid('conflicting withdrawn revision')
    if a & w:raise Invalid('active and withdrawn overlap')
    return {canonical(p) for p in active}

def inspect(proposal,reviews,snapshot,capability,now):
    """Return an INTERNAL applicability result for a complete trusted snapshot.

    The host attests current state, active-review completeness and authorities.
    It must resolve references independently; no remote artifacts are fetched.
    """
    dimension=snapshot.get('dimension') if isinstance(snapshot,dict) else None
    authorize(capability,dimension)
    active=validate_snapshot(snapshot,now)
    validate(proposal)
    if proposal['type']!='proposal' or proposal['dimension']!=dimension:raise Invalid('proposal scope')
    now=instant(now)
    if type(reviews) is not list or len(reviews)>64:raise Invalid('review set')
    counted=[];ignored=[];evaluated=False
    def result(status,reason=None):
        answer={'format':'vercy-disclosure-inspection','evaluatorVersion':VERSION,'status':status,'notServingAuthorization':True,'proposal':pin(proposal),'snapshotDigest':'sha256:'+hashlib.sha256(canonical(snapshot)).hexdigest(),'at':snapshot['asOf'],'reviewsEvaluated':evaluated,'counted':copy.deepcopy(counted),'ignored':copy.deepcopy(ignored),'withdrawn':copy.deepcopy(snapshot['withdrawnReviews'])}
        if reason:answer['reason']=reason
        return answer
    # Snapshot is a host catalog of current scalar metadata; exact equality avoids
    # undocumented classification order, schema adaptation, or shape widening.
    b=proposal['body'];context={k:b[k] for k in ('audience','purpose','environment','priorReleases','custodyContext')}
    if snapshot['proposal']!=pin(proposal):return result('stale','current-proposal-differs')
    if b['author'] not in snapshot['proposalAuthors']:return result('insufficient-context','proposal-author')
    if instant(b['capturedAt'])>now:return result('stale','future-capture')
    if context!=snapshot['context'] or b['members']!=snapshot['members']:return result('stale','current-inputs-differ')
    seen={};supplied=[]
    for r in reviews:
        validate(r)
        if r['type']!='review' or r['dimension']!=dimension:raise Invalid('review scope')
        if r['id']==proposal['id']:raise Invalid('identity changes type')
        if r['body']['proposal']!=pin(proposal):raise Invalid('review points to another proposal')
        if instant(r['body']['reviewedAt'])<instant(b['capturedAt']):raise Invalid('review predates proposal')
        key=(r['id'],r['revision'])
        if key in seen:raise Invalid('duplicate/conflicting review revision')
        if any(k[0]==r['id'] for k in seen):raise Invalid('multiple active revisions')
        seen[key]=r['digest'];supplied.append(pin(r))
    if {canonical(p) for p in supplied}!=active:return result('insufficient-context','review-set-incomplete')
    valid=[];evaluated=True
    for r in reviews:
        rb=r['body']
        if rb['supersedes'] and (rb['supersedes']['id'],rb['supersedes']['revision']) in seen:
            if rb['supersedes']['digest']!=seen[(rb['supersedes']['id'],rb['supersedes']['revision'])]:raise Invalid('incoherent supersession pin')
            raise Invalid('superseded review still active')
        reason=None
        if rb['reviewer'] not in snapshot['reviewers'] or rb['authority']!=snapshot['authority']:reason='authority'
        elif snapshot['separateReviewer'] and rb['reviewer']==b['author'] and rb['verdict']=='cleared':reason='self-clearance'
        elif instant(rb['reviewedAt'])>now:reason='future-assessment'
        elif now<instant(rb['validFrom']):reason='not-yet-valid'
        elif now>=instant(rb['validTo']):reason='expired'
        if reason:
            ignored.append({'pin':pin(r),'verdict':rb['verdict'],'reason':reason});continue
        counted.append(pin(r))
        valid.append(rb['verdict'])
    if not valid:return result('insufficient-context','no-applicable-review')
    if len(set(valid))>1:return result('conflict','active-review-disagreement')
    return result('applicable-review' if valid[0]=='cleared' else valid[0])

def import_records(existing,incoming,dimension,capability):
    """Pure transactional merge of immutable records, not persistent storage.

    Host must separately authorize writes, retain the full master set and apply
    compare-and-swap around persistence; this function has no database effects.
    """
    authorize(capability,dimension)
    if capability.get('record') is not True:raise Unauthorized('unavailable')
    if type(existing) is not list or type(incoming) is not list or len(existing)+len(incoming)>128:raise Invalid('record bounds')
    result=copy.deepcopy(existing);known={};types={}
    for n,r in enumerate(existing+incoming):
        validate(r)
        if r['dimension']!=dimension:raise Invalid('record scope')
        if r['id'] in types and types[r['id']]!=r['type']:raise Invalid('identity changes type')
        types[r['id']]=r['type']
        key=(r['type'],r['id'],r['revision'])
        if key in known:
            if known[key]!=r['digest']:raise Invalid('immutable revision conflict')
            if n<len(existing):raise Invalid('duplicate stored revision')
        else:
            known[key]=r['digest']
            if n>=len(existing):result.append(copy.deepcopy(r))
    # The supplied store is the complete local proposal/review master set. Domain
    # source and evidence references remain external; these two internal edges do not.
    records={(r['id'],r['revision']):r for r in result}
    edges={}
    def resolve(p,typ):
        target=records.get((p['id'],p['revision']))
        if target is None or target['type']!=typ or pin(target)!=p:raise Invalid('unresolved internal pin')
        return target
    for r in result:
        if r['type']!='review':continue
        rb=r['body'];proposal=resolve(rb['proposal'],'proposal')
        if instant(rb['reviewedAt'])<instant(proposal['body']['capturedAt']):raise Invalid('review predates proposal')
        if rb['supersedes']:
            prior=resolve(rb['supersedes'],'review')
            if prior['body']['proposal']['id']!=rb['proposal']['id']:raise Invalid('supersession crosses proposal identity')
            if instant(prior['body']['reviewedAt'])>instant(rb['reviewedAt']):raise Invalid('supersession time reversal')
            edges[(r['id'],r['revision'])]=(prior['id'],prior['revision'])
    for start in edges:
        visited=set();node=start
        while node in edges:
            if node in visited:raise Invalid('supersession cycle')
            visited.add(node);node=edges[node]
    return result

</file>
END FILE disclosure.py

## FILE disclosure.schema.json
ORIGINAL SHA256 45b2f2c82b9d9af72b2b462d3e502098fbd5b166bf8bd705947ba12e1e5cc834
<file>
{"$schema":"https://json-schema.org/draft/2020-12/schema","title":"Enterprise Disclosure Review 0.1.0 closed metadata records","oneOf":[{"$ref":"#/$defs/proposal"},{"$ref":"#/$defs/review"}],"$defs":{"pin":{"type":"object","properties":{"id":{"type":"string","pattern":"^[A-Za-z][A-Za-z0-9+.-]*:[!-~]+$","minLength":3,"maxLength":512},"revision":{"type":"string","pattern":"^[A-Za-z0-9][A-Za-z0-9._-]*$","minLength":1,"maxLength":128},"digest":{"type":"string","pattern":"^sha256:[0-9a-f]{64}$"}},"required":["id","revision","digest"],"additionalProperties":false},"time":{"type":"string","pattern":"^\\d{4}-\\d\\d-\\d\\dT\\d\\d:\\d\\d:\\d\\dZ$"},"field":{"type":"object","properties":{"name":{"type":"string","pattern":"^[A-Za-z_][A-Za-z0-9_]{0,63}$"},"kind":{"enum":["string","integer","number","boolean","null"]},"classificationBindings":{"type":"array","items":{"$ref":"#/$defs/pin"},"minItems":1,"maxItems":8,"uniqueItems":true}},"required":["name","kind","classificationBindings"],"additionalProperties":false},"member":{"type":"object","properties":{"key":{"type":"string","pattern":"^[A-Za-z0-9][A-Za-z0-9._-]*$","minLength":1,"maxLength":128},"source":{"$ref":"#/$defs/pin"},"schema":{"$ref":"#/$defs/pin"},"shape":{"$ref":"#/$defs/pin"},"fields":{"type":"array","items":{"$ref":"#/$defs/field"},"minItems":1,"maxItems":64,"uniqueItems":true}},"required":["key","source","schema","shape","fields"],"additionalProperties":false},"proposalBody":{"type":"object","properties":{"author":{"type":"string","pattern":"^[A-Za-z][A-Za-z0-9+.-]*:[!-~]+$","minLength":3,"maxLength":512},"capturedAt":{"$ref":"#/$defs/time"},"audience":{"$ref":"#/$defs/pin"},"purpose":{"$ref":"#/$defs/pin"},"environment":{"$ref":"#/$defs/pin"},"priorReleases":{"$ref":"#/$defs/pin"},"custodyContext":{"$ref":"#/$defs/pin"},"members":{"type":"array","items":{"$ref":"#/$defs/member"},"minItems":1,"maxItems":32,"uniqueItems":true}},"required":["author","capturedAt","audience","purpose","environment","priorReleases","custodyContext","members"],"additionalProperties":false},"reviewBody":{"type":"object","properties":{"proposal":{"$ref":"#/$defs/pin"},"reviewer":{"type":"string","pattern":"^[A-Za-z][A-Za-z0-9+.-]*:[!-~]+$","minLength":3,"maxLength":512},"authority":{"$ref":"#/$defs/pin"},"method":{"$ref":"#/$defs/pin"},"evidence":{"type":"array","items":{"$ref":"#/$defs/pin"},"minItems":1,"ma