#!/usr/bin/env python3
"""Validate provider research beyond the structural JSON Schema gate."""

from __future__ import annotations

import argparse
import json
import re
import sys
from collections import Counter
from pathlib import Path
from typing import Any

from jsonschema import Draft202012Validator, FormatChecker


ROOT = Path(__file__).resolve().parents[1]
SCHEMA_PATH = ROOT / "research" / "model-research.schema.json"
DATE_ID = re.compile(r"(?:^|-)\d{4}(?:\d{2}){1,2}(?:-|$)")


def walk_source_refs(value: Any, path: str = "$"):
    if isinstance(value, dict):
        for key, child in value.items():
            child_path = f"{path}.{key}"
            if key == "source_refs":
                yield child_path, child
            yield from walk_source_refs(child, child_path)
    elif isinstance(value, list):
        for index, child in enumerate(value):
            yield from walk_source_refs(child, f"{path}[{index}]")


def semantic_errors(data: dict[str, Any], expected_model_id: str | None = None) -> list[str]:
    errors: list[str] = []
    if expected_model_id and data.get("model", {}).get("model_id") != expected_model_id:
        errors.append(f"model_id does not match requested {expected_model_id}")

    sources = data.get("sources", [])
    source_ids = [source.get("id") for source in sources]
    if len(source_ids) != len(set(source_ids)):
        errors.append("source IDs are not unique")
    known_sources = set(source_ids)
    primary = [source for source in sources if source.get("primary_source")]
    if len(primary) < 4:
        errors.append("fewer than four primary sources")
    if len({source.get("organization", "").casefold() for source in primary}) < 3:
        errors.append("primary evidence comes from fewer than three organizations")
    for path, refs in walk_source_refs(data):
        for ref in refs if isinstance(refs, list) else []:
            if ref not in known_sources:
                errors.append(f"{path} contains unresolved source {ref}")

    all_ids: list[tuple[str, str]] = []
    questions: list[dict[str, Any]] = []
    findings = []
    bundles = data.get("structure", {}).get("bundles", [])
    for bundle in bundles:
        all_ids.append((bundle.get("id", ""), "bundle"))
        for layer in bundle.get("layers", []):
            all_ids.append((layer.get("id", ""), "layer"))
            for finding in layer.get("findings", []):
                findings.append(finding)
                all_ids.append((finding.get("id", ""), "finding"))
                questions.extend(finding.get("questions", []))
                for question in finding.get("questions", []):
                    all_ids.append((question.get("id", ""), "question"))
                for element in finding.get("data_elements", []):
                    all_ids.append((element.get("id", ""), "data-element"))
                artifacts = finding.get("artifacts", [])
                for artifact in artifacts:
                    all_ids.append((artifact.get("id", ""), "artifact"))
                rationale = finding.get("inline_only_rationale")
                if not artifacts and (not isinstance(rationale, str) or len(rationale.strip()) < 20):
                    errors.append(f"finding {finding.get('id')} has no artifact and no substantive inline-only rationale")
                if artifacts and rationale not in (None, ""):
                    errors.append(f"finding {finding.get('id')} has artifacts and an inline-only rationale")

    for function in data.get("functions", []):
        all_ids.append((function.get("id", ""), "function"))
    duplicates = [identifier for identifier, count in Counter(x[0] for x in all_ids).items() if count > 1]
    if duplicates:
        errors.append("local IDs are not globally unique: " + ", ".join(sorted(duplicates)[:20]))
    dated_ids = [identifier for identifier, _ in all_ids if DATE_ID.search(identifier)]
    if dated_ids:
        errors.append("stable IDs contain date-like components: " + ", ".join(sorted(dated_ids)[:20]))

    normalized_questions = [
        re.sub(r"[^a-z0-9]+", " ", q.get("text", "").casefold()).strip()
        for q in questions
    ]
    duplicate_questions = [text for text, count in Counter(normalized_questions).items() if text and count > 1]
    if duplicate_questions:
        errors.append(f"duplicate question texts detected ({len(duplicate_questions)})")
    kinds = {q.get("kind") for q in questions}
    minimum_kinds = 6 if data.get("model", {}).get("entry_kind") in {"mixin", "classifier"} else 8
    if len(kinds) < minimum_kinds:
        errors.append(f"question coverage uses only {len(kinds)} kinds; expected at least {minimum_kinds}")

    identity_priority = data.get("service_layers", {}).get("artifact_rules", {}).get("identity_priority", [])
    if not identity_priority or "master" not in identity_priority[0].casefold():
        errors.append("identity priority must start with the authoritative master-system identifier")
    timestamp_rule = data.get("service_layers", {}).get("artifact_rules", {}).get("timestamp_rule", "")
    for token in ("RFC 3339", "seconds", "offset"):
        if token.casefold() not in timestamp_rule.casefold():
            errors.append(f"timestamp rule does not explicitly require {token}")

    checklist_text = [
        f"{item.get('dimension', '')} {item.get('notes', '')}".casefold()
        for item in data.get("coverage", {}).get("checklist", [])
    ]
    aliases = {
        "identity": ("identity",),
        "lifecycle": ("lifecycle", "life cycle"),
        "relationships": ("relationship",),
        "temporal": ("temporal", "event time", "effective time"),
        "provenance": ("provenance",),
        "ownership": ("ownership", "owner"),
        "validation": ("validation", "conformance", "validity"),
        "access": ("access",),
        "interoperability": ("interoperability", "interoperable"),
    }
    missing_dimensions = [
        dimension for dimension, tokens in aliases.items()
        if not any(any(token in text for token in tokens) for text in checklist_text)
    ]
    delete_rules = " ".join(
        data.get("service_layers", {}).get("crud", {}).get("delete", [])
    ).casefold()
    if not any(token in delete_rules for token in ("retention", "retain", "tombstone", "retire", "deletion", "delete")):
        missing_dimensions.append("retention and deletion")
    missing_dimensions.sort()
    if missing_dimensions:
        errors.append("coverage checklist is missing: " + ", ".join(missing_dimensions))
    if not findings:
        errors.append("no findings were produced")
    return errors


