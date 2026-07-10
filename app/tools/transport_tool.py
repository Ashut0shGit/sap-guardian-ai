from app.services.transport_service import TransportService


def get_transport_tool(
    transport_id: str
) -> dict:

    transport = (
        TransportService.get_transport(
            transport_id
        )
    )

    return transport.model_dump()