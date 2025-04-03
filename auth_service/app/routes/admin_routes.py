from fastapi import APIRouter,Request
from app.controllers.admin_auth_controller import login_admin
from app.config.db import get_db
from fastapi import Depends
from sqlalchemy.orm import Session
from app.schemas.request.auth_req import *

router =APIRouter()

@router.post('/login')
async def login(request:AdminLoginRequest,db:Session=Depends(get_db)):
    return await login_admin(request.email,request.password,db)