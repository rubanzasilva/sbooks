

from sqlalchemy.ext.asyncio import create_async_engine, async_sessionmaker

from sqlmodel.ext.asyncio.session import AsyncSession

from app.core.config import settings



engine = create_async_engine(settings.DATABASE_URL)

async_session = async_sessionmaker(engine, class_=AsyncSession, expire_on_commit=False)



async def get_session():

    async with async_session() as session:

        yield session


