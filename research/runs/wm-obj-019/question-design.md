# Component Type / Engineering BOM: subject-authored structure

Proposed aggregate root: an engineering composition revision, not an installed
physical assembly. COMPOSE WM-OBJ-002 is the frozen registry relationship.
Component type identity remains in the product master; occurrence identity is
local to the engineering composition. The following questions are original
subject design, not claims that a cited vendor requires these exact fields.

## 1. Composition authority

### BOM identity, view and baseline

- Which issuer-qualified BOM identity, immutable revision and engineering view define the composition being read?
- Which parent product type and controlled design revision does this baseline describe, and which representations are authoritative?
- Which required members or referenced revisions are missing, unresolved or intentionally withheld from this baseline?

Candidate fields: identity {issuer, bom_id, revision, view, master}; subject
{WM-OBJ-002 reference, WM-OBJ-018 reference, representation authority}; baseline
{member IDs/revisions/digests, completeness criteria, absent status/reason}.
Sources: Microsoft BOM documentation; ISO AP242 public scope; NASA CM.

### Component types and occurrences

- Which component type and exact revision is referenced by each occurrence, independently of its displayed item number?
- How are repeated occurrences, hierarchical reference designators and merged display rows distinguished and reversibly mapped?
- Which occurrence-specific placement, footprint or interface binding identifies its intended position without asserting an actual item's location?

Candidate fields: component-binding {occurrence_id, component issuer/id/revision};
occurrence-map {parent occurrence, path, designators, display-row membership};
placement-definition {design feature/frame/interface references, footprint,
nominal transform or explicit unknown, not measured pose}.
Sources: Autodesk BOMRow and Electronics BOM; ISO AP242 public scope.

## 2. Quantified assembly graph

### Quantity basis and dimensional meaning

- What component quantity and unit apply per declared parent base quantity, rather than per an assumed single finished item?
- Which item-count, per-occurrence amount, conversion, rounding and override rules produce a reported total, and what evidence supports them?
- Which quantities are unknown, variable or outside the engineering view, including manufacturing scrap, yield and actual consumption?

Candidate fields: quantity-basis {component amount/unit, parent base amount/unit};
calculation {count, unit amount, conversion registry/version, precision,
rounding, override reason/authority}; quantity-state {known/unknown/conditional,
expression reference, excluded process terms and view-specific exceptions}.
Sources: Autodesk About BOM Quantity; Microsoft BOM documentation.

### Subassembly reuse and traversal integrity

- Which subordinate BOM revisions are reused, and which occurrence paths must remain distinct when the same subassembly appears more than once?
- Is a detected cycle in the unfiltered family graph or the selected effective graph, and where must traversal stop safely?
- Which unresolved references, depth limits, access-denied branches or intentional recursive-process boundaries make an expansion incomplete?

Candidate fields: dependency-graph {parent/child occurrence, pinned child BOM,
view}; cycle-analysis {graph scope, selection context, cycle path, stop reason,
declared handling policy}; expansion-completeness {visited revisions, truncated
paths, unavailable nodes, reason and responsible resolver}.
Sources: SAP Recursiveness Check; Autodesk BOMRow; Microsoft BOM documentation.
An intentional process-recursion reference is not permission for infinite
engineering expansion or a claim that a physical item contains itself.

## 3. Applicability and selection

### Effectivity and revision resolution

- Under which time, variant, site or other explicitly declared context predicates does a BOM revision or line apply?
- Which resolver and pinned context selected each component revision, and how are overlapping or missing applicable revisions reported?
- How are approval time, recording time and effective boundaries preserved when a retrospective correction changes applicability?

Candidate fields: applicability {typed predicate, context dimensions, endpoint
inclusivity, time offset}; resolution {rule/version, inputs, chosen revisions,
ambiguous/missing outcomes}; temporal-history {recorded/approved/effective
timestamps, superseding record, correction reason, historical query context}.
Sources: Microsoft BOM versions; NASA CM; RFC3339.

### Options, alternates and substitutes

- Which optional or alternative component groups are available, and what cardinality and compatibility conditions constrain selection?
- Which approved substitution is directional, context-limited or conditional on interface and capability evidence rather than universal interchangeability?
- Which selected option set and explicit exclusions belong to the configured engineering composition, without treating every candidate as installed?

Candidate fields: choice-groups {members, min/max selections, constraints,
unresolved predicates}; substitution {from/to revisions, direction, applicability,
qualification evidence, approver}; configured-selection {WM-OBJ-017 binding,
selected occurrences, not-selected/unknown reasons, evaluation receipt}.
Sources: Microsoft alternative BOM versions; Autodesk Electronics BOM.
Detailed alternate-group semantics are proposed Vercy design requiring further
industry review; no universal vendor-independent interchangeability implied.

