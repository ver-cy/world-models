import csv, hashlib, json, subprocess
from pathlib import Path

import yaml

W = Path(r"R:\02_PROJECTS\02_Meta_Models_Platforms\Ver.cy\current\ver-cy\world-models")
R = W / "research/enterprise/runs/em-prd-03"
IDS = {"WM-REC-006", "WM-KNW-013"}


def read_json(path):
    return json.loads(path.read_text(encoding="utf-8-sig"))


def read_rows(path):
    with path.open(encoding="utf-8-sig", newline="") as handle:
        return list(csv.DictReader(handle))


def project_spec(path):
    raw = path.read_bytes()
    spec = yaml.safe_load(raw.decode())
    findings = []
    for bundle in spec["structure"]["bundles"]:
        for layer in bundle["layers"]:
            for finding in layer["findings"]:
                findings.append(
                    {
                        "id": finding["id"],
                        "name": finding["name"],
                        "description": finding["description"],
                        "data_elements": [
                            {
                                key: element.get(key)
                                for key in (
                                    "id",
                                    "name",
                                    "description",
                                    "value_kind",
                                    "cardinality",
                                    "required",
                                )
                            }
                            for element in finding.get("data_elements", [])
                        ],
                    }
                )
    return {
        "bytes": len(raw),
        "sha256": hashlib.sha256(raw).hexdigest(),
        "publication": spec["publication"],
        "model": spec["model"],
        "findings": findings,
        "functions": [
            {key: function.get(key) for key in ("id", "name", "description")}
            for function in spec["functions"]
        ],
        "composition": spec["composition"],
        "adjudication": spec["researchAdjudication"],
        "statistics": spec["statistics"],
    }


registry = read_json(W / "research/enterprise/registry.json")
queue = read_json(W / "research/enterprise/queue.json")
unified = read_rows(W / "planning/VERCY-UNIFIED-MEGA-REGISTRY.csv")
relations = read_rows(W / "planning/VERCY-MODEL-RELATIONS.csv")

dossier = {
    "contour": next(item for item in registry["units"] if item["id"] == "EM-PRD-03"),
    "queue": next(item for item in queue["units"] if item["id"] == "EM-PRD-03"),
    "reservations": [item for item in unified if item.get("model_id") in IDS],
    "relations": [
        item
        for item in relations
        if item.get("source_model_id") in IDS or item.get("target_model_id") in IDS
    ],
    "specs": {
        "WM-REC-006": {
            "available": False,
            "reason": "No current specification file is referenced by the reservation or present in publications/models.",
        },
        "WM-KNW-013": project_spec(
            W / "publications/wm-knw-013-constraint-requirement-rule/spec.yaml"
        ),
    },
    "limits": [
        "WM-REC-006 is a reserved view-candidate with no current full specification; its boundary must be completed before publication.",
        "WM-KNW-013 is a non-canonical reviewable draft with a single-provider waiver; registry relations and v1 fields remain non-normative.",
    ],
}

R.mkdir(parents=True, exist_ok=True)
dossier_path = R / "provider-dossier.json"
dossier_path.write_text(
    json.dumps(dossier, ensure_ascii=False, indent=2) + "\n", encoding="utf-8"
)

prompt = """Independent enterprise metamodel review. Use only the dossier; no tools, browsing, or invented identifiers. Decide EM-PRD-03 Requirements and Expected Behaviour over reserved WM-REC-006 Requirement and WM-KNW-013 Constraint / Requirement Rule. Determine whether WM-REC-006 remains a view, must be completed/reclassified as an entity or aggregate, and how it references reusable formal rules. Separate stakeholder need, requirement, acceptance criterion, feature/design decision, implementation task, test case/result and observed evidence. Define immutable requirement revisions, baselines as exact revision sets, version-pinned trace links, conflict preservation and authority. A Done task must never prove requirement satisfaction; a failed test must remain visible. Test one requirement traced to three tasks and a failed test, then compare two baselines. Return <=1200 words with headings Verdict; Evidence; Identity and mastership; Need/requirement/feature/task boundary; Rule and acceptance-criterion boundary; Revision/baseline semantics; Trace/conflict semantics; Invariants; Scenario; Minimal completion shape; Holds. Do not claim canonical completeness or installability.\n\nDOSSIER\n""" + dossier_path.read_text(encoding="utf-8")

result = subprocess.run(
    ["claude", "-p", "--model", "opus", "--effort", "high", "--tools", ""],
    input=prompt,
    text=True,
    encoding="utf-8",
    errors="replace",
    capture_output=True,
    timeout=900,
)
if result.returncode:
    raise SystemExit(result.stderr)
(R / "claude-study.raw.md").write_text(
    result.stdout.rstrip() + "\n", encoding="utf-8"
)
print(dossier_path.stat().st_size, len(result.stdout))
