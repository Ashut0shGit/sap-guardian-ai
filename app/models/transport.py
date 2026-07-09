from pydantic import BaseModel
from typing import List

class TransportObject(BaseModel):
    name: str
    type: str
    description: str

class Transport(BaseModel):
    transport_id: str
    description: str
    developer: str
    objects: List[TransportObject]