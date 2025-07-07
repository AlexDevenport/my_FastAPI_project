from pydantic_settings import BaseSettings

class Settings(BaseSettings):
	# указываем все переменные
	DB_HOST: str
	DB_PORT: int
	DB_USER: str
	DB_PASS: str
	DB_NAME: str

	# задание url (более новый метод)
	@property # функция - параметр
	def DATABASE_URL(self):
		return f"postgresql+asyncpg://{self.DB_USER}:{self.DB_PASS}@{self.DB_HOST}:{self.DB_PORT}/{self.DB_NAME}"

	# класс для указания из какого файла забирать настройки
	class Config():
		env_file = '.env' # enviroment variables

settings = Settings() # задание экземпляра класса

print(settings.DATABASE_URL)