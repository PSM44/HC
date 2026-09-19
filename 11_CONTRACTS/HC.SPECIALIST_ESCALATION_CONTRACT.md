# HC Specialist Escalation Contract

STATUS: BOOTSTRAP_BASELINE
FRONT: G
CONTRACT_VERSION: hc.specialist-escalation.v0.1

## Purpose

A SPECIALIST is a bounded lateral escalation used when a WorkUnit encounters a
material subproblem that benefits from a different model, tool, expertise,
runtime or reasoning path.

A SPECIALIST is not an orchestrator.

Escalation must preserve HC identity, authority, evidence and verification
semantics.

## Core invariants

A Specialist escalation MUST:

- preserve ISSUE_ID;
- preserve ATTEMPT unless retry policy explicitly creates a new attempt;
- reference the originating TASK_ID and WORK_UNIT_ID;
- receive a bounded SpecialistProblemPack;
- declare the exact question or problem to solve;
- declare scope and prohibited actions;
- declare budget and stop conditions;
- declare required output;
- return a SpecialistReport;
- return through the normal evidence/verification path.

A Specialist MUST NOT:

- become MORCH or RORCH;
- create new global objectives;
- expand canonical mutation authority;
- change acceptance criteria;
- silently create a new ISSUE_ID;
- self-promote its report to VERIFIED;
- mark the parent WorkUnit or TaskEnvelope PASS;
- bypass TESTER or VERIFIER when verification is required.

## Escalation trigger

A Specialist may be requested when one or more explicit trigger conditions
apply, for example:

- repeated failure within retry policy;
- domain expertise gap;
- unresolved technical ambiguity;
- independent solution path required;
- architecture/risk cross-check required;
- solver diversity required;
- runtime/tool specialization required.

Escalation is not an excuse for unbounded retries.

## Problem identity

The SpecialistProblemPack preserves:

- TASK_ID;
- WORK_UNIT_ID;
- ISSUE_ID;
- ATTEMPT;
- escalation ID;
- requesting role.

The default rule is:

`SAME ISSUE_ID + SAME ATTEMPT`

A new ATTEMPT is only permitted when the parent retry policy explicitly defines
the escalation as a new execution attempt.

A new ISSUE_ID requires an authorized determination that the problem is
materially distinct.

## Scope

The SpecialistProblemPack defines:

- problem statement;
- requested output;
- allowed context;
- prohibited actions;
- mutation permission;
- resource limits;
- time/cost/tool budget;
- stop conditions.

Anything outside the pack is unauthorized.

If additional authority is required, the Specialist returns:

`SCOPE_EXPANSION_REQUIRED`

and stops.

It does not self-authorize.

## Mutation

Default Specialist mode is:

`NO_CANONICAL_MUTATION`

Canonical mutation is permitted only when the originating WorkUnit explicitly
delegates:

- canonical_mutation=true;
- exact mutation scope;
- required resource ownership;
- required acceptance/evidence obligations.

A Specialist cannot inherit broader local/system privileges as HC authority.

## Budget

A SpecialistProblemPack MUST carry explicit bounded execution policy.

At minimum:

- max rounds or calls;
- max elapsed budget or explicit no-time-budget classification;
- allowed tools/runtimes;
- stop conditions.

A Specialist MUST stop when:

- the requested result is achieved;
- a stop condition is reached;
- authority is insufficient;
- required input is unavailable;
- budget is exhausted;
- continuing would violate a trust/safety boundary.

## SpecialistReport

A SpecialistReport is a bounded result.

It records:

- identity linkage;
- status;
- findings;
- proposed answer/solution;
- assumptions;
- uncertainties;
- evidence references;
- mutations performed, if authorized;
- unresolved blockers;
- scope-expansion request, if any.

Allowed report statuses:

- SOLVED
- PARTIAL
- BLOCKED
- FAILED
- SCOPE_EXPANSION_REQUIRED
- BUDGET_EXHAUSTED

`SOLVED` means the Specialist believes it has produced the requested result.

It does not mean:

`VERIFIED`

## Evidence path

SpecialistReport may itself be evidence input.

Where testing is required:

SPECIALIST
→ SpecialistReport
→ TESTER
→ TestEvidence
→ VERIFIER
→ VerificationResult

A Specialist must not manufacture TestEvidence while acting as Specialist if
independent TESTER semantics are required.

## Verification

A Specialist cannot verify its own solution.

The VERIFIER evaluates the Specialist result only against:

- declared acceptance criteria;
- required evidence;
- applicable invariants;
- provenance.

A successful SpecialistReport does not permit the parent TaskEnvelope to emit
PASS before required verification and state persistence converge.

## Parallel specialists

Multiple Specialists may be launched in parallel when:

- they do not have conflicting resource claims;
- their scopes are independent or intentionally redundant;
- budget permits;
- the parent orchestrator retains deterministic reconciliation responsibility.

Specialists cannot reconcile themselves into a global decision unless that
authority is explicitly delegated to an orchestrator role.

## Result reconciliation

When multiple SpecialistReports disagree:

- the contradiction is preserved;
- no report silently overwrites another;
- reconciliation occurs upstream;
- additional testing or verification may be required.

Conflicting SpecialistReports are not resolved by majority vote unless an
explicit policy authorizes such a rule.

## Retry relationship

Specialist escalation is distinct from retry.

RETRY:
another attempt to execute a failed path according to retry policy.

SPECIALIST ESCALATION:
a bounded lateral problem-solving path under the same durable issue context.

A retry may invoke a Specialist, but the concepts are not interchangeable.

## Terminal convergence

A Specialist child is terminal only when:

- its report is returned;
- any authorized mutation is complete;
- required evidence references are attached;
- resource claims are released;
- its terminal status is persisted.

A parent cannot terminally converge while a mandatory Specialist remains active.

## Schemas

Machine-readable contracts:

- `11_CONTRACTS/schemas/specialist-problem-pack.schema.json`
- `11_CONTRACTS/schemas/specialist-report.schema.json`
