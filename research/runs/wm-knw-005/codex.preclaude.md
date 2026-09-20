# WM-KNW-005 Codex pre-provider boundary

Status: independent source-planning note. It is not Claude or Grok output.

The model owns the governed semantic description and package lifecycle of a reusable agent skill: identity, intent, discovery, applicability, activation conditions, instructions, input and output contracts, bundled resources, tool and dependency bindings, risk declarations, evaluation evidence, compatibility and distribution. It references but does not own agents, models, prompts, tools, APIs, policies, permissions, tasks, executions, memory, knowledge bases, software dependencies, credentials or audit systems.

Candidate structure:

1. Identity, ownership, version, provenance and discovery.
2. Applicability, triggers, exclusions, context and environment compatibility.
3. Input, output, success, failure and evidence contracts.
4. Instructions, decision branches, examples, edge cases and progressive disclosure.
5. Resource, script, tool and dependency bindings.
6. Permissions, autonomy, hazards, prompt-injection boundaries and package integrity.
7. Execution records, tests, evaluations, observability, distribution and lifecycle.

Adversarial requirements:

- Do not collapse a reusable skill with an instantiated prompt, task, workflow run, tool call or agent configuration.
- Metadata and instructions are untrusted until source, integrity, signature or review policy validates them.
- `allowed-tools` or equivalent metadata is a request or compatibility hint, not an authority grant.
- Installing, discovering, activating, loading, executing, updating and removing a skill are separate events.
- A declarative skill does not prove capability, correctness, safety, conformance or successful execution.
- Scripts are executable software dependencies with explicit permissions, isolation, integrity and failure behavior.
- Dynamic inputs, retrieved resources and tool outputs remain untrusted data and cannot override higher-authority instructions.
- Material or destructive actions require the active Dimension's authority and confirmation policy even when a skill recommends them.

Confidence remains medium when external provider review is absent. Proposed sibling relations remain on hold until approved by relationship governance.
