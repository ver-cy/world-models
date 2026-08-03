# N7 Message & Communication

This meta-model describes communications between agents: messages with parts and attachments, organized in threads, carried over channels to addresses, with delivery evidence and consent to be contacted. It is its own model because exchange semantics (send, deliver, read, bounce, reply) are identical whether the channel is email, chat, postal or broadcast, and because delivery evidence and consent form a distinct governed record separate from the content documents a message may carry.

## Manifest

```yaml
muif:
  version: "1.0"
metaModel:
  id: "vercy:world:n7"
  csn: world.messageCommunication
  version: 0.2.0
  displayName: "Message & Communication"
  description: "Messages, threads, channels, addresses, delivery evidence and contact consent between agents."
conformance:
  muc: "2.0: Conformant"
  mmas: A1
namespaces:
  - world.messageCommunication
bundles:
  - csn: world.messageCommunication.exchange
    displayName: "Exchange"
    layers:
      - world.messageCommunication.exchange.messageAndContent
      - world.messageCommunication.exchange.threadAndConversation
  - csn: world.messageCommunication.transport
    displayName: "Transport"
    layers:
      - world.messageCommunication.transport.channelAndAddress
      - world.messageCommunication.transport.deliveryAndReceipt
  - csn: world.messageCommunication.custody
    displayName: "Custody"
    layers:
      - world.messageCommunication.custody.consentAndPreference
      - world.messageCommunication.custody.archivalRetention
imports:
  - source: rfc-5322
    version: "*"
  - source: mime
    version: "*"
  - source: w3c-activitystreams-2
    version: "*"
```

## Bundles and layers

| Bundle | Responsibility | Layers |
|---|---|---|
| `exchange` | What was said and in which conversation | `messageAndContent`: messages, parts, attachments Â· `threadAndConversation`: threads, topics, participation |
| `transport` | How it travelled | `channelAndAddress`: channels, providers, address schemes Â· `deliveryAndReceipt`: delivery status and evidence |
| `custody` | Permission and preservation | `consentAndPreference`: consent to contact, preferences, revocation Â· `archivalRetention`: retention of communication records |

## Objects

- `message`: a unit of communication from a sender; key attributes: messageId, senderRef, sentAt, subject, sensitivity.
- `messagePart`: a content part of a message; key attributes: partIndex, mediaType, byteSize.
- `attachmentRef`: a pointer from a message to a carried document; key attributes: documentRef, filename, checksum.
- `thread`: a conversation grouping messages; key attributes: threadId, topic, startedAt, participantCount.
- `channel`: a transport medium; key attributes: channelType, providerRef, addressScheme.
- `address`: a reachable endpoint of an agent on a channel; key attributes: addressValue, schemeRef, ownerRef, verified.
- `deliveryReceipt`: evidence about a message's transport outcome; key attributes: statusCode, recordedAt, reporterRef.
- `consentRecord`: permission of a subject to be contacted; key attributes: subjectRef, channelRef, purpose, grantedAt, revokedAt.

## Relationships

- `message` -> belongsTo -> `thread` (N:1): conversation membership.
- `message` -> sentVia -> `channel` (N:1): the transport actually used.
- `message` -> addressedTo -> `address` (N:N): recipients as endpoints.
- `message` -> repliesTo -> `message` (N:1): reply chains within a thread.
- `messagePart` -> partOf -> `message` (N:1): multipart content structure.
- `deliveryReceipt` -> confirms -> `message` (N:1): transport evidence per message.
- `consentRecord` -> authorizes -> `address` (N:1): contact permission for an endpoint and purpose.

## Events

- `messageSent`: the sender released a message into a channel.
- `messageDelivered`: transport confirmed arrival at the recipient endpoint.
- `messageRead`: the recipient opened or acknowledged the message.
- `messageBounced`: transport failed and reported the failure.
- `messageRecalled`: the sender withdrew a message where the channel allows it.
- `consentGranted`: a subject permitted contact on a channel for a purpose.
- `consentRevoked`: a subject withdrew a previously granted permission.

## Contracts

- `deliveryServiceContract`: terms between sender and channel provider for carriage and receipts.
- `archiveAccessContract`: terms for access to retained communication records.
- `consentedContactContract`: the standing permission scope under which a sender may contact a subject.

## Projections

- `inboxView`: recipient-facing messages and threads; omits routing internals and other recipients' receipts.
- `complianceArchiveView`: full messages with delivery evidence and consent state for authorized review; omits live channel credentials.
- `threadSummaryView`: participants, timeline and subjects of a conversation; omits message bodies.

## Composition

- REFERENCE `world.person` (H1): individual senders, recipients and consent subjects.
- REFERENCE `world.organization` (O1): organizational senders and channel providers.
- REFERENCE `world.documentRecord` (N1): attachments resolve to governed documents held there.
- REFERENCE `world.identifierNaming` (N8): address schemes are registered identifier schemes.
- REFERENCE `world.languageTerminology` (N9): language tagging of message content.
- imports: rfc-5322 (ALIGN): message and header semantics.
- imports: mime (ALIGN): multipart content and media type semantics.
- imports: w3c-activitystreams-2 (ALIGN): actor-to-actor messaging semantics for social channels.

## Stewardship

The neutral owner archetype is the sender as owner of the message record, with recipients owning their own copies and consent subjects owning their consent records. Access is always granted by the respective owner through the catalogue's S1/S2 ownership and access models, with archive access audited via S4.
