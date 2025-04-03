import jwt
from datetime import datetime, timedelta
from fastapi import HTTPException
from app.schemas.response.response import *

SECRET_KEY = "P2M@rAaPdjFkf!089kba"
ALGORITHM = "HS256"

def create_access_token(data: dict, expires_delta: timedelta = None):
    try:
        to_encode = data.copy()
        if expires_delta:
            expire = datetime.utcnow() + expires_delta
        else:
            expire = datetime.utcnow() + timedelta(days=365)
        to_encode.update({"exp": expire})
        return jwt.encode(to_encode, SECRET_KEY, algorithm=ALGORITHM)
    except  Exception as e:
        raise HTTPException(status_code=403, detail=str(e))    

def decode_access_token(token: str):
    return jwt.decode(token, SECRET_KEY, algorithms=[ALGORITHM])

