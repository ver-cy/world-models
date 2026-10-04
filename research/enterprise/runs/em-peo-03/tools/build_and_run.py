import csv, hashlib, json, subprocess
from pathlib import Path
import yaml

W = Path(r"R:\02_PROJECTS\02_Meta_Models_Platforms\Ver.cy\current\ver-cy\world-models")
R = W / "research/enterprise/runs/em-peo-03"
IDS = {'WM-PER-009', 'WM-PER-008', 'WM-PER-013', 'WM-ACT-034', 'WM-XCT-017', 'WM-ORG-004', 'WM-PER-001', 'WM-KNW-005'}

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
    "WM-PER-008": "publications/wm-per-008-education-qualification/spec.yaml",
    "WM-PER-013": "publications/wm-per-013-professional-license-credential/spec.yaml",
    "WM-ACT-034": "publications/wm-act-034-assessment-evaluation/spec.yaml",
    "WM-XCT-017": "publications/wm-xct-017-attestation-credential/spec.yaml",
    "WM-ORG-004": "publications/wm-org-004-position/spec.yaml",
    "WM-PER-001": "publications/wm-per-001-person/spec.yaml",
    "WM-KNW-005": "publications/wm-knw-005-agent-skill-instruction/spec.yaml",
}
dossier = {
    "contour": next(x for x in registry["units"] if x["id"] == "EM-PEO-03"),
    "queue": next(x for x in queue["units"] if x["id"] == "EM-PEO-03"),
    "reservations": [x for x in unified if x.get("model_id") in IDS],
    "relations": [x for x in relations if x.get("source_model_id") in IDS or x.get("target_model_id") in IDS],
    "specs": {key: compact(W / value) for key, value in specs.items()},
    "prior_research": {
        "EM-PEO-01": text_document(W / "research/enterprise/runs/em-peo-01/local-evidence.md"),
        "EM-ORG-06": text_document(W / "research/enterprise/runs/em-org-06/local-evidence.md"),
        "EM-DAT-07": text_document(W / "research/enterprise/runs/em-dat-07/local-evidence.md"),
        "EM-KNW-02": text_document(W / "research/enterprise/runs/em-knw-02/local-evidence.md"),
        "EM-STR-03": text_document(W / "research/enterprise/runs/em-str-03/local-evidence.md"),
    },
}
R.mkdir(parents=True, exist_ok=True)
dossier_path = R / "provider-dossier.json"
dossier_path.write_text(json.dumps(dossier, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
prompt = """Independent enterprise metamodel review. Use only the frozen dossier; no tools, browsing or invented identifiers. Adjudicate EM-PEO-03 Competencies and Qualifications using the reserved-but-missing WM-PER-009 Skill / Competency boundary plus complete WM-PER-008 Education / Qualification, WM-PER-013 Professional Licence / Credential, WM-ACT-034 Assessment / Evaluation, WM-XCT-017 Attestation / Credential, Position, Person and Agent Skill / Instruction drafts and prior boundary work. Candidate types are Competency, Skill, ProficiencyScale, CompetencyAssessment, Qualification and Credential. Decide reuse/profile/new by independent identity and lifecycle without allocating identifiers. Separate skill/competency definition, proficiency scale/version, mapping between schemes, person capability assertion, assessment event/result, self-assessment, verified evidence, education qualification, professional licence, credential/attestation, role expectation and course completion. Determine what WM-PER-009 must own if completed; whether Skill and Competency are aliases, related but distinct definitions, or profiles; whether scale requires an independent versioned root; profile competency assessment over WM-ACT-034; reuse qualification and credential roots without conflating issue, verification, validity and current competence. Compare ESCO, SFIA and local schemes only as versioned mappings with loss; never invent exact level equivalence. Completed course does not imply expert proficiency. Test one competency assessed by different methods and scales, one expired certificate, and a lossy mapping. Return <=1200 words with headings Verdict; Evidence; Identity/mastership; Skill/competency definitions; Scales/mappings; Person assertions; Assessment/evidence; Qualification/credential/licence; Role/course boundary; Time/provenance/privacy; Governance; Acceptance scenario; Invariants; Minimal model set; Holds. Explicitly decide all candidates, note WM-PER-009 missing spec and relation gaps. Do not claim canonical completeness, installability or publication readiness.

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
