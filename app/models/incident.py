from pydantic import BaseModel
from typing import List


class Incident(BaseModel):
    id: str
    module: str
    description: str
    related_objects: List[str]