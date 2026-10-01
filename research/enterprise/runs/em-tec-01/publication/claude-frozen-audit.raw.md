REVISE

Identifier and publication status confirmed clean: modelId and registryId are null, allocationState is unassigned, newRuntimeId is false, canonicalPublishable is false, and fixtures are non-executable. No identifier or publication readiness is claimed.

Defect checklist (closed, 24 items)

1. ownerRef contradicted effective-dated stewardship; add an ownership-period carrier.
2. hostRef and namespace contradicted locator-independent identity; master them in RepositoryLocator.
3. status had no state history; add status periods.
4. transferred is an event, not a state; separate states and events and include tombstone handling.
5. fork provenance lacked a repository-level carrier; add fork-source reference.
6. retired identifiers lacked a tombstone carrier; require a retirement record on exit states.
7. RepositoryLocator key forbade concurrent locators; add a locator discriminator.
8. contentDigest lacked an algorithm and distinction from treeDigest; add digestAlgorithm and define both.
9. SR-06 legislated over the excluded build plane and an unapproved relation; move it to the profile and keep it pending relation approval.
10. SR-07 legislated product cardinality; move it to the profile.
11. WM-SFT-009 provenance was a derived path, not a direct repository reference; label it derived.
12. The profile did not bind the Source Repository candidate; register it as a pending neighbour.
13. WM-SFT-010 was dropped; record it as a reference.
14. Bases had no machine-readable draft/waiver status; add per-base status.
15. EP-02 falsely asserted child facts already removed; restate as a required edit and enumerate the eight bundles.
16. EP-07 mixed decided SBOM mastership with unresolved relation kind; split rule and hold.
17. Release versus deployment lacked an explicit N:M rule; add it.
18. Product support versus observation, interface ownership, and SBOM/product/component identity invariants were missing; add them.
19. Projection non-copying lacked derivation markers and an owner-validation gate; add them.
20. Architecture/engineering owner gap and named base defects were not enumerated; carry them in holds.
21. AISMM 3.1.0 lacked its evidence anchor; record repository pin evidence.
22. Repository and runtime evidence were flattened; distinguish repository evidence from unproven runtime compatibility.
23. Fixture polarity was asymmetric; add positive and negative cases for each rule.
24. Fixtures were abstract and overloaded; bind them to named fields, split scenarios, cover tags, and exercise delivery profiles individually.
