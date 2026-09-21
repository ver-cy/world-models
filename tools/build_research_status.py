#!/usr/bin/env python3
"""Project immutable run manifests into a compact catalogue research status."""

from __future__ import annotations

import csv
import hashlib
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
QUEUE = ROOT / "research" / "queue.csv"
RUNS = ROOT / "research" / "runs"
OUTPUT = ROOT / "research" / "status.csv"

FIELDS = [
    "sequence", "model_id", "name", "claude_status", "grok_status",
    "synthesis_status", "validation_status", "bundles", "layers",
    "findings", "questions", "artifacts", "functions",
]


def read_json(path: Path) -> dict:
    return json.loads(path.read_text(encoding="utf-8")) if path.exists() else {}


def provider_status(run_dir: Path, provider: str, manifest: dict, waived: set) -> str:
    """Keep terminal CLI history while surfacing a separately verified browser memo."""
    browser = read_json(run_dir / f"{provider}-browser.manifest.json")
    memo = run_dir / f"{provider}-browser.review.md"
    if browser.get("status") == "complete" and memo.is_file():
        if hashlib.sha256(memo.read_bytes()).hexdigest() == browser.get("output_sha256"):
            return "complete-browser-memo"
        return "browser-evidence-digest-mismatch"
    return manifest.get("status", "waived" if provider in waived else "queued")


def main() -> int:
    with QUEUE.open(encoding="utf-8-sig", newline="") as handle:
        queue = list(csv.DictReader(handle))
    rows = []
    for item in queue:
        run_dir = RUNS / item["model_id"].casefold()
        claude = read_json(run_dir / "claude.manifest.json")
        grok = read_json(run_dir / "grok.manifest.json")
        adjudication = read_json(run_dir / "adjudication.json")
        run_waived = set(adjudication.get("waived_providers", []))
        synthesis_validation = read_json(run_dir / "synthesis.validation.json")
        counts = synthesis_validation.get("counts", {})
        rows.append({
            "sequence": item["sequence"],
            "model_id": item["model_id"],
            "name": item["name"],
            "claude_status": provider_status(run_dir, "claude", claude, run_waived),
            "grok_status": provider_status(run_dir, "grok", grok, run_waived),
            "synthesis_status": adjudication.get("status", "blocked-on-providers"),
            "validation_status": "valid" if synthesis_validation.get("valid") else "not-valid-or-not-run",
            "bundles": counts.get("bundles", ""),
            "layers": counts.get("layers", ""),
            "findings": counts.get("findings", ""),
            "questions": counts.get("questions", ""),
            "artifacts": counts.get("artifacts", ""),
            "functions": counts.get("functions", ""),
        })
    with OUTPUT.open("w", encoding="utf-8", newline="") as handle:
        writer = csv.DictWriter(handle, fieldnames=FIELDS, lineterminator="\n")
        writer.writeheader()
        writer.writerows(rows)
    print(OUTPUT)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
