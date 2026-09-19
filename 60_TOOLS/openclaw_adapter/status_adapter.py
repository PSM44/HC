from __future__ import annotations

import json
import os
import subprocess
import tempfile
from pathlib import Path
from typing import Any


DEFAULT_VERSION = "2026.9.5"


def resolve_openclaw() -> tuple[Path, str]:
    version = os.environ.get(
        "HC_OPENCLAW_VERSION",
        DEFAULT_VERSION,
    )

    explicit = os.environ.get("HC_OPENCLAW_BIN")

    if explicit:
        binary = Path(explicit).expanduser().resolve()
    else:
        binary = (
            Path.home()
            / ".local"
            / "share"
            / "hc"
            / "openclaw"
            / version
            / "bin"
            / "openclaw"
        )

    if not binary.is_file():
        raise RuntimeError(
            f"OpenClaw binary not found: {binary}"
        )

    return binary, version


def verify_version(
    binary: Path,
    expected_version: str,
) -> str:
    result = subprocess.run(
        [str(binary), "--version"],
        check=True,
        capture_output=True,
        text=True,
        timeout=15,
    )

    observed = result.stdout.strip()

    if expected_version not in observed:
        raise RuntimeError(
            "OpenClaw version mismatch: "
            f"expected={expected_version}, "
            f"observed={observed}"
        )

    return observed


def isolated_environment(
    root: Path,
) -> dict[str, str]:
    env = os.environ.copy()

    locations = {
        "HOME": root / "home",
        "XDG_CONFIG_HOME": root / "config",
        "XDG_CACHE_HOME": root / "cache",
        "XDG_DATA_HOME": root / "data",
        "XDG_STATE_HOME": root / "state",
    }

    for path in locations.values():
        path.mkdir(parents=True, exist_ok=True)

    for key, path in locations.items():
        env[key] = str(path)

    env["NO_COLOR"] = "1"

    return env


def observe_status() -> dict[str, Any]:
    binary, expected_version = resolve_openclaw()

    observed_version = verify_version(
        binary,
        expected_version,
    )

    with tempfile.TemporaryDirectory(
        prefix="hc-openclaw-adapter-"
    ) as temp:
        sandbox = Path(temp)

        result = subprocess.run(
            [
                str(binary),
                "status",
                "--json",
            ],
            cwd=sandbox,
            env=isolated_environment(sandbox),
            capture_output=True,
            text=True,
            timeout=30,
        )

        stdout = result.stdout.strip()
        stderr = result.stderr.strip()

        if not stdout:
            raise RuntimeError(
                "OpenClaw status returned empty stdout"
            )

        try:
            upstream = json.loads(stdout)
        except json.JSONDecodeError as exc:
            raise RuntimeError(
                "OpenClaw status returned invalid JSON"
            ) from exc

        if not isinstance(upstream, dict):
            raise RuntimeError(
                "OpenClaw status JSON must be an object"
            )

        return {
            "ADAPTER": "HC_OPENCLAW_STATUS",
            "ADAPTER_STATUS": "PASS",
            "OPERATION": "STATUS",
            "UPSTREAM": {
                "PRODUCT": "OpenClaw",
                "EXPECTED_VERSION": expected_version,
                "OBSERVED_VERSION": observed_version,
                "RC": result.returncode,
                "JSON": upstream,
                "STDERR_NONEMPTY": bool(stderr),
            },
            "MUTATION_PERFORMED": False,
        }


def main() -> None:
    result = observe_status()

    print(
        json.dumps(
            result,
            sort_keys=True,
            separators=(",", ":"),
        )
    )


if __name__ == "__main__":
    main()
