from fastapi.responses import JSONResponse
from app.models import User,Role,UserRole
from app.utils.jwt_utils import * 
from app.utils.bcrypt_utils import * 
from app.utils.email_utils import * 
from app.schemas.response.user import UserResponse
import random

async def register_employee(email: str, password: str,first_name:str,last_name:str,phone_number: str , db):
    try:
        existing_user =db.query(User).filter(User.email==email).first()
        if existing_user :
            return bad_request(1,"User already exists")
        hashed_password = hash_password(password)
        print("====================hashed_password=========== > >>>>>> >>>> .>>>>>",hashed_password)
        new_user = User(email=email, password=hashed_password,first_name=first_name,last_name=last_name,phone_number=phone_number)
        new_user.set_otp()
        db.add(new_user)
        db.commit()
        await send_otp_email(new_user.email, new_user.otp)
        db.refresh(new_user)
        get_user_role = db.query(Role).filter(Role.role_name =="employee").first()
        add_userrole =UserRole(user_id=new_user.id,role_id=get_user_role.id)
        db.add(add_userrole)
        db.commit()
        db.refresh(add_userrole)
        print(add_userrole)
        user_response = UserResponse.from_orm(new_user)
        token_data ={
            "user_id": user_response.id,
            "email": user_response.email,
            "role":get_user_role.role_name
        }
        print(token_data)
        token = create_access_token(token_data)
        return success_response(1, "User registered successfully", {"token":token})
    except Exception  as e:
        err_message = e if isinstance(e, str) else getattr(e, "message", str(e))
        return server_error(1,None,err_message)

async def send_otp(email: str, db):
    try:
        user = db.query(User).filter(User.email == email).first()
        
        if not user:
            return bad_request(1, "User not found")
        
        otp = str(random.randint(100000, 999999))
        user.otp = otp
        db.commit()
        db.refresh(user)
        
        await send_otp_email(user.email, otp)
        
        return success_response(1, "OTP sent successfully", None)
    except Exception as e:
        err_message = str(e)
        return server_error(1, None, err_message)


async def verify_otp(email: str, otp: int, db):
    try:
        user = db.query(User).filter(User.email == email).first()
        
        if not user:
            return bad_request(1, "User not found")
        
        if user.otp is None:
            return bad_request(1, "OTP verification is not required")
        
        if user.otp != otp:
            return bad_request(1, "Invalid OTP")
        
        user.otp = None 
        user.is_verify = True
        db.commit()
        db.refresh(user)
        
        token_data = {
            "user_id": user.id,
            "email": user.email,
            "role": "employee"
        }
        token = create_access_token(token_data)
        
        return success_response(1, "OTP verified successfully", {"token": token})
    
    except Exception as e:
        err_message = str(e)
        return server_error(1, None, err_message)

async def login_employee(email: str, password: str, db):
    try:
        get_user = db.query(User).filter(User.email == email).first()
        if get_user:
            if get_user.otp is not None:
                return fail_authorization(1, "OTP verification required", {"email": email})
            
            if verify_password(password, get_user.password.strip()):
                get_user_role = db.query(UserRole).filter(UserRole.id == get_user.id).first()
                
                token_data = {
                    "user_id": get_user.id,
                    "email": get_user.email,
                    "role": get_user_role.role.role_name
                }
                token = create_access_token(token_data)
                return success_response(1, "User logged in successfully", {"token": token})
            else:
                return fail_authorization(1, "Invalid password")
        else:
            return fail_authorization(1, "Invalid email address", None)
    except Exception as e:
        err_message = e if isinstance(e, str) else getattr(e, "message", str(e))
        return server_error(1, None, err_message)
