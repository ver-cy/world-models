#!/usr/bin/env python3
"""Build a resumable claim-level source verification queue for one synthesis."""

from __future__ import annotations

import argparse
import csv
import json
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
FIELDS = [
    "source_id", "title", "organization", "url", "version_or_date",
    "used_by_claude", "used_by_grok", "accepted_in_synthesis",
    "live_status", "version_status", "claim_support_status", "notes",
]


def urls(path: Path) -> set[str]:
    if not path.exists():
        return set()
    data = json.loads(path.read_text(encoding="utf-8"))
    return {source["url"] for source in data["sources"]}


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--model-id", required=True)
    parser.add_argument("--run-root", type=Path, default=ROOT / "research" / "runs")
    args = parser.parse_args()
    run_dir = args.run_root / args.model_id.casefold()
    synthesis_path = run_dir / "synthesis.result.json"
    synthesis = json.loads(synthesis_path.read_text(encoding="utf-8"))
    output = run_dir / "source-verification.csv"
    prior = {}
    if output.exists():
        with output.open(encoding="utf-8-sig", newline="") as handle:
            prior = {row["url"]: row for row in csv.DictReader(handle)}
    claude_urls = urls(run_dir / "claude.result.json")
    grok_urls = urls(run_dir / "grok.result.json")
    rows = []
    for source in synthesis["sources"]:
        previous = prior.get(source["url"], {})
        rows.append({
            "source_id": source["id"],
            "title": source["title"],
            "organization": source["organization"],
            "url": source["url"],
            "version_or_date": source["version_or_date"],
            "used_by_claude": str(source["url"] in claude_urls).lower(),
            "used_by_grok": str(source["url"] in grok_urls).lower(),
            "accepted_in_synthesis": "true",
            "live_status": previous.get("live_status", "unverified"),
            "version_status": previous.get("version_status", "unverified"),
            "claim_support_status": previous.get("claim_support_status", "unverified"),
            "notes": previous.get("notes", ""),
        })
    with output.open("w", encoding="utf-8", newline="") as handle:
        writer = csv.DictWriter(handle, fieldnames=FIELDS, lineterminator="\n")
        writer.writeheader()
        writer.writerows(rows)
    print(output)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
