# HC North Star and Architecture Intent

STATUS: BOOTSTRAP_BASELINE
FRONT: A
PROJECT: Harness Council

## North Star

HC shall become a modular, replaceable, evidence-driven autonomous multi-harness
system capable of long-running, iterative, multipath and resumable execution.

The system must coordinate heterogeneous execution runtimes without coupling
project authority, state truth or completion semantics to any single harness,
provider, model or protocol.

## Primary operating loop

GOALS
→ LOOPS
→ GRAPH/DAG
→ AGENTS/SUBAGENTS
→ CROSS_CHECK
→ TERMINAL_CONVERGENCE

## Architectural invariants

1. HUMAN authority remains above every automated role.
2. MORCH owns global orchestration intent and system-level decisions.
3. RORCH owns runtime orchestration within delegated authority.
4. EXECUTOR performs bounded work units and does not self-authorize scope growth.
5. SPECIALIST is lateral bounded escalation, never an orchestrator.
6. TESTER executes or observes tests and produces evidence.
7. VERIFIER decides whether acceptance criteria and invariants are satisfied.
8. Evidence precedes claims.
9. UNKNOWN is never interpreted as PASS.
10. Completion is prohibited while mandatory work, verification, retry,
    convergence or state persistence remains active.
11. Parallel execution is the default when dependencies and resource ownership
    permit it.
12. Canonical mutation requires explicit authority and deterministic scope.
13. Canonical state must not be inferred from narrative output.
14. Technologies are replaceable implementation details behind explicit
    boundaries.
15. Installation, selection, verification and active ownership are distinct
    lifecycle states.

## Non-goals

HC is not:

- a wrapper around one agent framework;
- a permanent commitment to OpenClaw, DSH, Codex or any other candidate;
- a tool tournament;
- an LLM-generated state database;
- a system where executors self-verify or self-promote completion;
- a collection of undocumented scripts;
- an architecture where HUMAN manually relays normal machine-to-machine traffic.

## Automation target

The intended steady-state human boundary is:

HUMAN ↔ MORCH

Normal interactions beneath MORCH should be automated. HUMAN intervention is
reserved for authority, irreversible risk, credential/security gates, policy,
material cost, external publication and other explicitly defined governance
boundaries.

## Convergence condition

HC reaches terminal convergence only when:

- required DAG nodes are terminal;
- no mandatory child or job remains active;
- tests and verification required by policy have completed;
- issue/attempt state is reconciled;
- canonical state is persisted;
- no unresolved contradiction exists between evidence and claimed status.
