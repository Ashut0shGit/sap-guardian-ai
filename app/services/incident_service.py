import json
from pathlib import Path

from app.models.incident import Incident
from app.models.transport import TransportObject


class IncidentService:

    INCIDENT_FILE = Path(
        "data/incidents.json"
    )

    @staticmethod
    def search_related_incidents(
        object_names: list[str]
    ) -> list[Incident]:

        with open(
            IncidentService.INCIDENT_FILE,
            "r",
            encoding="utf-8"
        ) as file:
            incidents_data = json.load(file)

        incidents = [
            Incident(**incident)
            for incident in incidents_data
        ]

        matching_incidents = []

        for incident in incidents:

            incident_objects = (
                set(
                    incident.related_objects
                )
            )

            transport_objects = set(object_names)

            if (
                incident_objects
                &
                transport_objects
            ):
                matching_incidents.append(
                    incident
                )

        return matching_incidents