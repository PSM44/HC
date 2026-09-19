# HC Technology Watch Policy

STATUS: BOOTSTRAP_BASELINE
FRONT: J
VERSION: v0.1

## Purpose

Technology Watch maintains read-only intelligence about technologies that may
materially affect HC architecture, security, operability or cost.

Technology Watch observes and proposes.

It does not mutate runtime ownership.

## Sources of material change

A watch event is material when it may affect:

- provider execution;
- multi-executor coordination;
- durable workflow behavior;
- checkpoint/resume;
- state/recovery;
- observability;
- security or trust boundaries;
- credentials/authentication;
- licensing;
- pricing/packaging;
- protocol compatibility;
- deprecation/EOL;
- platform support;
- API stability;
- replacement risk.

## Watch output

A material watch event should produce:

- TECHNOLOGY_ID;
- observed change;
- source/evidence;
- observation date;
- affected HC capabilities;
- severity;
- architecture relevance;
- recommended action;
- lifecycle transition proposed, if any.

The output is a proposal.

It is not authority to perform the transition.

## Lifecycle separation

The Technology Registry keeps lifecycle and verification separate.

Examples:

- installed but unverified:
  `lifecycle_state=IMPLEMENTED`
  `verification_status=POC_PENDING`

- partially verified implementation:
  `lifecycle_state=IMPLEMENTED`
  `verification_status=PARTIAL_VERIFIED`

- fully verified but not adopted:
  `lifecycle_state=VERIFIED`
  `verification_status=VERIFIED`
  `active_owner=false`

- adopted:
  `lifecycle_state=ACTIVE_OWNER`
  `verification_status=VERIFIED`
  `active_owner=true`

`PARTIAL_VERIFIED` is not a lifecycle state.

## Promotion authority

Technology Watch cannot automatically:

- install;
- upgrade;
- enable;
- configure;
- promote;
- replace;
- retire;
- publish externally.

Lifecycle transitions require evidence and the authority defined by HC
governance.

Promotion to ACTIVE_OWNER requires an explicit architectural decision.

## Candidate isolation

A watched candidate remains isolated from canonical ownership until promoted.

Candidate-specific APIs should be hidden behind replaceable adapters whenever
implementation begins.

## Reassessment triggers

Reassessment should be proposed when:

- a blocker is resolved;
- a material security issue appears;
- a materially better capability becomes available;
- an adopted technology changes license or pricing materially;
- an API/protocol becomes deprecated;
- maintenance/maturity falls below accepted thresholds;
- HC requirements materially change.

## Registry

Canonical machine-readable registry:

`30_RESEARCH/HC.TECHNOLOGY_REGISTRY.json`

The registry records current HC classification.

Technology Watch evidence explains why a future classification should change.
