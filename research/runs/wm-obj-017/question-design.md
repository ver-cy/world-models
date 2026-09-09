# Subject-specific question design

These are candidate questions for synthesis, not a validated specification.

## Identity and applicability

- Does this record describe a partial selection, a solved configuration or a
  released reusable variant, and which transition gives it its release ID?
- Which product-family revision and option-space revision define its meaning?
- Which manufacturer, retailer or standards authority issued each identifier?
- Does the consumer variant share a GTIN with another variant, and which CPV
  qualifier disambiguates it within that GTIN?
- Which configured item instances reference this definition, without importing
  their serial numbers, location or operating state as variant properties?

## Features and choice provenance

- For each feature, was its value explicitly selected, inherited, defaulted,
  calculated or left unresolved, and which rule revision produced the value?
- Are absence, unknown, not applicable and an explicit false value distinct?
- Which values are allowed, in which unit and precision, and how many choices
  may be selected from each option group?
- When a family default changes, which existing variants retain their frozen
  value and which unfinished configurations require reevaluation?

## Constraints and explanations

- Which features require or exclude other features, under what conditions?
- Are compatibility tables exhaustive, and what does a missing combination mean?
- Is the selection complete, merely satisfiable, contradictory, or untested?
- Which exact rule set, solver version and inputs produced the verdict?
- When no solution exists, which conflicting selections and rules explain it?
- Is a suggested substitution technically compatible, commercially available
  and authorized, with each of those conclusions represented separately?

## Direct properties and capabilities

- What nominal dimensions, material, colour, mass and rated performance follow
  from this configuration, with tolerances, units and derivation evidence?
- Which observable features distinguish it from sibling variants, and how
  reliable is recognition from each feature or marking?
- Which actions and interfaces are supported by this variant, within which
  environmental, load, power, software and safety limits?
- Which properties require measurements of the built item rather than a
  conclusion from the reusable definition?

## Composition and release

- Which design revision and BOM selection define this variant, and which
  component alternatives remain unresolved?
- What dates, markets, serial ranges or production contexts limit effectivity?
- Who approved this baseline, against which requirements and test evidence?
- Does a change create a revision of the same variant or a new variant ID?
- Which predecessor remains resolvable after supersession or retirement?

## Interchange and governance

- Which feature values survive a Schema.org or GS1 projection and which rules
  and effectivity expressions cannot be represented there?
- What licensing restrictions apply to imported property dictionaries?
- Which organization controls the definition and can approve local extensions?
- Which selections are commercially confidential or customer-specific?
- What record must remain after deletion so dependent instances retain their
  interpretation without retaining unnecessary personal information?

## Additional inspected sources

- https://www.iso.org/standard/84300.html : ISO official index confirms
  ISO 10303-242:2025 edition 4, August 2025. Supports product-data management
  and engineering context; detailed licensed clauses still require review.
- https://schema.org/ProductModel : official page fetched; preserve the
  distinction between model relationships and ProductGroup membership.
- https://ref.gs1.org/standards/digital-link/uri-syntax/1.7.0/ : official page
  fetched; use GTIN/CPV qualifier scope rather than treating a locator as identity.
- https://docs.oasis-open.org/ubl/UBL-2.4.html : official indexed specification
  distinguishes catalogue item specification updates from pricing updates.
