import csv, hashlib, json, subprocess
from pathlib import Path
import yaml

W = Path(r"R:\02_PROJECTS\02_Meta_Models_Platforms\Ver.cy\current\ver-cy\world-models")
R = W / "research/enterprise/runs/em-peo-08"
IDS = {
    "WM-ORG-004", "WM-XCT-023", "WM-ACT-034", "WM-PER-008", "WM-REC-010",
    "WM-ORG-005", "WM-ECO-031", "WM-PER-009", "WM-XCT-017"
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
    "WM-ORG-004": "publications/wm-org-004-position/spec.yaml",
    "WM-XCT-023": "publications/wm-xct-023-party-role/spec.yaml",
    "WM-ACT-034": "publications/wm-act-034-assessment-evaluation/spec.yaml",
    "WM-PER-008": "publications/wm-per-008-education-qualification/spec.yaml",
    "WM-REC-010": "publications/wm-rec-010-decision-approval-record/spec.yaml",
    "WM-ORG-005": "publications/wm-org-005-employment/spec.yaml",
    "WM-ECO-031": "publications/wm-eco-031-payroll-compensation/spec.yaml",
    "WM-XCT-017": "publications/wm-xct-017-attestation-credential/spec.yaml",
}
dossier = {
    "contour": next(x for x in registry["units"] if x["id"] == "EM-PEO-08"),
    "queue": next(x for x in queue["units"] if x["id"] == "EM-PEO-08"),
    "reservations": [x for x in unified if x.get("model_id") in IDS],
    "relations": [x for x in relations if x.get("source_model_id") in IDS or x.get("target_model_id") in IDS],
    "specs": {key: compact(W / value) for key, value in specs.items()},
    "prior_research": {
        "EM-ORG-06": text_document(W / "research/enterprise/runs/em-org-06/local-evidence.md"),
        "EM-PEO-02": text_document(W / "research/enterprise/runs/em-peo-02/local-evidence.md"),
        "EM-PEO-03": text_document(W / "research/enterprise/runs/em-peo-03/local-evidence.md"),
        "EM-PEO-05": text_document(W / "research/enterprise/runs/em-peo-05/local-evidence.md"),
    },
}
R.mkdir(parents=True, exist_ok=True)
dossier_path = R / "provider-dossier.json"
dossier_path.write_text(json.dumps(dossier, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
prompt = """Independent enterprise metamodel review. Use only the frozen dossier; no tools, browsing or invented identifiers. Adjudicate EM-PEO-08 Grades and Expectation Profiles. There are no preassigned target IDs. Complete drafts cover Position, Party Role, Assessment / Evaluation, Education / Qualification, Decision / Approval Record, Employment, Payroll / Compensation and Attestation / Credential; WM-PER-009 Skill / Competency is reserved but lacks a current spec. Candidates are GradeScheme, GradeLevel, RoleProfile, GradeAssignment and GradeCalibration. Decide reuse/profile/new by independent identity and lifecycle without allocating identifiers. Separate job grade/level, skill proficiency, performance rating, qualification level, compensation band, role concept, position expectations, person grade assignment, assessment evidence, calibration session/result, appointment, pay decision and payroll fact. Determine whether Grade Scheme owns Grade Levels; whether Role Profile is a versioned definition referencing Party Role/Position and competency expectations; whether Grade Assignment needs an independent assertion root or profiles a decision/employment relation; and whether Grade Calibration is a process, assessment or decision profile. Mapping between two company ladders must be version-pinned, partial, directional, purpose-qualified and loss-declaring; matching labels or ordinals never prove equivalence. A grade decision must not automatically change pay, position, qualification or access. Test two ladders of different dimensionality, an unmappable level, a historical reassessment, and a compensation change requiring its own authority. Protect performance and calibration evidence by purpose and minimum disclosure. Return <=1200 words with headings Verdict; Evidence; Identity/mastership; Grade scheme/levels; Role profile; Assignment; Calibration; Crosswalk/merger; Competency/qualification/performance; Compensation/position/access; Privacy/retention; Time/provenance; Acceptance scenario; Invariants; Minimal model set; Holds. Explicitly decide all candidates and relation/spec gaps. Do not claim canonical completeness, installability or publication readiness.

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
