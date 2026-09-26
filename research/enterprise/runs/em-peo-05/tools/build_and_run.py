import csv, hashlib, json, subprocess
from pathlib import Path
import yaml

W = Path(r"R:\02_PROJECTS\02_Meta_Models_Platforms\Ver.cy\current\ver-cy\world-models")
R = W / "research/enterprise/runs/em-peo-05"
IDS = {
    "WM-ACT-038", "WM-PER-008", "WM-ACT-034", "WM-XCT-017",
    "WM-ACT-008", "WM-REC-010", "WM-ORG-004", "WM-ORG-016", "WM-PER-009"
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
    "WM-ACT-038": "publications/wm-act-038-learning-activity-course-delivery/spec.yaml",
    "WM-PER-008": "publications/wm-per-008-education-qualification/spec.yaml",
    "WM-ACT-034": "publications/wm-act-034-assessment-evaluation/spec.yaml",
    "WM-XCT-017": "publications/wm-xct-017-attestation-credential/spec.yaml",
    "WM-ACT-008": "publications/wm-act-008-plan-schedule/spec.yaml",
    "WM-REC-010": "publications/wm-rec-010-decision-approval-record/spec.yaml",
    "WM-ORG-004": "publications/wm-org-004-position/spec.yaml",
    "WM-ORG-016": "publications/wm-org-016-work-assignment/spec.yaml",
}
dossier = {
    "contour": next(x for x in registry["units"] if x["id"] == "EM-PEO-05"),
    "queue": next(x for x in queue["units"] if x["id"] == "EM-PEO-05"),
    "reservations": [x for x in unified if x.get("model_id") in IDS],
    "relations": [x for x in relations if x.get("source_model_id") in IDS or x.get("target_model_id") in IDS],
    "specs": {key: compact(W / value) for key, value in specs.items()},
    "prior_research": {
        "EM-PEO-03": text_document(W / "research/enterprise/runs/em-peo-03/local-evidence.md"),
        "EM-PEO-04": text_document(W / "research/enterprise/runs/em-peo-04/local-evidence.md"),
        "EM-WRK-02": text_document(W / "research/enterprise/runs/em-wrk-02/local-evidence.md"),
        "EM-ORG-06": text_document(W / "research/enterprise/runs/em-org-06/local-evidence.md"),
    },
}
R.mkdir(parents=True, exist_ok=True)
dossier_path = R / "provider-dossier.json"
dossier_path.write_text(json.dumps(dossier, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
prompt = """Independent enterprise metamodel review. Use only the frozen dossier; no tools, browsing or invented identifiers. Adjudicate EM-PEO-05 Learning, Development and Succession using complete WM-ACT-038 Learning Activity / Course Delivery plus complete Education / Qualification, Assessment / Evaluation, Attestation / Credential, Plan / Schedule, Decision / Approval Record, Position and Work Assignment drafts and prior boundary work. Candidate types are LearningProgram, Enrollment, LearningResult, DevelopmentPlan, CareerPath and SuccessionPlan. Decide reuse/profile/new by independent identity and lifecycle without allocating identifiers. Separate reusable learning definition/program/version, scheduled delivery/cohort, enrollment/participation, attendance/completion, assessed learning result, competency assertion, qualification award, credential, personal development plan, career aspiration/path, succession plan, readiness assessment, nomination, appointment and current assignment. Decide whether WM-ACT-038 currently owns definition and delivery or must be narrowed; whether Enrollment and LearningResult are aggregate-owned or independent roots; whether DevelopmentPlan can profile WM-ACT-008; and whether CareerPath and SuccessionPlan require roots. A plan is not a personnel decision, a readiness label is not appointment or access, and a learning result pins the objective/version and assessment basis. Protect sensitive potential/readiness ratings with purpose, minimum disclosure, review interval and challenge/correction route. Test one course serving two distinct development objectives, one learner completing attendance but failing assessment, a revised succession plan that leaves current assignments unchanged, and a later appointment requiring an explicit decision. Return <=1200 words with headings Verdict; Evidence; Identity/mastership; Learning definition/delivery; Enrollment/participation; Result/qualification/credential; Development plan; Career path; Succession/readiness; Decision/appointment/access; Privacy/retention; Time/provenance; Acceptance scenario; Invariants; Minimal model set; Holds. Explicitly decide all candidates and relation/spec gaps. Do not claim canonical completeness, installability or publication readiness.

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
