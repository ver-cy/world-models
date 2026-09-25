import json
from pathlib import Path

import yaml


REPO = Path(r"R:\02_PROJECTS\02_Meta_Models_Platforms\Ver.cy\current\ver-cy\world-models")
OUT = REPO / "research/enterprise/runs/em-fin-03/provider-dossier.json"

MODELS = {
    "invoice": {
        "path": REPO / "publications/wm-eco-008-invoice-commercial-document/spec.yaml",
        "findings": {
            "fnd-invoice-identity",
            "fnd-currency-and-conversion",
            "fnd-totals-rounding-and-arithmetic-consistency",
            "fnd-payment-means-terms-and-due-date",
            "fnd-order-contract-and-fulfilment-references",
            "fnd-preceding-document-and-correction-chain",
            "fnd-lifecycle-states-and-transitions",
            "fnd-buyer-response-and-dispute",
        },
    },
    "payment": {
        "path": REPO / "publications/wm-eco-009-payment/spec.yaml",
        "findings": {
            "instructed-and-settlement-amount",
            "currency-conversion-and-exchange-rate",
            "settlement-finality-and-obligation-discharge",
            "returns-reversals-and-recalls",
            "obligation-discharge-and-allocation",
            "remittance-information-and-purpose",
            "reconciliation-and-accounting-handoff",
        },
    },
}


def selected_findings(spec, ids):
    found = []
    for bundle in spec["structure"]["bundles"]:
        for layer in bundle["layers"]:
            for finding in layer["findings"]:
                if finding["id"] in ids:
                    found.append(
                        {
                            "bundle": {k: bundle.get(k) for k in ("id", "name", "description")},
                            "layer": {k: layer.get(k) for k in ("id", "name", "description")},
                            "finding": finding,
                        }
                    )
    return found


def main():
    dossier = {
        "contour": {
            "id": "EM-FIN-03",
            "name": "Invoice, payment and reconciliation",
            "scope": "Invoice/commercial document, lines, due dates, payments and allocations; local profiles for invoice, bill and tax invoice.",
            "questions": [
                "How are partial and consolidated payments represented without merging invoice and payment identities?",
                "How are foreign-exchange differences, rounding and residuals made explicit?",
                "How is invoice cancellation distinguished from a credit/correction document?",
                "Does reconciliation need an independent aggregate identity and lifecycle?",
            ],
            "invariants": [
                "Payment and commercial-document identifiers remain distinct.",
                "Allocation cannot exceed the admissible amount without an explicit exception or residual treatment.",
                "Reconciliation does not prove order fulfilment or delivery.",
            ],
            "negative_case": "One payment is incorrectly treated as fully closing two invoices.",
            "acceptance_case": "A cross-currency payment is allocated to two documents while one disputed remainder stays explicit.",
        },
        "registry_policy": {
            "rule": "Do not create a runtime/model identifier unless independent identity and lifecycle are proved and a registry allocation exists.",
            "candidate_ids": ["WM-ECO-008", "WM-ECO-009"],
        },
        "models": {},
    }
    for label, config in MODELS.items():
        spec = yaml.safe_load(config["path"].read_text(encoding="utf-8"))
        dossier["models"][label] = {
            "publication": spec.get("publication"),
            "model": spec["model"],
            "selected_findings": selected_findings(spec, config["findings"]),
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
