# D7 Tourism & Hospitality

This meta-model describes the world of travel for leisure and its service industry: destinations and attractions, accommodation offers and stays, and the catalogue of experiences visitors consume. It is its own model because tourism joins place (destinations), commerce (offers, grades) and personal movement (stays) into one lifecycle, from listing an offer through booking, arrival and departure, that neither a place model nor a generic commerce model expresses on its own.

## Manifest

```yaml
muif:
  version: "1.0"
metaModel:
  id: "vercy:world:d7"
  csn: world.tourismHospitality
  version: 0.2.0
  displayName: Tourism & Hospitality
  description: Destinations and attractions, accommodation offers and stays, visitor experiences and service quality.
conformance:
  muc: "2.0: Conformant"
  mmas: A1
namespaces:
  - world.tourismHospitality
bundles:
  - csn: world.tourismHospitality.destination
    displayName: Destination
    layers:
      - world.tourismHospitality.destination.destinationProfile
      - world.tourismHospitality.destination.seasonality
  - csn: world.tourismHospitality.stay
    displayName: Stay
    layers:
      - world.tourismHospitality.stay.accommodationOffer
      - world.tourismHospitality.stay.stayRecord
  - csn: world.tourismHospitality.experience
    displayName: Experience
    layers:
      - world.tourismHospitality.experience.experienceCatalogue
      - world.tourismHospitality.experience.serviceQuality
imports:
  - source: unwto
    version: "*"
  - source: schema-org
    version: "*"
```

## Bundles and layers

| Bundle | Responsibility | Layers |
|---|---|---|
| `destination` | Places in their role as visitor destinations | `destinationProfile`: destinations, attractions and their visitor-facing identity · `seasonality`: seasons, capacity and visitor flows over time |
| `stay` | Lodging supply and the fact of staying | `accommodationOffer`: lodging offers, room types, availability · `stayRecord`: bookings, arrivals and departures as facts of the world |
| `experience` | What visitors do and how well it is done | `experienceCatalogue`: tours, activities and packaged experiences · `serviceQuality`: classifications, star grades and quality signals |

## Objects

- `destination`: a place in its visitor-facing role; key attributes: name, territory reference, profile, seasonality pattern
- `attraction`: a visitable point of interest; key attributes: name, type, destination, access conditions
- `accommodationOffer`: a lodging offer by a provider; key attributes: provider reference, facility reference, room types, availability window
- `stay`: the fact of a guest staying; key attributes: offer reference, guest reference, arrival, departure, party size
- `experienceOffer`: a bookable activity or tour; key attributes: name, operator reference, destination, schedule, capacity
- `itinerary`: a planned sequence of stays and experiences; key attributes: owner reference, legs, dates
- `serviceGrade`: an awarded quality classification; key attributes: scheme, grade, awarding body reference, validity
- `visitorFlow`: an aggregate measure of visits; key attributes: destination, period, count, method

## Relationships

- `destination` -> features -> `attraction` (1..n): a destination's attractions define its profile
- `accommodationOffer` -> locatedIn -> `destination` (n..1): every offer belongs to a destination
- `accommodationOffer` -> housedIn -> `accommodation` (n..1): the physical lodging resolves to a structure in the built-environment model (U)
- `stay` -> bookedAt -> `accommodationOffer` (n..1): a stay realizes an offer
- `stay` -> madeBy -> `person` (n..1): the guest resolves to a natural person in H1 under that person's grant
- `itinerary` -> includes -> `experienceOffer` (n..m): itineraries assemble experiences and stays
- `serviceGrade` -> awardedTo -> `accommodationOffer` (n..1): grades attach to specific offers or properties
- `visitorFlow` -> aggregates -> `stay` (1..n): flows are computed from stays with no personal data retained

## Events

- `attractionListed`: an attraction entered a destination's public profile
- `offerPublished`: a provider published or updated an accommodation or experience offer
- `stayBooked`: a booking was made against an offer
- `guestArrived`: a stay began
- `guestDeparted`: a stay ended
- `experienceDelivered`: a booked experience took place
- `gradeAwarded`: a quality classification was granted or renewed
- `seasonOpened`: a destination's season began, changing capacity and availability

## Contracts

- `bookingDataExchange`: provider-to-provider exchange of minimal booking data, guest identity only under the guest's S1 consent
- `destinationStatisticsFeed`: aggregated visitor flows delivered to the statistics office and destination steward
- `catalogueSyndication`: public redistribution of offer and experience catalogues to travel channels

## Projections

- `travellerCatalogue`: offers, experiences and grades for trip planning; omits operational data and all guest records
- `destinationDashboard`: seasonality and aggregate flows for destination management; contains no individual stays
- `qualityRegister`: current grades and their awarding bodies; omits pricing and availability

## Composition

- REFERENCE `world.territoryAndPlace` (P): destinations are roles over territories and places; geography stays sovereign in the place model
- REFERENCE `world.buildingAndFacility` (U): accommodation resolves to physical structures (accommodation_ref)
- REFERENCE `world.organization` (O1): providers, operators and awarding bodies are organizations
- REFERENCE `world.person` (H1): guests are natural persons; stay records link to them only under consent
- REFERENCE `world.sportRecreation` (D5): sporting events and recreational activities surface as visitor experiences
- imports: UNWTO (ALIGN): visitor, trip and stay definitions from international tourism statistics recommendations
- imports: schema.org (ALIGN): TouristDestination, LodgingBusiness and TouristAttraction typing for public catalogues

## Stewardship

Providers own their offers, stays and service records; the territory steward, as a sub-agent for the destination, owns destination profiles and seasonality. Guest-related data is accessible only under the guest's own grant, with all access issued through the catalogue's S1/S2 ownership and access models and audited via S4.
