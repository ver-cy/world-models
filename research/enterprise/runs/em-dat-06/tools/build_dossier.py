from __future__ import annotations

import csv
import json
from pathlib import Path

REPO = Path(r"R:\02_PROJECTS\02_Meta_Models_Platforms\Ver.cy\current\ver-cy\world-models")
RUN = REPO / "research" / "enterprise" / "runs" / "em-dat-06"
RUN.mkdir(parents=True, exist_ok=True)

MODELS = {
    "WM-REC-001": "wm-rec-001-document-record",
    "WM-ACT-044": "wm-act-044-content-publication",
    "WM-ACT-053": "wm-act-053-data-processing-job-pipeline-run",
    "WM-XCT-003": "wm-xct-003-projection-disclosure-policy",
    "WM-MED-003": "wm-med-003-publication-edition",
}

SELECTED = {
    "WM-REC-001": {"record-identity-anchor", "content-structure-and-components", "version-chain-and-immutability", "instantiation-copy-and-original-status", "fixity-and-preservation-actions", "issuance-mandate-and-registration", "derivation-and-provenance-graph", "access-conditions-and-security-marking"},
    "WM-ACT-044": {"publication-operation-type-scope-target-and-neighbor-boundary", "content-edition-revision-rendition-and-translation-reference", "release-metadata-identifier-title-subject-language-audience-and-provenance-snapshot", "release-instruction-scheduled-effective-window-embargo-and-authority", "package-format-media-type-digest-rendition-manifest-and-accessibility", "delivery-attempt-response-acknowledgement-uri-and-availability-verification", "change-class-reason-authority-affected-version-distribution-and-effective-time", "correction-retraction-withdrawal-takedown-notice-replacement-and-propagation-check"},
    "WM-ACT-053": {"processing-run-root-identity-namespace-owner-status-and-lineage-head", "pipeline-job-workflow-definition-revision-code-location-and-parent-reference", "declared-input-dataset-version-partition-schema-contract-and-availability", "resolved-parameter-configuration-secret-reference-consumed-value-and-redaction", "runtime-platform-environment-region-clock-locale-effective-data-interval-and-watermark", "declared-output-dataset-artifact-schema-partition-destination-and-contract", "materialized-output-version-digest-size-row-count-publication-visibility-and-derivation", "backfill-replay-rerun-recovery-predecessor-successor-trigger-and-data-interval", "amend-correct-invalidate-supersede-current-head-reason-authority-and-lineage"},
    "WM-XCT-003": {"population-and-record-scope", "aggregation-grain-declaration", "compiled-template-and-fingerprint", "source-schema-binding-and-drift", "binding-target-and-audience", "assurance-method-and-evidence", "served-output-reproducibility", "shape-invalidation-signals"},
    "WM-MED-003": {"publication-edition-identifier-namespace-revision-owner-and-master", "work-expression-edition-manifestation-item-copy-file-and-url-boundary", "publication-release-online-availability-copyright-deposit-and-record-clocks", "edition-version-release-revision-erratum-corrigendum-successor-and-change-summary", "retraction-withdrawal-removal-takedown-silent-replacement-tombstone-and-notice"},
}


def load(slug: str) -> dict:
    text = (REPO / "publications" / slug / "spec.yaml").read_text(encoding="utf-8")
    return json.loads(text[text.index("{"):])


def compact(model_id: str, slug: str) -> dict:
    data = load(slug)
    findings = []
    for bundle in data.get("structure", {}).get("bundles", []):
        for layer in bundle.get("layers", []):
            for finding in layer.get("findings", []):
                if finding.get("id") in SELECTED[model_id]:
                    findings.append({
                        "id": finding.get("id"), "name": finding.get("name"), "description": finding.get("description"),
                        "dataElements": [
                            {key: element.get(key) for key in ("id", "name", "description", "value_kind", "cardinality", "required") if element.get(key) is not None}
                            for element in finding.get("data_elements", [])
                        ],
                    })
    adjudication = data.get("researchAdjudication") or {}
    return {
        "publication": data.get("publication"), "metaModel": data.get("metaModel"), "model": data.get("model"),
        "selectedFindings": findings,
        "functions": [{key: fn.get(key) for key in ("id", "name", "description")} for fn in data.get("functions", [])],
        "publicationHolds": adjudication.get("publicationHolds") or [],
    }


with (REPO / "planning" / "VERCY-UNIFIED-MEGA-REGISTRY.csv").open(encoding="utf-8-sig", newline="") as handle:
    planned = next(row for row in csv.DictReader(handle) if row.get("model_id") == "WM-REC-002")

dossier = {
    "contour": {
        "id": "EM-DAT-06", "name": "Report definition and release instance",
        "scope": "A reusable report specification, parameter contract, reproducible execution binding, issued report statement and governed publication/artifact references. A dashboard is a governed projection or a separately identified live view, not an arbitrary data join.",
        "questions": ["What makes a report issue reproducible?", "How is a corrected issue represented without overwriting the original?", "Which disclosure rules remain applicable to aggregates?"],
        "invariants": ["A report issue pins definition version, parameters, input snapshots, cutoff/as-of and execution evidence.", "Correction creates a successor issue and retains the published predecessor.", "Aggregation never bypasses disclosure policy.", "Report semantics, processing run, record artifact and publication operation have distinct identities."],
        "acceptanceScenario": "Issue a report, correct an input fact and issue a successor; both remain explainable and a sensitive slice is suppressed by a pinned disclosure policy.",
        "negativeCase": "One projection joins arbitrary HR and finance objects and publishes aggregates without purpose or disclosure evaluation.",
        "decision": "Decide whether EM-DAT-06 should complete the reserved WM-REC-002 Report / Statement, use a profile, or be a composition-only adoption model. Do not duplicate record, run, publication, edition or disclosure-policy lifecycles.",
    },
    "plannedRegistryEntry": planned,
    "models": {model_id: compact(model_id, slug) for model_id, slug in MODELS.items()},
}
out = RUN / "provider-dossier.json"
out.write_text(json.dumps(dossier, ensure_ascii=False, indent=2) + "\n", encoding="utf-8", newline="\n")
print(json.dumps({"output": str(out), "bytes": out.stat().st_size}))
