#!/usr/bin/env python3
"""Create a reviewable synthesis plan from two validated provider results.

This is a no-tools semantic adjudication pass. It cannot research new facts or
publish. The deterministic synthesis and validators remain separate gates.
"""

from __future__ import annotations

import argparse
import hashlib
import json
import shutil
import subprocess
from pathlib import Path
from typing import Any

from run_model_research import ROOT, extract_result, now, write_json


PLAN_SCHEMA: dict[str, Any] = {
    "type": "object",
    "additionalProperties": False,
    "required": [
        "base_provider", "confidence", "coverage_claim", "boundary_decision",
        "add_findings", "add_functions", "merge_service_layers", "decisions",
        "critical_conflicts", "publication_holds", "deferred_research",
    ],
    "properties": {
        "base_provider": {"enum": ["claude", "grok"]},
        "confidence": {"enum": ["low", "medium", "high"]},
        "coverage_claim": {"type": "string", "minLength": 40},
        "boundary_decision": {
            "type": "object", "additionalProperties": False,
            "required": ["entry_kind", "status", "rationale"],
            "properties": {
                "entry_kind": {"type": "string", "minLength": 1},
                "status": {"enum": ["accepted", "reclassified", "split", "merge", "deferred"]},
                "rationale": {"type": "string", "minLength": 40},
            },
        },
        "add_findings": {
            "type": "array", "maxItems": 12,
            "items": {
                "type": "object", "additionalProperties": False,
                "required": ["provider", "source_finding_id", "target_finding_id", "target_layer_id", "rationale"],
                "properties": {
                    "provider": {"enum": ["claude", "grok"]},
                    "source_finding_id": {"type": "string", "minLength": 1},
                    "target_finding_id": {"type": "string", "minLength": 1},
                    "target_layer_id": {"type": "string", "minLength": 1},
                    "rationale": {"type": "string", "minLength": 30},
                },
            },
        },
        "add_functions": {
            "type": "array", "maxItems": 8,
            "items": {
                "type": "object", "additionalProperties": False,
                "required": ["provider", "source_function_id", "rationale"],
                "properties": {
                    "provider": {"enum": ["claude", "grok"]},
                    "source_function_id": {"type": "string", "minLength": 1},
                    "target_function_id": {"type": "string", "minLength": 1},
                    "rationale": {"type": "string", "minLength": 30},
                },
            },
        },
        "merge_service_layers": {"const": True},
        "decisions": {
            "type": "array", "minItems": 5, "maxItems": 20,
            "items": {
                "type": "object", "additionalProperties": False,
                "required": ["concept", "disposition", "rationale"],
                "properties": {
                    "concept": {"type": "string", "minLength": 3},
                    "disposition": {"type": "string", "minLength": 3},
                    "rationale": {"type": "string", "minLength": 30},
                },
            },
        },
        "critical_conflicts": {"type": "array", "items": {"type": "string", "minLength": 20}},
        "publication_holds": {"type": "array", "minItems": 1, "items": {"type": "string", "minLength": 20}},
        "deferred_research": {"type": "array", "minItems": 2, "items": {"type": "string", "minLength": 20}},
    },
}


