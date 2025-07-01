from fastapi import Query
from datetime import date

# Схема для полей get_hotels
class SHotelsSearchArgs:
    def __init__(
        self,
        location: str,
        date_from: date,
        date_to: date,
        has_spa: bool | None = None,
        stars: int | None = Query(None, ge=1, le=5),
    ):
        self.location = location
        self.date_from = date_from
        self.date_to = date_to
        self.has_spa = has_spa
        self.stars = stars