## 4. Intended characteristics

### Component properties and recognition references

- Which versioned material, nominal size, mass and other physical-property definitions belong to each component type, with units and conditions?
- Which distinguishing features, markings, footprints or interface references help identify the intended component class, and what recognition uncertainty remains?
- Which aggregate property is derived from the selected composition, using what method and exclusions, instead of being mistaken for a measured assembly property?

Candidate fields: nominal-properties {property ID, value/unit, conditions,
source revision, unknown}; recognition {feature/design references, identifier
namespace, distinguishing evidence, ambiguity}; aggregate-derivation {target
property, method/version, selected inputs, exclusions, uncertainty, evidence}.
Sources: ISO AP242 public scope; Autodesk Electronics BOM and quantity docs;
W3C PROV-DM. Hardness, density, colour and safety cannot be guessed from a BOM.

### Functional contribution and assembly constraints

- What intended functional role does an occurrence contribute, and which design or requirement master defines that role?
- Which mating, material, load or environmental constraints must hold for components to function together in this composition?
- Which unverified capability, prohibited use or unresolved compatibility issue prevents an agent from claiming the assembly is fit for a requested action?

Candidate fields: role-binding {occurrence, function/class reference, design
revision}; assembly-constraints {endpoints, predicate, operating envelope,
verification evidence}; capability-disposition {claim, evidence status,
limitations, prohibited uses, unresolved reviewer decision}.
Sources: ISO AP242 public scope; NASA CM for controlled evidence;
W3C PROV-DM. This is proposed information structure, not a physical solver.

## 5. Change and realization boundary

### Approval, change and where-used impact

- Who may approve or retire this engineering baseline, and which open findings prevent release under the owning Dimension's policy?
- Which changed occurrence, quantity or revision affects which parent baselines and configured variants according to a context-qualified where-used query?
- What expected-base check, decision and history preserve concurrent edits and approved deviations without silently rewriting released composition?

Candidate fields: release {authority, gates, findings, decision, timestamp};
impact {changed IDs, reverse-reference graph scope, affected parent revisions,
unknown consumers, review disposition}; change-control {expected digest,
before/after revisions, reason, conflict, scoped deviation and approval}.
Sources: NASA CM; Microsoft BOM approval; W3C PROV-DM.

### Engineering-to-manufacturing handoff

- Which engineering occurrences map to which manufacturing BOM or process-master records, including split, merged, phantom or omitted representations?
- Which make-or-buy intention or manufacturing-only addition is recorded as a qualified handoff assumption rather than an engineering component fact?
- What receiving-system acknowledgement and discrepancy disposition preserve the original engineering baseline when the production or as-built view differs?

Candidate fields: cross-view-map {source/target revisions, occurrence mappings,
transform kind, loss}; realization-assumptions {make/buy status, authority,
process/material additions, target view}; handoff-receipt {recipient, package
digest, time, acceptance, divergence and change decision references}.
Sources: Microsoft BOM lifecycle; Autodesk BOMRow; NASA CM; W3C PROV-DM.
No purchase, production order or equipment actuation is authorized by this model.

## 6. Governed composition exchange

### Mastership, disclosure and preservation

- Which Dimension and engineering authority own the baseline while external component masters retain their own stewardship?
- Which occurrence details and artifacts may each recipient read or export, and how is a withheld branch distinguished from an empty assembly?
- Which retention triggers, holds and preserved dependency references keep retired BOM revisions interpretable without retaining unnecessary protected content?

Candidate fields: authority-map {owner, author, component master, custodian};
disclosure {recipient, purpose, scope, authorization, redaction/completeness
status}; preservation {retention trigger, hold, historical dependency policy,
readability checks, minimized tombstone}.
Sources: NASA CM; W3C PROV-DM. Specific access and retention policies are Vercy
governance requirements, not legal advice or claimed PROV authorization semantics.

### Exchange fidelity and semantic validation

- Which source and target profile versions, exact-byte digests and transformation provenance bind an exported composition?
- Which occurrence identity, unit, effectivity, selection or reference-designator semantics are lost or changed by flattening or row merging?
- Which declared acceptance fixtures and rejection rules establish a usable mapping while keeping unsupported constructs visible?

Candidate fields: exchange {profiles/versions, translator, source/target digest,
provenance}; semantic-loss {construct, affected paths, severity, sidecar or reject
disposition}; acceptance {fixture/version, criteria, results, limitations}.
Sources: Autodesk BOMRow and Electronics BOM; ISO AP242 public scope; PROV-DM.
The proposed nested field groups are not an executable instance schema or a
tested AP242 crosswalk. Adapters and real-product fixtures remain adoption work.
