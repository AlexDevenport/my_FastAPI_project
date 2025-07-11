from app.database import Base
from sqlalchemy import Column, Computed, Date, ForeignKey, Integer, String


class Bookings(Base):
    __tablename__ = 'bookings'

    id = Column(Integer, primary_key=True, nullable=False)

    # внешние ключи на другие таблицы
    room_id = Column(ForeignKey('rooms.id'))
    user_id = Column(ForeignKey('users.id'))

    # обязательные столбцы
    date_from = Column(Date, nullable=False)
    date_to = Column(Date, nullable=False)
    price = Column(Integer, nullable=False)

    # автогенерирующиеся столбцы
    total_cost = Column(Integer, Computed('(date_to - date_from) * price'))
    total_days = Column(Integer, Computed('date_to - date_from'))
