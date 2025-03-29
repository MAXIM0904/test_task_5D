import os

from pydantic import Field
from pydantic_settings import BaseSettings, SettingsConfigDict
from pathlib import Path

package_dir = Path(__file__).parent.parent
file_path = package_dir.joinpath(".env")

class ServiceSettings(BaseSettings):
    """ Service setting """

    service_name: str = Field("TestTask", alias="NAME_SERVICE")
    host: str = Field("127.0.0.1", alias="START_HOST")
    port: int = Field(8080, alias="START_PORT")
    token: str = Field('ad49c4f614f5fedd0b369c372303d4ab8829846e', alias="TOKEN_BITLY")

    model_config = SettingsConfigDict(env_file=file_path)

service_setting = ServiceSettings()
