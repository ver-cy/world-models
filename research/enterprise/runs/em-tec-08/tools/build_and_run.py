import csv, hashlib, json, subprocess
from pathlib import Path

import yaml

W = Path(r"R:\02_PROJECTS\02_Meta_Models_Platforms\Ver.cy\current\ver-cy\world-models")
R = W / "research/enterprise/runs/em-tec-08"
IDS = {"WM-SFT-015", "WM-SFT-014", "WM-ACT-006", "WM-REC-006", "WM-SFT-008", "WM-ACT-038"}


def read_json(path):
    return json.loads(path.read_text(encoding="utf-8-sig"))


def read_rows(path):
    with path.open(encoding="utf-8-sig", newline="") as handle:
        return list(csv.DictReader(handle))


def full_spec(path):
    raw = path.read_bytes()
    return {"bytes": len(raw), "sha256": hashlib.sha256(raw).hexdigest(), "document": yaml.safe_load(raw.decode("utf-8-sig"))}


registry = read_json(W / "research/enterprise/registry.json")
queue = read_json(W / "research/enterprise/queue.json")
unified = read_rows(W / "planning/VERCY-UNIFIED-MEGA-REGISTRY.csv")
relations = read_rows(W / "planning/VERCY-MODEL-RELATIONS.csv")

dossier = {
    "contour": next(x for x in registry["units"] if x["id"] == "EM-TEC-08"),
    "queue": next(x for x in queue["units"] if x["id"] == "EM-TEC-08"),
    "reservations": [x for x in unified if x.get("model_id") in IDS],
    "relations": [x for x in relations if x.get("source_model_id") in IDS or x.get("target_model_id") in IDS],
    "specs": {
        "WM-SFT-015": full_spec(W / "publications/wm-sft-015-test-case-test-result/spec.yaml"),
        "WM-SFT-014": full_spec(W / "publications/wm-sft-014-defect-bug/spec.yaml"),
        "WM-ACT-006": full_spec(W / "publications/wm-act-006-task/spec.yaml"),
        "WM-SFT-008": full_spec(W / "publications/wm-sft-008-build-release/spec.yaml"),
    },
    "missing_specs": {
        "WM-REC-006": "Reserved Requirement candidate has no current publication specification in this dossier.",
        "WM-ACT-038": "Its existing model is Learning Activity / Course Delivery and is not a generic testing parent despite registry parentage from WM-SFT-015.",
    },
    "prior_adjudication": {
        "EM-PRD-03": "WM-REC-006 is the Requirement aggregate with criteria, baselines and trace records.",
        "EM-TEC-05": "WM-SFT-014 owns software defect lifecycle and WM-ACT-006 owns remediation work.",
    },
}

R.mkdir(parents=True, exist_ok=True)
p = R / "provider-dossier.json"
p.write_text(json.dumps(dossier, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")

prompt = """Independent enterprise metamodel review. Use only the frozen dossier; no tools, browsing or invented identifiers. Decide EM-TEC-08 Testing, Verification and Defect against WM-SFT-015 Test Case / Test Result, WM-SFT-014 Defect / Bug, WM-ACT-006 Task, WM-REC-006 Requirement and WM-SFT-008 Build / Release. Determine boundaries and identities for TestSpecification, TestRun, TestResult, VerificationEvidence and Defect. Separate expected behavior from executable test implementation; distinguish product defect, test defect, environment failure and inconclusive/flaky result; pin exact subject versions and environments. Test one defect linked to multiple tests, a flaky run and re-verification against a different version. Ensure fixing a test never closes a product defect automatically. Evaluate the apparent incorrect parent WM-ACT-038. Return <=1200 words with headings Verdict; Evidence; Identity/mastership; Specification/run/result/evidence; Defect classification; Version/environment binding; Flaky and inconclusive; Lifecycle and closure; Scenario; Invariants; Minimal completion shape; Holds. Do not claim canonical completeness or installability.\n\nDOSSIER\n""" + p.read_text(encoding="utf-8")

result = subprocess.run(["claude", "-p", "--model", "opus", "--effort", "high", "--tools", ""], input=prompt, text=True, encoding="utf-8", errors="replace", capture_output=True, timeout=900)
if result.returncode:
    raise SystemExit(result.stderr)
(R / "claude-study.raw.md").write_text(result.stdout.rstrip() + "\n", encoding="utf-8")
print(p.stat().st_size, len(result.stdout))
