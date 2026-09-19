from __future__ import annotations

import json
from dataclasses import dataclass
from pathlib import Path
from typing import Any


ROOT = Path("/home/aazcl/repos/HC")
SCHEMA_DIR = ROOT / "11_CONTRACTS" / "schemas"

ROLE_ORDER = {
    "HUMAN": 5,
    "MORCH": 4,
    "RORCH": 3,
    "EXECUTOR": 2,
    "SPECIALIST": 2,
    "TESTER": 2,
    "VERIFIER": 2,
}


class ContractViolation(ValueError):
    pass


@dataclass(frozen=True)
class ValidationResult:
    valid: bool
    contract_type: str


def _load_schema(name: str) -> dict[str, Any]:
    return json.loads(
        (SCHEMA_DIR / name).read_text(encoding="utf-8")
    )


def _require_schema_minimum(
    payload: dict[str, Any],
    schema: dict[str, Any],
) -> None:
    if not isinstance(payload, dict):
        raise ContractViolation("payload-not-object")

    allowed = set(schema["properties"])
    required = set(schema["required"])

    missing = required - set(payload)
    if missing:
        raise ContractViolation(
            "missing-required:" + ",".join(sorted(missing))
        )

    extra = set(payload) - allowed
    if schema.get("additionalProperties") is False and extra:
        raise ContractViolation(
            "additional-properties:" + ",".join(sorted(extra))
        )

    for key, spec in schema["properties"].items():
        if key not in payload:
            continue
        if "const" in spec and payload[key] != spec["const"]:
            raise ContractViolation(f"const-mismatch:{key}")


def validate_task_envelope(
    payload: dict[str, Any],
) -> ValidationResult:
    schema = _load_schema("task-envelope.schema.json")
    _require_schema_minimum(payload, schema)

    if not payload["task_id"]:
        raise ContractViolation("empty-task-id")

    if not payload["issue_id"]:
        raise ContractViolation("empty-issue-id")

    if not payload["attempt_id"]:
        raise ContractViolation("empty-attempt-id")

    if not payload["work_unit_ids"]:
        raise ContractViolation("no-work-units")

    chain = payload["authority_chain"]

    if len(chain) < 2:
        raise ContractViolation("authority-chain-too-short")

    for role in chain:
        if role not in ROLE_ORDER:
            raise ContractViolation(
                f"unknown-authority-role:{role}"
            )

    for parent, child in zip(chain, chain[1:]):
        if ROLE_ORDER[parent] < ROLE_ORDER[child]:
            raise ContractViolation(
                f"authority-escalation:{parent}->{child}"
            )

    frc = payload["final_return_contract"]

    if frc.get("single_final_envelope") is not True:
        raise ContractViolation(
            "single-final-envelope-required"
        )

    if frc.get("delta_only") is not True:
        raise ContractViolation("delta-only-required")

    if frc.get("terminal_convergence_required") is not True:
        raise ContractViolation(
            "terminal-convergence-required"
        )

    return ValidationResult(
        valid=True,
        contract_type="TaskEnvelope",
    )


def validate_work_unit(
    payload: dict[str, Any],
) -> ValidationResult:
    schema = _load_schema("work-unit.schema.json")
    _require_schema_minimum(payload, schema)

    delegator = payload["delegated_by_role"]
    assignee = payload["assigned_role"]

    if delegator not in ROLE_ORDER or assignee not in ROLE_ORDER:
        raise ContractViolation("unknown-role")

    if ROLE_ORDER[delegator] < ROLE_ORDER[assignee]:
        raise ContractViolation(
            f"authority-escalation:{delegator}->{assignee}"
        )

    if payload["delegation_version"] < 1:
        raise ContractViolation("invalid-delegation-version")

    permissions = payload["permissions"]
    scope = payload["mutation_scope"]

    if permissions["canonical_mutation"] is False and scope:
        raise ContractViolation(
            "mutation-scope-without-canonical-authority"
        )

    if permissions["canonical_mutation"] is True and not scope:
        raise ContractViolation(
            "canonical-mutation-requires-explicit-scope"
        )

    criteria = payload["acceptance_criteria"]

    ids = [x["criterion_id"] for x in criteria]
    if len(ids) != len(set(ids)):
        raise ContractViolation(
            "duplicate-acceptance-criterion-id"
        )

    terminal = payload["terminal_return_contract"]

    if terminal.get("delta_only") is not True:
        raise ContractViolation("delta-only-required")

    if terminal.get("terminal_convergence_required") is not True:
        raise ContractViolation(
            "terminal-convergence-required"
        )

    return ValidationResult(
        valid=True,
        contract_type="WorkUnit",
    )
