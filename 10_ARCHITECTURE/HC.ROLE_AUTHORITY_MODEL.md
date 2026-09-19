# HC Role and Authority Model

STATUS: BOOTSTRAP_BASELINE
FRONT: C

## Authority hierarchy

HUMAN > MORCH > RORCH > EXECUTOR

Authority flows downward by explicit delegation. Evidence and results flow
upward. A lower role cannot expand its own authority.

## HUMAN

Owns:

- project intent;
- policy;
- irreversible decisions;
- credential/security approval;
- material cost approval;
- external publication;
- exceptional authority overrides.

Normal operational boundary:

HUMAN ↔ MORCH

## MORCH — Meta-Orchestrator

Owns:

- global objective reconciliation;
- system-level DAG;
- cross-runtime strategy;
- major prioritization;
- dependency/conflict reconciliation;
- technology ownership decisions;
- escalation policy;
- terminal system-level decision.

MORCH must not silently delegate its own authority to a runtime.

## RORCH — Runtime Orchestrator

Owns within delegated scope:

- runtime DAG execution;
- safe parallelism;
- executor spawning;
- resource scheduling;
- retry/wait/block handling;
- child convergence;
- runtime-level return envelope.

RORCH cannot redefine project policy or promote a candidate to ACTIVE_OWNER.

## EXECUTOR

Owns:

- one bounded work unit;
- permitted mutations;
- deterministic evidence return.

EXECUTOR must not:

- self-expand scope;
- self-authorize destructive operations;
- claim global completion;
- self-verify where independent verification is required.

## SPECIALIST

Purpose:

bounded lateral escalation for a difficult subproblem.

Rules:

- preserves ISSUE_ID and ATTEMPT;
- receives an explicit problem pack;
- cannot become orchestrator;
- cannot self-verify;
- returns a SpecialistReport through the normal evidence path.

## TESTER

Owns:

- test execution;
- observations;
- raw and normalized test evidence.

TESTER does not decide project completion.

## VERIFIER

Owns:

- acceptance-criteria evaluation;
- invariant evaluation;
- evidence sufficiency;
- verification result.

VERIFIER does not perform hidden implementation work to make its own verification
pass.

## Authority invariants

1. Delegation is immutable for a work unit unless the authority holder issues a
   new version.
2. Canonical mutation requires authority plus exact scope.
3. Conflicting canonical writers are prohibited.
4. Resource ownership must be explicit before parallel mutation.
5. A role may refuse unsafe or contradictory delegation.
6. Specialist, Tester and Verifier are distinct concerns even when temporarily
   implemented by the same underlying technology.
7. Runtime/provider identity never changes role authority.
