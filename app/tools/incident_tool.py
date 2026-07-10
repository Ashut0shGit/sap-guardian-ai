from app.services.incident_service import IncidentService


def get_related_incidents_tool(
    object_names: list[str]
) -> list[dict]:

    incidents = (
        IncidentService.search_related_incidents(
            object_names
        )
    )

    return [
        incident.model_dump()
        for incident in incidents
    ]