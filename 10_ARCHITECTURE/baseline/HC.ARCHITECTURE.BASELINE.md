# HC Architecture & Governance Baseline

VERSION: v0.2-BOOTSTRAP
STATUS: PARTIAL_BASELINE_ACTIVE

This file is the architecture baseline index. Detailed normative content lives
in the canonical source documents listed below.

## Canonicalized bootstrap areas

### A — North Star / Architecture Intent

Source:

`10_ARCHITECTURE/HC.NORTH_STAR.md`

Covers:

- NORTH_STAR
- NON_GOALS
- automation target
- system invariants
- terminal convergence

Status:

`CANONICALIZED`

### B — Capability Map

Source:

`10_ARCHITECTURE/HC.CAPABILITY_MAP.md`

Covers:

- control plane
- execution plane
- quality/evidence
- state/recovery
- memory/learning
- integration
- observability
- technology governance
- security/trust

Status:

`CANONICALIZED`

### C — Role / Authority Model

Source:

`10_ARCHITECTURE/HC.ROLE_AUTHORITY_MODEL.md`

Covers:

- HUMAN
- MORCH
- RORCH
- EXECUTOR
- SPECIALIST
- TESTER
- VERIFIER
- authority hierarchy

Status:

`CANONICALIZED`

### F — Issue / Attempt State Model

Source:

`12_STATE/HC.ISSUE_ATTEMPT_STATE_MODEL.md`

Covers:

- ISSUE_ID
- ATTEMPT
- state transitions
- WAIT / RETRY / BLOCKED / FAIL
- retry semantics
- state/convergence relationship

Status:

`CANONICALIZED`

### I — Technology Selection Framework

Source:

`30_RESEARCH/HC.TECHNOLOGY_SELECTION_FRAMEWORK.md`

Covers:

- technology lifecycle
- research
- ADRs
- targeted PoCs
- adoption
- reassessment
- Technology Watch

Status:

`CANONICALIZED`

### K — Runtime / Repository Boundary

Source:

`10_ARCHITECTURE/HC.RUNTIME_REPO_BOUNDARY.md`

Covers:

- canonical WSL2 runtime
- repository authority
- Windows access clone
- runtime isolation
- execution bridge target

Status:

`CANONICALIZED`

## Pending bootstrap areas

### D — Task / Work Unit Contracts

Status:

`ELIGIBLE`

Dependencies satisfied by B + C.

### E — Tester / Verifier / Evidence Contract

Status:

`BLOCKED_BY_D`

### G — Specialist Escalation Contract

Status:

`BLOCKED_BY_D_E`

### H — Parallel DAG / Resource Ownership

Status:

`BLOCKED_BY_D`

F and C are already satisfied.

### J — Technology Registry / Watch

Status:

`ELIGIBLE`

Dependency I is satisfied.

## Current parallel frontier

The next architecture iteration should advance:

`D + J`

in parallel.

After D converges, recompute E and H eligibility.

## HEAD authority

Git is authoritative for the live repository HEAD.

Canonical project files must not attempt to embed the SHA of the commit that
contains themselves. State/continuity records therefore use:

`HEAD_POLICY=RESOLVE_LIVE_FROM_GIT`

and may record a previous observed/reconciled parent SHA for provenance.
