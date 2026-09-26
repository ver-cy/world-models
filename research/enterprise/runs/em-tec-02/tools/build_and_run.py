import csv, hashlib, json, subprocess
from pathlib import Path

import yaml

W = Path(r"R:\02_PROJECTS\02_Meta_Models_Platforms\Ver.cy\current\ver-cy\world-models")
R = W / "research/enterprise/runs/em-tec-02"
MODEL_ID = "WM-SFT-002"
ADJACENT = {"WM-SFT-001", "WM-SFT-009", "WM-SFT-010"}


def read_json(path):
    return json.loads(path.read_text(encoding="utf-8-sig"))


def read_rows(path):
    with path.open(encoding="utf-8-sig", newline="") as handle:
        return list(csv.DictReader(handle))


def project_spec(path):
    raw = path.read_bytes()
    spec = yaml.safe_load(raw.decode())
    findings = []
    for bundle in spec["structure"]["bundles"]:
        for layer in bundle["layers"]:
            for finding in layer["findings"]:
                findings.append(
                    {
                        "id": finding["id"],
                        "name": finding["name"],
                        "description": finding["description"],
                    }
                )
    return {
        "bytes": len(raw),
        "sha256": hashlib.sha256(raw).hexdigest(),
        "publication": spec["publication"],
        "model": spec["model"],
        "findings": findings,
        "composition": spec["composition"],
        "adjudication": spec["researchAdjudication"],
        "statistics": spec["statistics"],
    }


registry = read_json(W / "research/enterprise/registry.json")
queue = read_json(W / "research/enterprise/queue.json")
unified = read_rows(W / "planning/VERCY-UNIFIED-MEGA-REGISTRY.csv")
relations = read_rows(W / "planning/VERCY-MODEL-RELATIONS.csv")
legacy_path = W / "models/knowledge-information/N4-software-product-and-system.md"
legacy_raw = legacy_path.read_bytes()

dossier = {
    "contour": next(item for item in registry["units"] if item["id"] == "EM-TEC-02"),
    "queue": next(item for item in queue["units"] if item["id"] == "EM-TEC-02"),
    "reservation": next(item for item in unified if item.get("model_id") == MODEL_ID),
    "adjacent_reservations": [
        item for item in unified if item.get("model_id") in ADJACENT
    ],
    "relations": [
        item
        for item in relations
        if item.get("source_model_id") in ({MODEL_ID} | ADJACENT)
        or item.get("target_model_id") in ({MODEL_ID} | ADJACENT)
    ],
    "specs": {
        "WM-SFT-002": {
            "format": "legacy-markdown",
            "path": "models/knowledge-information/N4-software-product-and-system.md",
            "bytes": len(legacy_raw),
            "sha256": hashlib.sha256(legacy_raw).hexdigest(),
            "content": legacy_raw.decode("utf-8-sig"),
        },
        "WM-SFT-001_adjacent": project_spec(
            W / "publications/wm-sft-001-software-product/spec.yaml"
        ),
        "WM-SFT-009_adjacent": project_spec(
            W / "publications/wm-sft-009-deployment/spec.yaml"
        ),
    },
    "limits": [
        "WM-SFT-002 has only the shared legacy N4 specification and is under migration boundary review.",
        "WM-SFT-010 has no current specification in the dossier; adjacent published drafts are non-canonical.",
    ],
}

R.mkdir(parents=True, exist_ok=True)
dossier_path = R / "provider-dossier.json"
dossier_path.write_text(
    json.dumps(dossier, ensure_ascii=False, indent=2) + "\n", encoding="utf-8"
)

prompt = """Independent enterprise metamodel review. Use only the dossier; no tools, browsing, or invented identifiers. Decide EM-TEC-02 Business Application and Software System against reserved WM-SFT-002 Deployed System, with adjacent WM-SFT-001 Software Product, WM-SFT-009 Deployment and WM-SFT-010 Runtime Environment. Determine whether to complete/rename WM-SFT-002 and how BusinessApplication, SoftwareSystem, ApplicationModule and ApplicationUsage fit without conflating vendor product, purchased licence, logical system, runtime installation or deployment occurrence. Define an evidence-based boundary for a system made of multiple products, and when a module becomes an independently managed application. Test one ERP product, two installations and three business applications without merging identities. Return <=1200 words with headings Verdict; Evidence; Identity/mastership; Product/licence/system/runtime/deployment; Business application and usage; Module/system boundary; Integrated system boundary; Invariants; Scenario; Minimal completion shape; Holds. Do not claim canonical completeness or installability.\n\nDOSSIER\n""" + dossier_path.read_text(encoding="utf-8")

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
