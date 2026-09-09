# WM-OBJ-019 frozen reusable engineering composition scope

Registry: Component Type / Engineering BOM; parent WM-OBJ-002.
Frozen relation: WM-OBJ-019 COMPOSE WM-OBJ-002, engineering BOM composes
component types (type-level assembly). Packaging standalone-mm is not a
research entry-kind enum. Prefer a coherent engineering-composition aggregate
root and distinguish its component-type references and internal occurrences.

Own reusable type-level composition, not physical as-built assembly, production
route, inventory, procurement order, software BOM or actual material consumption.
Reference component type identity and controlled design WM-OBJ-018; selected
variant WM-OBJ-017 selects/applicability-binds composition, not item serials.

Investigate BOM identity/revision, engineering view and baseline; parent/child
type references versus occurrence identity; repeated components, reference
designators, find numbers and subassembly reuse; quantity basis and unit
conversion; effectivity and revision resolution; option/alternate/substitute
semantics; graph cycle detection and incomplete dependencies; make/buy and
engineering-to-manufacturing handoff without owning routing or planning;
nominal material/property and capability references, aggregate derivation and
uncertainty; approvals/change/where-used impacts; access/retention/provenance;
native/neutral exchange and explicit loss.

Do not flatten repeated occurrences, confuse containment with instance
ownership, treat optional/alternate lines as simultaneously installed, silently
resolve latest revisions, multiply incompatible units, or count manufacturing
scrap/yield as intrinsic engineering composition without a declared view.

Use primary standards/public scopes and official product documentation;
vendor behavior is implementation evidence, not universal mandatory semantics.
Aim for six subject-specific bundles and 12-18 focused records with distinct
questions and explicit typed fields. Never reuse generic question templates.
