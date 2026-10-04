import csv, hashlib, json, subprocess
from pathlib import Path

import yaml

W = Path(r"R:\02_PROJECTS\02_Meta_Models_Platforms\Ver.cy\current\ver-cy\world-models")
R = W / "research/enterprise/runs/em-tec-03"
IDS = {"WM-SFT-003", "WM-SFT-018", "WM-DAT-004", "WM-REC-003", "WM-ACT-015"}


def read_json(path):
    return json.loads(path.read_text(encoding="utf-8-sig"))


def read_rows(path):
    with path.open(encoding="utf-8-sig", newline="") as handle:
        return list(csv.DictReader(handle))


def full_spec(path):
    raw = path.read_bytes()
    return {
        "bytes": len(raw),
        "sha256": hashlib.sha256(raw).hexdigest(),
        "document": yaml.safe_load(raw.decode("utf-8-sig")),
    }


registry = read_json(W / "research/enterprise/registry.json")
queue = read_json(W / "research/enterprise/queue.json")
unified = read_rows(W / "planning/VERCY-UNIFIED-MEGA-REGISTRY.csv")
relations = read_rows(W / "planning/VERCY-MODEL-RELATIONS.csv")

dossier = {
    "contour": next(item for item in registry["units"] if item["id"] == "EM-TEC-03"),
    "queue": next(item for item in queue["units"] if item["id"] == "EM-TEC-03"),
    "reservations": [item for item in unified if item.get("model_id") in IDS],
    "relations": [
        item for item in relations
        if item.get("source_model_id") in IDS or item.get("target_model_id") in IDS
    ],
    "specs": {
        "WM-DAT-004": full_spec(W / "publications/wm-dat-004-data-schema-data-contract/spec.yaml"),
        "WM-REC-003": full_spec(W / "publications/wm-rec-003-message/spec.yaml"),
        "WM-ACT-015": full_spec(W / "publications/wm-act-015-occurrence-event/spec.yaml"),
    },
    "missing_specs": {
        "WM-SFT-003": "Reserved API / Interface candidate has no current specification file.",
        "WM-SFT-018": "Reserved Network / Endpoint candidate has no current specification file.",
    },
    "prior_adjudication": {
        "EM-TEC-01": "Complete WM-SFT-003 as the independent API / Interface contract after its missing specification is written.",
        "EM-TEC-02": "Keep logical system/application, product, runtime and deployment identities separate.",
    },
}

R.mkdir(parents=True, exist_ok=True)
dossier_path = R / "provider-dossier.json"
dossier_path.write_text(json.dumps(dossier, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")

prompt = """Independent enterprise metamodel review. Use only the frozen dossier; no tools, browsing or invented identifiers. Decide EM-TEC-03 Interface, API and Integration. Test whether reserved WM-SFT-003 should be completed as the versioned logical interface contract, whether Integration and EndpointBinding belong inside it or need separate identity/lifecycle, and how ExchangeEvent relates without duplicating WM-ACT-015 Occurrence/Event or WM-REC-003 Message. Keep WM-DAT-004 Data Schema/Data Contract as payload semantics/constraints and WM-SFT-018 Network/Endpoint as logical connectivity/address/exposure. Distinguish logical contract, contract revision/API version, consumer pin, integration relationship, endpoint binding, message/exchange occurrence, data schema and transport. Define compatibility and migration rules. Test two cases: an endpoint URL changes without contract change; an incompatible payload change occurs without URL change. Return <=1200 words with headings Verdict; Evidence; Identity/mastership; Contract/version/consumer pin; Integration; Endpoint binding; Message/event/exchange; Compatibility and migration; Invariants; Scenarios; Minimal completion shape; Holds. Do not claim canonical completeness or installability.\n\nDOSSIER\n""" + dossier_path.read_text(encoding="utf-8")

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
(R / "claude-study.raw.md").write_text(result.stdout.rstrip() + "\n", encoding="utf-8")
print(dossier_path.stat().st_size, len(result.stdout))
