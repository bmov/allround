from contextlib import asynccontextmanager
from sqlalchemy.ext.asyncio import (
    AsyncSession, create_async_engine, async_sessionmaker
)

from .environment import env

database_uri = env['SQL_DATABASE_URI']
database_logging = False

if env['ALLROUND_MODE'] == 'dev':
    database_logging = True

engine = create_async_engine(database_uri, echo=database_logging)
async_session_local = async_sessionmaker(
    engine, expire_on_commit=False, class_=AsyncSession)


@asynccontextmanager
async def async_session():
    session = async_session_local()
    try:
        yield session
    finally:
        await session.close()
