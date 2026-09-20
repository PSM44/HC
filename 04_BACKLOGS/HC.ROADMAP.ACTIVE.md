# HC Active Roadmap

VERSION: v1.1-RUNTIME-FABRIC
STATUS: ACTIVE
PHASE: IMPLEMENTATION
NORTH_STAR_STATUS: NOT_YET_PROVEN

## North Star

Autonomous, durable, long-running, iterative, multipath, resumable,
multi-harness AI execution with verified outcomes and human-auditable state.

## Operating doctrine

PARALLEL_BY_DEFAULT.

Sequence only for real dependency, resource conflict, authority, safety, or
technical constraint.

Architecture is provider-, model-, harness-, runtime-, and protocol-replaceable.

## Current implementation state

- P1 Contract Enforcement Runtime: `IMPLEMENTED_BASELINE_VERIFIED`
- P2 State Transition Engine: `IMPLEMENTED_BASELINE_VERIFIED`
- P3 Resource Scheduler: `ELIGIBLE`
- P4 Tester / Verifier / Evidence Runtime: `ELIGIBLE`
- P5 Specialist Runtime Routing: `BLOCKED_BY_P4`
- P6 TraceContext + Failure Taxonomy: `CANONICALIZED`
- P7 Checkpoint / Resume / Recovery: `ELIGIBLE`
- P8 Runtime Fabric / Human-Relay Elimination: `ACTIVE_PRIORITY_P0`
- P9 Observability: `ELIGIBLE`
- P10 Verified Learning: `BLOCKED_BY_P4`
- P11 Autonomous E2E Chain: `BLOCKED`
- P12 Technology Research / ADR Pipeline: `CANONICALIZED`
- P13 Regression + Terminal Convergence Gate: `BLOCKED_BY_P11`

## WBS architecture mapping

| WBS | Module | Primary roadmap ownership |
|---:|---|---|
| 00.00 | HUMAN Authority | governance boundary |
| 10.00 | MORCH | global orchestration |
| 20.00 | HC Control Plane | P1 |
| 30.00 | RORCH | P1 / P3 / P8 |
| 40.00 | State Plane | P2 / P7 |
| 50.00 | Resource / DAG Control | P3 |
| 60.00 | Runtime / Session Fabric | P8 |
| 70.00 | Harness Plane | P5 / P8 |
| 80.00 | Execution Roles | P5 / P8 |
| 90.00 | Tester / Evidence / Verifier | P4 |
| 100.00 | Checkpoint / Resume / Recovery | P7 |
| 110.00 | Model Plane / OmniRoute | P8 / P12 |
| 120.00 | Observability / Telemetry | P6 / P9 |
| 130.00 | Memory / Verified Learning | P10 |
| 140.00 | Technology Governance | P12 |
| 150.00 | Security / Trust / Secrets | cross-cutting |
| 160.00 | Canonical Repo / State | cross-cutting |
| 170.00 | Autonomous E2E Chain | P11 |
| 180.00 | Terminal Convergence / North Star Gate | P13 |

## P8 — Runtime Fabric / Human-Relay Elimination

P8 is no longer modeled as one OpenClaw-only bridge.

### P8.1 RuntimeAdapter contract

Define a replaceable runtime/session interface preserving TASK_ID, WORK_UNIT_ID,
ISSUE_ID, ATTEMPT, exact authority, mutation scope, cancellation, evidence
return, and terminal state.

### P8.2 Herdr qualification

Candidate role: persistent terminal / process / session runtime.

Required spike:

1. isolated installation;
2. HC workspace;
3. agent start;
4. prompt;
5. wait;
6. read;
7. detach / reattach;
8. cancellation;
9. server/process recovery;
10. bounded write;
11. evidence return.

Herdr is a runtime candidate, not RORCH, TESTER, VERIFIER, STATE authority, or
technology owner.

### P8.3 ACP / ACPX adapter

Retain ACPX as an alternate structured agent-runtime path.
OpenClaw remains an interaction/agent-runtime candidate.
ACPX is not the sole runtime transport.

### P8.4 HarnessAdapter

Candidate harnesses include Codex, Claude Code, Hermes, OpenCode, DSH,
OpenClaw agent runtime, and future harnesses.

ROLE != PRODUCT.

### P8.5 Model-policy binding

Harness execution may bind to model policy rather than a fixed model.
OmniRoute is the primary model-plane candidate.

Example HC policies:

- `hc-control`
- `hc-coding`
- `hc-coding-hard`
- `hc-review`
- `hc-specialist`
- `hc-background`
- `hc-cheap`

