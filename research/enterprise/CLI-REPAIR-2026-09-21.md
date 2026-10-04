# Claude CLI and local Codex integration repair

The owner explicitly requested this repair on 2026-09-21. Installed versions verified: Claude Code 2.1.278 and Codex CLI 0.154.0-alpha.6.2.

The user-scope Claude Codex MCP wrapper invoked the removed `codex mcp-server` command. A local stdio compatibility adapter now exposes codex and codex-reply over `codex exec --json`; the original MCP registration is retained. The wrapper discovers the installed executable dynamically. Default sandbox is read-only; workspace-write requires an explicit authorized call. No unrestricted sandbox or approval bypass was added.

Verification:
- Claude CLI without MCP: successful response in about 3 seconds.
- Codex exec: successful JSONL response in about 8 seconds.
- Eight local adapter tests passed: exact stdin, error handling, timeout, cancellation, parameter boundaries and scoped session resumption.
- MCP handshake reports Connected.
- Actual new Codex request and continuation after bridge restart succeeded.
- Actual Claude-to-Codex-to-Claude tool flow invoked both MCP tools successfully, in about 27 seconds, with no permission denials.
- A bounded W3C ORG research probe using the exact Vercy build_command path, WebFetch permission and structured-output schema completed successfully in about 17 seconds.

The Vercy Claude runner now adds an empty strict MCP configuration for that invocation only. Built-in WebSearch and WebFetch remain allowed. Independent research therefore does not initialize unrelated local integrations or delegate its independent result to Codex. Normal Claude MCP use is unaffected.

This does not establish that the old MCP error was the sole cause of the WM-ORG-017 1200-second research timeout. The old failed terminal manifest is immutable evidence and was not overwritten. Do not rerun that same attempt merely to relabel it successful. New model studies may use the repaired, bounded isolated CLI route; browser fallback remains a separate labeled evidence mode.

The bridge is a local adapter, not an official OpenAI MCP replacement. Interactive approval callbacks, arbitrary config overrides, unrestricted sandbox and unrelated session adoption are not implemented. Existing Claude sessions may need to reconnect the codex MCP server before using the new process.

Official references:
- https://learn.chatgpt.com/docs/mcp-server
- https://learn.chatgpt.com/docs/non-interactive-mode
