from sqlmodel import SQLModel, Field, Enum, Column
from typing import Optional
from uuid import UUID, uuid4
from datetime import datetime, timezone
import enum


class WorkflowStatusEnum(str, enum.Enum):
    DRAFT = 'DRAFT'
    PUBLISHED = 'PUBLISHED'


class WorkflowModel(SQLModel):
    name: str = Field(default=None)
    title: str = Field(default=None)
    description: Optional[str] = Field(default=None)
    status: WorkflowStatusEnum = Field(sa_column=Column(Enum(WorkflowStatusEnum)), default=WorkflowStatusEnum.DRAFT)

    class Config:
        arbitrary_types_allowed = True


class Workflow(WorkflowModel, table=True):
    id: Optional[UUID] = Field(default_factory=uuid4, primary_key=True)
    created_at: datetime = Field(default_factory=lambda: datetime.now(timezone.utc))
    updated_at: datetime = Field(default_factory=lambda: datetime.now(timezone.utc))
