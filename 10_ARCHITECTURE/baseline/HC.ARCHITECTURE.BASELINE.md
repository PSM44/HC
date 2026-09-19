# HC Architecture & Governance Baseline

VERSION: v0.3-BOOTSTRAP
STATUS: PARTIAL_BASELINE_ACTIVE

This file is the bootstrap architecture index. Detailed normative content lives
in the canonical source documents referenced below.

## Canonicalized fronts

### A — North Star / Architecture Intent

Source:

`10_ARCHITECTURE/HC.NORTH_STAR.md`

Status:

`CANONICALIZED`

### B — Capability Map

Source:

`10_ARCHITECTURE/HC.CAPABILITY_MAP.md`

Status:

`CANONICALIZED`

### C — Role / Authority Model

Source:

`10_ARCHITECTURE/HC.ROLE_AUTHORITY_MODEL.md`

Status:

`CANONICALIZED`

### D — Task / Work Unit Contracts

Sources:

- `11_CONTRACTS/HC.TASK_WORK_UNIT_CONTRACT.md`
- `11_CONTRACTS/schemas/task-envelope.schema.json`
- `11_CONTRACTS/schemas/work-unit.schema.json`

Covers:

- TaskEnvelope
- WorkUnit
- bounded authority
- immutable delegation
- permissions
- mutation scope
- acceptance criteria
- evidence requirements
- retry policy
- terminal return

Status:

`CANONICALIZED`

### F — Issue / Attempt State Model

Source:

`12_STATE/HC.ISSUE_ATTEMPT_STATE_MODEL.md`

Status:

`CANONICALIZED`

### I — Technology Selection Framework

Source:

`30_RESEARCH/HC.TECHNOLOGY_SELECTION_FRAMEWORK.md`

Status:

`CANONICALIZED`

### J — Technology Registry / Watch

Sources:

- `30_RESEARCH/HC.TECHNOLOGY_REGISTRY.json`
- `30_RESEARCH/technology-watch/HC.TECHNOLOGY_WATCH_POLICY.md`

Covers:

- technology lifecycle
- verification status
- ownership separation
- candidate registry
- Technology Watch
- reassessment triggers

Status:

`CANONICALIZED`

### K — Runtime / Repository Boundary

Source:

`10_ARCHITECTURE/HC.RUNTIME_REPO_BOUNDARY.md`

Status:

`CANONICALIZED`

## Eligible fronts

### E — Tester / Verifier / Evidence Contract

Status:

`ELIGIBLE`

Dependencies satisfied by C + D.

### H — Parallel DAG / Resource Ownership

Status:

`ELIGIBLE`

Dependencies satisfied by C + D + F.

## Blocked front

### G — Specialist Escalation Contract

Status:

`BLOCKED_BY_E`

D is already satisfied. E remains outstanding.

## Current parallel frontier

The next architecture iteration should advance:

`E + H`

in parallel.

After E converges, G becomes eligible.

## Technology lifecycle rule

Lifecycle state and verification status are separate axes.

For OpenClaw HC-E05:

- lifecycle state: `IMPLEMENTED`
- verification status: `PARTIAL_VERIFIED`
- active owner: `false`

`PARTIAL_VERIFIED` is not a lifecycle state.

## HEAD authority

Git is authoritative for the live repository HEAD.

Canonical project files use:

`HEAD_POLICY=RESOLVE_LIVE_FROM_GIT`

and record only a previously reconciled parent SHA for provenance rather than
attempting to embed their own commit SHA.
