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
