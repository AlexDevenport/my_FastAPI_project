from fastapi import FastAPI
from typing import Optional # для опциональных аргументов
from datetime import date # для типа данных "дата"
from fastapi import Query # для ограничения введенных значений

app = FastAPI()

@app.get('/hotels')
def get_hotels(
	location: str,   # строка местоположения (обяз.)
	date_from: date, # дата прибытия (обяз.)
	date_to: date,   # дата отбытия (обяз.)
	has_spa: Optional[bool] = None, # опциональный логический с None
	# ограничение кол-ва звезд отеля
	stars: Optional[int] = Query(None, ge=1, le=5)
):
	return location, date_from, date_to, has_spa, stars