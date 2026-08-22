#!/usr/bin/env python3
"""Ask the originating Grok session to repair JSON syntax without new research."""

from __future__ import annotations

import argparse
import json
import os
import shutil
import subprocess
import tempfile
from pathlib import Path

from run_model_research import ROOT, extract_result, write_json


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--model-id", required=True)
    parser.add_argument("--run-root", type=Path, default=ROOT / "research" / "runs")
    parser.add_argument("--timeout", type=int, default=1800)
    args = parser.parse_args()
    run_dir = args.run_root / args.model_id.casefold()
    raw_path = run_dir / "grok.raw.json"
    research_raw_path = run_dir / "grok.research.raw.json"
    wrapper = json.loads(raw_path.read_text(encoding="utf-8"))
    session_id = wrapper.get("sessionId") or wrapper.get("session_id")
    if not session_id:
        raise SystemExit("Grok wrapper has no session ID")
    safe_original = {
        key: value for key, value in wrapper.items()
        if key not in {"thought", "thinking", "reasoning"}
    }
    write_json(research_raw_path, safe_original)

    executable = shutil.which("grok")
    if not executable:
        raise SystemExit("grok executable not found")
    prompt = (
        "Your previous final answer contains the completed independent research, "
        "but its JSON has syntax errors and may have schema-validation omissions. "
        "Preserve the substantive research, source URLs, hierarchy and questions. "
        "Fix JSON syntax and make it conform to the canonical schema already present "
        "in this conversation. Do not perform new research, do not use tools, do not "
        "narrate, and do not emit a code fence. Return exactly one JSON object starting "
        "with {\"schema_version\":\"1.0.0\"}. Replace placeholders with the already "
        "researched substantive values; never delete a node merely to pass validation."
    )
    with tempfile.TemporaryDirectory(prefix="vercy-grok-json-repair-") as temp_name:
        command = [
            executable,
            "--cwd", temp_name,
            "--resume", session_id,
            "-p", prompt,
            "--model", "grok-4.6",
            "--reasoning-effort", "high",
            "--no-memory",
            "--no-subagents",
            "--tools", "",
            "--max-turns", "6",
            "--output-format", "json",
            "--verbatim",
        ]
        completed = subprocess.run(
            command, cwd=temp_name, capture_output=True, text=True,
            encoding="utf-8", errors="replace", timeout=args.timeout,
            env={**os.environ, "PYTHONUTF8": "1"}, check=False,
        )
    if completed.returncode:
        print(completed.stderr[-8000:])
        return completed.returncode
    repaired_wrapper = json.loads(completed.stdout)
    result = extract_result(repaired_wrapper)
    safe_repaired = {
        key: value for key, value in repaired_wrapper.items()
        if key not in {"thought", "thinking", "reasoning"}
    }
    write_json(raw_path, safe_repaired)
    write_json(run_dir / "grok.result.json", result)
    print(run_dir / "grok.result.json")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
