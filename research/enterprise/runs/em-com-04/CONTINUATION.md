# EM-COM-04 continuation

## State

Research contour: **Customer inquiry and service request**. The primary candidate is WM-ACT-021 Service Case / Ticket.

Claude and Grok independently selected **PROFILE, no new aggregate**. Both confirmed existing coverage for merge/history, incident separation and resolution-versus-closure-versus-acceptance. Both found one narrow profile-level gap: intentional anonymous requester mode is different from an unknown requester.

The exact Grok prompt, raw response, provider comparison and frozen response manifest are preserved. The minimal English adoption binding is in `profile-binding/0.1.0/`. It allocates no model/runtime ID and contains no executable code.

## Holds

- WM-ACT-021 outgoing sibling relations are not approved in the relation ledger.
- WM-KNW-014 declares a CHILD relation to WM-ACT-021 while describing that target as an action/work authority, which conflicts with the actual service-case boundary.
- WM-ACT-027 permission-reference requiredness may not align with optional case-level communication bindings.
- Upstream models remain reviewable drafts.

## Publication decision

Publish the bounded research profile as an EM-COM-04 adoption/mapping artifact linked from the Enterprise card. Do not present it as canonical or installable. Canonical publication remains held until parent assurance, sibling relations and the WM-KNW-014 contradiction are resolved.
