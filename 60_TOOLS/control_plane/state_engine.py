from __future__ import annotations

import json
import os
import tempfile
from dataclasses import dataclass
from pathlib import Path
from typing import Any


ATTEMPT_TRANSITIONS = {
    "CREATED": {"ELIGIBLE", "CANCELLED", "SUPERSEDED"},
    "ELIGIBLE": {"RUNNING", "WAITING", "BLOCKED", "CANCELLED", "SUPERSEDED"},
    "RUNNING": {
        "WAITING",
        "RETRY_PENDING",
        "BLOCKED",
        "FAILED",
        "TESTING",
        "VERIFYING",
        "PASS",
        "CANCELLED",
        "SUPERSEDED",
    },
    "WAITING": {
        "ELIGIBLE",
        "RUNNING",
        "BLOCKED",
        "CANCELLED",
        "SUPERSEDED",
    },
    "RETRY_PENDING": {
        "ELIGIBLE",
        "FAILED",
        "CANCELLED",
        "SUPERSEDED",
    },
    "TESTING": {
        "VERIFYING",
        "FAILED",
        "BLOCKED",
        "CANCELLED",
        "SUPERSEDED",
    },
    "VERIFYING": {
        "PASS",
        "FAILED",
        "BLOCKED",
        "CANCELLED",
        "SUPERSEDED",
    },
    "BLOCKED": {
        "ELIGIBLE",
        "CANCELLED",
        "SUPERSEDED",
    },
    "FAILED": set(),
    "PASS": set(),
    "SUPERSEDED": set(),
    "CANCELLED": set(),
}

TERMINAL = {
    "FAILED",
    "PASS",
    "SUPERSEDED",
    "CANCELLED",
}


class StateTransitionError(ValueError):
    pass


@dataclass(frozen=True)
class Transition:
    issue_id: str
    attempt_id: str
    previous_state: str
    new_state: str
    reason_code: str
    actor_role: str
    sequence: int
    evidence_ref: str | None = None


def validate_transition(
    current: str,
    new: str,
) -> None:
    if current not in ATTEMPT_TRANSITIONS:
        raise StateTransitionError(
            f"unknown-current-state:{current}"
        )

    if new not in ATTEMPT_TRANSITIONS:
        raise StateTransitionError(
            f"unknown-new-state:{new}"
        )

    if new not in ATTEMPT_TRANSITIONS[current]:
        raise StateTransitionError(
            f"invalid-transition:{current}->{new}"
        )


class StateStore:
    def __init__(self, path: Path):
        self.path = path

    def load(self) -> dict[str, Any]:
        if not self.path.exists():
            return {
                "schema": "hc.attempt-store.v0.1",
                "attempts": {},
                "sequence": 0,
            }
        return json.loads(
            self.path.read_text(encoding="utf-8")
        )

    def save(self, payload: dict[str, Any]) -> None:
        self.path.parent.mkdir(
            parents=True,
            exist_ok=True,
        )

        fd, temp_name = tempfile.mkstemp(
            dir=str(self.path.parent),
            prefix=self.path.name + ".",
            suffix=".tmp",
        )

        try:
            with os.fdopen(fd, "w", encoding="utf-8") as handle:
                json.dump(
                    payload,
                    handle,
                    indent=2,
                    sort_keys=True,
                )
                handle.write("\n")
                handle.flush()
                os.fsync(handle.fileno())

            os.replace(temp_name, self.path)
        finally:
            if os.path.exists(temp_name):
                os.unlink(temp_name)

    def create_attempt(
        self,
        *,
        issue_id: str,
        attempt_id: str,
    ) -> dict[str, Any]:
        state = self.load()

        if attempt_id in state["attempts"]:
            raise StateTransitionError(
                f"attempt-already-exists:{attempt_id}"
            )

        state["sequence"] += 1

        state["attempts"][attempt_id] = {
            "issue_id": issue_id,
            "attempt_id": attempt_id,
            "state": "CREATED",
            "sequence": state["sequence"],
            "history": [],
        }

        self.save(state)
        return state["attempts"][attempt_id]

    def transition(
        self,
        *,
        issue_id: str,
        attempt_id: str,
        expected_state: str,
        new_state: str,
        reason_code: str,
        actor_role: str,
        evidence_ref: str | None = None,
    ) -> Transition:
        state = self.load()

        attempt = state["attempts"].get(attempt_id)
        if attempt is None:
            raise StateTransitionError(
                f"unknown-attempt:{attempt_id}"
            )

        if attempt["issue_id"] != issue_id:
            raise StateTransitionError(
                "issue-attempt-identity-mismatch"
            )

        if attempt["state"] != expected_state:
            raise StateTransitionError(
                "stale-attempt-state:"
                f"expected={expected_state}:"
                f"observed={attempt['state']}"
            )

        validate_transition(
            attempt["state"],
            new_state,
        )

        state["sequence"] += 1

        event = {
            "issue_id": issue_id,
            "attempt_id": attempt_id,
            "previous_state": attempt["state"],
            "new_state": new_state,
            "reason_code": reason_code,
            "actor_role": actor_role,
            "sequence": state["sequence"],
            "evidence_ref": evidence_ref,
        }

        attempt["history"].append(event)
        attempt["state"] = new_state
        attempt["sequence"] = state["sequence"]

        self.save(state)

        return Transition(**event)
