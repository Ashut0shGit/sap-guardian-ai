from app.services.incident_service import IncidentService
from langchain.tools import tool

@tool
def get_related_incidents_tool(
    object_names: list[str]
) -> list[dict]:

    """
    Retrieve related incidents using object names.
    Args:
        object_names: A list of object names to search for.
    Returns:
        A list of dictionaries containing the incident information.
    """
    incidents = (
        IncidentService.search_related_incidents(
            object_names
        )
    )

    return [
        incident.model_dump()
        for incident in incidents
    ]