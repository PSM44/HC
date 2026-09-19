# HC TaskEnvelope / WorkUnit Contract

STATUS: BOOTSTRAP_BASELINE
FRONT: D
CONTRACT_VERSION: hc.task-work-unit.v0.1

## Purpose

This contract defines the minimum deterministic delegation boundary between HC
orchestration roles and bounded execution roles.

A narrative prompt is not a canonical delegation contract.

Canonical delegation requires typed `TaskEnvelope` and `WorkUnit` data.

## Relationship

One `TaskEnvelope` represents one orchestrated task lineage.

A TaskEnvelope references one or more WorkUnits.

Each WorkUnit:

- belongs to exactly one TaskEnvelope;
- preserves ISSUE_ID and ATTEMPT identity;
- carries bounded authority;
- declares dependencies;
- declares resource claims;
- declares mutation scope;
- declares acceptance criteria;
- declares evidence requirements;
- declares retry policy;
- declares its terminal return contract.

## TaskEnvelope invariants

A TaskEnvelope MUST include:

- contract version;
- TASK_ID;
- ISSUE_ID;
- ATTEMPT;
- objective;
- authority chain;
- WorkUnit identifiers;
- required terminal states;
- final return contract;
- canonical-state persistence requirement.

A TaskEnvelope MUST NOT:

- grant authority implicitly through prose;
- permit an executor to add new canonical mutation scope;
- declare task-level PASS before mandatory WorkUnits converge;
- treat UNKNOWN as PASS.

## WorkUnit invariants

A WorkUnit MUST include:

- WORK_UNIT_ID;
- TASK_ID;
- ISSUE_ID;
- ATTEMPT;
- immutable delegation version;
- delegating role;
- assigned role;
- objective;
- dependency list;
- resource claims;
- permissions;
- exact mutation scope;
- acceptance criteria;
- evidence requirements;
- retry policy;
- terminal return contract.

A WorkUnit MUST be rejected before execution when:

- required identity is missing;
- dependency state is incompatible;
- delegated authority exceeds the delegator;
- mutation scope is ambiguous;
- a conflicting canonical writer exists;
- required evidence cannot be produced;
- the requested operation violates a trust/safety boundary.

## Delegation immutability

A running WorkUnit cannot silently alter its own delegation.

Material changes to:

- objective;
- authority;
- mutation scope;
- dependencies;
- acceptance criteria;
- resource claims

require a new delegation version issued by an authorized upstream role.

The WorkUnit may report that broader scope is required. It may not self-grant it.

## Resource claims

Resource claims exist to support safe DAG parallelism.

Claims use:

- resource identifier;
- access mode;
- optional scope.

Access modes:

- READ
- WRITE
- EXCLUSIVE

Conflicting canonical WRITE/EXCLUSIVE ownership must be resolved before
parallel execution.

The detailed scheduler/resource-ownership algorithm belongs to Front H.

## Permissions

Permissions are explicit booleans or bounded declarations.

At minimum the contract distinguishes:

- filesystem read;
- filesystem write;
- process execution;
- network access;
- credential use;
- canonical mutation;
- external publication.

Absence of permission means permission is not granted.

## Mutation scope

Canonical mutation scope is an allowlist.

An empty mutation scope means:

`NO_CANONICAL_MUTATION`

Broad implicit mutation such as repository-wide `git add .` is not authorized by
this contract unless the exact delegated scope itself is repository-wide and
explicitly justified.

## Acceptance criteria

Acceptance criteria are machine-addressable statements identified by stable IDs.

An executor may produce evidence for an acceptance criterion.

Where independent verification is required, the executor cannot mark that
criterion verified.

## Evidence requirements

Evidence requirements specify:

- evidence ID/type;
- required producer role where applicable;
- persistence requirement;
- sensitivity classification.

Evidence and verification semantics are expanded by Front E.

## Retry policy

Retry policy specifies:

- allowed failure classes;
- maximum attempts;
- backoff policy;
- idempotency requirement;
- checkpoint/resume rule;
- escalation threshold.

WAIT, RETRY, BLOCKED and FAIL remain distinct.

Blind retry is prohibited.

## Terminal return

A WorkUnit terminal return is machine-oriented and DELTA_ONLY.

Minimum fields:

- WORK_UNIT_ID;
- ISSUE_ID;
- ATTEMPT;
- STATUS;
- DELTA;
- EVIDENCE_REFS;
- TERMINAL_CONVERGENCE.

A TaskEnvelope final return may only be emitted after all mandatory children,
tests, verification, retries and required state writes have converged.

## Authority

Role/provider/runtime identities are separate.

A runtime implementing RORCH or EXECUTOR does not acquire additional authority
because of its vendor, model, installation mode or local privileges.

## Schemas

Machine-readable schemas:

- `11_CONTRACTS/schemas/task-envelope.schema.json`
- `11_CONTRACTS/schemas/work-unit.schema.json`

These schemas define structural minimums.

Semantic authority, resource conflicts and verification are enforced by their
respective HC control-plane components, not by JSON Schema alone.
