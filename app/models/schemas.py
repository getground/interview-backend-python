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


class Photo(BaseModel):
    """
    Photo model for listing images.
    
    Contains URLs for different image sizes and metadata.
    """
    original_url: str = Field(..., alias="OriginalURL", description="Original image URL")
    standard_url: str = Field(..., alias="StandardURL", description="Standard size image URL")
    thumbnail_url: str = Field(..., alias="ThumbnailURL", description="Thumbnail image URL")
    mime_type: str = Field(..., alias="MimeType", description="Image MIME type")
    
    class Config:
        """Pydantic configuration."""
        allow_population_by_field_name = True
        schema_extra = {
            "example": {
                "OriginalURL": "https://storage.googleapis.com/assets-terranova-qa-module-core/listings/1b2b53fd-398b-4129-8f7d-c5932f90b3c3",
                "StandardURL": "https://storage.googleapis.com/assets-terranova-qa-module-core/listings/1b2b53fd-398b-4129-8f7d-c5932f90b3c3_standard",
                "ThumbnailURL": "https://storage.googleapis.com/assets-terranova-qa-module-core/listings/1b2b53fd-398b-4129-8f7d-c5932f90b3c3_thumbnail",
                "MimeType": "image/png"
            }
        }


class ListingRecord(DatabaseRecord):
    """
    Property listing record model.
    
    Extends DatabaseRecord with property listing-specific fields.
    """
    listing_id: int = Field(..., alias="ID", description="Unique listing identifier")
    development_name: Optional[str] = Field(None, alias="DevelopmentName", description="Development name")
    post_town: str = Field(..., alias="PostTown", description="Post town")
    shortened_post_code: str = Field(..., alias="ShortenedPostCode", description="Shortened post code")
    region: str = Field(..., alias="Region", description="Region")
    property_type: str = Field(..., alias="PropertyType", description="Property type")
    bedrooms: int = Field(..., alias="Bedrooms", description="Number of bedrooms")
    bathrooms: int = Field(..., alias="Bathrooms", description="Number of bathrooms")
    size_sq_ft: int = Field(..., alias="SizeSqFt", description="Property size in square feet")
    price_in_cents: int = Field(..., alias="PriceInCents", description="Property price in cents")
    minimum_deposit_in_cents: int = Field(..., alias="MinimumDepositInCents", description="Minimum deposit in cents")
    estimated_deposit_in_cents: int = Field(..., alias="EstimatedDepositInCents", description="Estimated deposit in cents")
    rental_income_in_cents: int = Field(..., alias="RentalIncomeInCents", description="Rental income in cents")
    is_tenanted: bool = Field(..., alias="IsTenanted", description="Whether property is tenanted")
    is_cash_only: bool = Field(..., alias="IsCashOnly", description="Whether property is cash only")
    description: str = Field(..., alias="Description", description="Property description")
    photos: List[Photo] = Field(..., alias="Photos", description="Property photos")
    is_featured: bool = Field(..., alias="IsFeatured", description="Whether listing is featured")
    gross_yield: float = Field(..., alias="GrossYield", description="Gross yield percentage")
    has_user_requested_contact: bool = Field(..., alias="HasUserRequestedContact", description="Whether user has requested contact")
    has_user_saved_listing: bool = Field(..., alias="HasUserSavedListing", description="Whether user has saved listing")
    is_share_sale: bool = Field(..., alias="IsShareSale", description="Whether it's a share sale")
    is_getground_company: bool = Field(..., alias="IsGetgroundCompany", description="Whether it's a GetGround company")
    made_visible_at: Optional[str] = Field(None, alias="MadeVisibleAt", description="ISO format visibility timestamp")
    
    class Config:
        """Pydantic configuration."""
        allow_population_by_field_name = True
        schema_extra = {
            "example": {
                "ID": 187,
                "DevelopmentName": None,
                "PostTown": "London",
                "ShortenedPostCode": "N17",
                "Region": "South West",
                "PropertyType": "apartment",
                "Bedrooms": 1,
                "Bathrooms": 1,
                "SizeSqFt": 50,
                "PriceInCents": 12500000,
                "MinimumDepositInCents": 1000000,
                "EstimatedDepositInCents": 3125000,
                "RentalIncomeInCents": 110000,
                "IsTenanted": True,
                "IsCashOnly": False,
                "Description": "property",
                "Photos": [
                    {
                        "OriginalURL": "https://storage.googleapis.com/assets-terranova-qa-module-core/listings/1b2b53fd-398b-4129-8f7d-c5932f90b3c3",
                        "StandardURL": "https://storage.googleapis.com/assets-terranova-qa-module-core/listings/1b2b53fd-398b-4129-8f7d-c5932f90b3c3_standard",
                        "ThumbnailURL": "https://storage.googleapis.com/assets-terranova-qa-module-core/listings/1b2b53fd-398b-4129-8f7d-c5932f90b3c3_thumbnail",
                        "MimeType": "image/png"
                    }
                ],
                "IsFeatured": False,
                "GrossYield": 0.1056,
                "HasUserRequestedContact": False,
                "HasUserSavedListing": False,
                "IsShareSale": False,
                "IsGetgroundCompany": False,
                "MadeVisibleAt": None
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