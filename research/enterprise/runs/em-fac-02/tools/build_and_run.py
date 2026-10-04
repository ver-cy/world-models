import csv, hashlib, json, subprocess
from pathlib import Path
import yaml

W = Path(r"R:\02_PROJECTS\02_Meta_Models_Platforms\Ver.cy\current\ver-cy\world-models")
R = W / "research/enterprise/runs/em-fac-02"
IDS = {"WM-ECO-034", "WM-MAT-008", "WM-FLW-015", "WM-DAT-001", "WM-ORG-001", "WM-ORG-012", "WM-OBJ-001", "WM-KNW-012"}

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
    "WM-ECO-034": "publications/wm-eco-034-esg-sustainability-disclosure/spec.yaml",
    "WM-MAT-008": "publications/wm-mat-008-observation-measurement-record/spec.yaml",
    "WM-FLW-015": "publications/wm-flw-015-resource-consumption/spec.yaml",
    "WM-DAT-001": "publications/wm-dat-001-dataset/spec.yaml",
    "WM-ORG-001": "publications/wm-org-001-organization/spec.yaml",
    "WM-ORG-012": "publications/wm-org-012-inter-organizational-relationship/spec.yaml",
    "WM-OBJ-001": "publications/wm-obj-001-physical-item-instance/spec.yaml",
    "WM-KNW-012": "publications/wm-knw-012-policy-rule/spec.yaml",
}
dossier = {
    "contour": next(x for x in registry["units"] if x["id"] == "EM-FAC-02"),
    "queue": next(x for x in queue["units"] if x["id"] == "EM-FAC-02"),
    "reservations": [x for x in unified if x.get("model_id") in IDS],
    "relations": [x for x in relations if x.get("source_model_id") in IDS or x.get("target_model_id") in IDS],
    "specs": {key: compact(W / value) for key, value in specs.items()},
    "prior_research": {
        "EM-FAC-01": text_document(W / "research/enterprise/runs/em-fac-01/local-evidence.md"),
        "EM-OPS-01": text_document(W / "research/enterprise/runs/em-ops-01/local-evidence.md"),
        "EM-FIN-05": text_document(W / "research/enterprise/runs/em-fin-05/local-evidence.md"),
        "EM-DAT-04": text_document(W / "research/enterprise/runs/em-dat-04/local-evidence.md"),
        "EM-DAT-06": text_document(W / "research/enterprise/runs/em-dat-06/local-evidence.md"),
    },
}
R.mkdir(parents=True, exist_ok=True)
dossier_path = R / "provider-dossier.json"
dossier_path.write_text(json.dumps(dossier, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
prompt = """Independent enterprise metamodel review. Use only the frozen dossier; no tools, browsing or invented identifiers. Adjudicate EM-FAC-02 Impact, Sustainability and Environmental Reporting using complete WM-ECO-034 Sustainability Disclosure plus adjacent Observation, Resource Consumption, Dataset, Organization, Inter-organizational Relationship, Physical Item and Policy/Rule drafts and prior boundary work. Candidate types are ImpactBoundary, ActivityData, EmissionFactor, ImpactCalculation and SustainabilityDisclosure. Decide reuse/profile/new by independent identity and lifecycle without allocating identifiers. Separate disclosure from inventory boundary, observed or estimated activity, factor definition/version, calculation execution/result, metric definition, assurance, filing and source facts. Distinguish organizational boundary from operational boundary, own operations from upstream/downstream value chain, control/equity approaches, market- from location-based methods, measured from estimated values, and impact quantity from financial cost. Require method, factor source/version/geography/technology/time, units, conversions, uncertainty, coverage, allocation rule, exclusions, recalculation policy, base year and evidence pins. Define double-count prevention across counterparties, scopes and shared assets without erasing each participant's valid inventory. Test two calculation methods plus a boundary change producing explainable non-comparable results. Reject cloud spend as exact emissions. Return <=1200 words with headings Verdict; Evidence; Identity/mastership; Disclosure/boundary; Activity data; Factor registry; Calculation/result; Units/method/uncertainty; Double counting/allocation; Time/version/recalculation; Assurance/publication; Acceptance scenario; Invariants; Minimal model set; Holds. Explicitly decide which candidates need independent identity and identify gaps or contradictions. Do not claim canonical completeness, installability or publication readiness.

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
