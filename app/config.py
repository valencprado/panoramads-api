"""
    Módulo para configuração do projeto
"""
from functools import lru_cache
from pydantic_settings import BaseSettings


class AppSettings(BaseSettings): # pylint: disable=too-few-public-methods
    """
    Classe Configuração das variáveis de ambiente
    """
    app_name: str = "PanoramADS API"
    project_id: str
    private_key_id: str
    private_key: str
    client_email: str
    client_id: str
    client_url: str
    class Config:# pylint: disable=too-few-public-methods
        """
        Classe de configuração interna
        """
        env_file = ".env"

@lru_cache
def get_settings() -> AppSettings:
    """
    Método que retorna as configurações ao aplicativo
    """
    settings = AppSettings()
    return settings
