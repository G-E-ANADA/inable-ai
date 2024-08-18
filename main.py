from fastapi import FastAPI
from api.main import api_router
from core.config import settings
import os
from dotenv import load_dotenv
from pathlib import Path

app = FastAPI()

app = FastAPI(
    title=settings.PROJECT_NAME,
    openapi_url=f"{settings.API_V1_STR}/openapi.json",
)

project_root = Path(__file__).resolve().parent
load_dotenv(os.path.join(project_root, ".env"))

app.include_router(api_router, prefix=settings.API_V1_STR)