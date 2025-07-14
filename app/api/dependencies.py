"""
API Dependencies

This module contains FastAPI dependencies used throughout the application
for dependency injection, shared resources, and common functionality.
"""

from typing import Generator
from fastapi import Depends, HTTPException, status
from .config.settings import get_settings, Settings
from .services.database import get_database, InMemoryDatabase


def get_settings_dependency() -> Settings:
    """
    Dependency to get application settings.
    
    Returns:
        Settings: Application settings instance
    """
    return get_settings()


def get_database_dependency() -> InMemoryDatabase:
    """
    Dependency to get database instance.
    
    Returns:
        InMemoryDatabase: Database instance
    """
    return get_database()


def verify_api_key(api_key: str = None) -> bool:
    """
    Verify API key for protected endpoints.
    
    Args:
        api_key: API key to verify
        
    Returns:
        True if API key is valid
        
    Raises:
        HTTPException: If API key is invalid or missing
    """
    # For development, accept any non-empty API key
    # In production, this would validate against a secure key store
    if not api_key:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="API key is required"
        )
    
    # Simple validation for development
    if len(api_key) < 8:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Invalid API key"
        )
    
    return True


def get_current_user_id(user_id: str = None) -> str:
    """
    Get current user ID from request context.
    
    Args:
        user_id: User ID from request
        
    Returns:
        User ID string
        
    Raises:
        HTTPException: If user ID is missing
    """
    if not user_id:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="User ID is required"
        )
    
    return user_id


def validate_collection_name(collection: str) -> str:
    """
    Validate collection name for database operations.
    
    Args:
        collection: Collection name to validate
        
    Returns:
        Validated collection name
        
    Raises:
        HTTPException: If collection name is invalid
    """
    if not collection:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="Collection name is required"
        )
    
    # Validate collection name format
    if not collection.isalnum() and collection not in ["users", "sessions", "data"]:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="Invalid collection name"
        )
    
    return collection


def get_pagination_params(
    skip: int = 0,
    limit: int = 100
) -> dict:
    """
    Get pagination parameters with validation.
    
    Args:
        skip: Number of records to skip
        limit: Maximum number of records to return
        
    Returns:
        Dictionary with pagination parameters
        
    Raises:
        HTTPException: If pagination parameters are invalid
    """
    if skip < 0:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="Skip parameter must be non-negative"
        )
    
    if limit < 1 or limit > 1000:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="Limit parameter must be between 1 and 1000"
        )
    
    return {"skip": skip, "limit": limit}


# Common dependency combinations
def get_app_dependencies() -> Generator[tuple, None, None]:
    """
    Get common application dependencies.
    
    Yields:
        Tuple of (settings, database) dependencies
    """
    settings = get_settings_dependency()
    database = get_database_dependency()
    yield settings, database 