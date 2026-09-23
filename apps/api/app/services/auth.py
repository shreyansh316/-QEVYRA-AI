from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession

from app.core.security import create_access_token, hash_password, verify_password
from app.models.user import User
from app.schemas.auth import LoginRequest, RegisterRequest


class AuthenticationError(Exception):
    pass


async def register_user(
    session: AsyncSession,
    data: RegisterRequest,
) -> User:
    existing_user = await session.scalar(
        select(User).where(User.email == data.email)
    )

    if existing_user is not None:
        raise AuthenticationError("Email is already registered")

    user = User(
        email=data.email,
        password_hash=hash_password(data.password),
        full_name=data.full_name,
        is_active=True,
        is_verified=False,
    )

    session.add(user)
    await session.commit()
    await session.refresh(user)

    return user


async def authenticate_user(
    session: AsyncSession,
    data: LoginRequest,
) -> User:
    user = await session.scalar(
        select(User).where(User.email == data.email)
    )

    if user is None:
        raise AuthenticationError("Invalid email or password")

    if not verify_password(data.password, user.password_hash):
        raise AuthenticationError("Invalid email or password")

    if not user.is_active:
        raise AuthenticationError("User account is inactive")

    return user


def create_user_token(user: User) -> str:
    return create_access_token(str(user.id))
