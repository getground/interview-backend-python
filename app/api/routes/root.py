"""
Root API Routes

This module contains the root-level endpoints including application info and basic endpoints.
"""

from fastapi import APIRouter
from ...config.settings import get_settings

# Create router for root endpoints
router = APIRouter()


@router.get(
    "/",
    summary="Application Info", 
    description="Returns basic application information and available endpoints",
    tags=["Root"]
)
async def root():
    """
    Root endpoint.
    
    Returns basic application information and available endpoints.
    
    Returns:
        dict: Application information and links
    """
    settings = get_settings()
    
    return {
        "app_name": settings.app_name,
        "version": settings.app_version,
        "description": settings.app_description,
        "environment": settings.environment,
        "docs_url": settings.docs_url,
        "redoc_url": settings.redoc_url,
        "api_prefix": settings.api_prefix,
        "endpoints": {
            "health_check": f"{settings.api_prefix}/ping",
            "detailed_health": f"{settings.api_prefix}/health",
            "documentation": settings.docs_url,
            "redoc": settings.redoc_url
        }
    }


@router.get(
    "/favicon.ico",
    summary="Favicon",
    description="Returns a simple favicon response to prevent 404 errors",
    tags=["Root"]
)
async def favicon():
    """
    Favicon endpoint.
    
    Returns a simple favicon response to prevent 404 errors.
    """
    return {"message": "No favicon configured"}


@router.get(
    "/health",
    summary="Simple Health Check",
    description="Simple root-level health check for load balancers and uptime monitoring",
    tags=["Health"]
)
async def root_health():
    """
    Simple root-level health check endpoint.
    
    This provides a simple health check at the root level for load balancers
    and uptime monitoring tools that expect a /health endpoint.
    For detailed health information, use /api/v1/health instead.
    
    Returns:
        dict: Simple status response
    """
    return {"status": "ok"}
