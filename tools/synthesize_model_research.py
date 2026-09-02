#!/usr/bin/env python3
"""Build a reviewable synthesis from an explicit per-model adjudication plan."""

from __future__ import annotations

import argparse
import copy
import hashlib
import json
from datetime import datetime, timezone
from pathlib import Path
from typing import Any

from provider_policy import active_providers, load_provider_policy, waived_provider_names
from run_model_research import ROOT, write_json
from validate_model_research import validate


def unique(values: list[Any]) -> list[Any]:
    seen = set()
    result = []
    for value in values:
        key = json.dumps(value, sort_keys=True, ensure_ascii=False)
        if key not in seen:
            seen.add(key)
            result.append(value)
    return result


def remap_refs(value: Any, mapping: dict[str, str]) -> Any:
    if isinstance(value, dict):
        return {
            key: ([mapping.get(item, item) for item in child] if key == "source_refs" else remap_refs(child, mapping))
            for key, child in value.items()
        }
    if isinstance(value, list):
        return [remap_refs(item, mapping) for item in value]
    return value


def find_finding(result: dict[str, Any], finding_id: str) -> dict[str, Any]:
    for bundle in result["structure"]["bundles"]:
        for layer in bundle["layers"]:
            for finding in layer["findings"]:
                if finding["id"] == finding_id:
                    return finding
    raise KeyError(f"finding not found: {finding_id}")


def find_layer(result: dict[str, Any], layer_id: str) -> dict[str, Any]:
    for bundle in result["structure"]["bundles"]:
        for layer in bundle["layers"]:
            if layer["id"] == layer_id:
                return layer
    raise KeyError(f"layer not found: {layer_id}")


