import csv, hashlib, json, subprocess
from pathlib import Path
import yaml

W = Path(r"R:\02_PROJECTS\02_Meta_Models_Platforms\Ver.cy\current\ver-cy\world-models")
R = W / "research/enterprise/runs/em-ai-02"
IDS = {"WM-SFT-004", "WM-AI-007", "WM-AI-006", "WM-DAT-001", "WM-AI-005", "WM-AI-001", "WM-FLW-015"}

def j(p):
    return json.loads(p.read_text(encoding="utf-8-sig"))

def rows(p):
    with p.open(encoding="utf-8-sig", newline="") as h:
        return list(csv.DictReader(h))

def compact(p):
    raw = p.read_bytes()
    d = yaml.safe_load(raw.decode("utf-8-sig"))
    s = d.get("structure", {})
    bundles = []
    for b in s.get("bundles", []):
        layers = []
        for layer in b.get("layers", []):
            findings = [
                {k: v for k, v in finding.items() if k not in {"questions", "data_elements", "artifacts", "source_refs"}}
                for finding in layer.get("findings", [])
            ]
            layers.append({k: v for k, v in layer.items() if k not in {"findings", "source_refs"}} | {"findings": findings})
        bundles.append({k: v for k, v in b.items() if k not in {"layers", "source_refs"}} | {"layers": layers})
    c = {k: v for k, v in d.items() if k not in {"sources", "structure"}}
    c["sources"] = [
        {k: x.get(k) for k in ("id", "title", "organization", "version_or_date", "source_type", "primary_source", "authority_tier")}
        for x in d.get("sources", [])
    ]
    c["structure"] = {k: v for k, v in s.items() if k != "bundles"} | {"bundles": bundles}
    return {"bytes": len(raw), "sha256": hashlib.sha256(raw).hexdigest(), "document": c}

def text_document(p):
    raw = p.read_bytes()
    return {"bytes": len(raw), "sha256": hashlib.sha256(raw).hexdigest(), "content": raw.decode("utf-8-sig")}

registry = j(W / "research/enterprise/registry.json")
queue = j(W / "research/enterprise/queue.json")
unified = rows(W / "planning/VERCY-UNIFIED-MEGA-REGISTRY.csv")
relations = rows(W / "planning/VERCY-MODEL-RELATIONS.csv")
specs = {
    "WM-SFT-004": "publications/wm-sft-004-ml-model-artifact/spec.yaml",
    "WM-AI-007": "publications/wm-ai-007-ai-model-registry-entry/spec.yaml",
    "WM-AI-006": "publications/wm-ai-006-model-training-fine-tuning-run/spec.yaml",
    "WM-DAT-001": "publications/wm-dat-001-dataset/spec.yaml",
    "WM-AI-005": "publications/wm-ai-005-prompt-agent-configuration/spec.yaml",
    "WM-AI-001": "publications/wm-ai-001-ai-system/spec.yaml",
    "WM-FLW-015": "publications/wm-flw-015-resource-consumption/spec.yaml",
}
dossier = {
    "contour": next(x for x in registry["units"] if x["id"] == "EM-AI-02"),
    "queue": next(x for x in queue["units"] if x["id"] == "EM-AI-02"),
    "reservations": [x for x in unified if x.get("model_id") in IDS],
    "relations": [x for x in relations if x.get("source_model_id") in IDS or x.get("target_model_id") in IDS],
    "specs": {key: compact(W / value) for key, value in specs.items()},
    "prior_research": {
        "EM-AI-01": text_document(W / "research/enterprise/runs/em-ai-01/local-evidence.md"),
        "EM-DAT-01": text_document(W / "research/enterprise/runs/em-dat-01/local-evidence.md"),
        "EM-WRK-05": text_document(W / "research/enterprise/runs/em-wrk-05/local-evidence.md"),
        "EM-FIN-05": text_document(W / "research/enterprise/runs/em-fin-05/local-evidence.md"),
        "EM-TEC-04": text_document(W / "research/enterprise/runs/em-tec-04/local-evidence.md"),
    },
}
R.mkdir(parents=True, exist_ok=True)
dossier_path = R / "provider-dossier.json"
dossier_path.write_text(json.dumps(dossier, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
prompt = """Independent enterprise metamodel review. Use only the frozen dossier; no tools, browsing or invented identifiers. Adjudicate EM-AI-02 AI Model, Artifact and Training using complete WM-SFT-004 ML Model Artifact, WM-AI-007 AI Model Registry Entry, WM-AI-006 Training/Fine-tuning Run plus adjacent Dataset, Prompt/Agent Configuration, AI System and Resource Consumption drafts and prior boundary work. Candidate types are AIModel, ModelArtifact, TrainingRun, TrainingConfiguration and ComputeAllocation. Decide reuse/profile/new by independent identity and lifecycle without allocating identifiers. Separate conceptual model family/architecture from registry entry, immutable weights/checkpoint/artifact, training run, training configuration, evaluation, deployment, inference endpoint and AI system. Decide checkpoint versus final artifact and whether training configuration is independently reusable or run-contained. Separate requested, granted/allocated and observed compute; compute grant never implies employment, identity, runtime deployment or actual use. Require pinned base model, tokenizer, dataset snapshots/splits/transforms, code revision, dependencies, hyperparameters, seeds, environment, rights/licence/purpose restrictions, artifact digests and reproducibility limits. Weights and protected data remain outside the public catalogue. Test two fine-tunes from one checkpoint with different dataset licences and one shared endpoint; preserve separate lineage and restrictions. Reject treating a new endpoint as a newly trained model or equal model names as equal weights. Return <=1200 words with headings Verdict; Evidence; Identity/mastership; Model/registry/artifact; Training run/configuration; Data/rights/provenance; Checkpoint/final artifact; Compute allocation/actuals; Deployment/endpoint; Time/version/reproducibility; Acceptance scenario; Invariants; Minimal model set; Holds. Explicitly decide which candidates need independent identity and identify gaps or contradictions. Do not claim canonical completeness, installability or publication readiness.

DOSSIER
""" + dossier_path.read_text(encoding="utf-8")
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
    raise SystemExit((result.stderr or result.stdout or f"claude exit {result.returncode}").strip())
(R / "claude-study.raw.md").write_text(result.stdout.rstrip() + "\n", encoding="utf-8")
print(dossier_path.stat().st_size, len(result.stdout))
