import csv, hashlib, json, subprocess
from pathlib import Path

import yaml

W = Path(r"R:\02_PROJECTS\02_Meta_Models_Platforms\Ver.cy\current\ver-cy\world-models")
R = W / "research/enterprise/runs/em-ai-01"
IDS = {"WM-AI-001", "WM-AI-002", "WM-AI-004", "WM-AI-005"}


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

dossier = {
    "contour": next(x for x in registry["units"] if x["id"] == "EM-AI-01"),
    "queue": next(x for x in queue["units"] if x["id"] == "EM-AI-01"),
    "reservations": [x for x in unified if x.get("model_id") in IDS],
    "relations": [x for x in relations if x.get("source_model_id") in IDS or x.get("target_model_id") in IDS],
    "specs": {
        "WM-AI-001": full_spec(W / "publications/wm-ai-001-ai-system/spec.yaml"),
        "WM-AI-002": full_spec(W / "publications/wm-ai-002-ai-agent/spec.yaml"),
        "WM-AI-004": full_spec(W / "publications/wm-ai-004-ai-inference-agent-run/spec.yaml"),
        "WM-AI-005": full_spec(W / "publications/wm-ai-005-prompt-agent-configuration/spec.yaml"),
    },
}

R.mkdir(parents=True, exist_ok=True)
p = R / "provider-dossier.json"
p.write_text(json.dumps(dossier, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")

prompt = """Independent enterprise metamodel review. Use only the frozen dossier; no tools, browsing or invented identifiers. Decide EM-AI-01 AI System, Agent and Execution across WM-AI-001 AI System, WM-AI-002 AI Agent, WM-AI-005 Prompt/Agent Configuration and WM-AI-004 Inference/Agent Run. Place ToolBinding and InferenceEndpoint without duplicating software/runtime/endpoint masters. Separate AI system, model artifact/product, agent role/configuration, immutable configuration version and run. Define authority, delegation, human oversight, tool authorization and reproducibility across two model versions and three tools. The accountable subject must remain a defined human/organization/operator; role=agent grants no ambient authority. Test one agent using two models and three tools with each run pinning configuration, permissions and actions. Return <=1200 words with headings Verdict; Evidence; Identity/mastership; System/model/agent/configuration/run; Tool binding; Endpoint; Authority/delegation/oversight; Reproducibility; Scenario; Invariants; Minimal completion shape; Holds. Do not claim canonical completeness or installability.\n\nDOSSIER\n""" + p.read_text(encoding="utf-8")

result = subprocess.run(["claude", "-p", "--model", "opus", "--effort", "high", "--tools", ""], input=prompt, text=True, encoding="utf-8", errors="replace", capture_output=True, timeout=900)
if result.returncode:
    raise SystemExit(result.stderr)
(R / "claude-study.raw.md").write_text(result.stdout.rstrip() + "\n", encoding="utf-8")
print(p.stat().st_size, len(result.stdout))
