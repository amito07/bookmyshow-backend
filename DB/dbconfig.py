import logging
from fastapi import FastAPI
from tortoise.contrib.fastapi import register_tortoise

from config import get_settings

log = logging.getLogger("uvicorn")

settings = get_settings()

DATABASE_URL = f"postgres://{settings.DB_USER}:{settings.DB_PASSWORD}@{settings.DB_HOST}:{settings.DB_PORT}/{settings.DB_NAME}?schema={settings.DB_SCHEMA}"

TORTOISE_MODELS = ["models.users.user", "aerich.models"]

"""
We need `TORTOISE_ORM` for `aerich`.
`aerich` is a database migrations tool for TortoiseORM, ready to production.
Details : https://github.com/tortoise/aerich
"""
TORTOISE_ORM = {
    "connections": {"default": DATABASE_URL},
    "apps": {
        "models": {
            "models": TORTOISE_MODELS,
            "default_connection": "default",
        },
    },
}


async def init_db(app: FastAPI) -> None:
    register_tortoise(
        app,
        db_url=DATABASE_URL,
        modules={"models": TORTOISE_MODELS},
        generate_schemas=True,
        add_exception_handlers=True
    )
