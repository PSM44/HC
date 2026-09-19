# HC Project Backlog — Active

STATUS: ACTIVE
ROADMAP: `04_BACKLOGS/HC.ROADMAP.ACTIVE.md`

## Structural bootstrap

A–K:

`CANONICALIZED`

This means the structural baseline is established.

It does not mean HC is operationally complete.

## Current phase

`IMPLEMENTATION`

## Current parallel frontier

- P1 — Contract Enforcement Runtime
- P2 — State Transition Engine
- P6 — TraceContext + Failure Taxonomy
- P8 — MORCH → RORCH → WSL2 Runtime Bridge
- P12 — Technology Research / ADR Pipeline

## Blocked downstream fronts

- P3 waits on P1
- P4 waits on P1
- P5 waits on P1 + P4
- P7 waits on P2 + P6
- P9 waits on P6
- P10 waits on P4 + P6
- P11 waits on core execution/runtime dependencies
- P13 waits on P11

## External candidate condition

OpenClaw HC-E05:

- IMPLEMENTED
- PARTIAL_VERIFIED
- ACTIVE_OWNER=NO
- local repair churn stopped
- upstream runtime defect candidate documented

OpenClaw is not a global HC blocker.

## Runtime bridge

`HC-BOOTSTRAP-RUNTIME-BRIDGE-001`

Status:

`OPEN_DEFERRED`

P8 now owns advancing this gap.
