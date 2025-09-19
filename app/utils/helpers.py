"""
Utility Functions and Helpers

This module contains common utility functions used throughout the application
including response formatting, error handling, and data transformation helpers.
"""

import json
from datetime import datetime
from typing import Any, Dict, List, Optional, Union


def format_timestamp(dt: Optional[datetime] = None) -> str:
    """
    Format datetime to ISO format string.
    
    Args:
        dt: Datetime object to format. If None, uses current time.
        
    Returns:
        ISO format timestamp string
    """
    if dt is None:
        from datetime import timezone
        dt = datetime.now(timezone.utc)
    return dt.isoformat()


def create_success_response(
    message: str,
    data: Optional[Dict[str, Any]] = None
) -> Dict[str, Any]:
    """
    Create a standardized success response.
    
    Args:
        message: Success message
        data: Optional response data
        
    Returns:
        Dictionary with success response structure
    """
    response = {
        "success": True,
        "message": message,
        "timestamp": format_timestamp()
    }
    
    if data is not None:
        response["data"] = data
    
    return response


def create_error_response(
    message: str,
    error_code: Optional[str] = None,
    details: Optional[Dict[str, Any]] = None
) -> Dict[str, Any]:
    """
    Create a standardized error response.
    
    Args:
        message: Error message
        error_code: Optional error code for client handling
        details: Optional additional error details
        
    Returns:
        Dictionary with error response structure
    """
    response = {
        "success": False,
        "message": message,
        "timestamp": format_timestamp()
    }
    
    if error_code is not None:
        response["error_code"] = error_code
    
    if details is not None:
        response["details"] = details
    
    return response


def validate_json_data(data: str) -> Optional[Dict[str, Any]]:
    """
    Validate and parse JSON string data.
    
    Args:
        data: JSON string to validate
        
    Returns:
        Parsed dictionary if valid, None otherwise
    """
    try:
        return json.loads(data)
    except (json.JSONDecodeError, TypeError):
        return None


def safe_get_nested(data: Dict[str, Any], keys: List[str], default: Any = None) -> Any:
    """
    Safely get nested dictionary value using key path.
    
    Args:
        data: Dictionary to search in
        keys: List of keys to traverse
        default: Default value if key path doesn't exist
        
    Returns:
        Value at key path or default value
    """
    current = data
    
    for key in keys:
        if isinstance(current, dict) and key in current:
            current = current[key]
        else:
            return default
    
    return current


def filter_dict(data: Dict[str, Any], allowed_keys: List[str]) -> Dict[str, Any]:
    """
    Filter dictionary to only include specified keys.
    
    Args:
        data: Dictionary to filter
        allowed_keys: List of keys to keep
        
    Returns:
        Filtered dictionary with only allowed keys
    """
    return {key: value for key, value in data.items() if key in allowed_keys}


def merge_dicts(dict1: Dict[str, Any], dict2: Dict[str, Any]) -> Dict[str, Any]:
    """
    Merge two dictionaries, with dict2 values taking precedence.
    
    Args:
        dict1: First dictionary
        dict2: Second dictionary (values override dict1)
        
    Returns:
        Merged dictionary
    """
    result = dict1.copy()
    result.update(dict2)
    return result


def generate_id() -> str:
    """
    Generate a simple unique identifier.
    
    Returns:
        Unique string identifier
    """
    import uuid
    return str(uuid.uuid4())


def sanitize_string(text: str, max_length: int = 1000) -> str:
    """
    Sanitize string input for safe storage/display.
    
    Args:
        text: String to sanitize
        max_length: Maximum allowed length
        
    Returns:
        Sanitized string
    """
    if not isinstance(text, str):
        return ""
    
    # Remove null bytes and control characters
    sanitized = "".join(char for char in text if ord(char) >= 32)
    
    # Truncate if too long
    if len(sanitized) > max_length:
        sanitized = sanitized[:max_length]
    
    return sanitized.strip()


def format_file_size(size_bytes: int) -> str:
    """
    Format file size in human-readable format.
    
    Args:
        size_bytes: Size in bytes
        
    Returns:
        Formatted size string (e.g., "1.5 MB")
    """
    if size_bytes == 0:
        return "0 B"
    
    size_names = ["B", "KB", "MB", "GB", "TB"]
    import math
    
    i = int(math.floor(math.log(size_bytes, 1024)))
    p = math.pow(1024, i)
    s = round(size_bytes / p, 2)
    
    return f"{s} {size_names[i]}"


def is_valid_email(email: str) -> bool:
    """
    Basic email validation.
    
    Args:
        email: Email string to validate
        
    Returns:
        True if email format is valid, False otherwise
    """
    import re
    
    if not isinstance(email, str):
        return False
    
    # Basic email regex pattern
    pattern = r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'
    return bool(re.match(pattern, email))


def chunk_list(lst: List[Any], chunk_size: int) -> List[List[Any]]:
    """
    Split a list into chunks of specified size.
    
    Args:
        lst: List to chunk
        chunk_size: Size of each chunk
        
    Returns:
        List of chunks
    """
    if chunk_size <= 0:
        return [lst]
    
    return [lst[i:i + chunk_size] for i in range(0, len(lst), chunk_size)]


def flatten_list(nested_list: List[Any]) -> List[Any]:
    """
    Flatten a nested list structure.
    
    Args:
        nested_list: List that may contain nested lists
        
    Returns:
        Flattened list
    """
    result = []
    
    for item in nested_list:
        if isinstance(item, list):
            result.extend(flatten_list(item))
        else:
            result.append(item)
    
    return result 