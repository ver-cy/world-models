import csv, hashlib, json, subprocess
from pathlib import Path

import yaml

W = Path(r"R:\02_PROJECTS\02_Meta_Models_Platforms\Ver.cy\current\ver-cy\world-models")
R = W / "research/enterprise/runs/em-lnd-04"
IDS = {"WM-KNW-011", "WM-XCT-025", "WM-ACT-001", "WM-ACT-030", "WM-ACT-029", "WM-ACT-005", "WM-ACT-034", "WM-MAT-008"}


def read_json(path): return json.loads(path.read_text(encoding="utf-8-sig"))
def read_rows(path):
    with path.open(encoding="utf-8-sig", newline="") as h: return list(csv.DictReader(h))
def compact_spec(path):
    raw = path.read_bytes(); doc = yaml.safe_load(raw.decode("utf-8-sig")); structure = doc.get("structure", {})
    bundles = []
    for bundle in structure.get("bundles", []):
        layers = []
        for layer in bundle.get("layers", []):
            findings = [{k: v for k, v in f.items() if k not in {"questions", "data_elements", "artifacts", "source_refs"}} for f in layer.get("findings", [])]
            layers.append({k: v for k, v in layer.items() if k not in {"findings", "source_refs"}} | {"findings": findings})
        bundles.append({k: v for k, v in bundle.items() if k not in {"layers", "source_refs"}} | {"layers": layers})
    compact = {k: v for k, v in doc.items() if k not in {"sources", "structure"}}
    compact["sources"] = [{k: s.get(k) for k in ("id", "title", "organization", "version_or_date", "source_type", "primary_source", "authority_tier")} for s in doc.get("sources", [])]
    compact["structure"] = {k: v for k, v in structure.items() if k != "bundles"} | {"bundles": bundles}
    return {"bytes": len(raw), "sha256": hashlib.sha256(raw).hexdigest(), "document": compact}
def text_doc(path):
    raw = path.read_bytes(); return {"bytes": len(raw), "sha256": hashlib.sha256(raw).hexdigest(), "content": raw.decode("utf-8-sig")}


registry = read_json(W / "research/enterprise/registry.json")
queue = read_json(W / "research/enterprise/queue.json")
unified = read_rows(W / "planning/VERCY-UNIFIED-MEGA-REGISTRY.csv")
relations = read_rows(W / "planning/VERCY-MODEL-RELATIONS.csv")
dossier = {
    "contour": next(x for x in registry["units"] if x["id"] == "EM-LND-04"),
    "queue": next(x for x in queue["units"] if x["id"] == "EM-LND-04"),
    "related_registry_contours": [x for x in registry["units"] if x["id"] in {"EM-STR-01", "EM-STR-02", "EM-STR-03", "EM-STR-04"}],
    "reservations": [x for x in unified if x.get("model_id") in IDS],
    "relations": [x for x in relations if x.get("source_model_id") in IDS or x.get("target_model_id") in IDS],
    "spec_availability": {mid: bool(list((W / "publications").glob(mid.lower() + "-*/spec.yaml"))) for mid in IDS},
    "specs": {
        "WM-KNW-011": compact_spec(W / "publications/wm-knw-011-goal-objective/spec.yaml"),
        "WM-XCT-025": compact_spec(W / "publications/wm-xct-025-observable-result-fields/spec.yaml"),
        "WM-ACT-030": compact_spec(W / "publications/wm-act-030-initiative/spec.yaml"),
        "WM-ACT-029": compact_spec(W / "publications/wm-act-029-program-portfolio/spec.yaml"),
        "WM-ACT-005": compact_spec(W / "publications/wm-act-005-project/spec.yaml"),
        "WM-ACT-034": compact_spec(W / "publications/wm-act-034-assessment-evaluation/spec.yaml"),
        "WM-MAT-008": compact_spec(W / "publications/wm-mat-008-observation-measurement-record/spec.yaml"),
    },
    "prior_research": {
        "EM-STR-02": text_doc(W / "research/enterprise/runs/em-str-02/local-evidence.md"),
        "EM-LND-05": text_doc(W / "research/enterprise/runs/em-lnd-05/local-evidence.md"),
    },
}
R.mkdir(parents=True, exist_ok=True)
p = R / "provider-dossier.json"
p.write_text(json.dumps(dossier, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
prompt = """Independent enterprise metamodel review. Use only the frozen dossier; no tools, browsing or invented identifiers. Decide EM-LND-04 Strategic Landscape, whose registry has no target IDs, across intent/strategy, goals, capabilities, initiatives, benefits and measurements. Place StrategyLandscape and StrategicAlignment and decide whether either needs independent identity or is a governed profile/projection. Reuse complete WM-KNW-011, WM-XCT-025, WM-ACT-030, WM-ACT-029, WM-ACT-005, WM-ACT-034 and WM-MAT-008 where justified; account for reserved-but-missing WM-ACT-001 Business Capability and unassigned Strategy/Outcome/Benefit candidates without allocating IDs. Define evidence-bearing support/alignment and causal-hypothesis links, distinguish objective, portfolio, initiative output, outcome and realized benefit, and surface an initiative without a goal, a goal without measurement and a constraining capability. Define time, scenario, confidence, contradiction and owner-question semantics. Test the negative case that a project tagged strategy is automatically beneficial. Return <=1200 words with headings Verdict; Evidence; Identity/mastership; Strategic elements; Alignment and causality; Outputs/outcomes/benefits; Capability constraint; Time/scenarios; Gap questions; Scenario; Invariants; Minimal profile shape; Holds. Do not claim canonical completeness or installability.\n\nDOSSIER\n""" + p.read_text(encoding="utf-8")
result = subprocess.run(["claude", "-p", "--model", "opus", "--effort", "high", "--tools", ""], input=prompt, text=True, encoding="utf-8", errors="replace", capture_output=True, timeout=900)
if result.returncode: raise SystemExit((result.stderr or result.stdout or f"claude exit {result.returncode}").strip())
(R / "claude-study.raw.md").write_text(result.stdout.rstrip() + "\n", encoding="utf-8")
print(p.stat().st_size, len(result.stdout))
