from pydantic import BaseModel
from datetime import datetime

class ItineraryEventBase(BaseModel):
    name: str
    desc: str
    coords: str
    place_id: str
    order: int

class ItineraryEventCreate(ItineraryEventBase):
    pass

class ItineraryEventResponse(ItineraryEventBase):
    itinerary_id: int
    id: int
    created_at: datetime

    class Config:
        orm_mode = True
