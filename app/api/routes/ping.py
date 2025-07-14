"""
Ping API Routes

This module contains the ping endpoint for health checks and connectivity testing.
"""

from datetime import datetime
from fastapi import APIRouter, Depends
from ...models.schemas import PingResponse
from ...utils.helpers import format_timestamp

# Create router for ping endpoints
router = APIRouter()


@router.get(
    "/ping",
    response_model=PingResponse,
    summary="Health Check",
    description="Simple health check endpoint to verify API connectivity",
    tags=["Health"]
)
async def ping() -> PingResponse:
    """
    Health check endpoint.
    
    Returns a simple ping response to verify API connectivity and health.
    
    Returns:
        PingResponse: Health check response with message and timestamp
    """
    return PingResponse(
        message="pong",
        timestamp=format_timestamp()
    )


@router.get(
    "/health",
    response_model=PingResponse,
    summary="Detailed Health Check",
    description="Detailed health check with additional system information",
    tags=["Health"]
)
async def health_check() -> PingResponse:
    """
    Detailed health check endpoint.
    
    Returns a health check response with additional system information.
    This endpoint can be extended to include database connectivity,
    external service status, and other health indicators.
    
    Returns:
        PingResponse: Health check response with message and timestamp
    """
    # In a production environment, this would check:
    # - Database connectivity
    # - External service health
    # - System resources
    # - Configuration validity
    
    return PingResponse(
        message="healthy",
        timestamp=format_timestamp()
    ) 