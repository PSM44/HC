# HC Architecture & Governance Baseline

VERSION: v1.0-STRUCTURAL
STATUS: STRUCTURAL_BASELINE_CANONICAL

## Structural bootstrap

The following architectural fronts are canonical:

- A — North Star / Architecture Intent
- B — Capability Map
- C — Role / Authority
- D — Task / Work Unit Contracts
- E — Tester / Verifier / Evidence
- F — Issue / Attempt State
- G — Specialist Escalation
- H — Parallel DAG / Resource Ownership
- I — Technology Selection Framework
- J — Technology Registry / Watch
- K — Runtime / Repository Boundary

## Meaning of this milestone

`STRUCTURAL_BASELINE_CANONICAL` means HC now has a coherent architecture and
contract baseline sufficient to drive implementation.

It does NOT mean:

- HC is autonomous;
- runtime enforcement exists for all contracts;
- checkpoint/resume is proven;
- observability is complete;
- MORCH can directly execute canonical WSL2 work;
- an end-to-end autonomous chain has passed;
- terminal convergence has been proven system-wide.

## Next phase

Phase:

`IMPLEMENTATION`

Canonical active roadmap:

`04_BACKLOGS/HC.ROADMAP.ACTIVE.md`

Initial safe parallel frontier:

- P1 Contract Enforcement Runtime
- P2 State Transition Engine
- P6 TraceContext + Failure Taxonomy
- P8 MORCH → RORCH → WSL2 Runtime Bridge
- P12 Technology Research / ADR Pipeline

## North Star

North Star status:

`NOT_YET_PROVEN`

The North Star requires operational autonomous-chain proof and regression /
terminal-convergence proof, not merely architectural completeness.

## HEAD authority

Git is authoritative for live HEAD.

Canonical files use:

`HEAD_POLICY=RESOLVE_LIVE_FROM_GIT`
