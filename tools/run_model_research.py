#!/usr/bin/env python3
"""Run one isolated Claude or Grok research pass and checkpoint the result."""

from __future__ import annotations

import argparse
from contextlib import contextmanager
import csv
import hashlib
import json
import os
import re
import shutil
import subprocess
import tempfile
from datetime import datetime, timezone
from pathlib import Path
from typing import Any

from validate_model_research import validate


ROOT = Path(__file__).resolve().parents[1]
REGISTRY = ROOT / "planning" / "VERCY-UNIFIED-MEGA-REGISTRY.csv"
RELATIONS = ROOT / "planning" / "VERCY-MODEL-RELATIONS.csv"
PROMPT_TEMPLATE = ROOT / "research" / "MODEL-RESEARCH-PROMPT.md"
SCHEMA_PATH = ROOT / "research" / "model-research.schema.json"
CLAUDE_LOCAL_SETTINGS = Path.home() / ".claude" / "settings.local.json"

PROVIDER_FOCUS = {
    "claude": (
        "Take the conservative standards-led role. Stress-test model boundaries, "
        "distinguish normative requirements from common practice, search for "
        "counterexamples and reject attractive but unsupported structure. Keep "
        "the complete JSON under 52,000 output tokens: target 5-7 bundles, 10-16 "
        "layers and 20-28 well-bounded findings with 3-5 discriminating questions "
        "each; use concise descriptions and never pad the result with repetition."
    ),
    "grok": (
        "Take the wide-union omission-hunter role. Search across jurisdictions, "
        "industries and technical ecosystems; surface rare lifecycle cases and "
        "emerging standards, while marking anything that lacks primary support. "
        "The complete local context and schema are already in this prompt: do not "
        "read the prompt file or list the working directory. To stay within the "
        "research context budget, make no more than 10 focused web searches and "
        "12 web fetches total, with at most four tool calls in any one turn. Prefer "
        "one authoritative source that covers several claims over many duplicates."
    ),
}


