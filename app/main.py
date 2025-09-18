"""
FastAPI Application Entry Point

This module contains the main FastAPI application setup including:
- Application initialization
- CORS middleware configuration
- API router registration
- Exception handlers
- Startup and shutdown events
"""

from contextlib import asynccontextmanager
from fastapi import FastAPI, Request
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import JSONResponse
from fastapi.exceptions import RequestValidationError
from starlette.exceptions import HTTPException as StarletteHTTPException

from .config.settings import get_settings
from .api.routes import ping, root
from .utils.helpers import create_error_response


@asynccontextmanager
async def lifespan(app: FastAPI):
    """
    Application lifespan manager.
    
    Handles startup and shutdown events for the FastAPI application.
    
    Args:
        app: FastAPI application instance
    """
    # Startup events
    print("🚀 Starting FastAPI Backend...")
    print(f"📊 Environment: {get_settings().environment}")
    print(f"🔧 Debug mode: {get_settings().debug}")
    print(f"🌐 Server will run on: http://{get_settings().host}:{get_settings().port}")
    
    yield
    
    # Shutdown events
    print("🛑 Shutting down FastAPI Backend...")


def create_app() -> FastAPI:
    """
    Create and configure the FastAPI application.
    
    Returns:
        FastAPI: Configured FastAPI application instance
    """
    settings = get_settings()
    
    # Create FastAPI app with metadata
    app = FastAPI(
        title=settings.app_name,
        description=settings.app_description,
        version=settings.app_version,
        docs_url=settings.docs_url,
        redoc_url=settings.redoc_url,
        debug=settings.debug,
        lifespan=lifespan
    )
    
    # Configure CORS middleware
    app.add_middleware(
        CORSMiddleware,
        allow_origins=settings.cors_origins,
        allow_credentials=settings.cors_allow_credentials,
        allow_methods=settings.cors_allow_methods,
        allow_headers=settings.cors_allow_headers,
    )
    
    # Include API routers
    app.include_router(
        ping.router,
        prefix=settings.api_prefix,
        tags=["API"]
    )
    
    # Include root router (no prefix for root endpoints)
    app.include_router(
        root.router,
        tags=["Root"]
    )
    
    # Add exception handlers
    @app.exception_handler(StarletteHTTPException)
    async def http_exception_handler(request: Request, exc: StarletteHTTPException):
        """Handle HTTP exceptions."""
        return JSONResponse(
            status_code=exc.status_code,
            content=create_error_response(
                message=str(exc.detail),
                error_code=f"HTTP_{exc.status_code}"
            )
        )
    
    @app.exception_handler(RequestValidationError)
    async def validation_exception_handler(request: Request, exc: RequestValidationError):
        """Handle request validation errors."""
        return JSONResponse(
            status_code=422,
            content=create_error_response(
                message="Request validation error",
                error_code="VALIDATION_ERROR",
                details={"errors": exc.errors()}
            )
        )
    
    @app.exception_handler(Exception)
    async def general_exception_handler(request: Request, exc: Exception):
        """Handle general exceptions."""
        return JSONResponse(
            status_code=500,
            content=create_error_response(
                message="Internal server error",
                error_code="INTERNAL_ERROR"
            )
        )
    
    return app


# Create the application instance
app = create_app()






if __name__ == "__main__":
    """
    Run the application directly if this file is executed.
    
    This allows running the app with: python -m app.main
    """
    import uvicorn
    
    settings = get_settings()
    
    uvicorn.run(
        "app.main:app",
        host=settings.host,
        port=settings.port,
        reload=settings.debug,
        log_level="info" if settings.debug else "warning"
    ) 