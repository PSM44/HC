from __future__ import annotations

import json
import subprocess
from pathlib import Path
from typing import Any

from mcp.server import MCPServer

ROOT = Path("/home/aazcl/repos/HC")
STATE_FILE = ROOT / "12_STATE" / "HC.CURRENT_STATE.json"

mcp = MCPServer(
    "HC Control",
    instructions=(
        "Read-only Harness Council control-plane PoC. "
        "No tool exposed by this server may mutate canonical state."
    ),
)


def _git(*args: str) -> str:
    result = subprocess.run(
        ["git", "-C", str(ROOT), *args],
        check=True,
        capture_output=True,
        text=True,
    )
    return result.stdout.strip()


@mcp.tool()
def hc_get_project_state() -> dict[str, Any]:
    """Return observed read-only HC project and Git state."""
    canonical_state = json.loads(STATE_FILE.read_text(encoding="utf-8"))

    return {
        "project_id": "HC",
        "canonical_root": str(ROOT),
        "branch_observed": _git("branch", "--show-current"),
        "head_observed": _git("rev-parse", "HEAD"),
        "remote_origin": _git("remote", "get-url", "origin"),
        "worktree_clean": _git("status", "--porcelain") == "",
        "canonical_state_document": canonical_state,
        "mutation_performed": False,
    }


@mcp.tool()
def hc_get_capabilities() -> dict[str, Any]:
    """Return the initial HC capability model."""
    return {
        "observation": [
            "REMOTE_CANONICAL_OBSERVATION",
            "LOCAL_STATE_OBSERVATION",
            "TELEMETRY_OBSERVABILITY",
        ],
        "execution": [
            "LOCAL_RUNTIME_EXECUTION",
        ],
        "provisioning": [
            "TOOLCHAIN_PROVISIONING",
        ],
        "communication": [
            "TOOL_PROTOCOL",
            "AGENT_HARNESS_PROTOCOL",
        ],
        "assurance": [
            "TESTING",
            "EVIDENCE",
            "VERIFICATION",
        ],
        "durability": [
            "CHECKPOINT",
            "RESUME",
            "LONG_RUNNING_WORKFLOW",
        ],
        "mutation_performed": False,
    }


@mcp.tool()
def hc_get_dag() -> dict[str, Any]:
    """Return the currently authorized high-level HC development DAG."""
    return {
        "policy": "PARALLEL_BY_DEFAULT",
        "active_fronts": [
            "A01",
            "B01",
            "C01",
            "F01",
            "I01",
            "K01",
        ],
        "enablement_path": [
            "HC-E01",
            "HC-E03",
            "HC-E04",
            "HC-E05",
            "HC-E07",
            "HC-E09",
        ],
        "dependencies": {
            "HC-E03": ["HC-E01"],
            "HC-E04": ["HC-E03"],
            "HC-E05": ["HC-E04"],
            "HC-E07": ["HC-E04"],
            "HC-E09": ["HC-E07"],
        },
        "mutation_performed": False,
    }


if __name__ == "__main__":
    mcp.run()
