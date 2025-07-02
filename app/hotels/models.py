from app.database import Base
from sqlalchemy import JSON, Column, Integer, String

class Hotels(Base):
    __tablename__ = 'hotels'

    # id отеля - ключ
    id = Column(Integer, primary_key=True) 

    # обязательные столбцы
    name = Column(String, nullable=False)
    location = Column(String, nullable=False)
    rooms_quantity = Column(Integer, nullable=False)

    # необязательные столбцы
    services = Column(JSON)
    image_id = Column(Integer)