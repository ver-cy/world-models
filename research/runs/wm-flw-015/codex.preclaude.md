# Codex pre-provider hypothesis for WM-FLW-015

## Boundary

Resource Consumption should be an event aggregate for one source-qualified use
assertion over an interval. It owns consumption identity, measurement boundary,
qualified quantity, derivation or allocation method, component flow references,
performance context, evidence and correction lineage. Resource, inventory,
meter, observation, activity, asset, facility, invoice, ledger, emissions,
footprint, impact and evidence lifecycles remain external.

## Proposed structure

1. Consumption identity, class and boundary.
2. Quantity, units, measurement and derivation.
3. Gross, returned, recovered, exported, lost and net flow components.
4. Consumer, activity, interval, allocation and normalization.
5. Lifecycle, reconciliation, baseline, target and performance.
6. Governance, evidence, access and interoperability.

Each bundle should contain two layers and four findings. Each finding should ask
three model-specific questions and define one data element and one serial
evidence artifact. Ten functions should register an assertion, bind consumer and
resource, define boundary and interval, record measurement, derive quantity,
allocate shared use, reconcile sources, evaluate baseline or target variance,
correct or supersede and project an authorized standards view.

## Expected hard points

- Water withdrawal, use, consumption and discharge are not aliases.
- Power and energy are different quantities; fuel, materials and water require
  their own profiles and conversion rules.
- Meter reading, counter delta, allocated value, invoice quantity and reported
  consumption are different assertions.
- Gross and net consumption require an explicit system boundary and treatment of
  returns, recovery, exports and losses.
- Cost, emissions, footprint and impact are external derived contexts.
