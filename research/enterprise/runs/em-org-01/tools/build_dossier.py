import csv
import hashlib
import json
from pathlib import Path

import yaml

WORLD = Path(r"R:\02_PROJECTS\02_Meta_Models_Platforms\Ver.cy\current\ver-cy\world-models")
OUT = WORLD / "research/enterprise/runs/em-org-01/provider-dossier.json"
IDS = {"WM-ORG-001", "WM-ORG-012"}
SELECTED_IDS = {
    "name-forms-and-validity", "name-history-and-change", "entity-resolution-and-duplicates",
    "entity-category-and-personality", "statistical-unit-alignment", "lifecycle-event-records",
    "succession-and-continuity", "consolidation-and-group-links",
    "ownership-and-beneficial-ownership", "external-affiliation-and-accreditation",
    "record-stewardship-and-change-authority", "relation-identity-record",
    "participant-roles-record", "recognition-basis-record", "control-interest-record",
    "collaboration-scope-record", "relationship-time-record", "graph-interpretation-record",
    "assertion-evidence-record", "relationship-stewardship-record",
}


def read_json(path):
    return json.loads(path.read_text(encoding="utf-8-sig"))


def csv_rows(path):
    with path.open(encoding="utf-8-sig", newline="") as handle:
        return list(csv.DictReader(handle))


def spec_projection(path):
    raw = path.read_bytes()
    doc = yaml.safe_load(raw.decode("utf-8"))
    bundles = []
    selected = []
    for bundle in doc.get("structure", {}).get("bundles", []):
        b = {k: bundle.get(k) for k in ("id", "name", "description")}
        layers = []
        for layer in bundle.get("layers", []):
            layers.append({k: layer.get(k) for k in ("id", "name", "description")})
            for finding in layer.get("findings", []):
                if finding.get("id") in SELECTED_IDS:
                    selected.append({
                        "bundle": b,
                        "layer": layers[-1],
                        "finding": {
                            "id": finding.get("id"),
                            "name": finding.get("name"),
                            "description": finding.get("description"),
                            "source_refs": finding.get("source_refs"),
                            "questions": [q.get("text") for q in finding.get("questions", [])],
                            "data_elements": [
                                {k: e.get(k) for k in ("id", "name", "description", "value_kind", "cardinality", "required")}
                                for e in finding.get("data_elements", [])
                            ],
                        },
                    })
        bundles.append({**b, "layers": layers})
    return {
        "source_file": path.relative_to(WORLD).as_posix(),
        "source_bytes": len(raw),
        "source_sha256": hashlib.sha256(raw).hexdigest(),
        "publication": doc.get("publication"),
        "metaModel": doc.get("metaModel"),
        "model": doc.get("model"),
        "structure_index": bundles,
        "selected_complete_findings": selected,
        "functions": [
            {k: f.get(k) for k in ("id", "name", "description")}
            for f in (doc.get("functions") or [])
        ],
        "composition": doc.get("composition"),
        "researchAdjudication": doc.get("researchAdjudication"),
        "statistics": doc.get("statistics"),
    }


def main():
    registry = read_json(WORLD / "research/enterprise/registry.json")
    queue = read_json(WORLD / "research/enterprise/queue.json")
    unified = csv_rows(WORLD / "planning/VERCY-UNIFIED-MEGA-REGISTRY.csv")
    relations = csv_rows(WORLD / "planning/VERCY-MODEL-RELATIONS.csv")
    dossier = {
        "contour": next(x for x in registry["units"] if x["id"] == "EM-ORG-01"),
        "queue_reservation": next(x for x in queue["units"] if x["id"] == "EM-ORG-01"),
        "registry_reservations": [x for x in unified if x.get("model_id") in IDS],
        "relationship_ledger": [x for x in relations if x.get("source_model_id") in IDS or x.get("target_model_id") in IDS],
        "current_specs": {
            "WM-ORG-001": spec_projection(WORLD / "publications/wm-org-001-organization/spec.yaml"),
            "WM-ORG-012": spec_projection(WORLD / "publications/wm-org-012-inter-organizational-relationship/spec.yaml"),
        },
        "evidence_limits": [
            "Both current publications are reviewable drafts with publishableCanonical false.",
            "WM-ORG-012 used a single-provider waiver and has no independent external review.",
            "Selected findings are a keyword projection; source byte count and SHA-256 pin the complete parsed specifications.",
            "Candidate Enterprise v1 fields and registry relations are non-normative until independently accepted.",
        ],
    }
    OUT.parent.mkdir(parents=True, exist_ok=True)
    OUT.write_text(json.dumps(dossier, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    print(OUT)
    print(OUT.stat().st_size)


if __name__ == "__main__":
    main()
