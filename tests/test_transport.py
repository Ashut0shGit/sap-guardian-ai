from app.services.transport_service import (
    TransportService
)


transport = TransportService.get_transport( # Since get_transport() is a @staticmethod, we can call it directly.
    "DEVK900451"
)

print(
    transport.transport_id
)

print(
    transport.description
)

for obj in transport.objects:
    print(
        obj.name,
        obj.type
    )