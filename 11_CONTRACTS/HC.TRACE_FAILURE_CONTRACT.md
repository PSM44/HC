# HC TraceContext and Failure Taxonomy

STATUS: IMPLEMENTATION_BASELINE
FRONT: P6
VERSION: v0.1

TraceContext preserves correlation across MORCH, RORCH, WorkUnits, Specialists,
Testers and Verifiers.

Minimum durable correlation:

- trace_id
- task_id
- issue_id
- attempt_id

WorkUnit correlation is included when applicable.

FailureRecord separates failure class from retryability.

`UNKNOWN` retryability never authorizes blind retry.

Failure classes are structural categories, not vendor-specific exception names.

Reason codes SHOULD be stable machine-readable identifiers.

Failure evidence SHOULD preserve provenance through evidence references.

Canonical schemas:

- `11_CONTRACTS/schemas/trace-context.schema.json`
- `11_CONTRACTS/schemas/failure-record.schema.json`

These contracts enable P7 recovery policy and P9 observability.
