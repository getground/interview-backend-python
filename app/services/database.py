"""
In-Memory Database Service

This module provides an in-memory database service with JSON-like structure
and CRUD operations. It simulates a real database for development purposes.
"""

import json
import threading
from datetime import datetime
from typing import Any, Dict, List, Optional, Union
from uuid import uuid4

from app.data.seed_data import LISTING_SEED_DATA


class InMemoryDatabase:
    """
    In-memory database service with thread-safe operations.
    
    Provides CRUD operations for a JSON-like data structure with
    automatic ID generation and timestamp tracking.
    """
    
    def __init__(self):
        """Initialize the in-memory database with default structure."""
        self._data = {
            "users": [],
            "sessions": [],
            "listings": [],
            "data": {}
        }
        self._lock = threading.Lock()
    
    def _generate_id(self) -> str:
        """Generate a unique ID for new records."""
        return str(uuid4())
    
    def _add_timestamp(self, record: Dict[str, Any]) -> Dict[str, Any]:
        """Add timestamp to a record."""
        now = datetime.utcnow().isoformat()
        record["created_at"] = now
        record["updated_at"] = now
        return record
    
    def _update_timestamp(self, record: Dict[str, Any]) -> Dict[str, Any]:
        """Update timestamp for an existing record."""
        record["updated_at"] = datetime.utcnow().isoformat()
        return record
    
    def seed_listings(self):
        """Seed the listings collection with sample data."""
        with self._lock:
            if "listings" not in self._data:
                self._data["listings"] = []
            
            # Clear existing listings
            self._data["listings"] = []
            
            # Add seed data with proper formatting
            for listing_data in LISTING_SEED_DATA:
                # Convert the listing data to match our schema
                listing_record = {
                    "id": str(listing_data["id"]),  # Convert to string for consistency
                    "listing_id": listing_data["id"],
                    "development_name": listing_data.get("developmentName", ""),
                    "post_town": listing_data["addressDetails"]["city"],
                    "shortened_post_code": listing_data["addressDetails"]["shortenedPostcode"],
                    "region": listing_data["addressDetails"]["region"],
                    "property_type": listing_data["propertyType"],
                    "bedrooms": listing_data["bedrooms"],
                    "bathrooms": listing_data["bathrooms"],
                    "size_sq_ft": listing_data["sizeSqFt"],
                    "price_in_cents": listing_data["priceInCents"],
                    "minimum_deposit_in_cents": listing_data["minimumDepositInCents"],
                    "estimated_deposit_in_cents": listing_data["estimatedDepositInCents"],
                    "rental_income_in_cents": listing_data["monthlyRentalIncomeInCents"],
                    "is_tenanted": listing_data.get("isTenanted", False),
                    "is_cash_only": listing_data.get("isCashOnly", False),
                    "description": listing_data.get("description", ""),
                    "photos": listing_data.get("photos", []),
                    "is_featured": listing_data.get("isFeatured", False),
                    "gross_yield": listing_data.get("grossYield", 0),
                    "has_user_requested_contact": listing_data.get("hasUserRequestedContact", False),
                    "has_user_saved_listing": listing_data.get("hasUserSavedListing", False),
                    "is_share_sale": listing_data.get("isShareSale", False),
                    "is_getground_company": listing_data.get("isCompany", False),
                    "made_visible_at": listing_data.get("madeVisibleAt"),
                }
                
                # Add timestamps
                listing_record = self._add_timestamp(listing_record)
                self._data["listings"].append(listing_record)
    
    def get_all(self, collection: str) -> List[Dict[str, Any]]:
        """
        Get all records from a collection.
        
        Args:
            collection: Name of the collection to retrieve
            
        Returns:
            List of all records in the collection
            
        Raises:
            KeyError: If collection doesn't exist
        """
        with self._lock:
            if collection not in self._data:
                raise KeyError(f"Collection '{collection}' not found")
            return self._data[collection].copy()
    
    def get_by_id(self, collection: str, record_id: str) -> Optional[Dict[str, Any]]:
        """
        Get a record by ID from a collection.
        
        Args:
            collection: Name of the collection to search
            record_id: ID of the record to retrieve
            
        Returns:
            Record if found, None otherwise
            
        Raises:
            KeyError: If collection doesn't exist
        """
        with self._lock:
            if collection not in self._data:
                raise KeyError(f"Collection '{collection}' not found")
            
            for record in self._data[collection]:
                if record.get("id") == record_id:
                    return record.copy()
            return None
    
    def create(self, collection: str, data: Dict[str, Any]) -> Dict[str, Any]:
        """
        Create a new record in a collection.
        
        Args:
            collection: Name of the collection to add to
            data: Record data to create
            
        Returns:
            Created record with ID and timestamps
            
        Raises:
            KeyError: If collection doesn't exist
        """
        with self._lock:
            if collection not in self._data:
                raise KeyError(f"Collection '{collection}' not found")
            
            # Generate ID and add timestamps
            record = data.copy()
            record["id"] = self._generate_id()
            record = self._add_timestamp(record)
            
            # Add to collection
            self._data[collection].append(record)
            return record.copy()
    
    def update(self, collection: str, record_id: str, data: Dict[str, Any]) -> Optional[Dict[str, Any]]:
        """
        Update an existing record in a collection.
        
        Args:
            collection: Name of the collection to update
            record_id: ID of the record to update
            data: New data for the record
            
        Returns:
            Updated record if found, None otherwise
            
        Raises:
            KeyError: If collection doesn't exist
        """
        with self._lock:
            if collection not in self._data:
                raise KeyError(f"Collection '{collection}' not found")
            
            for i, record in enumerate(self._data[collection]):
                if record.get("id") == record_id:
                    # Update record with new data
                    updated_record = record.copy()
                    updated_record.update(data)
                    updated_record = self._update_timestamp(updated_record)
                    
                    # Replace in collection
                    self._data[collection][i] = updated_record
                    return updated_record.copy()
            
            return None
    
    def delete(self, collection: str, record_id: str) -> bool:
        """
        Delete a record from a collection.
        
        Args:
            collection: Name of the collection to delete from
            record_id: ID of the record to delete
            
        Returns:
            True if record was deleted, False if not found
            
        Raises:
            KeyError: If collection doesn't exist
        """
        with self._lock:
            if collection not in self._data:
                raise KeyError(f"Collection '{collection}' not found")
            
            for i, record in enumerate(self._data[collection]):
                if record.get("id") == record_id:
                    del self._data[collection][i]
                    return True
            
            return False
    
    def find(self, collection: str, filters: Dict[str, Any]) -> List[Dict[str, Any]]:
        """
        Find records in a collection matching filters.
        
        Args:
            collection: Name of the collection to search
            filters: Dictionary of field-value pairs to match
            
        Returns:
            List of matching records
            
        Raises:
            KeyError: If collection doesn't exist
        """
        with self._lock:
            if collection not in self._data:
                raise KeyError(f"Collection '{collection}' not found")
            
            matches = []
            for record in self._data[collection]:
                if all(record.get(key) == value for key, value in filters.items()):
                    matches.append(record.copy())
            
            return matches
    
    def get_collection_names(self) -> List[str]:
        """
        Get list of all collection names.
        
        Returns:
            List of collection names
        """
        with self._lock:
            return list(self._data.keys())
    
    def reset(self):
        """Reset database to initial state."""
        with self._lock:
            self._data = {
                "users": [],
                "sessions": [],
                "listings": [],
                "data": {}
            }
    
    def export_data(self) -> Dict[str, Any]:
        """
        Export all data as JSON-serializable dictionary.
        
        Returns:
            Dictionary containing all database data
        """
        with self._lock:
            return self._data.copy()
    
    def import_data(self, data: Dict[str, Any]):
        """
        Import data from dictionary.
        
        Args:
            data: Dictionary containing data to import
        """
        with self._lock:
            self._data = data.copy()


# Create global database instance
database = InMemoryDatabase()


def get_database() -> InMemoryDatabase:
    """
    Get database instance.
    
    Returns:
        InMemoryDatabase: Database instance
    """
    return database 