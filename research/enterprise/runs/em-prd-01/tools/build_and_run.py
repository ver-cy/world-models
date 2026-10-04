import csv, hashlib, json, subprocess
from pathlib import Path

import yaml

W = Path(r"R:\02_PROJECTS\02_Meta_Models_Platforms\Ver.cy\current\ver-cy\world-models")
R = W / "research/enterprise/runs/em-prd-01"
IDS = {"WM-ECO-021", "WM-ACT-008"}


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

dossier = {
    "contour": next(item for item in registry["units"] if item["id"] == "EM-PRD-01"),
    "queue": next(item for item in queue["units"] if item["id"] == "EM-PRD-01"),
    "reservations": [item for item in unified if item.get("model_id") in IDS],
    "relations": [
        item
        for item in relations
        if item.get("source_model_id") in IDS or item.get("target_model_id") in IDS
    ],
    "specs": {
        "WM-ECO-021": project_spec(W / "publications/wm-eco-021-offer-quote/spec.yaml"),
        "WM-ACT-008": project_spec(W / "publications/wm-act-008-plan-schedule/spec.yaml"),
    },
    "limits": [
        "Both bases are non-canonical reviewable drafts; complete specs were parsed and pinned. Registry relations and v1 fields remain non-normative."
    ],
}

R.mkdir(parents=True, exist_ok=True)
dossier_path = R / "provider-dossier.json"
dossier_path.write_text(
    json.dumps(dossier, ensure_ascii=False, indent=2) + "\n", encoding="utf-8"
)

prompt = """Independent enterprise metamodel review. Use only the dossier; no tools, browsing, or invented identifiers. Decide EM-PRD-01 Product, Offering and Roadmap over WM-ECO-021 Offer / Quote and WM-ACT-008 Plan / Schedule. Choose reuse, profile, complete-reserved, or identifier-unassigned candidate only where identity, lifecycle and mastership justify it. Separate durable Product and ProductFamily identity from market/time-scoped Offering; distinguish reusable PricePlan or price basis from proposal-specific quoted price; treat RoadmapItem as a planned intention, not proof of feature availability, contractual promise, release, task or completed delivery. Determine whether Product/ProductFamily and PricePlan need independent model candidates or can be bounded profiles/components. Test edition continuity, bundles, SaaS/device/internal products, tariff changes, free products, and roadmap confidence changes. Negative case: a tariff change creates a new software product. Acceptance: SaaS, device and internal product share base semantics without forcing subscription semantics on devices. Return <=1200 words with headings Verdict; Evidence; Identity and mastership; Product-family-edition rules; Offering and pricing; Roadmap boundary; Invariants; Scenarios; Minimal profile or candidate shape; Holds. Do not claim canonical completeness or installability.\n\nDOSSIER\n""" + dossier_path.read_text(encoding="utf-8")

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
