import csv, hashlib, json, subprocess
from pathlib import Path

import yaml

W = Path(r"R:\02_PROJECTS\02_Meta_Models_Platforms\Ver.cy\current\ver-cy\world-models")
R = W / "research/enterprise/runs/em-tec-04"
IDS = {"WM-SFT-010", "WM-SFT-002", "WM-XCT-039", "WM-SFT-009"}


def read_json(path):
    return json.loads(path.read_text(encoding="utf-8-sig"))


def read_rows(path):
    with path.open(encoding="utf-8-sig", newline="") as handle:
        return list(csv.DictReader(handle))


def full_spec(path):
    raw = path.read_bytes()
    return {"bytes": len(raw), "sha256": hashlib.sha256(raw).hexdigest(), "document": yaml.safe_load(raw.decode("utf-8-sig"))}


registry = read_json(W / "research/enterprise/registry.json")
queue = read_json(W / "research/enterprise/queue.json")
unified = read_rows(W / "planning/VERCY-UNIFIED-MEGA-REGISTRY.csv")
relations = read_rows(W / "planning/VERCY-MODEL-RELATIONS.csv")
legacy = W / "models/knowledge-information/N4-software-product-and-system.md"
legacy_raw = legacy.read_bytes()

dossier = {
    "contour": next(x for x in registry["units"] if x["id"] == "EM-TEC-04"),
    "queue": next(x for x in queue["units"] if x["id"] == "EM-TEC-04"),
    "reservations": [x for x in unified if x.get("model_id") in IDS],
    "relations": [x for x in relations if x.get("source_model_id") in IDS or x.get("target_model_id") in IDS],
    "specs": {
        "WM-SFT-002_legacy": {"bytes": len(legacy_raw), "sha256": hashlib.sha256(legacy_raw).hexdigest(), "content": legacy_raw.decode("utf-8-sig")},
        "WM-XCT-039": full_spec(W / "publications/wm-xct-039-managed-it-service-graph/spec.yaml"),
        "WM-SFT-009_adjacent": full_spec(W / "publications/wm-sft-009-deployment/spec.yaml"),
    },
    "missing_specs": {"WM-SFT-010": "Reserved Runtime / Compute Environment candidate has no current specification file."},
    "prior_adjudication": {
        "EM-TEC-02": "Complete/rename WM-SFT-002 as Software System and Business Application; installations resolve from current deployment and runtime environment.",
        "EM-TEC-03": "Endpoint binding is effective-dated and environment-qualified; address alone is not identity.",
    },
}

R.mkdir(parents=True, exist_ok=True)
p = R / "provider-dossier.json"
p.write_text(json.dumps(dossier, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")

prompt = """Independent enterprise metamodel review. Use only the frozen dossier; no tools, browsing or invented identifiers. Decide EM-TEC-04 Environment, Infrastructure and Service Instance against reserved WM-SFT-010 Runtime / Compute Environment, WM-SFT-002 Software System/Application, WM-XCT-039 Managed IT Service Graph and adjacent WM-SFT-009 Deployment. Determine the identity/lifecycle boundary for DeployedInstance, RuntimeEnvironment, InfrastructureResource, ConfigurationItem and HostingRelation. Explain ephemeral resources without lost history, when a configuration item and financial/physical asset coincide or merely reference each other, and logical cluster versus nodes. Preserve service identity across two regions and node replacement. Reject IP address as eternal identity. Return <=1200 words with headings Verdict; Evidence; Identity/mastership; Environment/resource/instance/CI; Hosting and topology; Ephemeral history; Asset boundary; Cluster/node; Scenario; Invariants; Minimal completion shape; Holds. Do not claim canonical completeness or installability.\n\nDOSSIER\n""" + p.read_text(encoding="utf-8")

result = subprocess.run(["claude", "-p", "--model", "opus", "--effort", "high", "--tools", ""], input=prompt, text=True, encoding="utf-8", errors="replace", capture_output=True, timeout=900)
if result.returncode:
    raise SystemExit(result.stderr)
(R / "claude-study.raw.md").write_text(result.stdout.rstrip() + "\n", encoding="utf-8")
print(p.stat().st_size, len(result.stdout))
