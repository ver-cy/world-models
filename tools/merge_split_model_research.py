#!/usr/bin/env python3
"""Deterministically merge validated bounded passes from one research provider.

The merger performs no semantic synthesis.  It keeps the model boundary from a
designated base part, service layers from a designated governance part, and
stable-unions the independently scoped structures.  Any identity mismatch,
duplicate local ID, duplicate question, unresolved source reference, or final
validation error fails closed.
"""

from __future__ import annotations

import argparse
from copy import deepcopy
from datetime import datetime, timezone
import hashlib
import json
from pathlib import Path
import re
from typing import Any

from run_model_research import ROOT, write_json
from validate_model_research import validate


IDENTITY_FIELDS = ("registry_id", "model_id", "name", "entry_kind")
CONFIDENCE_RANK = {"low": 0, "medium": 1, "high": 2}
SOURCE_TOKEN = re.compile(r"\bSRC-[0-9]{3}\b")


def sha256(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()


def canonical_url_key(url: str) -> str:
    """Collapse only presentation-suffix variants of the same HTTPS resource."""
    normalized = url.strip().rstrip("/")
    return re.sub(r"\.(?:html?|xhtml)$", "", normalized, flags=re.IGNORECASE)


def stable_unique(values: list[Any]) -> list[Any]:
    seen: set[str] = set()
    result = []
    for value in values:
        key = json.dumps(value, ensure_ascii=False, sort_keys=True, separators=(",", ":"))
        if key not in seen:
            seen.add(key)
            result.append(value)
    return result


def remap_source_refs(value: Any, mapping: dict[str, str], path: str = "$") -> Any:
    if isinstance(value, str):
        def replace_source_token(match: re.Match[str]) -> str:
            source_id = match.group(0)
            if source_id not in mapping:
                raise ValueError(f"{path} contains unknown source token {source_id}")
            return mapping[source_id]

        return SOURCE_TOKEN.sub(replace_source_token, value)
    if isinstance(value, list):
        return [remap_source_refs(child, mapping, f"{path}[{index}]") for index, child in enumerate(value)]
    if not isinstance(value, dict):
        return deepcopy(value)
    result: dict[str, Any] = {}
    for key, child in value.items():
        child_path = f"{path}.{key}"
        if key != "source_refs":
            result[key] = remap_source_refs(child, mapping, child_path)
            continue
        missing = [source_id for source_id in child if source_id not in mapping]
        if missing:
            raise ValueError(f"{child_path} contains unknown split-part source IDs: {missing}")
        result[key] = stable_unique([mapping[source_id] for source_id in child])
    return result


def parse_part(value: str) -> tuple[str, Path]:
    label, separator, raw_path = value.partition("=")
    if not separator or not label or not raw_path:
        raise argparse.ArgumentTypeError("part must be LABEL=PATH")
    return label, Path(raw_path)


def merge(args: argparse.Namespace) -> tuple[dict[str, Any], dict[str, Any]]:
    labels = [label for label, _ in args.part]
    if len(labels) != len(set(labels)):
        raise ValueError("split-part labels are not unique")
    if args.base_part not in labels:
        raise ValueError(f"base part is absent: {args.base_part}")
    if args.service_part not in labels:
        raise ValueError(f"service part is absent: {args.service_part}")
    coverage_plan = json.loads(args.coverage_plan.read_text(encoding="utf-8"))
    if not isinstance(coverage_plan.get("claim"), str) or not coverage_plan["claim"].strip():
        raise ValueError("coverage plan must contain a non-empty claim")
    coverage_dimensions = coverage_plan.get("dimensions")
    if not isinstance(coverage_dimensions, list) or len(coverage_dimensions) < 10:
        raise ValueError("coverage plan must route at least ten dimensions")

    parts: dict[str, dict[str, Any]] = {}
    reports: dict[str, dict[str, Any]] = {}
    paths: dict[str, Path] = {}
    for label, path in args.part:
        if not path.is_file():
            raise ValueError(f"split-part result is absent: {path}")
        data = json.loads(path.read_text(encoding="utf-8"))
        report = validate(data, args.model_id)
        if not report["valid"]:
            raise ValueError(f"split part {label} is invalid: {json.dumps(report, ensure_ascii=False)}")
        parts[label], reports[label], paths[label] = data, report, path

    base_identity = {field: parts[args.base_part]["model"][field] for field in IDENTITY_FIELDS}
    for label, data in parts.items():
        identity = {field: data["model"][field] for field in IDENTITY_FIELDS}
        if identity != base_identity:
            raise ValueError(f"model identity differs in split part {label}")

    sources: list[dict[str, Any]] = []
    source_by_url: dict[str, str] = {}
    mappings: dict[str, dict[str, str]] = {}
    source_metadata_variants: list[dict[str, Any]] = []
    for label in labels:
        mappings[label] = {}
        for source in parts[label]["sources"]:
            url_key = canonical_url_key(source["url"])
            target_id = source_by_url.get(url_key)
            if target_id is None:
                target_id = f"SRC-{len(sources) + 1:03d}"
                merged_source = deepcopy(source)
                merged_source["id"] = target_id
                sources.append(merged_source)
                source_by_url[url_key] = target_id
            else:
                retained = next(item for item in sources if item["id"] == target_id)
                comparable = {key: value for key, value in source.items() if key != "id"}
                retained_comparable = {key: value for key, value in retained.items() if key != "id"}
                if comparable != retained_comparable:
                    source_metadata_variants.append({
                        "part": label,
                        "url": source["url"],
                        "retained_source_id": target_id,
                        "differing_fields": sorted(
                            key for key in comparable if comparable.get(key) != retained_comparable.get(key)
                        ),
                    })
            mappings[label][source["id"]] = target_id

    remapped = {
        label: remap_source_refs(parts[label], mappings[label])
        for label in labels
    }
    base = remapped[args.base_part]
    model = deepcopy(base["model"])

    bundles = [
        deepcopy(bundle)
        for label in labels
        for bundle in remapped[label]["structure"]["bundles"]
    ]
    functions = stable_unique([
        deepcopy(function)
        for label in labels
        for function in remapped[label]["functions"]
    ])
    composition = stable_unique([
        deepcopy(item)
        for label in labels
        for item in remapped[label]["composition"]
    ])

    coverages = [remapped[label]["coverage"] for label in labels]
    confidence = min(
        (coverage["confidence"] for coverage in coverages),
        key=lambda value: CONFIDENCE_RANK[value],
    )
    routed_checklist = []
    routed_keys: set[tuple[str, str]] = set()
    for route in coverage_dimensions:
        if not isinstance(route, dict):
            raise ValueError("coverage dimension route must be an object")
        label = route.get("part")
        dimension = route.get("dimension")
        if label not in remapped or not isinstance(dimension, str):
            raise ValueError(f"invalid coverage dimension route: {route}")
        key = (label, dimension.casefold())
        if key in routed_keys:
            raise ValueError(f"duplicate coverage dimension route: {route}")
        routed_keys.add(key)
        matches = [
            item for item in remapped[label]["coverage"]["checklist"]
            if item["dimension"].casefold() == dimension.casefold()
        ]
        if len(matches) != 1:
            raise ValueError(
                f"coverage route {label}/{dimension} matched {len(matches)} checklist items"
            )
        routed_checklist.append(deepcopy(matches[0]))

    def routed_coverage_values(field: str, minimum: int = 0) -> list[str]:
        routes = coverage_plan.get(field)
        if not isinstance(routes, list) or len(routes) < minimum:
            raise ValueError(f"coverage plan must route at least {minimum} {field} values")
        values = []
        for route in routes:
            if not isinstance(route, dict):
                raise ValueError(f"{field} route must be an object")
            label, index = route.get("part"), route.get("index")
            if label not in remapped or not isinstance(index, int):
                raise ValueError(f"invalid {field} route: {route}")
            source_values = remapped[label]["coverage"][field]
            if index < 0 or index >= len(source_values):
                raise ValueError(f"{field} route is out of range: {route}")
            values.append(source_values[index])
        return stable_unique(values)

    coverage = {
        "claim": coverage_plan["claim"].strip(),
        "confidence": confidence,
        "checklist": routed_checklist,
        "known_omissions": routed_coverage_values("known_omissions"),
        "conflicts": stable_unique([
            item for partial in coverages for item in partial["conflicts"]
        ]),
        "regional_assumptions": routed_coverage_values("regional_assumptions"),
        "adversarial_checks": routed_coverage_values("adversarial_checks", minimum=3),
    }

    service_layers = deepcopy(remapped[args.service_part]["service_layers"])
    service_patch = None
    if args.service_patch:
        service_patch = json.loads(args.service_patch.read_text(encoding="utf-8"))
        allowed = {
            "contract_version", "basis", "identity_priority_insert_after_master",
            "access_exceptions_append",
        }
        unexpected = sorted(set(service_patch) - allowed)
        if unexpected:
            raise ValueError(f"unsupported service patch fields: {unexpected}")
        for field in ("identity_priority_insert_after_master", "access_exceptions_append"):
            if not isinstance(service_patch.get(field), list) or not all(
                isinstance(item, str) and item.strip() for item in service_patch[field]
            ):
                raise ValueError(f"service patch {field} must be a list of non-empty strings")
        identity_priority = service_layers["artifact_rules"]["identity_priority"]
        service_layers["artifact_rules"]["identity_priority"] = stable_unique(
            identity_priority[:1]
            + service_patch["identity_priority_insert_after_master"]
            + identity_priority[1:]
        )
        service_layers["access"]["exceptions"] = stable_unique(
            service_layers["access"]["exceptions"]
            + service_patch["access_exceptions_append"]
        )

    result = {
        "schema_version": "1.0.0",
        "model": model,
        "sources": sources,
        "structure": {"bundles": bundles},
        "functions": functions,
        "composition": composition,
        "service_layers": service_layers,
        "coverage": coverage,
    }
    report = validate(result, args.model_id)
    manifest = {
        "contract_version": "1.0.0",
        "provider": "claude",
        "provider_model": "split-pass-merge",
        "model_id": args.model_id,
        "status": "complete" if report["valid"] else "validation-failed",
        "generated_at": datetime.now(timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ"),
        "merge_policy": "deterministic-stable-union-v1",
        "base_part": args.base_part,
        "service_part": args.service_part,
        "coverage_plan": str(args.coverage_plan),
        "coverage_plan_sha256": sha256(args.coverage_plan),
        "service_patch": str(args.service_patch) if args.service_patch else None,
        "service_patch_sha256": sha256(args.service_patch) if args.service_patch else None,
        "parts": [
            {
                "label": label,
                "path": str(paths[label]),
                "sha256": sha256(paths[label]),
                "validation": reports[label],
            }
            for label in labels
        ],
        "source_metadata_variants": source_metadata_variants,
        "narrative_differences": {
            label: {
                field: remapped[label]["model"][field] != base["model"][field]
                for field in ("purpose", "scope_statement")
            }
            for label in labels if label != args.base_part
        },
        "validation": report,
    }
    return result, manifest


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--model-id", required=True)
    parser.add_argument("--part", action="append", type=parse_part, required=True)
    parser.add_argument("--base-part", required=True)
    parser.add_argument("--service-part", required=True)
    parser.add_argument("--coverage-plan", type=Path, required=True)
    parser.add_argument("--service-patch", type=Path)
    parser.add_argument("--output-root", type=Path, default=ROOT / "research" / "runs")
    args = parser.parse_args()
    run_dir = args.output_root / args.model_id.casefold()
    result, manifest = merge(args)
    result_path = run_dir / "claude.result.json"
    validation_path = run_dir / "claude.validation.json"
    manifest_path = run_dir / "claude.manifest.json"
    write_json(result_path, result)
    write_json(validation_path, manifest["validation"])
    manifest["result_sha256"] = sha256(result_path)
    write_json(manifest_path, manifest)
    print(json.dumps({"result": str(result_path), **manifest["validation"]}, ensure_ascii=False, indent=2))
    return 0 if manifest["validation"]["valid"] else 1


if __name__ == "__main__":
    raise SystemExit(main())
