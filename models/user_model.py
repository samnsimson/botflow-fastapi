from sqlmodel import SQLModel, Field, Relationship
from typing import Optional, List
from pydantic import UUID4
from uuid import uuid4
from models.base_model import Timestamps


class UserModel(SQLModel):
    id: Optional[UUID4] = Field(default_factory=uuid4, primary_key=True)
    first_name: str = Field(default=None)
    last_name: str = Field(default=None)
    email: str = Field(default=None)
    phone: str = Field(default=None)
    password: str = Field(default=None)
    email_verified: bool = Field(default=False)
    phone_verified: bool = Field(default=False)


class User(Timestamps, UserModel, table=True):
    created_workflows: List["Workflow"] = Relationship(back_populates='creator')  # type: ignore
    updated_workflows: List["Workflow"] = Relationship(back_populates='updator')  # type: ignore
