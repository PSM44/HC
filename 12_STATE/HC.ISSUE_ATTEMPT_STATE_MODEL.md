# HC Issue and Attempt State Model

STATUS: BOOTSTRAP_BASELINE
FRONT: F

## Durable identity

ISSUE_ID identifies the durable problem or objective.

ATTEMPT identifies one execution lineage addressing that ISSUE_ID.

Retries, specialists and resumed execution must preserve ISSUE_ID while creating
or retaining ATTEMPT according to the transition rules.

## Issue states

Recommended canonical issue states:

- OPEN
- READY
- RUNNING
- WAITING
- BLOCKED
- VERIFYING
- RESOLVED
- REJECTED
- SUPERSEDED

## Attempt states

Recommended attempt states:

- CREATED
- ELIGIBLE
- RUNNING
- WAITING
- RETRY_PENDING
- BLOCKED
- FAILED
- TESTING
- VERIFYING
- PASS
- SUPERSEDED
- CANCELLED

## Critical semantic distinctions

WAIT:
A known condition is expected to change without declaring execution failure.

RETRY:
A prior execution attempt did not reach the required result and policy permits
another attempt.

BLOCKED:
Progress cannot continue until a dependency, authority gate, external condition
or unresolved defect changes.

FAIL:
The attempt terminated unsuccessfully.

PASS:
The attempt's acceptance criteria have been independently satisfied when
verification is required.

These states must never be collapsed.

## Attempt rules

1. Every attempt references exactly one ISSUE_ID.
2. ATTEMPT identity is durable and traceable.
3. A retry must record the predecessor attempt and retry reason.
4. Specialist escalation does not create a new issue unless problem identity
   materially changes.
5. Resumption must distinguish same-attempt resume from new-attempt retry.
6. Superseded attempts cannot later overwrite current canonical state.
7. Completion requires evidence and, where required, verification.
8. UNKNOWN is not PASS.
9. State changes must be attributable to an actor and evidence source.
10. State persistence must occur before terminal completion is reported.

## Minimum transition evidence

A transition should carry:

- ISSUE_ID;
- ATTEMPT;
- previous state;
- new state;
- reason code;
- actor/role;
- timestamp or monotonic sequence;
- evidence reference;
- parent attempt when applicable.

## Retry policy

Retry eligibility should be explicit by failure class.

A retry policy must define:

- retryable classifications;
- maximum attempts or budget;
- backoff;
- idempotency requirements;
- checkpoint policy;
- escalation threshold;
- stop conditions.

Blind retry loops are prohibited.

## Terminal convergence relationship

System-level terminal convergence requires that all mandatory issues and attempts
have reached allowed terminal states and no stale active attempt retains mutation
authority.
