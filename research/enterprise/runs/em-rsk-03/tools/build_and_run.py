import csv, hashlib, json, subprocess
from pathlib import Path

import yaml

W = Path(r"R:\02_PROJECTS\02_Meta_Models_Platforms\Ver.cy\current\ver-cy\world-models")
R = W / "research/enterprise/runs/em-rsk-03"
IDS = {"WM-PER-002", "WM-XCT-002"}
ADJACENT = {"WM-VRT-005", "WM-XCT-001", "WM-ACT-034", "WM-XCT-004", "WM-XCT-007"}


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
                        "data_elements": [
                            {
                                key: element.get(key)
                                for key in (
                                    "id",
                                    "name",
                                    "description",
                                    "value_kind",
                                    "cardinality",
                                    "required",
                                )
                            }
                            for element in finding.get("data_elements", [])
                        ],
                    }
                )
    return {
        "bytes": len(raw),
        "sha256": hashlib.sha256(raw).hexdigest(),
        "publication": spec["publication"],
        "model": spec["model"],
        "findings": findings,
        "functions": [
            {key: function.get(key) for key in ("id", "name", "description")}
            for function in spec["functions"]
        ],
        "composition": spec["composition"],
        "adjudication": spec["researchAdjudication"],
        "statistics": spec["statistics"],
    }


registry = read_json(W / "research/enterprise/registry.json")
queue = read_json(W / "research/enterprise/queue.json")
unified = read_rows(W / "planning/VERCY-UNIFIED-MEGA-REGISTRY.csv")
relations = read_rows(W / "planning/VERCY-MODEL-RELATIONS.csv")
legacy_path = W / "models/registries-ledgers/R4-identity-register.md"
legacy_raw = legacy_path.read_bytes()

dossier = {
    "contour": next(item for item in registry["units"] if item["id"] == "EM-RSK-03"),
    "queue": next(item for item in queue["units"] if item["id"] == "EM-RSK-03"),
    "reservations": [item for item in unified if item.get("model_id") in IDS],
    "adjacent_reservations": [
        item for item in unified if item.get("model_id") in ADJACENT
    ],
    "relations": [
        item
        for item in relations
        if item.get("source_model_id") in IDS or item.get("target_model_id") in IDS
    ],
    "specs": {
        "WM-PER-002": {
            "format": "legacy-markdown",
            "path": "models/registries-ledgers/R4-identity-register.md",
            "bytes": len(legacy_raw),
            "sha256": hashlib.sha256(legacy_raw).hexdigest(),
            "content": legacy_raw.decode("utf-8-sig"),
        },
        "WM-XCT-002": project_spec(
            W / "publications/wm-xct-002-access-contract-consent/spec.yaml"
        ),
    },
    "limits": [
        "WM-PER-002 has only a legacy identity-register specification and is under migration boundary review; WM-VRT-005 Online Account is an adjacent unspecced reservation.",
        "WM-XCT-002 is a non-canonical reviewable draft limited to read/disclosure permission and consent.",
    ],
}

R.mkdir(parents=True, exist_ok=True)
dossier_path = R / "provider-dossier.json"
dossier_path.write_text(
    json.dumps(dossier, ensure_ascii=False, indent=2) + "\n", encoding="utf-8"
)

prompt = """Independent enterprise metamodel review. Use only the dossier; no tools, browsing, or invented identifiers. Decide EM-RSK-03 Access, Delegation and Secret Metadata over WM-PER-002 Digital Identity / Account and WM-XCT-002 Access Contract / Consent, considering adjacent reservations included in the dossier. Choose reuse/profile/complete-reserved/duplicate-retirement or identifier-unassigned candidate only where identity, lifecycle and mastership justify it. Separate subject identity, online account, authentication credential metadata, IAM access role, permission grant, consent/disclosure grant, delegation, access review, policy decision/enforcement and audit. Account and Person must not be equated. IAM role is not an organizational position. Delegation must attenuate rights and validity. Secret values must never enter the registry or projections; prove rotation/revocation via metadata and evidence references. Test assignment change revoking conditioned grants while retaining separately justified grants. Return <=1200 words with headings Verdict; Evidence; Identity/account boundary; Role/grant/delegation; Consent vs authorization; Access review/revocation; Credential metadata; Invariants; Scenario; Minimal profile/candidate shape; Holds. Do not claim canonical completeness or installability.\n\nDOSSIER\n""" + dossier_path.read_text(encoding="utf-8")

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
