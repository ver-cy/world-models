# EM-WRK-02 — Grok independent review

## Verdict

Conditional / revise. Reuse of WM-ACT-005 as Project, ProjectCharter as its serial revisioned authorization artifact, WM-ACT-032 profiled as ProjectChangeRequest, 005 change control reduced to a register projection plus baseline-transition link, and many-to-many project–product and project–tracker-container relations is coherent. Do not accept the baseline split or the combined WM-ACT-031 union as specified. Catalog text for the four types is not in hand; reuse fitness is unconfirmed. This review is not a complete catalog.

## Identity / mastership

WM-ACT-005 masters project identity, the current-package pointer, historical package identities, and the charter binding. ProjectCharter is not a second identity. WM-ACT-008 masters living plan/schedule content, forecasts, actuals and computations, and must also expose frozen revisions if packages are to remain readable. WM-ACT-032 masters change-request instances. WM-ACT-031 masters the reused result/event objects if kept. Product and tracker-container are external; 005 does not master them. Three revision axes exist and must not collapse: charter series, baseline-package series, working-plan series. Split-brain risk: “current baseline finish date” answered from an 005 package field versus an 008 schedule field. Declare one query path: approved numbers come from the current 005 package; working/forecast/actual numbers come from 008.

## Project / charter

Keep ProjectCharter as the serial revisioned authorization artifact of WM-ACT-005. It authorizes existence, sponsor intent, authority, funding envelope and success criteria. It is not the living plan and not the performance measurement baseline. At most one current-authorized charter per project; prior revisions retained. Charter revision ≠ baseline transition. Revise the charter only when the authorization envelope changes. An ordinary rebaseline must not force a charter revision. A charter revision that changes the envelope should usually require a subsequent new baseline, but do not auto-mint a package on every charter revision. A package that exceeds its current charter is invalid.

## Plan / forecast / baseline / actual

The 005-package / 008-content split is the right configuration-management pattern—authorized frozen package versus working content—and is unsafe as specified.

The proposal gives 005 a package label and 008 the substance, with no pin or snapshot contract. Working 008 objects are mutable. If a package only references live heads, BL-2 creation leaves BL-1 aliasing the same rows; BL-1 meaning is rewritten and the required scenario fails. Shared-tracker use makes this worse: a P1 package that pins “the tracker plan” rather than a project-scoped selection can move P2’s currentness.

Required contract, still using only the named types: 005 owns package identity, approval state, effective interval, predecessor link (BL-1→BL-2), frozen reference set, and current-package pointer. 008 owns the working graph, forecast and actual series, and computations. Packages cite immutable 008 revisions, or freeze-copy them; they do not cite live heads. Actuals and forecasts never write into an approved package. 008 may cache pinned values for locality; the cache is not authorization-authoritative. Every variance/EVM computation on 008 must take an explicit baseline-package id and read that package’s pins, never “current plan.”

BL-2 creation is one transition: freeze snapshot → mint package → switch current pointer → leave BL-1 immutable. Cross-master atomicity of that sequence is unspecified and is a blocker. Package grain is also unspecified. An atomic performance-measurement package blocks partial rebaseline of scope, schedule or cost; if separable packages are intended, say so. Working, forecast and actual objects must never themselves be the baseline.

## Milestone / deliverable / acceptance

Combined reuse of WM-ACT-031 is the weaker part of the proposal.

Milestone, Deliverable and Acceptance are different kinds. A milestone is a temporal control point or gate and may have zero deliverables and no product. A deliverable is a work product to be produced. Acceptance is a governance decision record: basis, authority, evidence, outcome. Cardinality differs: one deliverable can have many acceptances; one acceptance can cover several deliverables; a milestone may gate many deliverables. Lifecycles differ: reached/missed versus produced/revised versus approved/rejected/waived/withdrawn.

The scenario requires existing acceptance bases to survive BL-2. If Acceptance is the same row as the Deliverable or Milestone, a BL-2 revision of that row rewrites the BL-1 basis. If acceptance criteria resolve to “current baseline,” historical acceptances silently retarget. Shared product across two projects makes a single 031 row unsound: project-specific milestone dates, criteria and acceptance authorities must not live on the shared product object.

Reuse WM-ACT-031 only if it is already an abstract or generic controlled-result type and is used as a supertype with a mandatory kind discriminator, disjoint relation sets, and Acceptance as a separate immutable record that pins object revision + criteria revision + package id. Otherwise split Acceptance off 031. This review does not invent a replacement type. Acceptance is closer to an authorization act than to plan content; it should not be baselined as if it were schedule substance.

