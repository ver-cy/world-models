# N11 Time & Calendar Reference

This meta-model describes humanity's shared machinery for talking about time: time scales and their adjustments, time zones with their offset history, calendar systems and eras, recurrence rules, and the holidays and observances that structure civic and cultural life. It is its own model because temporal reference data is authority-managed and changes by decree (zone redefinitions, proclaimed holidays, calendar reforms), and because nearly every other model embeds intervals, schedules and deadlines that must resolve against it.

## Manifest

```yaml
muif:
  version: "1.0"
metaModel:
  id: "vercy:world:n11"
  csn: world.timeCalendar
  version: 0.2.0
  displayName: "Time & Calendar Reference"
  description: "Time scales, time zones, calendar systems, recurrence rules, holidays and observances."
conformance:
  muc: "2.0: Conformant"
  mmas: A1
namespaces:
  - world.timeCalendar
bundles:
  - csn: world.timeCalendar.timeBase
    displayName: "Time base"
    layers:
      - world.timeCalendar.timeBase.timeScaleAndEpoch
      - world.timeCalendar.timeBase.timezoneAndOffset
  - csn: world.timeCalendar.calendar
    displayName: "Calendar"
    layers:
      - world.timeCalendar.calendar.calendarSystemAndEra
      - world.timeCalendar.calendar.recurrenceAndScheduling
  - csn: world.timeCalendar.observance
    displayName: "Observance"
    layers:
      - world.timeCalendar.observance.publicHoliday
      - world.timeCalendar.observance.culturalObservance
imports:
  - source: iso-8601
    version: "*"
  - source: iana-tz
    version: "*"
  - source: rfc-5545-icalendar
    version: "*"
```

## Bundles and layers

| Bundle | Responsibility | Layers |
|---|---|---|
| `timeBase` | Physical and civil time | `timeScaleAndEpoch`: time scales, epochs, leap adjustments Â· `timezoneAndOffset`: zones, offsets, transition history |
| `calendar` | Structuring days into systems | `calendarSystemAndEra`: calendar systems, eras, intercalation Â· `recurrenceAndScheduling`: recurrence rules and scheduling primitives |
| `observance` | Days that matter to people | `publicHoliday`: jurisdictional public holidays Â· `culturalObservance`: religious and cultural observances, seasons |

## Objects

- `timeScale`: a reference scale for instants; key attributes: scaleId, epoch, leapPolicy.
- `timezone`: a civil time zone; key attributes: tzId, standardOffset, territoryRef.
- `offsetTransition`: one historical or scheduled change of a zone's offset; key attributes: effectiveAt, offsetBefore, offsetAfter, reason.
- `calendarSystem`: a system for structuring days into years; key attributes: calendarId, calendarType, intercalationRule.
- `era`: a named epoch within a calendar system; key attributes: eraName, calendarRef, epochDate.
- `recurrenceRule`: a rule generating recurring dates; key attributes: ruleExpression, frequency, exceptions.
- `holiday`: a jurisdictionally proclaimed day; key attributes: name, jurisdictionRef, dayOffStatus, firstObservedYear.
- `observance`: a cultural or religious recurring day; key attributes: name, tradition, movableFlag, computationMethod.

## Relationships

- `timezone` -> definedAgainst -> `timeScale` (N:1): civil offsets are relative to a scale.
- `offsetTransition` -> amends -> `timezone` (N:1): the zone's rule history.
- `era` -> partOf -> `calendarSystem` (N:1): eras belong to their calendar.
- `holiday` -> scheduledBy -> `recurrenceRule` (N:1): how the holiday's date is generated.
- `observance` -> computedIn -> `calendarSystem` (N:1): movable observances compute in their own calendar.
- `holiday` -> derivedFrom -> `observance` (N:1): public holidays often formalize an observance.

## Events

- `leapSecondScheduled`: an adjustment to the time scale was announced.
- `timezoneRuleChanged`: a jurisdiction redefined its zone or daylight rules.
- `calendarReformAdopted`: a jurisdiction or community adopted a calendar change.
- `holidayProclaimed`: a new public holiday was declared for a jurisdiction.
- `holidayRescinded`: a public holiday was removed or replaced.
- `annualCalendarIssued`: the authoritative holiday calendar for a year was published.

## Contracts

- `referenceDataSubscriptionContract`: subscription terms for consuming zone, calendar and holiday updates.
- `redistributionContract`: terms for republishing this reference data inside other products.
- `workingDayFeedContract`: service terms for computed working-day and deadline calendars per territory.

## Projections

- `tzCompatibleExport`: zone and transition data in tz database shape; omits holidays and observances.
- `workingDayCalendarView`: business days per territory and year combining holidays and weekend rules; omits transition history.
- `upcomingObservancesFeed`: the next occurrences of holidays and observances; omits rule internals.

## Composition

- EMBED (offered): temporalInterval and recurrenceRule are value-object shapes that sibling models embed wherever periods, schedules and deadlines occur.
- REFERENCE `world.place` (P1): the jurisdictions and territories where zones and holidays apply.
- REFERENCE `world.identifierNaming` (N8): zone and calendar identifiers are registered schemes.
- REFERENCED BY `world.officialStatistics` (N10) and `world.reportStatement` (N2) for reference periods, and by `world.documentRecord` (N1) for retention triggers.
- imports: iso-8601 (ALIGN): representation of dates, times, intervals and durations.
- imports: iana-tz (REFERENCE): the zone registry mirrored by the timezone layer.
- imports: rfc-5545-icalendar (ALIGN): recurrence rule semantics.

## Stewardship

The neutral owner archetype is a reference data steward at class level, with jurisdictional facts (zone rules, holidays) owned by the declaring authorities they describe. Access is open by default for reference data but always formally granted through the catalogue's S1/S2 ownership and access models, with redistribution audited via S4.
