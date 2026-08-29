#!/usr/bin/env python3
"""Load and validate the repository-wide research provider policy."""

from __future__ import annotations

import json
from pathlib import Path
from typing import Any


ROOT = Path(__file__).resolve().parents[1]
POLICY_PATH = ROOT / "research" / "provider-policy.json"
KNOWN_PROVIDERS = {"claude", "grok"}


def load_provider_policy(path: Path = POLICY_PATH) -> dict[str, Any]:
    if not path.exists():
        return {
            "contract_version": "1.0.0",
            "mode": "dual-provider",
            "active_providers": ["claude", "grok"],
            "waived_providers": [],
            "review_rule": "Both independent provider results are required.",
        }
    policy = json.loads(path.read_text(encoding="utf-8"))
    active = policy.get("active_providers")
    waived = policy.get("waived_providers")
    if not isinstance(active, list) or not active:
        raise ValueError("provider policy requires a non-empty active_providers array")
    if len(active) != len(set(active)) or any(item not in KNOWN_PROVIDERS for item in active):
        raise ValueError("provider policy contains duplicate or unknown active providers")
    if not isinstance(waived, list) or any(not isinstance(item, dict) for item in waived):
        raise ValueError("provider policy waived_providers must be an array of objects")
    waived_names = [item.get("provider") for item in waived]
    if len(waived_names) != len(set(waived_names)) or any(item not in KNOWN_PROVIDERS for item in waived_names):
        raise ValueError("provider policy contains duplicate or unknown waived providers")
    if set(active) & set(waived_names):
        raise ValueError("a provider cannot be both active and waived")
    expected_mode = "dual-provider" if len(active) == 2 else "single-provider-waiver"
    if policy.get("mode") != expected_mode:
        raise ValueError(f"provider policy mode must be {expected_mode!r}")
    if len(active) == 1 and set(active + waived_names) != KNOWN_PROVIDERS:
        raise ValueError("single-provider policy must explicitly waive the inactive provider")
    return policy


def active_providers(policy: dict[str, Any]) -> list[str]:
    return list(policy["active_providers"])


def waived_provider_names(policy: dict[str, Any]) -> list[str]:
    return [item["provider"] for item in policy.get("waived_providers", [])]


def provider_label(provider: str) -> str:
    return {"claude": "Claude", "grok": "Grok"}.get(provider, provider)