## Change request

Profiling WM-ACT-032 as ProjectChangeRequest, and reducing WM-ACT-005 change control to a register projection plus a baseline-transition link, is the cleanest part of the proposal—if 032 is already a change-request type, which cannot be confirmed here.

The 005 register must be a pure projection of 032, not a second writable log. The transition link is conditional: not every approved 032 creates BL-n+1; only rebaseline-class requests do. Approval time ≠ implementation time. Approval authorizes a transition; it does not itself mutate 008 or overwrite BL-1. Rejected requests remain on the projection.

Initial BL-1 must be an explicit path, typically charter-authorized first package, not a synthetic 032 and not a silent side effect of project creation. After BL-1, only an approved 032 may add a package. A request that exceeds the current charter envelope must require a charter revision; an in-envelope request must not. One 032 against a shared product may need coordinated transitions on more than one project; that rule is missing.

## Product / tracker relations

Keep both relations many-to-many. A tracker-container is a work container, not project identity. A product is an asset, not project identity. Sharing a tracker or a product must not imply shared charter, shared package, shared register or shared acceptances. Project–product and project–tracker links need a role (produces / enhances / consumes; manages / contributes). Shared tracker items must be project-attributable so actuals do not double-count. Package membership is a project-private selection over 008 content, not “the tracker’s plan.” Conflict ownership when two projects baseline different claims on one product is unspecified.

## Lifecycle

Project: initiated → authorized (Charter Rev1) → planned → BL-1 approved → executing / controlling → optional change-pending → re-baselined → closing → closed / cancelled / suspended. Package: draft snapshot → submitted → approved (immutable) → superseded (immutable). 032: draft → assessed → approved or rejected → implemented → closed. 008 working content is always current; history exists only through pins or snapshots. Charter series and package series run in parallel. Do not overload project state with charter state or baseline state. Prior acceptances remain historical facts after BL-2 and reopen only if the change request says so.

## Scenario

Two projects, P1 and P2, share one tracker-container and one product. P1 holds an approved BL-1 and acceptances against that basis. An approved P1 change creates BL-2.

Must hold: P1 current package is BL-2; BL-1 remains readable and immutable; 008 revisions cited by BL-1 do not mutate; P1 acceptances stay bound to the BL-1 basis; P2 charter, packages, register and acceptances are untouched unless the request explicitly names a P2 impact; product and tracker identities remain single and unowned by either project; P1 working plan may move, P2 overlay does not; P1 register shows the request and the BL-1→BL-2 link; P2 does not project P1’s request; P1 forecasts after transition compare to BL-2; historical variance against BL-1 remains computable; tracker items stay distinguishable by project; no duplication of tracker items.

## Invariants

Non-exhaustive. Project identity is stable across charter revisions and packages. One current-authorized charter per project. One current approved package per project; prior packages append-only, superseded not deleted. Package references pin revisions, not live heads. Charter serial ≠ package serial ≠ working-plan serial. 008 working content is not the performance baseline. Actuals and forecasts never mutate approved packages. 008 computations declare a package id. Acceptance basis includes package id and pinned revisions; later packages do not rewrite it. After initial BL-1, only an approved 032 may add a package. 005 register is a projection of 032 plus optional transition links. Many-to-many product and tracker relations do not share authorization artifacts. Shared tracker/product mutation is not an implicit project change. Milestone, deliverable and acceptance remain distinguishable even if all reuse WM-ACT-031.

## Blockers

(1) No 008 immutability or pin contract for 005 packages. (2) No cross-master atomicity for freeze → mint → switch-current. (3) Package grain unspecified. (4) Variance read-path unspecified. (5) WM-ACT-031 union lacks a kind discriminator and an acceptance-stability rule. (6) Acceptance-basis pinning unspecified. (7) Unknown whether the 008 graph is project-scoped or tracker-scoped. (8) Dual-log risk if the 005 register is stored rather than projected. (9) Initial BL-1 authorization path unspecified. (10) No rule for which request class forces a charter revision, and no multi-project impact rule for one 032 on a shared product. (11) Conflict owner when two projects baseline different claims on one product unspecified. (12) Original semantics of WM-ACT-005 / 008 / 031 / 032 not inspectable here, so reuse fitness is unproven.

Keep the reuse map. Condition the baseline split on pin or snapshot, package grain, and a declared variance path. Condition or split the 031 union so acceptance

> Capture note: the browser response ended at the word “acceptance”; the incomplete final sentence is preserved rather than repaired.
