from fastapi import FastAPI
from typing import Any # была нужна для валидации словаря

from fastapi import Depends # для валидности аргументов

# импорт моделей
from app.SHotelsSearchArgs import SHotelsSearchArgs
from app.SBooking import SBooking

app = FastAPI()

@app.get('/hotels')
def get_hotels(
    search_args: SHotelsSearchArgs = Depends() # использование схемы отлей
):
    return search_args

@app.post('/bookings')
def bookings(booking: SBooking):
    pass