# WM-FLW-015 bounded external research focus

Produce one complete schema-valid result for `WM-FLW-015 Resource Consumption`.

Treat the root as one governed consumption assertion: a consumer actor, asset,
facility, process, activity or project used a qualified quantity of a resource
during a defined interval and measurement boundary. Keep consumption distinct
from stock, availability, intake, withdrawal, receipt, return, discharge,
recovery, export, loss, meter reading, invoice, cost, emissions, environmental
impact, forecast and target. Require an explicit assertion kind for metered,
derived, allocated, estimated, modeled, planned or corrected consumption.

Cover stable identity and revision; consumer, resource, activity, asset, process,
facility and place references; system and organizational boundary; interval and
all relevant clocks; gross intake, return, recovery, export and loss components;
net consumption; quantity, unit, precision, tolerance and uncertainty; meter,
counter, sensor, observation and calibration references; counter delta, rollover,
conversion and derivation; shared-resource allocation and functional units;
energy, water, fuel and material profiles; baseline, normalization variables,
energy or resource performance indicator, intensity, efficiency, target and
variance; provenance, evidence, quality, correction, reconciliation, access,
retention and loss-aware interoperability.

Keep resource, product, stock position, meter, sensor, observation, actor, asset,
activity, process, project, facility, place, invoice, cost, ledger, emissions,
footprint, impact, waste, recovery, plan, target, document and evidence as
external masters. Do not infer ownership from consumption, efficiency from low
absolute use, emissions from energy quantity without a factor and boundary, or
truth from one meter, invoice, estimate or report.

Review, but do not automatically approve, candidate parent `WM-FLW-008
Mass-balance / Material Flow`. Treat consumption as a use-side assertion that
can participate in a balance without becoming the entire balance. Preserve the
missing canonical relation as a hold.

Target 6 bundles, 12 layers, 24 findings, 72 questions, 24 artifacts and 10
functions. Prefer ISO 50001, ISO 50006 and ISO 50015; ISO 14040, ISO 14044,
ISO 14046, ISO 14051 and ISO 14052; UN SEEA physical-flow, energy, water and
material-flow accounts; UN/CEFACT units; SOSA/SSN, OGC SensorThings, QUDT and
UCUM; RFC 3339; PROV-O, DQV and ODRL; and current GRI materials, energy and
water standards. Pin versions or access dates. Keep reporting, sector,
jurisdiction, allocation, billing, accounting, emissions and impact profiles
explicit.
