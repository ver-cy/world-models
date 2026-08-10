# M8 Device Sensor & Computing Hardware

This meta-model describes connected devices and computing equipment: the hardware unit, the sensors it hosts and what they observe, the firmware and configuration it runs, and how it is reached on a network. It is its own model because a device is the only kind of physical thing whose behavior is defined by mutable software state and whose main output is data streams, so its semantics bridge the matter cluster and the digital cluster in a way no other item family does.

## Manifest

```yaml
muif:
  version: "1.0"
metaModel:
  id: "vercy:world:m8"
  csn: world.deviceHardware
  version: 0.2.0
  displayName: "Device Sensor & Computing Hardware"
  description: Connected devices with hosted sensors, telemetry bindings, firmware, configuration and network presence.
conformance:
  muc: "2.0: Conformant"
  mmas: A1
namespaces:
  - world.deviceHardware
bundles:
  - csn: world.deviceHardware.hardware
    displayName: Hardware
    layers:
      - world.deviceHardware.hardware.deviceIdentity
      - world.deviceHardware.hardware.platformSpec
  - csn: world.deviceHardware.sensing
    displayName: Sensing
    layers:
      - world.deviceHardware.sensing.sensingCapability
      - world.deviceHardware.sensing.telemetryBinding
  - csn: world.deviceHardware.operation
    displayName: Operation
    layers:
      - world.deviceHardware.operation.firmwareState
      - world.deviceHardware.operation.configuration
      - world.deviceHardware.operation.connectivity
imports:
  - source: w3c-ssn-sosa
    version: "*"
  - source: w3c-wot-thing-description
    version: "*"
```

## Bundles and layers

| Bundle | Responsibility | Layers |
|---|---|---|
| `hardware` | The physical unit and its build | `deviceIdentity`: make, model, serial, hardware addresses and platform identifiers · `platformSpec`: compute resources, interfaces, power and environmental ratings |
| `sensing` | What the device can observe and where readings go | `sensingCapability`: hosted sensors, observed properties, ranges and accuracy · `telemetryBinding`: references binding sensors to the streams that carry their output |
| `operation` | The mutable state that defines behavior | `firmwareState`: installed firmware versions and update history · `configuration`: applied configuration profiles and settings · `connectivity`: network endpoints, reachability and online standing |

## Objects

- `device`: one hardware unit; key attributes: serial reference, model reference, lifecycle status, owner reference.
- `deviceModel`: the class of the unit; key attributes: maker reference, model code, capability baseline.
- `sensorUnit`: a sensor hosted by the device; key attributes: sensor kind, position, calibration state.
- `observedPropertySpec`: what a sensor measures; key attributes: property, unit, range, accuracy.
- `telemetryStreamRef`: a reference to the stream carrying readings; key attributes: stream identifier, cadence, retention hint.
- `firmwareVersion`: an installed or installable firmware state; key attributes: version, release reference, integrity hash.
- `configurationProfile`: a named set of applied settings; key attributes: profile identifier, parameters, applied date.
- `networkEndpoint`: how the device is reached; key attributes: address kind, address, protocol, reachability status.
- `hostAssetRef`: the asset the device is mounted on; key attributes: target model, target identifier, mount role.

## Relationships

- `device` -> instanceOf -> `deviceModel` (many-to-one): the unit inherits its model's capability baseline.
- `device` -> hosts -> `sensorUnit` (0..*): a device may carry zero or many sensors.
- `sensorUnit` -> observes -> `observedPropertySpec` (1..*): each sensor measures at least one property.
- `sensorUnit` -> emitsTo -> `telemetryStreamRef` (0..*): readings are bound to streams, not stored here.
- `device` -> runs -> `firmwareVersion` (1 current, 0..* historical): exactly one firmware state is current.
- `device` -> configuredBy -> `configurationProfile` (0..1 current): the profile in force, with history via events.
- `device` -> reachableAt -> `networkEndpoint` (0..*): endpoints may coexist across networks.
- `device` -> mountedOn -> `hostAssetRef` (0..1): the machine, vehicle, place or item the device serves.

## Events

- `deviceProvisioned`: the unit was set up, identified and bound to an owner.
- `firmwareUpdated`: a new firmware version became the current one.
- `sensorCalibrated`: a hosted sensor's calibration was performed and recorded.
- `connectivityLost`: the device stopped being reachable at its endpoints.
- `connectivityRestored`: reachability resumed after an outage.
- `configurationChanged`: a different configuration profile or setting set took effect.
- `deviceCompromiseReported`: a security compromise or vulnerability affecting the unit was reported.
- `deviceDecommissioned`: the unit was retired and its bindings closed.

## Contracts

- `telemetryAccess`: owner-granted subscription to streams bound to named sensors, scoped by property and period.
- `deviceAttestation`: query contract by which a party verifies the unit's identity, firmware integrity and calibration standing.
- `maintenanceAccess`: grant allowing a service party to read operation state and apply firmware or configuration changes.

## Projections

- `inventoryView`: identity, model, host asset and lifecycle status across a holding; omits streams and settings.
- `observabilityView`: sensors, observed properties and stream bindings; omits network addresses and security data.
- `securityAuditView`: firmware history, configuration changes and compromise reports; omits measurement semantics.

## Composition

- EXTEND `world.physicalItem` (M2): a device is an item; identity, custody and location semantics are inherited.
- REFERENCE `world.equipment` (M6): machines are host assets for monitoring devices; the machine's condition data arrives through streams bound here.
- REFERENCE `world.vehicle` (M7): telematics units mount on vehicles as host assets.
- REFERENCE the digital cluster (D): the telemetry stream content itself is a digital-cluster object; this model keeps only the binding reference.
- imports: w3c-ssn-sosa (ALIGN): sensor, observation and observed-property semantics.
- imports: w3c-wot-thing-description (ALIGN): capability and interface description of the unit.

## Stewardship

Each device record is stewarded by the device's owner per the catalogue's S1 ownership model; telemetry subscriptions, attestation queries and maintenance access exist only as S1/S2 grants from that owner, with operation-state changes traceable via S4 audit.
