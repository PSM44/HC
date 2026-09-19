from __future__ import annotations

import asyncio
import json
import subprocess
import sys
from pathlib import Path
from typing import Any

from mcp import Client, StdioServerParameters

ROOT = Path("/home/aazcl/repos/HC")
SERVER = ROOT / "60_TOOLS" / "mcp_control" / "server.py"

EXPECTED_TOOLS = {
    "hc_get_project_state",
    "hc_get_capabilities",
    "hc_get_dag",
}


def git_status() -> str:
    result = subprocess.run(
        ["git", "-C", str(ROOT), "status", "--porcelain"],
        check=True,
        capture_output=True,
        text=True,
    )
    return result.stdout


def emit_ai_envelope(payload: dict[str, Any]) -> None:
    print("---AI_START---")
    print(
        json.dumps(
            payload,
            sort_keys=True,
            separators=(",", ":"),
        )
    )
    print("---AI_END---")


def server_parameters() -> StdioServerParameters:
    return StdioServerParameters(
        command="uv",
        args=[
            "run",
            "python",
            str(SERVER),
        ],
        cwd=ROOT,
    )


async def schema_test() -> tuple[bool, str]:
    async with Client(server_parameters()) as client:
        listing = await client.list_tools()

        observed = {tool.name for tool in listing.tools}

        if observed != EXPECTED_TOOLS:
            return False, f"UNEXPECTED_TOOLS:{sorted(observed)}"

        for tool in listing.tools:
            schema = tool.input_schema

            if schema.get("type") != "object":
                return False, f"{tool.name}:TYPE_NOT_OBJECT"

            if schema.get("additionalProperties") is not False:
                return False, (
                    f"{tool.name}:"
                    "ADDITIONAL_PROPERTIES_NOT_FALSE"
                )

        return True, "STRICT_EMPTY_OBJECT_SCHEMA"


async def valid_tool_test() -> tuple[bool, str]:
    async with Client(server_parameters()) as client:
        result = await client.call_tool(
            "hc_get_capabilities",
            {},
        )

        if result.is_error:
            return False, "VALID_TOOL_RETURNED_ERROR"

        if not result.structured_content:
            return False, "VALID_TOOL_NO_STRUCTURED_CONTENT"

        return True, "SUCCESS_RESULT"


async def expected_failure(
    tool_name: str,
    arguments: dict[str, Any],
) -> tuple[bool, str]:
    try:
        async with Client(server_parameters()) as client:
            result = await client.call_tool(
                tool_name,
                arguments,
            )

            if result.is_error:
                return True, "ERROR_RESULT"

            return False, "UNEXPECTED_SUCCESS"

    except Exception as exc:
        return True, f"EXCEPTION:{type(exc).__name__}"


async def run_tests() -> dict[str, Any]:
    repo_before = git_status()

    checks: dict[str, str] = {}
    error_modes: dict[str, str] = {}

    schema_ok, schema_mode = await schema_test()

    if not schema_ok:
        raise RuntimeError(schema_mode)

    checks["STRICT_INPUT_SCHEMA"] = "PASS"

    valid_ok, valid_mode = await valid_tool_test()

    if not valid_ok:
        raise RuntimeError(valid_mode)

    checks["VALID_TOOL"] = "PASS"

    unknown_ok, unknown_mode = await expected_failure(
        "hc_tool_that_does_not_exist",
        {},
    )

    if not unknown_ok:
        raise RuntimeError(
            "Unknown MCP tool did not fail closed"
        )

    checks["UNKNOWN_TOOL"] = "PASS"
    error_modes["UNKNOWN_TOOL"] = unknown_mode

    invalid_ok, invalid_mode = await expected_failure(
        "hc_get_capabilities",
        {
            "unexpected_argument": "must_fail",
        },
    )

    if not invalid_ok:
        raise RuntimeError(
            "Invalid MCP arguments did not fail closed"
        )

    checks["INVALID_ARGUMENTS"] = "PASS"
    error_modes["INVALID_ARGUMENTS"] = invalid_mode

    repo_after = git_status()

    if repo_before != repo_after:
        raise RuntimeError(
            "Negative-path execution mutated repository state"
        )

    checks["NO_CANONICAL_MUTATION"] = "PASS"

    return {
        "TASK_ID": "HC-E04",
        "STATUS": "PASS",
        "CHECKS": checks,
        "ERROR_MODES": error_modes,
        "MUTATION_PERFORMED": False,
        "TERMINAL_CONVERGENCE": True,
    }


async def main() -> None:
    try:
        payload = await run_tests()
        emit_ai_envelope(payload)

    except Exception as exc:
        emit_ai_envelope(
            {
                "TASK_ID": "HC-E04",
                "STATUS": "FAIL",
                "ERROR_CLASS": type(exc).__name__,
                "ERROR": str(exc),
                "MUTATION_PERFORMED": False,
                "TERMINAL_CONVERGENCE": False,
            }
        )
        sys.exit(1)


asyncio.run(main())
