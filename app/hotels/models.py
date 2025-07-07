from app.database import Base
from sqlalchemy import JSON, Column, ForeignKey, Integer, String


class Hotels(Base):
    __tablename__ = 'hotels'

    # id отеля - ключ
    id = Column(Integer, primary_key=True, nullable=False) 

    # обязательные столбцы
    name = Column(String, nullable=False)
    location = Column(String, nullable=False)
    rooms_quantity = Column(Integer, nullable=False)

    # необязательные столбцы
    services = Column(JSON)
    image_id = Column(Integer)


class Rooms(Base):
    __tablename__ = 'rooms'

    id = Column(Integer, primary_key=True, nullable=False)

    # внешний ключ на hotels
    hotel_id = Column(ForeignKey('hotels.id'), nullable=False)

    # обязательные столбцы
    name = Column(String, nullable=False)
    price = Column(Integer, nullable=False)
    quantity = Column(Integer, nullable=False)

    # необязательные столбцы
    description = Column(String)
    services = Column(JSON)
    image_id = Column(Integer)