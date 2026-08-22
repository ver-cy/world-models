#!/usr/bin/env python3
"""Project immutable run manifests into a compact catalogue research status."""

from __future__ import annotations

import csv
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


def main() -> int:
    with QUEUE.open(encoding="utf-8-sig", newline="") as handle:
        queue = list(csv.DictReader(handle))
    rows = []
    for item in queue:
        run_dir = RUNS / item["model_id"].casefold()
        claude = read_json(run_dir / "claude.manifest.json")
        grok = read_json(run_dir / "grok.manifest.json")
        adjudication = read_json(run_dir / "adjudication.json")
        synthesis_validation = read_json(run_dir / "synthesis.validation.json")
        counts = synthesis_validation.get("counts", {})
        rows.append({
            "sequence": item["sequence"],
            "model_id": item["model_id"],
            "name": item["name"],
            "claude_status": claude.get("status", "queued"),
            "grok_status": grok.get("status", "queued"),
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
