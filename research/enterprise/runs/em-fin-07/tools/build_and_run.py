import csv, hashlib, json, subprocess
from pathlib import Path
import yaml

W = Path(r"R:\02_PROJECTS\02_Meta_Models_Platforms\Ver.cy\current\ver-cy\world-models")
R = W / "research/enterprise/runs/em-fin-07"
IDS = {"WM-POL-011", "WM-ECO-032", "WM-ACT-052", "WM-POL-001", "WM-POL-015", "WM-ORG-001", "WM-ORG-010", "WM-ECO-009"}

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
    "WM-POL-011": "publications/wm-pol-011-tax-obligation-assessment/spec.yaml",
    "WM-ECO-032": "publications/wm-eco-032-tax-return-filing/spec.yaml",
    "WM-ACT-052": "publications/wm-act-052-tax-filing-assessment-process/spec.yaml",
    "WM-POL-001": "publications/wm-pol-001-legal-instrument-norm/spec.yaml",
    "WM-POL-015": "publications/wm-pol-015-jurisdiction/spec.yaml",
    "WM-ORG-001": "publications/wm-org-001-organization/spec.yaml",
    "WM-ORG-010": "publications/wm-org-010-legal-entity-registration/spec.yaml",
    "WM-ECO-009": "publications/wm-eco-009-payment/spec.yaml",
}
dossier = {
    "contour": next(x for x in registry["units"] if x["id"] == "EM-FIN-07"),
    "queue": next(x for x in queue["units"] if x["id"] == "EM-FIN-07"),
    "reservations": [x for x in unified if x.get("model_id") in IDS],
    "relations": [x for x in relations if x.get("source_model_id") in IDS or x.get("target_model_id") in IDS],
    "specs": {key: compact(W / value) for key, value in specs.items()},
    "prior_research": {
        "EM-LEG-02": text_document(W / "research/enterprise/runs/em-leg-02/local-evidence.md"),
        "EM-ORG-02": text_document(W / "research/enterprise/runs/em-org-02/local-evidence.md"),
        "EM-FIN-03": text_document(W / "research/enterprise/runs/em-fin-03/local-evidence.md"),
        "EM-FIN-02": text_document(W / "research/enterprise/runs/em-fin-02/local-evidence.md"),
        "EM-RSK-02": text_document(W / "research/enterprise/runs/em-rsk-02/local-evidence.md"),
    },
}
R.mkdir(parents=True, exist_ok=True)
dossier_path = R / "provider-dossier.json"
dossier_path.write_text(json.dumps(dossier, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
prompt = """Independent enterprise metamodel review. Use only the frozen dossier; no tools, browsing or invented identifiers. Adjudicate EM-FIN-07 Tax Profile, Obligation and Filing using complete WM-POL-011 Tax Obligation / Assessment, WM-ECO-032 Tax Return / Filing, WM-ACT-052 Tax Filing / Assessment Process, Legal Instrument / Norm, Jurisdiction, Organization, Legal Entity Registration and Payment drafts plus prior boundary work. Candidate types are TaxProfile, TaxObligation, TaxCalculation, TaxReturn and TaxFiling. Decide reuse/profile/new by independent identity and lifecycle without allocating identifiers. Separate taxpayer identity, legal registration, tax registration/account, residence, source/place/nexus, jurisdiction, versioned legal rule, obligation, taxable event, period, calculation assertion, return revision, filing attempt, acknowledgement, authority assessment, notice, balance, payment/allocation, dispute and process case. Determine whether WM-POL-011 already owns TaxProfile and TaxObligation; whether TaxCalculation is an obligation/return assertion or an independent reusable run; whether WM-ECO-032 owns both TaxReturn and filing attempt; and whether WM-ACT-052 is a useful case aggregate or duplicates the two subject masters. Preserve multiple concurrent jurisdictional bases and never infer every obligation from an office address. Pin applicable law/rule/form/schema/taxonomy/rate versions to effective periods and knowledge time. Submitted return revisions and filing attempts are immutable facts; corrections append successors. Receipt, technical acceptance, assessment, liability, payment and finality remain distinct. Test one taxpayer with residence/source/nexus bases in two jurisdictions, two obligations and an amended return, preserving distinct grounds, calculation versions, receipts and authority responses. Return <=1200 words with headings Verdict; Evidence; Identity/mastership; Tax profile/registration/nexus; Obligation/rules/period; Calculation; Return/filing; Assessment/payment/dispute; Multi-jurisdiction; Time/version/provenance; Governance/privacy; Acceptance scenario; Invariants; Minimal model set; Holds. Explicitly decide which candidates need independent identity, identify duplicate roots and contradictions, and do not state current law or tax rates. Do not claim canonical completeness, installability or publication readiness.

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
