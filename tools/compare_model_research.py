#!/usr/bin/env python3
"""Create a deterministic provider overlap or waiver-aware omission report."""

from __future__ import annotations

import argparse
import json
import re
from collections import Counter
from datetime import datetime, timezone
from difflib import SequenceMatcher
from pathlib import Path
from typing import Any

from provider_policy import active_providers, load_provider_policy, waived_provider_names


ROOT = Path(__file__).resolve().parents[1]


def normalize(value: str) -> str:
    return " ".join(re.findall(r"[a-z0-9]+", value.casefold()))


def similarity(left: str, right: str) -> float:
    left_name, right_name = normalize(left), normalize(right)
    if left_name == right_name:
        return 1.0
    stop = {"and", "or", "the", "of", "a", "an", "to", "in", "for", "with"}
    left_tokens = set(left_name.split()) - stop
    right_tokens = set(right_name.split()) - stop
    overlap = left_tokens & right_tokens
    containment = len(overlap) / max(1, min(len(left_tokens), len(right_tokens)))
    jaccard = len(overlap) / max(1, len(left_tokens | right_tokens))
    sequence = SequenceMatcher(None, left_name, right_name).ratio()
    return max(sequence, containment * 0.9, jaccard)


def flatten(result: dict[str, Any], level: str) -> list[dict[str, str]]:
    rows = []
    for bundle in result["structure"]["bundles"]:
        if level == "bundle":
            rows.append({"id": bundle["id"], "name": bundle["name"], "path": bundle["id"]})
        for layer in bundle["layers"]:
            if level == "layer":
                rows.append({"id": layer["id"], "name": layer["name"], "path": f"{bundle['id']}/{layer['id']}"})
            for finding in layer["findings"]:
                if level == "finding":
                    rows.append({"id": finding["id"], "name": finding["name"], "path": f"{bundle['id']}/{layer['id']}/{finding['id']}"})
                if level == "question":
                    rows.extend({
                        "id": question["id"],
                        "name": question["text"],
                        "path": f"{bundle['id']}/{layer['id']}/{finding['id']}/{question['id']}",
                    } for question in finding["questions"])
    return rows


def match_nodes(left: list[dict[str, str]], right: list[dict[str, str]], threshold: float) -> dict[str, Any]:
    unused = set(range(len(right)))
    matches = []
    left_only = []
    for left_node in left:
        best_index = None
        best_score = 0.0
        for index in unused:
            score = similarity(left_node["name"], right[index]["name"])
            if score > best_score:
                best_index, best_score = index, score
        if best_index is not None and best_score >= threshold:
            unused.remove(best_index)
            matches.append({"claude": left_node, "grok": right[best_index], "similarity": round(best_score, 3)})
        else:
            left_only.append(left_node)
    return {"matches": matches, "claude_only": left_only, "grok_only": [right[index] for index in sorted(unused)]}


def counts(result: dict[str, Any]) -> dict[str, int]:
    bundles = flatten(result, "bundle")
    layers = flatten(result, "layer")
    findings = flatten(result, "finding")
    questions = flatten(result, "question")
    artifacts = sum(
        len(finding["artifacts"])
        for bundle in result["structure"]["bundles"]
        for layer in bundle["layers"]
        for finding in layer["findings"]
    )
    return {
        "sources": len(result["sources"]),
        "bundles": len(bundles),
        "layers": len(layers),
        "findings": len(findings),
        "questions": len(questions),
        "artifacts": artifacts,
        "functions": len(result["functions"]),
    }


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--model-id", required=True)
    parser.add_argument("--run-root", type=Path, default=ROOT / "research" / "runs")
    args = parser.parse_args()
    run_dir = args.run_root / args.model_id.casefold()
    policy = load_provider_policy()
    active = active_providers(policy)
    waived = waived_provider_names(policy)
    providers = {
        provider: json.loads((run_dir / f"{provider}.result.json").read_text(encoding="utf-8"))
        for provider in active
    }
    question_kinds = {}
    for provider, result in providers.items():
        question_kinds[provider] = dict(sorted(Counter(
            question["kind"]
            for bundle in result["structure"]["bundles"]
            for layer in bundle["layers"]
            for finding in layer["findings"]
            for question in finding["questions"]
        ).items()))

    report: dict[str, Any] = {
        "contract_version": "1.0.0",
        "model_id": args.model_id,
        "generated_at": datetime.now(timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ"),
        "mode": policy["mode"],
        "provider_policy": policy,
        "provider_counts": {provider: counts(result) for provider, result in providers.items()},
        "question_kinds": question_kinds,
    }
    if len(active) == 1:
        provider = active[0]
        result = providers[provider]
        urls = sorted(source["url"] for source in result["sources"])
        report.update({
            "entry_kind_agreement": {
                "status": "waived",
                "agrees": None,
                "claude": result["model"]["entry_kind"] if provider == "claude" else None,
                "grok": result["model"]["entry_kind"] if provider == "grok" else None,
            },
            "sources": {
                "common_urls": [],
                "claude_only": urls if provider == "claude" else [],
                "grok_only": urls if provider == "grok" else [],
            },
            "structure": {
                plural: {
                    "matches": [],
                    "claude_only": flatten(result, level) if provider == "claude" else [],
                    "grok_only": flatten(result, level) if provider == "grok" else [],
                }
                for plural, level in (
                    ("bundles", "bundle"),
                    ("layers", "layer"),
                    ("findings", "finding"),
                    ("questions", "question"),
                )
            },
            "synthesis_gate": {
                "status": "requires-single-provider-adjudication",
                "requirements": [
                    "Run a separate no-tools adversarial audit of the active provider result.",
                    "Verify the model boundary and entry kind against the frozen relationship contract.",
                    "Verify live URLs and version pins for all accepted sources.",
                    "Expose the owner-authorized provider waiver in every publication artifact.",
                    "Keep the result reviewable-draft while independent second-provider review is waived.",
                ],
            },
            "waived_providers": waived,
        })
    else:
        claude, grok = providers["claude"], providers["grok"]
        claude_urls = {source["url"]: source for source in claude["sources"]}
        grok_urls = {source["url"]: source for source in grok["sources"]}
        report.update({
            "entry_kind_agreement": {
                "agrees": claude["model"]["entry_kind"] == grok["model"]["entry_kind"],
                "claude": claude["model"]["entry_kind"],
                "grok": grok["model"]["entry_kind"],
            },
            "sources": {
                "common_urls": sorted(claude_urls.keys() & grok_urls.keys()),
                "claude_only": sorted(claude_urls.keys() - grok_urls.keys()),
                "grok_only": sorted(grok_urls.keys() - claude_urls.keys()),
            },
            "structure": {
                "bundles": match_nodes(flatten(claude, "bundle"), flatten(grok, "bundle"), 0.44),
                "layers": match_nodes(flatten(claude, "layer"), flatten(grok, "layer"), 0.48),
                "findings": match_nodes(flatten(claude, "finding"), flatten(grok, "finding"), 0.52),
                "questions": match_nodes(flatten(claude, "question"), flatten(grok, "question"), 0.68),
            },
            "synthesis_gate": {
            "status": "requires-adjudication",
            "requirements": [
                "Resolve every provider-only bundle, layer and finding against primary evidence.",
                "Resolve the model boundary and entry kind before accepting structure.",
                "Verify live URLs and version pins for all accepted sources.",
                "Record every rejected and deferred node with a reason.",
                "Do not publish while any critical conflict remains unresolved."
                ],
            },
        })
    output = run_dir / "comparison.json"
    output.write_text(json.dumps(report, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    print(output)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
