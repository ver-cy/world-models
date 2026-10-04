import csv, hashlib, json, subprocess
from pathlib import Path
import yaml

W = Path(r"R:\02_PROJECTS\02_Meta_Models_Platforms\Ver.cy\current\ver-cy\world-models")
R = W / "research/enterprise/runs/em-peo-04"
IDS = {'WM-ORG-008', 'WM-ACT-039', 'WM-ORG-004', 'WM-ORG-005', 'WM-PER-001', 'WM-ECO-021', 'WM-ACT-034', 'WM-ACT-025', 'WM-REC-010'}

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
    "WM-ACT-039": "publications/wm-act-039-recruitment-hiring-process/spec.yaml",
    "WM-ORG-004": "publications/wm-org-004-position/spec.yaml",
    "WM-ORG-005": "publications/wm-org-005-employment/spec.yaml",
    "WM-PER-001": "publications/wm-per-001-person/spec.yaml",
    "WM-ECO-021": "publications/wm-eco-021-offer-quote/spec.yaml",
    "WM-ACT-034": "publications/wm-act-034-assessment-evaluation/spec.yaml",
    "WM-ACT-025": "publications/wm-act-025-meeting-session/spec.yaml",
    "WM-REC-010": "publications/wm-rec-010-decision-approval-record/spec.yaml",
}
dossier = {
    "contour": next(x for x in registry["units"] if x["id"] == "EM-PEO-04"),
    "queue": next(x for x in queue["units"] if x["id"] == "EM-PEO-04"),
    "reservations": [x for x in unified if x.get("model_id") in IDS],
    "relations": [x for x in relations if x.get("source_model_id") in IDS or x.get("target_model_id") in IDS],
    "specs": {key: compact(W / value) for key, value in specs.items()},
    "prior_research": {
        "EM-ORG-06": text_document(W / "research/enterprise/runs/em-org-06/local-evidence.md"),
        "EM-PEO-01": text_document(W / "research/enterprise/runs/em-peo-01/local-evidence.md"),
        "EM-PEO-02": text_document(W / "research/enterprise/runs/em-peo-02/local-evidence.md"),
        "EM-PEO-03": text_document(W / "research/enterprise/runs/em-peo-03/local-evidence.md"),
        "EM-FIN-01": text_document(W / "research/enterprise/runs/em-fin-01/local-evidence.md"),
    },
}
R.mkdir(parents=True, exist_ok=True)
dossier_path = R / "provider-dossier.json"
dossier_path.write_text(json.dumps(dossier, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
prompt = """Independent enterprise metamodel review. Use only the frozen dossier; no tools, browsing or invented identifiers. Adjudicate EM-PEO-04 Recruitment and Hiring using reserved-but-missing WM-ORG-008 Vacancy / Matching plus complete WM-ACT-039 Recruitment / Hiring Process, Position, Employment, Person, Offer / Quote, Assessment, Meeting / Session and Decision / Approval drafts and prior boundary work. Candidate types are RecruitmentRequisition, Vacancy, Application, HiringStage, InterviewAssessment and Offer. Decide reuse/profile/new by independent identity and lifecycle without allocating identifiers. Separate approved hiring need/requisition, durable position, vacancy/opening, public posting, person, candidate identity, application/candidacy, process/campaign, stage definition/occurrence, interview session, assessment result, accountable selection decision, offer proposal, contract, assignment and employment. Determine what WM-ORG-008 must own if completed and whether it currently collapses Vacancy, Application and Matching; decide whether RecruitmentRequisition needs a root or profiles a request/authorization master; keep HiringStage process-owned; profile InterviewAssessment over assessment plus meeting/evidence; decide whether hiring Offer can profile WM-ECO-021 without importing commercial product semantics. One requisition may authorize two seats; one person may have several candidacies without duplicate Person. Offer withdrawal and later rehiring preserve lineage. CV possession is never unlimited consent: purpose, group company, retention trigger, withdrawal, legal hold and minimal disclosure are explicit. Test one requisition for two positions, three candidacies, withdrawn offer and later rehire. Return <=1200 words with headings Verdict; Evidence; Identity/mastership; Requisition/position/vacancy; Person/candidate/application; Process/stages; Interview/assessment/decision; Offer/employment; Privacy/retention; Time/provenance; Governance/fairness; Acceptance scenario; Invariants; Minimal model set; Holds. Explicitly decide all candidates, note missing WM-ORG-008 spec and relation gaps. Do not claim canonical completeness, installability or publication readiness.

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
