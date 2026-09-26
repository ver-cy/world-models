import csv, hashlib, json, subprocess
from pathlib import Path
import yaml

W = Path(r"R:\02_PROJECTS\02_Meta_Models_Platforms\Ver.cy\current\ver-cy\world-models")
R = W / "research/enterprise/runs/em-ai-03"
IDS = {"WM-AI-003", "WM-AI-009", "WM-AI-008", "WM-AI-010", "WM-SFT-004", "WM-DAT-001", "WM-MAT-008", "WM-KNW-010", "WM-ACT-024", "WM-REC-010"}

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
    "WM-AI-003": "publications/wm-ai-003-ai-model-evaluation/spec.yaml",
    "WM-AI-009": "publications/wm-ai-009-evaluation-dataset-benchmark/spec.yaml",
    "WM-AI-008": "publications/wm-ai-008-ai-safety-governance-assessment/spec.yaml",
    "WM-AI-010": "publications/wm-ai-010-ai-incident-report/spec.yaml",
    "WM-SFT-004": "publications/wm-sft-004-ml-model-artifact/spec.yaml",
    "WM-DAT-001": "publications/wm-dat-001-dataset/spec.yaml",
    "WM-MAT-008": "publications/wm-mat-008-observation-measurement-record/spec.yaml",
    "WM-KNW-010": "publications/wm-knw-010-decision-rationale/spec.yaml",
    "WM-ACT-024": "publications/wm-act-024-decision-approval-activity/spec.yaml",
    "WM-REC-010": "publications/wm-rec-010-decision-approval-record/spec.yaml",
}
dossier = {
    "contour": next(x for x in registry["units"] if x["id"] == "EM-AI-03"),
    "queue": next(x for x in queue["units"] if x["id"] == "EM-AI-03"),
    "reservations": [x for x in unified if x.get("model_id") in IDS],
    "relations": [x for x in relations if x.get("source_model_id") in IDS or x.get("target_model_id") in IDS],
    "specs": {key: compact(W / value) for key, value in specs.items()},
    "prior_research": {
        "EM-AI-01": text_document(W / "research/enterprise/runs/em-ai-01/local-evidence.md"),
        "EM-AI-02": text_document(W / "research/enterprise/runs/em-ai-02/local-evidence.md"),
        "EM-DAT-04": text_document(W / "research/enterprise/runs/em-dat-04/local-evidence.md"),
        "EM-DAT-07": text_document(W / "research/enterprise/runs/em-dat-07/local-evidence.md"),
        "EM-RSK-01": text_document(W / "research/enterprise/runs/em-rsk-01/local-evidence.md"),
    },
}
R.mkdir(parents=True, exist_ok=True)
dossier_path = R / "provider-dossier.json"
dossier_path.write_text(json.dumps(dossier, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
prompt = """Independent enterprise metamodel review. Use only the frozen dossier; no tools, browsing or invented identifiers. Adjudicate EM-AI-03 AI Evaluation and Safety Evidence using complete WM-AI-003 Model Evaluation, WM-AI-009 Evaluation Dataset/Benchmark, WM-AI-008 Safety/Governance Assessment, WM-AI-010 Incident Report plus artifact, dataset, observation and decision-triad drafts and prior boundary work. Candidate types are EvaluationPlan, EvaluationRun, BenchmarkSpecification, SafetyAssessment and DeploymentDecision. Decide reuse/profile/new by independent identity and lifecycle without allocating identifiers. Separate evaluation protocol/plan from execution run and result; benchmark specification from dataset snapshot; capability measurement from safety judgement; safety assessment from deployment authorization; assessment decision from rationale, decision act and issued instrument; incident report from incident evidence. Require pins for model artifact, configuration, benchmark/dataset, metric definition, code/tool versions, environment, context, intended use, population, uncertainty and limitations. Define contamination/leakage evidence, distribution shift, construct validity, context drift, staleness and reassessment triggers. Test a changed dataset and deployment context that requires a new evaluation and explicit decision rather than carrying old approval. Reject a high benchmark score as universal safety proof. Return <=1200 words with headings Verdict; Evidence; Identity/mastership; Plan/run/result; Benchmark/dataset; Measurement/uncertainty; Safety assessment; Deployment decision; Contamination/context drift; Incident feedback; Time/version/reassessment; Acceptance scenario; Invariants; Minimal model set; Holds. Explicitly decide which candidates need independent identity and identify gaps or contradictions. Do not claim canonical completeness, installability or publication readiness.

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
