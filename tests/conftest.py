"""
Pytest Configuration and Test Fixtures

This module contains pytest configuration and common test fixtures
used across all test modules.
"""

import pytest
from fastapi.testclient import TestClient
from app.main import app
from app.services.database import get_database, InMemoryDatabase


@pytest.fixture
def client() -> TestClient:
    """
    Create a test client for the FastAPI application.
    
    Returns:
        TestClient: FastAPI test client
    """
    return TestClient(app)


@pytest.fixture
def database() -> InMemoryDatabase:
    """
    Get a clean database instance for testing.
    
    Returns:
        InMemoryDatabase: Database instance
    """
    db = get_database()
    # Reset database to clean state before each test
    db.reset()
    return db


@pytest.fixture
def sample_user_data() -> dict:
    """
    Sample user data for testing.
    
    Returns:
        dict: Sample user data
    """
    return {
        "username": "test_user",
        "email": "test@example.com",
        "is_active": True
    }


@pytest.fixture
def sample_session_data() -> dict:
    """
    Sample session data for testing.
    
    Returns:
        dict: Sample session data
    """
    return {
        "user_id": "test_user_id",
        "session_token": "test_session_token_12345",
        "expires_at": "2024-12-31T23:59:59Z",
        "is_valid": True
    }


@pytest.fixture
def api_headers() -> dict:
    """
    Common API headers for testing.
    
    Returns:
        dict: Common headers
    """
    return {
        "Content-Type": "application/json",
        "Accept": "application/json"
    } 