# External research focus: WM-DAT-005 Data Pipeline

Research one governed reusable Data Pipeline definition as an executable
transformation graph and operations lifecycle, not an execution run, dataset,
data product, lineage event, source code, deployment, scheduler, credential,
quality observation, incident or records master.

## Frozen registry context

- Registry ID: `vr.wm-dat-005`
- Model ID: `WM-DAT-005`
- Catalogue kind: `standalone-mm`
- Record plane: `world-model`
- Purpose: executable transformation graph and operations lifecycle
- Owner archetype: data product owner or data steward
- Unified parent signal: `WM-ACT-003 Process / Workflow`
- Candidate relations: `WM-DAT-005 CONTAINS WM-ACT-053 Data Processing
  Job / Pipeline Run` and `WM-DAT-005 COMPOSE WM-DAT-006 Data Lineage`.
  Neither edge is approved or grants ownership.

## Boundary questions

- Separate reusable pipeline definition, release, deployment, schedule, trigger,
  run, task attempt, input/output data, lineage event and quality observation.
- Represent a typed directed graph of sources, transforms, sinks, ports,
  dependencies, conditions, subpipelines and data contracts.
- Preserve code, query, configuration, parameter, schema, container, dependency,
  environment and secret references without absorbing their masters.
- Distinguish expected static lineage from observed runtime lineage and keep
  lineage production externally owned.
- Cover validation, quality, observability, SLO, access, privacy, security,
  resilience, change control, release, deprecation and loss-aware projections.

## Required breadth

Target 6 bundles, 12 layers, 24 findings, 72 questions, 24 serial artifacts and
10 governed functions. Include graph and contracts; logic and configuration;
schedule and execution policy; lineage and quality; telemetry and SLOs;
security, privacy and resilience; lifecycle, governance and interoperability.

## Safety constraints

Do not autonomously deploy, run, backfill, replay, change production schedules,
rotate credentials, widen access, publish data, delete outputs or close incidents.
Require delegated authority, dry-run and impact checks for material operations.
Use RFC 3339 timestamps with seconds and explicit offset or Z.

