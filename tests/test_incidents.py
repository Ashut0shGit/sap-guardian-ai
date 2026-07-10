from app.services.transport_service import (
    TransportService
)

from app.services.incident_service import (
    IncidentService
)


transport = (
    TransportService.get_transport(
        "DEVK900451"
    )
)

incidents = (
    IncidentService
    .search_related_incidents(
        transport.objects
    )
)

for incident in incidents:
    print(
        incident.id,
        incident.description
    )