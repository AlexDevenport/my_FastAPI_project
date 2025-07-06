from sqlalchemy.ext.asyncio import AsyncSession, create_async_engine
from sqlalchemy.orm import DeclarativeBase, sessionmaker

# импорт чувствительных данных из config.py
from app.config import settings

# чувствительные данные были вынесены в отдельный файл

# URL базы данных был перемещен в app.config

# асинхронный движок Алхимии:
engine = create_async_engine(settings.DATABASE_URL)

# генератор сессий (транзацкий / инструкций) для БД
async_session_maker = sessionmaker(engine, 
								   class_=AsyncSession, 
								   expire_on_commit=False)

# создание класса для миграций
class Base(DeclarativeBase):
	pass