# EM-LND-17 local synthesis

## Disposition

- Reuse the existing spatial and physical-item masters. Do not create a new place, facility, building or asset type.
- Treat **Asset Place Landscape** as a governed landscape declaration with local artifact identity for scope, viewpoint, owner, pinned inputs, as-of time, disclosure policy and publication digest. No catalogue/runtime identifier is allocated without a registry reservation.
- Treat **Occupancy View** as a named, reproducible projection inside that declaration; it has no independent identity.
- Raise **Asset Placement Episode** and **Operational Responsibility Assignment** as identifier-unassigned relation candidates. They have independent validity and lifecycle, but registry allocation and boundary review are still required.

## Mastership and spatial spine

Gazetteer place, site/campus, facility, building/structure, interior spatial unit and movable physical item remain separate identities. The composed spine is place/parcel → site → facility → building → spatial unit, with movable items attachable at any appropriate level. Address is a binding/value object and never the identity of a place, facility or asset.

Containment is an authored, evidenced and effective-dated assertion. Geometry overlap, common address or reporting boundary cannot create containment. Site-to-facility membership may be absent or non-exclusive. A registered company address never locates all company assets.

## Placement, custody and responsibility

Placement, custody, title, operational responsibility, occupancy/use, availability and maintenance are distinct:

- placement records asset, locus, granularity, planned or observed mode, validity, basis, asserting party, confidence and disclosure class;
- custody remains owned by WM-OBJ-001;
- ownership/title and lease interest remain external legal/economic relations;
- operational responsibility relates a responsible party to an asset scope for a validity interval and governing basis;
- occupancy/use is an effective-dated designation or relation;
- availability is derived for a stated purpose;
- maintenance references work orders and condition evidence.

Possession does not imply title, responsibility does not imply custody, and placement does not grant access.

## Planned, observed and available

Planned placement belongs to a named plan/scenario and authorizing context. Observed placement carries observation time, ingestion time, source, precision and confidence. Divergence is an explicit exception. Unknown whereabouts is a state with an optional last-known fix; it is not absence or disposal.

Occupancy View computes effective placement intersected with space, use designation and capacity at a stated instant. Availability additionally depends on purpose, operating hours, access regime, operational/regulatory state, hazard overlays and maintenance windows. It is never stored as a timeless fact.

## Acceptance result

A leased asset moves from Site A to Site B. The A placement closes; a planned B placement exists under the move scenario; an observed B placement opens when evidence arrives. Ownership remains with the lessor. Custody may pass through a carrier. Operational responsibility transfers on its own effective date. An open maintenance order remains due and re-resolves to the new operational context without proving work completion. Every historical interval remains reconstructable.

## Privacy invariants

Personal/home loci are represented only at the authorized generalized place or jurisdiction level. Sensitive asset and site coordinates are coarsened or withheld according to policy. Withheld and absent remain distinct. Derived views cannot reconstruct finer location from released data, and exceptional access is purpose-bound and audited.

## Holds

WM-BLT-006 and WM-BLT-008 remain `publishableCanonical: false` with unresolved source, IFC, crosswalk and validation holds. WM-BLT-002 still needs completion as the interior-space authority. Multi-site facility apportionment and the two proposed relation boundaries remain unresolved. No new identifier is allocated, and no installable release is claimed.
