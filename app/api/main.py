from fastapi import APIRouter

from app.api.routes import test, chatlog

api_router = APIRouter()
api_router.include_router(test.router, prefix="/test", tags=["test"])
api_router.include_router(chatlog.router, prefix="/chatlog", tags=["chatlog"])