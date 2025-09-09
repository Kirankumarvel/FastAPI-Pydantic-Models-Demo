# FastAPI Pydantic Models Demo

A FastAPI application demonstrating Pydantic models for data validation, serialization, and API request/response handling.

---

## 🚀 Features

- FastAPI framework with automatic OpenAPI documentation
- Pydantic models for data validation and serialization
- Email validation with `EmailStr` type
- Optional fields with default values
- ORM mode configuration for database compatibility
- Interactive API documentation at `/docs` and `/redoc`
- Python 3.7+ compatibility
- Virtual environment setup

---

## 📋 Prerequisites

- Python 3.7 or higher
- pip (Python package manager)

---

## 🛠️ Installation

1. **Clone the repository**
   ```bash
   git clone https://github.com/Kirankumarvel/fastapi-pydantic-models-demo.git
   cd fastapi-pydantic-models-demo
   ```

2. **Create a virtual environment**
   ```bash
   python -m venv venv
   ```

3. **Activate the virtual environment**
   - **Windows:**
     ```bash
     venv\Scripts\activate
     ```
   - **macOS/Linux:**
     ```bash
     source venv/bin/activate
     ```

4. **Install dependencies**
   ```bash
   pip install -r requirements.txt
   ```

---

## 📦 Dependencies

- `fastapi` - The web framework for building APIs
- `uvicorn` - ASGI server for running FastAPI applications
- `pydantic` - Data validation and settings management
- `pydantic-extra-types` - Additional validation types like EmailStr

To generate requirements.txt:
```bash
pip freeze > requirements.txt
```

---

## 🚀 Running the Application

1. **Start the development server**
   ```bash
   uvicorn main:app --reload --reload-exclude venv
   ```

2. **Access the application**
   - API: http://127.0.0.1:8000
   - Interactive docs: http://127.0.0.1:8000/docs
   - Alternative docs: http://127.0.0.1:8000/redoc

---

## 📡 API Endpoints

### POST /users/
Create a new user with validated input data.

**Request Body:**
```json
{
  "username": "johndoe",
  "email": "john@example.com",
  "password": "securepassword123",
  "full_name": "John Doe"
}
```

**Response:**
```json
{
  "username": "johndoe",
  "email": "john@example.com",
  "full_name": "John Doe",
  "join_date": "2023-12-07T10:30:00.000000"
}
```

---

## 🎯 Key Concept: Pydantic Models

### What are Pydantic Models?
- Python classes that inherit from `pydantic.BaseModel`
- Define data structure with type hints
- Provide automatic data validation
- Handle serialization/deserialization
- Generate comprehensive OpenAPI documentation

### Model Definitions

#### UserCreate Model (Input)
```python
class UserCreate(BaseModel):
    username: str                    # Required field
    email: EmailStr                  # Validated email format
    password: str                    # Required field
    full_name: Optional[str] = None  # Optional field with default
```

#### UserOut Model (Output)
```python
class UserOut(BaseModel):
    username: str
    email: EmailStr
    full_name: Optional[str] = None
    join_date: datetime              # Auto-populated field

    class Config:
        from_attributes = True      # ORM compatibility
```

### Key Features

1. **Type Validation**: Automatic validation of data types
2. **Email Validation**: `EmailStr` ensures valid email format
3. **Optional Fields**: Use `Optional[str] = None` for optional data
4. **ORM Mode**: `from_attributes = True` enables database model compatibility
5. **Security**: Separate input/output models prevent password exposure

---

## 🧪 Testing the API

### Valid Request
```bash
curl -X POST "http://127.0.0.1:8000/users/" \
  -H "Content-Type: application/json" \
  -d '{
    "username": "johndoe",
    "email": "john@example.com",
    "password": "securepassword123",
    "full_name": "John Doe"
  }'
```

### Invalid Email (Validation Error)
```bash
curl -X POST "http://127.0.0.1:8000/users/" \
  -H "Content-Type: application/json" \
  -d '{
    "username": "johndoe",
    "email": "invalid-email",
    "password": "securepassword123"
  }'
```

### Missing Required Field
```bash
curl -X POST "http://127.0.0.1:8000/users/" \
  -H "Content-Type: application/json" \
  -d '{
    "email": "john@example.com",
    "password": "securepassword123"
  }'
```

---

## 📁 Project Structure

```
fastapi-pydantic-models-demo/
├── main.py          # Main application file
├── models.py        # Pydantic model definitions
├── requirements.txt # Project dependencies
├── README.md        # Project documentation
└── venv/            # Virtual environment (gitignored)
```

---

## 🔧 Code Explanation

### models.py
```python
from pydantic import BaseModel, EmailStr
from typing import Optional
from datetime import datetime

class UserCreate(BaseModel):
    """
    Model for user creation (input).
    - username: Required username
    - email: Validated email address
    - password: Required password (will be hashed)
    - full_name: Optional full name
    """
    username: str
    email: EmailStr  # Special type for email validation!
    password: str
    full_name: Optional[str] = None  # Optional field with default

class UserOut(BaseModel):
    """
    Model for user response (output).
    - Excludes password for security
    - Includes join_date timestamp
    - Supports ORM object conversion
    """
    username: str
    email: EmailStr
    full_name: Optional[str] = None
    join_date: datetime

    class Config:
        from_attributes = True  # ORM compatibility (was orm_mode)
```

### main.py
```python
from fastapi import FastAPI
from datetime import datetime
from models import UserCreate, UserOut

app = FastAPI()

@app.post("/users/", response_model=UserOut)
async def create_user(user: UserCreate):
    """
    Create a new user with validated data.
    - Uses UserCreate model for input validation
    - Returns UserOut model (excludes password)
    - response_model ensures output validation
    """
    # Simulate user creation (in real app, save to database)
    user_data = {
        "username": user.username,
        "email": user.email,
        "full_name": user.full_name,
        "join_date": datetime.now()
    }

    return UserOut(**user_data)
```

---

## 🎓 Learning Points

1. **Data Validation**: Automatic validation with type hints
2. **Security**: Separate models for input/output prevent data exposure
3. **Email Validation**: Specialized types for common data formats
4. **Optional Fields**: Design flexible APIs with optional parameters
5. **ORM Compatibility**: `from_attributes=True` for database integration
6. **API Documentation**: Automatic OpenAPI schema generation

---

## 🔧 Troubleshooting

### Common Issues

1. **Email validation errors**
   - Ensure valid email format: `user@example.com`
2. **Missing required fields**
   - Check that all required fields are provided
3. **ORM mode configuration**
   - Use `from_attributes = True` (was `orm_mode = True` in older versions)
4. **Type validation errors**
   - Ensure data types match model definitions
5. **Import errors**
   - Install `pydantic-extra-types` for `EmailStr` support

---

## 📚 Learning Resources

- [Pydantic Documentation](https://docs.pydantic.dev/)
- [FastAPI Body Parameters](https://fastapi.tiangolo.com/tutorial/body/)
- [Pydantic Model Config](https://docs.pydantic.dev/concepts/models/#model-config)
- [EmailStr Validation](https://docs.pydantic.dev/concepts/types/#emailstr)

---

## 🤝 Contributing

1. Fork the project
2. Create your feature branch (`git checkout -b feature/AmazingFeature`)
3. Commit your changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

---

## 📄 License

This project is licensed under the MIT License - see the LICENSE file for details.

---

## 🙏 Acknowledgments

- Pydantic team for excellent data validation library
- FastAPI team for seamless integration
- Uvicorn team for the ASGI server
- Python community for ongoing support
