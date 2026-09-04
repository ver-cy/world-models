Research the technical and information-system dependency taxonomy for
WM-XCT-037 Dependency / Impact.

- Use the exact frozen registry identity and output `entry_kind` `mixin`.
- The `model` block must describe the complete combined WM-XCT-037 boundary.
  Never mention a split, pass, sibling pass or partial delivery in model,
  coverage or adversarial prose.
- Define non-overlapping dependency kinds for software packages/modules,
  source/build/test toolchains, runtime services, APIs/protocols, data sets and
  streams, schemas/ontologies, configuration/secrets, infrastructure/compute,
  network/storage, deployment environments, security/trust material and
  external platforms.
- Separate build-time, test-time, deploy-time and runtime dependencies;
  direct/declared, discovered/observed and inferred relationships; functional
  requirement, resource consumption, compatibility, ordering and mere
  co-location or correlation.
- Align without collapsing SPDX and CycloneDX dependency graphs, package
  manifests and lockfiles, SBOM relationships, OASIS TOSCA requirements and
  relationships, OpenAPI/AsyncAPI links, infrastructure declarations and
  W3C PROV influence/usage semantics.
- For each kind declare canonical direction, endpoint type constraints,
  permitted cardinality, lifecycle phase, version/compatibility expression,
  whether it licenses graph propagation and common false-positive examples.
- Treat vulnerability reachability, software composition, runtime calls and
  data lineage as neighboring analyses or projections, not interchangeable
  dependency facts.
- Cover optional, peer, development, transitive, bundled/vendor, circular,
  platform-provided, capability/requirement and negative/conflicting technical
  relationships without adopting one package ecosystem's semantics globally.
- Do not install packages, resolve versions, scan vulnerabilities, orchestrate
  builds/deployments, call APIs, observe traffic or compute dependency closure.
- Target 2 bundles, 4-5 layers and 7-9 findings with 3-5 discriminating
  questions each. Use at least eight question kinds. Every local ID begins
  `dep-tech-`.
- Prefer primary SPDX, CycloneDX, OASIS TOSCA, W3C PROV and protocol or package
  specifications. Label ecosystem-specific rules explicitly.
