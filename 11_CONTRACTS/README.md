# Contracts

HC components communicate through versioned, typed contracts.

Narrative output must never mutate canonical state directly.

## Materialized

### Front D — Task / Work Unit

Normative contract:

- `HC.TASK_WORK_UNIT_CONTRACT.md`

Schemas:

- `schemas/task-envelope.schema.json`
- `schemas/work-unit.schema.json`

Status:

`CANONICALIZED`

### Front E — Tester / Verifier / Evidence

Normative contract:

- `HC.TESTER_VERIFIER_EVIDENCE_CONTRACT.md`

Schemas:

- `schemas/test-evidence.schema.json`
- `schemas/verification-result.schema.json`

Status:

`CANONICALIZED`

## Pending contract families

- SolverResult
- SpecialistProblemPack / SpecialistReport
- LearningEvent
- TraceContext
- Error/Failure classification

Specialist escalation is owned by Front G.

Parallel DAG/resource-conflict semantics are owned by Front H.
