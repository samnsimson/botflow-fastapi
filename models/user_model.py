from sqlmodel import SQLModel, Field
from typing import Optional
from pydantic import UUID4
from uuid import uuid4
from datetime import datetime, timezone


class User(SQLModel, table=True):
    id: Optional[UUID4] = Field(default_factory=uuid4, primary_key=True)
    first_name: str
    last_name: str
    email: str
    phone: str
    password: str
    created_at: datetime = Field(default_factory=lambda: datetime.now(timezone.utc))
