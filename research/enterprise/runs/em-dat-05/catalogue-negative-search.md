# EM-DAT-05 catalogue boundary search

## Result

No published cross-domain Metric Definition authority was found.

The search covered publication specifications and registry/planning records for `metric definition`, `indicator definition`, `KPI`, `target value`, `measurement method`, and `performance indicator`, followed by full-spec boundary inspection of the five closest models.

## Closest published models

- **WM-XCT-025 Observable Result Fields**: a mixin describing an individual reported result. It references procedure and unit authorities and explicitly excludes method authoring, unit governance and observation-act lifecycle.
- **WM-DAT-010 Time Series / Observation Collection**: owns collection and series identity, observation membership, values, vintages and revisions. It treats variable, indicator, measure, unit, classification, population and procedure as external authorities.
- **WM-KNW-011 Goal / Objective**: owns target commitments and explicitly excludes indicator/metric definitions and computation methods. Its required reference points to an identifier still to be assigned by the registry.
- **WM-DAT-007 Data Quality Assessment**: owns a reproducible quality assessment and its quality-specific metric/rule context. It is not a general business or scientific metric registry.
- **WM-DAT-002 Official Statistics**: owns official-statistics product semantics under an authority and explicitly excludes universal domain indicator catalogues.

## Corroborating references

Several other published models carry metric-definition references or domain-local metric descriptions, including WM-ORG-003, WM-ORG-004, WM-ACT-028, WM-ACT-029, WM-ACT-030, WM-AI-003 and WM-AI-009. These are consumers or bounded domain owners; none is a portable cross-domain definition master.

## Identifier reservation check

Do not assign an identifier from the apparent numeric gaps. WM-DAT-003 is reserved for Map Product, WM-DAT-011 for Knowledge Graph and WM-DAT-012 for Synthetic Data Product. The eventual identifier must be allocated through the registry workflow after the boundary is accepted.
