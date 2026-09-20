# HC Big Picture Roadmap

VERSION: v1.0-WBS
STATUS: ACTIVE
NORTH_STAR_STATUS: NOT_YET_PROVEN

## 00.00 HUMAN / Product Authority

- 00.10 Intent / goals
- 00.20 Policy / risk / cost / security approval
- 00.30 Irreversible decisions
- 00.40 External publication / credentials

Normal manual boundary: `HUMAN <-> MORCH`

## 10.00 MORCH — Meta-Orchestrator

- 10.10 Goal reconciliation
- 10.20 Global DAG
- 10.30 Cross-runtime strategy
- 10.40 Priority / conflict resolution
- 10.50 Technology ownership decisions
- 10.60 Escalation policy
- 10.70 Global terminal-convergence decision
- 10.80 Roadmap / North-Star control

## 20.00 HC Control Plane

- 20.10 TaskEnvelope enforcement
- 20.20 WorkUnit enforcement
- 20.30 Authority / delegation enforcement
- 20.40 Mutation-scope enforcement
- 20.50 Permission enforcement
- 20.60 Acceptance-criteria registry
- 20.70 Terminal return / single-envelope gate
- 20.80 Policy / invariant engine

## 30.00 RORCH — Runtime Orchestrator

- 30.10 Dispatch
- 30.20 Parallel execution
- 30.30 Child lifecycle
- 30.40 Retry
- 30.50 Wait
- 30.60 Cancel
- 30.70 Runtime convergence

## 40.00 State Plane

- 40.10 ISSUE_ID
- 40.20 ATTEMPT
- 40.30 State machine
- 40.40 Supersession
- 40.50 Persistence
- 40.60 Stale-attempt guard
- 40.70 Transition history

## 50.00 Resource / DAG Control

- 50.10 READ / WRITE / EXCLUSIVE
- 50.20 Single canonical writer
- 50.30 Atomic admission
- 50.40 Conflict detection
- 50.50 Resource WAIT
- 50.60 Claim release
- 50.70 Deadlock control
- 50.80 Fairness policy

## 60.00 Runtime / Session Fabric

- 60.10 RuntimeAdapter interface
- 60.20 Herdr adapter candidate
- 60.30 ACP / ACPX adapter
- 60.40 Direct CLI adapter
- 60.50 Local process adapter
- 60.60 Future remote-runtime adapter
- 60.70 MORCH -> RORCH -> WSL2 runtime bridge

Runtime technology transports work; it does not acquire HC authority.

## 70.00 Harness Plane

- 70.10 HarnessAdapter interface
- 70.20 Codex
- 70.30 Claude Code
- 70.40 Hermes
- 70.50 OpenCode
- 70.60 DSH
- 70.70 OpenClaw agent runtime
- 70.80 Future harnesses

`ROLE != PRODUCT`

## 80.00 Execution Roles

### 80.10 EXECUTOR

Bounded WorkUnit, authorized mutations, implementation, deterministic return.

### 80.20 SPECIALIST

Bounded lateral escalation, preserves ISSUE_ID / ATTEMPT, no orchestration, no
self-verification.

### 80.30 Tool Worker

Deterministic bounded tools.

### 80.40 Background Worker

Long-lived work under RORCH ownership.

## 90.00 Quality / Verification Plane

### 90.10 TESTER

- execute tests
- observe behavior
- produce raw evidence
- normalize TestEvidence
- never decide project completion

### 90.20 EVIDENCE

- provenance
- raw / normalized / derived distinction
- sensitivity classification
- integrity metadata
- persistence policy

### 90.30 VERIFIER

- evaluate acceptance criteria
- evaluate invariants
- evaluate evidence sufficiency
- detect contradictions
- produce VerificationResult
- cannot silently repair implementation

### 90.40 Verification Gate

PASS / FAIL / BLOCKED / INSUFFICIENT_EVIDENCE / CONTRADICTORY_EVIDENCE

## 100.00 Checkpoint / Resume / Recovery

- 100.10 Checkpoint persistence
- 100.20 Same-attempt resume
- 100.30 New-attempt retry
- 100.40 Crash recovery
- 100.50 Idempotency
- 100.60 Stale-attempt rejection
- 100.70 Session recovery
- 100.80 Runtime / harness reattachment

## 110.00 Model Plane

### 110.10 OmniRoute

Primary model-gateway candidate.

### 110.20 HC model policies / packs

- hc-control
- hc-coding
- hc-coding-hard
- hc-review
- hc-specialist
- hc-background
- hc-cheap

### 110.30 Provider adapters

OpenAI, Anthropic, DeepSeek, OpenRouter, Gemini, Qwen, GLM, and future providers.

### 110.40 Routing

Fallback/health, cost/quota, and capability routing.

### 110.50 Identity

Prefer one API key / credential identity per HC consumer or harness where the
gateway supports it.

The model plane supplies model execution; it does not own orchestration,
verification, or completion authority.

