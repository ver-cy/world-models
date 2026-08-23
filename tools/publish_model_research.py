#!/usr/bin/env python3
"""Project a validated research synthesis into a website-ready model package.

The publisher deliberately distinguishes a public research draft from a
canonical release.  A synthesis with publication holds may be made visible for
review, but it cannot be labelled published or canonical.
"""

from __future__ import annotations

import argparse
import csv
import hashlib
import html
import json
import re
import shutil
from pathlib import Path
from typing import Any


ROOT = Path(__file__).resolve().parents[1]
REGISTRY_PATH = ROOT / "planning" / "VERCY-UNIFIED-MEGA-REGISTRY.csv"

CATEGORY_LABELS = {
    "ACT": "Activities and processes",
    "SOC": "Society, people and institutions",
    "PHY": "Physical world and living systems",
    "INF": "Information and virtual systems",
    "XCT": "Cross-cutting context",
}
STOP_WORDS = {"a", "an", "and", "for", "in", "of", "or", "the", "to", "with"}


def slugify(value: str) -> str:
    return re.sub(r"[^a-z0-9]+", "-", value.casefold()).strip("-")


def load_json(path: Path) -> dict[str, Any]:
    with path.open(encoding="utf-8") as handle:
        return json.load(handle)


def load_json_projection(path: Path) -> dict[str, Any]:
    text = path.read_text(encoding="utf-8")
    if text.startswith("#"):
        text = text.split("\n", 1)[1]
    return json.loads(text)


def split_values(value: str | None) -> list[str]:
    if not value:
        return []
    return [part.strip() for part in re.split(r"\s*;\s*", value) if part.strip()]


def stable_unique(values: list[str]) -> list[str]:
    result: list[str] = []
    seen: set[str] = set()
    for value in values:
        key = value.casefold()
        if value and key not in seen:
            result.append(value)
            seen.add(key)
    return result


def registry_metadata(model_id: str, model_name: str) -> dict[str, Any]:
    with REGISTRY_PATH.open(encoding="utf-8-sig", newline="") as handle:
        row = next(
            (item for item in csv.DictReader(handle)
             if item.get("model_id", "").casefold() == model_id.casefold()),
            None,
        )
    if row is None:
        raise SystemExit(f"model is absent from unified registry: {model_id}")
    nav_path = row.get("nav_path", "")
    match = re.search(r"(?:^|/)NAV\.([A-Z]+)", nav_path)
    category = CATEGORY_LABELS.get(match.group(1), "World model") if match else "World model"
    domains = split_values(row.get("domain_tags"))
    words = [
        word for word in re.findall(r"[a-z0-9]+", model_name.casefold())
        if word not in STOP_WORDS and len(word) > 1
    ]
    tags = stable_unique(
        words
        + [value.casefold() for value in domains]
        + [value.casefold() for value in split_values(row.get("alternate_names"))]
    )
    return {
        "family": "World Models",
        "category": category,
        "industry": ["Cross-industry"],
        "domain": domains,
        "tags": tags,
    }


def archive_existing_publication(target: Path, new_version: str) -> list[dict[str, str]]:
    """Keep an immutable URL for the package replaced by a newer draft."""
    publication_path = target / "publication.json"
    spec_path = target / "spec.yaml"
    if not publication_path.is_file() or not spec_path.is_file():
        return []
    publication = load_json(publication_path)
    old_version = str(publication.get("version", "")).strip()
    old_spec = load_json_projection(spec_path)
    previous = list(old_spec.get("metaModel", {}).get("previousVersions", []))
    if not old_version or old_version == new_version:
        return previous
    if not re.fullmatch(r"[0-9A-Za-z][0-9A-Za-z._+-]{0,127}", old_version):
        raise SystemExit(f"unsafe existing publication version: {old_version}")
    archive = target / "versions" / old_version
    archive.mkdir(parents=True, exist_ok=True)
    for name in ("index.html", "spec.yaml", "AGENTS.md", "publication.json"):
        source = target / name
        if source.is_file():
            shutil.copy2(source, archive / name)
    previous.insert(0, {
        "version": old_version,
        "url": f"/models/{target.name}/versions/{old_version}/",
    })
    return previous


def write_json(path: Path, value: Any, *, header: str | None = None) -> None:
    body = json.dumps(value, ensure_ascii=False, indent=2) + "\n"
    if header:
        body = f"# {header}\n{body}"
    path.write_text(body, encoding="utf-8")


def counts(result: dict[str, Any]) -> dict[str, int]:
    bundles = result["structure"]["bundles"]
    layers = [layer for bundle in bundles for layer in bundle["layers"]]
    findings = [finding for layer in layers for finding in layer["findings"]]
    return {
        "sources": len(result["sources"]),
        "bundles": len(bundles),
        "layers": len(layers),
        "findings": len(findings),
        "questions": sum(len(finding["questions"]) for finding in findings),
        "artifacts": sum(len(finding["artifacts"]) for finding in findings),
        "functions": len(result["functions"]),
    }


