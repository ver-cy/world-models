#!/usr/bin/env python3
"""Ask the originating Grok session to repair JSON syntax without new research."""

from __future__ import annotations

import argparse
import hashlib
import json
import os
import shutil
import subprocess
import tempfile
from pathlib import Path

from run_model_research import (
    CLAUDE_LOCAL_SETTINGS,
    ROOT,
    SCHEMA_PATH,
    extract_result,
    hide_claude_local_settings,
    write_json,
)


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--model-id", required=True)
    parser.add_argument("--run-root", type=Path, default=ROOT / "research" / "runs")
    parser.add_argument("--provider-model", default="grok-4.6")
    parser.add_argument("--timeout", type=int, default=1800)
    args = parser.parse_args()
    run_dir = args.run_root / args.model_id.casefold()
    raw_path = run_dir / "grok.raw.json"
    research_raw_path = run_dir / "grok.research.raw.json"
    source_path = research_raw_path if research_raw_path.exists() else raw_path
    wrapper = json.loads(source_path.read_text(encoding="utf-8"))
    session_id = wrapper.get("sessionId") or wrapper.get("session_id")
    if not session_id:
        raise SystemExit("Grok wrapper has no session ID")
    safe_original = {
        key: value for key, value in wrapper.items()
        if key not in {"thought", "thinking", "reasoning"}
    }
    if not research_raw_path.exists():
        write_json(research_raw_path, safe_original)
    schema_text = SCHEMA_PATH.read_text(encoding="utf-8")

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
        temporary_cwd = Path(temp_name)
        command = [
            executable,
            "--cwd", temp_name,
            "--resume", session_id,
            "-p", prompt,
            "--model", args.provider_model,
            "--reasoning-effort", "high",
            "--no-memory",
            "--no-subagents",
            "--tools", "",
            "--max-turns", "6",
            "--output-format", "json",
            "--json-schema", schema_text,
            "--verbatim",
        ]
        environment = os.environ.copy()
        environment["PYTHONUTF8"] = "1"
        isolated_home = temporary_cwd / "home"
        isolated_home.mkdir(parents=True, exist_ok=True)
        environment["HOME"] = str(isolated_home)
        environment["USERPROFILE"] = str(isolated_home)
        environment["CLAUDE_CONFIG_DIR"] = str(isolated_home / ".claude")
        environment["XDG_CONFIG_HOME"] = str(isolated_home / ".config")
        environment["GROK_HOME"] = str(Path.home() / ".grok")
        try:
            with hide_claude_local_settings(True):
                completed = subprocess.run(
                    command, cwd=temporary_cwd, capture_output=True, text=True,
                    encoding="utf-8", errors="replace", timeout=args.timeout,
                    env=environment, check=False,
                )
        except subprocess.TimeoutExpired:
            print(f"repair timed out after {args.timeout}s; provider output suppressed")
            return 2
    unsafe_stderr = any(marker in completed.stderr.casefold() for marker in (
        str(CLAUDE_LOCAL_SETTINGS).casefold(),
        "settings.local.json",
        "allow.*password",
        "allow.*token",
        "allow.*secret",
    ))
    if unsafe_stderr:
        stderr_hash = hashlib.sha256(completed.stderr.encode("utf-8")).hexdigest()
        print(f"repair stderr referenced local settings; suppressed sha256={stderr_hash}")
        return 2
    if completed.returncode:
        stderr_hash = hashlib.sha256(completed.stderr.encode("utf-8")).hexdigest()
        print(
            f"repair failed with code {completed.returncode}; "
            f"provider stderr suppressed sha256={stderr_hash}"
        )
        return completed.returncode
    try:
        repaired_wrapper = json.loads(completed.stdout)
    except json.JSONDecodeError:
        stdout_hash = hashlib.sha256(completed.stdout.encode("utf-8")).hexdigest()
        print(f"repair returned a non-JSON wrapper; suppressed sha256={stdout_hash}")
        return 2
    try:
        result = extract_result(repaired_wrapper)
    except ValueError as error:
        print(str(error))
        return 2
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
