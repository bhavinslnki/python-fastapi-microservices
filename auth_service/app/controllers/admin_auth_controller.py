from fastapi.responses import JSONResponse
from app.models import User,Role,UserRole
from hashlib import sha256  
from app.schemas.response.user import UserResponse
from app.utils.jwt_utils import * 
from app.utils.bcrypt_utils import * 
from app.schemas.response.response import *

async def login_admin(email:str,password:str,db):
    try:
        get_user =db.query(User).filter(User.email==email).first()
        if get_user:
            if verify_password(password,get_user.password.strip()):
                get_user_role =db.query(UserRole).filter(UserRole.id ==get_user.id).first()
                token_data ={
                    "user_id": get_user.id,
                    "email": get_user.email,
                    "role":get_user_role.role.role_name
                }
                token = create_access_token(token_data)
                return success_response(1, "Admin logged in successfully", {"token":token})
            else:
                return fail_authorization(1, "Invalid password")
        else:
            return fail_authorization(1, "Invalid email address",None)
    except Exception  as e:
        err_message = e if isinstance(e, str) else getattr(e, "message", str(e))
        return server_error(1,None,err_message)