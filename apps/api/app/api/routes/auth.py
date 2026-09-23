from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.ext.asyncio import AsyncSession

from app.api.dependencies import get_current_user
from app.db.database import get_db
from app.models.user import User
from app.schemas.auth import (
    AuthResponse,
    LoginRequest,
    RegisterRequest,
    UserResponse,
)
from app.services.auth import (
    AuthenticationError,
    authenticate_user,
    create_user_token,
    register_user,
)


router = APIRouter(
    prefix="/api/auth",
    tags=["Authentication"],
)


@router.post(
    "/register",
    response_model=AuthResponse,
    status_code=status.HTTP_201_CREATED,
)
async def register(
    data: RegisterRequest,
    session: AsyncSession = Depends(get_db),
):
    try:
        user = await register_user(session, data)
    except AuthenticationError as exc:
        raise HTTPException(
            status_code=status.HTTP_409_CONFLICT,
            detail=str(exc),
        ) from exc

    return AuthResponse(
        access_token=create_user_token(user),
        user=UserResponse.model_validate(user),
    )


@router.post(
    "/login",
    response_model=AuthResponse,
)
async def login(
    data: LoginRequest,
    session: AsyncSession = Depends(get_db),
):
    try:
        user = await authenticate_user(session, data)
    except AuthenticationError as exc:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail=str(exc),
            headers={"WWW-Authenticate": "Bearer"},
        ) from exc

    return AuthResponse(
        access_token=create_user_token(user),
        user=UserResponse.model_validate(user),
    )


@router.get(
    "/me",
    response_model=UserResponse,
)
async def get_me(
    current_user: User = Depends(get_current_user),
):
    return UserResponse.model_validate(current_user)
