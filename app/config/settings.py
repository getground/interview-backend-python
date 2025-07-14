"""
Application Settings Configuration

This module contains all application configuration settings including:
- Environment variables
- Default values
- Configuration validation
- Development and production settings
"""

import os
from typing import List, Optional
from pydantic import validator
from pydantic_settings import BaseSettings


class Settings(BaseSettings):
    """
    Application settings with environment variable support.
    
    Uses Pydantic BaseSettings for automatic environment variable parsing
    and validation.
    """
    
    # Application metadata
    app_name: str = "FastAPI Backend"
    app_version: str = "1.0.0"
    app_description: str = "AI Coding Interview Backend API"
    
    # Server configuration
    host: str = "0.0.0.0"
    port: int = 3001
    debug: bool = True
    
    # Environment
    environment: str = "development"
    
    # CORS settings
    cors_origins: List[str] = ["*"]
    cors_allow_credentials: bool = True
    cors_allow_methods: List[str] = ["*"]
    cors_allow_headers: List[str] = ["*"]
    
    # API settings
    api_prefix: str = "/api"
    docs_url: str = "/docs"
    redoc_url: str = "/redoc"
    
    # Database settings (for future use)
    database_url: Optional[str] = None
    
    @validator("environment")
    def validate_environment(cls, v: str) -> str:
        """Validate environment setting."""
        allowed_environments = ["development", "production", "testing"]
        if v not in allowed_environments:
            raise ValueError(f"Environment must be one of {allowed_environments}")
        return v
    
    @validator("port")
    def validate_port(cls, v: int) -> int:
        """Validate port number."""
        if not 1 <= v <= 65535:
            raise ValueError("Port must be between 1 and 65535")
        return v
    
    class Config:
        """Pydantic configuration."""
        env_file = ".env"
        env_file_encoding = "utf-8"
        case_sensitive = False


# Create global settings instance
settings = Settings()


def get_settings() -> Settings:
    """
    Get application settings instance.
    
    Returns:
        Settings: Application settings instance
    """
    return settings 