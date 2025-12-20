from collections.abc import AsyncGenerator
from contextlib import asynccontextmanager

from fastapi import FastAPI

from core import db_helper


@asynccontextmanager
async def lifespan(app: FastAPI) -> AsyncGenerator[None]:
    yield
    await db_helper.dispose()


def create_app() -> FastAPI:
    app = FastAPI(lifespan=lifespan)
    return app
