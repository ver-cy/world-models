import csv, hashlib, json, subprocess
from pathlib import Path
import yaml

W = Path(r"R:\02_PROJECTS\02_Meta_Models_Platforms\Ver.cy\current\ver-cy\world-models")
R = W / "research/enterprise/runs/em-fin-06"
IDS = {"WM-ECO-038", "WM-ECO-002", "WM-ECO-016", "WM-ORG-001", "WM-ORG-012", "WM-ORG-018"}

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
    "WM-ECO-038": "publications/wm-eco-038-equity-security-holding/spec.yaml",
    "WM-ECO-002": "publications/wm-eco-002-price-valuation/spec.yaml",
    "WM-ECO-016": "publications/wm-eco-016-financial-transaction-journal-entry/spec.yaml",
    "WM-ORG-001": "publications/wm-org-001-organization/spec.yaml",
    "WM-ORG-012": "publications/wm-org-012-inter-organizational-relationship/spec.yaml",
    "WM-ORG-018": "publications/wm-org-018-governance-body-committee/spec.yaml",
}
dossier = {
    "contour": next(x for x in registry["units"] if x["id"] == "EM-FIN-06"),
    "queue": next(x for x in queue["units"] if x["id"] == "EM-FIN-06"),
    "reservations": [x for x in unified if x.get("model_id") in IDS],
    "relations": [x for x in relations if x.get("source_model_id") in IDS or x.get("target_model_id") in IDS],
    "specs": {key: compact(W / value) for key, value in specs.items()},
    "prior_research": {
        "EM-FIN-02": text_document(W / "research/enterprise/runs/em-fin-02/local-evidence.md"),
        "EM-FIN-04": text_document(W / "research/enterprise/runs/em-fin-04/local-evidence.md"),
        "EM-FIN-05": text_document(W / "research/enterprise/runs/em-fin-05/local-evidence.md"),
        "EM-ORG-03": text_document(W / "research/enterprise/runs/em-org-03/local-evidence.md"),
        "EM-LEG-04": text_document(W / "research/enterprise/runs/em-leg-04/local-evidence.md"),
    },
}
R.mkdir(parents=True, exist_ok=True)
dossier_path = R / "provider-dossier.json"
dossier_path.write_text(json.dumps(dossier, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
prompt = """Independent enterprise metamodel review. Use only the frozen dossier; no tools, browsing or invented identifiers. Adjudicate EM-FIN-06 Investments, Instruments and Valuation using complete WM-ECO-038 Equity / Security Holding, WM-ECO-002 Price / Valuation, WM-ECO-016 Financial Transaction / Journal Entry, Organization, Inter-organizational Relationship and Governance Body drafts plus prior boundary work. Candidate types are Investment, FinancialInstrument, InvestmentTransaction and Valuation. Decide reuse/profile/new by independent identity and lifecycle without allocating identifiers. Separate the investee or underlying asset, issued instrument, investor position/holding, acquisition or disposal transaction, journal posting, valuation assertion, contractual conversion right, conversion event, corporate ownership, voting power, control and consolidation scope. Determine whether WM-ECO-038 is only an equity/security position master or can own generic investment semantics; whether FinancialInstrument requires an independent master; whether Investment is a position profile, portfolio relationship or independent aggregate; whether InvestmentTransaction should reuse transaction masters; and whether Valuation should reuse/profile WM-ECO-002. Require immutable instrument terms and versions, issuer and holder capacities, quantities and units, acquisition lots, rights and restrictions, effective/observation/knowledge times, method/basis/currency, assumptions, inputs, model version, source evidence, uncertainty, review, supersession and lineage. For a convertible instrument, keep conversion terms and contingent future rights distinct from current equity/voting rights; conversion must be an explicit event that creates successor holdings and accounting effects. Test one convertible instrument and two same-date valuations under different methods/currencies, preserving divergence and provenance. Reject the latest company valuation as an automatic source of investor voting or control rights. Return <=1200 words with headings Verdict; Evidence; Identity/mastership; Instrument/investment/holding; Transactions/postings; Valuation; Convertible rights and conversion; Ownership/voting/control/consolidation; Time/currency/provenance; Governance/assurance; Acceptance scenario; Invariants; Minimal model set; Holds. Explicitly decide which candidates need independent identity and identify gaps or contradictions. Do not claim canonical completeness, installability or publication readiness.

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
