from fastapi import APIRouter
from .admin_routes import router as admin_router
# from .manager_routes import router as manager_router
from .employee_routes import router as employee_router

router =APIRouter()

router.include_router(admin_router,prefix='/admin')
# router.include_router(manager_router,prefi='/manager')
router.include_router(employee_router,prefix='/employee')