from langchain_core.messages import (
    HumanMessage,
    ToolMessage
)

from agents.tool_registry import (
    TOOLS
)

from app.models.llm import llm

class ReactAgent:

    MAX_ITERATIONS = 5

    @staticmethod
    def run(
        query: str
    ):

        llm_with_tools = (
            llm.bind_tools(
                TOOLS
            )
        )

        messages = [
            HumanMessage(
                content=query
            )
        ]

        for _ in range(
            ReactAgent.MAX_ITERATIONS
        ):

            response = (
                llm_with_tools.invoke(
                    messages
                )
            )

            messages.append(
                response
            )

            if not response.tool_calls:
                return response.content

            for tool_call in (
                response.tool_calls
            ):

                tool_name = (
                    tool_call["name"]
                )

                tool_args = (
                    tool_call["args"]
                )

                selected_tool = next(
                    tool
                    for tool in TOOLS
                    if tool.name
                    == tool_name
                )

                tool_result = (
                    selected_tool.invoke(
                        tool_args
                    )
                )

                messages.append(
                    ToolMessage(
                        content=str(
                            tool_result
                        ),
                        tool_call_id=
                        tool_call["id"]
                    )
                )

        return (
            "Maximum iterations reached."
        )