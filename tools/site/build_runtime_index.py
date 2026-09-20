#!/usr/bin/env python3
"""Build the fail-closed runtime model index used by the Vercy Skill."""

from __future__ import annotations

import hashlib
import json
from datetime import datetime, timezone
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
MODELS = ROOT / "models"
BASE = "https://ver.cy"


def absolute(value: str) -> str:
    if not value:
        return ""
    return value if value.startswith(("https://", "http://")) else BASE + "/" + value.lstrip("/")


def sha256(path: Path) -> str | None:
    return "sha256:" + hashlib.sha256(path.read_bytes()).hexdigest() if path.is_file() else None


def slug_from_url(value: str) -> str:
    parts = [part for part in value.split("?")[0].split("/") if part]
    return parts[-1] if parts else ""


def main() -> None:
    source = json.loads((ROOT / "tools" / "server" / "vercy-catalog-import.json").read_text(encoding="utf-8"))
    catalogue = json.loads((MODELS / "catalog-index.json").read_text(encoding="utf-8"))
    composer = json.loads((MODELS / "composer-index.json").read_text(encoding="utf-8"))

    old_id_to_slug = {item["id"]: slug_from_url(item.get("url", "")) for item in catalogue}
    rows = source["models"]
    registry_by_slug = {slug_from_url(row.get("page_url", "")): row["registry_id"] for row in rows}
    requires_by_registry: dict[str, set[str]] = {}
    unresolved_by_registry: dict[str, list[str]] = {}
    for old in composer.get("models", []):
        source_id = registry_by_slug.get(slug_from_url(old.get("pageUrl", "")))
        if not source_id:
            continue
        for ref in old.get("references", []):
            old_target = ref.get("resolvesTo")
            target = registry_by_slug.get(old_id_to_slug.get(old_target, "")) if old_target else None
            if target:
                requires_by_registry.setdefault(source_id, set()).add(target)
            else:
                unresolved_by_registry.setdefault(source_id, []).append(ref.get("csn") or ref.get("code") or "unknown")

    registered_ids = {row["registry_id"] for row in rows}
    entries = []
    for row in rows:
        slug = row["code"]
        page_slug = slug_from_url(row.get("page_url", "")) or slug
        spec_path = MODELS / page_slug / "spec.yaml"
        agents_path = MODELS / page_slug / "AGENTS.md"
        publication_path = MODELS / page_slug / "publication.json"
        if publication_path.is_file():
            publication = json.loads(publication_path.read_text(encoding="utf-8"))
            if "runtime_requires" in publication:
                declared = publication["runtime_requires"]
                if not isinstance(declared, list) or any(not isinstance(item, str) or not item for item in declared):
                    raise ValueError(f"invalid runtime_requires for {row['registry_id']}")
                spec_text = spec_path.read_text(encoding="utf-8")
                if spec_text.startswith("#"):
                    spec_text = spec_text.split("\n", 1)[1]
                spec = json.loads(spec_text)
                expected = {item["target"] for item in spec.get("composition", []) if item.get("required")}
                if set(declared) != expected:
                    raise ValueError(f"publication/spec dependency mismatch for {row['registry_id']}")
                for required in declared:
                    if required in registered_ids:
                        requires_by_registry.setdefault(row["registry_id"], set()).add(required)
                    else:
                        unresolved_by_registry.setdefault(row["registry_id"], []).append(required)
        status = str(row.get("status", "")).lower()
        unresolved = sorted(set(unresolved_by_registry.get(row["registry_id"], [])))
        entry = {
            "id": row["registry_id"],
            "modelId": row.get("model_id"),
            "aliases": sorted(set((row.get("alternate_names") or []) + (row.get("legacy_alias") or []))),
            "slug": page_slug,
            "name": row["name"],
            "version": row.get("version") or "unversioned",
            "status": status,
            "installable": bool(status == "published" and row.get("spec_available") and spec_path.is_file() and agents_path.is_file() and not unresolved),
            "specUrl": absolute(row.get("spec_url") or f"/models/{page_slug}/spec.yaml"),
            "agentsUrl": absolute(row.get("agents_url") or f"/models/{page_slug}/AGENTS.md"),
            "pageUrl": absolute(row.get("page_url") or f"/models/{page_slug}/"),
            "digest": sha256(spec_path),
            "family": row.get("family"),
            "category": row.get("category"),
            "domain": row.get("domain") or [],
            "industry": row.get("industry") or [],
            "tags": row.get("tags") or [],
            "purpose": row.get("purpose") or "",
            "requires": sorted(requires_by_registry.get(row["registry_id"], set())),
            "unresolvedRequires": unresolved,
            "relations": (
                [{"type": "parent", "target": item} for item in row.get("parent_ids") or []]
                + [{"type": "contains", "target": item} for item in row.get("contains_ids") or []]
                + [{"type": "aligned", "target": item} for item in row.get("aligned_model_ids") or []]
            ),
        }
        if not entry["digest"]:
            entry["installable"] = False
        entries.append(entry)

    by_id = {entry["id"]: entry for entry in entries}
    changed = True
    while changed:
        changed = False
        for entry in entries:
            if entry["installable"] and any(not by_id.get(req, {}).get("installable") for req in entry["requires"]):
                entry["installable"] = False
                changed = True

    output = {
        "vercy": "0.2-draft",
        "kind": "runtime-model-index",
        "generatedAt": datetime.now(timezone.utc).isoformat(timespec="seconds").replace("+00:00", "Z"),
        "catalogue": "https://ver.cy/models/",
        "policy": {
            "autoInstallable": "published and locally present AGENTS.md/spec.yaml and verified digest and resolved required closure",
            "requiredRelations": ["requires"],
            "optionalRelations": ["parent", "contains", "aligned"],
            "draftAndTodo": "never auto-install",
        },
        "summary": {
            "total": len(entries),
            "published": sum(item["status"] == "published" for item in entries),
            "installable": sum(item["installable"] for item in entries),
        },
        "models": sorted(entries, key=lambda item: item["id"]),
    }
    (MODELS / "runtime-index.json").write_text(json.dumps(output, ensure_ascii=False, indent=2) + "\n", encoding="utf-8", newline="\n")
    print(json.dumps(output["summary"], ensure_ascii=False))


if __name__ == "__main__":
    main()
