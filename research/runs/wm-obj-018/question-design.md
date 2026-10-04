# Subject-specific engineering-definition questions

Candidate information records for the six proposed bundles. These are design
questions, not claims that any real product has passed these checks.

## Design identity and authority

### Controlled revision and design subject

- Which authoritative design ID and revision denote the intended definition,
  independently of CAD filenames, exports and copies?
- Which product family, intended configuration and design maturity are in scope?
- Which representation is authoritative if a drawing and 3D model disagree,
  and who can resolve that disagreement?

Candidate fields: issuer-qualified design ID; revision; family reference;
maturity code; authority policy; competing representation assertions.

### Baseline and technical data package

- Which exact file revisions and digests constitute this baseline?
- Which deliverables are required at this maturity and which are intentionally
  absent rather than accidentally missing?
- Can a recipient retrieve the released package without following a mutable
  latest pointer or losing controlled external references?

Candidate fields: baseline ID; manifest entries; maturity-specific checklist;
missing-item reason; dependency digest; resolver and retrieval status.

## Intent and justification

### Requirement allocation

- Which WM-REC-006 requirement revision does each design element realize?
- Which requirements remain unallocated or have conflicting allocations?
- Which evidence and responsible reviewer justify marking an allocation
  satisfied instead of merely linked?

Candidate fields: requirement/design-element relation; revision pairs;
allocation status; verification criterion; evidence and reviewer references.

### Alternatives and rationale

- Which alternative solutions were evaluated against which decision criteria?
- Which assumptions or uncertain estimates could reverse the selected trade-off?
- Which decision authority selected the solution and what triggers reconsideration?

Candidate fields: alternatives; criteria and weights; assumptions; uncertainty;
decision reference; rejected-option rationale; reconsideration trigger.

## Definition geometry and structure

### Architecture and interface contract

- Which functional elements map to which physical components and BOM revisions?
- Which interface endpoints, reference frames and mating conditions must agree?
- Which external interface dependency remains unresolved and blocks release?

Candidate fields: logical/physical mapping; BOM occurrence references; interface
ID/revision; coordinate frame; connector/mating predicate; unresolved dependency.

### Geometry, material and semantic PMI

- Which geometric features carry the nominal dimensions, datums and tolerances?
- Is an annotation machine-interpretable PMI or only a graphical presentation?
- Which units, material specification, surface conditions and measurement
  conventions qualify the intended values?

Candidate fields: feature ID; geometry representation; dimension and unit;
datum system; tolerance expression; PMI semantic status; material/surface refs.

## Behavior and assurance

### Functional envelope and failure assumptions

- What functions and modes are intended under which loads and environments?
- Which failure modes, prohibited uses and interface limits constrain the design?
- Which declared capability still lacks analysis or test evidence and must not
  be treated as certified safe operation?

Candidate fields: functional class; modes; preconditions; expected outputs;
load/environment envelope; hazard/failure references; qualification status.

### Design verification and validation

- What demonstrates that the definition satisfies its allocated requirements?
- What separately demonstrates that the selected solution meets stakeholder
  intent in the intended use context?
- Which design revision, analysis assumptions and unresolved findings limit
  each result, without claiming the manufactured item was verified?

Candidate fields: assurance kind; target design revision; method; acceptance
criterion; stakeholder context; evidence; assumptions; finding disposition.

## Controlled change and realization

### Review, release, change and effectivity

- Who may approve this release and which unresolved findings prevent approval?
- What changed between revisions, why, and which dependent definitions need review?
- For which dates, variants, production contexts or serial ranges is the
  revision or approved deviation applicable?

Candidate fields: approval authority; review gate; change-set; expected-base
digest; impact analysis; applicability predicate; deviation authority and scope.

### Manufacturing and inspection handoff

- Which build-to and inspect-to documents and tooling references accompany release?
- Which receiving organization acknowledged which exact package revision?
- Which as-built differences are approved deviations and which require an
  engineering change rather than silently rewriting the intended definition?

Candidate fields: handoff manifest; recipient/purpose; acknowledgement receipt;
tooling/process/inspection refs; as-built discrepancy; disposition/change links.

## Governed exchange and preservation

### Technical stewardship, access and retention

- Who owns the definition and who merely stores or consumes its representations?
- Which proprietary or restricted fields may cross a Dimension boundary for
  the declared purpose and recipient?
- What must remain readable after tool obsolescence or product retirement,
  and which retention holds prohibit deletion?

Candidate fields: master/steward/custodian refs; disclosure scope; policy;
retention trigger; legal hold; preservation representation; tombstone reference.

### Transformation and engineering fidelity

- Which native and neutral schema releases and translator versions produced
  this exchanged representation?
- Which geometry, feature associations, units or semantic PMI were lost or
  degraded even if the rendered model looks correct?
- Which reference fixtures and comparison criteria justify acceptance, and
  when must the receiver reject the package instead of assuming equivalence?

Candidate fields: source/target format and release; transformation trace;
geometry/PMI validation results; explicit loss; acceptance policy; test fixtures.

Every final question should reference declared typed data-element IDs. A later
builder may reuse schema serialization helpers, never generic question text.
