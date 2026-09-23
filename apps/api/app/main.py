from contextlib import asynccontextmanager

from fastapi import FastAPI
from sqlalchemy import text

from app.core.config import settings
from app.db.database import AsyncSessionLocal, close_database
from app.db.redis import close_redis, redis_client


@asynccontextmanager
async def lifespan(app: FastAPI):
    yield

    await close_redis()
    await close_database()


app = FastAPI(
    title=settings.app_name,
    version=settings.app_version,
    description="Backend API for the QEVYRA AI platform.",
    lifespan=lifespan,
)


@app.get("/")
async def root():
    return {
        "name": settings.app_name,
        "status": "online",
        "version": settings.app_version,
        "environment": settings.environment,
    }


@app.get("/api/health")
async def health():
    postgres_status = "healthy"
    redis_status = "healthy"

    try:
        async with AsyncSessionLocal() as session:
            await session.execute(text("SELECT 1"))
    except Exception:
        postgres_status = "unhealthy"

    try:
        await redis_client.ping()
    except Exception:
        redis_status = "unhealthy"

    overall_status = (
        "healthy"
        if postgres_status == "healthy" and redis_status == "healthy"
        else "degraded"
    )

    return {
        "status": overall_status,
        "service": "qevyra-api",
        "version": settings.app_version,
        "dependencies": {
            "postgresql": postgres_status,
            "redis": redis_status,
        },
    }
