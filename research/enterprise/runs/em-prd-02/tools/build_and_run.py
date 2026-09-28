import csv, hashlib, json, subprocess
from pathlib import Path

W = Path(__file__).resolve().parents[5]
R = W / "research/enterprise/runs/em-prd-02"
MODEL_ID = "WM-ACT-004"


def read_json(path):
    return json.loads(path.read_text(encoding="utf-8-sig"))


def read_rows(path):
    with path.open(encoding="utf-8-sig", newline="") as handle:
        return list(csv.DictReader(handle))


registry = read_json(W / "research/enterprise/registry.json")
queue = read_json(W / "research/enterprise/queue.json")
unified = read_rows(W / "planning/VERCY-UNIFIED-MEGA-REGISTRY.csv")
relations = read_rows(W / "planning/VERCY-MODEL-RELATIONS.csv")
spec_path = W / "models/activity-work/K4-service.md"
raw = spec_path.read_bytes()

dossier = {
    "contour": next(item for item in registry["units"] if item["id"] == "EM-PRD-02"),
    "queue": next(item for item in queue["units"] if item["id"] == "EM-PRD-02"),
    "reservation": next(item for item in unified if item.get("model_id") == MODEL_ID),
    "relations": [
        item
        for item in relations
        if item.get("source_model_id") == MODEL_ID
        or item.get("target_model_id") == MODEL_ID
    ],
    "complete_current_spec": {
        "path": "models/activity-work/K4-service.md",
        "bytes": len(raw),
        "sha256": hashlib.sha256(raw).hexdigest(),
        "content": raw.decode("utf-8-sig"),
    },
    "limits": [
        "WM-ACT-004 is a described previous-version reservation under migration boundary review, not a canonical published package.",
        "The supplied specification is complete for the current repository state but predates current research assurance and must not be treated as canonical.",
    ],
}

R.mkdir(parents=True, exist_ok=True)
dossier_path = R / "provider-dossier.json"
dossier_path.write_text(
    json.dumps(dossier, ensure_ascii=False, indent=2) + "\n", encoding="utf-8"
)

prompt = """Independent enterprise metamodel review. Use only the dossier; no tools, browsing, or invented identifiers. Decide EM-PRD-02 Service and Service Model against reserved WM-ACT-004 Service. Determine whether to complete the reserved model, profile it, split it, or propose identifier-unassigned peers only where identity, lifecycle and mastership prove independence. Separate: durable Service definition and expected outcome; market/internal Service Offering and its terms; Service Consumption or entitlement/relationship; request/case; delivery episode/runtime realization; Service Dependency; SLA/quality commitment; measured quality observation; provider, consumer and technical API client. The enterprise scope delegates runtime instances and service-level agreements. An API endpoint must not automatically become a business service. Test an HR service and a digital platform service with multiple providers/realizations and the same outcome semantics; allow internal services with no price. Return <=1200 words with headings Verdict; Evidence; Identity and mastership; Service vs product/process/API; Offering and consumption; Provider/realization/dependency; SLA and observation boundary; Invariants; Scenarios; Minimal completion shape; Holds. Do not claim canonical completeness or installability.\n\nDOSSIER\n""" + dossier_path.read_text(encoding="utf-8")

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
    raise SystemExit(result.stderr)
(R / "claude-study.raw.md").write_text(
    result.stdout.rstrip() + "\n", encoding="utf-8"
)
print(dossier_path.stat().st_size, len(result.stdout))
