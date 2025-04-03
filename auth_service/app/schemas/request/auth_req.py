from pydantic import BaseModel

class CommonRegisterRequest(BaseModel):
    email: str
    password: str
    phone_number:str
    first_name: str
    last_name: str
    
class AdminLoginRequest(BaseModel):
    email: str
    password: str

class CommonLoginRequest(BaseModel):
    email: str
    password: str

class CommonSendOtpRequest(BaseModel):
    email: str

class CommonVerifyOtpRequest(BaseModel):
    email: str
    otp: int
