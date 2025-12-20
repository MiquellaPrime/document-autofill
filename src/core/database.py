from collections.abc import AsyncGenerator
from typing import Any, Self

from sqlalchemy.ext.asyncio import AsyncSession, async_sessionmaker, create_async_engine

from src.core import settings


class DatabaseHelper:
    def __init__(self, url: str, **engine_kw: Any) -> None:
        self.engine = create_async_engine(url, **engine_kw)
        self.session_factory = async_sessionmaker(
            self.engine,
            autocommit=False,
            autoflush=False,
            expire_on_commit=False,
        )

    @classmethod
    def init_postgres(
        cls,
        url: str,
        echo: bool,
        max_overflow: int,
        pool_size: int,
        pool_pre_ping: bool,
        pool_recycle: int,
    ) -> Self:
        return cls(
            url,
            echo=echo,
            max_overflow=max_overflow,
            pool_size=pool_size,
            pool_pre_ping=pool_pre_ping,
            pool_recycle=pool_recycle,
        )

    async def dispose(self) -> None:
        await self.engine.dispose()

    async def session_getter(self) -> AsyncGenerator[AsyncSession]:
        async with self.session_factory() as session:
            yield session


db_helper = DatabaseHelper.init_postgres(
    url=settings.db.url,
    echo=settings.db.echo,
    max_overflow=settings.db.max_overflow,
    pool_size=settings.db.pool_size,
    pool_pre_ping=settings.db.pool_pre_ping,
    pool_recycle=settings.db.pool_recycle,
)
