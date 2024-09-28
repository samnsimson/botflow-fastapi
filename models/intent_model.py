from sqlmodel import SQLModel, Field, Column, JSON, Relationship
from typing import Optional, List, Dict, Any
from uuid import UUID, uuid4
from models.base_model import Timestamps


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
