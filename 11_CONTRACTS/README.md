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

### Front G — Specialist Escalation

Normative contract:

- `HC.SPECIALIST_ESCALATION_CONTRACT.md`

Schemas:

- `schemas/specialist-problem-pack.schema.json`
- `schemas/specialist-report.schema.json`

Status:

`CANONICALIZED`

## Pending cross-cutting contract families

- LearningEvent
- TraceContext
- Error/Failure classification

Parallel DAG/resource-conflict semantics are owned by Front H.
