from fastapi import FastAPI
from typing import Any
from datetime import date
from fastapi import Query
from pydantic import BaseModel

app = FastAPI() # ГОЙДА

# Схема для валидации отелей
class SHotel(BaseModel):
    address: str
    name: str
    stars: int

@app.get('/hotels')
def get_hotels(
    location: str,
    date_from: date,
    date_to: date,
    has_spa: bool | None = None,
    stars: int | None = Query(None, ge=1, le=5),
) -> list[dict[str, Any]]: # словарь где ключ - строка, значения - любые
    # добавляем словарь с отелем
    hotels = [
        {
            'address': 'ул. Гагарина, 1, Алтай',
            'name': 'Super Hotel',
            'stars': 5,
        },
    ]
    return hotels

class SBooking(BaseModel):
    room_id: int
    date_from: date
    date_to: date

@app.post('/bookings')
def bookings(booking: SBooking):
    pass