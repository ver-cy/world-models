#!/usr/bin/env python3
"""Build the resumable Claude/Grok research queue from the unified registry."""

from __future__ import annotations

import argparse
import csv
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
REGISTRY = ROOT / "planning" / "VERCY-UNIFIED-MEGA-REGISTRY.csv"
TOP_50 = ROOT / "planning" / "VERCY-TOP-50-DELIVERY-SEQUENCE.csv"
OUTPUT = ROOT / "research" / "queue.csv"

FIELDS = [
    "sequence",
    "registry_id",
    "model_id",
    "name",
    "entry_kind",
    "priority_wave",
    "priority_score",
    "review_state",
    "claude_status",
    "grok_status",
    "synthesis_status",
    "validation_status",
]


def load_rows() -> list[dict[str, str]]:
    with TOP_50.open(encoding="utf-8-sig", newline="") as handle:
        top_order = {
            row["model_id"]: int(row["sequence"])
            for row in csv.DictReader(handle)
        }

    with REGISTRY.open(encoding="utf-8-sig", newline="") as handle:
        models = [
            row for row in csv.DictReader(handle)
            if row["record_plane"] == "world-model"
        ]

    def sort_key(row: dict[str, str]) -> tuple[int, int, float, str]:
        model_id = row["model_id"]
        if model_id in top_order:
            return (0, top_order[model_id], 0, model_id)
        return (
            1,
            int(row["priority_wave"] or 99),
            -float(row["priority_score"] or 0),
            model_id,
        )

    models.sort(key=sort_key)
    result = []
    for sequence, row in enumerate(models, 1):
        result.append({
            "sequence": str(sequence),
            "registry_id": row["registry_id"],
            "model_id": row["model_id"],
            "name": row["name"],
            "entry_kind": row["entry_kind"],
            "priority_wave": row["priority_wave"],
            "priority_score": row["priority_score"],
            "review_state": row["review_state"],
            "claude_status": "queued",
            "grok_status": "queued",
            "synthesis_status": "blocked-on-providers",
            "validation_status": "not-run",
        })
    return result


def render(rows: list[dict[str, str]]) -> str:
    import io

    buffer = io.StringIO(newline="")
    writer = csv.DictWriter(buffer, fieldnames=FIELDS, lineterminator="\n")
    writer.writeheader()
    writer.writerows(rows)
    return buffer.getvalue()


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--check", action="store_true")
    args = parser.parse_args()

    expected = render(load_rows())
    if args.check:
        if not OUTPUT.exists() or OUTPUT.read_text(encoding="utf-8") != expected:
            print(f"research queue is stale: {OUTPUT}")
            return 1
        print(f"research queue is current: {len(load_rows())} models")
        return 0

    OUTPUT.parent.mkdir(parents=True, exist_ok=True)
    OUTPUT.write_text(expected, encoding="utf-8", newline="")
    print(f"wrote {len(load_rows())} models to {OUTPUT}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