## 120.00 Observability / Telemetry

- 120.10 TraceContext
- 120.20 Structured logs
- 120.30 Metrics
- 120.40 ISSUE_ID / ATTEMPT correlation
- 120.50 Task / WorkUnit lineage
- 120.60 Runtime health
- 120.70 Harness health
- 120.80 Model / provider health
- 120.90 Cost / token / latency accounting
- 120.100 Failure taxonomy
- 120.110 OpenTelemetry adapter candidate

## 130.00 Memory / Learning Plane

- 130.10 Working context
- 130.20 Durable memory
- 130.30 LearningEvent
- 130.40 Verified-learning gate
- 130.50 Provenance
- 130.60 Supersession
- 130.70 Retention / TTL
- 130.80 Retrieval

Invariant: `VERIFIED_BEFORE_LEARNING`

## 140.00 Technology Governance

- 140.10 Technology Registry
- 140.20 Research record
- 140.30 Requirements filter
- 140.40 ADR
- 140.50 Targeted PoC
- 140.60 Verification
- 140.70 Lifecycle decision
- 140.80 Technology Watch
- 140.90 Replacement / retirement

Lifecycle:
CANDIDATE -> RESEARCHED -> SELECTED_FOR_POC -> IMPLEMENTED -> VERIFIED -> ACTIVE_OWNER

Side/terminal states: REJECTED, DEFERRED, SUPERSEDED, RETIRED.

## 150.00 Security / Trust / Secrets

- 150.10 Credential store
- 150.20 SecretRef
- 150.30 Per-harness / per-consumer API keys
- 150.40 Least privilege
- 150.50 Filesystem boundaries
- 150.60 Network permissions
- 150.70 External publication gate
- 150.80 Sensitive evidence handling
- 150.90 Audit

## 160.00 Canonical Repository / State

- 160.10 Git canonical authority
- 160.20 WSL2 canonical runtime
- 160.30 Exact mutation scope
- 160.40 Exact stage
- 160.50 Commit / push
- 160.60 Remote parity
- 160.70 Evidence store
- 160.80 Continuity / BATON
- 160.90 Roadmap / backlog

## 170.00 Autonomous E2E Chain

HUMAN -> MORCH -> HC Control Plane -> RORCH -> WorkUnit -> RuntimeAdapter ->
HarnessAdapter -> EXECUTOR / SPECIALIST -> TESTER -> EVIDENCE -> VERIFIER ->
STATE PERSISTENCE -> TERMINAL CONVERGENCE -> MORCH -> HUMAN

No normal manual relay below MORCH.

## 180.00 Terminal Convergence / North Star Gate

- 180.10 No mandatory child active
- 180.20 No mandatory tester active
- 180.30 No verifier active
- 180.40 No pending retry
- 180.50 No unreleased resource claim
- 180.60 Canonical state persisted
- 180.70 Required evidence persisted
- 180.80 No unresolved material contradiction
- 180.90 Single final envelope
- 180.100 Regression matrix PASS

Only after all required gates converge may HC claim its North Star.

## Cross-plane architecture

```text
HUMAN
  |
  v
MORCH
  |
  v
HC CONTROL PLANE
  |
  +---------------------+
  |                     |
  v                     v
RORCH                STATE / RESOURCE CONTROL
  |                     |
  +----------+----------+
             |
             v
      RUNTIME FABRIC
   Herdr / ACPX / CLI
             |
             v
       HARNESS PLANE
 Codex / Claude / Hermes
 OpenCode / DSH / OpenClaw
             |
      +------+------+
      |             |
      v             v
 EXECUTOR       SPECIALIST
      |             |
      +------+------+
             |
             v
           TESTER
             |
             v
          EVIDENCE
             |
             v
          VERIFIER
             |
             v
     STATE PERSISTENCE
             |
             v
  TERMINAL CONVERGENCE
             |
             v
           MORCH
```

Model-plane relationship:

```text
Harness
   |
   v
Model policy
   |
   v
OmniRoute
   |
   +--> OpenAI
   +--> Anthropic
   +--> DeepSeek
   +--> OpenRouter
   +--> Gemini
   +--> Qwen / GLM / others
```

## Immediate big-picture path

```text
NOW
 |
 +--> qualify Herdr
 |
 +--> retain ACPX as alternate runtime adapter
 |
 +--> define RuntimeAdapter / HarnessAdapter
 |
 +--> define OmniRoute HC model policies
 |
 v
FIRST AUTONOMOUS READ
 |
 v
FIRST BOUNDED AUTONOMOUS WRITE
 |
 v
HUMAN RELAY ELIMINATION
 |
 +--> P3 Resource Scheduler
 +--> P4 Quality Runtime
 +--> P7 Recovery
 +--> P9 Observability
 |
 v
P5 Specialist Routing
 |
 v
P10 Verified Learning
 |
 v
P11 Autonomous E2E
 |
 v
P13 Regression / Terminal Gate
 |
 v
HC NORTH STAR
```