def validate(data: dict[str, Any], expected_model_id: str | None = None) -> dict[str, Any]:
    schema = json.loads(SCHEMA_PATH.read_text(encoding="utf-8"))
    validator = Draft202012Validator(schema, format_checker=FormatChecker())
    schema_errors = [
        f"{'/'.join(str(part) for part in error.absolute_path) or '$'}: {error.message}"
        for error in sorted(validator.iter_errors(data), key=lambda item: list(item.absolute_path))
    ]
    semantic = semantic_errors(data, expected_model_id) if not schema_errors else []
    bundles = data.get("structure", {}).get("bundles", [])
    layers = [layer for bundle in bundles for layer in bundle.get("layers", [])]
    findings = [finding for layer in layers for finding in layer.get("findings", [])]
    questions = [question for finding in findings for question in finding.get("questions", [])]
    artifacts = [artifact for finding in findings for artifact in finding.get("artifacts", [])]
    return {
        "valid": not schema_errors and not semantic,
        "schema_errors": schema_errors,
        "semantic_errors": semantic,
        "counts": {
            "sources": len(data.get("sources", [])),
            "bundles": len(bundles),
            "layers": len(layers),
            "findings": len(findings),
            "questions": len(questions),
            "artifacts": len(artifacts),
            "functions": len(data.get("functions", [])),
        },
    }


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("path", type=Path)
    parser.add_argument("--model-id")
    parser.add_argument("--report", type=Path)
    args = parser.parse_args()
    data = json.loads(args.path.read_text(encoding="utf-8"))
    report = validate(data, args.model_id)
    rendered = json.dumps(report, ensure_ascii=False, indent=2) + "\n"
    if args.report:
        args.report.parent.mkdir(parents=True, exist_ok=True)
        args.report.write_text(rendered, encoding="utf-8")
    print(rendered, end="")
    return 0 if report["valid"] else 1


if __name__ == "__main__":
    sys.exit(main())
