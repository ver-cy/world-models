#!/usr/bin/env python3
"""Normalize a substantive provider answer that failed JSON transport parsing.

The raw provider wrapper remains immutable evidence.  This pass gives Claude no
tools and asks it only to repair/extract the supplied JSON into the canonical
schema; it must not perform research or add facts.
"""

from __future__ import annotations

import argparse
import hashlib
import json
import shutil
import subprocess
from pathlib import Path
from typing import Any

from run_model_research import ROOT, SCHEMA_PATH, extract_result, now, write_json
from validate_model_research import validate


def repair_cross_grain_id_collisions(result: dict[str, Any]) -> list[dict[str, str]]:
    """Namespace unambiguous duplicate IDs without changing their meaning.

    A question and its answer element often receive the same natural local ID
    from a provider. Vercy's canonical contract requires global uniqueness, so
    the later node receives a stable grain prefix. A data element repeated in
    distinct findings is equally safe to namespace with its parent finding ID.
    Other duplicates within the same grain are left untouched for semantic
    adjudication rather than guessed.
    """
    nodes: list[tuple[dict[str, Any], str, str]] = []
    for bundle in result.get("structure", {}).get("bundles", []):
        nodes.append((bundle, "bundle", ""))
        for layer in bundle.get("layers", []):
            nodes.append((layer, "layer", ""))
            for finding in layer.get("findings", []):
                finding_id = finding.get("id", "")
                nodes.append((finding, "finding", ""))
                nodes.extend((item, "question", finding_id) for item in finding.get("questions", []))
                nodes.extend((item, "data", finding_id) for item in finding.get("data_elements", []))
                nodes.extend((item, "artifact", finding_id) for item in finding.get("artifacts", []))
    nodes.extend((item, "function", "") for item in result.get("functions", []))

    by_id: dict[str, list[tuple[dict[str, Any], str, str]]] = {}
    for node, grain, parent_id in nodes:
        by_id.setdefault(node.get("id", ""), []).append((node, grain, parent_id))
    occupied = {identifier for identifier in by_id if identifier}
    repairs: list[dict[str, str]] = []
    for identifier, matches in by_id.items():
        if not identifier or len(matches) < 2:
            continue
        grains = [grain for _, grain, _ in matches]
        cross_grain = len(grains) == len(set(grains))
        parent_ids = [parent_id for _, _, parent_id in matches]
        repeated_data_across_findings = (
            set(grains) == {"data"}
            and all(parent_ids)
            and len(parent_ids) == len(set(parent_ids))
        )
        if not cross_grain and not repeated_data_across_findings:
            continue
        for node, grain, parent_id in matches[1:]:
            prefix = parent_id if repeated_data_across_findings else grain
            candidate = f"{prefix}-{identifier}"
            counter = 2
            while candidate in occupied:
                candidate = f"{prefix}-{identifier}-{counter}"
                counter += 1
            node["id"] = candidate
            occupied.add(candidate)
            repair = {"from": identifier, "to": candidate, "grain": grain}
            if repeated_data_across_findings:
                repair["parent_finding_id"] = parent_id
            repairs.append(repair)
    return repairs


def repair_authoritative_identity_priority(result: dict[str, Any]) -> list[dict[str, str]]:
    """Make an already-authoritative identifier explicit as master-system ID.

    The semantic validator intentionally requires the first artifact identity
    priority to name the master system. Providers sometimes describe exactly
    that identifier as an authoritative register/court number without using the
    literal ``master-system`` token. Only that narrow, evidence-preserving case
    is normalized; UUIDs, hashes and otherwise ambiguous priorities are left for
    adjudication.
    """
    priority = (
        result.get("service_layers", {})
        .get("artifact_rules", {})
        .get("identity_priority", [])
    )
    if not priority or not isinstance(priority[0], str):
        return []
    first = priority[0]
    folded = first.casefold()
    if "master" in folded:
        return []
    is_authoritative_master_id = (
        "authoritative" in folded
        and any(token in folded for token in ("register", "registry", "court", "directory"))
        and any(token in folded for token in ("identifier", "number", "code"))
    )
    if not is_authoritative_master_id:
        return []
    replacement = f"Authoritative master-system identifier: {first}"
    priority[0] = replacement
    return [{
        "kind": "identity-priority-label",
        "from": first,
        "to": replacement,
    }]


