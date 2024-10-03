from sqlmodel import SQLModel, Field, Column, JSON, Relationship, Enum
from typing import Optional, List, Dict, Any
from uuid import UUID, uuid4
from datetime import datetime, timezone
from pydantic import UUID4
from uuid import uuid4
import enum


class WorkflowStatusEnum(str, enum.Enum):
    DRAFT = 'DRAFT'
    PUBLISHED = 'PUBLISHED'


class Timestamps:
    created_at: datetime = Field(default_factory=lambda: datetime.now(timezone.utc))
    updated_at: datetime = Field(default_factory=lambda: datetime.now(timezone.utc))


class UserWorkflowPermission(Timestamps, SQLModel, table=True):
    user_id: UUID | None = Field(default=None, foreign_key='user.id', primary_key=True)
    workflow_id: UUID | None = Field(default=None, foreign_key='workflow.id', primary_key=True)


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
    updated_workflows: List["Workflow"] = Relationship(back_populates='updater')  # type: ignore
    permitted_workflows: Optional["Workflow"] = Relationship(back_populates='permitted_users', link_model=UserWorkflowPermission)  # type: ignore


class WorkflowModel(SQLModel):
    id: Optional[UUID] = Field(default_factory=uuid4, primary_key=True)
    name: str = Field(default=None)
    title: str = Field(default=None)
    description: Optional[str] = Field(default=None)
    status: WorkflowStatusEnum = Field(sa_column=Column(Enum(WorkflowStatusEnum)), default=WorkflowStatusEnum.DRAFT)
    created_by: UUID = Field(foreign_key='user.id')
    updated_by: UUID = Field(foreign_key='user.id')

    class Config:
        arbitrary_types_allowed = True


class Workflow(Timestamps, WorkflowModel, table=True):
    intents: List["Intent"] = Relationship(back_populates='workflow')  # type:ignore
    creator: Optional["User"] = Relationship(back_populates="created_workflows")  # type:ignore
    updater: Optional["User"] = Relationship(back_populates="updated_workflows")  # type:ignore
    permitted_users: Optional["User"] = Relationship(back_populates="permitted_workflows", link_model=UserWorkflowPermission)  # type:ignore


class IntentModel(SQLModel):
    id: Optional[UUID] = Field(default_factory=uuid4, primary_key=True)
    name: str
    title: str
    description: Optional[str] = Field(default=None)
    nodes: Optional[List[Dict[str, Any]]] = Field(sa_column=Column(JSON), default=[])
    edges: Optional[List[Dict[str, Any]]] = Field(sa_column=Column(JSON), default=[])
    workflow_id: UUID = Field(foreign_key='workflow.id')

    class Config:
        arbitrary_types_allowed = True


class Intent(Timestamps, IntentModel, table=True):
    workflow: Optional["Workflow"] = Relationship(back_populates='intents')  # type: ignore
