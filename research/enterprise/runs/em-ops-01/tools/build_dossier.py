import csv
import json
from pathlib import Path

WORLD = Path(r"R:\02_PROJECTS\02_Meta_Models_Platforms\Ver.cy\current\ver-cy\world-models")
OUT = WORLD / "research/enterprise/runs/em-ops-01/provider-dossier.json"
IDS = {"WM-ACT-003", "WM-ACT-009"}


def read_json(path):
    return json.loads(path.read_text(encoding="utf-8-sig"))


def csv_rows(path):
    with path.open(encoding="utf-8-sig", newline="") as handle:
        return list(csv.DictReader(handle))


def main():
    registry = read_json(WORLD / "research/enterprise/registry.json")
    queue = read_json(WORLD / "research/enterprise/queue.json")
    unified = csv_rows(WORLD / "planning/VERCY-UNIFIED-MEGA-REGISTRY.csv")
    relations = csv_rows(WORLD / "planning/VERCY-MODEL-RELATIONS.csv")
    status = csv_rows(WORLD / "research/status.csv")

    dossier = {
        "contour": next(x for x in registry["units"] if x["id"] == "EM-OPS-01"),
        "queue_reservation": next(x for x in queue["units"] if x["id"] == "EM-OPS-01"),
        "registry_reservations": [x for x in unified if x.get("model_id") in IDS],
        "research_status": [x for x in status if x.get("model_id") in IDS],
        "relationship_ledger": [
            x for x in relations
            if x.get("source_model_id") in IDS or x.get("target_model_id") in IDS
        ],
        "complete_candidate_specs": {
            "WM-ACT-003": (WORLD / "models/activity-work/K3-process-and-workflow.md").read_text(encoding="utf-8"),
            "WM-ACT-009": (WORLD / "models/activity-work/K6-practice-method-and-procedure.md").read_text(encoding="utf-8"),
        },
        "evidence_limits": [
            "Both candidates are reserved registry rows with described-previous-version status and migration-boundary-review state.",
            "The supplied specifications use wildcard imports and legacy K3/K6 identifiers; no executable fixtures or current publication packages were found for either candidate.",
            "Candidate properties from the Enterprise v1 registry are non-normative.",
            "Relationship-ledger rows are candidate relations and do not grant inheritance, mutation or cascade authority.",
        ],
    }
    OUT.parent.mkdir(parents=True, exist_ok=True)
    OUT.write_text(json.dumps(dossier, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    print(OUT)
    print(OUT.stat().st_size)


if __name__ == "__main__":
    main()
