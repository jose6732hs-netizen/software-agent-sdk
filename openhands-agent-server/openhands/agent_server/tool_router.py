"""Tool router for the MSK OpenHands runtime."""

from fastapi import APIRouter

from openhands.sdk.tool.registry import list_registered_tools
from openhands.tools.preset.default import register_default_tools


tool_router = APIRouter(prefix="/tools", tags=["Tools"])

# MSK/Render low-memory profile.
# This runtime edits Git repositories and only needs the core terminal,
# file editor and task tracker tools. Browser, built-in subagents, Gemini
# presets and planning presets are intentionally not preloaded because they
# add memory pressure without being used by the MSK editing flow.
register_default_tools(enable_browser=False)


@tool_router.get("/")
async def list_available_tools() -> list[str]:
    """List all available tools."""
    return list_registered_tools()
