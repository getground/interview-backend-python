"""
Pydantic Models and Schemas

This module contains all Pydantic models used for request/response validation,
data serialization, and API documentation.
"""

from datetime import datetime
from typing import Any, Dict, List, Optional, Union
from enum import Enum
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


class Region(str, Enum):
    """
    Region enumeration for property locations.
    """
    NORTH_WEST = "North West"
    LONDON = "London"
    NORTH_EAST = "North East"
    SOUTH_WEST = "South West"
    SOUTH_EAST = "South East"
    MIDLANDS = "Midlands"
    SCOTLAND = "Scotland"
    WALES = "Wales"


class PropertyType(str, Enum):
    """
    Property type enumeration.
    """
    APARTMENT = "apartment"
    DETACHED = "detached"
    SEMI_DETACHED = "semi-detached"
    TERRACED = "terraced"
    END_TERRACE = "end-terrace"


class Photo(BaseModel):
    """
    Photo model for listing images.
    
    Contains URLs for different image sizes and metadata.
    """
    original_url: str = Field(..., alias="originalURL", description="Original image URL")
    standard_url: str = Field(..., alias="standardURL", description="Standard size image URL")
    thumbnail_url: str = Field(..., alias="thumbnailURL", description="Thumbnail image URL")
    mime_type: str = Field(..., alias="mimeType", description="Image MIME type")
    
    class Config:
        """Pydantic configuration."""
        allow_population_by_field_name = True
        schema_extra = {
            "example": {
                "originalURL": "https://storage.googleapis.com/assets-terranova-qa-module-core/listings/1b2b53fd-398b-4129-8f7d-c5932f90b3c3",
                "standardURL": "https://storage.googleapis.com/assets-terranova-qa-module-core/listings/1b2b53fd-398b-4129-8f7d-c5932f90b3c3_standard",
                "thumbnailURL": "https://storage.googleapis.com/assets-terranova-qa-module-core/listings/1b2b53fd-398b-4129-8f7d-c5932f90b3c3_thumbnail",
                "mimeType": "image/png"
            }
        }


class AddressDetails(BaseModel):
    """
    Address details model for property locations.
    
    Contains all address-related information for a property.
    """
    address_line1: str = Field(..., alias="addressLine1", description="First line of address")
    address_line2: str = Field(..., alias="addressLine2", description="Second line of address")
    city: str = Field(..., description="City name")
    postcode: str = Field(..., description="Full postcode")
    shortened_postcode: str = Field(..., alias="shortenedPostcode", description="Shortened postcode")
    country: str = Field(..., description="Country name")
    region: Region = Field(..., description="Region")
    
    class Config:
        """Pydantic configuration."""
        allow_population_by_field_name = True
        schema_extra = {
            "example": {
                "addressLine1": "123 Example Street",
                "addressLine2": "Apartment 4B",
                "city": "London",
                "postcode": "N17 6AB",
                "shortenedPostcode": "N17",
                "country": "United Kingdom",
                "region": "London"
            }
        }



class ListingRecord(BaseModel):
    """
    Property listing record model.
    
    Contains all property listing information matching the TypeScript interface.
    """
    address_details: AddressDetails = Field(..., alias="addressDetails", description="Property address details")
    bedrooms: int = Field(..., description="Number of bedrooms")
    bathrooms: int = Field(..., description="Number of bathrooms")
    description: str = Field(..., description="Property description")
    id: int = Field(..., description="Unique listing identifier")
    # The gross yield of a property is the annual rental income divided by the purchase price
    # This is a key metric for investors to consider when evaluating a property
    gross_yield: float = Field(..., alias="grossYield", description="The gross yield of a property is the annual rental income divided by the purchase price. This is a key metric for investors to consider when evaluating a property")
    is_cash_only: bool = Field(..., alias="isCashOnly", description="Whether property is cash only")
    # If the listing is being sold as part of a company.
    # Having a rental unit under a company has certain tax benefits.
    is_company: bool = Field(..., alias="isCompany", description="If the listing is being sold as part of a company. Having a rental unit under a company has certain tax benefits.")
    # A new build is a listing that is currently under construction.
    # Typically, less risk of maintenance issues.
    # But less potential for appreciation over time
    is_new_build: bool = Field(..., alias="isNewBuild", description="A new build is a listing that is currently under construction. Typically, less risk of maintenance issues. But less potential for appreciation over time")
    # A share sale is a listing that is being sold as a share of a property
    is_share_sale: bool = Field(..., alias="isShareSale", description="A share sale is a listing that is being sold as a share of a property")
    # A tenanted property is a property that is currently being rented out
    # This is a key metric for investors to consider when evaluating a property
    is_tenanted: bool = Field(..., alias="isTenanted", description="A tenanted property is a property that is currently being rented out. This is a key metric for investors to consider when evaluating a property")
    made_visible_at: Optional[str] = Field(None, alias="madeVisibleAt", description="ISO format visibility timestamp")
    # The estimated deposit required after fees
    estimated_deposit_in_cents: int = Field(..., alias="estimatedDepositInCents", description="The estimated deposit required after fees")
    # The minimum deposit required to secure the property
    # This is the minimum deposit required to secure the property
    minimum_deposit_in_cents: int = Field(..., alias="minimumDepositInCents", description="The minimum deposit required to secure the property")
    photos: List[Photo] = Field(..., description="Property photos")
    price_in_cents: int = Field(..., alias="priceInCents", description="Property price in cents")
    property_type: PropertyType = Field(..., alias="propertyType", description="Property type")
    monthly_rental_income_in_cents: int = Field(..., alias="monthlyRentalIncomeInCents", description="Monthly rental income in cents")
    size_sq_ft: int = Field(..., alias="sizeSqFt", description="Property size in square feet")
    
    class Config:
        """Pydantic configuration."""
        allow_population_by_field_name = True
        schema_extra = {
            "example": {
                "addressDetails": {
                    "addressLine1": "123 Example Street",
                    "addressLine2": "Apartment 4B",
                    "city": "London",
                    "postcode": "N17 6AB",
                    "shortenedPostcode": "N17",
                    "country": "United Kingdom",
                    "region": "London"
                },
                "bedrooms": 1,
                "bathrooms": 1,
                "description": "Beautiful modern apartment in the heart of London",
                "id": 187,
                "grossYield": 0.1056,
                "isCashOnly": False,
                "isCompany": False,
                "isNewBuild": False,
                "isShareSale": False,
                "isTenanted": True,
                "madeVisibleAt": None,
                "estimatedDepositInCents": 3125000,
                "minimumDepositInCents": 1000000,
                "photos": [
                    {
                        "originalURL": "https://storage.googleapis.com/assets-terranova-qa-module-core/listings/1b2b53fd-398b-4129-8f7d-c5932f90b3c3",
                        "standardURL": "https://storage.googleapis.com/assets-terranova-qa-module-core/listings/1b2b53fd-398b-4129-8f7d-c5932f90b3c3_standard",
                        "thumbnailURL": "https://storage.googleapis.com/assets-terranova-qa-module-core/listings/1b2b53fd-398b-4129-8f7d-c5932f90b3c3_thumbnail",
                        "mimeType": "image/png"
                    }
                ],
                "priceInCents": 12500000,
                "propertyType": "apartment",
                "monthlyRentalIncomeInCents": 110000,
                "sizeSqFt": 50
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