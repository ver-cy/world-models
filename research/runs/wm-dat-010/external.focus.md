# WM-DAT-010 bounded provider focus

Research one governed Time Series / Observation Collection specification for an
ordered, versioned collection of observations. Freeze the title ambiguity: the
root is the collection and series-definition aggregate, not an individual
observation, sensor, statistical unit, dataset distribution, forecast model or
analytics result. Keep the series definition, observation, phenomenon/reference
time, result time, release, vintage/revision, source, procedure, feature of
interest and dataset as independently identifiable concepts and lifecycles.

The root owns series identity, version, key and status; variable, indicator,
measure and unit bindings; dimensions and classifications; ordered observation
membership; values, flags, status and missingness; reference periods, instants,
intervals, frequency, calendars and time zones; observation, result,
availability, release, revision, vintage, recorded, ingestion and knowledge
times; population, spatial and domain coverage; sampling and granularity;
aggregation, weighting, index bases, normalization and seasonal adjustment;
forecast/scenario qualifiers; uncertainty and confidence; collection method,
sensor/procedure/feature bindings; provenance, lineage, validation, quality,
anomalies, gaps, corrections and restatements; lifecycle, access, retention,
distribution and interoperability projections. It does not autonomously ingest,
recalculate, revise, publish, certify, change units or dispose observations.

Known registry context:

- registry_id: vr.wm-dat-010
- parent signal: WM-MAT-008 (unresolved boundary signal, not asserted ownership)
- purpose: ordered observations with sampling semantics
- owner archetype: data product owner or data steward
- no frozen relation row exists; composition signals remain visible holds

Target 6 bundles, 12 layers, 24 findings, 72 discriminating questions, at least
24 artifacts and 10 functions. Prefer current primary official sources from
SDMX, W3C, OGC, UNECE, IETF, ISO public metadata, DataCite, HL7 and domain
standards. Pin versions, distinguish observed estimates from forecasts and
revisions, and declare all projection loss.

Agents must not autonomously ingest or alter source readings, impute values,
change a series key or unit, revise or suppress observations, publish a release,
certify quality, infer protected traits, widen access, override retention/legal
holds or dispose records without delegated authority.
