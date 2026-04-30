"""Environment configuration for the backend application."""

from pydantic_settings import BaseSettings
from functools import lru_cache


class Settings(BaseSettings):
    """Application settings loaded from environment variables."""

    # Database
    database_url: str

    # Authentication
    better_auth_secret: str
    better_auth_url: str = "http://localhost:3000"

    # CORS
    cors_origins: str = "http://localhost:3000"

    # AI Chatbot providers
    gemini_api_key: str = ""
    gemini_model: str = "gemini-2.0-flash"
    grok_api_key: str = ""
    grok_model: str = "grok-2-latest"
    max_conversation_history: int = 50

    @property
    def cors_origins_list(self) -> list[str]:
        """Parse CORS origins as a list."""
        return [origin.strip() for origin in self.cors_origins.split(",")]

    class Config:
        env_file = ".env"
        env_file_encoding = "utf-8"


@lru_cache
def get_settings() -> Settings:
    """Get cached settings instance."""
    return Settings()
