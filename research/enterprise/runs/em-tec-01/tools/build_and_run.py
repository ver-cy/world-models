import csv, hashlib, json, subprocess
from pathlib import Path

import yaml

W = Path(r"R:\02_PROJECTS\02_Meta_Models_Platforms\Ver.cy\current\ver-cy\world-models")
A = Path(r"R:\02_PROJECTS\02_Meta_Models_Platforms\Ver.cy\current\software-meta-model")
R = W / "research/enterprise/runs/em-tec-01"
IDS = {"WM-SFT-001", "WM-SFT-007", "WM-SFT-003", "WM-SFT-008", "WM-SFT-009"}


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


def file_projection(path):
    raw = path.read_bytes()
    return {
        "path": path.relative_to(A).as_posix(),
        "bytes": len(raw),
        "sha256": hashlib.sha256(raw).hexdigest(),
        "content": raw.decode("utf-8-sig"),
    }


registry = read_json(W / "research/enterprise/registry.json")
queue = read_json(W / "research/enterprise/queue.json")
unified = read_rows(W / "planning/VERCY-UNIFIED-MEGA-REGISTRY.csv")
relations = read_rows(W / "planning/VERCY-MODEL-RELATIONS.csv")
legacy_path = W / "models/knowledge-information/N4-software-product-and-system.md"
legacy_raw = legacy_path.read_bytes()

aismm_files = sorted(
    path
    for path in A.rglob("*")
    if path.is_file() and ".git" not in path.parts
)
aismm_manifest = []
tree_hash = hashlib.sha256()
for path in aismm_files:
    raw = path.read_bytes()
    rel = path.relative_to(A).as_posix()
    digest = hashlib.sha256(raw).hexdigest()
    tree_hash.update(f"{rel}\0{len(raw)}\0{digest}\n".encode())
    aismm_manifest.append({"path": rel, "bytes": len(raw), "sha256": digest})

key_aismm_paths = [
    "README.md",
    "RELEASE_NOTES_v3.1.0.md",
    "aismm-versioning-and-conformance.md",
    "aismm-meta-universe-alignment.md",
    "b0-product-core/001-product-definition-context.md",
    "b2-system-design/201-applications-and-system-architecture.md",
    "b2-system-design/203-api-and-interfaces.md",
    "b3-implementation/302-code-and-implementation.md",
    "b3-implementation/303-build-deployment-and-runtime-artifacts.md",
    "b3-implementation/304-dependency-inventory-sbom-and-reproducibility.md",
    "b8-change-execution/804-release-version-and-rollout-management.md",
]

dossier = {
    "contour": next(item for item in registry["units"] if item["id"] == "EM-TEC-01"),
    "queue": next(item for item in queue["units"] if item["id"] == "EM-TEC-01"),
    "reservations": [item for item in unified if item.get("model_id") in IDS],
    "relations": [
        item
        for item in relations
        if item.get("source_model_id") in IDS or item.get("target_model_id") in IDS
    ],
    "specs": {
        "WM-SFT-001": project_spec(
            W / "publications/wm-sft-001-software-product/spec.yaml"
        ),
        "WM-SFT-007": project_spec(
            W / "publications/wm-sft-007-software-component-package/spec.yaml"
        ),
        "WM-SFT-003": {
            "available": False,
            "reason": "Reserved candidate has no current specification file.",
        },
        "WM-SFT-008": project_spec(
            W / "publications/wm-sft-008-build-release/spec.yaml"
        ),
        "WM-SFT-009": project_spec(
            W / "publications/wm-sft-009-deployment/spec.yaml"
        ),
        "legacy_N4": {
            "path": "models/knowledge-information/N4-software-product-and-system.md",
            "bytes": len(legacy_raw),
            "sha256": hashlib.sha256(legacy_raw).hexdigest(),
            "content": legacy_raw.decode("utf-8-sig"),
        },
        "AISMM": {
            "repository": str(A),
            "git_head": subprocess.check_output(
                ["git", "-C", str(A), "rev-parse", "HEAD"], text=True
            ).strip(),
            "tree_manifest_sha256": tree_hash.hexdigest(),
            "file_count": len(aismm_manifest),
            "file_manifest": aismm_manifest,
            "key_documents": [file_projection(A / path) for path in key_aismm_paths],
        },
    },
    "limits": [
        "AISMM in the available repository declares version 3.1.0; no 3.2.0 text was found, so a 3.2-vs-runtime comparison cannot be asserted.",
        "WM-SFT-003 has no current full spec. Published WM-SFT drafts remain non-canonical and their holds remain active.",
    ],
}

R.mkdir(parents=True, exist_ok=True)
dossier_path = R / "provider-dossier.json"
dossier_path.write_text(
    json.dumps(dossier, ensure_ascii=False, indent=2) + "\n", encoding="utf-8"
)

prompt = """Independent enterprise metamodel review. Use only the dossier; no tools, browsing, or invented identifiers. Decide EM-TEC-01 Software Product and AISMM engineering context across WM-SFT-001, AISMM, WM-SFT-007, WM-SFT-003, WM-SFT-008 and WM-SFT-009. AISMM is a product knowledge/context specification, not a second SoftwareProduct master. Assign one fact owner for product identity, architecture/context, component/package, repository, build, release, artifact/SBOM and deployment. Distinguish build, release, artifact and deployment; artifact digest is not a semantic fingerprint. Reconcile the contour's claimed AISMM 3.2.0 with the dossier's available 3.1.0 only. Test SaaS, library, on-prem, container and firmware delivery, one product with several repositories, and no copying of HR/incident/dataset facts into AISMM. Return <=1400 words with headings Verdict; Evidence; WM-SFT-001/AISMM relationship; Identity/mastership; Component/repository; Build/release/artifact/SBOM; Deployment boundary; Five delivery profiles; AISMM version finding; Invariants; Minimal composition; Holds. Do not claim canonical completeness or installability.\n\nDOSSIER\n""" + dossier_path.read_text(encoding="utf-8")

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
