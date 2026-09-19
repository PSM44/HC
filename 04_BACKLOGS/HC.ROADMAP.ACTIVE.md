# HC Active Roadmap

VERSION: v1.0-POST-BOOTSTRAP
STATUS: ACTIVE

## North Star

Autonomous, durable, long-running, iterative, multipath, resumable,
multi-harness AI execution with verified outcomes and human-auditable state.

The structural architecture baseline is canonical.

The North Star is not yet operationally proven.

## Operating rule

PARALLEL_BY_DEFAULT.

Sequence only when required by:

- dependency;
- resource conflict;
- authority;
- safety;
- technical constraint.

## Post-bootstrap DAG

### P1 — Contract Enforcement Runtime

Status:

`ELIGIBLE`

Purpose:

Implement executable enforcement for:

- TaskEnvelope;
- WorkUnit;
- delegation version;
- permission checks;
- mutation scope;
- acceptance criteria;
- terminal return contract.

Acceptance direction:

Invalid or unauthorized contracts fail closed before execution.

Dependencies:

None beyond canonical structural bootstrap.

### P2 — State Transition Engine

Status:

`ELIGIBLE`

Purpose:

Implement durable machine-enforced:

- ISSUE_ID;
- ATTEMPT;
- state transitions;
- WAIT / RETRY / BLOCKED / FAIL distinctions;
- supersession;
- state persistence;
- stale-attempt rejection.

Dependencies:

None beyond canonical structural bootstrap.

### P3 — Resource Scheduler / Ownership Enforcement

Status:

`BLOCKED_BY_P1`

Purpose:

Implement:

- READ / WRITE / EXCLUSIVE admission;
- atomic claim grant;
- single canonical writer;
- conflict detection;
- waiting on resource contention;
- stale claim recovery.

Dependencies:

P1.

P2 may enhance durable claim recovery but does not block initial scheduler implementation.

### P4 — Tester / Verifier / Evidence Runtime

Status:

`BLOCKED_BY_P1`

Purpose:

Implement executable:

- Tester role;
- TestEvidence;
- evidence provenance;
- Verifier role;
- VerificationResult;
- contradiction handling;
- no false PASS.

Dependencies:

P1.

### P5 — Specialist Runtime Routing

Status:

`BLOCKED_BY_P1_P4`

Purpose:

Implement SpecialistProblemPack / SpecialistReport routing across replaceable
specialist backends while preserving ISSUE_ID and ATTEMPT.

Must return through evidence/verification flow.

Dependencies:

P1 + P4.

### P6 — TraceContext + Failure Taxonomy

Status:

`ELIGIBLE`

Purpose:

Materialize remaining cross-cutting contract families:

- TraceContext;
- Error/Failure classification;
- reason codes;
- correlation identifiers;
- retryability classification.

Dependencies:

None beyond canonical structural bootstrap.

### P7 — Checkpoint / Resume / Recovery

Status:

`BLOCKED_BY_P2_P6`

Purpose:

Implement:

- checkpoint persistence;
- same-attempt resume;
- new-attempt retry from checkpoint;
- crash recovery;
- idempotent recovery;
- stale authority rejection.

Dependencies:

P2 + P6.

### P8 — MORCH → RORCH → WSL2 Runtime Bridge

Status:

`ELIGIBLE`

Issue:

`HC-BOOTSTRAP-RUNTIME-BRIDGE-001`

Purpose:

Eliminate HUMAN-as-runtime-relay for normal execution.

Required properties:

- exact identity;
- exact delegated scope;
- canonical WSL2 execution;
- evidence return;
- cancellation;
- bounded authority;
- no hidden canonical mutation.

Dependencies:

Structural K boundary already canonical.

### P9 — Observability

Status:

`BLOCKED_BY_P6`

Purpose:

Implement structured:

- logs;
- traces;
- metrics;
- task/work-unit lineage;
- ISSUE_ID / ATTEMPT correlation;
- runtime health;
- cost/usage;
- failure classification.

Dependencies:

P6.

### P10 — Verified Learning

Status:

`BLOCKED_BY_P4_P6`

Purpose:

Implement LearningEvent and verified-learning ingestion.

Only verified evidence may become durable learning.

Dependencies:

P4 + P6.

### P11 — Autonomous E2E Chain

Status:

`BLOCKED`

Purpose:

Prove an end-to-end autonomous chain:

HUMAN
→ MORCH
→ RORCH
→ WorkUnits
→ Executors / Specialist
→ Tester
→ Evidence
→ Verifier
→ state persistence
→ terminal return

without manual relay below MORCH.

Minimum dependencies:

P1 + P2 + P3 + P4 + P5 + P7 + P8 + P9.

P10 is valuable but not a prerequisite for the first autonomous chain proof.

### P12 — Technology Research / ADR Pipeline

Status:

`ELIGIBLE`

Purpose:

Operationalize:

- Technology Registry;
- deep research;
- ADRs;
- targeted PoCs;
- Technology Watch;
- lifecycle transitions;
- replacement decisions.

OpenClaw remains:

- lifecycle_state = IMPLEMENTED
- verification_status = PARTIAL_VERIFIED
- active_owner = false
- blocked on upstream runtime defect candidate

No candidate becomes ACTIVE_OWNER merely by being installed or functional.

### P13 — Regression + Terminal Convergence Gate

Status:

`BLOCKED_BY_P11`

Purpose:

Prove:

- failure matrix;
- retry/resume;
- cancellation;
- stale-attempt protection;
- single-envelope final return;
- no active mandatory children;
- deterministic state persistence;
- no false DONE.

Dependencies:

P11.

## Initial parallel frontier

The following are independently eligible and should advance concurrently:

1. P1 Contract Enforcement Runtime
2. P2 State Transition Engine
3. P6 TraceContext + Failure Taxonomy
4. P8 MORCH/RORCH Runtime Bridge
5. P12 Technology Research / ADR Pipeline

## North Star gate

HC must not claim the North Star until at minimum:

- P11 autonomous E2E chain is proven;
- P13 regression/terminal-convergence gate passes;
- required state/evidence is canonical;
- no unresolved mandatory blocker remains.