### P8.6 First autonomous read-only WorkUnit

MORCH -> RORCH -> RuntimeAdapter -> Harness -> canonical WSL2 repo observation
without HUMAN script relay and without canonical mutation.

### P8.7 First bounded autonomous mutation

Exact WorkUnit and mutation scope; harness executes; TESTER runs; evidence
persists; VERIFIER evaluates; canonical state persists; commit/push only when
explicitly authorized.

### P8.8 Persistent session / resume

Prove detach, reattach, same-attempt continuation, crash/restart handling, and
stale-attempt rejection.

### P8.9 Human relay elimination gate

Target: `HUMAN_AS_RUNTIME_RELAY=NO`

Normal manual boundary becomes `HUMAN <-> MORCH`.

## P3 — Resource Scheduler

Status: `ELIGIBLE`

Implement READ / WRITE / EXCLUSIVE claims, atomic admission, one canonical
writer, contention -> WAIT, stale-claim rejection, deterministic release, and
deadlock controls.

Prefer implementation by delegated harness after P8 first autonomous mutation
is proven.

## P4 — Tester / Evidence / Verifier Runtime

Status: `ELIGIBLE`

- P4.1 TESTER runtime
- P4.2 TestEvidence
- P4.3 Evidence persistence
- P4.4 VERIFIER runtime
- P4.5 Contradiction handling
- P4.6 Verification gate

No WorkUnit PASS until mandatory tester/evidence/verifier work converges.

## P7 — Checkpoint / Resume / Recovery

Status: `ELIGIBLE`

Integrate P2 State Engine with runtime/session persistence: checkpoint, resume,
retry, crash recovery, idempotency, stale-authority rejection, and harness
reattachment.

Herdr may provide runtime persistence mechanisms but cannot own canonical HC
state semantics.

## P9 — Observability

Status: `ELIGIBLE`

Observe TaskEnvelope / WorkUnit lineage, ISSUE_ID / ATTEMPT, RuntimeAdapter,
harness, model policy, effective model/provider, tester/verifier, latency,
tokens, cost, failures, retries, checkpoint, and recovery.

## P10 — Verified Learning

Status: `BLOCKED_BY_P4`

Only verified outcomes may become durable learning.

`VERIFIED_BEFORE_LEARNING=YES`

## P11 — Autonomous E2E Chain

Status: `BLOCKED`

Target proof:

HUMAN -> MORCH -> RORCH -> WorkUnit -> RuntimeAdapter -> Harness ->
EXECUTOR / SPECIALIST -> TESTER -> EVIDENCE -> VERIFIER -> STATE PERSISTENCE ->
TERMINAL CONVERGENCE -> MORCH -> HUMAN

No manual relay below MORCH.

## P12 — Technology Governance

Status: `CANONICALIZED`

Operational flow:
CAPABILITY_NEED -> RESEARCH -> HARD_REQUIREMENT_FILTER -> ADR -> TARGETED_POC ->
VERIFICATION -> LIFECYCLE_DECISION -> TECHNOLOGY_WATCH

Current relevant candidates:

- Herdr: runtime/session candidate; `RESEARCH_REQUIRED`
- OpenClaw: interaction/agent-runtime candidate; implemented but not owner
- ACPX: ACP runtime candidate
- OmniRoute: model gateway candidate/current operational dependency outside HC ownership decision
- Hermes: harness/learning candidate
- Codex: coding harness candidate
- Claude Code: coding/specialist harness candidate
- DSH: runtime/execution candidate

Installed or working does not imply ACTIVE_OWNER.

## P13 — Regression + Terminal Convergence

Status: `BLOCKED_BY_P11`

Prove failure matrix, retry/resume, cancellation, stale-attempt protection,
resource release, no active mandatory child/tester/verifier, evidence/state
persistence, one final machine envelope, and no false DONE.

## Immediate frontier

Priority is dependency-aware, not strictly sequential.

### P0 operational priority

Advance P8 until HC can delegate at least one bounded mutation without HUMAN
script relay.

### Parallel research/control work

- P12 Herdr research + ADR/PoC definition
- P8 OmniRoute model-policy design
- P8 RuntimeAdapter and HarnessAdapter design

### Eligible implementation held for autonomous executor

Once first autonomous write is proven, delegate in parallel where resources do
not conflict: P3, P4, P7, and P9.

## North Star gate

HC must not claim North Star until P11 autonomous E2E and P13 terminal
convergence/regression pass, state/evidence are canonical, mandatory blockers
are resolved, and HUMAN is not the normal runtime relay below MORCH.
