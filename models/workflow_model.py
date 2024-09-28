from sqlmodel import SQLModel, Field, Enum, Column, Relationship
from typing import Optional, List
from uuid import UUID, uuid4
from models.base_model import Timestamps
import enum


class WorkflowStatusEnum(str, enum.Enum):
    DRAFT = 'DRAFT'
    PUBLISHED = 'PUBLISHED'


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
