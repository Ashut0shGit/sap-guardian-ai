import json
from pathlib import Path

from app.models.transport import Transport


class TransportService:

    DATA_FOLDER = Path("data/transports")

    @staticmethod # static method is a method that is bound to the class and not the instance of the class
    def get_transport(
        transport_id: str
    ) -> Transport:

        file_path = (
            TransportService.DATA_FOLDER
            / f"{transport_id}.json"
        )

        if not file_path.exists():
            raise FileNotFoundError(
                f"Transport {transport_id} not found"
            )

        with open(
            file_path,
            "r",
            encoding="utf-8"
        ) as file:
            data = json.load(file)

        return Transport(**data) # ** is used to unpack the dictionary into keyword arguments