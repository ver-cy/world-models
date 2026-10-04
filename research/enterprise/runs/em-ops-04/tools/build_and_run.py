import csv, hashlib, json, subprocess
from pathlib import Path
import yaml

W = Path(r"R:\02_PROJECTS\02_Meta_Models_Platforms\Ver.cy\current\ver-cy\world-models")
R = W / "research/enterprise/runs/em-ops-04"
IDS = {'WM-OBJ-001', 'WM-OBJ-002', 'WM-OBJ-017', 'WM-OBJ-018', 'WM-OBJ-019', 'WM-SFT-007', 'WM-SFT-008', 'WM-SFT-012', 'WM-ACT-007', 'WM-FLW-013'}

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
    "WM-OBJ-001": "publications/wm-obj-001-physical-item-instance/spec.yaml",
    "WM-OBJ-002": "publications/wm-obj-002-product-type-catalog-item/spec.yaml",
    "WM-OBJ-017": "publications/wm-obj-017-product-configuration-variant/spec.yaml",
    "WM-OBJ-018": "publications/wm-obj-018-engineering-design-product-definition/spec.yaml",
    "WM-OBJ-019": "publications/wm-obj-019-component-type-engineering-bom/spec.yaml",
    "WM-SFT-007": "publications/wm-sft-007-software-component-package/spec.yaml",
    "WM-SFT-008": "publications/wm-sft-008-build-release/spec.yaml",
    "WM-SFT-012": "publications/wm-sft-012-sbom-supply-chain-manifest/spec.yaml",
    "WM-ACT-007": "publications/wm-act-007-work-order/spec.yaml",
    "WM-FLW-013": "publications/wm-flw-013-supply-chain-trace-chain-of-custody/spec.yaml",
}
dossier = {
    "contour": next(x for x in registry["units"] if x["id"] == "EM-OPS-04"),
    "queue": next(x for x in queue["units"] if x["id"] == "EM-OPS-04"),
    "reservations": [x for x in unified if x.get("model_id") in IDS],
    "relations": [x for x in relations if x.get("source_model_id") in IDS or x.get("target_model_id") in IDS],
    "specs": {key: compact(W / value) for key, value in specs.items()},
    "prior_research": {
        "EM-LND-11": text_document(W / "research/enterprise/runs/em-lnd-11/local-evidence.md"),
        "EM-TEC-01": text_document(W / "research/enterprise/runs/em-tec-01/local-evidence.md"),
        "EM-TEC-04": text_document(W / "research/enterprise/runs/em-tec-04/local-evidence.md"),
        "EM-PRD-01": text_document(W / "research/enterprise/runs/em-prd-01/local-evidence.md"),
        "EM-PRD-02": text_document(W / "research/enterprise/runs/em-prd-02/local-evidence.md"),
        "EM-OPS-03": text_document(W / "research/enterprise/runs/em-ops-03/local-evidence.md"),
    },
}
R.mkdir(parents=True, exist_ok=True)
dossier_path = R / "provider-dossier.json"
dossier_path.write_text(json.dumps(dossier, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
prompt = """Independent enterprise metamodel review. Use only the frozen dossier; no tools, browsing or invented identifiers. Adjudicate EM-OPS-04 Item, Design and Bill of Materials using complete Physical Item, Product Type/Catalog Item, Product Configuration Variant, Engineering Design/Product Definition, Component Type/Engineering BOM, Software Component/Package, Build/Release, SBOM, Work Order and Supply Trace drafts plus prior boundary work. Candidate types are ItemDefinition, SKU, EngineeringRevision, BillOfMaterials, BOMLine and SubstitutionRule. Decide reuse/profile/new by independent identity and lifecycle without allocating identifiers. Separate commercial catalog item/SKU, product type, variant, engineering definition, engineering revision, EBOM, manufacturing BOM/routing, BOM occurrence/line, substitution rule, firmware/software release, SBOM, serialized physical item, lot/batch, as-built assembly and actual transformation evidence. Determine which candidates map to existing roots or contained identities; identify missing MBOM/manufacturing-plan and as-built masters. BOM must state kind and immutable version; quantities carry units and basis; substitutions carry applicability/effectivity and authority. A shared Product record cannot stand for drawing, SKU and serial number. Test two engineering revisions, an alternate component, a firmware release and a manufactured instance; preserve revision effectivity by lot and prove as-built composition only from actual events/evidence, never BOM intent. Return <=1200 words with headings Verdict; Evidence; Identity/mastership; Product/SKU/variant; Engineering definition/revision; EBOM/MBOM; Lines/substitutions/effectivity; Firmware/software; Instance/lot/as-built; Time/quantity/provenance; Governance; Acceptance scenario; Invariants; Minimal model set; Holds. Explicitly decide all candidates and identify missing roots or relation contradictions. Do not claim canonical completeness, installability or publication readiness.

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
