from sqlmodel import SQLModel, Field
from uuid import UUID
from models.base_model import Timestamps


class UserWorkflowPermission(Timestamps, SQLModel, table=True):
    user_id: UUID = Field(foreign_key='user.id', primary_key=True)
    workflow_id: UUID = Field(foreign_key='workflow.id', primary_key=True)
