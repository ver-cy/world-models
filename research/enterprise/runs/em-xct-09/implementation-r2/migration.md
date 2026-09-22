# Version, correction and migration

Scheme migration is a review proposal with qualified source/target releases. Original assignments remain in their original version; new live assignments require a separately authorized host workflow. Split/merge, incomplete or competing correspondences are retained for human review. No nearest-label or score tie-break is permitted.

A correction creates a new captured assignment revision referencing its predecessor. The host explicitly selects which source revision is authoritative; this evaluator does not pick the highest revision. Packet revisions preserve their predecessor digest but the host maintains and verifies that chain. Assessment identity includes packet, evaluator build and approval basis; no existing result is edited.

migrate_snapshot only round-trips a current exact-build0.1.0 snapshot. Any other version/build or changed meaning is refused; there is no automatic upgrade/downgrade, lossful export, writable restoration or model-ID replacement. Preserve the original files and their verifier. Native recording supports new local assessment objects; migration of an existing Dimension is separate work.
