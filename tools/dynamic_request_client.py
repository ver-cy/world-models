#!/usr/bin/env python3
"""Claim and update Vercy dynamic model requests without printing worker secrets."""

from __future__ import annotations

import argparse
import json
import os
import sys
import urllib.error
import urllib.request
from pathlib import Path

DEFAULT_BASE = "https://ver.cy/api/v1"


def read_json(path: str | None) -> dict | None:
    if not path:
        return None
    return json.loads(Path(path).expanduser().read_text(encoding="utf-8"))


def worker_token(token_file: str | None) -> str:
    configured = os.environ.get("VERCY_WORKER_TOKEN")
    path = Path(token_file).expanduser() if token_file else Path.home() / ".vercy" / "model-worker.token"
    token = configured or (path.read_text(encoding="utf-8").strip() if path.is_file() else "")
    if not token:
        raise ValueError(f"worker token is unavailable; expected VERCY_WORKER_TOKEN or {path}")
    return token


def request_json(url: str, method: str = "GET", payload: dict | None = None, token: str | None = None) -> tuple[int, dict]:
    data = json.dumps(payload, ensure_ascii=False).encode("utf-8") if payload is not None else None
    headers = {"Accept": "application/json", "User-Agent": "vercy-dynamic-worker/1.0"}
    if data is not None:
        headers["Content-Type"] = "application/json"
    if token:
        headers["Authorization"] = f"Bearer {token}"
    outgoing = urllib.request.Request(url, data=data, headers=headers, method=method)
    try:
        with urllib.request.urlopen(outgoing, timeout=45) as response:
            return response.status, json.loads(response.read().decode("utf-8"))
    except urllib.error.HTTPError as error:
        body = error.read().decode("utf-8", errors="replace")
        try:
            parsed = json.loads(body)
        except json.JSONDecodeError:
            parsed = {"error": {"code": "http_error", "message": body[:500]}}
        return error.code, parsed


def atomic_write(path: Path, payload: dict) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    temporary = path.with_name(path.name + ".tmp")
    temporary.write_text(json.dumps(payload, ensure_ascii=False, indent=2) + "\n", encoding="utf-8", newline="\n")
    os.chmod(temporary, 0o600)
    os.replace(temporary, path)


def claim(args: argparse.Namespace) -> int:
    token = worker_token(args.token_file)
    status, response = request_json(
        args.base_url.rstrip("/") + "/model-requests/claim/",
        "POST",
        {"worker_id": args.worker_id, "lease_seconds": args.lease_seconds},
        token,
    )
    if status != 200:
        print(json.dumps(response, ensure_ascii=False, indent=2), file=sys.stderr)
        return 2
    if response.get("status") == "empty":
        print(json.dumps({"status": "empty", "retry_after_seconds": response.get("retry_after_seconds", 300)}, indent=2))
        return 0
    claim_path = Path(args.claim_file).expanduser().resolve()
    atomic_write(claim_path, response)
    item = response.get("request", {})
    need = item.get("request_json", {}).get("need", {})
    request_path = None
    if args.request_root:
        request_id = item.get("request_id", "")
        if not isinstance(request_id, str) or not request_id:
            raise ValueError("claimed response has no request_id")
        request_path = Path(args.request_root).expanduser().resolve() / request_id / "request.json"
        atomic_write(request_path, item.get("request_json") or {})
    print(json.dumps({
        "status": "claimed",
        "request_id": item.get("request_id"),
        "kind": item.get("kind"),
        "concept": need.get("name"),
        "candidate_id": item.get("candidate_id"),
        "lease_until": response.get("lease_until"),
        "claim_file": str(claim_path),
        "request_file": str(request_path) if request_path else None,
        "warning": response.get("untrusted_input_warning"),
    }, ensure_ascii=False, indent=2))
    return 0


def show(args: argparse.Namespace) -> int:
    claim_data = read_json(args.claim_file) or {}
    claim_data.pop("lease_token", None)
    print(json.dumps(claim_data, ensure_ascii=False, indent=2))
    return 0


def update(args: argparse.Namespace) -> int:
    claim_data = read_json(args.claim_file) or {}
    item = claim_data.get("request", {})
    payload = {
        "request_id": item.get("request_id"),
        "worker_id": args.worker_id,
        "lease_token": claim_data.get("lease_token"),
        "status": args.status,
    }
    progress = read_json(args.progress_json)
    resolution = read_json(args.resolution_json)
    if progress is not None:
        payload["progress"] = progress
    if resolution is not None:
        payload["resolution"] = resolution
    if args.error_code or args.error_message:
        payload["error"] = {"code": args.error_code or "worker_error", "message": args.error_message or "Worker failed closed."}
    status, response = request_json(
        args.base_url.rstrip("/") + "/model-requests/update/",
        "POST",
        payload,
        worker_token(args.token_file),
    )
    if status != 200:
        print(json.dumps(response, ensure_ascii=False, indent=2), file=sys.stderr)
        return 2
    if args.status in {"published", "needs-review", "failed", "retry"}:
        Path(args.claim_file).expanduser().unlink(missing_ok=True)
    print(json.dumps(response, ensure_ascii=False, indent=2))
    return 0


def status_command(args: argparse.Namespace) -> int:
    status, response = request_json(args.base_url.rstrip("/") + f"/model-requests/?id={args.request_id}")
    print(json.dumps(response, ensure_ascii=False, indent=2))
    return 0 if status == 200 else 2


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--base-url", default=DEFAULT_BASE)
    parser.add_argument("--token-file")
    sub = parser.add_subparsers(dest="command", required=True)

    claim_parser = sub.add_parser("claim")
    claim_parser.add_argument("--worker-id", required=True)
    claim_parser.add_argument("--lease-seconds", type=int, default=3600)
    claim_parser.add_argument("--claim-file", required=True)
    claim_parser.add_argument("--request-root", help="Write a sanitized <uuid>/request.json without the lease token")
    claim_parser.set_defaults(run=claim)

    show_parser = sub.add_parser("show")
    show_parser.add_argument("--claim-file", required=True)
    show_parser.set_defaults(run=show)

    update_parser = sub.add_parser("update")
    update_parser.add_argument("--worker-id", required=True)
    update_parser.add_argument("--claim-file", required=True)
    update_parser.add_argument("--status", required=True, choices=("researching", "validating", "publishing", "published", "retry", "needs-review", "failed"))
    update_parser.add_argument("--progress-json")
    update_parser.add_argument("--resolution-json")
    update_parser.add_argument("--error-code")
    update_parser.add_argument("--error-message")
    update_parser.set_defaults(run=update)

    status_parser = sub.add_parser("status")
    status_parser.add_argument("request_id")
    status_parser.set_defaults(run=status_command)

    args = parser.parse_args()
    try:
        return args.run(args)
    except (OSError, ValueError, json.JSONDecodeError) as error:
        print(f"ERROR: {error}", file=sys.stderr)
        return 2


if __name__ == "__main__":
    raise SystemExit(main())
