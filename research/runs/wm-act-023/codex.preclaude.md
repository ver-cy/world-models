# WM-ACT-023 frozen pre-provider dossier

## Identity and boundary

- Registry ID: `vr.wm-act-023`
- Model ID: `WM-ACT-023`
- Name: `Public Health / Epidemiology`
- Record-plane label: `standalone-mm`
- Candidate subject kind: `aggregate`
- Prior catalogue card: `models/society/B14-public-health-and-epidemiology.md`
- Approved outgoing relation ledger: empty; every proposed relation is held for
  later registry reconciliation.

The model owns population and cohort-grain public-health observations,
indicator series, surveillance signals, outbreak determinations, epidemiologic
assessments, immunization programme and coverage aggregates, public-health
measure bindings and evaluation results. It must not become a person health
record, clinical-care model, laboratory master, identity register, pathogen or
genomic sequence repository, geographic master, policy authoring system,
resource deployment workflow or legal adjudication record.

Privacy language must not promise that simple de-identification is sufficient.
Small cells, rare combinations, location-time granularity, linkage and repeated
releases may remain re-identifiable. The adopting Dimension must bind a
disclosure-control profile and preserve suppression or transformation lineage.

## Existing conceptual structure to test

The earlier card identifies surveillance, outbreaks, immunization and measures.
Research should test and deepen these areas rather than copy them mechanically:

1. Scope, populations, geography and time.
2. Indicator definition, denominator, stratification and series revisions.
3. Case definition, notifiable aggregate intake, data quality and delays.
4. Signal detection, verification and situation assessment.
5. Outbreak identity, declaration, extent, transmission, severity and closure.
6. Immunization programme, product or dose semantics, coverage and equity.
7. Public-health intervention, authority, target population and effectiveness.
8. Provenance, uncertainty, privacy, access, retention, federation and
   international reporting.

## Source priorities

Prefer current official material from WHO, World Health Assembly regulations,
CDC, ECDC, HL7 and W3C. Pin versions and distinguish a disease classification,
case definition, exchange resource, surveillance method and legal reporting
obligation. Use RFC 3339 for event timestamps with seconds and offset.

## Adversarial checks

- Do not store identifiable patient records or claim that an aggregate is
  anonymous merely because names were removed.
- Do not treat a reported case, confirmed case, signal, event and declared
  outbreak as synonyms.
- Keep event time, report time, specimen time, detection time, publication time
  and knowledge time distinct.
- Keep counts, rates, ratios, risks, proportions and modelled estimates distinct
  and retain numerator, denominator, unit, method and uncertainty.
- Do not universalize case definitions, outbreak thresholds, severity scales,
  vaccination schedules, public-health powers or reporting deadlines.
- Separate observed association, causal claim, forecast, scenario and policy
  decision.
- Keep statistical revisions and corrections visible rather than overwriting
  earlier releases.
