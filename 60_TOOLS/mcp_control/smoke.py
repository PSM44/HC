from __future__ import annotations

import asyncio
import json
from pathlib import Path

from mcp import Client, StdioServerParameters

ROOT = Path("/home/aazcl/repos/HC")
SERVER = ROOT / "60_TOOLS" / "mcp_control" / "server.py"

EXPECTED_TOOLS = {
    "hc_get_project_state",
    "hc_get_capabilities",
    "hc_get_dag",
}


def server_parameters() -> StdioServerParameters:
    return StdioServerParameters(
        command="uv",
        args=["run", "python", str(SERVER)],
        cwd=ROOT,
    )


async def run_tests() -> dict[str, object]:
    async with Client(server_parameters()) as client:
        listing = await client.list_tools()
        tools = {tool.name for tool in listing.tools}

        if tools != EXPECTED_TOOLS:
            raise RuntimeError(
                f"Unexpected MCP tool set: "
                f"expected={EXPECTED_TOOLS}, observed={tools}"
            )

        state = await client.call_tool("hc_get_project_state", {})
        if state.is_error or not state.structured_content:
            raise RuntimeError("hc_get_project_state failed")

        payload = state.structured_content

        if payload.get("project_id") != "HC":
            raise RuntimeError("Unexpected project_id")

        if payload.get("branch_observed") != "main":
            raise RuntimeError("Unexpected branch")

        if payload.get("mutation_performed") is not False:
            raise RuntimeError("Mutation invariant violated")

        capabilities = await client.call_tool(
            "hc_get_capabilities",
            {},
        )
        if capabilities.is_error or not capabilities.structured_content:
            raise RuntimeError("hc_get_capabilities failed")

        dag = await client.call_tool("hc_get_dag", {})
        if dag.is_error or not dag.structured_content:
            raise RuntimeError("hc_get_dag failed")

        return {
            "TEST_ID": "HC-E03-POSITIVE",
            "STATUS": "PASS",
            "PROTOCOL": str(client.protocol_version),
            "CHECKS": {
                "DISCOVERY": "PASS",
                "PROJECT_STATE": "PASS",
                "CAPABILITIES": "PASS",
                "DAG": "PASS",
                "READ_ONLY_ROUNDTRIP": "PASS",
            },
            "MUTATION_PERFORMED": False,
        }


async def main() -> None:
    result = await run_tests()
    print(json.dumps(result, sort_keys=True, separators=(",", ":")))


asyncio.run(main())
