from __future__ import annotations

import json
import os
import subprocess
import sys
from pathlib import Path
from typing import Any


ROOT = Path("/home/aazcl/repos/HC")

ADAPTER = (
    ROOT
    / "60_TOOLS"
    / "openclaw_adapter"
    / "status_adapter.py"
)

OPENCLAW_PREFIX = (
    Path.home()
    / ".local"
    / "share"
    / "hc"
    / "openclaw"
    / "2026.9.5"
)


def git_status() -> str:
    result = subprocess.run(
        [
            "git",
            "-C",
            str(ROOT),
            "status",
            "--porcelain",
            "--untracked-files=all",
        ],
        check=True,
        capture_output=True,
        text=True,
    )

    return result.stdout


def process_snapshot() -> list[str]:
    result = subprocess.run(
        [
            "pgrep",
            "-af",
            str(OPENCLAW_PREFIX),
        ],
        capture_output=True,
        text=True,
    )

    if result.returncode not in (0, 1):
        raise RuntimeError(
            f"pgrep failed: rc={result.returncode}"
        )

    return sorted(
        line
        for line in result.stdout.splitlines()
        if line.strip()
    )


def run_adapter() -> dict[str, Any]:
    env = os.environ.copy()

    env["HC_OPENCLAW_VERSION"] = "2026.9.5"
    env["HC_OPENCLAW_BIN"] = str(
        OPENCLAW_PREFIX / "bin" / "openclaw"
    )

    result = subprocess.run(
        [
            sys.executable,
            str(ADAPTER),
        ],
        cwd=ROOT,
        env=env,
        capture_output=True,
        text=True,
        timeout=45,
    )

    if result.returncode != 0:
        raise RuntimeError(
            "Adapter failed: "
            f"rc={result.returncode}; "
            f"stderr={result.stderr.strip()}"
        )

    stdout = result.stdout.strip()

    if "---AI_START---" in stdout:
        raise RuntimeError(
            "Adapter emitted forbidden AI_START marker"
        )

    if "---AI_END---" in stdout:
        raise RuntimeError(
            "Adapter emitted forbidden AI_END marker"
        )

    try:
        payload = json.loads(stdout)
    except json.JSONDecodeError as exc:
        raise RuntimeError(
            "Adapter returned non-JSON stdout"
        ) from exc

    return payload


def validate(payload: dict[str, Any]) -> None:
    expected_top = {
        "ADAPTER",
        "ADAPTER_STATUS",
        "OPERATION",
        "UPSTREAM",
        "MUTATION_PERFORMED",
    }

    if set(payload) != expected_top:
        raise RuntimeError(
            "Unexpected adapter contract keys"
        )

    if payload["ADAPTER"] != "HC_OPENCLAW_STATUS":
        raise RuntimeError(
            "Unexpected adapter identity"
        )

    if payload["ADAPTER_STATUS"] != "PASS":
        raise RuntimeError(
            "Adapter status is not PASS"
        )

    if payload["OPERATION"] != "STATUS":
        raise RuntimeError(
            "Unexpected operation"
        )

    if payload["MUTATION_PERFORMED"] is not False:
        raise RuntimeError(
            "Adapter reported mutation"
        )

    upstream = payload["UPSTREAM"]

    required_upstream = {
        "PRODUCT",
        "EXPECTED_VERSION",
        "OBSERVED_VERSION",
        "RC",
        "JSON",
        "STDERR_NONEMPTY",
    }

    if set(upstream) != required_upstream:
        raise RuntimeError(
            "Unexpected upstream contract keys"
        )

    if upstream["PRODUCT"] != "OpenClaw":
        raise RuntimeError(
            "Unexpected upstream product"
        )

    if upstream["EXPECTED_VERSION"] != "2026.9.5":
        raise RuntimeError(
            "Unexpected expected version"
        )

    if "2026.9.5" not in upstream["OBSERVED_VERSION"]:
        raise RuntimeError(
            "Observed OpenClaw version mismatch"
        )

    if not isinstance(upstream["RC"], int):
        raise RuntimeError(
            "Upstream RC must be integer"
        )

    if not isinstance(upstream["JSON"], dict):
        raise RuntimeError(
            "Upstream JSON must be object"
        )


def emit_final() -> None:
    payload = {
        "TASK_ID": "HC-E05-PHASE4",
        "STATUS": "PASS",
        "DELTA": {
            "OPENCLAW_ADAPTER_SEAM": "VERIFIED",
            "HC_NORMALIZED_CONTRACT": "VERIFIED",
            "UPSTREAM_STATUS_JSON": "VERIFIED",
            "ISOLATED_EXECUTION": "VERIFIED",
            "NO_HC_MUTATION": "VERIFIED",
            "NO_PERSISTENT_PROCESS": "VERIFIED",
            "FINAL_ENVELOPE_BOUNDARY": "VERIFIED",
        },
        "TERMINAL_CONVERGENCE": True,
    }

    print("---AI_START---")
    print(
        json.dumps(
            payload,
            sort_keys=True,
            separators=(",", ":"),
        )
    )
    print("---AI_END---")


def main() -> None:
    repo_before = git_status()
    processes_before = process_snapshot()

    first = run_adapter()
    validate(first)

    second = run_adapter()
    validate(second)

    repo_after = git_status()
    processes_after = process_snapshot()

    if repo_before != repo_after:
        raise RuntimeError(
            "Adapter execution changed HC repository"
        )

    if processes_before != processes_after:
        raise RuntimeError(
            "OpenClaw process set did not converge"
        )

    first_contract = {
        key: first[key]
        for key in (
            "ADAPTER",
            "ADAPTER_STATUS",
            "OPERATION",
            "MUTATION_PERFORMED",
        )
    }

    second_contract = {
        key: second[key]
        for key in (
            "ADAPTER",
            "ADAPTER_STATUS",
            "OPERATION",
            "MUTATION_PERFORMED",
        )
    }

    if first_contract != second_contract:
        raise RuntimeError(
            "Adapter contract is not stable"
        )

    emit_final()


if __name__ == "__main__":
    main()
