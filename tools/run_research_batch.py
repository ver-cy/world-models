#!/usr/bin/env python3
"""Run a small resumable provider batch in dependency order."""

from __future__ import annotations

import argparse
import csv
import json
import subprocess
import sys
from concurrent.futures import ThreadPoolExecutor
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
QUEUE = ROOT / "research" / "queue.csv"
RUNNER = ROOT / "tools" / "run_model_research.py"
COMPARE = ROOT / "tools" / "compare_model_research.py"
REPAIR_GROK = ROOT / "tools" / "repair_grok_research_json.py"
NORMALIZE = ROOT / "tools" / "normalize_model_research_response.py"


def run_provider(model_id: str, provider: str, timeout: int) -> int:
    command = [
        sys.executable, str(RUNNER), "--provider", provider,
        "--model-id", model_id, "--timeout", str(timeout),
    ]
    result = subprocess.run(command, cwd=ROOT, check=False)
    if result.returncode and provider == "grok":
        raw_path = ROOT / "research" / "runs" / model_id.casefold() / "grok.raw.json"
        if raw_path.exists():
            raw_wrapper = json.loads(raw_path.read_text(encoding="utf-8"))
            raw_text = raw_wrapper.get("text") or ""
            if '{"schema_version"' not in raw_text and '{ "schema_version"' not in raw_text:
                # A cancelled Grok turn may contain useful search progress but no
                # answer to repair. Retry the independent run once from its frozen
                # prompt instead of asking a repair turn to invent missing output.
                result = subprocess.run(command + ["--force"], cwd=ROOT, check=False)
                if result.returncode == 0:
                    return 0
                raw_wrapper = json.loads(raw_path.read_text(encoding="utf-8"))
                raw_text = raw_wrapper.get("text") or ""
            if '{"schema_version"' not in raw_text and '{ "schema_version"' not in raw_text:
                return result.returncode
            repaired = subprocess.run([
                sys.executable, str(REPAIR_GROK), "--model-id", model_id,
                "--timeout", str(min(timeout, 1800)),
            ], cwd=ROOT, check=False)
            if repaired.returncode == 0:
                normalized = subprocess.run([
                    sys.executable, str(NORMALIZE), "--provider", "grok",
                    "--model-id", model_id,
                ], cwd=ROOT, check=False)
                return normalized.returncode
    return result.returncode


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--start-sequence", type=int, default=1)
    parser.add_argument("--limit", type=int, default=1)
    parser.add_argument("--providers", default="claude,grok")
    parser.add_argument("--timeout", type=int, default=3600)
    parser.add_argument("--continue-on-error", action="store_true")
    args = parser.parse_args()
    providers = [item.strip() for item in args.providers.split(",") if item.strip()]
    if not providers or any(item not in {"claude", "grok"} for item in providers):
        raise SystemExit("--providers must contain claude and/or grok")

    with QUEUE.open(encoding="utf-8-sig", newline="") as handle:
        rows = [
            row for row in csv.DictReader(handle)
            if int(row["sequence"]) >= args.start_sequence
        ][:args.limit]

    failed = False
    for row in rows:
        model_id = row["model_id"]
        print(f"[{row['sequence']}] {model_id} {row['name']}", flush=True)
        with ThreadPoolExecutor(max_workers=len(providers)) as executor:
            return_codes = list(executor.map(
                lambda provider: run_provider(model_id, provider, args.timeout),
                providers,
            ))
        if any(return_codes):
            failed = True
            if not args.continue_on_error:
                return 1
            continue
        if set(providers) == {"claude", "grok"}:
            compared = subprocess.run([
                sys.executable, str(COMPARE), "--model-id", model_id,
            ], cwd=ROOT, check=False)
            if compared.returncode:
                failed = True
                if not args.continue_on_error:
                    return 1
    return 1 if failed else 0


if __name__ == "__main__":
    raise SystemExit(main())
