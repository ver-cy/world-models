Research only contact-point identity and channel endpoints for WM-PER-010
Contact Point / Party Profile.

- Use the exact registry identity and output `entry_kind` `mixin`. This is a
  reusable contact-profile component attached to a person, organization or
  other party; it is not the party identity itself and not a communication
  event or message.
- The `model` block must describe the boundary of the final combined
  WM-PER-010, not merely this split pass. Its purpose, scope statement,
  in-scope list, out-of-scope list and boundary notes must include the complete
  channels + preferences + governance model. Assigned split areas must never
  appear in `out_of_scope`, and the scope statement must not say "this pass".
- Cover stable contact-point identity and owning-party reference; endpoint
  type and purpose; telephone, email, postal, web/URI, messaging and comparable
  addressable channels; canonical and display forms; internationalization;
  verification assertions; validity interval; operational reachability and
  supersession. Keep message content and delivery attempts out of scope.
- Distinguish this mixin from WM-XCT-024 Contact Point if the registry boundary
  is unresolved, from WM-PER-001 party/person identity, postal-address or place
  models, identity credentials, communication/message events, consent/legal
  basis records and customer/account relationships. Record unresolved overlap
  as a conflict or gap rather than inventing a frozen relation.
- Target 2-3 bundles, 5-7 layers and 10-13 findings with 3-5 discriminating
  questions each. Use at least eight distinct question kinds.
- Every local ID, including bundle, layer, finding, question, data element,
  artifact and function IDs, must begin with `cp-chan-`.
- Limit functions to registering, verifying, normalizing, resolving and
  superseding channel endpoints. Provide complete schema-valid service_layers
  and coverage objects, but keep them concise; the merger takes canonical
  service layers from `governance`.
- Prefer primary standards and first-party specifications such as ITU E.164,
  IETF email/URI/IDNA work, Universal Postal Union addressing guidance and
  W3C vocabularies where their actual scope supports a claim.
