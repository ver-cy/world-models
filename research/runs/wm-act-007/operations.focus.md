Research only planning bindings, resource requirements, execution interfaces and acceptance interfaces for WM-ACT-007 Work Order.

- Keep the work order as aggregate root and use exact registry identity.
- Cover priority and planned window; dependencies and release conditions; permit, safety and quality constraints; responsible-party assignment; personnel capability requirements; equipment, physical asset and material requirements; estimates and cost bounds; dispatch and acknowledgement; completion-claim references; acceptance or rejection interfaces; deviations and escalation.
- Contained tasks are references under candidate `CONTAINS WM-ACT-006`; never duplicate task execution semantics. Procedures, schedules, inventory, people, organizations, contracts, performed work and evidence remain referenced models.
- The model block must describe the complete final model, while structure and functions remain limited to this pass.
- Target 2-3 bundles, 5-7 layers and 10-13 findings with 3-5 questions each.
- Every local ID must begin with `wo-ops-`.
- Use at least eight question kinds. Functions may bind requirements, release/dispatch, attach completion claims and evaluate declared acceptance criteria, but cannot execute work.
- Provide complete required service_layers and coverage objects concisely; governance owns merged service layers.
- Prefer primary ISA-95/IEC 62264, OPC UA ISA-95 Job Control, OASIS PLCS and relevant safety/maintenance standards.
