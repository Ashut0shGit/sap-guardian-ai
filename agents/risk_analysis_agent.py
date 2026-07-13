from app.models.llm import llm

from prompts.transport_analysis_prompt import (
    TRANSPORT_ANALYSIS_PROMPT
)
from rag.retrieval import retrieve_context

class RiskAnalysisAgent:

    @staticmethod
    def analyze(
        transport: dict,
        incidents: list[dict]
    ) -> str:

        query = (
            transport["description"] + " " + " ".join(obj["name"] for obj in transport["objects"])
        )

        rag_context = (retrieve_context(query))
        prompt = (
            TRANSPORT_ANALYSIS_PROMPT.format(
                transport=transport,
                incidents=incidents,
                context = "/n".join(rag_context)
            )
        )

        response = llm.invoke(
            prompt
        )

        return response.content