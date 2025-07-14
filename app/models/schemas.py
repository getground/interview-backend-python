"""
Pydantic Models and Schemas

This module contains all Pydantic models used for request/response validation,
data serialization, and API documentation.
"""

from datetime import datetime
from typing import Any, Dict, List, Optional, Union
from pydantic import BaseModel, Field


class PingResponse(BaseModel):
    """
    Response model for ping endpoint.
    
    Provides a simple health check response with message and timestamp.
    """
    message: str = Field(..., description="Response message")
    timestamp: str = Field(..., description="ISO format timestamp")
    
    class Config:
        """Pydantic configuration."""
        schema_extra = {
            "example": {
                "message": "pong",
                "timestamp": "2024-01-01T00:00:00Z"
            }
        }


class BaseResponse(BaseModel):
    """
    Base response model for all API endpoints.
    
    Provides consistent response structure across all endpoints.
    """
    success: bool = Field(..., description="Whether the operation was successful")
    message: str = Field(..., description="Response message")
    data: Optional[Dict[str, Any]] = Field(None, description="Response data")
    
    class Config:
        """Pydantic configuration."""
        schema_extra = {
            "example": {
                "success": True,
                "message": "Operation completed successfully",
                "data": {}
            }
        }


class ErrorResponse(BaseModel):
    """
    Error response model for API endpoints.
    
    Provides consistent error response structure.
    """
    success: bool = Field(False, description="Always false for error responses")
    message: str = Field(..., description="Error message")
    error_code: Optional[str] = Field(None, description="Error code for client handling")
    details: Optional[Dict[str, Any]] = Field(None, description="Additional error details")
    
    class Config:
        """Pydantic configuration."""
        schema_extra = {
            "example": {
                "success": False,
                "message": "An error occurred",
                "error_code": "VALIDATION_ERROR",
                "details": {"field": "example_field"}
            }
        }


class DatabaseRecord(BaseModel):
    """
    Base model for database records.
    
    Provides common fields for all database records including
    ID, timestamps, and metadata.
    """
    id: str = Field(..., description="Unique record identifier")
    created_at: str = Field(..., description="ISO format creation timestamp")
    updated_at: str = Field(..., description="ISO format last update timestamp")
    
    class Config:
        """Pydantic configuration."""
        schema_extra = {
            "example": {
                "id": "123e4567-e89b-12d3-a456-426614174000",
                "created_at": "2024-01-01T00:00:00Z",
                "updated_at": "2024-01-01T00:00:00Z"
            }
        }


class UserRecord(DatabaseRecord):
    """
    User record model.
    
    Extends DatabaseRecord with user-specific fields.
    """
    username: str = Field(..., description="User's username")
    email: Optional[str] = Field(None, description="User's email address")
    is_active: bool = Field(True, description="Whether the user is active")
    
    class Config:
        """Pydantic configuration."""
        schema_extra = {
            "example": {
                "id": "123e4567-e89b-12d3-a456-426614174000",
                "username": "john_doe",
                "email": "john@example.com",
                "is_active": True,
                "created_at": "2024-01-01T00:00:00Z",
                "updated_at": "2024-01-01T00:00:00Z"
            }
        }


class SessionRecord(DatabaseRecord):
    """
    Session record model.
    
    Extends DatabaseRecord with session-specific fields.
    """
    user_id: str = Field(..., description="Associated user ID")
    session_token: str = Field(..., description="Session authentication token")
    expires_at: str = Field(..., description="ISO format expiration timestamp")
    is_valid: bool = Field(True, description="Whether the session is valid")
    
    class Config:
        """Pydantic configuration."""
        schema_extra = {
            "example": {
                "id": "123e4567-e89b-12d3-a456-426614174000",
                "user_id": "456e7890-e89b-12d3-a456-426614174000",
                "session_token": "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9...",
                "expires_at": "2024-01-02T00:00:00Z",
                "is_valid": True,
                "created_at": "2024-01-01T00:00:00Z",
                "updated_at": "2024-01-01T00:00:00Z"
            }
        }


class CreateUserRequest(BaseModel):
    """
    Request model for creating a new user.
    
    Contains the required fields for user creation.
    """
    username: str = Field(..., min_length=3, max_length=50, description="User's username")
    email: Optional[str] = Field(None, description="User's email address")
    
    class Config:
        """Pydantic configuration."""
        schema_extra = {
            "example": {
                "username": "john_doe",
                "email": "john@example.com"
            }
        }


class UpdateUserRequest(BaseModel):
    """
    Request model for updating an existing user.
    
    Contains optional fields that can be updated.
    """
    username: Optional[str] = Field(None, min_length=3, max_length=50, description="User's username")
    email: Optional[str] = Field(None, description="User's email address")
    is_active: Optional[bool] = Field(None, description="Whether the user is active")
    
    class Config:
        """Pydantic configuration."""
        schema_extra = {
            "example": {
                "username": "john_doe_updated",
                "email": "john.updated@example.com",
                "is_active": True
            }
        }


class DatabaseStatus(BaseModel):
    """
    Database status response model.
    
    Provides information about the database state and collections.
    """
    collections: List[str] = Field(..., description="List of available collections")
    total_records: int = Field(..., description="Total number of records across all collections")
    record_counts: Dict[str, int] = Field(..., description="Record count per collection")
    
    class Config:
        """Pydantic configuration."""
        schema_extra = {
            "example": {
                "collections": ["users", "sessions", "data"],
                "total_records": 5,
                "record_counts": {
                    "users": 2,
                    "sessions": 1,
                    "data": 2
                }
            }
        } 