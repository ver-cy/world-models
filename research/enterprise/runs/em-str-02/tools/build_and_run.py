import csv, hashlib, json, subprocess
from pathlib import Path

import yaml

W = Path(r"R:\02_PROJECTS\02_Meta_Models_Platforms\Ver.cy\current\ver-cy\world-models")
R = W / "research/enterprise/runs/em-str-02"
IDS = {"WM-KNW-011", "WM-XCT-025"}


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
    "contour": next(item for item in registry["units"] if item["id"] == "EM-STR-02"),
    "queue": next(item for item in queue["units"] if item["id"] == "EM-STR-02"),
    "reservations": [item for item in unified if item.get("model_id") in IDS],
    "adjacent_reservations": [
        item for item in unified if item.get("model_id") in {"WM-ACT-034", "WM-MAT-008"}
    ],
    "relations": [
        item
        for item in relations
        if item.get("source_model_id") in IDS or item.get("target_model_id") in IDS
    ],
    "specs": {
        "WM-KNW-011": project_spec(
            W / "publications/wm-knw-011-goal-objective/spec.yaml"
        ),
        "WM-XCT-025": project_spec(
            W / "publications/wm-xct-025-observable-result-fields/spec.yaml"
        ),
    },
    "limits": [
        "Both bases are non-canonical reviewable drafts; complete specs were parsed and pinned.",
        "Metric Definition from EM-DAT-05 and benefit/value mastership are not allocated in these two reservations.",
    ],
}

R.mkdir(parents=True, exist_ok=True)
dossier_path = R / "provider-dossier.json"
dossier_path.write_text(
    json.dumps(dossier, ensure_ascii=False, indent=2) + "\n", encoding="utf-8"
)

prompt = """Independent enterprise metamodel review. Use only the dossier; no tools, browsing, or invented identifiers. Decide EM-STR-02 Objectives, Key Results and Benefits over WM-KNW-011 Goal / Objective and WM-XCT-025 Observable Result Fields. Choose reuse/profile/complete-reserved or identifier-unassigned candidate only where independent identity, lifecycle and mastership justify it. Separate Objective, Key Result, Target, Metric Definition, Observation, Outcome, expected Benefit, realised Benefit, disbenefit/anti-value, Value Assessment, deliverable and work contribution. Explain attribution from multiple projects without double counting and comparison when value/harm scales are incompatible. A planned effect must never become a realised outcome without observation. Target values pin metric versions. Test one benefit contributed to by two projects, delayed measurement and a negative side effect while preserving uncertainty. Return <=1200 words with headings Verdict; Evidence; Identity/mastership; Objective/KR/target; Outcome/observation; Benefit attribution; Value/anti-value comparison; Invariants; Scenario; Minimal profile/candidate shape; Holds. Do not claim canonical completeness or installability.\n\nDOSSIER\n""" + dossier_path.read_text(encoding="utf-8")

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
