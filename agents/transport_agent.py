from app.tools.transport_tool import (
    get_transport_tool
)

from app.tools.incident_tool import (
    get_related_incidents_tool
)


class TransportAgent:

    @staticmethod
    def analyze_transport(
        transport_id: str
    ) -> dict:

        transport = (
            get_transport_tool.invoke(
                {
                    "transport_id": transport_id
                }
            )
        )

        object_names = [
            obj["name"]
            for obj in transport["objects"]
        ]

        incidents = (
            get_related_incidents_tool.invoke(
                {
                    "object_names": object_names
                }
            )
        )

        return {
            "transport": transport,
            "incidents": incidents,
            "similar_releases": [],
            "testing_guidelines": []
        }