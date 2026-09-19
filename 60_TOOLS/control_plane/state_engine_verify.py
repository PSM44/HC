from __future__ import annotations

import importlib.util
import sys
import tempfile
from pathlib import Path


HERE = Path(__file__).resolve().parent

spec = importlib.util.spec_from_file_location(
    "state_engine",
    HERE / "state_engine.py",
)
module = importlib.util.module_from_spec(spec)
assert spec.loader is not None
sys.modules[spec.name] = module
spec.loader.exec_module(module)


def must_fail(fn, marker):
    try:
        fn()
    except module.StateTransitionError:
        print(f"{marker}=PASS")
        return
    raise SystemExit(f"{marker}=FAIL")


with tempfile.TemporaryDirectory() as tmp:
    path = Path(tmp) / "state.json"
    store = module.StateStore(path)

    created = store.create_attempt(
        issue_id="I1",
        attempt_id="A1",
    )
    assert created["state"] == "CREATED"

    store.transition(
        issue_id="I1",
        attempt_id="A1",
        expected_state="CREATED",
        new_state="ELIGIBLE",
        reason_code="DEPENDENCIES_SATISFIED",
        actor_role="RORCH",
    )

    store.transition(
        issue_id="I1",
        attempt_id="A1",
        expected_state="ELIGIBLE",
        new_state="RUNNING",
        reason_code="DISPATCHED",
        actor_role="RORCH",
    )

    must_fail(
        lambda: store.transition(
            issue_id="I1",
            attempt_id="A1",
            expected_state="ELIGIBLE",
            new_state="PASS",
            reason_code="STALE",
            actor_role="RORCH",
        ),
        "P2_STALE_STATE_REJECTED",
    )

    must_fail(
        lambda: store.transition(
            issue_id="OTHER",
            attempt_id="A1",
            expected_state="RUNNING",
            new_state="PASS",
            reason_code="BAD_IDENTITY",
            actor_role="RORCH",
        ),
        "P2_IDENTITY_MISMATCH_REJECTED",
    )

    must_fail(
        lambda: store.transition(
            issue_id="I1",
            attempt_id="A1",
            expected_state="RUNNING",
            new_state="CREATED",
            reason_code="INVALID_BACKWARD",
            actor_role="RORCH",
        ),
        "P2_INVALID_TRANSITION_REJECTED",
    )

    final = store.load()
    assert final["attempts"]["A1"]["state"] == "RUNNING"

print("P2_STATE_ENGINE_VERIFY=PASS")
