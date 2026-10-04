import csv, hashlib, json, subprocess
from pathlib import Path
import yaml

W = Path(r"R:\02_PROJECTS\02_Meta_Models_Platforms\Ver.cy\current\ver-cy\world-models")
R = W / "research/enterprise/runs/em-peo-09"
IDS = {
    "WM-ECO-031", "WM-ORG-005", "WM-ORG-004", "WM-ECO-004", "WM-ECO-002",
    "WM-REC-010", "WM-ECO-009", "WM-XCT-003", "WM-XCT-005", "WM-POL-012", "WM-MAT-008"
}

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
    "WM-ECO-031": "publications/wm-eco-031-payroll-compensation/spec.yaml",
    "WM-ORG-005": "publications/wm-org-005-employment/spec.yaml",
    "WM-ORG-004": "publications/wm-org-004-position/spec.yaml",
    "WM-ECO-004": "publications/wm-eco-004-money-instrument/spec.yaml",
    "WM-ECO-002": "publications/wm-eco-002-price-valuation/spec.yaml",
    "WM-REC-010": "publications/wm-rec-010-decision-approval-record/spec.yaml",
    "WM-ECO-009": "publications/wm-eco-009-payment/spec.yaml",
    "WM-XCT-003": "publications/wm-xct-003-projection-disclosure-policy/spec.yaml",
    "WM-MAT-008": "publications/wm-mat-008-observation-measurement-record/spec.yaml",
}
dossier = {
    "contour": next(x for x in registry["units"] if x["id"] == "EM-PEO-09"),
    "queue": next(x for x in queue["units"] if x["id"] == "EM-PEO-09"),
    "reservations": [x for x in unified if x.get("model_id") in IDS],
    "relations": [x for x in relations if x.get("source_model_id") in IDS or x.get("target_model_id") in IDS],
    "specs": {key: compact(W / value) for key, value in specs.items()},
    "prior_research": {
        "EM-PEO-02": text_document(W / "research/enterprise/runs/em-peo-02/local-evidence.md"),
        "EM-PEO-08": text_document(W / "research/enterprise/runs/em-peo-08/local-evidence.md"),
        "EM-FIN-05": text_document(W / "research/enterprise/runs/em-fin-05/local-evidence.md"),
        "EM-DAT-01": text_document(W / "research/enterprise/runs/em-dat-01/local-evidence.md"),
    },
}
R.mkdir(parents=True, exist_ok=True)
dossier_path = R / "provider-dossier.json"
dossier_path.write_text(json.dumps(dossier, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
prompt = """Independent enterprise metamodel review. Use only the frozen dossier; no tools, browsing or invented identifiers. Adjudicate EM-PEO-09 Compensation and Benefits. There are no preassigned target IDs. Complete drafts cover Payroll / Compensation, Employment, Position, Money / Instrument, Price / Valuation, Decision / Approval Record, Payment, Projection / Disclosure Policy and Observation / Measurement; Privacy Aggregation Floor and Public Benefit / Program are reservations without current specs. Candidates are CompensationBand, CompensationAssignment, BenefitPlan, BenefitEnrollment and CompensationReview. Decide reuse/profile/new by independent identity and lifecycle without allocating identifiers. Separate position salary range, grade/band definition, person compensation terms, employment agreement, periodic review, approval decision, payroll calculation, payslip, payment, statutory contribution, benefit-plan definition, eligibility rule, election/enrollment, coverage period, claim/use, valuation and aggregate disclosure. Determine which semantics can profile WM-ECO-031 and which require new roots. Every amount pins currency, unit/basis, period, frequency, FTE/working-time normalization and source authority. Range is not an individual assignment; payment facts come from financial sources. Multiple currencies and mid-period changes require effective-dated components and explicit FX source/time, never silent conversion. Aggregate publishing must resist reconstruction through small groups, differencing, repeated queries and joins, with governed suppression and audit. Test part-time work, multiple currencies, a mid-period term change, benefit enrollment independent of payroll, and an unsafe singleton/differencing aggregate. Return <=1200 words with headings Verdict; Evidence; Identity/mastership; Band/range; Assignment/components; Review/decision; Benefit plan/enrollment; Payroll/payment; Currency/time; Aggregation/privacy; Acceptance scenario; Invariants; Minimal model set; Holds. Explicitly decide all candidates, distinguish employee benefits from WM-POL-012 public benefit, and identify relation/spec gaps. Do not claim canonical completeness, installability or publication readiness.

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
