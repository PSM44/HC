# HC Parallel DAG and Resource Ownership Model

STATUS: BOOTSTRAP_BASELINE
FRONT: H
VERSION: v0.1

## Purpose

HC executes independent eligible work in parallel by default.

Sequential execution is justified only by:

- a real dependency;
- a resource conflict;
- an authority boundary;
- a safety boundary;
- a technical constraint.

Scheduling convenience alone is not a reason to serialize independent work.

## DAG node eligibility

A WorkUnit is eligible to start only when:

1. all mandatory predecessor conditions are satisfied;
2. its delegation is valid;
3. its resource claims can be granted;
4. its required authority is available;
5. no superseding WorkUnit has invalidated it;
6. no safety/trust gate blocks execution.

Eligibility is not equivalent to execution.

Execution additionally requires resource admission.

## Resource claim model

Each WorkUnit declares zero or more resource claims.

Each claim has:

- resource_id;
- access;
- optional scope.

Access modes:

- READ
- WRITE
- EXCLUSIVE

## Compatibility matrix

Two claims may execute concurrently when all applicable claims are compatible.

Default compatibility:

| Existing | Requested READ | Requested WRITE | Requested EXCLUSIVE |
| --- | --- | --- | --- |
| READ | ALLOW | BLOCK | BLOCK |
| WRITE | BLOCK | BLOCK | BLOCK |
| EXCLUSIVE | BLOCK | BLOCK | BLOCK |

READ + READ is parallel-safe by default.

All other same-resource combinations block unless a future resource-specific
policy explicitly proves a narrower non-conflicting scope.

## Scope

Resource scope may narrow a resource claim.

Two scoped claims may execute concurrently only when HC can deterministically
prove the scopes do not overlap.

UNKNOWN overlap is treated as conflict.

String inequality alone is not proof of non-overlap.

## Canonical single-writer rule

A canonical resource may have at most one active writer.

Canonical mutation requires:

- valid delegation;
- canonical_mutation permission;
- WRITE or EXCLUSIVE resource ownership;
- exact mutation scope.

No two WorkUnits may simultaneously hold conflicting canonical write authority.

## Admission

Resource admission is atomic with respect to conflicting claims.

The scheduler must not:

1. inspect resources;
2. observe no conflict;
3. allow another writer;
4. then grant the original claim.

Claim evaluation and grant must behave as one serialized control-plane decision
for each conflict domain.

## Claim lifecycle

A granted claim belongs to:

- TASK_ID;
- WORK_UNIT_ID;
- ISSUE_ID;
- ATTEMPT.

A claim terminates when the WorkUnit:

- reaches a terminal state;
- is cancelled;
- is superseded;
- explicitly releases the claim.

A stale attempt MUST NOT retain resource authority.

Recovery must reconcile persisted claim state against live attempt state before
granting new conflicting claims.

## WAIT and resource contention

Resource contention does not automatically mean FAIL.

When a WorkUnit is otherwise eligible but a required resource is held by another
valid WorkUnit, it enters or remains:

`WAITING`

with a machine-readable reason such as:

`RESOURCE_CONFLICT`

This is distinct from retrying a failed execution attempt.

## Deadlock prevention

The scheduler should avoid cyclic resource acquisition.

Preferred rule:

- WorkUnits declare complete required claims before execution;
- claims are admitted atomically as a set.

If incremental claims are later supported, HC must define deterministic ordering
and deadlock detection before enabling them.

## Fairness

Correctness and authority dominate throughput.

Subject to those constraints, the scheduler should avoid indefinite starvation.

Fairness policy may consider:

- readiness time;
- explicit priority;
- dependency criticality;
- retry/escalation policy.

Priority cannot override authority or conflicting canonical ownership.

## Supersession

When an attempt or WorkUnit is superseded:

- it loses eligibility for new mutation;
- new resource claims are denied;
- existing claims must be released or revoked safely;
- late results cannot overwrite current canonical state.

Superseded work may retain evidence value.

## Cancellation

Cancellation is a control-plane event.

The scheduler must distinguish:

- cancellation requested;
- runtime acknowledged;
- process stopped;
- resource claims released;
- final state persisted.

A cancellation request alone does not prove resource release.

## Parallel convergence

Parent convergence requires:

- all mandatory child nodes terminal;
- no mandatory child running;
- no required test/verifier active;
- no unresolved resource lease owned by stale work;
- required canonical mutations/state writes persisted.

The parent cannot emit terminal PASS merely because all executors have returned.

## ResourceClaim schema

Machine-readable structural contract:

`11_CONTRACTS/schemas/resource-claim.schema.json`

Front D embeds compatible resource-claim fields in WorkUnit.

Front H owns scheduling semantics and conflict resolution.
