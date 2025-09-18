# FastAPI Backend - AI Coding Interview Project

A modern, scalable Python FastAPI backend designed for AI coding interview projects. This backend provides a solid foundation with best practices for API development, testing, and documentation.

## 🚀 Features

- **FastAPI Framework**: Modern, fast web framework for building APIs
- **In-Memory Database**: JSON-based data storage with CRUD operations
- **Comprehensive Testing**: Pytest-based test suite with fixtures
- **API Documentation**: Automatic OpenAPI/Swagger documentation
- **CORS Support**: Cross-origin resource sharing configuration
- **Error Handling**: Standardized error responses and validation
- **Type Safety**: Full type hints and Pydantic validation
- **Modular Architecture**: Clean separation of concerns

## 📋 Requirements

- Python 3.10+
- pip (Python package installer)

## 🛠️ Installation

1. **Clone the repository** (if applicable):
   ```bash
   git clone <repository-url>
   cd interview-backend-python
   ```

2. **Create a virtual environment** (recommended):
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```

3. **Install dependencies**:
   ```bash
   pip install -r requirements.txt
   ```

## 🏃‍♂️ Running the Server

### Development Mode (with auto-reload)
```bash
uvicorn app.main:app --reload --port 3001
```

### Production Mode
```bash
uvicorn app.main:app --host 0.0.0.0 --port 3001
```

### Direct Python Execution
```bash
python -m app.main
```

## 🌐 API Endpoints

### Root Endpoints
- `GET /` - Application information and available endpoints
- `GET /health` - Simple health check for load balancers
- `GET /favicon.ico` - Favicon handling

### API Endpoints (prefixed with `/api`)
- `GET /api/ping` - Quick health check
- `GET /api/health` - Detailed health check with system information

### Documentation
- `GET /docs` - Swagger UI documentation
- `GET /redoc` - ReDoc documentation
- `GET /openapi.json` - OpenAPI schema

## 🧪 Testing

### Run all tests
```bash
pytest
```

### Run tests with coverage
```bash
pytest --cov=app
```

### Run specific test file
```bash
pytest tests/test_ping.py
```

### Run tests with verbose output
```bash
pytest -v
```

## 📁 Project Structure

```
interview-backend-python/
├── app/                    # Main application package
│   ├── __init__.py
│   ├── main.py            # FastAPI application entry point
│   ├── config/            # Configuration management
│   │   ├── __init__.py
│   │   └── settings.py    # Application settings
│   ├── api/               # API layer
│   │   ├── __init__.py
│   │   ├── dependencies.py # API dependencies
│   │   └── routes/        # API route definitions
│   │       ├── __init__.py
│   │       ├── ping.py    # Health check endpoints
│   │       └── root.py    # Root-level endpoints
│   ├── models/            # Data models
│   │   ├── __init__.py
│   │   └── schemas.py     # Pydantic schemas
│   ├── services/          # Business logic
│   │   ├── __init__.py
│   │   └── database.py    # In-memory database
│   └── utils/             # Utility functions
│       ├── __init__.py
│       └── helpers.py     # Helper functions
├── tests/                 # Test suite
│   ├── __init__.py
│   ├── conftest.py        # Pytest configuration
│   └── test_ping.py       # Ping endpoint tests
├── requirements.txt        # Python dependencies
├── README.md              # Project documentation
└── plan.md                # Project planning document
```

## 🔧 Configuration

The application uses environment variables for configuration. Create a `.env` file in the root directory:

```env
# Server Configuration
PORT=3001
HOST=0.0.0.0
DEBUG=true

# Environment
ENVIRONMENT=development

# CORS Settings
CORS_ORIGINS=["*"]
```

## 📊 Database

The application includes an in-memory database service with the following collections:

- **users**: User records with authentication data
- **sessions**: Session management and tokens
- **data**: General application data

### Database Operations

```python
from app.services.database import get_database

db = get_database()

# Create a record
user = db.create("users", {"username": "john", "email": "john@example.com"})

# Get all records
users = db.get_all("users")

# Get by ID
user = db.get_by_id("users", "user_id")

# Update record
updated_user = db.update("users", "user_id", {"is_active": False})

# Delete record
success = db.delete("users", "user_id")
```

## 🛡️ Security Features

- **Input Validation**: Pydantic models for request/response validation
- **CORS Configuration**: Configurable cross-origin resource sharing
- **Error Handling**: Standardized error responses
- **Type Safety**: Full type hints throughout the codebase

## 📝 API Documentation

Once the server is running, you can access:

- **Swagger UI**: http://localhost:3001/docs
- **ReDoc**: http://localhost:3001/redoc
- **OpenAPI Schema**: http://localhost:3001/openapi.json

## 🧪 Example API Calls

### Quick Health Check
```bash
curl http://localhost:3001/api/ping
```

Expected response:
```json
{
  "message": "pong",
  "timestamp": "2024-01-01T00:00:00Z"
}
```

### Simple Health Check
```bash
curl http://localhost:3001/health
```

Expected response:
```json
{
  "status": "ok"
}
```

### Detailed Health Check
```bash
curl http://localhost:3001/api/health
```

Expected response:
```json
{
  "message": "healthy",
  "timestamp": "2024-01-01T00:00:00Z"
}
```

### Application Info
```bash
curl http://localhost:3001/
```

Expected response:
```json
{
  "app_name": "FastAPI Backend",
  "version": "1.0.0",
  "description": "AI Coding Interview Backend API",
  "environment": "development",
  "endpoints": {
    "health_check": "/api/ping",
    "detailed_health": "/api/health",
    "documentation": "/docs",
    "redoc": "/redoc"
  }
}
```

## 🔍 Development

### Adding New Endpoints

1. Create a new route file in `app/api/routes/` (for API endpoints) or add to `app/api/routes/root.py` (for root endpoints)
2. Define your endpoint with proper FastAPI router syntax and documentation
3. Include the router in `app/main.py` with appropriate prefix (use `/api` prefix for API endpoints)
4. Add tests in `tests/`

### Adding New Models

1. Define Pydantic models in `app/models/schemas.py`
2. Use them in your endpoints for validation
3. Add corresponding tests

### Database Operations

1. Use the database service in `app/services/database.py`
2. Add proper error handling
3. Include validation with Pydantic models

## 🚀 Deployment

### Docker (Optional)

Create a `Dockerfile`:

```dockerfile
FROM python:3.11-slim

WORKDIR /app
COPY requirements.txt .
RUN pip install -r requirements.txt

COPY . .

CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "3001"]
```

### Environment Variables

Set production environment variables:

```env
ENVIRONMENT=production
DEBUG=false
PORT=3001
```

## 🤝 Contributing

1. Follow the existing code structure
2. Add comprehensive tests for new features
3. Update documentation as needed
4. Use type hints and docstrings
5. Follow PEP 8 style guidelines

## 📄 License

This project is for AI coding interview purposes.

## 🆘 Support

For issues or questions:
1. Check the API documentation at `/docs`
2. Review the test files for usage examples
3. Check the configuration in `app/config/settings.py`

---

**Happy Coding! 🎉** 