# HC Runtime and Repository Boundary

STATUS: BOOTSTRAP_BASELINE
FRONT: K

## Canonical repository

Canonical root:

`/home/aazcl/repos/HC`

Canonical runtime:

`WSL2 / kali-linux`

Canonical branch:

`main`

Remote:

`https://github.com/PSM44/HC.git`

## Windows access clone

Windows path:

`C:\01. GitHub\HC`

This clone is an access/transition surface. It is not the canonical mutation
root unless HUMAN explicitly changes that policy.

## Mutation authority

Canonical code/state mutations should execute against the canonical WSL2 root.

Remote GitHub observation may verify published state but is not equivalent to:

- local worktree observation;
- local process observation;
- local runtime execution;
- local filesystem mutation.

These capabilities must remain explicitly distinguished.

## Current control-plane gap

MORCH currently lacks a direct canonical execution bridge into the WSL2 root.

Until that bridge exists:

- HUMAN may temporarily operate exact fail-closed scripts;
- scripts must verify root, branch, HEAD and worktree;
- scripts must use exact staging;
- mutation scope must be explicit;
- results return as machine-oriented envelopes.

This is a temporary operating condition, not the target architecture.

## Runtime isolation principles

1. Shared toolchains should have an explicit owner.
2. Candidate-specific runtimes should be isolated until adoption.
3. System/global package mutation is avoided unless justified.
4. Credential stores must remain outside the repository.
5. Runtime caches are not canonical state.
6. Generated artifacts must not be confused with evidence.
7. Persistent services require explicit lifecycle ownership.
8. Rollback scope must be known before installation.

## Repository principles

The repository stores durable project truth:

- governance;
- architecture;
- contracts;
- state;
- research decisions;
- evidence;
- adapters and approved tooling.

The repository should not accumulate:

- secrets;
- transient caches;
- arbitrary logs;
- abandoned PoCs;
- duplicated state;
- cosmetic placeholder directories.

## Execution bridge target

Long-term target:

HUMAN
↕
MORCH
↕
RORCH
↕
canonical WSL2 execution
↕
EXECUTORS / SPECIALISTS / TESTERS / VERIFIERS

The bridge must preserve:

- identity;
- authority;
- ISSUE_ID / ATTEMPT;
- exact work-unit scope;
- evidence;
- cancellation;
- convergence;
- deterministic return.