def now() -> str:
    return datetime.now(timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ")


def load_registry_row(model_id: str) -> dict[str, str]:
    with REGISTRY.open(encoding="utf-8-sig", newline="") as handle:
        for row in csv.DictReader(handle):
            if row["record_plane"] == "world-model" and row["model_id"] == model_id:
                return row
    raise SystemExit(f"unknown world model: {model_id}")


def load_relations(model_id: str) -> list[dict[str, str]]:
    if not RELATIONS.exists():
        return []
    with RELATIONS.open(encoding="utf-8-sig", newline="") as handle:
        return [
            row for row in csv.DictReader(handle)
            if row["source_model_id"] == model_id or row["target_model_id"] == model_id
        ]


def legacy_excerpt(row: dict[str, str], max_chars: int = 80_000) -> str:
    reference = row.get("existing_spec_ref", "").strip()
    if not reference:
        return "No previous-version material is registered."
    candidate = (ROOT / reference).resolve()
    try:
        candidate.relative_to(ROOT)
    except ValueError:
        return f"Registered legacy path is outside the repository and was not read: {reference}"
    if not candidate.is_file():
        return f"Registered legacy path was not found: {reference}"
    text = candidate.read_text(encoding="utf-8", errors="replace")
    if len(text) > max_chars:
        text = text[:max_chars] + "\n[excerpt truncated by runner]"
    return text


def render_prompt(provider: str, row: dict[str, str]) -> str:
    template = PROMPT_TEMPLATE.read_text(encoding="utf-8")
    rendered = (
        template
        .replace("{{PROVIDER_FOCUS}}", PROVIDER_FOCUS[provider])
        .replace("{{REGISTRY_RECORD}}", json.dumps(row, ensure_ascii=False, indent=2))
        .replace("{{RELATIONS}}", json.dumps(load_relations(row["model_id"]), ensure_ascii=False, indent=2))
        .replace("{{LEGACY_EXCERPT}}", legacy_excerpt(row))
    )
    if provider == "grok":
        rendered += (
            "\n\n## Canonical validation schema\n\n"
            "The transport constraint is intentionally shallow. Your actual output "
            "must satisfy this complete schema and will be validated after the run.\n\n"
            "```json\n"
            + SCHEMA_PATH.read_text(encoding="utf-8")
            + "\n```\n"
        )
    return rendered


def git_commit() -> str:
    result = subprocess.run(
        ["git", "rev-parse", "HEAD"], cwd=ROOT, capture_output=True,
        text=True, encoding="utf-8", errors="replace", check=False,
    )
    return result.stdout.strip() if result.returncode == 0 else "unknown"


def git_is_dirty() -> bool:
    result = subprocess.run(
        ["git", "status", "--porcelain"], cwd=ROOT, capture_output=True,
        text=True, encoding="utf-8", errors="replace", check=False,
    )
    return result.returncode != 0 or bool(result.stdout.strip())


@contextmanager
def hide_claude_local_settings(enabled: bool):
    """Keep Grok from importing Claude permission entries and their secrets.

    Grok 1.0 discovers the Windows user's Claude local settings even when HOME,
    USERPROFILE and CLAUDE_CONFIG_DIR point elsewhere.  Rename the one local
    settings file on the same volume for the duration of a Grok subprocess and
    restore it in a finally block.  Provider runs are deliberately sequential.
    """
    if not enabled or not CLAUDE_LOCAL_SETTINGS.is_file():
        yield
        return
    holding = CLAUDE_LOCAL_SETTINGS.with_name(CLAUDE_LOCAL_SETTINGS.name + ".vercy-grok-hold")
    if holding.exists():
        raise RuntimeError(f"Grok settings holding path already exists: {holding}")
    before = hashlib.sha256(CLAUDE_LOCAL_SETTINGS.read_bytes()).hexdigest()
    CLAUDE_LOCAL_SETTINGS.replace(holding)
    try:
        yield
    finally:
        if holding.exists():
            holding.replace(CLAUDE_LOCAL_SETTINGS)
        if not CLAUDE_LOCAL_SETTINGS.is_file():
            raise RuntimeError("Claude local settings were not restored after Grok")
        after = hashlib.sha256(CLAUDE_LOCAL_SETTINGS.read_bytes()).hexdigest()
        if before != after:
            raise RuntimeError("Claude local settings changed during Grok isolation")


def build_command(provider: str, provider_model: str, schema: str, prompt_path: Path, temporary_cwd: Path) -> list[str]:
    if provider == "claude":
        executable = shutil.which("claude")
        if not executable:
            raise SystemExit("claude executable not found")
        return [
            executable,
            "-p",
            "--model", provider_model,
            "--effort", "max",
            "--permission-mode", "dontAsk",
            "--tools", "WebSearch,WebFetch",
            "--allowedTools", "WebSearch,WebFetch",
            "--disallowedTools", "Bash,Write,Edit,NotebookEdit,Read,Glob,Grep",
            "--no-session-persistence",
            "--output-format", "json",
            "--json-schema", schema,
        ]
    executable = shutil.which("grok")
    if not executable:
        raise SystemExit("grok executable not found")
    return [
        executable,
        "--cwd", str(temporary_cwd),
        "--prompt-file", str(prompt_path),
        "--model", provider_model,
        "--reasoning-effort", "high",
        "--no-memory",
        "--no-subagents",
        "--tools", "web_search,web_fetch",
        "--allow", "WebSearch(*)",
        "--allow", "WebFetch(*)",
        "--deny", "MCPTool(*)",
        "--max-turns", "100",
        "--output-format", "json",
    ]


def parse_json_text(value: Any) -> dict[str, Any] | None:
    if isinstance(value, dict):
        return value
    if not isinstance(value, str):
        return None
    text = value.strip()
    if text.startswith("```json") and text.endswith("```"):
        text = text[7:-3].strip()
    try:
        parsed = json.loads(text)
    except json.JSONDecodeError:
        # Headless Grok may prepend concise tool-progress narration before its
        # final JSON object. Extract only a complete schema-rooted object; never
        # guess from an arbitrary brace in prose.
        decoder = json.JSONDecoder()
        for marker in ('{"schema_version"', '{ "schema_version"'):
            start = text.find(marker)
            if start < 0:
                continue
            try:
                parsed, _ = decoder.raw_decode(text, start)
            except json.JSONDecodeError:
                continue
            if isinstance(parsed, dict):
                return parsed
        return None
    return parsed if isinstance(parsed, dict) else None


def extract_result(wrapper: dict[str, Any]) -> dict[str, Any]:
    if wrapper.get("schema_version") == "1.0.0":
        return wrapper
    for key in ("structured_output", "structuredOutput", "output", "text", "result", "response"):
        candidate = parse_json_text(wrapper.get(key))
        if candidate and candidate.get("schema_version") == "1.0.0":
            return candidate
    raise ValueError("provider response did not contain a schema_version=1.0.0 result")


def write_json(path: Path, value: Any) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(json.dumps(value, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--provider", required=True, choices=sorted(PROVIDER_FOCUS))
    parser.add_argument("--provider-model")
    parser.add_argument("--model-id", required=True)
    parser.add_argument("--output-root", type=Path, default=ROOT / "research" / "runs")
    parser.add_argument(
        "--run-label",
        help="Store an isolated split pass under <model>/parts/<label>.",
    )
    parser.add_argument(
        "--focus-file",
        type=Path,
        help="Append a bounded split-pass scope that overrides the normal size targets.",
    )
    parser.add_argument("--prompt-only", action="store_true")
    parser.add_argument("--force", action="store_true")
    parser.add_argument("--timeout", type=int, default=3600)
    args = parser.parse_args()
    if args.run_label and not re.fullmatch(r"[a-z0-9][a-z0-9-]{0,63}", args.run_label):
        parser.error("--run-label must match [a-z0-9][a-z0-9-]{0,63}")
    if args.focus_file and not args.focus_file.is_file():
        parser.error(f"--focus-file does not exist: {args.focus_file}")
    provider_model = args.provider_model or ("opus" if args.provider == "claude" else "grok-4.6")

    row = load_registry_row(args.model_id)
    run_dir = args.output_root / args.model_id.casefold()
    if args.run_label:
        run_dir = run_dir / "parts" / args.run_label
    prompt_path = run_dir / f"{args.provider}.prompt.md"
    raw_path = run_dir / f"{args.provider}.raw.json"
    result_path = run_dir / f"{args.provider}.result.json"
    validation_path = run_dir / f"{args.provider}.validation.json"
    manifest_path = run_dir / f"{args.provider}.manifest.json"
    run_dir.mkdir(parents=True, exist_ok=True)
    if result_path.exists() and not args.force and not args.prompt_only:
        print(f"result already exists; use --force to replace: {result_path}")
        return 0
    if args.force and not args.prompt_only:
        # A failed replacement must never leave an older provider result beside
        # a newer parse-error/timeout manifest: downstream comparison would
        # otherwise consume stale evidence as if the current run had passed.
        for stale_path in (result_path, validation_path, run_dir / f"{args.provider}.raw.txt"):
            stale_path.unlink(missing_ok=True)
    prompt = render_prompt(args.provider, row)
    focus_text = None
    if args.focus_file:
        focus_text = args.focus_file.read_text(encoding="utf-8")
        prompt += (
            "\n\n## Bounded split-pass override\n\n"
            "This is one deliberately bounded part of a larger provider pass. "
            "The instructions below supersede the normal bundle/layer/finding "
            "quantity targets, but not the canonical JSON contract, evidence "
            "quality rules, or local validation requirements. Return only the "
            "assigned subject structure and do not duplicate adjacent split "
            "areas. The result must still be a complete schema-valid object.\n\n"
            + focus_text.strip()
            + "\n"
        )
    prompt_path.write_text(prompt, encoding="utf-8")

    if args.prompt_only:
        print(prompt_path)
        return 0

    schema_data = json.loads(SCHEMA_PATH.read_text(encoding="utf-8"))
    # Claude's structured-output transport currently rejects the 2020-12 meta
    # schema URI even though the canonical Vercy validator uses that dialect.
    # Removing only the dialect declaration keeps the same constraints and lets
    # Claude's bundled validator consume the schema as its default dialect.
    if args.provider == "claude":
        schema_data.pop("$schema", None)
    # Grok 1.0's constrained decoder repeats placeholder envelopes even with a
    # shallow schema. The complete canonical schema stays in the prompt and the
    # returned object is validated locally; do not pass --json-schema to Grok.
    schema_text = json.dumps(schema_data, separators=(",", ":"))
    started_at = now()
    manifest: dict[str, Any] = {
        "contract_version": "1.0.0",
        "provider": args.provider,
        "provider_model": provider_model,
        "model_id": args.model_id,
        "registry_id": row["registry_id"],
        "input_commit": git_commit(),
        "input_worktree_dirty": git_is_dirty(),
        "prompt_sha256": hashlib.sha256(prompt.encode("utf-8")).hexdigest(),
        "run_label": args.run_label,
        "focus_sha256": (
            hashlib.sha256(focus_text.encode("utf-8")).hexdigest()
            if focus_text is not None else None
        ),
        "schema_sha256": hashlib.sha256(SCHEMA_PATH.read_bytes()).hexdigest(),
        "started_at": started_at,
        "completed_at": None,
        "web_tools_requested": True,
        "status": "running",
    }
    write_json(manifest_path, manifest)

    with tempfile.TemporaryDirectory(prefix="vercy-model-research-") as temp_name:
        temporary_cwd = Path(temp_name)
        temporary_prompt = temporary_cwd / "prompt.md"
        temporary_prompt.write_text(prompt, encoding="utf-8")
        command = build_command(args.provider, provider_model, schema_text, temporary_prompt, temporary_cwd)
        environment = os.environ.copy()
        environment["PYTHONUTF8"] = "1"
        if args.provider == "grok":
            isolated_home = str(temporary_cwd / "home")
            Path(isolated_home).mkdir(parents=True, exist_ok=True)
            environment["HOME"] = isolated_home
            environment["USERPROFILE"] = isolated_home
            environment["CLAUDE_CONFIG_DIR"] = str(Path(isolated_home) / ".claude")
            environment["XDG_CONFIG_HOME"] = str(Path(isolated_home) / ".config")
            environment["GROK_HOME"] = str(Path.home() / ".grok")
        try:
            with hide_claude_local_settings(args.provider == "grok"):
                completed = subprocess.run(
                    command,
                    cwd=temporary_cwd,
                    input=prompt if args.provider == "claude" else None,
                    capture_output=True,
                    text=True,
                    encoding="utf-8",
                    errors="replace",
                    timeout=args.timeout,
                    env=environment,
                    check=False,
                )
        except subprocess.TimeoutExpired as error:
            manifest.update({"completed_at": now(), "status": "timeout", "error": str(error)})
            write_json(manifest_path, manifest)
            print(f"provider timed out after {args.timeout}s")
            return 2

    manifest["completed_at"] = now()
    manifest["return_code"] = completed.returncode
    unsafe_stderr = any(marker in completed.stderr.casefold() for marker in (
        str(CLAUDE_LOCAL_SETTINGS).casefold(),
        "settings.local.json",
        "allow.*password",
        "allow.*token",
        "allow.*secret",
    ))
    if args.provider == "grok" and unsafe_stderr:
        manifest.update({
            "status": "unsafe-config",
            "stderr_sha256": hashlib.sha256(completed.stderr.encode("utf-8")).hexdigest(),
            "error": "Grok referenced Claude local settings; output was suppressed",
        })
        write_json(manifest_path, manifest)
        print(manifest["error"])
        return 2
    if completed.returncode != 0:
        manifest.update({
            "status": "provider-error",
            "stderr_sha256": hashlib.sha256(completed.stderr.encode("utf-8")).hexdigest(),
            "stderr_bytes": len(completed.stderr.encode("utf-8")),
            "stdout_sha256": hashlib.sha256(completed.stdout.encode("utf-8")).hexdigest(),
            "stdout_bytes": len(completed.stdout.encode("utf-8")),
        })
        # Headless providers can return a JSON diagnostic wrapper on stdout with
        # a non-zero process code. Preserve that safe wrapper (minus reasoning)
        # outside the canonical result path so failures remain diagnosable.
        if completed.stdout.strip():
            try:
                error_wrapper = json.loads(completed.stdout)
            except json.JSONDecodeError:
                error_wrapper = None
            if isinstance(error_wrapper, dict):
                safe_error_wrapper = {
                    key: value for key, value in error_wrapper.items()
                    if key not in {"thought", "thinking", "reasoning"}
                }
                write_json(run_dir / f"{args.provider}.error.raw.json", safe_error_wrapper)
        write_json(manifest_path, manifest)
        print("provider failed; stderr was suppressed and only its hash was recorded")
        return completed.returncode or 2

    try:
        wrapper = json.loads(completed.stdout)
    except json.JSONDecodeError as error:
        fallback = run_dir / f"{args.provider}.raw.txt"
        fallback.write_text(completed.stdout, encoding="utf-8")
        manifest.update({"status": "parse-error", "error": str(error)})
        write_json(manifest_path, manifest)
        print(str(error))
        return 2
    safe_wrapper = {
        key: value for key, value in wrapper.items()
        if key not in {"thought", "thinking", "reasoning"}
    }
    write_json(raw_path, safe_wrapper)
    session_id = wrapper.get("session_id") or wrapper.get("sessionId")
    if session_id:
        manifest["session_id"] = session_id
    stop_reason = wrapper.get("stop_reason") or wrapper.get("stopReason")
    if stop_reason:
        manifest["stop_reason"] = stop_reason
    try:
        result = extract_result(wrapper)
    except ValueError as error:
        manifest.update({"status": "parse-error", "error": str(error)})
        write_json(manifest_path, manifest)
        print(str(error))
        return 2

    write_json(result_path, result)
    report = validate(result, args.model_id)
    write_json(validation_path, report)
    manifest.update({
        "status": "complete" if report["valid"] else "validation-failed",
        "result_sha256": hashlib.sha256(result_path.read_bytes()).hexdigest(),
        "validation": report,
    })
    write_json(manifest_path, manifest)
    print(json.dumps({"result": str(result_path), **report}, ensure_ascii=False, indent=2))
    return 0 if report["valid"] else 1


if __name__ == "__main__":
    raise SystemExit(main())
