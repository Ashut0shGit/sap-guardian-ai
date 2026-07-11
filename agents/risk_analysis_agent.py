from app.models.llm import llm

from prompts.transport_analysis_prompt import (
    TRANSPORT_ANALYSIS_PROMPT
)


class RiskAnalysisAgent:

    @staticmethod
    def analyze(
        transport: dict,
        incidents: list[dict]
    ) -> str:

        prompt = (
            TRANSPORT_ANALYSIS_PROMPT.format(
                transport=transport,
                incidents=incidents
            )
        )

        response = llm.invoke(
            prompt
        )

        return response.content