def render_question(question: dict[str, Any]) -> str:
    answer_data = "".join(f"<li>{html.escape(str(item))}</li>" for item in question.get("answer_data", []))
    answer = f"<details class=\"answer-shape\"><summary>Expected answer</summary><ul>{answer_data}</ul></details>" if answer_data else ""
    return (
        f"<li><span>{html.escape(question.get('text', question.get('id', 'Question')))}</span>"
        f"<small>{html.escape(question.get('kind', ''))}</small>{answer}</li>"
    )


def render_finding(finding: dict[str, Any]) -> str:
    questions = "".join(render_question(question) for question in finding.get("questions", []))
    artifacts = "".join(
        f"<li><strong>{html.escape(artifact.get('name', artifact.get('id', 'Artifact')))}</strong>"
        f"<span>{html.escape(artifact.get('description', ''))}</span></li>"
        for artifact in finding.get("artifacts", [])
    )
    artifact_block = f"<h5>Artifacts</h5><ul class=\"artifact-list\">{artifacts}</ul>" if artifacts else ""
    return f"""
      <article class="finding" id="finding-{html.escape(finding['id'])}">
        <div class="finding-head"><code>{html.escape(finding['id'])}</code><h4>{html.escape(finding['name'])}</h4></div>
        <p>{html.escape(finding.get('description', ''))}</p>
        <h5>Questions</h5><ol class="question-list">{questions}</ol>
        {artifact_block}
      </article>"""


def render_tree(result: dict[str, Any]) -> str:
    bundles = []
    for bundle in result["structure"]["bundles"]:
        layers = []
        for layer in bundle["layers"]:
            findings = "".join(render_finding(finding) for finding in layer["findings"])
            layers.append(f"""
          <details class="layer">
            <summary><code>{html.escape(layer['id'])}</code><strong>{html.escape(layer['name'])}</strong><span>{len(layer['findings'])} findings</span></summary>
            <div class="layer-body"><p>{html.escape(layer.get('description', ''))}</p>{findings}</div>
          </details>""")
        bundles.append(f"""
      <details class="bundle">
        <summary><code>{html.escape(bundle['id'])}</code><strong>{html.escape(bundle['name'])}</strong><span>{len(bundle['layers'])} layers</span></summary>
        <div class="bundle-body"><p>{html.escape(bundle.get('description', ''))}</p>{''.join(layers)}</div>
      </details>""")
    return "".join(bundles)


