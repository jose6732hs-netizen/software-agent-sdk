"""Tool router for OpenHands SDK."""

from fastapi import APIRouter

from openhands.sdk.tool.registry import list_registered_tools
from openhands.tools.preset.default import (
    register_builtins_agents,
    register_default_tools,
)
from openhands.tools.preset.gemini import register_gemini_tools
from openhands.tools.preset.planning import register_planning_tools


tool_router = APIRouter(prefix="/tools", tags=["Tools"])

# MSK/Render low-memory profile:
# The MSK code-editing flow uses terminal + file editor and does not require
# BrowserTool at server boot. Importing the browser stack eagerly adds a large
# memory spike on small Render instances and can cause the service to be killed
# while the first conversation is starting.
register_default_tools(enable_browser=False)
register_builtins_agents(enable_browser=False)
register_gemini_tools(enable_browser=False)
register_planning_tools()


# Tool listing
@tool_router.get("/")
async def list_available_tools() -> list[str]:
    """List all available tools."""
    tools = list_registered_tools()
    return tools
