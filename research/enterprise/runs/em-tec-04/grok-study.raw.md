# EM-TEC-04 — Independent Grok Review

## Verdict

**Accept-with-conditions.** Completing reserved WM-SFT-010 as Runtime / Compute Environment is the right place-and-capacity boundary if WM-SFT-002 stays the logical system/application and WM-SFT-009 stays the deployment occurrence. WM-XCT-039 may be reused only for mastership assignment and impact projection. Two conditions are mandatory: DeployedInstance is not accepted as a first-class 010 gold-copy master; ConfigurationItem is not an independent subject identity. This is an independent boundary review of given codes. It is not a catalog and does not claim completeness. Reservation text for WM-SFT-010 was not available, so “complete reserved” is unverified.

## Identity / mastership

One durable subject has one master. 002 owns logical identity and is invariant under deploy, region, scale, and node replacement. 009 owns the placement act and its intended binding. 010 owns RuntimeEnvironment and InfrastructureResource identity. HostingRelation is a temporal fact, not a third system of record. 039 records which source is authoritative for which attribute slice and projects impact from those masters plus observed hosting; it must not mint or redefine 002/009/010 identity. Observed hosting and declared placement may disagree. Coincidence of name, address, or CI label is not identity merge.

## Environment / resource / instance / CI

RuntimeEnvironment is durable place or compute context, including a regional runtime. InfrastructureResource is allocatable operational capacity (node, pool, host slice), not a financial asset. DeployedInstance as proposed does not belong in 010 as a competing master. “Deployed” names a 009 result; “instance” is ambiguous among replica, environment-binding, and occurrence-result. Live replicas outnumber and outlive one occurrence (scale-out, restart, reschedule) without becoming a new 002 subject or, necessarily, a new 009 act. A thin dependent occupant record may sit with 010 for as-of hosting if and only if it is not a gold-copy master and is bound to a 009 occurrence and a 002 subject; minting authority should not default to 010. ConfigurationItem is an effective-dated control designation (owner, criticality, change window, audit scope) over a referenced 002, 009, or 010 subject. A designation-record surrogate key is allowed. That key is not a fourth identity for the designated thing. Withdrawing the designation must not destroy the subject.

## Hosting / topology

HostingRelation is the only temporal bind of occupant to environment or resource. Topology is derived from as-of hosting plus membership, not a separate master. Membership (node in cluster) and hosting (occupant on resource) are different intervals; the proposal names the latter and leaves the former implicit. Desired placement lives on 009; observed hosting lives on 010 relations. Neither silently overwrites the other. Multi-region is two environments, not one environment with a region attribute pretending to be topology. Allowed HostingRelation endpoints and subject classes are not given.

## Ephemeral history

Keys are never recycled. End of life is a tombstone, not a delete-and-reuse. As-of queries reconstruct occupancy from open and closed intervals plus tombstones. Addresses, hostnames, and IPs are time-stamped observations attached to a subject or relation; they are never identity. Recycled node names or addresses must not resurrect a closed subject. Retention bounds for tombstones are required policy and are not specified here.

## Asset boundary

Physical and financial assets remain in separate masters. 010 InfrastructureResource is a runtime view of capacity. Join asset to resource only by evidence (correlation, serial, provider resource identifier, effective dating, confidence). Do not collapse the asset register into the runtime model. Cloud capacity may have no asset; an asset may have no current runtime resource. Asset identity, resource identity, and CI designation remain distinct.

## Cluster / node

A logical cluster keeps identity while node membership changes. Membership rewrite is not identity rewrite. Node replacement closes the old membership and hosting intervals, issues a new non-recycled node key, tombstones or closes the old node record, and opens new intervals. Cluster identity is unchanged. The 002 service is unchanged.

## Scenario

One 002 service. Two 010 RuntimeEnvironments in two regions. One 009 occurrence per region placing the same logical service. One cluster identity per region. Occupants referenced from those occurrences are hosted on nodes in each environment. At T1, 039 as-of impact for the 002 subject includes the old node in the first region. That node is replaced: old key is not recycled; HostingRelation and membership close; new node key is issued; new relations open; cluster identity unchanged. At T2, impact for the same 002 subject no longer includes the old node and includes the new node. CI designations ride the 002 subject, and optionally the environment, not the replaced node. Addresses observed on the old and new nodes remain observations.

## Invariants

1. 002 identity is invariant under deploy, host, scale, region, and node replace.
2. 009 records an occurrence, not place/capacity and not automatically the replica.
3. 010 masters are place and capacity; keys are never recycled; tombstones stay as-of queryable.
4. HostingRelation is the sole temporal occupant-capacity bind; topology is derived.
5. Desired 009 placement and observed 010 hosting may diverge.
6. CI designates; designation-record key is not subject identity.
7. Asset identity is not InfrastructureResource identity; join by evidence only.
8. Address, hostname, and IP are observations, not identities.
9. Cluster identity survives node membership change.
10. 039 projects mastership and impact; it does not own 010 facts.
11. Region is not flattened into a single environment identity.

## Blockers

1. DeployedInstance semantics (replica vs environment-binding vs 009 result) and minting authority are unspecified; placement cannot close until named.
2. Cardinality from one 009 occurrence to N occupants and M resources is unspecified; this decides whether a separate occupant record is necessary.
3. Possible name collision if 009 already has an instance concept is unknown and is not invented here.
4. HostingRelation allowed endpoint types and subject classes are not given.
5. Cluster-membership versus hosting is not distinguished as temporal facts.
6. CI-eligible subject types for this boundary are not enumerated.
7. Asset-resource evidence contract is unspecified.
8. Reservation text for WM-SFT-010 is unavailable.
9. Region / environment / cluster / node identity stack is not stratified.
10. Tombstone retention policy is unspecified; as-of history is otherwise unbounded.
11. Instance key authority (orchestrator identifier versus registry) is unassigned, with recycle risk.
12. Mastership of observed versus declared hosting is unspecified, so 039 cannot project an authoritative slice.

## Challenges

DeployedInstance does not belong in WM-SFT-010 as a first-class owned master. ConfigurationItem does not need independent subject identity.
