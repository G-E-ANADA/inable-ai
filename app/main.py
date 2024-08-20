from fastapi import FastAPI
from starlette.middleware.cors import CORSMiddleware

from app.api.main import api_router
from app.core.config import settings
import os
from dotenv import load_dotenv
from pathlib import Path

app = FastAPI()

app = FastAPI(
    title=settings.PROJECT_NAME,
    openapi_url=f"{settings.API_V1_STR}/openapi.json",
)

app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:1234"],  # 허용할 도메인 (React 앱이 실행되는 도메인)
    allow_credentials=True,
    allow_methods=["*"],  # 허용할 HTTP 메서드
    allow_headers=["*"],  # 허용할 HTTP 헤더
)

project_root = Path(__file__).resolve().parent
load_dotenv(os.path.join(project_root, ".env"))

app.include_router(api_router, prefix=settings.API_V1_STR)