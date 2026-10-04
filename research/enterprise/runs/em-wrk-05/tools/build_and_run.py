import csv, hashlib, json, subprocess
from pathlib import Path
import yaml

W = Path(r"R:\02_PROJECTS\02_Meta_Models_Platforms\Ver.cy\current\ver-cy\world-models")
R = W / "research/enterprise/runs/em-wrk-05"
IDS = {"WM-ORG-016", "WM-ECO-012", "WM-PER-001", "WM-OBJ-001", "WM-XCT-009", "WM-ACT-008", "WM-FLW-015"}

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
    "WM-ORG-016": "publications/wm-org-016-work-assignment/spec.yaml",
    "WM-ECO-012": "publications/wm-eco-012-budget/spec.yaml",
    "WM-PER-001": "publications/wm-per-001-person/spec.yaml",
    "WM-OBJ-001": "publications/wm-obj-001-physical-item-instance/spec.yaml",
    "WM-XCT-009": "publications/wm-xct-009-time-calendar/spec.yaml",
    "WM-ACT-008": "publications/wm-act-008-plan-schedule/spec.yaml",
    "WM-FLW-015": "publications/wm-flw-015-resource-consumption/spec.yaml",
}
dossier = {
    "contour": next(x for x in registry["units"] if x["id"] == "EM-WRK-05"),
    "queue": next(x for x in queue["units"] if x["id"] == "EM-WRK-05"),
    "reservations": [x for x in unified if x.get("model_id") in IDS],
    "relations": [x for x in relations if x.get("source_model_id") in IDS or x.get("target_model_id") in IDS],
    "specs": {key: compact(W / value) for key, value in specs.items()},
    "prior_research": {
        "EM-WRK-04": text_document(W / "research/enterprise/runs/em-wrk-04/local-evidence.md"),
        "EM-PEO-07": text_document(W / "research/enterprise/runs/em-peo-07/local-evidence.md"),
        "EM-OPS-03": text_document(W / "research/enterprise/runs/em-ops-03/local-evidence.md"),
        "EM-TEC-04": text_document(W / "research/enterprise/runs/em-tec-04/local-evidence.md"),
        "EM-FIN-01": text_document(W / "research/enterprise/runs/em-fin-01/local-evidence.md"),
    },
}
R.mkdir(parents=True, exist_ok=True)
dossier_path = R / "provider-dossier.json"
dossier_path.write_text(json.dumps(dossier, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
prompt = """Independent enterprise metamodel review. Use only the frozen dossier; no tools, browsing or invented identifiers. Adjudicate EM-WRK-05 Capacity and Resource Allocation using complete WM-ORG-016 Work Assignment, WM-ECO-012 Budget, WM-PER-001 Person, WM-OBJ-001 Physical Item, WM-XCT-009 Time/Calendar, WM-ACT-008 Plan/Schedule and WM-FLW-015 Resource Consumption drafts plus prior boundary work. Candidate types are ResourceDemand, ResourcePool, CapacityPlan, ResourceAllocation and AllocationScenario. Decide reuse/profile/new by independent identity and lifecycle without allocating identifiers. Separate human assignment from planned capacity, financial budget from non-money capacity, physical/compute masters from pools, plan from fact, demand from allocation, reusable pool from scenario membership, divisible from indivisible resource, competence requirement from named-person assignment, scheduled capacity from availability and actual consumption. Test two projects competing for one specialist and one GPU pool; detect overlap without changing employment, assignment or asset masters. Explain when >100% is an error versus separate scenarios. Preserve units, calendars, time zones, effective intervals, scenario identity, uncertainty, reservations, overbooking policy and source mastership. Reject addition of FTE, GPU-hours and currency. Return <=1200 words with headings Verdict; Evidence; Identity/mastership; Resource kinds/units; Demand/pool; Capacity plan/scenarios; Allocation/reservation; Human/asset/compute boundaries; Time/calendar; Plan versus fact; Acceptance scenario; Invariants; Minimal model set; Holds. Explicitly decide which candidates need independent identity and identify gaps or contradictions. Do not claim canonical completeness, installability or publication readiness.

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
