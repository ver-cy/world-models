from __future__ import annotations

import json
from pathlib import Path

REPO = Path(r"R:\02_PROJECTS\02_Meta_Models_Platforms\Ver.cy\current\ver-cy\world-models")
RUN = REPO / "research" / "enterprise" / "runs" / "em-dat-05"
RUN.mkdir(parents=True, exist_ok=True)

MODELS = {
    "WM-XCT-025": "wm-xct-025-observable-result-fields",
    "WM-DAT-010": "wm-dat-010-time-series-observation-collection",
    "WM-KNW-011": "wm-knw-011-goal-objective",
    "WM-DAT-007": "wm-dat-007-data-quality-assessment",
    "WM-DAT-002": "wm-dat-002-official-statistics",
}

SELECTED = {
    "WM-XCT-025": {
        "measurand-and-observed-property", "value-kind-and-datatype",
        "unit-code-and-code-system", "method-and-procedure-reference",
        "validity-window-and-aggregation-period", "result-status-and-supersession",
        "absent-result-and-nil-reason", "derivation-and-assertion-lineage",
    },
    "WM-DAT-010": {
        "collection-series-id-version-head-status-owner-and-purpose",
        "variable-indicator-observed-property-measure-unit-scale-and-datatype",
        "dimension-key-coordinate-classification-code-list-and-concept",
        "observation-id-series-membership-dimension-key-and-order",
        "result-value-type-unit-precision-resolution-range-and-component",
        "status-flag-missing-not-applicable-suppressed-confidential-and-provisional",
        "phenomenon-reference-effective-validity-instant-interval-and-bounds",
        "aggregation-weighting-index-base-normalization-seasonal-adjustment-and-chain",
        "revision-correction-benchmark-restatement-backcast-retraction-and-supersession",
    },
    "WM-KNW-011": {
        "fd-objective-target-indicator-roles", "fd-measure-binding",
        "fd-target-value-and-baseline", "fd-target-methodology-and-assumptions",
        "fd-time-horizon", "fd-target-restatement",
    },
    "WM-DAT-007": {
        "metric-definition-indicator-formula-direction-scale-unit-and-aggregation",
        "rule-constraint-applicability-threshold-tolerance-severity-and-unknown-policy",
        "method-procedure-query-code-tool-version-parameter-and-precondition",
        "observation-feature-property-procedure-result-phenomenon-time-and-result-time",
        "measurement-value-unit-scale-distribution-uncertainty-confidence-and-limit",
    },
    "WM-DAT-002": {
        "measure-indicator-formula-unit-and-direction",
        "target-observed-population-and-statistical-unit",
        "data-structure-dimensions-measures-and-attributes",
        "series-key-frequency-unit-and-domain",
        "observation-value-status-unit-and-flags",
        "break-correction-backcast-and-discontinuation",
    },
}


def load(slug: str) -> dict:
    path = REPO / "publications" / slug / "spec.yaml"
    text = path.read_text(encoding="utf-8")
    return json.loads(text[text.index("{"):])


def compact_finding(finding: dict) -> dict:
    return {
        "id": finding.get("id"),
        "name": finding.get("name"),
        "description": finding.get("description"),
        "dataElements": [
            {key: element.get(key) for key in ("id", "name", "description", "value_kind", "cardinality", "required") if element.get(key) is not None}
            for element in finding.get("data_elements", [])
        ],
    }


def compact(model_id: str, slug: str) -> dict:
    data = load(slug)
    findings = []
    for bundle in data.get("structure", {}).get("bundles", []):
        for layer in bundle.get("layers", []):
            for finding in layer.get("findings", []):
                if finding.get("id") in SELECTED[model_id]:
                    findings.append(compact_finding(finding))
    adjudication = data.get("researchAdjudication") or {}
    return {
        "publication": data.get("publication"),
        "metaModel": data.get("metaModel"),
        "model": data.get("model"),
        "selectedFindings": findings,
        "functions": [
            {key: item.get(key) for key in ("id", "name", "description")}
            for item in data.get("functions", [])
        ],
        "composition": [
            {key: item.get(key) for key in ("target", "relation", "purpose", "required") if item.get(key) is not None}
            for item in (data.get("composition") or [])
        ],
        "publicationHolds": adjudication.get("publicationHolds") or [],
    }


dossier = {
    "contour": {
        "id": "EM-DAT-05",
        "name": "Metric, target and observation",
        "scope": "A versioned definition of a measurable quantity, unit, dimensions, population, method, aggregation and comparison direction; observations and target commitments remain distinct records.",
        "questions": [
            "How are periods and populations made comparable?",
            "How are zero, unknown, not applicable, suppressed and missing distinguished?",
            "What happens to identity and comparability when a KPI formula changes?",
        ],
        "invariants": [
            "An observation pins metric definition version, method, period, population and dimension coordinates.",
            "Observed values are not stored as the single current value of a metric definition.",
            "Unit, scale, aggregation, denominator and null semantics are explicit.",
            "A target commitment references a metric definition and does not own its formula.",
        ],
        "acceptanceScenario": "One KPI has two method versions, a missing period and a later recalculation; comparison is preserved only where method, population, unit and dimensions remain compatible.",
        "negativeCase": "Headcount from one population is summed with FTE from another without a declared method or reconciliation.",
        "decision": "Choose REUSE ONLY, PROFILE, EXTEND, or NEW MODEL. Prove any new aggregate has independent identity and lifecycle. Reuse observations, result fields, goals and quality assessments rather than absorbing them.",
    },
    "catalogueSearchFinding": "Several published models explicitly reference an external metric/measure definition authority, while no generic cross-domain metric-definition model was found. WM-DAT-007 owns quality-assessment metrics only; WM-DAT-002 owns official-statistics product semantics only; WM-KNW-011 owns target commitments and explicitly excludes metric definitions.",
    "models": {model_id: compact(model_id, slug) for model_id, slug in MODELS.items()},
}

out = RUN / "provider-dossier.json"
out.write_text(json.dumps(dossier, ensure_ascii=False, indent=2) + "\n", encoding="utf-8", newline="\n")
print(json.dumps({"output": str(out), "bytes": out.stat().st_size}))
