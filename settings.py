from pydantic import BaseSettings
from dotenv import load_dotenv


class Settings(BaseSettings):
    mysql_user: str
    mysql_password: str
    mysql_database: str
    mysql_root_password: str
    mysql_external_port: int
    mysql_host: str
    backend_debug_port: int
    backend_debug_host: str

    @property
    def sql_connection_string(self):
        return f'mysql+pymysql://{self.mysql_user}:{self.mysql_root_password}@{self.mysql_host}:{self.mysql_external_port}/{self.mysql_database}'

    class Config:
        case_sensitive = False


load_dotenv('.env')
settings = Settings()
