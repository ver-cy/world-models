# External research focus: WM-ECO-023 Reservation / Booking

Research one governed reservation or booking aggregate that requests, temporarily holds, confirms, changes, cancels or releases capacity for a specified subject, service, resource, place or time. The aggregate may have travel, accommodation, mobility, event, restaurant, appointment, equipment, facility and general resource profiles; do not silently universalize any one sector.

## Frozen root boundary

The reservation owns its identity and version; booking profile; requester, booker, provider and beneficiary role bindings; reserved subject and capacity references; party count, quantity, allocation, slot and preference assertions; request, offer or quote, hold, waitlist, confirmation, modification, cancellation, expiration, no-show, check-in and fulfilment bindings; policy acknowledgements, notices, evidence and provenance.

Keep these identities external: party, account, resource or inventory item, capacity ledger, product or service offering, availability observation, schedule or calendar event, location, offer or quote, contract, order, ticket, entitlement, invoice, payment method, payment transaction, fulfilment, check-in, attendance, service execution, support case and records disposition. A reservation references these masters and must not duplicate their authoritative lifecycle.

Separate request from availability lookup, quoted terms, provisional hold, confirmed booking, contract formation, ticket or entitlement issuance, payment authorization, actual capacity allocation and service fulfilment. Confirmation does not prove payment, entitlement, attendance, delivery, legal validity or fitness. A cancelled or expired reservation does not prove resource release until the owning capacity system records it.

Separate desired, offered, held, confirmed, modified, waitlisted, cancelled, expired, checked-in, fulfilled, no-show, observation, ingestion and knowledge times. Record start and end with timezone or location context, booking cutoff, hold expiry, cancellation deadline and modification window. RFC 3339 timestamps require seconds and explicit offset or Z.

## Required research outcomes

- Resolve reservation versus availability, hold, appointment, calendar event, offer, contract, order, ticket, entitlement, payment, allocation and fulfilment boundaries.
- Cover instant confirmation, request-to-confirm, provisional hold, waitlist, recurring or multi-segment, group, pooled-capacity and open-time profiles.
- Cover reserved units, party composition, beneficiaries, segments, seats, rooms, tables, slots, preferences, accessibility needs, dependencies and alternatives by reference.
- Cover capacity guarantees, overbooking, allocation state, source system, inventory class, quota and release semantics without owning inventory masters.
- Cover quoted price and deposit bindings, guarantee or payment-policy references, taxes, fees, cancellation or no-show charges and refunds without owning financial masters.
- Cover modification, split, merge, transfer where permitted, cancellation, expiry, no-show, check-in, fulfilment link, dispute, correction, access, privacy, retention and evidence.
- Provide 6 bundles, 12 layers, 24 model-specific findings, at least 72 discriminating questions, artifacts and 10 safe functions.

Use primary official sources where possible and pin editions or effective dates. Include UN/EDIFACT reservation request and response semantics, Schema.org reservation vocabulary, a current domain booking or appointment standard, consumer booking obligations where applicable, and general provenance, policy, time and API projections. Do not fabricate conformance or legal conclusions. Agents may not autonomously create binding bookings, commit scarce capacity, accept terms, charge or refund funds, disclose sensitive itinerary or attendance data, cancel, transfer or dispose records without delegated authority.
