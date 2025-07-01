from pydantic import BaseModel
from datetime import date

class SBooking(BaseModel):
    room_id: int
    date_from: date
    date_to: date