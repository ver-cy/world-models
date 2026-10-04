# WM-OBJ-019 source evidence and research limitations

Source inspection occurred in this canonical dialogue on 2026-09-07. Work
resumed on 2026-09-09 after R: became available. This note preserves observed
evidence; it does not claim that the URLs were fetched again on the resume date.
The 36 questions in question-design.md are a proposed Vercy decomposition.
Documentation supports concepts, not every proposed field or policy.

## Admitted sources

1. Microsoft, Bills of materials and formulas, updated 2025-07-10:
   https://learn.microsoft.com/en-us/dynamics365/supply-chain/production-control/bill-of-material-bom
   Inspected public page content: BOM header/lines, single-level identity and
   referenced subordinate BOMs; different engineering, production and costing
   views; version applicability, approval and ambiguity. Vendor-specific
   behavior is not a universal BOM rule. Route and manufacturing transactions
   retain separate ownership.
2. Autodesk Inventor 2023, About BOM Quantity:
   https://help.autodesk.com/cloudhelp/2023/ENU/Inventor-Help/files/GUID-37BA8DB6-E39C-4C96-AAF1-E7B342F20D0E.htm
   Inspected indexed documentation text: occurrence count, amount contributed
   by each occurrence, units and overrides. This motivates preserving a declared
   calculation basis; it does not justify blindly applying one product's
   exclusions to every engineering view.
3. Autodesk Inventor 2023 API, BOMRow Object:
   https://help.autodesk.com/cloudhelp/2023/ENU/Inventor-API/files/BOMRow.htm
   Inspected public property table: component definitions and occurrences,
   merged/promoted rows and quantity override status. A display row need not
   identify exactly one component occurrence. No actual adapter was executed.
4. Autodesk Fusion Electronics, Electronics Bill of materials:
   https://help.autodesk.com/cloudhelp/ENU/Fusion-ECAD/files/ECD-BOM-CPT.htm
   Inspected short public page: reference designators, footprints and component
   identification; flattened versus hierarchical designators. Electronics
   examples are not mandatory fields for every mechanical or process BOM.
5. SAP ERP 6.0 EHP8, Recursiveness Check:
   https://help.sap.com/docs/SAP_ERP/43fa3cddb00348beb3ed12212a94448f/dd05c453f57eb44ce10000000a174cb4.html
   Indexed public text was readable; direct web opening returned an empty
   client-rendered shell. The text distinguishes group-level recursion from
   individual variants and describes stopping expansion. Intentional process
   recirculation exists in examples; it must not be misrepresented as literal
   physical self-containment or permission for infinite traversal. Source-depth
   limitation must remain in the publication evidence.
6. ISO 10303-242:2025, edition 4, public scope only:
   https://www.iso.org/standard/84300.html
   Public catalogue scope inspected for engineering product definition and
   structure. Licensed clauses, schema bindings and conformance rules were not
   inspected. This is a candidate alignment, not implemented AP242 conformance.
7. NASA Systems Engineering Handbook, Configuration Management, chapter 6.5:
   https://www.nasa.gov/reference/6-5-configuration-management/
   Selected public chapter content inspected for controlled baselines, change
   authority and historical configuration context. This domain guidance does
   not impose NASA's lifecycle on all adopters. Vercy-specific access, expected
   base and retention policies are proposed safeguards, not NASA compliance.
8. W3C, PROV-DM Recommendation 2013-04-30:
   https://www.w3.org/TR/prov-dm/
   Selected entity/activity/agent and derivation concepts inspected for
   attribution of composition assertions and transformations. PROV does not
   grant access, certify truth or implement a BOM resolver.
9. IETF, RFC 3339, July 2002:
   https://www.rfc-editor.org/rfc/rfc3339
   Timestamp syntax supports seconds and explicit UTC offset. Master IDs or
   UUIDs provide identity; a timestamp alone is neither collision-proof nor an
   applicability interval definition. Pin interval boundary semantics separately.

## Rejected or deferred evidence

SAP Using Alternative Item Groups was found, but direct reading returned an
empty shell and the available snippet described an MBOM-specific workflow.
It is not admitted as support for a complete general engineering-alternates
contract. Directional substitutions and group cardinalities are explicit Vercy
design proposals pending further specialist review.

No evidence from former stream worktrees was copied. No valid external research
was returned: Claude and Grok each have a terminal timeout manifest from their
single bounded attempt. Neither may be retried for WM-OBJ-019.

## Required visible holds

- No independent external research or review; eventual assurance remains
  reviewable-draft with medium or low confidence, never canonical.
- Selected vendor documentation and public ISO scope are not normative
  source-to-field compliance, exhaustive industry research or working adapters.
- SAP source inspection is indexed text only; licensed ISO clauses unread.
- No executable instance schema, BOM solver, unit-calculation implementation,
  substitution qualification or real-product round-trip fixtures delivered.
- Direct properties and functional claims need component/design evidence.
  No physical capability, safety, hardness, density or actual condition may be
  inferred merely from a structurally valid composition record.