def render_page(spec: dict[str, Any], adjudication: dict[str, Any], digest: str) -> str:
    meta = spec["metaModel"]
    model = spec["model"]
    metric = spec["statistics"]
    holds = "".join(f"<li>{html.escape(item)}</li>" for item in adjudication.get("publication_holds", []))
    omissions = "".join(f"<li>{html.escape(item)}</li>" for item in adjudication.get("deferred_research", []))
    previous = "".join(
        f"<a href=\"{html.escape(item['url'])}\">{html.escape(item['version'])}</a>"
        for item in meta.get("previousVersions", [])
    ) or "-"
    return f"""<!doctype html>
<html lang="en"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1">
<title>{html.escape(meta['name'])} · Vercy</title>
<meta name="description" content="{html.escape(model['purpose'])}">
<link rel="canonical" href="{html.escape(spec['canonicalUrl'])}">
<link rel="stylesheet" href="/assets/site.css?v=20260822.1">
<style>
.model{{max-width:var(--v-width);margin:auto;padding:58px 24px 100px}}.model h1{{font-size:clamp(42px,7vw,82px);line-height:1;margin:15px 0}}.draft-note{{border:1px solid #8a632d;background:#211e14;color:#ead49a;border-radius:12px;padding:18px;margin:28px 0}}.draft-note strong{{color:#ffcb85}}.stats{{display:grid;grid-template-columns:repeat(6,1fr);gap:10px;margin:28px 0 46px}}.stats div{{border:1px solid var(--v-line);background:var(--v-panel);border-radius:11px;padding:15px}}.stats strong{{display:block;font-size:25px}}.stats span{{font-size:12px;color:var(--v-muted)}}.facts{{display:grid;grid-template-columns:repeat(3,1fr);gap:10px;margin:24px 0}}.fact{{border:1px solid var(--v-line);background:var(--v-panel);border-radius:10px;padding:15px}}.fact span{{display:block;color:var(--v-muted);font-size:11px;text-transform:uppercase;letter-spacing:.08em}}.fact strong,.fact a{{display:block;margin-top:7px}}.bundle,.layer{{border:1px solid var(--v-line);border-radius:12px;background:var(--v-panel);margin:12px 0}}.bundle>summary,.layer>summary{{display:grid;grid-template-columns:minmax(120px,.45fr) 1.6fr auto;gap:14px;align-items:center;padding:18px;cursor:pointer}}summary code,.finding code{{color:var(--v-cyan)}}summary span{{color:var(--v-muted);font-size:12px}}.bundle-body,.layer-body{{padding:0 18px 18px}}.bundle-body>p,.layer-body>p,.finding>p{{color:var(--v-muted);line-height:1.6}}.layer{{background:#091724}}.finding{{border:1px solid var(--v-line);border-radius:10px;padding:18px;margin:12px 0;background:#08131f}}.finding-head{{display:flex;gap:12px;align-items:baseline}}.finding h4{{margin:0}}.finding h5{{margin-bottom:8px}}.question-list{{padding-left:22px}}.question-list>li{{padding:7px 0;color:var(--v-text)}}.question-list small{{display:inline-block;margin-left:8px;color:var(--v-cyan)}}.answer-shape{{margin:7px 0 0 4px;color:var(--v-muted)}}.answer-shape summary{{cursor:pointer}}.artifact-list{{display:grid;grid-template-columns:repeat(2,1fr);gap:8px;padding:0;list-style:none}}.artifact-list li{{border:1px solid var(--v-line);border-radius:8px;padding:12px}}.artifact-list span{{display:block;color:var(--v-muted);font-size:13px;margin-top:5px}}.review-grid{{display:grid;grid-template-columns:1fr 1fr;gap:14px;margin-top:42px}}.review-grid section{{border:1px solid var(--v-line);border-radius:12px;background:var(--v-panel);padding:20px}}.review-grid li{{color:var(--v-muted);margin:8px 0;line-height:1.5}}@media(max-width:900px){{.stats{{grid-template-columns:repeat(3,1fr)}}.facts,.review-grid{{grid-template-columns:1fr}}}}@media(max-width:620px){{.stats,.artifact-list{{grid-template-columns:1fr 1fr}}.bundle>summary,.layer>summary{{grid-template-columns:1fr}}}}
</style></head><body><main class="model">
<nav class="v-breadcrumb"><a class="v-breadcrumb-link" href="/models/">← Catalogue</a></nav>
<span class="v-eyebrow">World Models · public research draft</span><h1>{html.escape(meta['name'])}</h1>
<p class="v-lede">{html.escape(model['purpose'])}</p>
<div class="v-actions"><a class="v-button v-button-primary" href="spec.yaml">AI YAML</a><a class="v-button" href="AGENTS.md">AGENTS.md</a><a class="v-button" href="{html.escape(spec['sourceUrl'])}">Research evidence</a></div>
<div class="draft-note"><strong>Research draft.</strong> The Claude + Grok synthesis is public for review and use with caution. It passed structural validation but is not yet a canonical Vercy release because the source and coverage holds below remain open.</div>
<section class="facts"><div class="fact"><span>Catalogue ID</span><strong>{html.escape(meta['id'])}</strong></div><div class="fact"><span>Version</span><strong>{html.escape(meta['version'])}</strong></div><div class="fact"><span>Previous version</span><strong>{previous}</strong></div><div class="fact"><span>Type</span><strong>{html.escape(meta['entryKind'])}</strong></div><div class="fact"><span>Validation</span><strong>Passed</strong></div><div class="fact"><span>Synthesis digest</span><strong><code>sha256:{digest[:16]}…</code></strong></div></section>
<section class="stats">{''.join(f'<div><strong>{metric[key]}</strong><span>{key.title()}</span></div>' for key in ('sources','bundles','layers','findings','questions','artifacts'))}</section>
<section><span class="v-eyebrow">Format-independent logical structure</span><h2>Bundles → Layers → Findings → Questions + Artifacts</h2>{render_tree(spec)}</section>
<div class="review-grid"><section><h2>Publication holds</h2><ul>{holds}</ul></section><section><h2>Deferred research</h2><ul>{omissions}</ul></section></div>
</main><script src="/assets/site-shell.js?v=20260822.1"></script><script src="/assets/zip-store.js"></script><script src="/assets/template-builder.js?v=20260822.1"></script></body></html>
"""


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--model-id", required=True)
    parser.add_argument("--version", required=True)
    parser.add_argument("--run-root", type=Path, default=ROOT / "research" / "runs")
    parser.add_argument("--output-root", type=Path, default=ROOT / "publications")
    parser.add_argument("--source-url", default="")
    parser.add_argument("--previous-version", default="")
    parser.add_argument("--previous-url", default="")
    args = parser.parse_args()

    run_dir = args.run_root / args.model_id.casefold()
    result_path = run_dir / "synthesis.result.json"
    validation = load_json(run_dir / "synthesis.validation.json")
    adjudication = load_json(run_dir / "adjudication.json")
    result = load_json(result_path)
    if not validation.get("valid"):
        raise SystemExit("synthesis does not pass validation")
    if adjudication.get("critical_conflicts"):
        raise SystemExit("critical conflicts prevent even research-draft publication")

    model = result["model"]
    if model["model_id"].casefold() != args.model_id.casefold():
        raise SystemExit("model id does not match synthesis")
    catalogue = registry_metadata(model["model_id"], model["name"])
    slug = f"{args.model_id.casefold()}-{slugify(model['name'])}"
    target = args.output_root / slug
    target.mkdir(parents=True, exist_ok=True)
    previous_versions = archive_existing_publication(target, args.version)
    synthesis_digest = hashlib.sha256(result_path.read_bytes()).hexdigest()
    source_url = args.source_url or (
        f"https://github.com/ver-cy/world-models/tree/feat/mega-model-registry/"
        f"research/runs/{args.model_id.casefold()}"
    )
    if args.previous_version and args.previous_url:
        previous_versions.insert(0, {"version": args.previous_version, "url": args.previous_url})
    deduplicated_previous: dict[str, dict[str, str]] = {}
    for item in previous_versions:
        deduplicated_previous.setdefault(item["version"], item)
    previous_versions = list(deduplicated_previous.values())

    metric = counts(result)
    spec = {
        "vercy": "1.0-draft",
        "publication": {
            "status": "research-draft",
            "adjudicationStatus": adjudication["status"],
            "publishableCanonical": bool(adjudication.get("publishable")),
            "generatedAt": adjudication["generated_at"],
            "synthesisSha256": synthesis_digest,
            "providers": ["Claude", "Grok"],
        },
        "metaModel": {
            "id": model["model_id"],
            "registryId": model["registry_id"],
            "name": model["name"],
            "version": args.version,
            "previousVersions": previous_versions,
            "entryKind": model["entry_kind"],
            "family": catalogue["family"],
            "category": catalogue["category"],
            "industry": catalogue["industry"],
            "domain": catalogue["domain"],
            "tags": catalogue["tags"],
            "status": "research draft",
        },
        "canonicalUrl": f"https://ver.cy/models/{slug}/",
        "sourceUrl": source_url,
        "model": model,
        "sources": result["sources"],
        "structure": result["structure"],
        "functions": result["functions"],
        "composition": result["composition"],
        "serviceLayers": result["service_layers"],
        "coverage": result["coverage"],
        "researchAdjudication": {
            "boundaryDecision": adjudication["boundary_decision"],
            "decisions": adjudication["decisions"],
            "publicationHolds": adjudication.get("publication_holds", []),
            "deferredResearch": adjudication.get("deferred_research", []),
        },
        "statistics": metric,
    }
    write_json(target / "spec.yaml", spec, header="Vercy AI instruction - YAML 1.2 (JSON-compatible)")
    publication = {
        "schema": "https://ver.cy/schemas/model-publication/v1",
        "model_id": model["model_id"],
        "registry_id": model["registry_id"],
        "name": model["name"],
        "slug": slug,
        "version": args.version,
        "status": "draft",
        "review_state": adjudication["status"],
        "spec_available": True,
        "canonical_publishable": bool(adjudication.get("publishable")),
        "source_url": source_url,
        "synthesis_sha256": synthesis_digest,
        "statistics": metric,
        "publication_holds": adjudication.get("publication_holds", []),
    }
    write_json(target / "publication.json", publication)
    agents = f"""# {model['name']}

- Name: {model['name']}
- Catalogue ID: {model['model_id']}
- Registry ID: {model['registry_id']}
- Type: Vercy {model['entry_kind']} (public research draft)
- Version: {args.version}
- Specification: https://ver.cy/models/{slug}/spec.yaml
- Storage type: format-independent; select a binding in the page constructor
- Interface: https://ver.cy/models/{slug}/#template-builder
- Processes: https://ver.cy/processes/
- Research evidence: {source_url}

Read this file first, then `spec.yaml`. Traverse Bundle → Layer → Finding →
Questions and Artifacts. Treat the specification as a research draft: do not
claim canonical completeness while `researchAdjudication.publicationHolds` is
non-empty. Preserve source references, master-system identity and access rules.
"""
    (target / "AGENTS.md").write_text(agents, encoding="utf-8")
    page = render_page(spec, adjudication, synthesis_digest)
    page = "\n".join(line.rstrip() for line in page.splitlines()) + "\n"
    (target / "index.html").write_text(page, encoding="utf-8")
    print(json.dumps({"output": str(target), "statistics": metric}, ensure_ascii=False))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
