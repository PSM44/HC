from __future__ import annotations

import copy
import importlib.util
import sys
from pathlib import Path


HERE = Path(__file__).resolve().parent

spec = importlib.util.spec_from_file_location(
    "contract_enforcer",
    HERE / "contract_enforcer.py",
)
module = importlib.util.module_from_spec(spec)
assert spec.loader is not None
sys.modules[spec.name] = module
spec.loader.exec_module(module)

ContractViolation = module.ContractViolation


TASK = {
    "contract_version": "hc.task-envelope.v0.1",
    "task_id": "T1",
    "issue_id": "I1",
    "attempt_id": "A1",
    "objective": "verify contract enforcement",
    "authority_chain": [
        "HUMAN",
        "MORCH",
        "RORCH",
        "EXECUTOR",
    ],
    "work_unit_ids": ["W1"],
    "required_terminal_states": ["PASS"],
    "final_return_contract": {
        "format": "HC_MACHINE_ENVELOPE",
        "single_final_envelope": True,
        "delta_only": True,
        "terminal_convergence_required": True,
    },
    "canonical_state_persistence_required": True,
}

WORK = {
    "contract_version": "hc.work-unit.v0.1",
    "work_unit_id": "W1",
    "task_id": "T1",
    "issue_id": "I1",
    "attempt_id": "A1",
    "delegation_version": 1,
    "delegated_by_role": "RORCH",
    "assigned_role": "EXECUTOR",
    "objective": "bounded write",
    "dependencies": [],
    "resource_claims": [
        {
            "resource_id": "repo:HC",
            "access": "WRITE",
            "scope": "60_TOOLS/example.py",
        }
    ],
    "permissions": {
        "filesystem_read": True,
        "filesystem_write": True,
        "process_execution": True,
        "network_access": False,
        "credential_use": False,
        "canonical_mutation": True,
        "external_publication": False,
    },
    "mutation_scope": [
        "60_TOOLS/example.py"
    ],
    "acceptance_criteria": [
        {
            "criterion_id": "AC1",
            "statement": "file created",
            "verification_required": True,
        }
    ],
    "evidence_requirements": [],
    "retry_policy": {
        "max_attempts": 1,
        "retryable_failure_classes": [],
        "backoff": "NONE",
        "idempotency_required": True,
        "checkpoint_rule": "NONE",
        "escalation_after_attempt": None,
    },
    "terminal_return_contract": {
        "delta_only": True,
        "evidence_refs_required": True,
        "terminal_convergence_required": True,
    },
}


def must_fail(payload, fn, marker):
    try:
        fn(payload)
    except ContractViolation:
        print(f"{marker}=PASS")
        return
    raise SystemExit(f"{marker}=FAIL")


assert module.validate_task_envelope(TASK).valid
assert module.validate_work_unit(WORK).valid

bad = copy.deepcopy(WORK)
bad["permissions"]["canonical_mutation"] = False
must_fail(
    bad,
    module.validate_work_unit,
    "P1_FAIL_CLOSED_MUTATION_AUTHORITY",
)

bad = copy.deepcopy(WORK)
bad["mutation_scope"] = []
must_fail(
    bad,
    module.validate_work_unit,
    "P1_FAIL_CLOSED_EMPTY_MUTATION_SCOPE",
)

bad = copy.deepcopy(TASK)
bad["authority_chain"] = [
    "RORCH",
    "MORCH",
]
must_fail(
    bad,
    module.validate_task_envelope,
    "P1_FAIL_CLOSED_AUTHORITY_ESCALATION",
)

bad = copy.deepcopy(TASK)
bad["unexpected"] = True
must_fail(
    bad,
    module.validate_task_envelope,
    "P1_FAIL_CLOSED_ADDITIONAL_PROPERTIES",
)

print("P1_CONTRACT_ENFORCEMENT_VERIFY=PASS")
