"""
Tests for Ping Endpoints

This module contains tests for the ping and health check endpoints.
"""

import pytest
from fastapi.testclient import TestClient
from app.models.schemas import PingResponse


class TestPingEndpoint:
    """Test cases for the ping endpoint."""
    
    def test_ping_endpoint_success(self, client: TestClient):
        """
        Test that the ping endpoint returns a successful response.
        
        Args:
            client: FastAPI test client
        """
        response = client.get("/api/ping")
        
        assert response.status_code == 200
        data = response.json()
        
        # Check response structure
        assert "message" in data
        assert "timestamp" in data
        assert data["message"] == "pong"
        
        # Validate timestamp format (ISO format)
        assert "T" in data["timestamp"]
        assert "Z" in data["timestamp"] or "+" in data["timestamp"]
    
    def test_ping_endpoint_response_model(self, client: TestClient):
        """
        Test that the ping endpoint response matches the expected model.
        
        Args:
            client: FastAPI test client
        """
        response = client.get("/api/ping")
        
        assert response.status_code == 200
        data = response.json()
        
        # Validate against Pydantic model
        ping_response = PingResponse(**data)
        assert ping_response.message == "pong"
        assert isinstance(ping_response.timestamp, str)
    
    def test_ping_endpoint_different_messages(self, client: TestClient):
        """
        Test that ping and health endpoints return different messages.
        
        Args:
            client: FastAPI test client
        """
        ping_response = client.get("/api/ping")
        health_response = client.get("/api/health")
        
        assert ping_response.status_code == 200
        assert health_response.status_code == 200
        
        ping_data = ping_response.json()
        health_data = health_response.json()
        
        assert ping_data["message"] == "pong"
        assert health_data["message"] == "healthy"
    
    def test_ping_endpoint_headers(self, client: TestClient):
        """
        Test that the ping endpoint returns proper headers.
        
        Args:
            client: FastAPI test client
        """
        response = client.get("/api/ping")
        
        assert response.status_code == 200
        assert "application/json" in response.headers["content-type"]
    
    def test_ping_endpoint_methods(self, client: TestClient):
        """
        Test that the ping endpoint only accepts GET method.
        
        Args:
            client: FastAPI test client
        """
        # Test POST method (should fail)
        response = client.post("/api/ping")
        assert response.status_code == 405  # Method Not Allowed
        
        # Test PUT method (should fail)
        response = client.put("/api/ping")
        assert response.status_code == 405  # Method Not Allowed
        
        # Test DELETE method (should fail)
        response = client.delete("/api/ping")
        assert response.status_code == 405  # Method Not Allowed


class TestHealthEndpoint:
    """Test cases for the health endpoint."""
    
    def test_health_endpoint_success(self, client: TestClient):
        """
        Test that the health endpoint returns a successful response.
        
        Args:
            client: FastAPI test client
        """
        response = client.get("/api/health")
        
        assert response.status_code == 200
        data = response.json()
        
        # Check response structure
        assert "message" in data
        assert "timestamp" in data
        assert data["message"] == "healthy"
        
        # Validate timestamp format
        assert "T" in data["timestamp"]
    
    def test_health_endpoint_response_model(self, client: TestClient):
        """
        Test that the health endpoint response matches the expected model.
        
        Args:
            client: FastAPI test client
        """
        response = client.get("/api/health")
        
        assert response.status_code == 200
        data = response.json()
        
        # Validate against Pydantic model
        health_response = PingResponse(**data)
        assert health_response.message == "healthy"
        assert isinstance(health_response.timestamp, str)


class TestRootEndpoint:
    """Test cases for the root endpoint."""
    
    def test_root_endpoint_success(self, client: TestClient):
        """
        Test that the root endpoint returns application information.
        
        Args:
            client: FastAPI test client
        """
        response = client.get("/")
        
        assert response.status_code == 200
        data = response.json()
        
        # Check required fields
        assert "app_name" in data
        assert "version" in data
        assert "description" in data
        assert "environment" in data
        assert "endpoints" in data
        
        # Check endpoint links
        endpoints = data["endpoints"]
        assert "health_check" in endpoints
        assert "documentation" in endpoints
        assert "redoc" in endpoints
    
    def test_root_endpoint_structure(self, client: TestClient):
        """
        Test that the root endpoint has the correct structure.
        
        Args:
            client: FastAPI test client
        """
        response = client.get("/")
        
        assert response.status_code == 200
        data = response.json()
        
        # Validate endpoint URLs
        assert data["endpoints"]["health_check"] == "/api/ping"
        assert data["endpoints"]["detailed_health"] == "/api/health"
        assert data["endpoints"]["documentation"] == "/docs"
        assert data["endpoints"]["redoc"] == "/redoc"


class TestErrorHandling:
    """Test cases for error handling."""
    
    def test_404_endpoint(self, client: TestClient):
        """
        Test that non-existent endpoints return 404.
        
        Args:
            client: FastAPI test client
        """
        response = client.get("/api/nonexistent")
        
        assert response.status_code == 404
    
    def test_favicon_endpoint(self, client: TestClient):
        """
        Test that favicon endpoint returns a response.
        
        Args:
            client: FastAPI test client
        """
        response = client.get("/favicon.ico")
        
        assert response.status_code == 200
        data = response.json()
        assert "message" in data 