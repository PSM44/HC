from __future__ import annotations

import json
import subprocess
import sys
from pathlib import Path
from typing import Any

ROOT = Path("/home/aazcl/repos/HC")
TOOLS_DIR = ROOT / "60_TOOLS" / "mcp_control"

POSITIVE = TOOLS_DIR / "smoke.py"
NEGATIVE = TOOLS_DIR / "failure_smoke.py"


def run_child(path: Path) -> dict[str, Any]:
    result = subprocess.run(
        [sys.executable, str(path)],
        cwd=ROOT,
        capture_output=True,
        text=True,
    )

    if result.returncode != 0:
        raise RuntimeError(
            f"{path.name} failed: rc={result.returncode}; "
            f"stderr={result.stderr.strip()}"
        )

    stdout = result.stdout.strip()

    if not stdout:
        raise RuntimeError(f"{path.name} returned empty stdout")

    if "---AI_START---" in stdout or "---AI_END---" in stdout:
        raise RuntimeError(
            f"{path.name} emitted forbidden final-envelope markers"
        )

    try:
        payload = json.loads(stdout)
    except json.JSONDecodeError as exc:
        raise RuntimeError(
            f"{path.name} returned non-JSON stdout"
        ) from exc

    if payload.get("STATUS") != "PASS":
        raise RuntimeError(
            f"{path.name} returned non-PASS status"
        )

    if payload.get("MUTATION_PERFORMED") is not False:
        raise RuntimeError(
            f"{path.name} reported mutation"
        )

    return payload


def git_status() -> str:
    result = subprocess.run(
        ["git", "-C", str(ROOT), "status", "--porcelain"],
        check=True,
        capture_output=True,
        text=True,
    )
    return result.stdout


def emit_final(payload: dict[str, Any]) -> None:
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

    positive = run_child(POSITIVE)
    negative = run_child(NEGATIVE)

    repo_after = git_status()

    if repo_before != repo_after:
        raise RuntimeError(
            "Task verification changed repository state"
        )

    required_positive = {
        "DISCOVERY",
        "PROJECT_STATE",
        "CAPABILITIES",
        "DAG",
        "READ_ONLY_ROUNDTRIP",
    }

    if set(positive["CHECKS"]) != required_positive:
        raise RuntimeError("Unexpected positive check set")

    if any(
        positive["CHECKS"][key] != "PASS"
        for key in required_positive
    ):
        raise RuntimeError("Positive validation incomplete")

    required_negative = {
        "STRICT_INPUT_SCHEMA",
        "VALID_TOOL",
        "UNKNOWN_TOOL",
        "INVALID_ARGUMENTS",
        "NO_CANONICAL_MUTATION",
    }

    if set(negative["CHECKS"]) != required_negative:
        raise RuntimeError("Unexpected negative check set")

    if any(
        negative["CHECKS"][key] != "PASS"
        for key in required_negative
    ):
        raise RuntimeError("Negative validation incomplete")

    emit_final(
        {
            "TASK_ID": "HC-E04-R4",
            "STATUS": "PASS",
            "DELTA": {
                "FINAL_ENVELOPE_BOUNDARY": "VERIFIED",
                "MCP_POSITIVE_PATH": "VERIFIED",
                "STRICT_INPUT_CONTRACT": "VERIFIED",
                "FAIL_CLOSED": "VERIFIED",
                "NO_CANONICAL_MUTATION": "VERIFIED",
            },
            "TERMINAL_CONVERGENCE": True,
        }
    )


if __name__ == "__main__":
    main()
