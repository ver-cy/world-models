import json
from pathlib import Path

import yaml


REPO = Path(r"R:\02_PROJECTS\02_Meta_Models_Platforms\Ver.cy\current\ver-cy\world-models")
OUT = REPO / "research/enterprise/runs/em-knw-01/provider-dossier.json"
MODELS = {
    "document": (
        "wm-rec-001-document-record",
        {
            "record-identity-anchor", "content-structure-and-components",
            "version-chain-and-immutability", "instantiation-copy-and-original-status",
            "supersession-between-records", "derivation-and-provenance-graph",
            "record-status-and-transitions", "document-versus-record",
            "metadata-alignment-and-conformance", "exchange-packaging-and-projections",
        },
    ),
    "concept": (
        "wm-knw-006-concept-term",
        {
            "ct-core-concept-identity", "ct-core-concept-delimitation",
            "ct-core-designation-inventory", "ct-core-designation-identity",
            "ct-core-language-script", "ct-core-definition", "ct-core-subject-field",
            "ct-rel-find-scheme-membership", "ct-rel-find-mapping-relation",
            "ct-gov-finding-deprecation-retirement-succession",
            "ct-gov-finding-version-release-binding", "ct-gov-finding-duplicate-merge-split",
            "ct-gov-finding-authoritative-source-provenance",
        },
    ),
    "scheme": (
        "wm-knw-018-taxonomy-classification-scheme",
        {
            "scheme-identifier-canonical-uri-namespace-prefix-and-local-id-policy",
            "version-edition-release-status-date-predecessor-successor-and-distribution",
            "taxonomy-thesaurus-classification-list-synonym-ring-ontology-and-hybrid-profile",
            "concept-uri-local-identifier-in-scheme-top-concept-and-concept-type",
            "preferred-alternative-hidden-label-language-script-direction-and-uniqueness",
            "definition-scope-note-example-history-change-editorial-note-notation-and-code",
            "exact-close-broad-narrow-related-equivalent-subclass-and-same-as-distinction",
            "source-concept-target-concept-scheme-version-direction-symmetry-and-transitivity",
            "candidate-accepted-rejected-contested-superseded-conflict-and-resolution",
            "draft-proposed-reviewed-approved-published-deprecated-superseded-and-retired-state",
            "change-set-add-update-move-split-merge-replace-delete-rationale-and-impact",
            "profile-version-context-shape-conformance-round-trip-migration-and-semantic-loss",
        },
    ),
}


def select(spec, ids):
    result = []
    for bundle in spec["structure"]["bundles"]:
        for layer in bundle["layers"]:
            for finding in layer["findings"]:
                if finding["id"] in ids:
                    result.append({
                        "bundle": {k: bundle.get(k) for k in ("id", "name", "description")},
                        "layer": {k: layer.get(k) for k in ("id", "name", "description")},
                        "finding": finding,
                    })
    missing = ids - {x["finding"]["id"] for x in result}
    if missing:
        raise ValueError(f"Missing findings: {sorted(missing)}")
    return result


def main():
    registry = json.loads((REPO / "research/enterprise/registry.json").read_text(encoding="utf-8"))
    unit = next(x for x in registry["units"] if x["id"] == "EM-KNW-01")
    dossier = {
        "contour": unit,
        "registry_policy": {
            "rule": "Reuse existing identities. Do not create a runtime/model identifier without independent identity/lifecycle and a registry allocation.",
            "reserved_candidates": ["WM-REC-001", "WM-KNW-006", "WM-KNW-018"],
        },
        "models": {},
    }
    for label, (folder, ids) in MODELS.items():
        spec = yaml.safe_load((REPO / "publications" / folder / "spec.yaml").read_text(encoding="utf-8"))
        dossier["models"][label] = {
            "publication": spec.get("publication"),
            "model": spec["model"],
            "selected_findings": select(spec, ids),
            "functions": spec.get("functions"),
            "composition": spec.get("composition"),
            "researchAdjudication": spec.get("researchAdjudication"),
        }
    OUT.parent.mkdir(parents=True, exist_ok=True)
    OUT.write_text(json.dumps(dossier, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    print(OUT)
    print(OUT.stat().st_size)


if __name__ == "__main__":
    main()
