# HC Capability Map

STATUS: BOOTSTRAP_BASELINE
FRONT: B

Capabilities are architectural requirements. Products and tools implement
capabilities; they do not define them.

## 1. Control Plane

Required capabilities:

- goal decomposition;
- DAG construction and dependency management;
- safe parallel scheduling;
- role and authority enforcement;
- work-unit delegation;
- resource ownership and conflict control;
- cancellation and supersession;
- retry/wait/block/failure semantics;
- terminal convergence;
- human authority gates.

## 2. Execution Plane

Required capabilities:

- heterogeneous harness invocation;
- local and remote execution;
- bounded filesystem/process/network permissions;
- provider/model routing;
- agent/subagent execution;
- specialist escalation;
- checkpoint/resume;
- long-running task supervision;
- deterministic return envelopes.

## 3. Quality and Evidence

Required capabilities:

- test execution;
- verifier evaluation;
- acceptance-criteria checking;
- invariant checking;
- evidence collection;
- evidence retention;
- provenance;
- reproducible diagnostics;
- regression testing;
- failure-matrix testing.

## 4. State and Recovery

Required capabilities:

- canonical current state;
- issue identity;
- durable attempt identity;
- state transitions;
- checkpoint persistence;
- recovery after process/runtime interruption;
- idempotent resume;
- stale-state detection;
- reconciliation before mutation.

## 5. Memory and Learning

Required capabilities:

- bounded project memory;
- runtime/session context;
- verified-learning ingestion;
- provenance and expiry;
- conflict detection;
- separation between observations, hypotheses and verified facts.

Only verified outputs may become durable learning.

## 6. Integration

Required capabilities:

- tool/resource/service integration;
- harness/client session integration;
- agent-to-agent communication where justified;
- protocol adapters;
- versioned contracts;
- replaceable providers.

Candidate protocols may include MCP, ACP and A2A, but protocol choice must remain
subordinate to architectural requirements.

## 7. Observability

Required capabilities:

- structured logs;
- traces;
- metrics;
- work-unit lifecycle visibility;
- parent/child correlation;
- issue/attempt correlation;
- runtime health;
- cost/usage visibility;
- failure classification;
- audit trail.

## 8. Technology Governance

Required capabilities:

- candidate registry;
- lifecycle state;
- deep research;
- ADRs;
- targeted PoCs;
- technology watch;
- security/licensing review;
- upgrade/reassessment policy;
- deprecation and replacement.

## 9. Security and Trust

Required capabilities:

- explicit trust boundaries;
- least privilege;
- credential isolation;
- secret non-propagation;
- execution sandboxing;
- mutation authorization;
- read-only/no-touch boundaries;
- external publication gates.

## Capability ownership rule

No candidate may become ACTIVE_OWNER merely because it is installed,
discoverable or functional.

The lifecycle must distinguish at least:

CANDIDATE
→ RESEARCHED
→ SELECTED_FOR_POC
→ IMPLEMENTED
→ VERIFIED
→ ACTIVE_OWNER

with REJECTED, DEFERRED, SUPERSEDED and RETIRED as valid terminal or side states.
