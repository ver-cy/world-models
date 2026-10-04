Research lifecycle and health semantics for WM-XCT-037 Dependency / Impact.

- Preserve weak host-dependent assertion identity and externally owned endpoint state.
- Cover proposal, review, activation, satisfaction, degradation, breakage, restoration, deprecation, supersession, retirement and historical state.
- Separate assertion lifecycle from endpoint lifecycle and from observations about health.
- Define valid transitions, effective intervals, as-of reconstruction, late observations and correction without rewriting history.
- Treat dates and timestamps as qualifiers, never identifiers; timestamps include seconds and an explicit offset or `Z`.
- Do not monitor endpoints or perform remediation.
- Target 2 bundles, 4-5 layers and 7-9 findings. Every local ID begins `dep-life-`.
