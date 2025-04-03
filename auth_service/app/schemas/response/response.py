from fastapi import HTTPException
from fastapi.responses import JSONResponse
from typing import Optional, Any

def success_response(code: int, message:str,data: Optional[Any] = None):
    return JSONResponse(
        status_code=200,
        content={
            "code": code,
            "message":message,
            "data": data
        }
    )

def server_error(code: int, data: Optional[Any] = None, err: Optional[Any] = None):
    return JSONResponse(
        status_code=500,
        content={
            "code": code,
            "message": "Somethingwent Wrong!",
            "data": data,
            "err": err
        }
    )

def bad_request(code: int, message: str = "Bad Request",data: Optional[Any] = None,err:Optional[Any] = None):
    return JSONResponse(
        status_code=400,
        content={
            "code": code,
            "message":message,
            "data": data,
            "err": err
        }
    )

def not_found(code:int,message:str,data:Optional[Any] =None,err:Optional[Any] =None):
    return JSONResponse(
        status_code=404,
        content={
            "code": code,
            "message":message,
            "data":data,
            "err":err
        })


def validation_error(code:int,message:str,data:Optional[Any] =None,err:Optional[Any] =None):
    return JSONResponse(
        status_code=422,
        content={
            "code":code,
            "message":message,
            "data":data,
            "err":err
        }
    )

def fail_conflict(code:int,message:str,data:Optional[Any] =None,err:Optional[Any] =None):
    return JSONResponse(
        status_code=409,
        content={
            "code":code,
            "message":message,
            "data":data,
            "err":err
        }
    )

def forbidden(code:int,message:str,data:Optional[Any] =None,err:Optional[Any] =None):
    return JSONResponse(
        status_code=403,
        content={
            "code":code,
            "message":message,
            "data":data,
            "err":err
        }
    )

def request_timeout(code:int,message:str,data:Optional[Any] =None,err:Optional[Any] =None):
    return JSONResponse(
        status_code=408,
        content={
            "code":code,
            "message":message,
            "data":data,
            "err":err
        }
    )

def fail_authorization(code:int,message:str,data:Optional[Any] =None,err:Optional[Any] =None):
    return JSONResponse(
        status_code=401,
        content={
            "code":code,
            "message":message,
            "data":data,
            "err":err
        }
    )