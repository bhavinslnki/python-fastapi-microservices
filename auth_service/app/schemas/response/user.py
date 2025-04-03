from pydantic import BaseModel,root_validator
from datetime import datetime

class UserResponse(BaseModel):
    id: int
    first_name: str
    last_name: str
    email: str

    class Config:
        from_attributes = True  # This allows SQLAlchemy models to be serialized
