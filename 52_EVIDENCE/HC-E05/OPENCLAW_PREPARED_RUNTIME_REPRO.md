# HC-E05 — OpenClaw 2026.9.5 Prepared Runtime Reproduction

## Classification

UPSTREAM_REPRODUCIBLE_DEFECT_CANDIDATE

Likely layer:

`prepared runtime / plugin generation consistency`

## Environment

- OpenClaw: 2026.9.5
- Codex plugin: official `@openclaw/codex` 2026.9.5
- Primary provider/model: `openai/gpt-6-astra`
- Primary auth profile: `openai:psanmartin`
- Auth status: usable
- Model inference performed during diagnosis: no

## Observed contradiction

Runtime inspection reports Codex as:

- installed
- loaded
- enabled
- activated
- official/trusted
- agent harness `codex` registered by inspection
- plugin doctor clean

However:

`openclaw models status --json --check`

returns:

- exit code 1
- runtimeStatus = unavailable
- runtimeReason = owner-plugin-not-activatable
- runtimeDetail = No enabled plugin owns agent harness "codex".

## Repair attempts already executed

1. Canonical `models set openai/gpt-6-astra`
   - invokes OpenClaw's Codex runtime-plugin repair seam
   - no resolution

2. `plugins registry --refresh`
   - registry changed
   - no resolution

No plugin reinstall and no broad `doctor --fix` were executed.

## Upstream correlation

Related OpenClaw issue:

`#140393`

Related fix:

`98e5590a999ddded4d6c9534234075e47616500f`

The fix is already contained in OpenClaw `v2026.9.5`.

No issue matching both OpenClaw 2026.9.5 and this exact
`owner-plugin-not-activatable` reproduction was found during duplicate search.

## HC conclusion

Local configuration/auth/model/plugin-install causes have been eliminated to
a sufficient degree for this PoC.

Further local repair churn is stopped.

Next step:

prepare a sanitized upstream defect report; publication requires HUMAN
authorization.
