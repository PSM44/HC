from __future__ import annotations

import json
import subprocess
from pathlib import Path
from typing import Any

import anyio

from mcp import MCPError
from mcp.server import Server, ServerRequestContext
from mcp.server.stdio import stdio_server
from mcp.types import (
    INVALID_PARAMS,
    CallToolRequestParams,
    CallToolResult,
    ListToolsResult,
    PaginatedRequestParams,
    TextContent,
    Tool,
)

ROOT = Path("/home/aazcl/repos/HC")
STATE_FILE = ROOT / "12_STATE" / "HC.CURRENT_STATE.json"

EMPTY_INPUT_SCHEMA: dict[str, Any] = {
    "type": "object",
    "additionalProperties": False,
}


def _git(*args: str) -> str:
    result = subprocess.run(
        ["git", "-C", str(ROOT), *args],
        check=True,
        capture_output=True,
        text=True,
    )
    return result.stdout.strip()


def _project_state() -> dict[str, Any]:
    canonical_state = json.loads(
        STATE_FILE.read_text(encoding="utf-8")
    )

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


def _capabilities() -> dict[str, Any]:
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


def _dag() -> dict[str, Any]:
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


TOOLS = [
    Tool(
        name="hc_get_project_state",
        description="Return observed read-only HC project and Git state.",
        input_schema=EMPTY_INPUT_SCHEMA,
    ),
    Tool(
        name="hc_get_capabilities",
        description="Return the initial HC capability model.",
        input_schema=EMPTY_INPUT_SCHEMA,
    ),
    Tool(
        name="hc_get_dag",
        description="Return the authorized high-level HC development DAG.",
        input_schema=EMPTY_INPUT_SCHEMA,
    ),
]


async def on_list_tools(
    ctx: ServerRequestContext,
    params: PaginatedRequestParams | None,
) -> ListToolsResult:
    return ListToolsResult(tools=TOOLS)


def _tool_result(payload: dict[str, Any]) -> CallToolResult:
    return CallToolResult(
        content=[
            TextContent(
                type="text",
                text=json.dumps(
                    payload,
                    sort_keys=True,
                    separators=(",", ":"),
                ),
            )
        ],
        structured_content=payload,
    )


async def on_call_tool(
    ctx: ServerRequestContext,
    params: CallToolRequestParams,
) -> CallToolResult:
    arguments = params.arguments or {}

    if arguments:
        raise MCPError(
            INVALID_PARAMS,
            f"Tool {params.name} accepts no arguments",
        )

    if params.name == "hc_get_project_state":
        return _tool_result(_project_state())

    if params.name == "hc_get_capabilities":
        return _tool_result(_capabilities())

    if params.name == "hc_get_dag":
        return _tool_result(_dag())

    raise MCPError(
        INVALID_PARAMS,
        f"Unknown tool: {params.name}",
    )


server: Server[Any] = Server(
    "HC Control",
    on_list_tools=on_list_tools,
    on_call_tool=on_call_tool,
)


async def main() -> None:
    async with stdio_server() as (
        read_stream,
        write_stream,
    ):
        await server.run(
            read_stream,
            write_stream,
            server.create_initialization_options(),
        )


if __name__ == "__main__":
    anyio.run(main)
