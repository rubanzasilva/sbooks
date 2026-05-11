
from contextlib import asynccontextmanager
from fastapi import FastAPI
from sqlalchemy import text
from app.database import engine, async_session

@asynccontextmanager
async def lifespan(app:FastAPI):
    async with async_session() as session:
        await session.execute(text("SELECT 1"))
    yield
    await engine.dispose()

app = FastAPI(lifespan=lifespan)


