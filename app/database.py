from sqlalchemy.ext.asyncio import AsyncSession, create_async_engine
from sqlalchemy.orm import DeclarativeBase, sessionmaker

# отдельные переменные для удобства
DB_HOST = 'localhost' # хост
DB_PORT = 5432        # исходный порт
DB_USER = 'postgres'  # имя пользователя
DB_PASS = 'postgres'  # пароль
DB_NAME = 'postgres'  # название БД

# URL базы данных:
DATABASE_URL = f'postgresql+asyncpg://{DB_USER}:{DB_PASS}@{DB_HOST}:{DB_PORT}/{DB_NAME}'

# асинхронный движок Алхимии:
engine = create_async_engine(DATABASE_URL)

# генератор сессий (транзацкий / инструкций) для БД
async_session_maker = sessionmaker(engine, 
								   class_=AsyncSession, 
								   expire_on_commit=False)

# создание класса для миграций
class Base(DeclarativeBase):
	pass