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
