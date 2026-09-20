# WM-ACT-030 source notes

Accessed 2026-09-06. This fallback uses official primary publishers. ISO source
pages are explicitly marked abstract-only and do not support a conformance
claim.

- ISO 21500 and ISO 21502 establish the project, programme and portfolio
  neighborhood but do not define a universal Initiative class.
- The Open Group exchange schema keeps CourseOfAction, Goal, Outcome,
  Capability, WorkPackage, Deliverable, ImplementationEvent, Plateau and Gap
  distinct. This supports an initiative crosswalk without making Initiative
  identical to one ArchiMate element.
- IATI Activity supplies a broad intervention profile with stable identity,
  organizations, scope, status, dates, locations, classifications, budgets,
  transactions, related activities, conditions and results. Its lifecycle also
  separates pipeline, implementation, finalisation, closure, cancellation and
  suspension.
- HM Treasury Green Book and business-case guidance ground case for change,
  strategic fit, option generation and appraisal, costs, benefits, risks and
  staged decisions.
- European Commission PM2 grounds the formal Project boundary, governance,
  lifecycle, phase gates, activities and artifacts.
- W3C ActivityStreams supplies generic activities, actors, objects, targets,
  results, instruments, contexts and collections. W3C PROV-O supplies
  responsibility, generation, derivation, revision and attribution.
- OECD results guidance separates inputs, activities, outputs, outcomes and
  impacts and requires indicators, baselines, targets, sources, assumptions and
  risks.
- NIST Privacy Framework and UK National Archives guidance ground privacy-risk
  governance, retention and responsible disposition.
- RFC 3339 supplies timestamps with seconds and an explicit offset or Z.

The Vercy Initiative root is intentionally an aggregate with a controlled
membership and transition boundary. Formalization into Project, Program,
Campaign or Operation creates a new identity and an attributable derivation;
it never silently renames the Initiative.
