#!/usr/bin/env python3
"""Expose Enterprise programme contours in the public model catalogue.

The catalogue distinguishes programme contour cards from independently released
model specifications. No runtime/model identifier is allocated by this script.
"""

import argparse
import json
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
REGISTRY = ROOT / "research/enterprise/registry.json"
QUEUE = ROOT / "research/enterprise/queue.json"
ENGLISH = ROOT / "research/enterprise/i18n/units.en.json"


def read_json(path: Path):
    return json.loads(path.read_text(encoding="utf-8-sig"))


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--site-root", type=Path, required=True)
    parser.add_argument("--check", action="store_true")
    args = parser.parse_args()

    registry = read_json(REGISTRY)
    queue = read_json(QUEUE)
    english = read_json(ENGLISH) if ENGLISH.is_file() else {}
    catalogue_path = args.site_root / "models/catalog-index.json"
    catalogue = read_json(catalogue_path)
    queue_by_id = {unit["id"]: unit for unit in queue["units"]}
    contour_ids = {unit["id"] for unit in registry["units"]}

    # Independently released specifications keep their cards, but use a family
    # label that does not conflate them with the 111 programme contours.
    preserved = []
    for entry in catalogue:
        if entry.get("id") in contour_ids:
            continue
        entry = dict(entry)
        if entry.get("family") == "Enterprise profiles":
            entry["family"] = "Enterprise releases"
        preserved.append(entry)

    cards = []
    for unit in registry["units"]:
        contour = unit["id"]
        progress = queue_by_id[contour]
        translation = english.get(contour, {})
        exports = unit.get("candidate_types") or unit.get("exports") or []
        name = translation.get("name") or " / ".join(exports[:2]) or contour
        immutable = progress.get("status") == "published"
        cards.append({
            "id": contour,
            "name": name,
            "version": "0.1.0" if immutable else "research-checkpoint",
            "family": "Enterprise profiles",
            "category": f"Enterprise {unit.get('kind', 'profile')}",
            "industry": ["Cross-industry"],
            "domain": ["Enterprise", unit.get("domain", "Cross-domain")],
            "tags": [contour, unit.get("wave", ""), unit.get("kind", "profile"), *exports[:5]],
            "url": f"/enterprise/models/{contour.lower()}/",
            "status": "immutable release" if immutable else "published partial research",
            "sourceUrl": (progress.get("publication_urls") or [f"https://ver.cy/enterprise/models/{contour.lower()}/"])[0],
            "canonical": immutable,
            "installable": immutable,
        })

    output = preserved + cards
    enterprise_profiles = [item for item in output if item.get("family") == "Enterprise profiles"]
    enterprise_releases = [item for item in output if item.get("family") == "Enterprise releases"]
    if len(cards) != 111 or len(enterprise_profiles) != 111:
        raise SystemExit(f"expected 111 Enterprise contour cards, got {len(enterprise_profiles)}")
    if len({item["id"] for item in output}) != len(output):
        raise SystemExit("catalogue IDs are not unique")

    if args.check:
        current = read_json(catalogue_path)
        if current != output:
            raise SystemExit("catalogue discoverability projection is stale")
    else:
        catalogue_path.write_text(
            json.dumps(output, ensure_ascii=False, indent=2) + "\n",
            encoding="utf-8",
        )

    print(json.dumps({
        "catalogueEntries": len(output),
        "enterpriseProfiles": len(enterprise_profiles),
        "enterpriseReleases": len(enterprise_releases),
        "immutableContours": sum(1 for item in cards if item["canonical"]),
        "partialResearchContours": sum(1 for item in cards if not item["canonical"]),
    }))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
