from fastapi import APIRouter,HTTPException,Request
from app.controllers.manager_auth_controller import register_manager,login_manager,send_otp,verify_otp
from app.config.db import get_db
from fastapi import Depends
from sqlalchemy.orm import Session
from app.schemas.request.auth_req import *
router =APIRouter()

@router.post('/register')
async def register(request:CommonRegisterRequest,db:Session=Depends(get_db)):
    return await register_manager(request.email,request.password,request.first_name,request.last_name,request.phone_number,db)

@router.post('/login')
async def login(request:CommonLoginRequest,db:Session=Depends(get_db)):
    return await login_manager(request.email,request.password,db)

@router.post('/send-otp')
async def login(request:CommonSendOtpRequest,db:Session=Depends(get_db)):
    return await send_otp(request.email,db)

@router.post('/verify-otp')
async def login(request:CommonVerifyOtpRequest,db:Session=Depends(get_db)):
    return await verify_otp(request.email,request.otp,db)