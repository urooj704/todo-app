"""Pydantic schemas for auth endpoints."""

from pydantic import BaseModel, EmailStr


class SignUpRequest(BaseModel):
    email: EmailStr
    password: str
    name: str | None = None


class SignInRequest(BaseModel):
    email: EmailStr
    password: str


class UserOut(BaseModel):
    id: str
    email: str
    name: str | None

    model_config = {"from_attributes": True}


class AuthResponse(BaseModel):
    user: UserOut
    accessToken: str
