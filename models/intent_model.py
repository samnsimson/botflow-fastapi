from sqlmodel import SQLModel, Field, Column, JSON
from typing import Optional, List, Dict, Any
from uuid import UUID, uuid4
from datetime import datetime, timezone


class IntentModel(SQLModel):
    name: str = Field(default=None)
    title: str = Field(default=None)
    description: Optional[str] = Field(default=None)
    nodes: Optional[List[Dict[str, Any]]] = Field(sa_column=Column(JSON), default=[])
    edges: Optional[List[Dict[str, Any]]] = Field(sa_column=Column(JSON), default=[])

    class Config:
        arbitrary_types_allowed = True


class Intent(IntentModel):
    id: Optional[UUID] = Field(default_factory=uuid4, primary_key=True)
    created_at: datetime = Field(default_factory=lambda: datetime.now(timezone.utc))
    updated_at: datetime = Field(default_factory=lambda: datetime.now(timezone.utc))
