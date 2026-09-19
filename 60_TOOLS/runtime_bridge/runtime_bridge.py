from __future__ import annotations

import json
import os
import subprocess
from pathlib import Path


ROOT = Path("/home/aazcl/repos/HC")


def _git(*args: str) -> str:
    return subprocess.run(
        ["git", "-C", str(ROOT), *args],
        check=True,
        capture_output=True,
        text=True,
    ).stdout.strip()


def bridge_status() -> dict[str, object]:
    transport = os.environ.get(
        "HC_RUNTIME_BRIDGE_TRANSPORT"
    )

    return {
        "schema": "hc.runtime-bridge-status.v0.1",
        "canonical_root": str(ROOT),
        "branch_observed": _git(
            "branch",
            "--show-current",
        ),
        "head_observed": _git(
            "rev-parse",
            "HEAD",
        ),
        "worktree_clean": (
            _git("status", "--porcelain") == ""
        ),
        "transport_configured": bool(transport),
        "transport_name": transport,
        "execution_ready": bool(transport),
        "mutation_performed": False,
    }


def main() -> None:
    print(
        json.dumps(
            bridge_status(),
            sort_keys=True,
            separators=(",", ":"),
        )
    )


if __name__ == "__main__":
    main()
