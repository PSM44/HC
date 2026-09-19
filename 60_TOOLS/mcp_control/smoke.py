from __future__ import annotations

import asyncio
import json
from pathlib import Path
from typing import Any

from mcp import Client, StdioServerParameters

ROOT = Path("/home/aazcl/repos/HC")

EXPECTED_TOOLS = {
    "hc_get_project_state",
    "hc_get_capabilities",
    "hc_get_dag",
}


def emit_ai_envelope(payload: dict[str, Any]) -> None:
    print("---AI_START---")
    print(json.dumps(payload, sort_keys=True, separators=(",", ":")))
    print("---AI_END---")


async def main() -> None:
    server = StdioServerParameters(
        command="uv",
        args=[
            "run",
            "python",
            str(ROOT / "60_TOOLS" / "mcp_control" / "server.py"),
        ],
        cwd=ROOT,
    )

    protocol_version: str | None = None
    observed_tools: list[str] = []

    async with Client(server) as client:
        tools_result = await client.list_tools()
        tools = {tool.name for tool in tools_result.tools}

        protocol_version = str(client.protocol_version)
        observed_tools = sorted(tools)

        if tools != EXPECTED_TOOLS:
            raise RuntimeError(
                f"Unexpected MCP tool set: expected={EXPECTED_TOOLS}, observed={tools}"
            )

        state = await client.call_tool("hc_get_project_state", {})
        if state.is_error:
            raise RuntimeError("hc_get_project_state returned error")

        state_payload = state.structured_content
        if not state_payload:
            raise RuntimeError("hc_get_project_state returned no structured content")

        if state_payload.get("project_id") != "HC":
            raise RuntimeError("Unexpected project_id")

        if state_payload.get("branch_observed") != "main":
            raise RuntimeError("Unexpected branch")

        if state_payload.get("mutation_performed") is not False:
            raise RuntimeError("Mutation invariant violated")

        capabilities = await client.call_tool("hc_get_capabilities", {})
        if capabilities.is_error or not capabilities.structured_content:
            raise RuntimeError("hc_get_capabilities failed")

        dag = await client.call_tool("hc_get_dag", {})
        if dag.is_error or not dag.structured_content:
            raise RuntimeError("hc_get_dag failed")

    emit_ai_envelope(
        {
            "TASK_ID": "HC-E03-PHASE1",
            "STATUS": "PASS",
            "PROTOCOL": protocol_version,
            "TOOLS": observed_tools,
            "CHECKS": {
                "DISCOVERY": "PASS",
                "PROJECT_STATE": "PASS",
                "CAPABILITIES": "PASS",
                "DAG": "PASS",
                "READ_ONLY_ROUNDTRIP": "PASS",
            },
            "MUTATION_PERFORMED": False,
        }
    )


asyncio.run(main())
