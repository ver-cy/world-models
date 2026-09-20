# WM-ACT-035 Codex pre-provider boundary

Status: preparatory boundary analysis. This is not a provider result.

- A Test Execution is an occurrence, not the reusable Test Case or Procedure,
  the tested Subject, the resulting Defect, or the broader Assessment.
- The root owns execution identity, procedure revision binding, run context,
  ordered step occurrences, source observations, result assertions, evidence
  pointers and immutable lifecycle history. Referenced masters retain identity.
- Expected result, actual observation, comparison, verdict, confidence and
  compliance conclusion are separate assertions with separate provenance.
- Planned, prepared, running, paused, blocked, aborted, completed, invalidated,
  reviewed and superseded states must be event-backed and append-only.
- A retry or rerun receives a new identity and links to the prior attempt; it
  never overwrites earlier evidence or silently changes the procedure revision.
- Test terminology differs across software, laboratories, manufacturing,
  healthcare, security and safety engineering. Profiles must keep the shared
  execution kernel while making domain-specific rules explicit.

Adjudication must reject a Test Case clone, a generic Assessment clone, an
unversioned subject or procedure, inferred pass or compliance, overwritten raw
observations, a failed test automatically becoming a defect, and autonomous
execution or sign-off without delegated authority and applicable safety rules.
