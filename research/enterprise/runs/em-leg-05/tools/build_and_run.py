import csv, hashlib, json, subprocess
from pathlib import Path
import yaml

W = Path(r"R:\02_PROJECTS\02_Meta_Models_Platforms\Ver.cy\current\ver-cy\world-models")
R = W / "research/enterprise/runs/em-leg-05"
IDS = {"WM-POL-009", "WM-POL-019", "WM-POL-020", "WM-POL-021", "WM-POL-022", "WM-KNW-007", "WM-KNW-008", "WM-KNW-010", "WM-ECO-006", "WM-ECO-018"}

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
    "WM-POL-009": "publications/wm-pol-009-court-arbitration-case/spec.yaml",
    "WM-KNW-007": "publications/wm-knw-007-claim-proposition/spec.yaml",
    "WM-KNW-008": "publications/wm-knw-008-evidence-citation/spec.yaml",
    "WM-KNW-010": "publications/wm-knw-010-decision-rationale/spec.yaml",
    "WM-ECO-006": "publications/wm-eco-006-commercial-contract/spec.yaml",
    "WM-ECO-018": "publications/wm-eco-018-financial-statement/spec.yaml",
}
dossier = {
    "contour": next(x for x in registry["units"] if x["id"] == "EM-LEG-05"),
    "queue": next(x for x in queue["units"] if x["id"] == "EM-LEG-05"),
    "reservations": [x for x in unified if x.get("model_id") in IDS],
    "relations": [x for x in relations if x.get("source_model_id") in IDS or x.get("target_model_id") in IDS],
    "specs": {key: compact(W / value) for key, value in specs.items()},
    "prior_research": {
        "EM-KNW-02": text_document(W / "research/enterprise/runs/em-knw-02/local-evidence.md"),
        "EM-LEG-02": text_document(W / "research/enterprise/runs/em-leg-02/local-evidence.md"),
        "EM-LEG-04": text_document(W / "research/enterprise/runs/em-leg-04/local-evidence.md"),
        "EM-FIN-04": text_document(W / "research/enterprise/runs/em-fin-04/local-evidence.md"),
        "EM-RSK-02": text_document(W / "research/enterprise/runs/em-rsk-02/local-evidence.md"),
    },
}
R.mkdir(parents=True, exist_ok=True)
dossier_path = R / "provider-dossier.json"
dossier_path.write_text(json.dumps(dossier, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
prompt = """Independent enterprise metamodel review. Use only the frozen dossier; no tools, browsing or invented identifiers. Adjudicate EM-LEG-05 Legal Case and Dispute using complete WM-POL-009 Court / Arbitration Case plus Claim / Proposition, Evidence / Citation, Decision / Rationale, Commercial Contract and Financial Statement drafts; include reservations for missing WM-POL-019 Filing, WM-POL-020 Evidence Item, WM-POL-021 Judgment and WM-POL-022 Appeal / Review; use prior boundary work. Candidate types are LegalCase, Claim, ProceedingEvent and CaseOutcome. Decide reuse/profile/new by independent identity and lifecycle without allocating identifiers. Separate underlying dispute, proceeding/case, forum, party role, pleading, party allegation, counterclaim, defense, issue, evidence item, admissibility/use assertion, procedural event/order, finding of fact, legal conclusion, judgment/award, remedy, appeal/review, enforcement, financial provision and confirmed debt. Determine whether WM-POL-009 fully covers LegalCase; whether Claim belongs as a case-owned procedural assertion, a WM-KNW-007 profile or an independent root; whether ProceedingEvent is case-owned; whether CaseOutcome is a view/profile over judgment and finality rather than a root; and how multiple proceedings of one dispute and appeals preserve lineage. Reject a claimed amount as confirmed debt. Require author, procedural capacity, asserted fact vs adjudicated finding, burden/standard, evidence provenance, forum authority, effective/service/knowledge times, access/sealing/redaction, finality and non-destructive reversal. Test a dispute with claim and counterclaim, a first-instance decision later set aside on appeal, continuing evidence restrictions and financial provisioning that never becomes legal debt automatically. Return <=1200 words with headings Verdict; Evidence; Identity/mastership; Dispute/case/proceedings; Claims/allegations/findings; Events/filings/evidence; Decisions/outcomes/remedies; Appeal/review/enforcement; Finance boundary; Time/provenance/access; Governance; Acceptance scenario; Invariants; Minimal model set; Holds. Explicitly decide candidates and flag missing reserved specs and relation contradictions. Do not claim canonical completeness, installability or publication readiness.

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