def compact_result(result: dict[str, Any]) -> dict[str, Any]:
    structure = []
    for bundle in result["structure"]["bundles"]:
        layers = []
        for layer in bundle["layers"]:
            findings = []
            for finding in layer["findings"]:
                findings.append({
                    "id": finding["id"],
                    "name": finding["name"],
                    "description": finding["description"],
                    "source_refs": finding["source_refs"],
                    "questions": [
                        {"id": q["id"], "text": q["text"], "kind": q["kind"]}
                        for q in finding["questions"]
                    ],
                    "artifacts": [
                        {
                            "id": a["id"], "name": a["name"],
                            "media_or_form": a.get("media_or_form"),
                            "serial": a.get("serial"),
                        }
                        for a in finding["artifacts"]
                    ],
                    "inline_only_rationale": finding.get("inline_only_rationale"),
                })
            layers.append({"id": layer["id"], "name": layer["name"], "findings": findings})
        structure.append({"id": bundle["id"], "name": bundle["name"], "layers": layers})
    return {
        "model": result["model"],
        "sources": [
            {key: source.get(key) for key in ("id", "title", "organization", "url", "version_or_date", "primary_source", "authority_tier")}
            for source in result["sources"]
        ],
        "structure": structure,
        "functions": [
            {key: function.get(key) for key in ("id", "name", "description", "source_refs")}
            for function in result["functions"]
        ],
        "coverage": result["coverage"],
    }


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--model-id", required=True)
    parser.add_argument("--model", default="opus")
    parser.add_argument("--run-root", type=Path, default=ROOT / "research" / "runs")
    parser.add_argument("--output-name", default="synthesis-plan.auto.json")
    parser.add_argument("--timeout", type=int, default=1800)
    parser.add_argument("--force", action="store_true")
    args = parser.parse_args()

    run_dir = args.run_root / args.model_id.casefold()
    output_path = run_dir / args.output_name
    manifest_path = run_dir / "adjudication-run.manifest.json"
    if output_path.exists() and not args.force:
        print(f"adjudication plan exists; use --force to replace: {output_path}")
        return 0
    providers = {
        provider: json.loads((run_dir / f"{provider}.result.json").read_text(encoding="utf-8"))
        for provider in ("claude", "grok")
    }
    comparison = json.loads((run_dir / "comparison.json").read_text(encoding="utf-8"))
    payload = {
        "model_id": args.model_id,
        "providers": {provider: compact_result(result) for provider, result in providers.items()},
        "comparison": comparison,
    }
    prompt = """You are the Vercy dual-research adjudicator. You cannot browse or
add facts. Compare the two independently researched, already validated provider
results below and return an explicit synthesis plan for the deterministic Vercy
synthesizer.

Rules:
- Choose the provider with the clearest complete boundaries as base; size alone
  is not decisive.
- Add a finding only when it is materially missing from the base, evidence-backed
  in the source provider, non-duplicative, and fits an existing base layer.
- The deterministic synthesizer copies an accepted finding verbatim. Inspect its
  name, description and questions as a whole: reject or defer the finding when
  any of them contradict the chosen aggregate root, entry kind or boundary. Do
  not accept a node on the assumption that its wording will be edited later.
- `provider` on each addition must be the non-base source provider; use exact
  source IDs and exact existing target layer IDs.
- Prefer rejection/deferral over duplicate or weakly supported structure.
- Decide the model boundary and entry kind before accepting nodes.
- Record important accepted and rejected concepts with concrete rationale.
- Critical conflicts are only unresolved contradictions that prevent even a
  public research draft. Source/live-version and domain-profile verification are
  publication holds instead.
- Always retain source verification and multi-profile validation as holds unless
  the evidence pack itself proves they are complete.
- Do not claim universal completeness.

Return only the structured synthesis-plan object.

<evidence-pack>
""" + json.dumps(payload, ensure_ascii=False, separators=(",", ":")) + "\n</evidence-pack>\n"

    executable = shutil.which("claude")
    if not executable:
        raise SystemExit("claude executable not found")
    schema_text = json.dumps(PLAN_SCHEMA, separators=(",", ":"))
    command = [
        executable, "-p", "--model", args.model, "--effort", "max",
        "--permission-mode", "dontAsk", "--tools", "",
        "--disallowedTools", "Bash,Write,Edit,NotebookEdit,Read,Glob,Grep,WebSearch,WebFetch",
        "--disable-slash-commands", "--no-session-persistence",
        "--output-format", "json", "--json-schema", schema_text,
    ]
    started_at = now()
    completed = subprocess.run(
        command, cwd=ROOT, input=prompt, capture_output=True, text=True,
        encoding="utf-8", errors="replace", timeout=args.timeout, check=False,
    )
    manifest: dict[str, Any] = {
        "contract_version": "1.0.0", "model_id": args.model_id,
        "provider": "claude", "provider_model": args.model,
        "started_at": started_at, "completed_at": now(), "tools_enabled": [],
        "return_code": completed.returncode,
        "input_sha256": hashlib.sha256(json.dumps(payload, sort_keys=True, ensure_ascii=False).encode("utf-8")).hexdigest(),
    }
    if completed.returncode != 0:
        manifest.update({
            "status": "provider-error",
            "stderr_sha256": hashlib.sha256(completed.stderr.encode("utf-8")).hexdigest(),
            "stderr_bytes": len(completed.stderr.encode("utf-8")),
        })
        write_json(manifest_path, manifest)
        print("adjudicator failed; stderr was suppressed and only its hash was recorded")
        return completed.returncode or 2
    wrapper = json.loads(completed.stdout)
    plan = extract_result(wrapper) if wrapper.get("schema_version") == "1.0.0" else None
    if plan is None:
        for key in ("structured_output", "structuredOutput", "output", "result", "response"):
            candidate = wrapper.get(key)
            if isinstance(candidate, dict) and "base_provider" in candidate:
                plan = candidate
                break
            if isinstance(candidate, str):
                try:
                    candidate = json.loads(candidate)
                except json.JSONDecodeError:
                    continue
                if isinstance(candidate, dict) and "base_provider" in candidate:
                    plan = candidate
                    break
    if not isinstance(plan, dict):
        manifest.update({"status": "parse-error"})
        write_json(manifest_path, manifest)
        raise SystemExit("adjudicator response did not contain a synthesis plan")
    write_json(output_path, plan)
    manifest.update({
        "status": "complete",
        "output": output_path.name,
        "output_sha256": hashlib.sha256(output_path.read_bytes()).hexdigest(),
    })
    session_id = wrapper.get("session_id") or wrapper.get("sessionId")
    if session_id:
        manifest["session_id"] = session_id
    write_json(manifest_path, manifest)
    print(output_path)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
