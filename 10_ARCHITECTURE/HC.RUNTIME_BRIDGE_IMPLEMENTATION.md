# HC Runtime Bridge Implementation Boundary

STATUS: PARTIAL_IMPLEMENTATION
FRONT: P8

The runtime bridge owns the MORCH → RORCH → canonical WSL2 execution boundary.

Current executable artifact:

`60_TOOLS/runtime_bridge/runtime_bridge.py`

Current capability:

- observes canonical root;
- observes branch;
- observes HEAD;
- observes worktree cleanliness;
- reports whether an execution transport is configured;
- performs no canonical mutation.

Current limitation:

`HC_RUNTIME_BRIDGE_TRANSPORT` is not yet backed by an authorized transport in
this session.

Therefore:

`P8 != COMPLETE`

and:

`HUMAN_AS_RUNTIME_RELAY != ELIMINATED`

The bridge MUST fail closed rather than simulate execution.

Next P8 step is to select and verify an actual transport adapter preserving:

- request identity;
- ISSUE_ID / ATTEMPT;
- exact WorkUnit scope;
- cancellation;
- evidence return;
- mutation authority;
- terminal result.

Canonical request schema:

`11_CONTRACTS/schemas/runtime-bridge-request.schema.json`
