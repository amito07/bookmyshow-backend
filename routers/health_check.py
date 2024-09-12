import os
from fastapi.requests import Request
from fastapi import APIRouter, status
from config import get_settings

router = APIRouter(prefix="/health", tags=["health_check"])

@router.get("/", status_code=status.HTTP_200_OK)
async def health_check(request: Request):
    settings = get_settings()
    db_url = f"postgres://{settings.DB_USER}:{settings.DB_PASSWORD}@{settings.DB_HOST}:{settings.DB_PORT}/{settings.DB_NAME}?schema={settings.DB_SCHEMA}"
    return {"message": "Server health is ok", "db-connection": db_url}