def provider_text(wrapper: dict[str, Any]) -> str:
    for key in ("text", "result", "response", "output"):
        value = wrapper.get(key)
        if isinstance(value, str) and value.strip():
            return value
    raise SystemExit("raw provider wrapper has no textual result to normalize")


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--model-id", required=True)
    parser.add_argument("--provider", default="grok", choices=("claude", "grok"))
    parser.add_argument("--normalizer-model", default="opus")
    parser.add_argument("--run-root", type=Path, default=ROOT / "research" / "runs")
    parser.add_argument("--timeout", type=int, default=1800)
    parser.add_argument("--force", action="store_true")
    parser.add_argument("--repair-existing", action="store_true")
    args = parser.parse_args()

    run_dir = args.run_root / args.model_id.casefold()
    raw_path = run_dir / f"{args.provider}.raw.json"
    result_path = run_dir / f"{args.provider}.result.json"
    validation_path = run_dir / f"{args.provider}.validation.json"
    provider_manifest_path = run_dir / f"{args.provider}.manifest.json"
    normalization_raw_path = run_dir / f"{args.provider}.normalization.raw.json"
    normalization_manifest_path = run_dir / f"{args.provider}.normalization.manifest.json"
    if args.repair_existing:
        result = json.loads(result_path.read_text(encoding="utf-8"))
        repairs = repair_cross_grain_id_collisions(result)
        semantic_repairs = repair_authoritative_identity_priority(result)
        report = validate(result, args.model_id)
        write_json(result_path, result)
        write_json(validation_path, report)
        result_sha256 = hashlib.sha256(result_path.read_bytes()).hexdigest()
        normalization_manifest: dict[str, Any] | None = None
        if normalization_manifest_path.is_file():
            normalization_manifest = json.loads(normalization_manifest_path.read_text(encoding="utf-8"))
            recorded_repairs = normalization_manifest.get("cross_grain_id_repairs", [])
            recorded_semantic_repairs = normalization_manifest.get("semantic_repairs", [])
            normalization_manifest.update({
                "status": "complete" if report["valid"] else "validation-failed",
                "cross_grain_id_repairs": recorded_repairs + [
                    repair for repair in repairs if repair not in recorded_repairs
                ],
                "semantic_repairs": recorded_semantic_repairs + [
                    repair for repair in semantic_repairs if repair not in recorded_semantic_repairs
                ],
                "result_sha256": result_sha256,
                "validation": report,
            })
            write_json(normalization_manifest_path, normalization_manifest)
        provider_manifest = json.loads(provider_manifest_path.read_text(encoding="utf-8"))
        recorded_repairs = provider_manifest.get("cross_grain_id_repairs", [])
        recorded_semantic_repairs = provider_manifest.get("semantic_repairs", [])
        provider_manifest.update({
            "status": "complete" if report["valid"] else "validation-failed",
            "result_sha256": result_sha256,
            "cross_grain_id_repairs": recorded_repairs + [
                repair for repair in repairs if repair not in recorded_repairs
            ],
            "semantic_repairs": recorded_semantic_repairs + [
                repair for repair in semantic_repairs if repair not in recorded_semantic_repairs
            ],
            "validation": report,
        })
        if normalization_manifest is not None:
            provider_manifest.update({
                "normalization_status": "complete" if report["valid"] else "validation-failed",
                "normalization_manifest": normalization_manifest_path.name,
            })
        write_json(provider_manifest_path, provider_manifest)
        print(json.dumps({
            "result": str(result_path),
            "repairs": repairs,
            "semantic_repairs": semantic_repairs,
            **report,
        }, ensure_ascii=False, indent=2))
        return 0 if report["valid"] else 1
    if result_path.exists() and not args.force:
        print(f"result already exists; use --force to replace: {result_path}")
        return 0

    wrapper = json.loads(raw_path.read_text(encoding="utf-8"))
    raw_text = provider_text(wrapper)
    schema_data = json.loads(SCHEMA_PATH.read_text(encoding="utf-8"))
    schema_data.pop("$schema", None)
    schema_text = json.dumps(schema_data, separators=(",", ":"))
    prompt = f"""You are a syntax-preserving JSON normalizer, not a researcher.

The supplied Grok research answer is substantive but its JSON transport has
syntax mistakes and may contain progress narration before the object. Extract
the single object whose schema_version is 1.0.0 and make only the minimum edits
needed to satisfy the supplied Vercy schema:

- preserve all supported claims, sources, bundles, layers, findings, questions,
  artifacts, functions, service rules, omissions, conflicts and caveats;
- fix punctuation, misplaced braces and field names/types only;
- remove narration and unsupported extra fields;
- do not browse, infer, add facts, improve coverage or merge another provider;
- if malformed content cannot be placed without inventing meaning, omit that
  fragment instead of guessing.

Return only the schema-conformant object through structured output.

<provider-output provider="{args.provider}" model-id="{args.model_id}">
{raw_text}
</provider-output>
"""

    executable = shutil.which("claude")
    if not executable:
        raise SystemExit("claude executable not found")
    command = [
        executable,
        "-p",
        "--model", args.normalizer_model,
        "--effort", "max",
        "--permission-mode", "dontAsk",
        "--tools", "",
        "--disallowedTools", "Bash,Write,Edit,NotebookEdit,Read,Glob,Grep,WebSearch,WebFetch",
        "--disable-slash-commands",
        "--no-session-persistence",
        "--output-format", "json",
        "--json-schema", schema_text,
    ]
    started_at = now()
    completed = subprocess.run(
        command,
        cwd=ROOT,
        input=prompt,
        capture_output=True,
        text=True,
        encoding="utf-8",
        errors="replace",
        timeout=args.timeout,
        check=False,
    )
    normalization_manifest: dict[str, Any] = {
        "contract_version": "1.0.0",
        "model_id": args.model_id,
        "source_provider": args.provider,
        "normalizer_provider": "claude",
        "normalizer_model": args.normalizer_model,
        "started_at": started_at,
        "completed_at": now(),
        "source_raw_sha256": hashlib.sha256(raw_path.read_bytes()).hexdigest(),
        "schema_sha256": hashlib.sha256(SCHEMA_PATH.read_bytes()).hexdigest(),
        "tools_enabled": [],
        "return_code": completed.returncode,
    }
    if completed.returncode != 0:
        normalization_manifest.update({
            "status": "provider-error",
            "stderr_sha256": hashlib.sha256(completed.stderr.encode("utf-8")).hexdigest(),
            "stderr_bytes": len(completed.stderr.encode("utf-8")),
        })
        write_json(normalization_manifest_path, normalization_manifest)
        print("normalizer failed; stderr was suppressed and only its hash was recorded")
        return completed.returncode or 2

    normalized_wrapper = json.loads(completed.stdout)
    safe_wrapper = {
        key: value for key, value in normalized_wrapper.items()
        if key not in {"thought", "thinking", "reasoning"}
    }
    write_json(normalization_raw_path, safe_wrapper)
    result = extract_result(normalized_wrapper)
    repairs = repair_cross_grain_id_collisions(result)
    semantic_repairs = repair_authoritative_identity_priority(result)
    report = validate(result, args.model_id)
    write_json(result_path, result)
    write_json(validation_path, report)
    normalization_manifest.update({
        "status": "complete" if report["valid"] else "validation-failed",
        "cross_grain_id_repairs": repairs,
        "semantic_repairs": semantic_repairs,
        "result_sha256": hashlib.sha256(result_path.read_bytes()).hexdigest(),
        "validation": report,
    })
    session_id = normalized_wrapper.get("session_id") or normalized_wrapper.get("sessionId")
    if session_id:
        normalization_manifest["session_id"] = session_id
    write_json(normalization_manifest_path, normalization_manifest)

    provider_manifest = json.loads(provider_manifest_path.read_text(encoding="utf-8"))
    provider_manifest.update({
        "status": "complete" if report["valid"] else "validation-failed",
        "normalization_status": "complete" if report["valid"] else "validation-failed",
        "normalization_manifest": normalization_manifest_path.name,
        "result_sha256": normalization_manifest["result_sha256"],
        "cross_grain_id_repairs": repairs,
        "semantic_repairs": semantic_repairs,
        "validation": report,
    })
    write_json(provider_manifest_path, provider_manifest)
    print(json.dumps({"result": str(result_path), **report}, ensure_ascii=False, indent=2))
    return 0 if report["valid"] else 1


if __name__ == "__main__":
    raise SystemExit(main())
