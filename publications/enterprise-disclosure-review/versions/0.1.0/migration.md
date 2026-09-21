# Version and migration policy

The only implemented transport is complete same-version JSON roundtrip and idempotent immutable import. Version 0.1.0 rejects prototype versions and all unknown versions. The version is included in the digest, so a version edit changes every record and dependent review pin. Preserve old bytes and their original validator. No automatic upgrade, downgrade, mixed-version merge or silent schema reinterpretation is offered.

A future governed conversion must explicitly map proposal, review, supersession and external pins, preserve originals and attribution, identify changed meaning and obtain fresh assessments for changed packages. Re-sealing an old review under a new version must never impersonate its reviewer. Rollback is restoration of the complete verified register and matching governance state, not choosing an old clearance as a current grant. Concurrency/CAS, backups and existing-Dimension migration remain host integrations.
