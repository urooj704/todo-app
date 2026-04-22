"""Authentication endpoints: signup, signin, signout, session."""

import bcrypt
from fastapi import APIRouter, Depends, HTTPException, Request, status
from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession

from app.database import get_db
from app.models.user import User
from app.schemas.auth import SignUpRequest, SignInRequest, AuthResponse, UserOut
from app.auth.utils import create_token, verify_token

router = APIRouter(prefix="/auth", tags=["Auth"])


def _hash_password(password: str) -> str:
    return bcrypt.hashpw(password.encode(), bcrypt.gensalt()).decode()


def _verify_password(password: str, hashed: str) -> bool:
    return bcrypt.checkpw(password.encode(), hashed.encode())


@router.post("/signup", response_model=AuthResponse, status_code=status.HTTP_201_CREATED)
async def signup(body: SignUpRequest, db: AsyncSession = Depends(get_db)) -> AuthResponse:
    """Register a new user and return a JWT."""
    result = await db.execute(select(User).where(User.email == body.email))
    if result.scalar_one_or_none():
        raise HTTPException(status_code=status.HTTP_409_CONFLICT, detail="Email already registered")

    user = User(
        email=body.email,
        password_hash=_hash_password(body.password),
        name=body.name,
    )
    db.add(user)
    await db.commit()
    await db.refresh(user)

    token = create_token(user.id)
    return AuthResponse(user=UserOut.model_validate(user), accessToken=token)


@router.post("/signin", response_model=AuthResponse)
async def signin(body: SignInRequest, db: AsyncSession = Depends(get_db)) -> AuthResponse:
    """Authenticate a user and return a JWT."""
    result = await db.execute(select(User).where(User.email == body.email))
    user = result.scalar_one_or_none()

    if not user or not _verify_password(body.password, user.password_hash):
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Invalid email or password",
        )

    token = create_token(user.id)
    return AuthResponse(user=UserOut.model_validate(user), accessToken=token)


@router.post("/signout", status_code=status.HTTP_200_OK)
async def signout() -> dict:
    """Sign out — JWTs are stateless; client must discard the token."""
    return {"message": "Signed out"}


@router.get("/session", response_model=AuthResponse)
async def session(request: Request, db: AsyncSession = Depends(get_db)) -> AuthResponse:
    """Validate Bearer token and return the current user."""
    auth_header = request.headers.get("Authorization", "")
    if not auth_header.startswith("Bearer "):
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail="Missing token")

    token = auth_header.removeprefix("Bearer ").strip()
    try:
        user_id = verify_token(token)
    except Exception as e:
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail=str(e))

    result = await db.execute(select(User).where(User.id == user_id))
    user = result.scalar_one_or_none()
    if not user:
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail="User not found")

    return AuthResponse(user=UserOut.model_validate(user), accessToken=token)
