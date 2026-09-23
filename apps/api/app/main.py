from fastapi import FastAPI

from app.core.config import settings


app = FastAPI(
    title=settings.app_name,
    version=settings.app_version,
    description="Backend API for the QEVYRA AI platform.",
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
    return {
        "status": "healthy",
        "service": "qevyra-api",
        "version": settings.app_version,
    }
