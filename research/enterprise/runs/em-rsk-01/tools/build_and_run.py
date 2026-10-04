import csv, hashlib, json, subprocess
from pathlib import Path

import yaml

W = Path(r"R:\02_PROJECTS\02_Meta_Models_Platforms\Ver.cy\current\ver-cy\world-models")
R = W / "research/enterprise/runs/em-rsk-01"
IDS = {"WM-KNW-015", "WM-XCT-027"}


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
    "contour": next(item for item in registry["units"] if item["id"] == "EM-RSK-01"),
    "queue": next(item for item in queue["units"] if item["id"] == "EM-RSK-01"),
    "reservations": [item for item in unified if item.get("model_id") in IDS],
    "relations": [
        item
        for item in relations
        if item.get("source_model_id") in IDS or item.get("target_model_id") in IDS
    ],
    "specs": {
        "WM-KNW-015": project_spec(
            W / "publications/wm-knw-015-risk-opportunity/spec.yaml"
        ),
        "WM-XCT-027": project_spec(
            W / "publications/wm-xct-027-risk-control/spec.yaml"
        ),
    },
    "limits": [
        "Both bases are non-canonical single-provider reviewable drafts; complete specs were parsed and pinned.",
        "WM-XCT-027 has an explicit unresolved ownership split between its mixin boundary and authored control/assessment artifacts.",
    ],
}

R.mkdir(parents=True, exist_ok=True)
dossier_path = R / "provider-dossier.json"
dossier_path.write_text(
    json.dumps(dossier, ensure_ascii=False, indent=2) + "\n", encoding="utf-8"
)

prompt = """Independent enterprise metamodel review. Use only the dossier; no tools, browsing, or invented identifiers. Decide EM-RSK-01 Risk, Control and Performance Assessment over WM-KNW-015 Risk / Opportunity and WM-XCT-027 Risk / Control. Choose reuse/profile/complete-reserved or identifier-unassigned candidate only where independent identity, lifecycle and mastership justify it. Separate risk entity, assessment context/result, treatment decision/action, control design, control implementation/execution, control test/effectiveness determination, evidence, appetite/tolerance and residual-risk acceptance. Resolve WM-XCT-027's stated ownership split: which fields remain a host mixin and which require an external control/assessment master. Explain comparison across scales/horizons and shared causes without false aggregation. A policy green status must never close risk; control existence must never prove effectiveness. Test one control linked to three risks where failed execution changes an assessment only through an explicit evidence/causal link. Return <=1200 words with headings Verdict; Evidence; Identity/mastership; Assessment and comparability; Control design/execution/effectiveness; Treatment/residual risk; Shared cause; Invariants; Scenario; Minimal profile/candidate shape; Holds. Do not claim canonical completeness or installability.\n\nDOSSIER\n""" + dossier_path.read_text(encoding="utf-8")

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
