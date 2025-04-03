from fastapi import HTTPException, Request, Depends, Security
from fastapi.security import HTTPBearer, HTTPAuthorizationCredentials
from fastapi.responses import JSONResponse
from sqlalchemy.orm import Session
from functools import wraps
from app.models import Role, UserRole
from app.utils import decode_access_token
from app.schemas.response.response import *
from typing import List, Optional

security = HTTPBearer()

def admin_role():
    return ["admin"]

def employee_role():
    return ["employee"]

def manager_role():
    return ["employee"]


# Token validation function
def check_bearer_token(credentials: HTTPAuthorizationCredentials = Security(security)):
    try:
        token = credentials.credentials
        # if not credentials:
        #     raise HTTPException(status_code=401, detail="Not ssauthenticated")
        decoded = decode_access_token(token)
        print("Token successfully decoded:", decoded)
        return decoded
    except Exception as e:
        print("Unexpected error in check_bearer_token:", e)
        return fail_authorization(1,"Invalid Token!",None,str(e))

# Authorization check
async def check_auth(request: Request, db: Session, roles: List[str]):
    credentials = await security(request)
    user_details = check_bearer_token(credentials)
    if isinstance(user_details, JSONResponse):
        return user_details
    print("User details from token:", user_details)
    request.state.user_details = user_details
    role_data = (
        db.query(Role)
        .join(UserRole)
        .filter(UserRole.user_id == user_details["user_id"])
        .first()
    )

    if not role_data or role_data.role_name not in roles:
        print(f"Access denied for user ID: {user_details['user_id']}")
        return forbidden(1,"You do not have permission to access this resource.!",None,None)
    print(f"Access granted for user ID: {user_details['user_id']}")

# Role-based decorator
def role_required(roles: List[str]):
    def decorator(func):
        @wraps(func)
        async def wrapper(*args, **kwargs):
            request = kwargs.get("request")
            db = kwargs.get("db")
            if not request or not db:
                raise HTTPException(
                    status_code=500,
                    detail="Request or database session is not provided",
                )
            response  =await check_auth(request, db, roles)
            if isinstance(response, JSONResponse): 
                return response
            return await func(*args, **kwargs)

        return wrapper

    return decorator
