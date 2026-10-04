import csv, hashlib, json, subprocess
from pathlib import Path
import yaml

W = Path(r"R:\02_PROJECTS\02_Meta_Models_Platforms\Ver.cy\current\ver-cy\world-models")
R = W / "research/enterprise/runs/em-wrk-06"
IDS = {"WM-XCT-037", "WM-ACT-034", "WM-KNW-007", "WM-KNW-008", "WM-MAT-008", "WM-KNW-015"}

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
    "WM-XCT-037": "publications/wm-xct-037-dependency-impact/spec.yaml",
    "WM-ACT-034": "publications/wm-act-034-assessment-evaluation/spec.yaml",
    "WM-KNW-007": "publications/wm-knw-007-claim-proposition/spec.yaml",
    "WM-KNW-008": "publications/wm-knw-008-evidence-citation/spec.yaml",
    "WM-MAT-008": "publications/wm-mat-008-observation-measurement-record/spec.yaml",
    "WM-KNW-015": "publications/wm-knw-015-risk-opportunity/spec.yaml",
}
dossier = {
    "contour": next(x for x in registry["units"] if x["id"] == "EM-WRK-06"),
    "queue": next(x for x in queue["units"] if x["id"] == "EM-WRK-06"),
    "reservations": [x for x in unified if x.get("model_id") in IDS],
    "relations": [x for x in relations if x.get("source_model_id") in IDS or x.get("target_model_id") in IDS],
    "specs": {key: compact(W / value) for key, value in specs.items()},
    "prior_research": {
        "EM-WRK-05": text_document(W / "research/enterprise/runs/em-wrk-05/local-evidence.md"),
        "EM-TEC-03": text_document(W / "research/enterprise/runs/em-tec-03/local-evidence.md"),
        "EM-LND-12": text_document(W / "research/enterprise/runs/em-lnd-12/local-evidence.md"),
        "EM-RSK-01": text_document(W / "research/enterprise/runs/em-rsk-01/local-evidence.md"),
        "EM-KNW-02": text_document(W / "research/enterprise/runs/em-knw-02/local-evidence.md"),
    },
}
R.mkdir(parents=True, exist_ok=True)
dossier_path = R / "provider-dossier.json"
dossier_path.write_text(json.dumps(dossier, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
prompt = """Independent enterprise metamodel review. Use only the frozen dossier; no tools, browsing or invented identifiers. Adjudicate EM-WRK-06 Dependencies and Impact Analysis using complete WM-XCT-037 Dependency/Impact plus adjacent Assessment, Claim, Evidence Citation, Observation and Risk drafts and prior boundary work. Candidate types are Dependency, DependencyType, CriticalityAssessment, ImpactScenario and DependencyEvidence. Decide reuse/profile/new by independent identity and lifecycle without allocating identifiers. Separate dependency assertion from dependency-type vocabulary, endpoint masters, evidence artifact, observation, causal claim, risk, assessment and computed impact projection. Decide whether WM-XCT-037 already covers each candidate or only the edge declaration. Define canonical direction, inverse derivation, arity, conditions, lag, phases, transitivity, cycle rules, completeness, unknown/absent states, confidence, evidence references, scenario snapshot, propagation licence, traversal limits, criticality scheme and uncertainty. Test an API change and a resource delay producing different affected sets; unknown or incomplete edges must reduce completeness. Reject treating every graph path as a proven causal chain. Return <=1200 words with headings Verdict; Evidence; Identity/mastership; Dependency edge/type; Evidence/epistemics; Graph rules; Impact scenario; Criticality/assessment; Causality/risk; Time/version/snapshot; Acceptance scenario; Invariants; Minimal model set; Holds. Explicitly decide which candidates need independent identity and identify gaps or contradictions. Do not claim canonical completeness, installability or publication readiness.

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
