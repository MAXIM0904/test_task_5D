from pydantic import Field
from pydantic_settings import BaseSettings


class ServiceSettings(BaseSettings):
    """ Service setting """

    service_name: str = Field("TestTask", alias="NAME_SERVICE")
    host: str = Field("127.0.0.1", alias="START_HOST")
    port: int = Field(8081, alias="START_PORT")
    token: str = Field('ad49c4f614f5fedd0b369c372303d4ab8829846e', alias="TOKEN_BITLY")

service_setting = ServiceSettings()