def rekey_finding(finding: dict[str, Any], target_id: str) -> dict[str, Any]:
    finding = copy.deepcopy(finding)
    finding["id"] = target_id
    for index, question in enumerate(finding["questions"], 1):
        question["id"] = f"{target_id}-q{index:02d}"
    for index, element in enumerate(finding["data_elements"], 1):
        element["id"] = f"{target_id}-data{index:02d}"
    for index, artifact in enumerate(finding["artifacts"], 1):
        artifact["id"] = f"{target_id}-artifact{index:02d}"
    return finding


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--model-id", required=True)
    parser.add_argument("--run-root", type=Path, default=ROOT / "research" / "runs")
    parser.add_argument(
        "--plan-path",
        type=Path,
        help="Use an adjudicator-generated plan and snapshot it as synthesis-plan.json.",
    )
    args = parser.parse_args()
    run_dir = args.run_root / args.model_id.casefold()
    plan_path = args.plan_path or (run_dir / "synthesis-plan.json")
    plan = json.loads(plan_path.read_text(encoding="utf-8"))
    if args.plan_path:
        write_json(run_dir / "synthesis-plan.json", plan)
    policy = load_provider_policy()
    active = active_providers(policy)
    waived = waived_provider_names(policy)
    providers = {
        provider: json.loads((run_dir / f"{provider}.result.json").read_text(encoding="utf-8"))
        for provider in active
    }
    if len(active) == 1 and (plan.get("add_findings") or plan.get("add_functions")):
        raise ValueError("single-provider synthesis cannot add nodes from a waived provider")

    source_by_url: dict[str, dict[str, Any]] = {}
    source_maps: dict[str, dict[str, str]] = {provider: {} for provider in active}
    for provider in active:
        for source in providers[provider]["sources"]:
            url_key = source["url"].rstrip("/")
            if url_key not in source_by_url:
                source_by_url[url_key] = copy.deepcopy(source)
            canonical_id = f"SRC-{list(source_by_url).index(url_key) + 1:03d}"
            source_maps[provider][source["id"]] = canonical_id
            source_by_url[url_key]["id"] = canonical_id

    transformed = {
        provider: remap_refs(providers[provider], source_maps[provider])
        for provider in providers
    }
    base_provider = plan["base_provider"]
    if base_provider not in active:
        raise ValueError(f"base provider is not active under provider policy: {base_provider}")
    result = copy.deepcopy(transformed[base_provider])
    result["sources"] = list(source_by_url.values())

    for addition in plan.get("add_findings", []):
        provider = addition["provider"]
        finding = find_finding(transformed[provider], addition["source_finding_id"])
        finding = rekey_finding(finding, addition.get("target_finding_id", finding["id"]))
        target_layer = find_layer(result, addition["target_layer_id"])
        if any(item["id"] == finding["id"] for item in target_layer["findings"]):
            raise ValueError(f"duplicate finding ID in synthesis: {finding['id']}")
        target_layer["findings"].append(finding)

    function_ids = {function["id"] for function in result["functions"]}
    for addition in plan.get("add_functions", []):
        provider = addition["provider"]
        function = next(
            copy.deepcopy(item) for item in transformed[provider]["functions"]
            if item["id"] == addition["source_function_id"]
        )
        function["id"] = addition.get("target_function_id", function["id"])
        if function["id"] not in function_ids:
            result["functions"].append(function)
            function_ids.add(function["id"])

    if len(active) > 1 and plan.get("merge_service_layers", True):
        other_provider = "grok" if base_provider == "claude" else "claude"
        other_service = transformed[other_provider]["service_layers"]
        result["service_layers"]["policies"] = unique(
            result["service_layers"]["policies"] + other_service["policies"]
        )
        for key in ("exceptions", "audit_requirements"):
            result["service_layers"]["access"][key] = unique(
                result["service_layers"]["access"][key] + other_service["access"][key]
            )

    if len(active) > 1:
        other_provider = "grok" if base_provider == "claude" else "claude"
        for key in ("known_omissions", "conflicts", "regional_assumptions", "adversarial_checks"):
            result["coverage"][key] = unique(
                result["coverage"][key] + transformed[other_provider]["coverage"][key]
            )
    result["coverage"]["confidence"] = plan.get("confidence", "medium")
    result["coverage"]["claim"] = plan["coverage_claim"]

    validation = validate(result, args.model_id)
    result_path = run_dir / "synthesis.result.json"
    write_json(result_path, result)
    write_json(run_dir / "synthesis.validation.json", validation)
    input_hashes = {
        provider: hashlib.sha256((run_dir / f"{provider}.result.json").read_bytes()).hexdigest()
        for provider in providers
    }
    publication_holds = list(plan.get("publication_holds", []))
    if len(active) == 1:
        publication_holds = unique(publication_holds + [
            "Independent second-provider review was explicitly waived by the repository owner; this Claude-only result remains a reviewable draft."
        ])
    publishable = (
        len(active) > 1
        and validation["valid"]
        and not plan.get("critical_conflicts", [])
        and not publication_holds
    )
    reviewable = validation["valid"] and not plan.get("critical_conflicts", [])
    adjudication = {
        "contract_version": "1.0.0",
        "model_id": args.model_id,
        "generated_at": datetime.now(timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ"),
        "input_sha256": input_hashes,
        "provider_mode": policy["mode"],
        "active_providers": active,
        "waived_providers": waived,
        "provider_policy": policy,
        "base_provider": base_provider,
        "boundary_decision": plan["boundary_decision"],
        "decisions": plan["decisions"],
        "critical_conflicts": plan.get("critical_conflicts", []),
        "deferred_research": plan.get("deferred_research", []),
        "publication_holds": publication_holds,
        "status": "publishable-draft" if publishable else "reviewable-draft",
        "publishable": publishable,
        "reviewable": reviewable,
        "validation": validation,
    }
    write_json(run_dir / "provider-policy.json", policy)
    write_json(run_dir / "adjudication.json", adjudication)
    print(json.dumps(adjudication, ensure_ascii=False, indent=2))
    return 0 if adjudication["reviewable"] else 1


if __name__ == "__main__":
    raise SystemExit(main())
