from core.settings import settings
from sqlalchemy.ext.asyncio import create_async_engine,async_sessionmaker
from sqlalchemy.orm import DeclarativeBase

url=settings.db_url
engine=create_async_engine(url,echo=True)

async_session=async_sessionmaker(engine,expire_on_commit=False)


async def get_db():
    async with async_session() as session:
        yield session


class Base(DeclarativeBase):
    pass

async def create_tables():
    async with engine.begin() as conn:
        await conn.run_sync(Base.metadata.create_all)
