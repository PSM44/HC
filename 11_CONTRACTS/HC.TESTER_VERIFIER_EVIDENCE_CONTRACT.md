# HC Tester / Verifier / Evidence Contract

STATUS: BOOTSTRAP_BASELINE
FRONT: E
CONTRACT_VERSION: hc.test-verification.v0.1

## Purpose

This contract separates three concerns that MUST NOT be conflated:

1. TESTER execution and observation;
2. EVIDENCE as durable factual output;
3. VERIFIER evaluation and decision.

A successful test command alone is not equivalent to verification.

## TESTER

The TESTER owns:

- execution of delegated tests;
- observation of system behavior;
- capture of raw results;
- normalization of test results;
- production of TestEvidence.

The TESTER does not own:

- implementation repair;
- acceptance of its own evidence;
- project-level completion;
- mutation outside explicitly delegated test scope.

A TESTER may report PASS for an individual test observation.

That does not imply the WorkUnit or TaskEnvelope is verified.

## VERIFIER

The VERIFIER owns:

- acceptance-criterion evaluation;
- invariant evaluation;
- evidence sufficiency evaluation;
- provenance evaluation;
- contradiction detection;
- VerificationResult production.

The VERIFIER MUST NOT:

- silently repair implementation;
- synthesize missing evidence and then verify it;
- convert UNKNOWN into PASS;
- ignore contradictory evidence;
- expand acceptance criteria after observing results.

Where a verification condition cannot be established, the result is not PASS.

## Evidence

Evidence is a durable observation or artifact supporting a factual claim.

Evidence MUST have:

- EVIDENCE_ID;
- ISSUE_ID;
- ATTEMPT;
- producer role;
- producer identity;
- evidence type;
- observed subject;
- result/status;
- provenance;
- creation sequence or timestamp;
- sensitivity;
- persistence classification;
- integrity metadata where applicable.

Evidence SHOULD reference:

- TASK_ID;
- WORK_UNIT_ID;
- acceptance criterion IDs;
- source artifact;
- command/test identifier;
- parent evidence when derived.

## Raw vs normalized evidence

Raw evidence is the closest retained representation of what was directly
observed.

Normalized evidence converts raw evidence into a stable HC contract.

Normalization MUST NOT alter the substantive result.

Derived evidence MUST retain provenance back to its source.

## Evidence statuses

Evidence may report observational states such as:

- PASS
- FAIL
- ERROR
- SKIPPED
- NOT_RUN
- UNKNOWN

Evidence status is not VerificationResult status.

## VerificationResult

VerificationResult is an evaluative decision over identified evidence and
criteria.

Allowed statuses:

- PASS
- FAIL
- BLOCKED
- INSUFFICIENT_EVIDENCE
- CONTRADICTORY_EVIDENCE

PASS requires:

- all mandatory criteria evaluated;
- required evidence present;
- evidence provenance acceptable;
- required invariants satisfied;
- no unresolved material contradiction;
- no required criterion remaining UNKNOWN.

## Acceptance criteria

Verification operates only on declared acceptance criteria and invariants.

Each evaluated criterion records:

- criterion ID;
- verdict;
- evidence references;
- rationale/reason code.

The VERIFIER may identify that criteria are incomplete or invalid.

It may not silently rewrite them.

A new or changed criterion requires authorized delegation/versioning.

## Independence

Independent verification means the verification decision is not controlled by
the actor whose implementation result is being evaluated.

Distinct role semantics are mandatory even if one physical product temporarily
implements multiple roles.

At minimum:

- EXECUTOR implementation state;
- TESTER evidence-production state;
- VERIFIER decision state

must remain logically distinguishable.

## Evidence sensitivity

Sensitivity classifications:

- PUBLIC
- INTERNAL
- SENSITIVE
- SECRET

Evidence persistence policy MUST respect sensitivity.

SECRET evidence MUST NOT be committed to canonical Git storage.

The canonical repository may retain metadata or sanitized evidence references
without retaining the secret itself.

## Persistence

Evidence requirements in the WorkUnit determine whether evidence must persist.

Persisted evidence should be immutable or append-only where practical.

Replacing evidence under the same EVIDENCE_ID is prohibited unless the contract
explicitly identifies a new version/revision.

## Contradiction handling

When evidence sources materially disagree:

1. verification MUST stop short of PASS;
2. the contradiction MUST be recorded;
3. provenance MUST remain available;
4. additional testing or investigation may be requested.

Narrative preference cannot resolve contradictory factual evidence.

## Terminal convergence

A WorkUnit requiring verification cannot terminally converge as PASS until:

- required TESTER work is terminal;
- required evidence exists;
- VERIFIER is terminal;
- VerificationResult is PASS;
- required evidence/state persistence is complete.

A parent TaskEnvelope cannot emit final PASS while required verification remains
active, missing or contradictory.

## Schemas

Machine-readable schemas:

- `11_CONTRACTS/schemas/test-evidence.schema.json`
- `11_CONTRACTS/schemas/verification-result.schema.json`

JSON Schema validates structure.

HC control-plane logic must enforce semantic independence, provenance,
contradiction handling and authority.
