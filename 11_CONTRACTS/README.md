# Contracts

HC components communicate through versioned, typed contracts.

Narrative output must never mutate canonical state directly.

## Materialized

### Front D — Task / Work Unit

Normative contract:

- `HC.TASK_WORK_UNIT_CONTRACT.md`

Machine-readable schemas:

- `schemas/task-envelope.schema.json`
- `schemas/work-unit.schema.json`

Status:

`CANONICALIZED`

## Pending contract families

- SolverResult
- SpecialistProblemPack / SpecialistReport
- TestEvidence
- VerificationResult
- LearningEvent
- TraceContext
- Error/Failure classification

Tester/Verifier/Evidence is owned by Front E.

Specialist escalation is owned by Front G.

Parallel DAG/resource-conflict semantics are owned by Front H.
