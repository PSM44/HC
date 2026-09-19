# HC Architecture & Governance Baseline

VERSION: v0.4-BOOTSTRAP
STATUS: PARTIAL_BASELINE_ACTIVE

This file is the bootstrap architecture index.

## Canonicalized fronts

### A — North Star / Architecture Intent
`10_ARCHITECTURE/HC.NORTH_STAR.md`
Status: `CANONICALIZED`

### B — Capability Map
`10_ARCHITECTURE/HC.CAPABILITY_MAP.md`
Status: `CANONICALIZED`

### C — Role / Authority Model
`10_ARCHITECTURE/HC.ROLE_AUTHORITY_MODEL.md`
Status: `CANONICALIZED`

### D — Task / Work Unit Contracts

Sources:

- `11_CONTRACTS/HC.TASK_WORK_UNIT_CONTRACT.md`
- `11_CONTRACTS/schemas/task-envelope.schema.json`
- `11_CONTRACTS/schemas/work-unit.schema.json`

Status: `CANONICALIZED`

### E — Tester / Verifier / Evidence

Sources:

- `11_CONTRACTS/HC.TESTER_VERIFIER_EVIDENCE_CONTRACT.md`
- `11_CONTRACTS/schemas/test-evidence.schema.json`
- `11_CONTRACTS/schemas/verification-result.schema.json`

Key invariants:

- Tester produces observations/evidence.
- Verifier evaluates declared criteria and invariants.
- UNKNOWN is not PASS.
- Contradictory evidence prevents PASS.
- Verification cannot silently repair implementation.

Status: `CANONICALIZED`

### F — Issue / Attempt State Model
`12_STATE/HC.ISSUE_ATTEMPT_STATE_MODEL.md`
Status: `CANONICALIZED`

### H — Parallel DAG / Resource Ownership

Sources:

- `10_ARCHITECTURE/HC.PARALLEL_DAG_RESOURCE_OWNERSHIP.md`
- `11_CONTRACTS/schemas/resource-claim.schema.json`

Key invariants:

- parallel by default;
- READ/READ compatible;
- WRITE and EXCLUSIVE conflict by default;
- unknown scope overlap is conflict;
- one active canonical writer;
- superseded/stale work loses mutation authority.

Status: `CANONICALIZED`

### I — Technology Selection Framework
`30_RESEARCH/HC.TECHNOLOGY_SELECTION_FRAMEWORK.md`
Status: `CANONICALIZED`

### J — Technology Registry / Watch

Sources:

- `30_RESEARCH/HC.TECHNOLOGY_REGISTRY.json`
- `30_RESEARCH/technology-watch/HC.TECHNOLOGY_WATCH_POLICY.md`

Status: `CANONICALIZED`

### K — Runtime / Repository Boundary
`10_ARCHITECTURE/HC.RUNTIME_REPO_BOUNDARY.md`
Status: `CANONICALIZED`

## Eligible front

### G — Specialist Escalation

Status:

`ELIGIBLE`

Dependencies D and E are canonical.

G must preserve ISSUE_ID and ATTEMPT, remain lateral rather than supervisory,
and return through the evidence/verification path.

## Current frontier

`G_SPECIALIST_ESCALATION`

## HEAD authority

Git is authoritative for live HEAD.

Canonical files use:

`HEAD_POLICY=RESOLVE_LIVE_FROM_GIT`

and retain the last reconciled parent SHA only for provenance.
