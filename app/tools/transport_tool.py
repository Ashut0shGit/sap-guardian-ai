from app.services.transport_service import TransportService
from langchain.tools import tool

@tool
def get_transport_tool(
    transport_id: str
) -> dict:

    """
    Retrieve SAP transport information using a transport ID.
    Args:
        transport_id: The ID of the transport to retrieve.
    Returns:
        A dictionary containing the transport information.
    """
    transport = (
        TransportService.get_transport(
            transport_id
        )
    )

    return transport.model_dump()