from __future__ import annotations

import json
from pathlib import Path

REPO = Path(r"R:\02_PROJECTS\02_Meta_Models_Platforms\Ver.cy\current\ver-cy\world-models")
RUN = REPO / "research" / "enterprise" / "runs" / "em-dat-01"
RUN.mkdir(parents=True, exist_ok=True)
MODELS = {
    "WM-DAT-001": REPO / "publications" / "wm-dat-001-dataset" / "spec.yaml",
    "WM-DAT-004": REPO / "publications" / "wm-dat-004-data-schema-data-contract" / "spec.yaml",
}
SELECTED = {
    "WM-DAT-001": {
        "dataset-identity-and-designation", "catalogue-record-and-listing",
        "declared-schema-reference", "distribution-manifest-and-fixity",
        "use-restrictions-and-policy", "holder-and-role-assignment",
        "source-and-derivation", "version-identity-and-change",
        "quality-measurements", "fitness-for-use",
    },
    "WM-DAT-004": {
        "f-contract-identifier", "f-governed-subject", "f-version-designation",
        "f-object-property-structure", "f-term-value-domain-binding",
        "f-quality-rule-declaration", "f-compatibility-mode",
        "f-producer-consumer-parties", "f-obligations-acceptance",
        "f-classification-privacy-terms", "f-registry-publication",
    },
}


def load(path: Path) -> dict:
    text = path.read_text(encoding="utf-8")
    return json.loads(text[text.index("{"):])


def compact_function(item: dict) -> dict:
    return {key: item.get(key) for key in ("id", "name", "description")}


def compact_finding(item: dict) -> dict:
    return {
        "id": item.get("id"),
        "name": item.get("name"),
        "description": item.get("description"),
        "dataElements": [
            {key: element.get(key) for key in ("id", "name", "value_kind", "cardinality", "required")}
            for element in item.get("data_elements", [])
        ],
    }


def compact_composition(composition: list | None) -> list:
    return [
        {field: item.get(field) for field in ("target", "relation", "purpose", "required") if item.get(field) is not None}
        for item in (composition or [])
    ]


def compact_hold(item: dict | str) -> dict | str:
    if not isinstance(item, dict):
        return item
    return {key: item.get(key) for key in ("id", "status", "description", "reason") if item.get(key) is not None}


def compact(model_id: str, path: Path) -> dict:
    data = load(path)
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
        "sources": [
            {key: source.get(key) for key in ("id", "title", "organization", "url", "version_or_date")}
            for source in data.get("sources", []) if source.get("primary_source")
        ],
        "composition": compact_composition(data.get("composition")),
        "functions": [compact_function(item) for item in data.get("functions", [])],
        "researchAdjudication": {
            "boundaryDecision": adjudication.get("boundaryDecision"),
            "publicationHolds": [compact_hold(item) for item in (adjudication.get("publicationHolds") or [])],
        },
        "selectedFindings": findings,
        "statistics": data.get("statistics"),
    }


dossier = {
    "contour": {
        "id": "EM-DAT-01",
        "name": "Dataset, schema and contract",
        "scope": "Dataset identity and versions, distributions, schema, quality and permitted-use contract. A catalogue entry references a dataset; it is not the dataset.",
        "questions": [
            "What preserves dataset identity across a new export?",
            "How is structural schema separated from field meaning?",
            "When is a contract change incompatible?",
        ],
        "invariants": [
            "Dataset version and schema version are independent.",
            "A contract names producer/owner and consumer scope.",
            "A catalogue record references the dataset rather than replacing it.",
        ],
        "acceptanceScenario": "One dataset has two delivery formats and later changes schema while preserving provenance and explicit compatibility.",
        "decision": "Choose REUSE ONLY, PROFILE, or NEW MODEL. Do not duplicate WM-DAT-001 or WM-DAT-004 merely to create an Enterprise page.",
    },
    "models": {model_id: compact(model_id, path) for model_id, path in MODELS.items()},
}
(RUN / "provider-dossier.json").write_text(
    json.dumps(dossier, ensure_ascii=False, indent=2) + "\n",
    encoding="utf-8",
    newline="\n",
)
print(json.dumps({"output": str(RUN / "provider-dossier.json"), "bytes": (RUN / "provider-dossier.json").stat().st_size}))
