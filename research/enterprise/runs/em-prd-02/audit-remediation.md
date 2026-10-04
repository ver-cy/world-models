# EM-PRD-02 audit remediation

The single frozen Claude audit returned `ACCEPT WITH LIMITS`. All eight holds were incorporated deterministically; the audit was not repeated.

- Service-definition revisions are contained under the existing `serviceId`. The Service owner assigns a monotonic `ownerAssignedVersion`; identity-dimension changes create a successor Service rather than silently re-versioning.
- Realization Binding and Service Dependency are definition-scoped append-only history records. They expose no public URI, independent lookup or lifecycle event.
- The accountable-provider role type is an accountability archetype independent of provider party, geography and internal or outsourced sourcing mode.
- Association record keys use owner version plus owner-local ordinal. Kind, type and scope labels never participate in persistent keys.
- Effective bindings and dependencies remain held until pinned external realization-kind, scope and dependency-type vocabularies are approved.
- Offering-backed consumption derives from Service, offering and party; offering-less internal activity derives from Service, party and its owning entitlement/request/fulfilment record.
- Requestability is catalogue applicability, not Service identity. Requestable or subscribed Services remain held until an allocated EM-PRD-01 offering resolves.
- SLA and observation joins use the instance-level `(registryId, serviceId)` tuple and `serviceVersionRef` when revision-specific.
- Reference visibility is the intersection of every linked record's permissions, with non-disclosing redaction.

Fixtures cover each correction. The disposition remains completion of reserved WM-ACT-004 with `newRuntimeId=false` and held publication status.
