import csv, hashlib, json, subprocess
from pathlib import Path
import yaml

W = Path(r"R:\02_PROJECTS\02_Meta_Models_Platforms\Ver.cy\current\ver-cy\world-models")
R = W / "research/enterprise/runs/em-lnd-14"
IDS = {'WM-AI-001', 'WM-AI-002', 'WM-AI-003', 'WM-AI-004', 'WM-AI-005', 'WM-AI-006', 'WM-AI-007', 'WM-AI-008', 'WM-AI-009', 'WM-AI-010', 'WM-DAT-001', 'WM-MAT-008', 'WM-SFT-004', 'WM-XCT-037'}

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
    "WM-AI-001": "publications/wm-ai-001-ai-system/spec.yaml",
    "WM-AI-002": "publications/wm-ai-002-ai-agent/spec.yaml",
    "WM-AI-003": "publications/wm-ai-003-ai-model-evaluation/spec.yaml",
    "WM-AI-004": "publications/wm-ai-004-ai-inference-agent-run/spec.yaml",
    "WM-AI-005": "publications/wm-ai-005-prompt-agent-configuration/spec.yaml",
    "WM-AI-006": "publications/wm-ai-006-model-training-fine-tuning-run/spec.yaml",
    "WM-AI-007": "publications/wm-ai-007-ai-model-registry-entry/spec.yaml",
    "WM-AI-008": "publications/wm-ai-008-ai-safety-governance-assessment/spec.yaml",
    "WM-AI-009": "publications/wm-ai-009-evaluation-dataset-benchmark/spec.yaml",
    "WM-AI-010": "publications/wm-ai-010-ai-incident-report/spec.yaml",
    "WM-DAT-001": "publications/wm-dat-001-dataset/spec.yaml",
    "WM-MAT-008": "publications/wm-mat-008-observation-measurement-record/spec.yaml",
    "WM-SFT-004": "publications/wm-sft-004-ml-model-artifact/spec.yaml",
    "WM-XCT-037": "publications/wm-xct-037-dependency-impact/spec.yaml",
}
dossier = {
    "contour": next(x for x in registry["units"] if x["id"] == "EM-LND-14"),
    "queue": next(x for x in queue["units"] if x["id"] == "EM-LND-14"),
    "reservations": [x for x in unified if x.get("model_id") in IDS],
    "relations": [x for x in relations if x.get("source_model_id") in IDS or x.get("target_model_id") in IDS],
    "specs": {key: compact(W / value) for key, value in specs.items()},
    "prior_research": {
        "EM-AI-01": text_document(W / "research/enterprise/runs/em-ai-01/local-evidence.md"),
        "EM-AI-02": text_document(W / "research/enterprise/runs/em-ai-02/local-evidence.md"),
        "EM-AI-03": text_document(W / "research/enterprise/runs/em-ai-03/local-evidence.md"),
        "EM-DAT-02": text_document(W / "research/enterprise/runs/em-dat-02/local-evidence.md"),
        "EM-LND-12": text_document(W / "research/enterprise/runs/em-lnd-12/local-evidence.md"),
        "EM-LND-13": text_document(W / "research/enterprise/runs/em-lnd-13/local-evidence.md"),
    },
}
R.mkdir(parents=True, exist_ok=True)
dossier_path = R / "provider-dossier.json"
dossier_path.write_text(json.dumps(dossier, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
prompt = """Independent enterprise metamodel review. Use only the frozen dossier; no tools, browsing or invented identifiers. Adjudicate EM-LND-14 AI Research Landscape and AI Usage Network using complete AI System, Agent, Evaluation, Inference Run, Prompt/Agent Configuration, Training Run, Model Registry Entry, Safety Assessment, Benchmark/Dataset, Incident, Dataset, Measurement, Model Artifact and Dependency/Impact drafts plus prior AI/data/landscape work. Candidate types are AIResearchLandscape and AIUsageNetwork. Decide reuse/profile/new by independent identity and lifecycle without allocating identifiers. Determine whether both are governed declarations and reproducible graph projections, not subject roots. Separate research programme/question, dataset revision, model artifact, registry record, training run, effective configuration, evaluation plan/run/result, benchmark version, safety assessment, deployment decision, AI system, deployment/end point, inference run, incident, compute allocation and commercial product. Require lineage and rights to survive every derived edge. Run is not artifact; benchmark result is not universal deployment permission; a research checkpoint need not create a product. Test withdrawal of one dataset revision: identify affected training runs, artifacts, evaluations and systems; invalidate applicability without deleting evidence; preserve separate deployment decisions and distinguish proven, potential and unknown impact. Model compute used by research without requiring product identity. Return <=1200 words with headings Verdict; Evidence; Identity/mastership; Landscape/usage network; Research/data/rights; Training/artifacts/registry; Evaluation/benchmark/safety; Systems/deployments/runs; Withdrawal/impact; Compute/product boundary; Time/provenance/access; Governance; Acceptance scenario; Invariants; Minimal model set; Holds. Explicitly decide both candidates and identify missing roots or contradictions. Do not claim canonical completeness, installability or publication readiness.

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
