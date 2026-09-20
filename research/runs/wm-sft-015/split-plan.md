# WM-SFT-015 bounded Claude research plan

WM-SFT-015 combines a reusable test definition, execution evidence and the
governance needed to use both safely. To keep the research bounded and avoid
identifier collisions, Claude is run through three non-overlapping passes.

1. `design` owns test-case identity, specification, inputs, preconditions,
   steps, expected outcomes, oracles, parametrization and traceability.
2. `execution` owns execution context, observed outcomes, result disposition,
   evidence, retries, flakiness and links to defects and releases.
3. `governance` owns assurance, coverage, review, authority, lifecycle,
   provenance, access, retention, interoperability and canonical service rules.

Each pass must be independently schema-valid and use its assigned local-ID
prefix. The deterministic merger unions the structures, keeps the full model
boundary from `design`, keeps service layers from `governance`, remaps source
IDs and validates the combined result. A no-tools adjudication remains
mandatory and may require a registry split if Test Case and Test Result cannot
be defended as one aggregate boundary.
