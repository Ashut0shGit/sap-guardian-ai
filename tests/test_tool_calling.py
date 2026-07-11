from app.models.llm import llm

from agents.tool_registry import (
    TOOLS
)


llm_with_tools = (
    llm.bind_tools(
        TOOLS
    )
)

response = (
    llm_with_tools.invoke(
        "Analyze transport DEVK900451"
    )
)

print(response)