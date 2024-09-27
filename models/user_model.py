from sqlmodel import SQLModel, Field
from typing import Optional
from pydantic import UUID4
from uuid import uuid4
from datetime import datetime, timezone


class UserModel(SQLModel):
    first_name: str = Field(default=None)
    last_name: str = Field(default=None)
    email: str = Field(default=None)
    phone: str = Field(default=None)
    password: str = Field(default=None)


class User(UserModel, table=True):
    id: Optional[UUID4] = Field(default_factory=uuid4, primary_key=True)
    created_at: datetime = Field(default_factory=lambda: datetime.now(timezone.utc))
    updated_at: datetime = Field(default_factory=lambda: datetime.now(timezone.utc))
