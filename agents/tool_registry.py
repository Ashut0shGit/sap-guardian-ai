from app.tools.transport_tool import (
    get_transport_tool
)

from app.tools.incident_tool import (
    get_related_incidents_tool
)


TOOLS = [
    get_transport_tool,
    get_related_incidents_tool
]