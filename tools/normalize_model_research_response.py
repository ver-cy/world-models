#!/usr/bin/env python3
"""Re-normalize an already captured provider wrapper without another AI call."""

from __future__ import annotations

import argparse
import hashlib
import json
from datetime import datetime, timezone
from pathlib import Path

from run_model_research import ROOT, extract_result, write_json
from validate_model_research import validate


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--provider", required=True, choices=["claude", "grok"])
    parser.add_argument("--model-id", required=True)
    parser.add_argument("--run-root", type=Path, default=ROOT / "research" / "runs")
    args = parser.parse_args()
    run_dir = args.run_root / args.model_id.casefold()
    raw_path = run_dir / f"{args.provider}.raw.json"
    result_path = run_dir / f"{args.provider}.result.json"
    validation_path = run_dir / f"{args.provider}.validation.json"
    manifest_path = run_dir / f"{args.provider}.manifest.json"

    wrapper = json.loads(raw_path.read_text(encoding="utf-8"))
    result = extract_result(wrapper)
    safe_wrapper = {
        key: value for key, value in wrapper.items()
        if key not in {"thought", "thinking", "reasoning"}
    }
    write_json(raw_path, safe_wrapper)
    write_json(result_path, result)
    report = validate(result, args.model_id)
    write_json(validation_path, report)
    manifest = json.loads(manifest_path.read_text(encoding="utf-8"))
    manifest.update({
        "completed_at": manifest.get("completed_at") or datetime.now(timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ"),
        "status": "complete" if report["valid"] else "validation-failed",
        "result_sha256": hashlib.sha256(result_path.read_bytes()).hexdigest(),
        "validation": report,
        "schema_sha256_at_validation": hashlib.sha256(
            (ROOT / "research" / "model-research.schema.json").read_bytes()
        ).hexdigest(),
    })
    session_id = wrapper.get("session_id") or wrapper.get("sessionId")
    if session_id:
        manifest["session_id"] = session_id
    manifest.pop("error", None)
    write_json(manifest_path, manifest)
    print(json.dumps(report, ensure_ascii=False, indent=2))
    return 0 if report["valid"] else 1


if __name__ == "__main__":
    raise SystemExit(main())
